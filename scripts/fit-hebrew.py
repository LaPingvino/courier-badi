#!/usr/bin/env python3
"""Fit the imported Hebrew (scripts/import-hebrew.py) to Courier Badi.

The donor (Cousine / Liberation Mono Hebrew) is a monoline monospace already;
this brings it to Courier Badi's proportions and pen, in the same spirit as
widen-seen-family.py (geometry first, then an inset to restore the stroke):

  1. Scale: y by SY (0.888, so he/he-height = 1090 sits between x-height 924
     and cap height 1187, the donors' own Hebrew:cap ratio); x by SX (0.93)
     around the cell centre, so the widest letters (alef, shin, tet) keep a
     side bearing like W/M instead of touching the neighbouring cell. The
     donor's 1229 advance becomes 1228. Anchors go through the same map, so
     mark attachment is unchanged relative to the ink.
  2. Stroke: an inset along the contour normal (like make-bold.py's dilation,
     negative and with miter joins; needs the canonical winding the import
     produced) thins
     the vertical stems by 2*DX and the horizontals by 2*DY, to Courier Badi's
     150 / 144 (Regular). DX/DY are measured from the scaled donor, not
     guessed: vav's stem and he's roof.
  3. Terminals (done before the inset): every convex line-line corner is
     rounded like the Latin
     (the corner replaced by a short cubic, ~64 units each way, handles at
     0.72 -- cf. the corners of L). Concave corners stay sharp, as in the Latin.
  4. Marks keep advance 0 and their donor position (centred on the cell), which
     is also the sensible overlay when no GPOS is applied: in right-to-left
     text a zero-width mark is drawn from the preceding letter's origin. Their
     stroke parts get the same inset; dots (both sides < 220) keep their size.
     Top and bottom marks get mark-to-mark anchors so cantillation stacks.
  5. The presentation forms (FB1D-FB4E) are composites; their mark components
     are placed from the anchors (base anchor - mark anchor), i.e. exactly
     where the GPOS would put them, and they copy the base letter's anchors.

Only glyphs tagged "imported" are fitted; they are retagged "fitted", so the
script is idempotent (re-running it changes nothing; re-run the import to
start again). --check verifies the result numerically:
  vertical stems 150 +/- 5, horizontals 144 +/- 8, all base ink inside the
  cell, all marks advance 0, every composite's mark placed from an anchor.

Usage:
  python3 scripts/fit-hebrew.py [--ufo sources/CourierBadi-Regular.ufo] [--check]
"""
import argparse
import math
import sys
import unicodedata as ud

import ufoLib2
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.freetypePen import FreeTypePen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen

HEBREW_KEY = "org.courierbadi.hebrew"
CELL = 1228
DONOR_CENTRE = 1229 / 2
SX, SY = 0.93, 0.888
STEM_V, STEM_H = 150.0, 144.0       # Courier Badi Regular (measure: H, n, E)
CORNER, HANDLE = 64.0, 0.72         # corner rounding (cf. L.glif)
MIN_TURN = math.radians(35)         # only real corners, not shallow bends
DOT_MAX = 220                       # mark contours smaller than this are dots
STACK_GAP = 50                      # ink gap between stacked marks


def is_mark_glyph(g):
    return any(ud.category(chr(u)) in ("Mn", "Me") for u in g.unicodes)


def tx(x):
    return CELL / 2 + (x - DONOR_CENTRE) * SX


# --- measuring ----------------------------------------------------------------

Y0, X0 = 900, 300


def bitmap(font, name):
    pen = FreeTypePen(None)
    rp = DecomposingRecordingPen(font)
    font[name].draw(rp)
    rp.replay(TransformPen(pen, (1, 0, 0, 1, X0, Y0)))
    a = pen.array(width=CELL + 2 * X0, height=3000, contain=False)
    return a[::-1] > 0.5


def runs(line):
    out, s = [], None
    for i, v in enumerate(line):
        if v and s is None:
            s = i
        if not v and s is not None:
            out.append((s, i - s))
            s = None
    if s is not None:
        out.append((s, len(line) - s))
    return out


def row_runs(B, y):
    return [(a - X0, w) for a, w in runs(B[Y0 + y])]


def col_runs(B, x):
    return [(a - Y0, w) for a, w in runs(B[:, X0 + x])]


