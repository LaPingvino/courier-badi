#!/usr/bin/env python3
"""Fit the imported Devanagari (scripts/import-devanagari.py) to Courier Badi.

Cells. Courier Badi is a strict monospace: every glyph advances 1228 (UPM
2048) or, a combining mark, 0. Accolade and Lexington give a character one
cell, a combining mark (Mn/Me) and a joiner none, so a Devanagari cluster has
as many cells as it has letters, spacing vowel signs (Mc: ा ि ी ो ौ ः) and
other spacing characters: N cells. The donor's shaping gives the cluster its
own (proportional) glyphs; each glyph g here is drawn over c(g) cells, the
characters it stands for that take a cell: a consonant or a half form 1, a
conjunct of two consonants (क्ष, द्ध, त्र) 2, reph and rakar (र्, ्र: a
consonant drawn as a mark) 1, a vowel sign or other mark 0. So the shaped
cluster is N cells wide, whatever ligatures the donor makes.
  - hmtx stays 1228 / 0 (fontbakery's monospace checks; a renderer without
    GPOS still steps 1228 per spacing glyph); the cells past the first come
    from GPOS: a 'dist' lookup adds 1228 x (c - 1) to a multi-cell glyph and
    1228 to NullMark.cell, the cell of a reph or rakar.
  - Within its cells a glyph is placed by what it joins: a consonant (or
    conjunct) centred; a half form against its cell's right edge, so it
    meets the consonant after it; the i-matra (pre-base) against its right
    edge too; the post-base signs (ा ी ो ौ ः) against their left edge,
    beside the consonant. A multi-cell conjunct moves (DevaPackSub: .pr, .pl) to
    the sign it goes with. Reph and rakar stay marks placed by their
    anchors, as in the donor; their cell is a NullMark.cell (a headline, no
    more) that a psts lookup puts after them. A spacing glyph without the
    donor's top anchors (ा ी ो ौ) gets them where the donor's mark fell
    after its advance, so ं ँ and reph sit on it.
  - The headline (shirorekha) of every glyph that has one is extended to the
    edges of its cells, so a word's headline runs unbroken over the empty part
    of a cell; .init/.fina/.isol forms without the stub at a word's edges.
  - The i-matra's hook must reach the consonant after it, over as many cells
    as the following half forms and consonant take: the donor's 15 width
    variants are replaced, after all of its own substitutions, by variants
    reaching the consonant (`iMatraDeva.q7` ...), the hook stretched in its
    middle (the tail and any reph / anusvara on it moved rigidly).
  - The donor turns a reph after an i-matra into part of the i-matra glyph
    and the reph into NullMark; here the reph becomes NullMark.cell, which
    keeps the reph's cell (after the consonant) and its headline.
  - A letter wider than its cells (आ, औ, ऋ, ॐ ...) is condensed into them, its
    vertical stems grown back to the stroke.

Vertically (the 12 pt screenplay line: baseline 1628 under the line's top,
399 above its bottom): the donor is scaled so its headline top (622) is at
HEAD = 1000 (x-height 924, cap height 1187; Hebrew 1086), which also makes a
consonant about one cell wide; below Y_KNEE the depth is scaled by K_BELOW,
so the vowel signs under the letter (ु ू ृ, halant, rakar) end above -399;
the strokes there are grown back vertically. The donor instance (wght 475)
has the Latin's 150 stem at this scale; the horizontals (headline 130) grow
to the Latin's 144. Convex corners are rounded like the Latin's terminals
(fit-hebrew.py's round_corners).

Every glyph tagged "imported" is fitted and retagged "fitted"; the feature
block is fitted once ("# state: raw" -> "fitted"). Run import and fit
together; scripts/check-devanagari.py verifies the cells by shaping the
built fonts.

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
CELLS_KEY = "org.courierbadi.devanagari.cells"   # c(g), for check-devanagari.py
BEGIN = "# >>> BEGIN DEVANAGARI FEATURES (scripts/import-devanagari.py, fit-devanagari.py) >>>"
END = "# <<< END DEVANAGARI FEATURES <<<"

CELL = 1228
DONOR_HEAD = 622          # the donor's headline top (ka)
HEAD = 1000               # ... here
S = HEAD / DONOR_HEAD
Y_KNEE, K_BELOW = -120, 0.78
Y_TOP_KNEE, K_ABOVE = 1460, 0.5
STEM_V, STEM_H = 150.0, 144.0
GROW_H = 7                # headline 130 -> 144
TARGET_IN = 1028          # where the i-matra's hook meets a consonant, in its last cell
TAIL = 330                # the i-matra hook's end, moved rigidly when stretched
MAX_K = 5
IMATRA_FAMILIES = ["iMatraDeva", "iMatra_anusvDeva", "iMatra_cBinduDeva",
                   "iMatra_rephDeva", "iMatra_reph_anusvDeva", "iMatra_reph_cBinduDeva"]
SPECIAL_CELLS = {"reph": 1, "rakar": 1, "eyelashReph": 1, "r": 1, "nukta": 0, "anusv": 0,
                 "cBindu": 0, "heavy": 0, "NullMark": 0}


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

    def cp_of(self, name):
        if name in self.cps:
            return self.cps[name]
        base = name.split(".")[0]
        return self.cps.get(base)

    def token_cells(self, t):
        if t in SPECIAL_CELLS:
            return SPECIAL_CELLS[t]
        n = t + "Deva"
        if n in self.cps:
            return 0 if ud.category(chr(self.cps[n])) in ("Mn", "Me") else 1
        if n in self.half or n in self.font:
            return 1
        if t + "aDeva" in self.cps:      # tt, ng, ddh: a consonant's stem
            return 1
        return None

    def cells(self, g):
        name = g.name
        if name == "NullMark.cell":
            return 1
        cp = self.cp_of(name)
        if g.unicodes:
            return 0 if ud.category(chr(g.unicodes[0])) in ("Mn", "Me") else 1
        toks = stem(name).split("_")
        if self.cats.get(name) == "mark" or g.width == 0:
            return 1 if any(t in ("reph", "rakar") for t in toks) and toks[0] != "iMatra" else 0
        if toks[0] == "iMatra":
            return 1      # its reph's cell is NullMark.cell's
        if cp is not None and len(toks) == 1:
            return 0 if ud.category(chr(cp)) in ("Mn", "Me") else 1
        n = 0
        for t in toks:
            c = self.token_cells(t)
            if c is None:
                self.unknown.add(name)
                return 1
            n += c
        return max(n, 1)

    def mode(self, g, c):
        name = g.name
        if g.unicodes:          # an encoded glyph: its character decides
            cat = ud.category(chr(g.unicodes[0]))
            if cat in ("Mn", "Me"):
                return "mark"
            if cat == "Mc":
                return "pre" if g.unicodes[0] in (0x093F, 0x094E) else "post"
            return "half" if name in self.half else "base"
        if self.cats.get(name) == "mark" or g.width == 0:
            if name == "NullMark.cell":
                return "cellmark"
            # reph, rakar (and their ligatures with marks): marks placed by
            # their anchors as in the donor; their cell is a NullMark.cell
            # put after them (DevaCellAfter)
            return "cellafter" if c >= 1 else "mark"
        if name in self.half:
            return "half"
        first = stem(name).split("_")[0]
        cp = self.cps.get(first + "Deva")
        if cp is None and g.unicodes:
            cp = g.unicodes[0]
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
    (x0, y0, x1, y1) or None, and whether its headline reaches each edge"""
    path = to_path(g)
    b = path.bounds
    if not b or b == (0, 0, 0, 0):
        return None, None, False, False
    x0, _, x1, _ = b
    left = right = None
    ltouch = rtouch = False
    run = headline_run(path, x0 + 12, band_top)
    # (the rectangle is the headline band measured on ka: at the ink's
    # very edge the run is thinner, where the corner is rounded)
    if run and x0 > 2:
        left = (0, band[0], x0 + 60, band[1])
    run = headline_run(path, x1 - 12, band_top)
    if run and x1 < width - 2:
        right = (x1 - 60, band[0], width, band[1])
    # has a headline at all: then it belongs to a word's run of headline
    has = any(headline_run(path, x0 + (x1 - x0) * k / 8, band_top) for k in range(1, 8))
    return left, right, has or bool(left or right), has or bool(left or right)


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
    for k in (DEVA_KEY, CELLS_KEY):
        if k in src.lib:
            g.lib[k] = src.lib[k]
    cats = font.lib.setdefault("public.openTypeCategories", {})
    if src.name in cats:
        cats[name] = cats[src.name]
    return g


