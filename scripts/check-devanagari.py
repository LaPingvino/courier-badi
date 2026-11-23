#!/usr/bin/env python3
"""Check the Devanagari of built fonts by shaping (HarfBuzz), against Lekhan
monospace (docs/LEKHAN.md):

  - cells: every text is exactly as wide as the Lekhan width counts it,
    1228 a cell: the test vectors (docs/lekhan-vectors.txt), every
    consonant with every vowel sign and mark, every C+virama+C, C+C+C
    conjuncts, reph and rakar forms, and a Hindi text, word by word;
  - no dotted circle (U+25CC) in any of them; the C+virama+C pairs whose
    virama stays visible are counted (no half form or conjunct);
  - no stretched headline: the room a conjunct leaves in its cells (its
    pads, headline alone inside a word: a cluster drawn too narrow for its
    cells) at most STRETCH_MAX;
  - the ink's extent against the 12 pt line (1628 above the baseline, 399
    under it): the worst cases are listed;
  - the headline: in the text, gaps in the headline band inside a word.

The Lekhan width here is a port of Lexington's lekhan package (Go), the
reference; both read the same vectors.

Usage: python3 scripts/check-devanagari.py [--sample FILE] fonts/ttf/CourierBadi-*.ttf
Exit status 1 if a text has the wrong width, a dotted circle or a
stretched headline.
"""
import argparse
import os
import re
import sys
import unicodedata as ud

import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

CELL = 1228
LINE_TOP, LINE_BOTTOM = 1628, -399
STRETCH_MAX = 500          # font units of pads (headline alone) in a conjunct's two cells:
                           # about what a narrow simple letter (र) leaves in its one
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
VECTORS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "lekhan-vectors.txt")


# --- Lekhan width (port of lexington/lekhan) ------------------------------------

VIRAMA, ZWNJ, ZWJ = 0x094D, 0x200C, 0x200D


def is_consonant(ch):
    r = ord(ch)
    return 0x0915 <= r <= 0x0939 or 0x0958 <= r <= 0x095F or 0x0978 <= r <= 0x097F


def is_devanagari(ch):
    r = ord(ch)
    return 0x0900 <= r <= 0x097F or 0xA8E0 <= r <= 0xA8FF or 0x1CD0 <= r <= 0x1CFF or 0x11B00 <= r <= 0x11B5F


def is_mark(ch):
    return ud.category(ch) in ("Mn", "Mc", "Me")


def rune_width(ch):
    r = ord(ch)
    if r < 0x300:
        return 1
    if ud.category(ch) in ("Mn", "Me") or 0x200B <= r <= 0x200F or 0x202A <= r <= 0x202E \
            or 0x2066 <= r <= 0x2069 or 0x1160 <= r <= 0x11FF:
        return 0
    if r < 0x1100:
        return 1
    if r <= 0x115F or (0x2E80 <= r <= 0xA4CF and r != 0x303F) or 0xAC00 <= r <= 0xD7A3 \
            or 0xF900 <= r <= 0xFAFF or 0xFE30 <= r <= 0xFE4F or 0xFF00 <= r <= 0xFF60 \
            or 0xFFE0 <= r <= 0xFFE6 or 0x1F300 <= r <= 0x1F64F or 0x1F900 <= r <= 0x1F9FF \
            or 0x20000 <= r <= 0x3FFFD:
        return 2
    return 1


def joins(a, b):
    if ord(a) < 0x20:
        return False
    return is_mark(b) or ord(b) in (ZWNJ, ZWJ) or ord(a) == ZWJ or ord(a) == VIRAMA and is_consonant(b)


def boundary(rs, i):
    if i <= 0 or i >= len(rs):
        return True
    a, b = rs[i - 1], rs[i]
    if not joins(a, b):
        return True
    if not is_consonant(b):
        return False
    seen = False
    for k in range(i - 1, -1, -1):
        c = rs[k]
        if ord(c) == VIRAMA:
            seen = True
        elif ord(c) == ZWJ or ud.category(c) == "Mn":
            pass
        elif is_consonant(c):
            return not seen
        else:
            return True
    return True