# Measuring sites: (letter, y) rows crossing only vertical stems, and
# (letter, x) columns crossing only horizontal strokes.
V_SITES = [(0x05D5, 500), (0x05D3, 500), (0x05E8, 500), (0x05D4, 300),
           (0x05DF, 300), (0x05D7, 500), (0x05EA, 500), (0x05D6, 500),
           (0x05D2, 700), (0x05DA, 300)]
H_SITES = [(0x05D4, 500), (0x05D3, 500), (0x05E8, 500), (0x05D1, 600),
           (0x05DB, 600), (0x05EA, 600), (0x05D7, 614)]


def cpname(cp):
    return "uni%04X" % cp


def measure(font):
    v, h = {}, {}
    for cp, y in V_SITES:
        v[chr(cp) + "@y%d" % y] = [w for _, w in row_runs(bitmap(font, cpname(cp)), y)]
    for cp, x in H_SITES:
        h[chr(cp) + "@x%d" % x] = [w for _, w in col_runs(bitmap(font, cpname(cp)), x)]
    return v, h


# --- fitting --------------------------------------------------------------------

def transform_glyph(g):
    for c in g.contours:
        for p in c.points:
            p.x, p.y = tx(p.x), p.y * SY
    for a in g.anchors:
        a.x, a.y = round(tx(a.x)), round(a.y * SY)


def contour_bounds(c):
    xs = [p.x for p in c.points]
    ys = [p.y for p in c.points]
    return min(xs), min(ys), max(xs), max(ys)


def is_dot(c):
    x0, y0, x1, y1 = contour_bounds(c)
    return x1 - x0 < DOT_MAX and y1 - y0 < DOT_MAX


def round_corners(contour):
    """Replace convex line-line corners by a short cubic (outer CCW / holes CW:
    the ink is always to the left, so a left turn is a convex ink corner)."""
    from ufoLib2.objects import Point
    pts = list(contour.points)
    n = len(pts)
    if n < 3:
        return 0
    out, done = [], 0
    for i, p in enumerate(pts):
        prv, nxt = pts[i - 1], pts[(i + 1) % n]
        if p.type == "line" and nxt.type == "line" and prv.type is not None:
            ix, iy = p.x - prv.x, p.y - prv.y
            ox, oy = nxt.x - p.x, nxt.y - p.y
            li, lo = math.hypot(ix, iy), math.hypot(ox, oy)
            if li > 1 and lo > 1:
                ix, iy, ox, oy = ix / li, iy / li, ox / lo, oy / lo
                cross, dot = ix * oy - iy * ox, ix * ox + iy * oy
                if cross > 0 and math.atan2(cross, dot) > MIN_TURN:
                    d = min(CORNER, 0.45 * li, 0.45 * lo)
                    ax, ay = p.x - d * ix, p.y - d * iy
                    bx, by = p.x + d * ox, p.y + d * oy
                    out += [Point(ax, ay, "line"),
                            Point(ax + HANDLE * d * ix, ay + HANDLE * d * iy),
                            Point(bx - HANDLE * d * ox, by - HANDLE * d * oy),
                            Point(bx, by, "curve")]
                    done += 1
                    continue
        out.append(Point(p.x, p.y, p.type, p.smooth))
    contour.points[:] = out
    return done


def inset_contour(contour, dx, dy):
    """Move every point inward (to the left of travel, where the ink is) by dx horizontally / dy vertically. Unlike make-bold.py's chord
    normal, a point between two differently-directed neighbours is moved to
    the intersection of the two offset lines (a miter), so the sharp corners
    the donor still has after round_corners() (concave joins, shallow bends)
    inset by the full amount instead of ~0.7 of it. Miters are capped at 2x."""
    pts = list(contour.points)
    n = len(pts)
    orig = [(p.x, p.y) for p in pts]

    def unit_normal(a, b):
        tx_, ty_ = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx_, ty_)
        if L < 1e-6:
            return None
        return ty_ / L, -tx_ / L   # right-hand normal: outward, the ink is on the left

    for i in range(n):
        p = orig[i]
        # nearest distinct neighbours on either side
        j = (i - 1) % n
        while orig[j] == p and j != i:
            j = (j - 1) % n
        k = (i + 1) % n
        while orig[k] == p and k != i:
            k = (k + 1) % n
        n1, n2 = unit_normal(orig[j], p), unit_normal(p, orig[k])
        if n1 is None or n2 is None:
            continue
        mx, my = n1[0] + n2[0], n1[1] + n2[1]
        dot = n1[0] * n2[0] + n1[1] * n2[1]
        if 1 + dot < 0.25:          # near reversal: fall back to the chord normal
            c = unit_normal(orig[j], orig[k])
            if c is None:
                continue
            mx, my = c
        else:
            mx, my = mx / (1 + dot), my / (1 + dot)
        L = math.hypot(mx, my)
        if L > 2:
            mx, my = mx * 2 / L, my * 2 / L
        pts[i].x = p[0] - dx * mx
        pts[i].y = p[1] - dy * my