# --- the fit ------------------------------------------------------------------

def imatra_targets(font, classes):
    """base glyph -> where (x, donor units, from its origin) the donor's
    i-matra variant for it ends its hook"""
    adv = font["iMatraDeva"].width
    out = {}
    for cname, members in classes.items():
        m = re.fullmatch(r"Short-iMatra_(\d\d)_Bases", cname)
        if not m:
            continue
        v = f"iMatraDeva.{m.group(1)}"
        xmax = bounds(font, font[v])[2]
        for b in members:
            out.setdefault(b, xmax - adv)
    return out


def imatra_family_members(font, fam):
    return [g for g in font if g.name == fam or (g.name.startswith(fam + ".")
            and re.fullmatch(r"\.\d\d", g.name[len(fam):]))]


def fit(font):
    a, b = fea_block(font)
    text = font.features.text[a:b]
    classes = fea_classes(text)
    info = Info(font, classes)
    targets = imatra_targets(font, classes)        # donor units, before the fit
    todo = [g for g in font if g.lib.get(DEVA_KEY) == "imported"]
    if not todo:
        return None
    cats = font.lib.setdefault("public.openTypeCategories", {})

    # NullMark.cell: a reph's cell after an i-matra took the reph's drawing
    nm = font.newGlyph("NullMark.cell") if "NullMark.cell" not in font else font["NullMark.cell"]
    nm.width = 0
    nm.lib[DEVA_KEY] = "imported"
    cats["NullMark.cell"] = "mark"
    if nm not in todo:
        todo.append(nm)

    meta = {}
    for g in todo:
        c = info.cells(g)
        meta[g.name] = [c, info.mode(g, c), g.width * S]
    for g in todo:
        transform(g)

    # place each glyph in its cells
    target_x = {}          # base glyph -> where the i-matra's hook should end
    slack = {}             # multi-cell consonant -> its (left, right) room in its cells
    ends = {}              # spacing glyph -> where its donor advance now ends
    for g in todo:
        c, mode, adv = meta[g.name]
        bb = bounds(font, g)
        if mode in ("mark", "cellmark", "cellafter") or not bb:
            continue
        x0, _, x1, _ = bb
        box = c * CELL
        f = 1.0
        if mode in ("base", "half") and x1 - x0 > box:
            f = box / (x1 - x0)
            condense(g, x0, f)
            x0, _, x1, _ = bounds(font, g)
            adv *= f
        if mode == "half":
            dx = box - x1 if x1 - adv > 0 else box - adv
        elif mode == "pre":
            dx = CELL - adv
        elif mode == "post":
            dx = 0
        else:
            dx = (box - adv) / 2
            if x0 + dx < 0 or x1 + dx > box:      # overhanging ink: centre the ink
                dx = (box - (x1 - x0)) / 2 - x0
            t = targets.get(g.name)
            # (the donor's hook end, through the same condensing and shift)
            target_x[g.name] = (x0 + (t * S - x0) * f if t is not None else x1 - 120) + dx
            if c >= 2:
                slack[g.name] = (x0 + dx, box - (x1 + dx))
                # after an i-matra (or a half form) such a consonant moves
                # left in its cells (DevaPack), so the hook reaches less far
                target_x[g.name] -= x0 + dx
        shift(g, dx)
        ends[g.name] = adv + dx

    # A multi-cell conjunct (about one cell wide in two) goes with its sign:
    # .pr against a post-base sign after it (ज्ञा), .pl against an i-matra or
    # half form before it (त्रि, स्त्र); chosen by DevaPackSub (psts).
    for name, (sl, sr) in list(slack.items()):
        src = font[name]
        for suf, d in (("pr", sr), ("pl", -sl)):
            v = copy_glyph(font, src, f"{name}.{suf}")
            shift(v, d)
            meta[v.name] = list(meta[name])
            ends[v.name] = ends[name] + d
            todo.append(v)

    # A spacing glyph without the donor's top anchors (ा ी ो ौ ः and a few
    # others) took a following mark (anusvara, candrabindu, reph) at the
    # mark's own place after the glyph's advance; it is now placed in a
    # cell, so it gets the anchors that put the mark where it was: the
    # glyph's (donor) end plus the mark's attaching anchor.
    for cls_ in ("topDeva", "candraDeva"):
        xs = [an.x for g in todo for an in g.anchors if an.name == "_" + cls_
              and meta[g.name][1] in ("mark", "cellafter")]
        ys = [an.y for g in todo for an in g.anchors if an.name == "_" + cls_
              and meta[g.name][1] in ("mark", "cellafter")]
        if not xs:
            continue
        mx, my = statistics.median(xs), statistics.median(ys)
        for g in todo:
            if meta[g.name][1] in ("post", "base") and g.name in ends \
                    and not any(an.name == cls_ for an in g.anchors):
                g.appendAnchor({"name": cls_, "x": round(ends[g.name] + mx), "y": round(my)})

    # the headline band, measured on ka
    kp = to_path(font["kaDeva"])
    kb = kp.bounds
    band = headline_run(kp, (kb[0] + kb[2]) / 2, HEAD) or (HEAD - STEM_H, HEAD + GROW_H)

    # reph, rakar and the like: a fixed place over (under) the cell before
    base_anchor = {}
    for g in todo:
        c, mode, _ = meta[g.name]
        if mode == "base" and c == 1:
            for an in g.anchors:
                if not an.name.startswith("_"):
                    base_anchor.setdefault(an.name, []).append((an.x - CELL, an.y))
    for g in todo:
        c, mode, _ = meta[g.name]
        if mode != "cellmark":
            continue
        att = [an for an in g.anchors if an.name.startswith("_")]
        if att:
            an = att[0]
            pts = base_anchor.get(an.name[1:], [])
            if pts:
                shift(g, statistics.median(p[0] for p in pts) - an.x,
                      statistics.median(p[1] for p in pts) - an.y)
            for an in att:
                g.anchors.remove(an)

    for g in todo:
        c, mode, _ = meta[g.name]
        g.width = 0 if mode in ("mark", "cellmark", "cellafter") else CELL
        for cc in g.contours:
            for p in cc.points:
                p.x, p.y = round(p.x), round(p.y)
        for an in g.anchors:
            an.x, an.y = round(an.x), round(an.y)
        g.lib[DEVA_KEY] = "fitted"
        g.lib[CELLS_KEY] = c

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

    made = make_imatra_variants(font, target_x)
    for fam, qs in made.items():
        for q, name in qs.items():
            meta[name] = [1, "pre", 0]
    edges = make_edge_variants(font, meta, band, slack)
    # canonical winding, overlaps removed (as normalize-winding.py does)
    for g in font:
        if g.lib.get(DEVA_KEY) == "fitted" and g.contours:
            path = to_path(g)
            path.simplify()
            from_path(g, path)
    fit_features(font, info, meta, made, target_x, edges, slack)
    return len(todo), edges, info.unknown, meta


