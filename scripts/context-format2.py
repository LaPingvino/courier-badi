#!/usr/bin/env python3
"""Merge runs of format-3 contextual subtables into format-2 ones.

Post-build, for the speed of shaping. fontTools (feaLib) writes a
contextual lookup as format 3, one subtable per rule, whenever that is
smallest, and it is for rules of single glyphs and small classes: the
Lekhan monospace lookups (scripts/fit-devanagari.py) came out as 1453
subtables for LekSum and LekSum2 each, 72 for LekReset. A shaper tries a
lookup's subtables one after another at every glyph, so HarfBuzz and
go-text (Lexington, Accolade) went through all of them for every counter
mark: Devanagari shaped several times slower than before 1.105.

A run of consecutive format-3 subtables of a (chain) context lookup is
written as one format-2 subtable that means the same: the glyph sets each
position uses are split into classes (glyphs in the same sets share one),
a rule whose set is several classes is repeated for each (they cannot both
match), the rules kept in their order within each class set, their lookup
records as they were. A shaper tries the first rule that matches, as it
tried the first subtable that matched, so the result is the same. Runs
whose rules would be repeated too often are cut into several subtables.

Usage: python3 scripts/context-format2.py FONT...
"""
import itertools
import sys

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables as ot

MAX_COPIES = 64          # a rule repeated at most this often (its classes' product)
MAX_RULES = 20000        # rules in one merged subtable


def unwrap(lookup):
    """(the subtables, the real lookup type, extension-wrapped)"""
    ext = {"GSUB": 7, "GPOS": 9}
    subs = lookup.SubTable
    t = lookup.LookupType
    if subs and hasattr(subs[0], "ExtSubTable"):
        return [s.ExtSubTable for s in subs], subs[0].ExtensionLookupType, True
    return subs, t, False


class Kind:
    def __init__(self, tag, chain):
        self.tag, self.chain = tag, chain
        sp = "Subst" if tag == "GSUB" else "Pos"
        rs = "Sub" if tag == "GSUB" else "Pos"     # (fontTools' names of the class sets and rules)
        self.rec = f"{sp}LookupRecord"
        self.count = f"{sp}Count"
        if chain:
            self.cls = getattr(ot, f"ChainContext{sp}")
            self.set_attr, self.rule_attr = f"Chain{rs}ClassSet", f"Chain{rs}ClassRule"
        else:
            self.cls = getattr(ot, f"Context{sp}")
            self.set_attr, self.rule_attr = f"{rs}ClassSet", f"{rs}ClassRule"
        self.set_, self.rule = getattr(ot, self.set_attr), getattr(ot, self.rule_attr)


def roles(st, chain):
    """the subtable's glyph sets: backtrack (nearest first), input, lookahead"""
    if chain:
        return ([frozenset(c.glyphs) for c in st.BacktrackCoverage],
                [frozenset(c.glyphs) for c in st.InputCoverage],
                [frozenset(c.glyphs) for c in st.LookAheadCoverage])
    return [], [frozenset(c.glyphs) for c in st.Coverage], []


def partition(sets):
    """classes (1, 2, ...) for the glyphs of the sets, each set a union of
    classes: glyph -> class, set -> its classes"""
    sig = {}
    for i, s in enumerate(sets):
        for g in s:
            sig.setdefault(g, []).append(i)
    blocks = {}
    for g, k in sig.items():
        blocks.setdefault(tuple(k), []).append(g)
    order = sorted(blocks, key=lambda k: (k, min(blocks[k])))
    cls = {}
    for n, k in enumerate(order, 1):
        for g in blocks[k]:
            cls[g] = n
    of = {}
    for s in set(sets):
        of[s] = sorted({cls[g] for g in s})
    return cls, of


def copies(rules, part):
    n = 0
    for r in rules:
        m = 1
        for role, sets in enumerate(r[:3]):
            for s in sets:
                m *= len(part[role][1][s])
        n += m
        if m > MAX_COPIES:
            return None
    return n


def parts(rules):
    return [partition([s for r in rules for s in r[role]]) for role in range(3)]


