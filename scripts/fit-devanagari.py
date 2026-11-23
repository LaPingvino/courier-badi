#!/usr/bin/env python3
"""Fit the imported Devanagari (scripts/import-devanagari.py) to Courier Badi.

Cells: Lekhan monospace (docs/LEKHAN.md). A Devanagari cluster takes one
cell, 1228 (UPM 2048), or, a conjunct (two or more consonants joined by the
virama: क्ष त्न स्क्री र्य), two, 2456: as many as Accolade and Lexington
count by the Lekhan width (lexington/lekhan). The cluster is drawn as the
donor draws it, its own proportional glyphs where its shaping puts them,
then scaled across to fill its cells: a simple cluster condensed when it is
wider than its cell (का, कौ, औ), a conjunct condensed or widened to its two
cells (क्ष widened, स्क्री condensed), the stems kept at the Latin's 150.
What is left over, at most a step of the scale, is shared out before and
after it as headline.

How a cluster finds its width. HarfBuzz (and go-text, its Go port) applies
the Indic presentation features (pres ... psts) one syllable at a time, and
a syllable is a cluster. The lookups at the end of psts, after all of the
donor's, work out each syllable's width from its glyphs:
  - every spacing glyph advances by its donor advance (scaled, rounded to a
    step Q = 76, a sixteenth of a cell less 12/16; GPOS dist: hmtx stays
    1228 / 0 for the monospace checks and renderers without GPOS);
  - LekIns puts a start mark (lekS) before the syllable's first glyph and a
    counter mark after each spacing glyph (acc.wN: its width in steps) and
    each glyph that stands for a consonant (kc.N, its consonants: a half
    form 1, क्ष 2, reph 1);
  - LekK, a reverse chaining lookup, counts the consonants from the end to
    the start: lekS.t1 (one cell) or lekS.t2 (two or more: two cells);
  - LekSum adds the widths up from the start (the counters turn into what
    is left of the cells: s1.N / s2.N), LekLast marks the last, LekLevel
    turns it into a scale level, LekLevelBack (reverse) gives it to every
    counter, LekScale swaps each spacing glyph for its variant at that level
    (kaDeva.w9: drawn at 1.4), LekReset gives the counters the new widths;
  - LekSum2 / LekLast2 add up again, LekBack (reverse) takes what is left
    back to the start, LekPads turns lekS into the pad before the cluster
    (lead.N, half of it) and the last counter into the pad after it
    (trail1.N / trail2.N: the other half, plus the 12 / 24 the steps leave),
    the other counters into lekZ (nothing).
So a cluster is exactly one or two cells, whatever its glyphs. The pads are
marks (GDEF), so marks after a glyph still attach to it; inside a word they
carry the headline (calt: LekPadHead, when the glyphs on both sides have
one at that edge), at a word's edges not.

Vertically (the 12 pt screenplay line: baseline 1628 under the line's top,
399 above its bottom): the donor is scaled so its headline top (622) is at
HEAD = 1000 (x-height 924, cap height 1187; Hebrew 1086); below Y_KNEE the
depth is scaled by K_BELOW, so the vowel signs under the letter (ु ू ृ,
halant, rakar) end above -399; the strokes there are grown back vertically.
The donor instance (wght 475) has the Latin's 150 stem at this scale; the
horizontals (headline 130) grow to the Latin's 144. Convex corners are
rounded like the Latin's terminals (fit-hebrew.py's round_corners).

Every glyph tagged "imported" is fitted and retagged "fitted"; the feature
block is fitted once ("# state: raw" -> "fitted"). Run import and fit
together; scripts/check-devanagari.py checks the cells by shaping the built
fonts, against docs/lekhan-vectors.txt.

Usage: python3 scripts/fit-devanagari.py [--ufo sources/CourierBadi-Regular.ufo]
"""
import argparse
import importlib.util
import math
import os
import re
import statistics
import unicodedata as ud

import pathops
import ufoLib2
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("fit_hebrew", os.path.join(HERE, "fit-hebrew.py"))
fit_hebrew = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fit_hebrew)
round_corners, inset_contour = fit_hebrew.round_corners, fit_hebrew.inset_contour

DEVA_KEY = "org.courierbadi.devanagari"
WIDTH_KEY = "org.courierbadi.devanagari.width"   # the advance in a cluster, for check-devanagari.py
BEGIN = "# >>> BEGIN DEVANAGARI FEATURES (scripts/import-devanagari.py, fit-devanagari.py) >>>"
END = "# <<< END DEVANAGARI FEATURES <<<"

