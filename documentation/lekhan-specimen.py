#!/usr/bin/env python3
"""Lekhan monospace specimen: every cluster type of docs/lekhan-vectors.txt
on the cell grid, with its cells, in each style; a Hindi text set by cells.

Each line is shaped by HarfBuzz from the built font, as an editor or a
typesetter would, and drawn on a grid of 1228-unit cells (faint lines; the
Lekhan width function's cluster edges as ticks under the line), so a cluster
that does not fill its cells, or overruns them, shows by eye.

Usage: python3 documentation/lekhan-specimen.py [--fonts fonts/ttf] [--out out/lekhan-specimen.pdf]
       pdftoppm -r 600 -png out/lekhan-specimen.pdf out/lekhan-specimen
"""
import argparse
import importlib.util
import os

import cairo
import uharfbuzz as hb
from fontTools.pens.cairoPen import CairoPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("check_devanagari",
                                               os.path.join(HERE, "..", "scripts", "check-devanagari.py"))
cd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cd)

CELL, UPM = 1228, 2048
PT = 22                      # the specimen's size (cells 13 pt wide)
SCALE = PT / UPM             # font units to points
PAGE_W, PAGE_H = 595, 842    # A4
MARGIN = 42
LINE = 40


class Face:
    def __init__(self, path):
        self.tt = TTFont(path)
        self.gs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.font = hb.Font(hb.Face(open(path, "rb").read()))

    def shape(self, text):
        b = hb.Buffer()
        b.add_str(text)
        b.guess_segment_properties()
        hb.shape(self.font, b, {})
        return [(self.order[i.codepoint], p) for i, p in zip(b.glyph_infos, b.glyph_positions)]

    def draw(self, ctx, text, x, y):
        """draw text from x on baseline y (points); its advance, in units"""
        pen_x = 0
        for name, p in self.shape(text):
            ctx.save()
            ctx.translate(x + (pen_x + p.x_offset) * SCALE, y - p.y_offset * SCALE)
            ctx.scale(SCALE, -SCALE)
            self.gs[name].draw(CairoPen(self.gs, ctx))
            ctx.fill()
            ctx.restore()
            pen_x += p.x_advance
        return pen_x


class Doc:
    def __init__(self, path):
        self.surface = cairo.PDFSurface(path, PAGE_W, PAGE_H)
        self.ctx = cairo.Context(self.surface)
        self.y = MARGIN

    def need(self, h):
        if self.y + h > PAGE_H - MARGIN:
            self.ctx.show_page()
            self.y = MARGIN

    def label(self, text, x, y, size=7, grey=0.35):
        c = self.ctx
        c.save()
        c.set_source_rgb(grey, grey, grey)
        c.select_font_face("sans-serif")
        c.set_font_size(size)
        c.move_to(x, y)
        c.show_text(text)
        c.restore()

    def grid(self, x, y, cells, edges):
        """faint cells from x on baseline y; ticks at the clusters' edges"""
        c = self.ctx
        w = CELL * SCALE
        top, bottom = y - 1628 * SCALE, y + 399 * SCALE
        c.save()
        c.set_line_width(0.15)
        c.set_source_rgb(0.75, 0.82, 0.95)
        for k in range(cells + 1):
            c.move_to(x + k * w, top)
            c.line_to(x + k * w, bottom)
        c.stroke()
        c.set_source_rgb(0.85, 0.2, 0.2)
        c.set_line_width(0.6)
        for e in edges:
            c.move_to(x + e * w, bottom)
            c.line_to(x + e * w, bottom + 2.5)
        c.stroke()
        c.restore()


def clusters(text):
    rs = list(text)
    out, i = [], 0
    while i < len(rs):
        j = cd.cluster_end(rs, i)
        out.append("".join(rs[i:j]))
        i = j
    return out


