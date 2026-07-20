#!/usr/bin/env python3
"""Add a STAT table declaring the italic axis to a Regular+Italic family.

fontbakery's opentype/STAT/ital_axis check requires the family to carry a STAT
table with an 'ital' axis linking the Roman and Italic. gftools builder does not
add one for a static two-style family, so this runs as a post-build step: the
Roman gets ital=0 (elidable, linked to the Italic at 1) and the Italic gets
ital=1.

Usage: python3 scripts/add-stat.py fonts/ttf/*.ttf
"""
import sys

from fontTools.ttLib import TTFont
from fontTools.otlLib.builder import buildStatTable


def is_italic(font):
    if font["head"].macStyle & 0x02:
        return True
    sub = font["name"].getDebugName(17) or font["name"].getDebugName(2) or ""
    return "Italic" in sub


def add_stat(path):
    font = TTFont(path)
    if is_italic(font):
        values = [{"value": 1, "name": "Italic"}]
    else:
        # Roman: elidable, and linked to the Italic (value 1) for style linking.
        values = [{"value": 0, "name": "Roman", "flags": 0x2, "linkedValue": 1}]
    buildStatTable(font, [{"tag": "ital", "name": "Italic", "values": values}])
    font.save(path)
    print(f"{path}: STAT ital = {values[0]['value']} ({values[0]['name']})")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        add_stat(p)