CELL = 1228
Q, QREM = 76, 12          # CELL = 16 Q + QREM
T1, T2 = 16, 32           # one and two cells, in steps
DONOR_HEAD = 622          # the donor's headline top (ka)
HEAD = 1000               # ... here
S = HEAD / DONOR_HEAD
Y_KNEE, K_BELOW = -120, 0.78
Y_TOP_KNEE, K_ABOVE = 1460, 0.5
STEM_V, STEM_H = 150.0, 144.0
GROW_H = 7                # headline 130 -> 144

# scale levels: a cluster is drawn at the largest that fits its cells
LEVELS = {1: 0.72, 2: 0.82, 3: 0.91, 4: 1.12, 5: 1.25, 6: 1.4, 7: 1.58, 8: 1.78, 9: 2.0, 10: 2.25,
          11: 2.55, 12: 2.9}
LEVELS_T1 = [1, 2, 3]                     # a simple cluster is only condensed
LEVELS_T2 = list(LEVELS)
VMIN = {T1: -8, T2: -14}                  # what is left of the cells, at least (saturating)
CONS_TOKENS = {"reph", "rakar", "eyelashReph", "r"}


def is_consonant(cp):
    return 0x0915 <= cp <= 0x0939 or 0x0958 <= cp <= 0x095F or 0x0978 <= cp <= 0x097F


# --- reading the donor's data --------------------------------------------------

def fea_block(font):
    t = font.features.text
    return t.index(BEGIN), t.index(END)


def fea_classes(text):
    out = {}
    for m in re.finditer(r"@([\w.\-]+)\s*=\s*\[([^\]]*)\]\s*;", text):
        out[m.group(1)] = m.group(2).split()
    return out


def bounds(font, g):
    bp = BoundsPen(font)
    g.draw(bp)
    return bp.bounds


def stem(name):
    """the glyph's base name without variant suffix and script suffix"""
    base = name.split(".")[0]
    for suf in ("Deva", "Vedic", "Cinf"):
        if base.endswith(suf):
            return base[: -len(suf)]
    return base


class Info:
    def __init__(self, font, classes):
        self.font = font
        self.cps = {}
        for g in font:
            for u in g.unicodes:
                self.cps.setdefault(g.name, u)
        self.half = set(classes.get("All_HalfForms", []))
        self.cats = font.lib.get("public.openTypeCategories", {})
        self.unknown = set()

    def token_consonants(self, t):
        """how many consonants a name's token stands for (None: unknown)"""
        if t in CONS_TOKENS:
            return 1
        n = t + "Deva"
        if n in self.cps:
            return 1 if is_consonant(self.cps[n]) else 0
        if t + "aDeva" in self.cps:           # k, kh, ss: a consonant's stem
            return 1 if is_consonant(self.cps[t + "aDeva"]) else 0
        if t in ("nukta", "anusv", "cBindu", "heavy", "NullMark", "UI", "SAN", "MAR", "NEP") \
                or t.endswith("Matra") or t.endswith("VocMatra"):
            return 0
        return None

    def consonants(self, g):
        """the consonants a glyph stands for: what makes a cluster a conjunct"""
        if g.unicodes:
            return 1 if is_consonant(g.unicodes[0]) else 0
        n = 0
        for t in stem(g.name).split("_"):
            c = self.token_consonants(t)
            if c is None:
                self.unknown.add(g.name)
                c = 0
            n += c
        return n

    def mode(self, g):
        """mark (no advance) or spacing; spacing ones: pre (the i-matra), half,
        base, post"""
        name = g.name
        if g.unicodes and ud.category(chr(g.unicodes[0])) not in ("Mn", "Me", "Mc"):
            # a letter or a sign: spacing, also one the donor draws without
            # an advance (the caret, U+A8FA): a cluster of its own
            return "half" if name in self.half else "base"
        if self.cats.get(name) == "mark" or g.width == 0:
            return "mark"
        if g.unicodes:
            cat = ud.category(chr(g.unicodes[0]))
            if cat in ("Mn", "Me"):
                return "mark"
            if cat == "Mc":
                return "pre" if g.unicodes[0] in (0x093F, 0x094E) else "post"
            return "half" if name in self.half else "base"
        if name in self.half:
            return "half"
        first = stem(name).split("_")[0]
        cp = self.cps.get(first + "Deva")
        if cp is not None and ud.category(chr(cp)) == "Mc":
            return "pre" if cp in (0x093F, 0x094E) else "post"
        return "base"


# --- outline operations -------------------------------------------------------

def ymap(y):
    y = y * S
    if y > Y_TOP_KNEE:      # only the Vedic signs stacked high
        return Y_TOP_KNEE + (y - Y_TOP_KNEE) * K_ABOVE
    return y if y >= Y_KNEE else Y_KNEE + (y - Y_KNEE) * K_BELOW


