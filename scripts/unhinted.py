#!/usr/bin/env python3
"""Write the static TTFs without their TrueType hinting: fonts/unhinted/ttf.

For programs that embed the font and draw it with a rasterizer of their own
(Lexington's PDFs, Accolade's editor: go-text, poppler, pdf.js, PDF viewers
generally do not run TrueType instructions). The hinting (ttfautohint's
glyph programs, fpgm, prep, cvt) is about 1.5 MB of each 4 MB style, most
of it in the Devanagari's scaled variants (scripts/fit-devanagari.py); the
outlines, metrics and OpenType tables are the hinted font's, unchanged.
The hinted fonts in fonts/ttf stay the ones to install.

Usage: python3 scripts/unhinted.py OUTDIR FONT...
"""
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import ttProgram

HINT_TABLES = ("fpgm", "prep", "cvt ", "hdmx", "LTSH", "VDMX")


def unhint(font):
    for tag in HINT_TABLES:
        if tag in font:
            del font[tag]
    glyf = font["glyf"]
    for name in font.getGlyphOrder():
        g = glyf[name]
        if hasattr(g, "program") and g.isComposite():
            del g.program            # (a composite then has no instructions flag)
        elif hasattr(g, "program"):
            g.program = ttProgram.Program()
            g.program.fromBytecode(b"")


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for path in sys.argv[2:]:
        font = TTFont(path)
        unhint(font)
        dst = os.path.join(out, os.path.basename(path))
        font.save(dst)
        print(f"{dst}: {os.path.getsize(path)} -> {os.path.getsize(dst)} bytes without hinting")


if __name__ == "__main__":
    main()
