#!/usr/bin/env python3
"""Widen the cramped teeth of the seen/sheen family in the UFO.

The seen/sheen letters merged from No Name Fixed have their tooth cluster
scrunched into a narrow band with a large empty bowl, which reads poorly
(see google/fonts#6491). This applies a position-aware horizontal scale to the
teeth so they fill the cell, while keeping the joining strokes pinned to the
cell edge so Arabic connections still line up:

  isolated / final : anchor at the RIGHT (xMax) and scale left. The right side
                     is the word-start / the join to the previous letter, so it
                     stays put; the non-connecting terminal tail extends left.
  initial          : anchor at the LEFT join (xMin) and scale right, so the
                     teeth grow into the empty right gap while the left join
                     stays put.
  medial           : both edges are joins (pinned), so it is left unchanged.

Only the seen/sheen *teeth* family is touched; the sad/dad loop letters have a
different structure and are not scrunched. The transform scales every contour
of each glyph, so the dots of the dotted variants move with the teeth.

Usage: python3 scripts/widen-seen-family.py [--scale 1.5] [--apply] [--ufo PATH]
Without --apply it reports what it would do. Idempotent per run only in the
sense that re-running scales again — run once from pristine glyphs.
"""
import argparse
import json
import os
import re
import unicodedata as ud

# seen/sheen teeth family (NOT the sad/dad loop letters).
FAMILY = [0x0633, 0x0634, 0x069A, 0x069B, 0x069C, 0x06FA, 0x0770, 0x077D, 0x077E]
POS_TAGS = {"initial": "init", "medial": "medi", "final": "fina"}


def load(ufo):
    import plistlib
    gdir = os.path.join(ufo, "glyphs")
    contents = plistlib.load(open(os.path.join(gdir, "contents.plist"), "rb"))
    cp2name = {}
    for n, fn in contents.items():
        for m in re.findall(r'<unicode hex="([0-9A-Fa-f]+)"', open(os.path.join(gdir, fn)).read()):
            cp2name.setdefault(int(m, 16), n)
    return gdir, contents, cp2name


def form_positions():
    """(base_cp, pos) -> presentation-form cp, from the Unicode database."""
    out = {}
    for cp in list(range(0xFB50, 0xFE00)) + list(range(0xFE70, 0xFF00)):
        d = ud.decomposition(chr(cp))
        if d.startswith("<"):
            tag = d[1:d.index(">")]
            if tag in POS_TAGS:
                comps = d[d.index(">") + 1:].split()
                if len(comps) == 1:
                    out.setdefault((int(comps[0], 16), POS_TAGS[tag]), cp)
    return out


def plan_glyphs(contents, cp2name):
    fp = form_positions()
    plan = []
    for bcp in FAMILY:
        isol = cp2name.get(bcp)
        if isol:
            plan.append((isol, "isol"))
        for pos in ("init", "medi", "fina"):
            fcp = fp.get((bcp, pos))
            g = None
            if fcp and cp2name.get(fcp):
                g = cp2name[fcp]
            elif fcp and ("uni%04X" % fcp) in contents:
                g = "uni%04X" % fcp
            if not g and isol and f"{isol}.{pos}" in contents:
                g = f"{isol}.{pos}"
            if g:
                plan.append((g, pos))
    return plan


def transform_glyph(path, pos, scale):
    d = open(path, encoding="utf-8").read()
    xs = [float(x) for x, y in re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', d)]
    if not xs:
        return False
    if pos in ("isol", "fina"):
        anchor = max(xs)  # right side (join for final / word-start) stays put
        fn = lambda x: anchor - (anchor - x) * scale
    elif pos == "init":
        anchor = min(xs)  # left join stays put
        fn = lambda x: anchor + (x - anchor) * scale
    else:  # medi: both edges pinned, leave unchanged
        return False

    def repl(m):
        return f'{m.group(1)}{fn(float(m.group(2))):.0f}'

    new = re.sub(r'(<point x=")(-?[0-9.]+)', repl, d)  # only <point x>, never hex
    open(path, "w", encoding="utf-8").write(new)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--scale", type=float, default=1.5)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    gdir, contents, cp2name = load(args.ufo)
    plan = plan_glyphs(contents, cp2name)
    done = 0
    for name, pos in plan:
        if pos == "medi":
            print(f"  skip  {name:16} (medial: both edges pinned)")
            continue
        if args.apply:
            if transform_glyph(os.path.join(gdir, contents[name]), pos, args.scale):
                done += 1
        print(f"  {'widen' if args.apply else 'would':5} {name:16} {pos} x{args.scale}")
    print(f"{'Applied' if args.apply else 'Planned'}: {done if args.apply else len([p for p in plan if p[1] != 'medi'])} glyphs (medial left unchanged)")


if __name__ == "__main__":
    main()