def grow_amount(y_scaled_unmapped):
    """vertical growth at a point: the headline / horizontals' GROW_H, plus
    half of what the compression below Y_KNEE took from a ~130 stroke"""
    extra = (1 - K_BELOW) * 130 / 2
    w = min(max((Y_KNEE - y_scaled_unmapped) / 100, 0), 1)
    return GROW_H + extra * w


def transform(g):
    pre = {}
    for c in g.contours:
        for p in c.points:
            pre[id(p)] = p.y * S
            p.x, p.y = p.x * S, ymap(p.y)
    for a in g.anchors:
        a.x, a.y = a.x * S, ymap(a.y)
    for c in g.contours:
        round_corners(c)
    # grow the horizontals (per point: inset_contour with a negative dy)
    for c in g.contours:
        pts = list(c.points)
        ys = [pre.get(id(p), p.y) for p in pts]
        snapshot = [(p.x, p.y) for p in pts]
        inset_contour(c, 0, -1.0)            # unit vertical normals
        for p, (x0, y0), ys_ in zip(pts, snapshot, ys):
            ny = p.y - y0                     # = -(-1) * my
            p.x, p.y = x0, y0 + ny * grow_amount(ys_)


def shift(g, dx, dy=0):
    for c in g.contours:
        for p in c.points:
            p.x += dx
            p.y += dy
    for a in g.anchors:
        a.x += dx
        a.y += dy


def condense(g, x0, f):
    for c in g.contours:
        for p in c.points:
            p.x = x0 + (p.x - x0) * f
    for a in g.anchors:
        a.x = x0 + (a.x - x0) * f
    grow = STEM_V * (1 - f) / 2
    for c in g.contours:
        inset_contour(c, -grow, 0)


def to_path(g):
    path = pathops.Path()
    g.draw(path.getPen())
    return path


class CubicPen:
    """passes a path on with its quadratic segments raised to cubics (pathops
    can emit quadratics; the masters' remove-overlaps takes cubics only)"""

    def __init__(self, pen):
        self.pen, self.cur = pen, None

    def moveTo(self, p):
        self.pen.moveTo(p); self.cur = p

    def lineTo(self, p):
        self.pen.lineTo(p); self.cur = p

    def curveTo(self, *pts):
        self.pen.curveTo(*pts); self.cur = pts[-1]

    def qCurveTo(self, *pts):
        from fontTools.pens.basePen import decomposeQuadraticSegment
        if pts[-1] is None:
            raise ValueError("closed quadratic contour")
        for a, b in decomposeQuadraticSegment(pts):
            p0 = self.cur
            c1 = (p0[0] + 2 / 3 * (a[0] - p0[0]), p0[1] + 2 / 3 * (a[1] - p0[1]))
            c2 = (b[0] + 2 / 3 * (a[0] - b[0]), b[1] + 2 / 3 * (a[1] - b[1]))
            self.pen.curveTo(c1, c2, b)
            self.cur = b

    def closePath(self):
        self.pen.closePath()

    def endPath(self):
        self.pen.endPath()

    def addComponent(self, *a, **k):
        self.pen.addComponent(*a, **k)


def from_path(g, path):
    g.clearContours()
    path.draw(CubicPen(g.getPen()))
    for c in g.contours:
        for p in c.points:
            p.x, p.y = round(p.x), round(p.y)


def rect(path_pen_target, x0, y0, x1, y1):
    pen = path_pen_target.getPen()
    pen.moveTo((x0, y0)); pen.lineTo((x1, y0)); pen.lineTo((x1, y1)); pen.lineTo((x0, y1))
    pen.closePath()


def headline_run(path, x, top):
    """the ink run at x through the headline band, or None"""
    ys = [y for y in range(int(top + 40), int(top - 260), -2) if path.contains((x, y))]
    if not ys:
        return None
    hi = ys[0]
    lo = hi
    for y in ys[1:]:
        if y == lo - 2:
            lo = y
        else:
            break
    if not (hi > top - 40 and 90 <= hi - lo <= 220):
        return None
    return lo, hi