QUARTER = CELL / 4


def make_imatra_variants(font, target_x):
    """i-matra family F -> {Q: glyph}: the hook ends Q quarter cells from the
    i-matra's origin (its own cell, the half forms' cells, and the consonant's
    target rounded to a quarter cell)"""
    qs = sorted({round(t / QUARTER) for t in target_x.values()})
    made = {}
    for fam in IMATRA_FAMILIES:
        variants = imatra_family_members(font, fam)
        if not variants:
            continue
        ends = sorted(((bounds(font, g)[2], g) for g in variants), key=lambda e: e[0])
        made[fam] = {}
        for Q in sorted({4 + 4 * h + q for h in range(4) for q in qs}):
            T = Q * QUARTER
            below = [e for e in ends if e[0] <= T]
            xmax, src = below[-1] if below else ends[0]
            g = copy_glyph(font, src, f"{fam}.q{Q}")
            lo, hi = CELL, xmax - TAIL          # the stem and its headline stay
            if hi > lo + 50:
                k = (T - TAIL - lo) / (hi - lo)

                def mx(x):
                    if x <= lo:
                        return x
                    if x >= hi:
                        return x + (T - xmax)
                    return lo + (x - lo) * k
                for c in g.contours:
                    for p in c.points:
                        p.x = round(mx(p.x))
                for an in g.anchors:
                    an.x = round(mx(an.x))
            font.lib["public.openTypeCategories"][g.name] = "base"
            made[fam][Q] = g.name
    return made


