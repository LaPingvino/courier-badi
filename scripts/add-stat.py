#!/usr/bin/env python3
"""Add a STAT table (wght + ital axes) to the static Courier Badi family.

fontbakery requires a STAT table describing the family's axes. For the static
Regular/Italic/Bold/Bold-Italic family each font declares its own position on
the weight and italic axes, with the default values (Regular, Roman) marked
elidable and style-linked to their bold/italic partners.

Usage: python3 scripts/add-stat.py fonts/ttf/*.ttf
"""
import sys

from fontTools.ttLib import TTFont
from fontTools.otlLib.builder import buildStatTable

ELIDABLE = 0x2


def is_italic(font):
    if font["head"].macStyle & 0x02:
        return True
    sub = font["name"].getDebugName(17) or font["name"].getDebugName(2) or ""
    return "Italic" in sub


def add_stat(path):
    font = TTFont(path)
    if "fvar" in font:
        print(f"{path}: variable font, STAT handled by the builder; skipping")
        return
    wght = font["OS/2"].usWeightClass
    ital = 1 if is_italic(font) else 0

    if wght >= 700:
        wght_vals = [{"value": 700, "name": "Bold"}]
    else:
        wght_vals = [{"value": 400, "name": "Regular", "flags": ELIDABLE, "linkedValue": 700}]

    if ital:
        ital_vals = [{"value": 1, "name": "Italic"}]
    else:
        ital_vals = [{"value": 0, "name": "Roman", "flags": ELIDABLE, "linkedValue": 1}]

    buildStatTable(font, [
        {"tag": "wght", "name": "Weight", "values": wght_vals},
        {"tag": "ital", "name": "Italic", "values": ital_vals},
    ])
    font.save(path)
    print(f"{path}: STAT wght={wght_vals[0]['value']} ital={ital_vals[0]['value']}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        add_stat(p)