def edge_rects(g, width, band_top, band):
    """the headline extensions a glyph needs: (left, right), each a rectangle
    (x0, y0, x1, y1) or None, and whether its headline reaches each edge. A
    glyph with a headline reaches an edge with it, or with a stem up to it
    (ा ी ो at the right, the i-matra at the left: the headline goes on from
    the stem's top, as in a word set by hand)"""
    path = to_path(g)
    b = path.bounds
    if not b or b == (0, 0, 0, 0):
        return None, None, False, False
    x0, _, x1, _ = b
    # has a headline at all: then it belongs to a word's run of headline
    has = any(headline_run(path, x0 + (x1 - x0) * k / 8, band_top) for k in range(1, 8))
    if not has:
        return None, None, False, False

    def reaches(x):
        if headline_run(path, x, band_top):
            return True
        ys = [y for y in range(int(band_top + 40), int(band_top - 260), -2) if path.contains((x, y))]
        return bool(ys) and ys[0] > band_top - 40 and len(ys) * 2 > 220     # a stem's top
    left = right = None
    # (the rectangle is the headline band measured on ka: at the ink's
    # very edge the run is thinner, where the corner is rounded)
    def inward(x, step):
        """where, from an edge inwards, the headline (or a stem's top) is
        first met (a bowl or a tail may stand out past it), or None"""
        for d in range(12, 300, 24):
            if reaches(x + step * d):
                return x + step * d
        return None
    lx, rx = inward(x0, 1), inward(x1, -1)
    lt, rt = lx is not None, rx is not None
    if lt and lx > 2:
        left = (0, band[0], lx + 60, band[1])
    if rt and rx < width - 2:
        right = (rx - 60, band[0], width, band[1])
    return left, right, lt, rt


def with_rects(g, rects):
    path = to_path(g)
    add = pathops.Path()
    for r in rects:
        rect(add, *r)
    # a union of the two fills (adding the rectangle's contour to the path
    # would cancel where the windings oppose)
    from_path(g, pathops.op(path, add, pathops.PathOp.UNION))


def copy_glyph(font, src, name):
    if name in font:
        del font[name]
    g = font.newGlyph(name)
    g.width = src.width
    src.draw(g.getPen())
    for an in src.anchors:
        g.appendAnchor({"name": an.name, "x": an.x, "y": an.y})
    for k in (DEVA_KEY, WIDTH_KEY):
        if k in src.lib:
            g.lib[k] = src.lib[k]
    cats = font.lib.setdefault("public.openTypeCategories", {})
    if src.name in cats:
        cats[name] = cats[src.name]
    return g


# --- the fit ------------------------------------------------------------------

def num(v):
    return f"m{-v}" if v < 0 else str(v)


def steps(adv):
    return max(1, round(adv / Q))


def scaled(font, src, name, f):
    """src drawn f times as wide (from x = 0), its stems kept"""
    g = copy_glyph(font, src, name)
    for c in g.contours:
        for p in c.points:
            p.x *= f
    for an in g.anchors:
        an.x *= f
    grow = STEM_V * (1 - f) / 2
    if abs(grow) > 0.5:
        for c in g.contours:
            inset_contour(c, -grow, 0)
    return g


def empty_mark(font, name):
    if name in font:
        del font[name]
    g = font.newGlyph(name)
    g.width = 0
    g.lib[DEVA_KEY] = "lekhan"
    font.lib.setdefault("public.openTypeCategories", {})[name] = "mark"
    return g


def level_of(t, v):
    """the scale level (0: as drawn) for a cluster of t steps with v left"""
    w = t - v
    if w <= 0:
        return 0
    r = t / w
    allowed = LEVELS_T1 if t == T1 else LEVELS_T2
    best = 0 if r >= 1 else None
    for lv in allowed:
        f = LEVELS[lv]
        if f <= r and (best is None or f > (1 if best == 0 else LEVELS[best])):
            best = lv
    if best is None:
        best = min(allowed, key=lambda lv: LEVELS[lv])
    return best


