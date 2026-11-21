#!/usr/bin/env python3
"""Draw the Hebrew dots where they read without GPOS.

A renderer that applies no GPOS (Lexington's PDF writer, other simple ones)
draws a zero-width mark at its default outline position over the letter's
cell. The donor drew every point centred on the cell, so there the shin dot
and the sin dot looked alike and a holam male sat on the vav's stem. This
step moves those marks' default outlines
(translating each glyph whole: outline and its own anchors together, so every
GPOS position stays exactly as it was) to where they read on their letter:

  - shin dot U+05C1, sin dot U+05C2: where the GPOS puts them on shin (over
    the right arm, over the left arm);
  - holam U+05B9: where it reads as holam male, above-left of the vav's head,
    its ink ending at the line of the stem's left edge (HOLAM_GAP). The vav's
    `holam` anchor moves there too, so HarfBuzz draws the holam male the same
    way (it used to sit straight over the stem). On the other letters the
    holam keeps its GPOS place (their anchors are unchanged); without GPOS it
    now stands left of the centre, nearer the usual top-left of a holam haser;
  - holam haser for vav U+05BA (consonantal vav + holam, as in mitsvot):
    HASER_STEP further left than the holam male on the vav, in the GPOS and
    without, so the two stay distinct;
  - the dagesh U+05BC stays centred: one glyph serves every letter, and
    centred is right for most of them. In vav (shuruk), zayin, yod and final
    nun it hides in the stem; a renderer without GPOS should use the
    presentation forms there (U+FB35 is vav with dagesh, drawn as a shuruk),
    as Lexington's PDF writer does.

The precomposed forms (U+FB1D-FB4F) are composites placed from the anchors;
they are placed again afterwards, so they match the GPOS.

Everything is measured on each master's own ink (the Bold's thicker stems,
the Italic's slant), so run it on every master after they are derived (make
masters does). Idempotent.

Usage: python3 scripts/place-default-marks.py sources/CourierBadi-*.ufo
"""
import argparse
import math

import pathops
import ufoLib2
from fontTools.pens.boundsPen import BoundsPen

HEBREW_KEY = "org.courierbadi.hebrew"
VAV, SHIN = "uni05D5", "uni05E9"
SHINDOT, SINDOT, HOLAM, HOLAM_HASER = (
    "uni05C1", "uni05C2", "uni05B9", "uni05BA")
HOLAM_GAP = 0      # holam male: ink ends this far left of the stem's line
HASER_STEP = 60    # holam haser for vav: this much ink gap left of holam male


def bounds(font, g):
    bp = BoundsPen(font)
    g.draw(bp)
    return bp.bounds


def own_anchor(g):
    return next(a for a in g.anchors if a.name.startswith("_"))


def anchor(g, name):
    return next(a for a in g.anchors if a.name == name)


def translate(g, dx, dy):
    """Move a mark glyph whole (outline and every anchor on it)."""
    if not dx and not dy:
        return
    for c in g.contours:
        for p in c.points:
            p.x += dx
            p.y += dy
    for a in g.anchors:
        a.x += dx
        a.y += dy


def stem_left(font, g, y, slant):
    """The vav stem's left ink edge at height y (extrapolated along the slant
    above the letter's ink)."""
    b = bounds(font, g)
    yy = min(y, b[3] - 80)
    path = pathops.Path()
    g.draw(path.getPen())
    band = pathops.Path()
    pen = band.getPen()
    pen.moveTo((b[0] - 10, yy - 1))
    pen.lineTo((b[2] + 10, yy - 1))
    pen.lineTo((b[2] + 10, yy + 1))
    pen.lineTo((b[0] - 10, yy + 1))
    pen.closePath()
    cut = pathops.op(path, band, pathops.PathOp.INTERSECTION)
    return cut.bounds[0] + (y - yy) * slant


def snap(g, name, target):
    """Translate mark g so its own anchor `name` sits on `target` (x, y)."""
    a = own_anchor(g)
    assert a.name == name, (g.name, a.name)
    translate(g, target[0] - a.x, target[1] - a.y)   # exact: anchor on anchor


def place_composites(font):
    for g in font:
        if g.lib.get(HEBREW_KEY) is None or g.contours or len(g.components) < 2:
            continue
        base = {a.name: a for a in font[g.components[0].baseGlyph].anchors}
        for c in g.components[1:]:
            ma = [a for a in font[c.baseGlyph].anchors if a.name.startswith("_")]
            if ma and ma[0].name[1:] in base:
                b = base[ma[0].name[1:]]
                c.transformation = (1, 0, 0, 1, b.x - ma[0].x, b.y - ma[0].y)
        # the form carries its letter's anchors (fit-hebrew.py); keep the
        # one this step moves (vav's holam) in step
        for a in g.anchors:
            if a.name == "holam" and "holam" in base:
                a.x, a.y = base["holam"].x, base["holam"].y


def run(path):
    font = ufoLib2.Font.open(path)
    slant = math.tan(math.radians(-(font.info.italicAngle or 0)))
    vav, shin = font[VAV], font[SHIN]

    # shin and sin dots: their place on shin
    for mark, cls in ((SHINDOT, "_shindot"), (SINDOT, "_sindot")):
        a = anchor(shin, cls[1:])
        snap(font[mark], cls, (a.x, a.y))

    # holam male: the vav's anchor, then the holam's default on it
    hol = font[HOLAM]
    hb = bounds(font, hol)
    ha = own_anchor(hol)
    va = anchor(vav, "holam")
    ink_y = (hb[1] + hb[3]) / 2 + (va.y - ha.y)        # its centre on the vav
    half = (hb[2] - hb[0]) / 2
    cx = stem_left(font, vav, ink_y, slant) - HOLAM_GAP - half
    va.x = round(cx + (ha.x - (hb[0] + hb[2]) / 2))
    snap(hol, "_holam", (va.x, va.y))

    # holam haser for vav: further left, same anchor on the vav
    has = font[HOLAM_HASER]
    sb = bounds(font, has)
    sa = own_anchor(has)
    hb = bounds(font, hol)                              # moved
    cx_h = hb[0] - HASER_STEP - (sb[2] - sb[0]) / 2
    cy_h = (hb[1] + hb[3]) / 2
    translate(has, round(cx_h - (sb[0] + sb[2]) / 2), round(cy_h - (sb[1] + sb[3]) / 2))
    sa.x, sa.y = va.x, va.y                             # lands where drawn

    place_composites(font)
    font.save()
    out = {n: [round(v) for v in bounds(font, font[n])]
           for n in (SHINDOT, SINDOT, HOLAM, HOLAM_HASER)}
    print(f"{path}: vav holam anchor ({va.x}, {va.y}); default ink {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ufos", nargs="+")
    for p in ap.parse_args().ufos:
        run(p)


if __name__ == "__main__":
    main()
