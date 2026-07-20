#!/usr/bin/env python3
"""Normalize contour winding in a UFO so outer contours are CCW and holes CW.

The Latin was digitized CCW-outer, but the merged Cyrillic/Greek/Arabic came in
CW-outer. Inconsistent winding breaks anything that offsets along the normal
(e.g. the emboldening in make-bold.py, which thinned the CW glyphs instead of
thickening them) and can trip up other tools. This rewinds every contour to the
PostScript convention based on its nesting depth (even = outer = CCW,
odd = hole = CW), reversing only the ones that are wrong.

Usage: python3 scripts/normalize-winding.py [--ufo sources/CourierBadi-Regular.ufo]
"""
import argparse

import ufoLib2
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.pointPen import PointToSegmentPen, ReverseContourPointPen
from fontTools.pens.recordingPen import RecordingPointPen


def contour_area(contour):
    """True signed area of a contour (curves included). Positive = CCW."""
    ap = AreaPen()
    pp = PointToSegmentPen(ap)
    pp.beginPath()
    for p in contour:
        pp.addPoint((p.x, p.y), p.type)
    pp.endPath()
    return ap.value


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-9) + xi):
            inside = not inside
        j = i
    return inside


def on_curve_poly(contour):
    pts = [(p.x, p.y) for p in contour if p.type is not None]
    return pts if len(pts) >= 3 else [(p.x, p.y) for p in contour]


def normalize(ufo):
    """The merged Cyrillic/Greek/Arabic were digitized with the whole glyph wound
    backwards (outer CW instead of CCW). Detect that per glyph -- the largest
    contour by absolute area is the outer, and it must be CCW (positive area) --
    and if it is CW, reverse EVERY contour of the glyph (so the outer becomes CCW
    and its holes become CW). This is robust to overlapping strokes (serifs),
    where per-contour nesting is unreliable."""
    font = ufoLib2.Font.open(ufo)
    fixed = 0
    for glyph in font:
        contours = list(glyph.contours)
        if not contours:
            continue
        areas = [contour_area(c) for c in contours]
        outer = max(range(len(contours)), key=lambda i: abs(areas[i]))
        if areas[outer] >= 0:
            continue  # already CCW-outer
        recs = []
        for c in contours:
            rp = RecordingPointPen()
            c.drawPoints(rp)
            recs.append(rp)
        glyph.contours.clear()
        pen = glyph.getPointPen()
        for rp in recs:
            rp.replay(ReverseContourPointPen(pen))
        fixed += 1
    font.save()
    return fixed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    args = ap.parse_args()
    n = normalize(args.ufo)
    print(f"{args.ufo}: reversed {n} mis-wound contours")


if __name__ == "__main__":
    main()
