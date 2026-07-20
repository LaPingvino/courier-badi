#!/usr/bin/env python3
"""Make a weight-neutral CONTRAST master from a base master.

The XOPQ ("vertical stroke thickness") axis needs, at each weight, a partner
master with more stroke modulation: vertical stems thicker, horizontal bars
thinner. This applies exactly that -- it dilates every outline outward along the
horizontal normal (+dx, thickens verticals) and inward along the vertical normal
(-dy, thins horizontals), reusing make-bold's dilation. Because it thickens one
direction and thins the other, the overall colour stays close to the source, so
the axis reads as *contrast*, not weight, and is orthogonal to wght.

Crucially it keeps the source's weight class and style names (unlike make-bold,
which forces Bold), so a contrast partner can be built for the Regular and the
Bold alike. Point structure is untouched, so base and contrast interpolate.

Usage:
  python3 scripts/make-contrast-master.py --src <base.ufo> --out <contrast.ufo> \
      [--dx 26] [--dy 14]
"""
import argparse
import importlib.util
import os

import ufoLib2

# reuse the dilation from make-bold.py (hyphenated filename -> load by path)
_spec = importlib.util.spec_from_file_location(
    "makebold", os.path.join(os.path.dirname(__file__), "make-bold.py"))
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)


def make_contrast(src, out, dx, dy):
    font = ufoLib2.Font.open(src)
    for glyph in font:
        for contour in glyph:
            _mb.dilate_contour(contour, dx, -dy)  # +dx thickens V, -dy thins H
    info = font.info
    # Keep weight/style as-is (this is a same-weight sibling, not a bolder one);
    # only nudge the stem hints: verticals fatter, horizontals thinner.
    if info.postscriptStemSnapV:
        info.postscriptStemSnapV = [v + int(2 * dx) for v in info.postscriptStemSnapV]
    if info.postscriptStemSnapH:
        info.postscriptStemSnapH = [max(1, v - int(2 * dy)) for v in info.postscriptStemSnapH]
    font.save(out, overwrite=True)
    return len(list(font))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dx", type=float, default=26.0,
                    help="vertical-stem thickening (outward, horizontal normal)")
    ap.add_argument("--dy", type=float, default=14.0,
                    help="horizontal-bar thinning (inward, vertical normal)")
    args = ap.parse_args()
    n = make_contrast(args.src, args.out, args.dx, args.dy)
    print(f"wrote {args.out}: {n} glyphs, contrast +{args.dx:.0f}V/-{args.dy:.0f}H")


if __name__ == "__main__":
    main()
