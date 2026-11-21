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
fallback's rule down as anchors, so the GPOS places those marks where the
fallback did (and now also in shapers that never had a fallback).

The rule (hb-ot-shape-fallback.cc, position_mark): with gap = UPM/16 = 128,
  - x: the mark's ink is centred on the base's *advance* (not its ink);
    "right" classes align the mark's right ink edge to the advance;
  - above: the mark's ink bottom sits `gap` above the base's ink top;
    below: the mark's ink top sits `gap` under the base's ink bottom;
    attached classes: the same without the gap;
  - stacked marks: the next mark sits `gap` beyond the previous mark's ink.
The fallback's two clamps (a below mark is never moved up, an above mark is
moved down only halfway) depend on the pair and cannot be expressed by
anchors; they only matter where a mark is drawn far from where it attaches.
scripts/check-mark-parity.py measures the difference against a build without
GPOS.

Combining classes come from the Unicode database, with HarfBuzz's Arabic
re-categorisation (fathatan..sukun, superscript alef: above; kasratan, kasra:
below). Classes HarfBuzz does not position (0, overlay) get no anchor.

Anchors depend on the ink, so this runs on every master after it is derived
(make masters): the Bold's taller ink gets correspondingly higher anchors,
exactly as the fallback measured it. Every base glyph gets the same anchor
names in every master, so the masters stay interpolation-compatible. The
script owns only the anchor names in CLASSES (plus their "_" forms) and is
idempotent: it removes and rewrites them.

Usage: python3 scripts/make-mark-anchors.py sources/CourierBadi-*.ufo
"""
import sys
import unicodedata as ud

import ufoLib2
from fontTools.pens.boundsPen import BoundsPen

GAP = 128  # UPM / 16

# anchor name -> (horizontal alignment, vertical side, gap)
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


def is_hebrew(cp):
    return 0x0591 <= cp <= 0x05C7 or cp == 0xFB1E


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


def bounds(font, g):
    bp = BoundsPen(font)
    g.draw(bp)
    return bp.bounds


def owned(name):
    return name.lstrip("_") in CLASSES


def run(path):
    font = ufoLib2.Font.open(path)
    marks = {}
    for g in font:
        for cp in g.unicodes:
            cls = mark_class(cp)
            if cls:
                marks[g.name] = cls
    all_marks = {g.name for g in font
                 if any(ud.category(chr(c)) in ("Mn", "Me") for c in g.unicodes)}
    used = sorted(set(marks.values()))
    nb = nm = 0
    for g in font:
        keep = [a for a in g.anchors if not owned(a.name)]
        if len(keep) != len(g.anchors):
            g.anchors.clear()
            for a in keep:
                g.appendAnchor({"name": a.name, "x": a.x, "y": a.y})
        b = bounds(font, g)
        if b is None:
            continue
        x0, y0, x1, y1 = b
        if g.name in marks:
            cls = marks[g.name]
            halign, side, gap = CLASSES[cls]
            ax = x1 if halign == "right" else (x0 + x1) / 2
            ay = y0 if side == "top" else y1
            g.appendAnchor({"name": "_" + cls, "x": round(ax), "y": round(ay)})
            if cls in STACKING:
                sy = y1 + gap if side == "top" else y0 - gap
                g.appendAnchor({"name": cls, "x": round((x0 + x1) / 2), "y": round(sy)})
            nm += 1
        elif g.name not in all_marks and g.width > 0:
            for cls in used:
                halign, side, gap = CLASSES[cls]
                ax = g.width if halign == "right" else g.width / 2
                ay = y1 + gap if side == "top" else y0 - gap
                g.appendAnchor({"name": cls, "x": round(ax), "y": round(ay)})
            nb += 1
    font.save()
    print(f"{path}: anchors for {nb} bases and {nm} marks ({', '.join(used)})")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        run(p)