def round_all(g):
    for c in g.contours:
        for p in c.points:
            p.x, p.y = round(p.x), round(p.y)


def stack_anchors(g):
    """mark-to-mark: a second top mark sits STACK_GAP above this one's ink,
    a second bottom mark STACK_GAP below."""
    names = {a.name: a for a in g.anchors}
    if not g.contours:
        return
    bp = BoundsPen(None)
    g.draw(bp)
    x0, y0, x1, y1 = bp.bounds
    for a in list(g.anchors):
        if a.name in ("top", "bottom"):
            g.anchors.remove(a)
    if "_top" in names:
        t = names["_top"]
        g.appendAnchor({"name": "top", "x": t.x, "y": round(y1 + STACK_GAP - (y0 - t.y))})
    if "_bottom" in names:
        b = names["_bottom"]
        g.appendAnchor({"name": "bottom", "x": b.x, "y": round(y0 - STACK_GAP - (y1 - b.y))})


def place_composite(font, g):
    """Base component at the origin; each mark component moved so its _anchor
    meets the base's anchor of the same class."""
    comps = list(g.components)
    base = font[comps[0].baseGlyph]
    banchors = {a.name: a for a in base.anchors}
    missing = []
    for c in comps[1:]:
        m = font[c.baseGlyph]
        ma = [a for a in m.anchors if a.name.startswith("_")]
        if not ma or ma[0].name[1:] not in banchors:
            missing.append(c.baseGlyph)
            c.transformation = (1, 0, 0, 1, 0, 0)
            continue
        cls = ma[0].name[1:]
        b = banchors[cls]
        c.transformation = (1, 0, 0, 1, b.x - ma[0].x, b.y - ma[0].y)
    comps[0].transformation = (1, 0, 0, 1, 0, 0)
    # the form takes the base letter's anchors, so further marks (a vowel
    # under a precomposed shin-with-dot, cantillation) still attach
    g.anchors.clear()
    for a in base.anchors:
        g.appendAnchor({"name": a.name, "x": a.x, "y": a.y})
    return missing


def fit(font, dx, dy):
    n = corners = 0
    for g in font:
        if g.lib.get(HEBREW_KEY) != "imported" or not g.contours:
            continue
        transform_glyph(g)
        mark = is_mark_glyph(g)
        for c in g.contours:
            if mark and is_dot(c):
                continue
            corners += round_corners(c)
            inset_contour(c, dx, dy)
        round_all(g)
        g.width = 0 if mark else CELL
        if mark:
            stack_anchors(g)
        g.lib[HEBREW_KEY] = "fitted"
        n += 1
    # dotted circle: only its (donor-height) anchors are Hebrew
    for g in font:
        if g.lib.get(HEBREW_KEY) == "anchors":
            for a in g.anchors:
                a.y = round(a.y * SY)
            g.lib[HEBREW_KEY] = "anchors-fitted"
    missing = {}
    for g in font:
        if g.lib.get(HEBREW_KEY) == "imported" and g.components and not g.contours:
            miss = place_composite(font, g)
            if miss:
                missing[g.name] = miss
            g.lib[HEBREW_KEY] = "fitted"
            n += 1
    return n, corners, missing


# --- derived glyphs and anchors (re-run on every invocation; idempotent) -----

YOD_TRIANGLE_SCALE = 0.9   # three yods in two rows must fit the letter height


