#!/usr/bin/env python3
"""Generate mark-attachment anchors that reproduce HarfBuzz's fallback mark
positioning, for every script except Hebrew (which has its own anchors, see
scripts/import-hebrew.py).

Why: until the Hebrew, Courier Badi had no GPOS. Its zero-width combining
marks (Latin, Greek, Cyrillic, Arabic) were placed by the shaper's *fallback*
mark positioning, which HarfBuzz applies only to fonts without a GPOS table.
The Hebrew needs real mark positioning (GPOS mark/mkmk), and the moment the
font has a GPOS, HarfBuzz switches the fallback off for every script -- so the
other scripts' marks would collapse onto the next cell. This script writes the
fallback down as anchors, so the GPOS puts those marks where the fallback did
(and now also in shapers that never had a fallback).

The fallback (hb-ot-shape-fallback.cc, position_mark), with gap = UPM/16:
  - x: the mark's ink is centred on the base's *advance* (not its ink);
    "right" classes align the mark's right ink edge to the advance;
  - above: the mark's ink bottom goes `gap` above the base's ink top -- but a
    mark that would have to move DOWN moves only half way;
  - below: the mark's ink top goes `gap` under the base's ink bottom -- but a
    mark is never moved UP (it stays where it is drawn);
  - attached classes: the same without the gap;
  - stacked marks: the next mark goes `gap` beyond the previous mark's ink.

The clamps make the offset depend on the base's ink edge AND the mark's drawn
edge, which one anchor pair cannot express. So the marks of each class are
grouped by their drawn edge (within TOL units; the Arabic marks are drawn at
many heights), each group gets its own anchor name (`aboveArab3`, ...), and
each base's anchor for a group has the clamp folded in for that group's edge:
    above: E + d      if d >= 0, else E + d/2   (d = base top + gap - E)
    below: min(base bottom - gap, E)
with E the group's mean edge. The groups are made once, on the Regular, and
the same membership is used in every master (so the masters stay
interpolation-compatible); E and the base edges are measured per master, as
the fallback measured each instance.

Groups are per script family: Arabic marks on Arabic bases (encoded Arabic and
the presentation/positional forms), Latin/Greek/Cyrillic marks on everything
else; the dotted circle gets both. A mark on a base of the other family gets
no positioning.

Combining classes come from the Unicode database, with HarfBuzz's Arabic
re-categorisation (fathatan..sukun, superscript alef: above; kasratan, kasra:
below). Classes HarfBuzz does not position (0, overlay) get no anchor.
scripts/check-mark-parity.py measures the result against the fallback.

The script owns only the anchor names it generates and is idempotent.

Usage: python3 scripts/make-mark-anchors.py [--ref sources/CourierBadi-Regular.ufo] \
           sources/CourierBadi-*.ufo
"""
import argparse
import re
import unicodedata as ud

import ufoLib2
from fontTools.pens.boundsPen import BoundsPen

GAP = 128  # UPM / 16
TOL = 40   # marks whose drawn edge differs by up to this share a group

# class -> (horizontal alignment, side, gap)
CLASSES = {
    "above": ("centre", "top", GAP),
    "below": ("centre", "bottom", GAP),
    "attachedBelow": ("centre", "bottom", 0),
    "attachedAboveRight": ("right", "top", 0),
}
CCC = {230: "above", 220: "below", 202: "attachedBelow", 216: "attachedAboveRight"}
# HarfBuzz's modified classes for Arabic (recategorize_combining_class)
ARABIC_ABOVE = {27, 28, 30, 31, 33, 34, 35, 36}
ARABIC_BELOW = {29, 32}
STACKING = {"above", "below"}

