#!/usr/bin/env python3
"""Write the static TTFs without their TrueType hinting: fonts/unhinted/ttf.

For programs that embed the font and draw it with a rasterizer of their own
(Accolade's editor and Lexington's shaping: go-text; Lexington's PDFs:
poppler and pdf.js do not run TrueType instructions, Ghostscript does, so
there its edges move by a fraction of a pixel). The hinting (ttfautohint's
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