def yod_triangle(font):
    """U+05EF HEBREW YOD TRIANGLE, a ligature of three yods: one on top, two
    below, each the fitted yod scaled by YOD_TRIANGLE_SCALE. Scaling thins the
    stems (150 -> 135), so it is built as outlines, not scaled components,
    and the stroke is restored with the same normal offset as the fit."""
    from fontTools.misc.transform import Transform
    yod = font[cpname(0x05D9)]
    bp = BoundsPen(font)
    yod.draw(bp)
    x0, y0, x1, y1 = bp.bounds
    s = YOD_TRIANGLE_SCALE
    h = (y1 - y0) * s
    gap = (1086 - 2 * h)              # between the rows, letter height 1086
    cx = (x0 + x1) / 2
    spread = 230                      # bottom yods' centres at 614 -/+ spread
    places = [(CELL / 2, h + gap), (CELL / 2 - spread, 0), (CELL / 2 + spread, 0)]
    name = cpname(0x05EF)
    if name in font:
        del font[name]
    g = font.newGlyph(name)
    g.unicodes = [0x05EF]
    g.width = CELL
    pen = g.getPen()
    for px, py in places:
        t = Transform().translate(px, py).scale(s).translate(-cx, -y0)
        yod.draw(TransformPen(pen, t))
    grow_x, grow_y = STEM_V * (1 - s) / 2, STEM_H * (1 - s) / 2
    for c in g.contours:
        inset_contour(c, -grow_x, -grow_y)
    round_all(g)
    # anchors: those of he (a full-width letter), minus the letter-specific
    # dagesh / shin-dot positions
    for a in font[cpname(0x05D4)].anchors:
        if a.name in ("center", "shindot", "sindot") or a.name.startswith("*"):
            continue
        if a.name.startswith(("above", "below", "attached")):
            continue  # make-mark-anchors.py owns these
        g.appendAnchor({"name": a.name, "x": a.x, "y": a.y})
    g.lib[HEBREW_KEY] = "fitted"
    return g


# Below marks that go *beside* a below vowel instead of under it (the donor's
# contextual lookups): meteg and the below cantillation marks.
VOWELS = [0x05B0, 0x05B1, 0x05B2, 0x05B3, 0x05B4, 0x05B5, 0x05B6, 0x05B7,
          0x05B8, 0x05BB, 0x05C7]
VOWEL_NUDGE = 137      # the vowel's move to the right (half the narrowest pair)
SIDE_GAP = 60          # ink gap between the vowel and the mark beside it
SIDE_TOL = 40          # vowels whose widths differ this little share a shift
CONTEXT_KEY = "GPOS_Context"   # ufo2ft contextual anchors


def is_side_mark(cp):
    return cp == 0x05BD or 0x0591 <= cp <= 0x05AF


