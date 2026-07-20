#!/usr/bin/env python3
"""Generate a Bold UFO from the Regular by dilating the outlines (emboldening).

The idea (spotted from the seen/sad widening): growing the black while the
counters stay put thickens the stroke. Done uniformly this is a classic
emboldening -- every outline point is offset OUTWARD along its normal by
`weight` units, which grows the filled area and shrinks the counters, so stems
get heavier while the advance width (and thus the monospace) is unchanged.

This becomes the second master of the weight axis: Regular (offset 0) and Bold
(offset `weight`) interpolate to any weight in between.

Usage:
  python3 scripts/make-bold.py [--weight 34] \
      [--src sources/CourierBadi-Regular.ufo] [--out sources/CourierBadi-Bold.ufo]
"""
import argparse
import math

import ufoLib2


def dilate_contour(contour, delta):
    pts = list(contour)
    n = len(pts)
    if n < 3:
        return
    # Offset every point along the right-hand normal of its travel direction.
    # With PostScript winding (outer CCW, holes CW) this grows the outer contour
    # and shrinks the counters -- i.e. thickens the stroke -- for both straight
    # stems and curved bowls, without needing a winding sign.
    orig = [(p.x, p.y) for p in pts]
    for i in range(n):
        px, py = orig[(i - 1) % n]
        nx, ny = orig[(i + 1) % n]
        tx, ty = nx - px, ny - py
        L = math.hypot(tx, ty) or 1.0
        pts[i].x += delta * (ty / L)
        pts[i].y += delta * (-tx / L)


def make_bold(src, out, weight):
    font = ufoLib2.Font.open(src)
    for glyph in font:
        for contour in glyph:
            dilate_contour(contour, weight)
        # components inherit boldness from their (bolded) base glyphs
    info = font.info
    italic = bool(info.italicAngle)  # preserve italic-ness of the source
    info.openTypeOS2WeightClass = 700
    if italic:
        info.styleName = "Bold Italic"
        info.styleMapStyleName = "bold italic"
        info.postscriptFontName = "CourierBadi-BoldItalic"
        info.postscriptFullName = "Courier Badi Bold Italic"
        info.openTypeNamePreferredSubfamilyName = "Bold Italic"
    else:
        info.styleName = "Bold"
        info.styleMapStyleName = "bold"
        info.postscriptFontName = "CourierBadi-Bold"
        info.postscriptFullName = "Courier Badi Bold"
        info.openTypeNamePreferredSubfamilyName = "Bold"
    # heavier stems for the hinter
    if info.postscriptStemSnapV:
        info.postscriptStemSnapV = [v + int(2 * weight) for v in info.postscriptStemSnapV]
    if info.postscriptStemSnapH:
        info.postscriptStemSnapH = [v + int(2 * weight) for v in info.postscriptStemSnapH]
    font.save(out, overwrite=True)
    return len(list(font))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--out", default="sources/CourierBadi-Bold.ufo")
    ap.add_argument("--weight", type=float, default=34.0,
                    help="outward offset in font units (stem grows by ~2x this)")
    args = ap.parse_args()
    n = make_bold(args.src, args.out, args.weight)
    print(f"wrote {args.out}: {n} glyphs, emboldened by {args.weight} units")


if __name__ == "__main__":
    main()