def cluster_end(rs, i):
    j = i + 1
    while j < len(rs) and not boundary(rs, j):
        j += 1
    return min(j, len(rs))


def cluster_cells(c):
    if not c:
        return 0
    if not is_devanagari(c[0]):
        n = 0
        for k, r in enumerate(c):
            if k > 0 and is_devanagari(r) and is_mark(r) and \
                    not any(is_devanagari(x) and not is_mark(x) for x in c[:k]):
                n += 1
            else:
                n += rune_width(r)
        return n
    return 2 if sum(1 for r in c if is_consonant(r)) >= 2 else 1


def width(text):
    rs, n, i = list(text), 0, 0
    while i < len(rs):
        j = cluster_end(rs, i)
        n += cluster_cells(rs[i:j])
        i = j
    return n


def unescape(s):
    s = s.replace("<ZWJ>", "‍").replace("<ZWNJ>", "‌")
    return re.sub(r"<U\+([0-9A-Fa-f]{4,6})>", lambda m: chr(int(m.group(1), 16)), s)


def vectors():
    """(clusters, cells, note) per line of docs/lekhan-vectors.txt"""
    out = []
    for line in open(VECTORS, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        out.append((unescape(parts[0]).split("|"), [int(x) for x in parts[1].split()],
                    parts[2] if len(parts) > 2 else ""))
    return out


def vector_sections():
    """the vectors by their section comments: [(heading, [(text, note)])]"""
    secs, cur = [], None
    for line in open(VECTORS, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            cur = (line[3:], [])
            secs.append(cur)
            continue
        if not line or line.startswith("#") or cur is None:
            continue
        parts = line.split("\t")
        cur[1].append((unescape(parts[0]).replace("|", ""), parts[2] if len(parts) > 2 else ""))
    return secs


def check_vectors():
    bad = 0
    for cl, cells, note in vectors():
        rs = list("".join(cl))
        got, i = [], 0
        while i < len(rs):
            j = cluster_end(rs, i)
            got.append(("".join(rs[i:j]), cluster_cells(rs[i:j])))
            i = j
        if [g for g, _ in got] != cl or [n for _, n in got] != cells:
            print(f"  vector {'|'.join(cl)} ({note}): got {got}")
            bad += 1
    return bad


# --- the font --------------------------------------------------------------------

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
    for cl, _, _ in vectors():
        if any(is_devanagari(ch) for ch in "".join(cl)):
            out.add("".join(cl))
    return sorted(out)


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
        lo, hi = 0, 0
        for name, p in glyphs:
            bb = self.bounds(name)
            if bb:
                lo = min(lo, bb[1] + p.y_offset)
                hi = max(hi, bb[3] + p.y_offset)
        return lo, hi

    def placed(self, w):
        out, x = [], 0
        for name, p in self.shape(w):
            out.append((name, x + p.x_offset, p.y_offset))
            x += p.x_advance
        return out, x


def coverage(f, placed, x0, x1, band, step=16):
    """for x in [x0, x1): (ink in the headline band, ink under it)"""
    from fontTools.pens.pointInsidePen import PointInsidePen
    yh = (band[0] + band[1]) / 2
    ys = [band[0] - 60 - k * 90 for k in range(16)] + [band[1] + 60 + k * 90 for k in range(6)]
    out = []
    for X in range(int(x0), int(x1), step):
        head = body = False
        for name, gx, gy in placed:
            bb = f.bounds(name)
            if not bb or not (bb[0] <= X - gx <= bb[2]):
                continue
            for y, kind in [(yh, "h")] + [(y, "b") for y in ys]:
                if kind == "h" and head or kind == "b" and body:
                    continue
                if not (bb[1] <= y - gy <= bb[3]):
                    continue
                pen = PointInsidePen(f.gs, (X - gx, y - gy))
                f.gs[name].draw(pen)
                if pen.getResult():
                    if kind == "h":
                        head = True
                    else:
                        body = True
        out.append((head, body))
    return out


def stretch(f, cluster, band=None):
    """the room (units) a cluster leaves in its cells, filled with headline
    in a word: its pads (lead.N, trail1.N, trail2.N), shaped alone. The
    glyphs are scaled to fill the cells; what is left is less than a step
    of the scale, unless the cluster is narrower than the widest step
    reaches (र्र)"""
    return sum(p.x_advance for name, p in f.shape(cluster) if name.startswith(("lead.", "trail")))


def headline_gaps(f, w, band):
    """x stretches (font units) inside the word where no glyph covers the
    middle of the headline band"""
    placed, x = f.placed(w)
    cov = coverage(f, placed, 0, x, band, step=20)
    covered = [h for h, _ in cov]
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


def check(path, sample_lines, full):
    f = Font(path)
    bad, circles, visible = [], [], 0
    worst_hi, worst_lo = [], []
    ws = words() + sample_lines
    for w in ws:
        g = f.shape(w)
        names = [n for n, _ in g]
        adv = sum(p.x_advance for _, p in g)
        if adv != width(w) * CELL:
            bad.append((w, width(w), round(adv / CELL, 3), " ".join(names)))
        if f.circle in names and w not in ("ा", "ं"):
            circles.append(w)
        if len(w) == 3 and w[1] == V and f.virama in names:
            visible += 1
        lo, hi = f.ink(g)
        worst_hi.append((hi, w))
        worst_lo.append((lo, w))
    worst_hi.sort(reverse=True)
    worst_lo.sort()
    print(f"== {path}: {len(ws)} texts")
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
    stretched = []
    if full:
        # every cluster of the vectors and the text, and the conjuncts
        cs = set()
        for w in [("".join(cl)) for cl, _, _ in vectors()] + TEXT.split() + sample_lines + words():
            rs, i = list(w), 0
            while i < len(rs):
                j = cluster_end(rs, i)
                c = "".join(rs[i:j])
                if any(is_devanagari(ch) and not is_mark(ch) for ch in c):
                    cs.add(c)
                i = j
        res = sorted(((stretch(f, c, band), c) for c in cs), reverse=True)
        # (a simple cluster is not widened: a narrow one, र, stands in its
        # cell as a narrow Latin letter does)
        res = [(s_, c) for s_, c in res if width(c) == 2]
        stretched = [(s, c) for s, c in res if s > STRETCH_MAX]
        print(f"  stretched headline (pads > {STRETCH_MAX} units): {len(stretched)}; longest " +
              ", ".join(f"{c} {s}" for s, c in res[:8]))
    gapped = []
    for w in TEXT.split():
        gaps = headline_gaps(f, w, band)
        if gaps:
            gapped.append(f"{w}{gaps}")
    print(f"  headline gaps in the text's words: {len(gapped)} " + " ".join(gapped))
    return not bad and not circles and not stretched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fonts", nargs="+")
    ap.add_argument("--sample", action="append", default=[],
                    help="a text whose Devanagari words are checked too (sample.hi-Deva.fountain)")
    ap.add_argument("--quick", action="store_true", help="leave out the stretched-headline scan")
    args = ap.parse_args()
    nv = check_vectors()
    print(f"Lekhan width against {VECTORS}: {nv} vectors wrong")
    sample = []
    for s in args.sample:
        for line in open(s, encoding="utf-8"):
            for w in line.split():
                if any(is_devanagari(ch) for ch in w):
                    sample.append(w)
    ok = all([check(p, sorted(set(sample)), not args.quick) for p in args.fonts])
    sys.exit(0 if ok and not nv else 1)


if __name__ == "__main__":
    main()