def side_by_side(font):
    """Meteg / a below accent after a below vowel on the same letter goes
    beside the vowel, at the vowel's level, instead of under it. As in the
    donor, the pair is spread around the letter's anchor: the vowel moves
    right (VOWEL_NUDGE) and the mark left (toward the end of the word), so
    that they are separated by half the vowel's width + SIDE_GAP + half the
    median side-mark width.

    Done with ufo2ft contextual anchors, so the GPOS comes from per-master
    anchors and stays right in every master (fea written by hand would carry
    the Regular's coordinates into the Bold and Italic):
      - those marks attach through their own class `bottomacc` (bases get a
        `bottomacc` anchor equal to `bottom`), so they no longer stack under
        a vowel through mark-to-mark;
      - every base gets, per vowel-width group, a contextual anchor
        `*bottomacc.vN` (that separation - VOWEL_NUDGE to the left), with the
        context "* [vowels of group N] &", and one `*bottom.next` for the
        vowel (VOWEL_NUDGE to the right), with the context "* & [side
        marks]"; marks other than vowels and side marks are skipped by a
        mark filtering set."""
    import statistics
    from ufoLib2.objects import Anchor
    side = [g for g in font if g.unicodes and is_side_mark(g.unicodes[0])
            and g.lib.get(HEBREW_KEY) == "fitted"
            and any(a.name in ("_bottom", "_bottomacc") for a in g.anchors)]
    vowels = [font[cpname(c)] for c in VOWELS if cpname(c) in font]

    def width(g):
        bp = BoundsPen(font)
        g.draw(bp)
        return bp.bounds[2] - bp.bounds[0]

    # 1. side marks: class bottom -> bottomacc (idempotent)
    for g in side:
        for a in g.anchors:
            if a.name == "_bottom":
                a.name = "_bottomacc"
            elif a.name == "bottom":
                a.name = "bottomacc"
    half_mark = statistics.median(width(g) for g in side) / 2
    # 2. vowel groups by width
    ws = sorted((width(v), v.name) for v in vowels)
    groups = []
    for w, n in ws:
        if groups and w - groups[-1][0][0] <= SIDE_TOL:
            groups[-1].append((w, n))
        else:
            groups.append([(w, n)])
    filt = " ".join(sorted({g.name for g in side} | {v.name for v in vowels}))
    # 3. base anchors
    n = 0
    for g in font:
        if is_mark_glyph(g):
            continue
        objlibs = g.lib.get("public.objectLibs", {})
        for a in list(g.anchors):
            if a.name == "bottomacc" or a.name.startswith(("*bottomacc", "*bottom.")):
                if a.identifier:
                    objlibs.pop(a.identifier, None)
                g.anchors.remove(a)
        bottom = [a for a in g.anchors if a.name == "bottom"]
        if not bottom:
            continue
        b = bottom[0]
        g.appendAnchor({"name": "bottomacc", "x": b.x, "y": b.y})
        ctx = f"lookupflag UseMarkFilteringSet [{filt}];"
        ident = f"side-{g.name}-next"
        g.anchors.append(Anchor(x=round(b.x + VOWEL_NUDGE), y=b.y,
                                name="*bottom.next", identifier=ident))
        objlibs[ident] = {CONTEXT_KEY: ctx + "* & [" + " ".join(sorted(x.name for x in side)) + "]"}
        for i, grp in enumerate(groups):
            wv = sum(w for w, _ in grp) / len(grp)
            shift = wv / 2 + SIDE_GAP + half_mark - VOWEL_NUDGE
            ident = f"side-{g.name}-v{i}"
            g.anchors.append(Anchor(x=round(b.x - shift), y=b.y,
                                    name=f"*bottomacc.v{i}", identifier=ident))
            objlibs[ident] = {CONTEXT_KEY: ctx + f"* [{' '.join(nm for _, nm in grp)}] &"}
        if objlibs:
            g.lib["public.objectLibs"] = objlibs
        n += 1
    return n, len(groups)


# The dagesh is drawn larger than the vowel points (148, the stroke's width):
# at 12 pt a 148-unit dot is 0.3 mm and all but vanished in yod (beside it)
# and lamed (in its open bowl), and inside bet, kaf, pe it is only as heavy as
# the strokes around it. DAGESH units across, scaled about its own anchor, so
# every placement (GPOS and the presentation forms) is kept.
DAGESH = 184


def dagesh_size(font):
    dag = font[cpname(0x05BC)]
    b = bounds(font, dag)
    k = DAGESH / (b[2] - b[0])
    if abs(k - 1) < 1e-3:
        return
    a = next(a for a in dag.anchors if a.name == "_center")
    for c in dag.contours:
        for p in c.points:
            p.x = a.x + (p.x - a.x) * k
            p.y = a.y + (p.y - a.y) * k


# Dagesh in yod: beside the letter at its height, as the donor's own
# precomposed U+FB39 draws it (its ink 88 units left of the yod's, its centre
# at 0.454 of the yod's height, once fitted). The donor's GPOS puts it under
# the yod, where it reads as "!"; that is where the import took the anchor
# from (the GPOS wins over the composition there).
YOD_DAGESH_GAP = 72   # (88 in the donor; a little closer, so it is read with the yod)
YOD_DAGESH_HEIGHT = 0.454


def yod_dagesh(font):
    yod, dag = font[cpname(0x05D9)], font[cpname(0x05BC)]
    yb, db = (bounds(font, g) for g in (yod, dag))
    da = next(a for a in dag.anchors if a.name == "_center")
    x = yb[0] - YOD_DAGESH_GAP - (db[2] - db[0]) / 2 + (da.x - (db[0] + db[2]) / 2)
    y = yb[1] + YOD_DAGESH_HEIGHT * (yb[3] - yb[1]) + (da.y - (db[1] + db[3]) / 2)
    for g in (yod, font[cpname(0xFB39)]):
        for a in g.anchors:
            if a.name == "center":
                a.x, a.y = round(x), round(y)
    form = font[cpname(0xFB39)]
    for c in form.components[1:]:
        if c.baseGlyph == dag.name:
            c.transformation = (1, 0, 0, 1, round(x) - da.x, round(y) - da.y)