def fit(font):
    a, b = fea_block(font)
    text = font.features.text[a:b]
    classes = fea_classes(text)
    info = Info(font, classes)
    todo = [g for g in font if g.lib.get(DEVA_KEY) == "imported"]
    if not todo:
        return None
    cats = font.lib.setdefault("public.openTypeCategories", {})
    for g in [g for g in font if g.lib.get(DEVA_KEY) == "lekhan"]:
        del font[g.name]

    meta = {}             # name -> [consonants, mode, donor advance (scaled), steps]
    for g in todo:
        meta[g.name] = [info.consonants(g), info.mode(g), g.width * S, 0]
    for g in todo:
        transform(g)

    # A spacing glyph without the donor's top anchors (ा ी ो ौ ः and a few
    # others) took a following mark (anusvara, candrabindu, reph) at the
    # mark's own place after the glyph's advance: it gets the anchors that
    # put the mark there, its advance's end plus the mark's attaching anchor,
    # so the mark stays where it was when the glyph is moved or scaled.
    for cls_ in ("topDeva", "candraDeva"):
        att = [an for g in todo for an in g.anchors if an.name == "_" + cls_ and meta[g.name][1] == "mark"]
        if not att:
            continue
        mx, my = statistics.median(an.x for an in att), statistics.median(an.y for an in att)
        for g in todo:
            if meta[g.name][1] in ("post", "base") and not any(an.name == cls_ for an in g.anchors):
                g.appendAnchor({"name": cls_, "x": round(meta[g.name][2] + mx), "y": round(my)})

    # the levels a glyph is drawn at: a conjunct's parts (half forms, a
    # ligature of consonants) only in two cells, a letter that is no
    # consonant (a vowel, a digit, a sign) only in one, the others in both
    levels = {}
    for g in todo:
        k, mode, adv, _ = meta[g.name]
        if mode == "mark":
            continue
        if mode == "half" or k >= 2:
            levels[g.name] = LEVELS_T2
        elif mode == "base" and k == 0:
            levels[g.name] = LEVELS_T1
        else:
            levels[g.name] = sorted(set(LEVELS_T1) | set(LEVELS_T2))
    variants = {}         # level -> [(glyph, variant)]
    for name, lvs in list(levels.items()):
        src = font[name]
        k, mode, adv, _ = meta[name]
        for lv in lvs:
            vname = f"{name}.w{lv}"
            if len(vname) > 31:          # (31 characters for legacy systems)
                vname = vname.replace("Deva", "Dv", 1)
            v = scaled(font, src, vname, LEVELS[lv])
            meta[v.name] = [k, mode, adv * LEVELS[lv], 0]
            variants.setdefault(lv, []).append((name, v.name))
            todo.append(v)
    # each in its steps, its donor advance centred in them
    for g in todo:
        k, mode, adv, _ = meta[g.name]
        if mode == "mark":
            continue
        n = steps(adv)
        meta[g.name][3] = n
        shift(g, (n * Q - adv) / 2)

    # the headline band, measured on ka
    kp = to_path(font["kaDeva"])
    kb = kp.bounds
    band = headline_run(kp, (kb[0] + kb[2]) / 2, HEAD) or (HEAD - STEM_H, HEAD + GROW_H)

    touch = {"l": set(), "r": set()}
    for g in todo:
        k, mode, adv, n = meta[g.name]
        g.width = 0 if mode == "mark" else CELL
        if mode != "mark":
            cats[g.name] = "base"       # GDEF: the counters' lookups skip it
            left, right, lt, rt = edge_rects(g, n * Q, HEAD, band)
            rects = [r for r in (left, right) if r]
            if rects:
                with_rects(g, rects)
            if lt:
                touch["l"].add(g.name)
            if rt:
                touch["r"].add(g.name)
            g.lib[WIDTH_KEY] = n * Q
        for cc in g.contours:
            for p in cc.points:
                p.x, p.y = round(p.x), round(p.y)
        for an in g.anchors:
            an.x, an.y = round(an.x), round(an.y)
        g.lib[DEVA_KEY] = "fitted"

    # the dotted circle: the donor circle's anchors mapped onto this circle
    for g in font:
        if g.lib.get(DEVA_KEY) == "anchors":
            db = g.lib.pop(DEVA_KEY + ".donorbox")
            ob = bounds(font, g)
            for an in g.anchors:
                if "Deva" in an.name:
                    an.x = round(ob[0] + (an.x - db[0]) * (ob[2] - ob[0]) / (db[2] - db[0]))
                    an.y = round(ymap(an.y))
            g.lib[DEVA_KEY] = "anchors-fitted"

    # canonical winding, overlaps removed (as normalize-winding.py does)
    for g in todo:
        if g.contours:
            path = to_path(g)
            path.simplify()
            from_path(g, path)

    marks = make_marks(font, meta, band)
    fit_features(font, info, meta, variants, touch, marks)
    return len(todo), info.unknown, meta