OWNED = re.compile(r"^_?(%s)(LGC|Arab)?\d*$" % "|".join(CLASSES))
ARABIC_RANGES = [(0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
                 (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)]


def is_hebrew(cp):
    return 0x0591 <= cp <= 0x05C7 or cp == 0xFB1E


def is_arabic_cp(cp):
    return any(a <= cp <= b for a, b in ARABIC_RANGES)


def mark_class(cp):
    ch = chr(cp)
    if ud.category(ch) not in ("Mn", "Me") or is_hebrew(cp) or 0xFE70 <= cp <= 0xFE7F:
        return None
    c = ud.combining(ch)
    if c in ARABIC_ABOVE:
        return "above"
    if c in ARABIC_BELOW:
        return "below"
    return CCC.get(c)


def family_of_glyph(g):
    """'Arab' for Arabic letters and their (possibly unencoded) forms."""
    if g.unicodes:
        return "Arab" if any(is_arabic_cp(c) for c in g.unicodes) else "LGC"
    base = g.name.split(".")[0]
    m = re.match(r"uni([0-9A-F]{4})", base)
    if m and is_arabic_cp(int(m.group(1), 16)):
        return "Arab"
    if base.endswith("_ar") or "-ar" in base or base.endswith("ar") and "_" in base:
        return "Arab"
    return "LGC"


def bounds(font, g):
    bp = BoundsPen(font)
    g.draw(bp)
    return bp.bounds


def edge(cls, b):
    return b[1] if CLASSES[cls][1] == "top" else b[3]


def mark_table(font):
    """glyph name -> (class, family) for the positioned marks."""
    out = {}
    for g in font:
        for cp in g.unicodes:
            cls = mark_class(cp)
            if cls:
                out[g.name] = (cls, "Arab" if 0x0600 <= cp <= 0x08FF else "LGC")
    return out


def make_groups(ref):
    """{(class, family): [[mark names], ...]} from the reference master."""
    font = ufoLib2.Font.open(ref)
    marks = mark_table(font)
    items = {}
    for name, key in marks.items():
        b = bounds(font, font[name])
        if b:
            items.setdefault(key, []).append((edge(key[0], b), name))
    groups = {}
    for key, lst in sorted(items.items()):
        lst.sort()
        gs = []
        for e, n in lst:
            if gs and e - gs[-1][0][0] <= TOL:
                gs[-1].append((e, n))
            else:
                gs.append([(e, n)])
        groups[key] = [[n for _, n in g] for g in gs]
    return groups


def anchor_name(cls, fam, i):
    return f"{cls}{fam}{i}"


def run(path, groups):
    font = ufoLib2.Font.open(path)
    marks = mark_table(font)
    all_marks = {g.name for g in font
                 if any(ud.category(chr(c)) in ("Mn", "Me") for c in g.unicodes)}
    # this master's mean edge per group
    E = {}
    member = {}
    for (cls, fam), gs in groups.items():
        for i, names in enumerate(gs):
            es = []
            for n in names:
                b = bounds(font, font[n]) if n in font else None
                if b:
                    es.append(edge(cls, b))
                    member[n] = (cls, fam, i)
            if es:
                E[(cls, fam, i)] = sum(es) / len(es)

    def targets(cls, fam, top, bottom, width):
        """anchors (name, x, y) a base/carrier offers to every group of cls."""
        halign, side, gap = CLASSES[cls]
        x = width if halign == "right" else width / 2
        out = []
        for i in range(len(groups.get((cls, fam), []))):
            e = E.get((cls, fam, i))
            if e is None:
                continue
            if side == "top":
                d = top + gap - e
                y = e + (d if d >= 0 else d / 2)
            else:
                y = min(bottom - gap, e)
            out.append((anchor_name(cls, fam, i), x, y))
        return out

    nb = nm = 0
    for g in font:
        keep = [a for a in g.anchors if not OWNED.match(a.name)]
        if len(keep) != len(g.anchors):
            g.anchors.clear()
            for a in keep:
                g.appendAnchor({"name": a.name, "x": a.x, "y": a.y})
        b = bounds(font, g)
        if b is None:
            continue
        x0, y0, x1, y1 = b
        new = []
        if g.name in member:
            cls, fam, i = member[g.name]
            halign, side, gap = CLASSES[cls]
            ax = x1 if halign == "right" else (x0 + x1) / 2
            new.append(("_" + anchor_name(cls, fam, i), ax, edge(cls, b)))
            if cls in STACKING:
                # the next mark stacks on this one's ink, centred on its ink
                for n, _, y in targets(cls, fam, y1, y0, 0):
                    new.append((n, (x0 + x1) / 2, y))
            nm += 1
        elif g.name not in all_marks and g.width > 0:
            # the dotted circle (U+25CC) carries marks of every script
            fams = {"LGC", "Arab"} if 0x25CC in g.unicodes else {family_of_glyph(g)}
            for (cls, f) in groups:
                if f in fams:
                    new += targets(cls, f, y1, y0, g.width)
            nb += 1
        for n, x, y in new:
            g.appendAnchor({"name": n, "x": round(x), "y": round(y)})
    font.save()
    ng = sum(len(v) for v in groups.values())
    print(f"{path}: anchors for {nb} bases and {nm} marks in {ng} groups")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("ufos", nargs="+")
    args = ap.parse_args()
    groups = make_groups(args.ref)
    for (cls, fam), gs in groups.items():
        print(f"  {cls}/{fam}: {len(gs)} groups")
    for p in args.ufos:
        run(p, groups)


if __name__ == "__main__":
    main()
