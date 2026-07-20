#!/usr/bin/env python3
"""Add an OpenType 'meta' table with dlng/slng ScriptLangTags to built fonts.

Google Fonts (and fontbakery's googlefonts/meta/script_lang_tags check) want a
'meta' table declaring the scripts the font is designed for (dlng) and supports
(slng). gftools builder does not add one, so this runs as a post-build step over
the produced binaries. The script list is derived from the font's actual cmap
coverage, so it stays correct as coverage changes.

Usage: python3 scripts/add-meta-table.py fonts/ttf/*.ttf fonts/otf/*.otf
"""
import sys
from fontTools.ttLib import TTFont

# Minimum number of encoded codepoints in a Unicode block before we claim the
# script, to avoid declaring a script for a stray symbol or two.
THRESHOLD = 8

# (ScriptLangTag, ranges) — ranges are inclusive (start, end) codepoints.
SCRIPTS = [
    ("Latn", [(0x0041, 0x024F), (0x1E00, 0x1EFF)]),
    ("Grek", [(0x0370, 0x03FF), (0x1F00, 0x1FFF)]),
    ("Cyrl", [(0x0400, 0x04FF), (0x0500, 0x052F), (0xA640, 0xA69F)]),
    ("Arab", [(0x0600, 0x06FF), (0x0750, 0x077F), (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)]),
    ("Hebr", [(0x0590, 0x05FF)]),
]


def scripts_for(font):
    cmap = set(font.getBestCmap())
    tags = []
    for tag, ranges in SCRIPTS:
        n = sum(1 for cp in cmap if any(a <= cp <= b for a, b in ranges))
        if n >= THRESHOLD:
            tags.append(tag)
    return tags


def add_meta(path):
    font = TTFont(path)
    tags = scripts_for(font)
    if not tags:
        print(f"{path}: no scripts detected, skipping")
        return
    value = ", ".join(tags)
    if "meta" in font:
        meta = font["meta"]
    else:
        from fontTools.ttLib import newTable
        meta = newTable("meta")
        meta.data = {}
        font["meta"] = meta
    meta.data["dlng"] = value
    meta.data["slng"] = value
    font.save(path)
    print(f"{path}: meta dlng/slng = {value}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        add_meta(p)