def make_marks(font, meta, band):
    """the counters and pads (empty marks; the pads inside a word with the
    headline, .h)"""
    wmax = max(n for k, m, a, n in meta.values() if m != "mark")
    out = {"acc": [f"acc.w{w}" for w in range(1, wmax + 1)], "kc": ["kc.1", "kc.2", "kc.3"],
           "kcs": ["kcs.1", "kcs.2"], "lekS": ["lekS", "lekS.t1", "lekS.t2"], "lekZ": ["lekZ"],
           "lv": [f"lv.{lv}" for lv in [0] + list(LEVELS)]}
    for f, t in ((1, T1), (2, T2)):
        vs = range(VMIN[t], t + 1)
        out[f"s{f}"] = [f"s{f}.{num(v)}" for v in vs]
        out[f"l{f}"] = [f"l{f}.{num(v)}" for v in vs]
        out[f"p{f}"] = [f"p{f}.{num(v)}" for v in vs]
    leads = sorted({math.floor(v / 2) for t in (T1, T2) for v in range(VMIN[t], t + 1)})
    trails = {f: sorted({v - math.floor(v / 2) for v in range(VMIN[t], t + 1)}) for f, t in ((1, T1), (2, T2))}
    out["lead"] = [f"lead.{num(v)}" for v in leads]
    out["trail1"] = [f"trail1.{num(v)}" for v in trails[1]]
    out["trail2"] = [f"trail2.{num(v)}" for v in trails[2]]
    out["adv"] = {}
    for kind in ("lead", "trail1", "trail2"):
        extra = {"lead": 0, "trail1": QREM, "trail2": 2 * QREM}[kind]
        vals = leads if kind == "lead" else trails[int(kind[-1])]
        out[kind + ".h"] = []
        for v in vals:
            n = f"{kind}.{num(v)}"
            out["adv"][n] = v * Q + extra
            if v * Q + extra > 0:
                out["adv"][n + ".h"] = v * Q + extra
                out[kind + ".h"].append((n, n + ".h"))
    for key, names in out.items():
        if key == "adv":
            continue
        for n in names:
            if isinstance(n, tuple):
                n = n[1]
                g = empty_mark(font, n)
                # drawn left of its origin, and placed (GPOS) its width on:
                # a PDF viewer (poppler, Ghostscript) leaves out the ink a
                # glyph without width has right of its origin
                w = out["adv"][n]
                add = pathops.Path()
                rect(add, -w - 20, band[0], 20, band[1])
                from_path(g, add)
            else:
                empty_mark(font, n)
    return out


