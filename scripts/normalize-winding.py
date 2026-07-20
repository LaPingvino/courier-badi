#!/usr/bin/env python3
"""Normalize contour winding (and overlaps) in a UFO via skia-pathops.

The Latin was digitized with the PostScript convention (outer CCW, holes CW),
but the merged Cyrillic/Greek/Arabic came in with the whole glyph -- or, worse,
only *parts* of a glyph (e.g. a Vietnamese base backwards while its accents were
correct) -- wound the other way. Inconsistent winding breaks anything that
offsets along the normal, most visibly the emboldening in make-bold.py, which
then thinned those contours instead of thickening them.

Rather than guess per contour, this resolves the actual filled region of each
glyph with skia-pathops and rewrites it: `simplify()` returns a canonical,
non-self-intersecting outline with consistent winding (outer CCW, holes CW).
Overlaps are merged in the process, which the build does anyway. Components are
left untouched (they inherit from their normalized base glyphs).

Usage: python3 scripts/normalize-winding.py [--ufo sources/CourierBadi-Regular.ufo]
"""
import argparse

import pathops
import ufoLib2
from fontTools.pens.qu2cuPen import Qu2CuPen


def normalize(ufo):
    font = ufoLib2.Font.open(ufo)
    changed = 0
    for glyph in font:
        if not glyph.contours:
            continue
        path = pathops.Path()
        pen = path.getPen()
        for contour in glyph.contours:
            contour.draw(pen)
        path.simplify()
        glyph.contours.clear()
        # skia-pathops can emit quadratics/conics; convert back to cubics so the
        # (cubic) UFO and the OTF build stay happy.
        path.draw(Qu2CuPen(glyph.getPen(), max_err=0.5, all_cubic=True))
        changed += 1
    font.save()
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    args = ap.parse_args()
    n = normalize(args.ufo)
    print(f"{args.ufo}: normalized winding/overlaps on {n} glyphs")


if __name__ == "__main__":
    main()