STUB_MIN = 150     # a shorter headline extension stays at a word's edge


def make_edge_variants(font, meta, band, slack):
    """Extend each spacing glyph's headline to its cells' edges. Where that
    adds more than STUB_MIN at an edge, also make the glyph without it, for
    a word's first (.init: no left extension) and last glyph (.fina), and
    both (.isol): a word does not start or end with a stub of headline.
    Reph's and rakar's cells get a headline of their own (.fina without)."""
    out = {"init": [], "fina": [], "isol": [], "ltouch": set(), "rtouch": set(),
           "cellfina": []}
    for name, (c, mode, _) in list(meta.items()):
        g = font[name]
        if mode == "cellmark":
            copy_glyph(font, g, name + ".fina")
            with_rects(g, [(-20, band[0], CELL, band[1])])
            out["cellfina"].append(name)
            out["ltouch"].add(name)
            out["rtouch"].add(name)
            continue
        if mode not in ("base", "half", "pre", "post"):
            continue
        replaced = mode == "pre" and re.search(r"\.\d\d$", name)   # always becomes a .q variant
        left, right, lt, rt = edge_rects(g, c * CELL, HEAD, band)
        big_l = left and left[2] - left[0] - 60 > STUB_MIN
        big_r = right and right[2] - right[0] - 60 > STUB_MIN
        if lt:
            out["ltouch"].add(name)
        if rt:
            out["rtouch"].add(name)
        plain = [r for r in (left, right) if r]
        variants = {}
        if replaced:
            pass
        elif big_l:
            variants["init"] = [r for r in (right,) if r]
        if big_r and not replaced:
            variants["fina"] = [r for r in (left,) if r]
        if big_l and big_r and not replaced:
            variants["isol"] = []
        for suf, rects in variants.items():
            v = copy_glyph(font, g, f"{name}.{suf}")
            if rects:
                with_rects(v, rects)
            out[suf].append(name)
        if plain:
            with_rects(g, plain)
    return out