def fit_features(font, info, meta, variants, touch, marks):
    a, b = fea_block(font)
    t = font.features.text
    block = t[a:b]
    if "# state: raw" not in block:
        return
    block = block.replace("# state: raw", "# state: fitted")
    # value records are in donor units
    block = re.sub(r"<(-?\d+) (-?\d+) (-?\d+) (-?\d+)>",
                   lambda m: "<%s>" % " ".join(str(round(int(v) * S)) for v in m.groups()), block)
    langs = re.findall(r"(?m)^languagesystem (deva|dev2) (\w+);", t)

    def cls(name, glyphs):
        return f"@{name} = [{' '.join(glyphs)}];\n"

    spacing = {n: m for n, m in meta.items() if m[1] != "mark"}
    base_spacing = sorted(n for n in spacing if not re.search(r"\.w\d+$", n))
    first = base_spacing + ["uni25CC"]
    allg = sorted("\\" + n for n in font.keys())
    o = ["\n# --- Lekhan monospace: cells per cluster (fit-devanagari.py) ---\n"]
    o.append(cls("LekAll", allg))
    o.append(cls("LekFirst", first))
    o.append(cls("LekAcc", marks["acc"]))
    o.append(cls("LekKc", marks["kc"]))
    o.append(cls("LekKcs", marks["kcs"]))
    o.append(cls("LekLv", marks["lv"]))
    for f in (1, 2):
        for k in ("s", "l", "p"):
            o.append(cls(f"Lek{k}{f}", marks[f"{k}{f}"]))
    o.append(cls("LekSums", marks["s1"] + marks["s2"]))
    o.append(cls("LekKSet", ["lekS"] + marks["kc"] + marks["kcs"]))
    o.append(cls("LekSumSet", ["lekS.t1", "lekS.t2"] + marks["acc"] + marks["s1"] + marks["s2"]))
    o.append(cls("LekLvSet", marks["s1"] + marks["s2"] + marks["lv"]))
    o.append(cls("LekBackSet", ["lekS.t1", "lekS.t2"] + [n for f in (1, 2) for k in "slp" for n in marks[f"{k}{f}"]]))

    # insert the start and the counters
    o.append("lookup LekInsStartSub {\n" + "".join(f"    sub {n} by lekS {n};\n" for n in first)
             + "} LekInsStartSub;\n\n")
    o.append("lookup LekInsStart {\n    lookupflag 0;\n    ignore sub @LekAll @LekFirst';\n"
             "    sub @LekFirst' lookup LekInsStartSub;\n} LekInsStart;\n\n")
    ins = []
    for n in first:
        k, mode, adv, w = meta.get(n, [0, "base", CELL, T1])
        kc = f" kc.{min(k, 3)}" if k > 0 else ""
        ins.append(f"    sub {n} by {n} acc.w{w}{kc};\n")
    for n, (k, mode, adv, w) in sorted(meta.items()):
        if mode == "mark" and k > 0:
            ins.append(f"    sub {n} by {n} kc.{min(k, 3)};\n")
    o.append("lookup LekInsAcc {\n" + "".join(ins) + "} LekInsAcc;\n\n")

    # one cell or two: the consonants, counted from the end (reverse)
    flags_k = "    lookupflag IgnoreBaseGlyphs UseMarkFilteringSet @LekKSet;\n"
    o.append("lookup LekK {\n" + flags_k +
             "    rsub kc.1' kcs.1 by kcs.2;\n    rsub kc.1' kcs.2 by kcs.2;\n"
             "    rsub [kc.2 kc.3]' [kcs.1 kcs.2] by kcs.2;\n"
             "    rsub kc.1' by kcs.1;\n    rsub [kc.2 kc.3]' by kcs.2;\n"
             "    rsub lekS' kcs.2 by lekS.t2;\n    rsub lekS' by lekS.t1;\n} LekK;\n\n")
    o.append("lookup LekKDone {\n" + "".join(f"    sub {n} by lekZ;\n" for n in marks["kc"] + marks["kcs"])
             + "} LekKDone;\n\n")

    # the widths added up from the start: what is left of the cells
    for f, tt in ((1, T1), (2, T2)):
        for v in range(VMIN[tt], tt + 1):
            o.append(f"lookup LekTo{f}_{num(v)} {{\n    sub @LekAcc by s{f}.{num(v)};\n}} LekTo{f}_{num(v)};\n")
    o.append("\n")
    wmax = len(marks["acc"])

    def sum_lookup(name):
        r = [f"lookup {name} {{\n    lookupflag IgnoreBaseGlyphs UseMarkFilteringSet @LekSumSet;\n"]
        for f, tt in ((1, T1), (2, T2)):
            states = [(f"lekS.t{f}", tt)] + [(f"s{f}.{num(v)}", v) for v in range(VMIN[tt], tt + 1)]
            for prev, v in states:
                for w in range(1, wmax + 1):
                    u = max(VMIN[tt], v - w)
                    r.append(f"    sub {prev} acc.w{w}' lookup LekTo{f}_{num(u)};\n")
        r.append(f"}} {name};\n\n")
        return "".join(r)

    def last_lookup(name):
        return (f"lookup {name} {{\n    lookupflag IgnoreBaseGlyphs UseMarkFilteringSet @LekSumSet;\n"
                "    ignore sub @LekSums' @LekSums;\n"
                "    sub @Leks1' by @Lekl1;\n    sub @Leks2' by @Lekl2;\n"
                f"}} {name};\n\n")
    o.append(sum_lookup("LekSum"))
    o.append(last_lookup("LekLast"))
    # the scale level, from the last counter back to every counter
    lv = []
    for f, tt in ((1, T1), (2, T2)):
        for v in range(VMIN[tt], tt + 1):
            lv.append(f"    sub l{f}.{num(v)} by lv.{level_of(tt, v)};\n")
    o.append("lookup LekLevel {\n" + "".join(lv) + "} LekLevel;\n\n")
    o.append("lookup LekLevelBack {\n    lookupflag IgnoreBaseGlyphs UseMarkFilteringSet @LekLvSet;\n"
             + "".join(f"    rsub @LekSums' lv.{n} by lv.{n};\n" for n in [0] + list(LEVELS))
             + "} LekLevelBack;\n\n")
    sc = ["lookup LekScale {\n    lookupflag UseMarkFilteringSet @LekLv;\n"]
    for lvl, pairs in sorted(variants.items()):
        ins_, outs = [p[0] for p in pairs], [p[1] for p in pairs]
        o.append(cls(f"LekIn{lvl}", ins_))
        o.append(cls(f"LekOut{lvl}", outs))
        sc.append(f"    sub @LekIn{lvl}' lv.{lvl} by @LekOut{lvl};\n")
    sc.append("} LekScale;\n\n")
    o.append("".join(sc))
    widths = {}
    for n, (k, mode, adv, w) in spacing.items():
        widths.setdefault(w, []).append(n)
    widths.setdefault(T1, []).append("uni25CC")
    rs = ["lookup LekReset {\n    lookupflag UseMarkFilteringSet @LekLv;\n"]
    for w, gl in sorted(widths.items()):
        o.append(cls(f"LekW{w}", sorted(gl)))
        rs.append(f"    sub @LekW{w} @LekLv' by acc.w{w};\n")
    rs.append("} LekReset;\n\n")
    o.append("".join(rs))
    o.append(sum_lookup("LekSum2"))
    o.append(last_lookup("LekLast2"))
    # what is left, back to the start: half before the cluster, half after
    bk = ["lookup LekBack {\n    lookupflag IgnoreBaseGlyphs UseMarkFilteringSet @LekBackSet;\n"]
    for f, tt in ((1, T1), (2, T2)):
        for v in range(VMIN[tt], tt + 1):
            ctx = f"[l{f}.{num(v)} p{f}.{num(v)}]"
            bk.append(f"    rsub @Leks{f}' {ctx} by p{f}.{num(v)};\n")
            bk.append(f"    rsub lekS.t{f}' {ctx} by lead.{num(math.floor(v / 2))};\n")
    bk.append("} LekBack;\n\n")
    o.append("".join(bk))
    pads = []
    for f, tt in ((1, T1), (2, T2)):
        for v in range(VMIN[tt], tt + 1):
            pads.append(f"    sub l{f}.{num(v)} by trail{f}.{num(v - math.floor(v / 2))};\n")
            pads.append(f"    sub p{f}.{num(v)} by lekZ;\n")
    o.append("lookup LekPads {\n" + "".join(pads) + "} LekPads;\n\n")

    o.append("feature psts {\n" + "".join(f"    lookup {n};\n" for n in (
        "LekInsStart", "LekInsAcc", "LekK", "LekKDone", "LekSum", "LekLast", "LekLevel", "LekLevelBack",
        "LekScale", "LekReset", "LekSum2", "LekLast2", "LekBack", "LekPads")) + "} psts;\n\n")

    # the pads' headline inside a word (across syllables: calt)
    tr = [p for k in ("trail1.h", "trail2.h") for p in marks[k]]
    ld = marks["lead.h"]
    o.append(cls("LekTouchL", sorted(touch["l"])))
    o.append(cls("LekTouchR", sorted(touch["r"])))
    o.append(cls("LekTrailIn", [p[0] for p in tr]))
    o.append(cls("LekTrailOut", [p[1] for p in tr]))
    o.append(cls("LekLeadIn", [p[0] for p in ld]))
    o.append(cls("LekLeadOut", [p[1] for p in ld]))
    o.append(cls("LekTrails", marks["trail1"] + marks["trail2"] + [p[1] for p in tr]))
    o.append(cls("LekLeads", marks["lead"] + [p[1] for p in ld]))
    o.append(cls("LekPadSet", marks["trail1"] + marks["trail2"] + marks["lead"] + [p[1] for p in tr + ld]))
    o.append("lookup LekPadHead {\n    lookupflag UseMarkFilteringSet @LekPadSet;\n"
             "    sub @LekTouchR @LekTrailIn' @LekLeads @LekTouchL by @LekTrailOut;\n"
             "    sub @LekTouchR @LekTrails @LekLeadIn' @LekTouchL by @LekLeadOut;\n} LekPadHead;\n\n")
    o.append("feature calt {\n    lookup LekPadHead;\n} calt;\n\n")

    # GPOS: each glyph's advance in its cluster, the pads'
    adv = {}
    for n, (k, mode, a_, w) in spacing.items():
        d = w * Q - CELL
        if d:
            adv.setdefault(d, []).append(n)
    adv.setdefault(T1 * Q - CELL, []).append("uni25CC")
    pads = {}
    for n, d in marks["adv"].items():
        if d:
            pads.setdefault(d, []).append(n)
    o.append("lookup LekAdvance {\n")
    for d, gl in sorted(adv.items()):
        o.append(f"    pos [{' '.join(sorted(gl))}] <0 0 {d} 0>;\n")
    for d, gl in sorted(pads.items()):       # (a pad's headline is drawn left of its origin)
        o.append(f"    pos [{' '.join(sorted(gl))}] <{d} 0 {d} 0>;\n")
    o.append("} LekAdvance;\n\n")
    # only where the Indic shaper puts the pads: a Devanagari glyph in
    # another script's run (a danda in Latin) keeps its cell
    regs = []
    for script in ("deva", "dev2"):
        regs.append(f"    script {script};\n    language dflt;\n    lookup LekAdvance;\n")
        for s_, lang in langs:
            if s_ == script and lang != "dflt":
                regs.append(f"    language {lang};\n")
    o.append("feature dist {\n" + "".join(regs) + "} dist;\n\n")
    block = block.rstrip() + "\n" + "".join(o)
    font.features.text = t[:a] + block + t[b:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    args = ap.parse_args()
    font = ufoLib2.Font.open(args.ufo)
    res = fit(font)
    if res is None:
        print(f"{args.ufo}: nothing to fit (run import-devanagari.py first)")
        return
    n, unknown, meta = res
    font.save()
    from collections import Counter
    cnt = Counter(m[1] for m in meta.values())
    print(f"{args.ufo}: fitted {n} Devanagari glyphs (with their scaled variants); modes {dict(cnt)}")
    if unknown:
        print("consonants guessed (0) for:", " ".join(sorted(unknown)))


if __name__ == "__main__":
    main()
