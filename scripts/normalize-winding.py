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

# Glyphs deliberately excluded from simplification. `f` has an interpolation
# partner -- the descending italic form in sources/italic-overrides/ -- that
# shares its (two-contour) point structure. simplify() would merge its overlaps
# into a single contour, breaking that compatibility. Its winding was already
# correct (it is native Latin, outer CCW), so it needs no normalization.
SKIP = {"f"}


def normalize(ufo, only=None):
    font = ufoLib2.Font.open(ufo)
    changed = 0
    for glyph in font:
        if not glyph.contours or glyph.name in SKIP:
            continue
        if only is not None and glyph.name not in only:
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
    ap.add_argument("--glyphs", default=None,
                    help="comma-separated glyph names to normalize (default: all)")
    args = ap.parse_args()
    only = set(args.glyphs.split(",")) if args.glyphs else None
    n = normalize(args.ufo, only)
    print(f"{args.ufo}: normalized winding/overlaps on {n} glyphs")


if __name__ == "__main__":
    main()