def bounds(font, g):
    bp = BoundsPen(font)
    g.draw(bp)
    return bp.bounds


def derive(font):
    yod_triangle(font)
    dagesh_size(font)
    yod_dagesh(font)
    n, ng = side_by_side(font)
    print(f"derived: U+05EF yod triangle; dagesh {DAGESH} across, beside yod; side-by-side anchors on {n} bases "
          f"({ng} vowel-width groups)")


def scaled_stems(font):
    """Stem widths of the scaled (not yet thinned) donor, to derive the inset."""
    tmp = ufoLib2.Font()
    for cp in (0x05D5, 0x05D4):
        src = font[cpname(cp)]
        g = tmp.newGlyph(src.name)
        g.width = CELL
        src.draw(g.getPen())
        transform_glyph(g)
    vav = [w for _, w in row_runs(bitmap(tmp, cpname(0x05D5)), 500)]
    he = [w for _, w in col_runs(bitmap(tmp, cpname(0x05D4)), 500)]
    return vav[0], he[-1]


def check(font):
    ok = True
    v, h = measure(font)
    print("vertical stems (target %d +/- 5):" % STEM_V)
    for k, ws in v.items():
        bad = [w for w in ws if abs(w - STEM_V) > 5]
        ok &= not bad
        print(f"  {k:10s} {ws}{'  <-- off' if bad else ''}")
    print("horizontal strokes (target %d +/- 8):" % STEM_H)
    for k, ws in h.items():
        bad = [w for w in ws if abs(w - STEM_H) > 8]
        ok &= not bad
        print(f"  {k:10s} {ws}{'  <-- off' if bad else ''}")
    heb = [g for g in font if g.lib.get(HEBREW_KEY) == "fitted"]
    out_of_cell, bad_width, marks = [], [], 0
    for g in heb:
        mark = is_mark_glyph(g)
        if mark:
            marks += 1
            if g.width != 0:
                bad_width.append(g.name)
        elif g.width != CELL:
            bad_width.append(g.name)
        bp = BoundsPen(font)
        g.draw(bp)
        if bp.bounds and (bp.bounds[0] < 0 or bp.bounds[2] > CELL):
            out_of_cell.append((g.name, [round(v) for v in bp.bounds]))
    ok &= not out_of_cell and not bad_width
    print(f"glyphs: {len(heb)} Hebrew, {marks} marks (advance 0), "
          f"bad advance: {bad_width or 'none'}")
    print(f"ink outside the cell [0,{CELL}]: {out_of_cell or 'none'}")
    he = font[cpname(0x05D4)]
    bp = BoundsPen(font)
    he.draw(bp)
    print(f"he height: {round(bp.bounds[3])} (target 1090)")
    unplaced = []
    for g in heb:
        if g.components and not g.contours:
            base = {a.name for a in font[g.components[0].baseGlyph].anchors}
            for c in g.components[1:]:
                m = font[c.baseGlyph]
                ma = [a.name[1:] for a in m.anchors if a.name.startswith("_")]
                if not ma or ma[0] not in base:
                    unplaced.append((g.name, c.baseGlyph))
    print(f"composite marks without anchor: {unplaced or 'none'}")
    ok &= not unplaced
    print("CHECK", "OK" if ok else "FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    font = ufoLib2.Font.open(args.ufo)
    if args.check:
        sys.exit(0 if check(font) else 1)
    todo = [g for g in font if g.lib.get(HEBREW_KEY) == "imported"]
    if not todo:
        print("nothing to fit (no glyphs in the 'imported' state)")
        derive(font)
        font.save()
        return
    vav, roof = scaled_stems(font)
    dx, dy = (vav - STEM_V) / 2, (roof - STEM_H) / 2
    print(f"scaled donor: vav stem {vav}, he roof {roof} -> inset dx={dx:.1f} dy={dy:.1f}")
    n, corners, missing = fit(font, dx, dy)
    derive(font)
    font.save()
    print(f"{args.ufo}: fitted {n} Hebrew glyphs, rounded {corners} corners")
    for k, v in missing.items():
        print(f"  {k}: no anchor for {v}, left at the default overlay")


if __name__ == "__main__":
    main()