def build(kind, rules, font):
    part = parts(rules)
    st = kind.cls()
    st.Format = 2
    (bcls, bof), (icls, iof), (lcls, lof) = part
    first = set()
    for r in rules:
        first |= r[1][0]
    st.Coverage = ot.Coverage()
    st.Coverage.glyphs = sorted(first, key=font.getGlyphID)
    nin = max(icls.values()) + 1

    def classdef(m):
        cd = ot.ClassDef()
        cd.classDefs = dict(m)
        return cd

    if kind.chain:
        st.BacktrackClassDef, st.InputClassDef, st.LookAheadClassDef = classdef(bcls), classdef(icls), classdef(lcls)
    else:
        st.ClassDef = classdef(icls)
    sets = [[] for _ in range(nin)]
    for back, inp, ahead, recs in rules:
        choices = [bof[s] for s in back] + [iof[s] for s in inp] + [lof[s] for s in ahead]
        for combo in itertools.product(*choices):
            b = list(combo[:len(back)])
            i = list(combo[len(back):len(back) + len(inp)])
            a = list(combo[len(back) + len(inp):])
            rule = kind.rule()
            if kind.chain:
                rule.BacktrackGlyphCount, rule.Backtrack = len(b), b
                rule.InputGlyphCount, rule.Input = len(i), i[1:]
                rule.LookAheadGlyphCount, rule.LookAhead = len(a), a
            else:
                rule.GlyphCount, rule.Class = len(i), i[1:]
            setattr(rule, kind.count, len(recs))
            setattr(rule, kind.rec, recs)
            sets[i[0]].append(rule)
    out = []
    for rs in sets:
        if not rs:
            out.append(None)
            continue
        cs = kind.set_()
        setattr(cs, kind.rule_attr, rs)
        setattr(cs, kind.rule_attr + "Count", len(rs))
        out.append(cs)
    setattr(st, kind.set_attr, out)
    setattr(st, kind.set_attr + "Count", len(out))
    return st


def merge_run(kind, subs, font):
    """the run's subtables as few format-2 ones as the limits allow"""
    out, group = [], []

    def close():
        if len(group) == 1:
            out.append(group[0][1])
        elif group:
            out.append(build(kind, [r for r, _ in group], font))

    for st in subs:
        r = (*roles(st, kind.chain), list(getattr(st, kind.rec)))
        trial = [g for g, _ in group] + [r]
        n = copies(trial, parts(trial))
        if n is None or n > MAX_RULES:
            close()
            group = []
            if copies([r], parts([r])) is None:      # too many copies alone: kept as it is
                out.append(st)
                continue
        group.append((r, st))
    close()
    return out


def merge(font, tag):
    if tag not in font:
        return 0, 0
    table = font[tag].table
    if not table.LookupList:
        return 0, 0
    before = after = 0
    ctx = {"GSUB": (5, 6), "GPOS": (7, 8)}[tag]
    for lookup in table.LookupList.Lookup:
        subs, t, ext = unwrap(lookup)
        if t not in ctx:
            continue
        kind = Kind(tag, t == ctx[1])
        new, run = [], []
        for st in subs:
            if st.Format == 3:
                run.append(st)
                continue
            if len(run) > 1:
                new += merge_run(kind, run, font)
            else:
                new += run
            run = []
            new.append(st)
        new += merge_run(kind, run, font) if len(run) > 1 else run
        before += len(subs)
        after += len(new)
        if len(new) == len(subs):
            continue
        if ext:
            wrapped = []
            for st in new:
                e = (ot.ExtensionSubst if tag == "GSUB" else ot.ExtensionPos)()
                e.Format, e.ExtensionLookupType, e.ExtSubTable = 1, t, st
                wrapped.append(e)
            new = wrapped
        lookup.SubTable = new
        lookup.SubTableCount = len(new)
    return before, after


def main():
    for path in sys.argv[1:]:
        font = TTFont(path)
        res = {tag: merge(font, tag) for tag in ("GSUB", "GPOS")}
        font.save(path)
        print(f"{path}: contextual subtables " + ", ".join(f"{t} {b} -> {a}" for t, (b, a) in res.items()))


if __name__ == "__main__":
    main()