def item(doc, face, text, x, y):
    """text on its cells from x on baseline y; its width in points, whether
    it is as wide as its cells"""
    cs = clusters(text)
    cells = [cd.cluster_cells(list(c)) for c in cs]
    edges, at = [0], 0
    for n in cells:
        at += n
        edges.append(at)
    doc.grid(x, y, at, edges)
    adv = face.draw(doc.ctx, text, x, y)
    ok = adv == at * CELL
    doc.label(("WRONG " if not ok else "") + " ".join(str(n) for n in cells), x, y + 399 * SCALE + 9,
              size=6, grey=0.35 if ok else 0)
    return at * CELL * SCALE, ok


def flow(doc, face, texts, x0=MARGIN, gap=16):
    """texts side by side, as many as fit a row"""
    bad, x = 0, x0
    doc.need(LINE)
    for t in texts:
        w = max(width_pt(t), 14)
        if x + w > PAGE_W - MARGIN and x > x0:
            doc.y += LINE
            doc.need(LINE)
            x = x0
        _, ok = item(doc, face, t, x, doc.y + 1628 * SCALE)
        bad += not ok
        x += w + gap
    doc.y += LINE
    return bad


def width_pt(text):
    return cd.width(text) * CELL * SCALE


def line(doc, face, text, x, note=""):
    doc.need(LINE)
    _, ok = item(doc, face, text, x, doc.y + 1628 * SCALE)
    if note:
        doc.label(note, x + width_pt(text) + 8, doc.y + 1628 * SCALE, size=7)
    doc.y += LINE
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", default="fonts/ttf")
    ap.add_argument("--out", default="out/lekhan-specimen.pdf")
    ap.add_argument("--sample", default=None, help="a text (Fountain) whose Devanagari lines are set too")
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    styles = {s: Face(os.path.join(args.fonts, f"CourierBadi-{s}.ttf"))
              for s in ("Regular", "Bold", "Italic", "BoldItalic")}
    reg = styles["Regular"]
    doc = Doc(args.out)
    doc.label("Lekhan monospace in Courier Badi " + reg.tt["head"].fontRevision.__format__(".3f"),
              MARGIN, doc.y + 12, size=14, grey=0)
    doc.y += 22
    doc.label("A simple cluster takes one cell, a conjunct two (docs/LEKHAN.md). Blue: the 12 pt cells; "
              "red ticks: the clusters' edges by the Lekhan width; the numbers: each cluster's cells.",
              MARGIN, doc.y + 8, size=6.5)
    doc.y += 16
    bad = 0
    for kind, items in cd.vector_sections():
        doc.need(LINE * 2)
        doc.label(kind, MARGIN, doc.y + 12, size=8.5, grey=0)
        doc.y += 16
        cmap = reg.tt.getBestCmap()
        bad += flow(doc, reg, [t for t, _ in items if all(ord(ch) in cmap for ch in t)])
    doc.need(LINE * 6)
    doc.label("The four styles", MARGIN, doc.y + 12, size=8.5, grey=0)
    doc.y += 16
    for s, f in styles.items():
        bad += not line(doc, f, "क्षत्रिय स्क्री श्रीमान् हिन्दी का कि ला", MARGIN, s)
    if args.sample:
        doc.need(LINE * 3)
        doc.label(os.path.basename(args.sample), MARGIN, doc.y + 12, size=8.5, grey=0)
        doc.y += 16
        for raw in open(args.sample, encoding="utf-8"):
            text = raw.rstrip("\n")
            if not any(cd.is_devanagari(ch) for ch in text):
                continue
            # wrapped at 36 cells
            words, cur = text.split(" "), ""
            for w in words:
                trial = (cur + " " + w) if cur else w
                if cd.width(trial) > 36 and cur:
                    bad += not line(doc, reg, cur, MARGIN)
                    cur = w
                else:
                    cur = trial
            if cur:
                bad += not line(doc, reg, cur, MARGIN)
    doc.surface.finish()
    print(f"{args.out}: {bad} lines of the wrong width")


if __name__ == "__main__":
    main()
