#!/usr/bin/env python3
"""Check the Devanagari of built fonts by shaping (HarfBuzz).

  - cells: every cluster is as wide as the editor counts it, 1228 per letter
    or spacing sign (not Mn/Me, not a joiner): every consonant, every
    consonant with every vowel sign and mark, every C+virama+C pair, C+C+C
    conjuncts, reph and rakar forms, and a Hindi text;
  - no dotted circle (U+25CC) in any of them; the C+virama+C pairs whose
    virama stays visible are counted (no half form or conjunct; ङ छ ट ठ ड ढ
    द ह have none in Hindi either);
  - the ink's extent against the 12 pt line (1628 above the baseline, 399
    under it): the worst cases are listed;
  - the headline: in the text, gaps in the headline band inside a word.

Usage: python3 scripts/check-devanagari.py fonts/ttf/CourierBadi-*.ttf
Exit status 1 if a cluster has the wrong width or a dotted circle.
"""
import sys
import unicodedata as ud

import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

CELL = 1228
LINE_TOP, LINE_BOTTOM = 1628, -399
V = "्"
CONS = [chr(c) for c in range(0x0915, 0x093A)]
NUKTA_CONS = [chr(c) for c in range(0x0958, 0x0960)]
MATRAS = [chr(c) for c in range(0x093E, 0x094D)] + ["ॢ", "ॣ"]
MARKS = ["ँ", "ं", "ः", "़"]
TEXT = ("क्षत्रिय कि की धर्म श्रद्धा ज्ञान र्‍य कृष्ण हिन्दी। "
        "बहाउल्लाह ने कहा कि पृथ्वी एक देश है और मानवजाति उसके नागरिक हैं। "
        "प्रार्थना ईश्वर के साथ वार्तालाप है। स्त्री और पुरुष समान हैं। "
        "विद्यार्थी उद्देश्य संस्कृत राष्ट्र द्वारा श्रीमान् आत्मा अर्थ सूर्य "
        "क्या प्यार ट्रेन ड्रामा हृदय ऋषि ॐ ०१२३४५६७८९ ।॥ नहीं पढ़ाई ज़िंदगी फ़िल्म")


def words():
    out = set(CONS + NUKTA_CONS)
    for c in CONS + NUKTA_CONS:
        for m in MATRAS + MARKS:
            out.add(c + m)
        out.add(c + V)
        out.add("र" + V + c)                    # reph
        out.add(c + V + "र")                    # rakar
        out.add("र" + V + c + "ि")
        out.add("र" + V + c + "ी")
        out.add("र" + V + c + "ीं")
        for d in CONS:
            out.add(c + V + d)
            out.add(c + V + d + "ि")
            out.add(c + V + d + "ा")
    for c in ("स", "न", "क", "द", "श"):
        for d in ("त", "द", "थ", "क", "व"):
            for e in ("र", "य", "व"):
                out.add(c + V + d + V + e)
                out.add(c + V + d + V + e + "ि")
    for w in TEXT.split():
        out.add(w)
    for c in range(0x0904, 0x0915):
        out.add(chr(c))
    return sorted(out)


def cells(w):
    return sum(1 for ch in w if ud.category(ch) not in ("Mn", "Me", "Cf"))


class Font:
    def __init__(self, path):
        self.tt = TTFont(path)
        self.order = self.tt.getGlyphOrder()
        self.gs = self.tt.getGlyphSet()
        self.font = hb.Font(hb.Face(open(path, "rb").read()))
        self.circle = self.tt.getBestCmap().get(0x25CC)
        self.virama = self.tt.getBestCmap().get(0x094D)
        self._b = {}

    def shape(self, w):
        b = hb.Buffer()
        b.add_str(w)
        b.guess_segment_properties()
        hb.shape(self.font, b, {})
        return [(self.order[i.codepoint], p) for i, p in zip(b.glyph_infos, b.glyph_positions)]

    def bounds(self, name):
        if name not in self._b:
            bp = BoundsPen(self.gs)
            self.gs[name].draw(bp)
            self._b[name] = bp.bounds
        return self._b[name]

    def ink(self, glyphs):
        x, lo, hi = 0, 0, 0
        for name, p in glyphs:
            bb = self.bounds(name)
            if bb:
                lo = min(lo, bb[1] + p.y_offset)
                hi = max(hi, bb[3] + p.y_offset)
            x += p.x_advance
        return lo, hi


def headline_gaps(f, w, band):
    """x stretches (font units) inside the word where no glyph covers the
    middle of the headline band"""
    from fontTools.pens.pointInsidePen import PointInsidePen
    glyphs = f.shape(w)
    placed, x = [], 0
    for name, p in glyphs:
        placed.append((name, x + p.x_offset, p.y_offset))
        x += p.x_advance
    y = (band[0] + band[1]) / 2
    covered = []
    for X in range(0, x, 20):
        inside = False
        for name, gx, gy in placed:
            bb = f.bounds(name)
            if not bb or not (bb[0] <= X - gx <= bb[2]):
                continue
            pen = PointInsidePen(f.gs, (X - gx, y - gy))
            f.gs[name].draw(pen)
            if pen.getResult():
                inside = True
                break
        covered.append(inside)
    if True not in covered:
        return []
    a = covered.index(True)
    b = len(covered) - 1 - covered[::-1].index(True)
    gaps, run = [], 0
    for i in range(a, b + 1):
        if not covered[i]:
            run += 20
        elif run:
            gaps.append(run)
            run = 0
    return gaps


def check(path):
    f = Font(path)
    bad, circles, visible = [], [], 0
    worst_hi, worst_lo = [], []
    for w in words():
        g = f.shape(w)
        names = [n for n, _ in g]
        adv = sum(p.x_advance for _, p in g)
        if adv != cells(w) * CELL:
            bad.append((w, cells(w), adv / CELL, " ".join(names)))
        if f.circle in names:
            circles.append(w)
        if len(w) == 3 and w[1] == V and f.virama in names:
            visible += 1
        lo, hi = f.ink(g)
        worst_hi.append((hi, w))
        worst_lo.append((lo, w))
    worst_hi.sort(reverse=True)
    worst_lo.sort()
    n_words = len(words())
    print(f"== {path}: {n_words} clusters/words")
    print(f"  wrong width: {len(bad)}")
    for b in bad[:15]:
        print("    ", b)
    print(f"  dotted circles: {len(circles)} {' '.join(circles[:10])}")
    print(f"  C+virama+C with the virama visible: {visible}/{len(CONS) ** 2}")
    over_hi = sum(1 for h, _ in worst_hi if h > LINE_TOP)
    over_lo = sum(1 for l, _ in worst_lo if l < LINE_BOTTOM)
    print(f"  above {LINE_TOP}: {over_hi}; highest " +
          ", ".join(f"{w} {h:.0f}" for h, w in worst_hi[:6]))
    print(f"  under {LINE_BOTTOM}: {over_lo}; lowest " +
          ", ".join(f"{w} {l:.0f}" for l, w in worst_lo[:8]))
    band = (870, 990)
    gapped = []
    for w in TEXT.split():
        gaps = headline_gaps(f, w, band)
        if gaps:
            gapped.append(f"{w}{gaps}")
    print(f"  headline gaps in the text's words: {len(gapped)} " + " ".join(gapped))
    return not bad and not circles


def main():
    ok = all([check(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
