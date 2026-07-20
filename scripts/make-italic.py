#!/usr/bin/env python3
"""Generate the Italic UFO from the (corrected) Regular UFO by shearing.

Courier Badi's Italic is produced as an oblique: the Regular is sheared by the
italic angle, so the Italic inherits every correction made to the Regular
(fontbakery fixes, Arabic shaping, the seen/sheen widening, new coverage
glyphs, ...) and the lowercase `a` is simply the roman `a` slanted -- which is
exactly the harmonisation we want (the old bespoke italic `a` was inconsistent).

Shearing is linear, so:
  - contour points are sheared directly: (x, y) -> (x + y*tan, y);
  - a component's transform is conjugated (skew . T . skew^-1) so that a
    component pointing at an already-sheared base lands in the right place;
  - advance widths are unchanged, preserving the strict monospace.

Run after regenerating the Regular. Usage:
  python3 scripts/make-italic.py [--angle 10] \
      [--src sources/CourierBadi-Regular.ufo] [--out sources/CourierBadi-Italic.ufo]
"""
import argparse
import glob
import math
import os
import re

import ufoLib2
from fontTools.misc.transform import Transform
from fontTools.ufoLib.glifLib import readGlyphFromString


def apply_overrides(font, overrides_dir):
    """Replace sheared glyphs with genuine cursive italic forms dropped in the
    overrides directory (already drawn at the italic angle). Filenames don't
    matter; the glyph name is read from the .glif."""
    n = 0
    for path in sorted(glob.glob(os.path.join(overrides_dir, "*.glif"))):
        data = open(path, encoding="utf-8").read()
        m = re.search(r'<glyph\s+name="([^"]+)"', data)
        if not m:
            continue
        name = m.group(1)
        if name in font:
            del font[name]
        g = font.newGlyph(name)
        readGlyphFromString(data, g, g.getPointPen())
        n += 1
    return n


def make_italic(src, out, angle, overrides_dir=None):
    font = ufoLib2.Font.open(src)
    t = math.tan(math.radians(angle))
    skew = Transform(1, 0, t, 1, 0, 0)
    skew_inv = Transform(1, 0, -t, 1, 0, 0)

    for glyph in font:
        for contour in glyph:
            for pt in contour:
                pt.x, pt.y = skew.transformPoint((pt.x, pt.y))
        for comp in glyph.components:
            comp.transformation = tuple(
                skew.transform(Transform(*comp.transformation)).transform(skew_inv)
            )
        for anchor in glyph.anchors:
            anchor.x, anchor.y = skew.transformPoint((anchor.x, anchor.y))
        # advance width is unchanged -> monospace preserved

    n_over = 0
    if overrides_dir and os.path.isdir(overrides_dir):
        n_over = apply_overrides(font, overrides_dir)

    info = font.info
    info.styleName = "Italic"
    info.styleMapStyleName = "italic"
    info.italicAngle = -float(angle)
    info.postscriptFontName = "CourierBadi-Italic"
    info.postscriptFullName = "Courier Badi Italic"
    info.openTypeNamePreferredSubfamilyName = "Italic"
    # postscriptSlantAngle mirrors the italic angle for some renderers
    info.postscriptSlantAngle = -float(angle)

    font.save(out, overwrite=True)
    return len(list(font)), n_over


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--out", default="sources/CourierBadi-Italic.ufo")
    ap.add_argument("--overrides", default="sources/italic-overrides")
    ap.add_argument("--angle", type=float, default=10.0)
    args = ap.parse_args()
    n, n_over = make_italic(args.src, args.out, args.angle, args.overrides)
    print(f"wrote {args.out}: {n} glyphs ({n_over} cursive overrides), "
          f"sheared {args.angle} deg from {args.src}")


if __name__ == "__main__":
    main()
