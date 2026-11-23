#!/usr/bin/env python3
"""Write every GSUB/GPOS/GDEF Coverage table as format 1 (a glyph list).

Post-build workaround for go-text/typesetting (v0.3.5; the shaper of
Lexington and of Fyne, so of Accolade): its port of HarfBuzz's set digest
(harfbuzz/set_digest.go, setDigest.addRange) stops adding a format-2
coverage's ranges as soon as ANY of its three bit filters is full, where
HarfBuzz stops only when all three are. In a lookup whose coverage spans
many glyphs (the Devanagari cell lookups, ~600 glyphs) the glyphs of the
later ranges are then skipped as "not covered": a conjunct loses its second
cell. Format 1 coverages go through setDigest.add, which has no such early
return. The tables mean the same; they are a little larger.

Usage: python3 scripts/coverage-format1.py FONT...
"""
import sys

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables


def _format1(self, font):
    glyphs = getattr(self, "glyphs", None)
    if glyphs is None:
        glyphs = self.glyphs = []
    glyphs.sort(key=font.getGlyphID)
    self.Format = 1
    return {"GlyphArray": glyphs}


def main():
    otTables.Coverage.preWrite = _format1
    for path in sys.argv[1:]:
        font = TTFont(path)
        for tag in ("GDEF", "GSUB", "GPOS"):
            if tag in font:
                font[tag].ensureDecompiled() if hasattr(font[tag], "ensureDecompiled") else None
        font.save(path)
        print(f"{path}: coverage tables written as format 1")


if __name__ == "__main__":
    main()
