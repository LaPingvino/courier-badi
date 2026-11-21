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


def dilate_contour(contour, dx, dy):
    pts = list(contour)
    n = len(pts)
    if n < 3:
        return
    # Offset every point along the right-hand normal of its travel direction.
    # With PostScript winding (outer CCW, holes CW) this grows the outer contour
    # and shrinks the counters -- i.e. thickens the stroke -- for both straight
    # stems and curved bowls, without needing a winding sign.
    #
    # dx grows the horizontal component of the offset (thickens VERTICAL stems);
    # dy grows the vertical component (thickens HORIZONTAL strokes). Equal dx=dy
    # is a balanced (monolinear) bold; dx>dy adds stroke contrast/modulation.
    orig = [(p.x, p.y) for p in pts]
    for i in range(n):
        px, py = orig[(i - 1) % n]
        nx, ny = orig[(i + 1) % n]
        tx, ty = nx - px, ny - py
        L = math.hypot(tx, ty) or 1.0
        pts[i].x += dx * (ty / L)
        pts[i].y += dy * (-tx / L)


HEBREW_KEY = "org.courierbadi.hebrew"


def ink_bounds(font):
    from fontTools.pens.boundsPen import BoundsPen
    out = {}
    for g in font:
        bp = BoundsPen(font)
        g.draw(bp)
        out[g.name] = bp.bounds
    return out


def move_anchors(font, bounds, dx, dy):
    """Move anchors with the dilation, so marks keep the source's clearance:
    an anchor above the glyph's (source) ink goes up by dy, one below it down,
    one left of it left by dx, one right of it right; anchors inside the ink
    (a dagesh's centre, a dot's own anchor) stay. A mark's own attaching
    anchor sits on its ink edge, so it moves with that edge."""
    n = 0
    for g in font:
        b = bounds.get(g.name)
        if b is None:
            continue
        x0, y0, x1, y1 = b
        for a in g.anchors:
            mx = dx if a.x >= x1 - 0.5 else -dx if a.x <= x0 + 0.5 else 0
            my = dy if a.y >= y1 - 0.5 else -dy if a.y <= y0 + 0.5 else 0
            if mx or my:
                a.x += mx
                a.y += my
                n += 1
    return n


def replace_hebrew_composites(font):
    """The Hebrew presentation forms are composites placed from the anchors
    (fit-hebrew.py); after the anchors moved, place their marks again."""
    for g in font:
        if g.lib.get(HEBREW_KEY) is None or g.contours or len(g.components) < 2:
            continue
        base = {a.name: a for a in font[g.components[0].baseGlyph].anchors}
        for c in g.components[1:]:
            ma = [a for a in font[c.baseGlyph].anchors if a.name.startswith("_")]
            if ma and ma[0].name[1:] in base:
                b = base[ma[0].name[1:]]
                c.transformation = (1, 0, 0, 1, b.x - ma[0].x, b.y - ma[0].y)


def make_bold(src, out, dx, dy):
    font = ufoLib2.Font.open(src)
    bounds = ink_bounds(font)
    for glyph in font:
        for contour in glyph:
            dilate_contour(contour, dx, dy)
        # components inherit boldness from their (bolded) base glyphs
    move_anchors(font, bounds, dx, dy)
    replace_hebrew_composites(font)
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
        info.postscriptStemSnapV = [v + int(2 * dx) for v in info.postscriptStemSnapV]
    if info.postscriptStemSnapH:
        info.postscriptStemSnapH = [v + int(2 * dy) for v in info.postscriptStemSnapH]
    font.save(out, overwrite=True)
    return len(list(font))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--out", default="sources/CourierBadi-Bold.ufo")
    ap.add_argument("--weight", type=float, default=34.0,
                    help="outward offset in font units (stem grows by ~2x this)")
    ap.add_argument("--contrast", type=float, default=1.0,
                    help="horizontal/vertical offset ratio; 1=balanced, >1 adds "
                         "stroke contrast (thin horizontals, thick verticals)")
    args = ap.parse_args()
    dx = args.weight
    dy = args.weight / args.contrast
    n = make_bold(args.src, args.out, dx, dy)
    print(f"wrote {args.out}: {n} glyphs, emboldened dx={dx:.0f} dy={dy:.0f}")


if __name__ == "__main__":
    main()