def fit_features(font, info, meta, made, target_x, edges, slack):
    a, b = fea_block(font)
    t = font.features.text
    block = t[a:b]
    if "# state: raw" not in block:
        return
    block = block.replace("# state: raw", "# state: fitted")
    # value records are in donor units
    block = re.sub(r"<(-?\d+) (-?\d+) (-?\d+) (-?\d+)>",
                   lambda m: "<%s>" % " ".join(str(round(int(v) * S)) for v in m.groups()), block)
    # the reph's cell stays when an i-matra takes its drawing
    for r in ("rephDeva", "reph_anusvDeva", "reph_cBinduDeva"):
        block = block.replace(f"sub {r} by NullMark;", f"sub {r} by NullMark.cell;")
    block = block.replace("NullMark];", "NullMark NullMark.cell];")
    # र + ृ ॄ ॢ ॣ: the donor draws ऋ (ॠ ऌ ॡ) and a reph for the sign, a cell
    # more than the sign has; here they are र with the sign under it
    block = re.sub(r"(?m)^(\s*sub (raDeva' (r|rr|l|ll)VocMatraDeva by|(r|rr|l|ll)VocalicDeva "
                   r"(r|rr|l|ll)VocMatraDeva' by rephDeva))", r"#\1", block)
    block = re.sub(r"(?m)^(\s*sub \[rVocalicDeva rrVocalicDeva lVocalicDeva llVocalicDeva\] rephDeva')",
                   r"#\1", block)
    # ई stays one glyph (the donor draws it as इ + reph, a second cell)
    block = block.replace("sub iiDeva by iDeva rephDeva;", "# (iiDeva stays whole here)")

    def cls(name, glyphs):
        # in order: an In/Out pair maps position to position
        return f"@{name} = [{' '.join(glyphs)}];\n"

    out = ["\n# --- cells, i-matra, word edges (fit-devanagari.py) ---\n"]
    halves = {}
    for name, (c, mode, _) in meta.items():
        if mode == "half":
            halves.setdefault(c, []).append(name)
    bases = {}
    for name, x in target_x.items():
        bases.setdefault(round(x / QUARTER), []).append(name)
    if "uni25CC" in font:
        bases.setdefault(round((CELL - 120) / QUARTER), []).append("uni25CC")
    for c, gl in sorted(halves.items()):
        out.append(cls(f"DevaHalf{c}", gl))
    for q, gl in sorted(bases.items()):
        out.append(cls(f"DevaBaseQ{q}", gl))
    # i-matra: its hook reaches the consonant after the half forms
    import itertools
    out.append("lookup DevaIMatraCells {\n    lookupflag IgnoreMarks;\n")
    for fam, qs in made.items():
        cname = f"DevaI_{fam.replace('-', '_')}"
        members = [g.name for g in imatra_family_members(font, fam)]
        out.append(f"    @{cname} = [{' '.join(sorted(members))}];\n")
        for h in (3, 2, 1, 0):
            for hs in itertools.product(sorted(halves), repeat=h):
                for q in sorted(bases):
                    Q = 4 + 4 * sum(hs) + q
                    if Q not in qs:
                        continue
                    ctx = " ".join([f"@DevaHalf{x}" for x in hs] + [f"@DevaBaseQ{q}"])
                    out.append(f"    sub @{cname}' {ctx} by {qs[Q]};\n")
    out.append("} DevaIMatraCells;\n\n")
    # (defined before the word-edge lookups: lookups apply in this order)
    after = sorted(n for n, (c, m, _) in meta.items() if m == "cellafter")
    if after:
        out.append("lookup DevaCellAfter {\n")
        for n in after:
            out.append(f"    sub {n} by {n} NullMark.cell;\n")
        out.append("} DevaCellAfter;\n\n")

    # word edges: no headline stub before a word's first glyph or after its
    # last (a glyph is a word's first when no glyph whose headline reaches
    # its right edge comes before it)
    spacing = [n for n, (c, m, _) in meta.items() if m in ("base", "half", "pre", "post")]

    def all_forms(names):
        res = []
        for n in names:
            res.append(n)
            for suf in ("init", "fina", "isol"):
                if n in edges[suf]:
                    res.append(f"{n}.{suf}")
        return res
    # packing: a multi-cell consonant goes with its sign: .pr against a
    # post-base sign (ा ी ो ौ ः) after it, .pl against an i-matra or a half
    # form before it (after DevaIMatraCells, which measured the hook to .pl)
    packs = sorted(n for n in slack)
    if packs:
        posts = [n for n, (c, m, _) in meta.items() if m == "post"]
        pres = [n for n, (c, m, _) in meta.items() if m in ("pre", "half")]
        out.append(cls("DevaPostAll", sorted(posts)))
        out.append(cls("DevaPreHalfAll", sorted(pres)))
        out.append(cls("DevaPackIn", packs))
        out.append(cls("DevaPackR", [n + ".pr" for n in packs]))
        out.append(cls("DevaPackL", [n + ".pl" for n in packs]))
        out.append("lookup DevaPackSub {\n    lookupflag IgnoreMarks;\n"
                   "    sub @DevaPackIn' @DevaPostAll by @DevaPackR;\n"
                   "    sub @DevaPreHalfAll @DevaPackIn' by @DevaPackL;\n} DevaPackSub;\n\n")
    rt = [n for n in edges["rtouch"] if n in spacing]
    lt = [n for n in edges["ltouch"] if n in spacing]
    out.append(cls("DevaJoinsRight", all_forms(rt)))
    out.append(cls("DevaJoinsLeft", all_forms(lt)))
    for k in ("init", "fina", "isol", "cellfina"):
        edges[k] = sorted(edges[k])
    if edges["init"]:
        out.append(cls("DevaInitIn", edges["init"]))
        out.append(cls("DevaInitOut", [n + ".init" for n in edges["init"]]))
        out.append("lookup DevaWordStart {\n    lookupflag IgnoreMarks;\n"
                   "    ignore sub @DevaJoinsRight @DevaInitIn';\n"
                   "    sub @DevaInitIn' by @DevaInitOut;\n} DevaWordStart;\n\n")
    if edges["fina"]:
        both = [n for n in edges["fina"] if n in edges["isol"]]
        out.append(cls("DevaFinaIn", edges["fina"]))
        out.append(cls("DevaFinaOut", [n + ".fina" for n in edges["fina"]]))
        rules = ["    ignore sub @DevaFinaIn' @DevaJoinsLeft;\n",
                 "    sub @DevaFinaIn' by @DevaFinaOut;\n"]
        if both:
            out.append(cls("DevaIsolIn", [n + ".init" for n in both]))
            out.append(cls("DevaIsolOut", [n + ".isol" for n in both]))
            rules = ["    ignore sub @DevaFinaIn' @DevaJoinsLeft;\n",
                     "    ignore sub @DevaIsolIn' @DevaJoinsLeft;\n",
                     "    sub @DevaFinaIn' by @DevaFinaOut;\n",
                     "    sub @DevaIsolIn' by @DevaIsolOut;\n"]
        out.append("lookup DevaWordEnd {\n    lookupflag IgnoreMarks;\n" + "".join(rules)
                   + "} DevaWordEnd;\n\n")
    if edges["cellfina"]:
        cm = edges["cellfina"]
        out.append(cls("DevaCellMarks", cm + [n + ".fina" for n in cm]))
        out.append(cls("DevaCellIn", cm))
        out.append(cls("DevaCellOut", [n + ".fina" for n in cm]))
        out.append("lookup DevaCellWordEnd {\n    lookupflag UseMarkFilteringSet @DevaCellMarks;\n"
                   "    ignore sub @DevaCellIn' @DevaJoinsLeft;\n"
                   "    ignore sub @DevaCellIn' @DevaCellMarks;\n"
                   "    sub @DevaCellIn' by @DevaCellOut;\n} DevaCellWordEnd;\n\n")
    out.append("feature psts {\n" + ("    lookup DevaCellAfter;\n" if after else "")
               + "    lookup DevaIMatraCells;\n"
               + ("    lookup DevaPackSub;\n" if packs else "") + "} psts;\n\n")
    # HarfBuzz applies psts (and the other Indic features) per syllable; a
    # word's edges are found across syllables, so these are calt lookups
    out.append("feature calt {\n")
    for n in ("DevaWordStart", "DevaWordEnd", "DevaCellWordEnd"):
        if f"lookup {n} {{" in "".join(out):
            out.append(f"    lookup {n};\n")
    out.append("} calt;\n\n")

    # GPOS: the cells past the first
    multi = {}
    for name, (c, mode, _) in meta.items():
        if mode in ("base", "half", "pre", "post") and c >= 2:
            multi.setdefault(c, []).extend(all_forms([name]))
    marks = [n for n, (c, m, _) in meta.items() if m == "cellmark"]
    marks += [n + ".fina" for n in marks]
    out.append("lookup DevaCells {\n")
    for c, gl in sorted(multi.items()):
        out.append(f"    pos [{' '.join(sorted(gl))}] <0 0 {CELL * (c - 1)} 0>;\n")
    if marks:
        out.append(f"    pos [{' '.join(sorted(marks))}] <0 0 {CELL} 0>;\n")
    out.append("} DevaCells;\n\nfeature dist {\n    lookup DevaCells;\n} dist;\n\n")
    block = block.rstrip() + "\n" + "".join(out)
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
    n, edges, unknown, meta = res
    font.save()
    from collections import Counter
    cnt = Counter((m, c) for c, m, _ in meta.values())
    print(f"{args.ufo}: fitted {n} Devanagari glyphs; word-edge variants: "
          f"{len(edges['init'])} init, {len(edges['fina'])} fina, {len(edges['isol'])} isol; "
          f"modes {dict(sorted(cnt.items()))}")
    if unknown:
        print("cells guessed (1) for:", " ".join(sorted(unknown)))


if __name__ == "__main__":
    main()
