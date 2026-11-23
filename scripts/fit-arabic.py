#!/usr/bin/env python3
"""Fit the Arabic into the screenplay line (12 pt, six lines to the inch).

A screenplay is single-spaced: Courier at 12 pt, one line every 12 pt, so a
line has 2048 units (UPM) for everything it draws -- in Lexington's PDF the
baseline sits 1628 under the top of the line and 399 above its bottom. The
Latin fits (ascender 1322, descender -410). The Arabic, merged from No Name
Fixed, did not: its letters alone ran from -1024 (final yeh) to 1845, its
vowel marks were 530-680 units tall, and once the GPOS put each mark 128
above (below) its letter, a vowelled line reached 2600 up and 1700 down, so
cue, parenthetical and dialogue lines ran into each other.

This brings the Arabic to the line, keeping the advance (1228, monospace)
and every join:

  1. Letters: one vertical map F for every Arabic letter glyph (encoded,
     presentation forms, positional variants), so the joins, which all sit on
     the same baseline stroke (225-369), still meet. F is the identity in the
     body (BODY_LO-BODY_HI: the baseline stroke, the bowls, the teeth),
     shortens the ascenders by KA and the descenders by KD for the first
     DEPTH under the body and KD2 beyond it. x is untouched.
     Horizontal strokes in a compressed zone would thin with it, so each
     outline point grows back out by half of what its stroke lost (the
     stroke's thickness measured vertically into the ink, up to STROKE_MAX;
     a stem's end just moves): the strokes keep their weight.
  2. Dots, hamzas and the wasla (separate contours that are not counters;
     small, or wholly outside the body) are not squashed: each cluster (the
     two or three dots of a letter) is scaled by DOT (a hamza or wasla by
     MARK + 0.1) and moved rigidly, its edge nearest the body put where F
     puts it; then it comes as close as DOT_GAP to the ink under (over) it,
     looking DOT_SIDE beside it too, so teh's dots come down between its
     horns while zain's dot stays above the reh's head -- but never closer
     to the letter than min(its old gap, DOT_GAP), so the Bold (68 units
     heavier) keeps its dots apart.
  3. Marks (U+064B-065F, U+0670, the Quranic marks, ...): scaled by MARK
     about their ink centre, the stroke grown back to MARK_STROKE (offset
     outward along the normal), centre moved by F, advance 0. They come out
     about the size of the Latin acute.

The GPOS anchors are then made from this ink by make-mark-anchors.py (an
Arabic mark sits ARAB_GAP from the letter's ink, a below mark measured
under its own footprint). Run once;
the glyphs are tagged in their lib (org.courierbadi.arabic = "fitted") and a
second run changes nothing. --check reports the extents.

Usage:
  python3 scripts/fit-arabic.py [--ufo sources/CourierBadi-Regular.ufo] [--check]
then `make masters` (the Italic and Bold follow) and `make build`.
"""
import argparse
import importlib.util
import math
import os
import sys
import unicodedata as ud

import ufoLib2
from fontTools.pens.boundsPen import BoundsPen

ARABIC_KEY = "org.courierbadi.arabic"
STEM_H = 144.0

# the vertical map: identity on [BODY_LO, BODY_HI], slope KA above, KD below
BODY_LO, BODY_HI = 225.0, 800.0
KA = 0.32         # ascenders: straight stems, shortened evenly
# descenders: the first DEPTH under the body keep most of their depth (KD),
# so reh, zain, waw and noon still clearly go below the line (reh is not
# dal); deeper than that (the bowls of jeem, ain, meem, yeh) flattens (KD2)
KD, DEPTH, KD2 = 0.75, 400.0, 0.2
MARK = 0.42       # mark scale
MARK_STROKE = 124 # the marks' stroke after scaling (letters: 144-150)
DOT = 0.75        # dot cluster scale (a hamza or wasla drawn into a letter: MARK + 0.1)
DOT_MAX = 440     # a separate contour up to this size (both sides) is a dot
CLUSTER = 120     # dots closer than this (bbox distance) move together
DOT_GAP = 110     # a dot cluster comes down (up) to this far from the ink under (over) it
DOT_SIDE = 150    # ... looking this far beside the cluster too
OUTSIDE_TOL = 60  # a contour this close to the body still counts as outside it (kaf's sign)
STROKE_MAX = 230  # ink thicker than this along the normal is a stem's end, not a stroke

_spec = importlib.util.spec_from_file_location(
    "mma", os.path.join(os.path.dirname(__file__), "make-mark-anchors.py"))
_mma = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mma)


def F(y):
    if y > BODY_HI:
        return BODY_HI + (y - BODY_HI) * KA
    if y < BODY_LO - DEPTH:
        return BODY_LO - DEPTH * KD - (BODY_LO - DEPTH - y) * KD2
    if y < BODY_LO:
        return BODY_LO - (BODY_LO - y) * KD
    return y


def slope(y):
    if y > BODY_HI:
        return KA
    if y < BODY_LO - DEPTH:
        return KD2
    return KD if y < BODY_LO else 1.0


def is_mark(g):
    return any(ud.category(chr(c)) in ("Mn", "Me") for c in g.unicodes)


# The spacing hamzas are left as they are: they join nothing, the hamza on
# the line sits in the body, and the high hamza (U+0674, Kazakh) should stay
# the same shape and size as it (fontbakery's arabic_high_hamza).
UNFITTED = {0x0621, 0x0674, 0xFE80}


def kind(g):
    """'mark', 'letter' or None (not fitted: digits, punctuation, symbols)."""
    if _mma.family_of_glyph(g) != "Arab" or UNFITTED & set(g.unicodes):
        return None
    if not g.unicodes:
        return "letter"
    if is_mark(g):
        return "mark"
    if ud.category(chr(g.unicodes[0])) in ("Lo", "Lm"):
        return "letter"
    return None


def cbounds(c):
    xs = [p.x for p in c.points]
    ys = [p.y for p in c.points]
    return min(xs), min(ys), max(xs), max(ys)


def area(c):
    pts = [(p.x, p.y) for p in c.points]
    return sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1])) / 2


def inside(pt, c):
    """pt inside the polygon of c's points (on- and off-curve: close enough)."""
    x, y = pt
    pts = [(p.x, p.y) for p in c.points]
    n, ins = len(pts), False
    for i in range(n):
        (x0, y0), (x1, y1) = pts[i], pts[i - 1]
        if (y0 > y) != (y1 > y) and x < (x1 - x0) * (y - y0) / (y1 - y0) + x0:
            ins = not ins
    return ins


def normals(c):
    """outward unit normal at every point (miter of the two segments)."""
    pts = [(p.x, p.y) for p in c.points]
    n = len(pts)
    out = []
    for i in range(n):
        p = pts[i]
        j = (i - 1) % n
        while pts[j] == p and j != i:
            j = (j - 1) % n
        k = (i + 1) % n
        while pts[k] == p and k != i:
            k = (k + 1) % n

        def un(a, b):
            tx, ty = b[0] - a[0], b[1] - a[1]
            L = math.hypot(tx, ty)
            return None if L < 1e-6 else (ty / L, -tx / L)
        n1, n2 = un(pts[j], p), un(p, pts[k])
        if n1 is None or n2 is None:
            out.append((0.0, 0.0))
            continue
        d = n1[0] * n2[0] + n1[1] * n2[1]
        if 1 + d < 0.25:
            c_ = un(pts[j], pts[k]) or (0.0, 0.0)
            out.append(c_)
            continue
        mx, my = (n1[0] + n2[0]) / (1 + d), (n1[1] + n2[1]) / (1 + d)
        L = math.hypot(mx, my)
        if L > 2:
            mx, my = mx * 2 / L, my * 2 / L
        out.append((mx, my))
    return out


def dots_of(g):
    """indices of the contours moved rigidly: dots and hamzas (small), and
    marks drawn into a letter (a separate contour wholly outside the body,
    like alef wasla's), never a counter or a contour lying in another's ink;
    a counter goes with the contour it is in."""
    cs = list(g.contours)
    if not cs:
        return set()
    big = max(cs, key=lambda c: abs(area(c)))
    sign = 1 if area(big) > 0 else -1
    out = set()
    for i, c in enumerate(cs):
        x0, y0, x1, y1 = cbounds(c)
        small = x1 - x0 <= DOT_MAX and y1 - y0 <= DOT_MAX
        outside = y0 >= BODY_HI - OUTSIDE_TOL or y1 <= BODY_LO + OUTSIDE_TOL
        if not (small or outside) or area(c) * sign <= 0:
            continue
        ctr = ((x0 + x1) / 2, (y0 + y1) / 2)
        if any(inside(ctr, o) for o in cs if o is not c):
            continue
        out.add(i)
    if len(out) == sum(1 for c in cs if area(c) * sign > 0):
        return set()    # all of it is outside the body: a letter, not dots
    for i, c in enumerate(cs):
        if area(c) * sign < 0:
            x0, y0, x1, y1 = cbounds(c)
            if any(inside(((x0 + x1) / 2, (y0 + y1) / 2), cs[j]) for j in out):
                out.add(i)
    return out


def clusters(g, idx):
    cs = list(g.contours)
    groups = []
    for i in sorted(idx):
        b = cbounds(cs[i])
        hit = [gr for gr in groups if any(
            max(b[0] - cbounds(cs[j])[2], cbounds(cs[j])[0] - b[2],
                b[1] - cbounds(cs[j])[3], cbounds(cs[j])[1] - b[3]) < CLUSTER for j in gr)]
        merged = [i]
        for gr in hit:
            merged += gr
            groups.remove(gr)
        groups.append(merged)
    return groups


def move_rigid(contours, scale, anchor_y_of):
    """scale the contours about their joint (centre-x, anchor) point and put
    that point at F(anchor)."""
    xs, ys = [], []
    for c in contours:
        b = cbounds(c)
        xs += [b[0], b[2]]
        ys += [b[1], b[3]]
    cx = (min(xs) + max(xs)) / 2
    ay = anchor_y_of(min(ys), max(ys))
    ny = F(ay)
    for c in contours:
        for p in c.points:
            p.x = cx + (p.x - cx) * scale
            p.y = ny + (p.y - ay) * scale


def anchor_edge(lo, hi):
    """the edge of a dot cluster nearest the body."""
    if lo >= BODY_HI:
        return lo
    if hi <= BODY_LO:
        return hi
    return (lo + hi) / 2


def crossings(polys, x):
    """the y where the vertical line at x crosses the (flattened) outline."""
    ys = []
    for pts in polys:
        for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]):
            if (x0 <= x < x1) or (x1 <= x < x0):
                ys.append(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
    return sorted(ys)


def thickness(polys, x, y, d):
    """how far the ink reaches from the outline point (x, y) in direction d
    (+1 up, -1 down): a horizontal stroke's thickness, or a stem's length."""
    ys = crossings(polys, x + 0.5)
    ahead = [v - y for v in ys if (v - y) * d > 4]
    return min(abs(v) for v in ahead) if ahead else 0


def min_dist(a, b):
    return min(math.hypot(p[0] - q[0], p[1] - q[1]) for p in a[::2] for q in b[::2])


def fit_letter(g):
    cs = list(g.contours)
    dots = dots_of(g)
    polys = [_mma.outline_points_contour(c, 6) for c in cs]
    ink0 = [q for i, pl in enumerate(polys) if i not in dots for q in pl]
    gap0 = {}
    for gr in clusters(g, dots):
        gap0[tuple(gr)] = min_dist([q for i in gr for q in polys[i]], ink0) if ink0 else 0
    body = [pl for i, pl in enumerate(polys) if i not in dots]
    for i, c in enumerate(cs):
        if i in dots:
            continue
        ns = normals(c)
        pts = list(c.points)
        n = len(pts)
        # the growth is measured at the on-curve points; a handle moves with
        # the on-curve point it belongs to (its neighbour on that side)
        shift = [0.0] * n
        for k, (p, (nx, ny)) in enumerate(zip(pts, ns)):
            if p.type is None or abs(ny) <= 0.2:
                continue
            dirn = -1 if ny > 0 else 1        # into the ink
            t = thickness(body, p.x, p.y, dirn)
            if 0 < t <= STROKE_MAX:
                # keep the stroke's thickness t: the map makes it
                # F(y) - F(y - t); each side grows back half the loss. The
                # end of a stem (t long) is no stroke: it just moves.
                lost = t - abs(F(p.y) - F(p.y + dirn * t))
                shift[k] = (1 if ny > 0 else -1) * lost / 2
        for k, p in enumerate(pts):
            if p.type is None:
                a, b = pts[k - 1], pts[(k + 1) % n]
                if a.type is not None:
                    shift[k] = shift[k - 1]
                elif b.type is not None:
                    shift[k] = shift[(k + 1) % n]
        new = [F(p.y) + shift[k] for k, p in enumerate(pts)]
        for p, y in zip(c.points, new):
            p.y = y
    # the letter's ink (dots apart), flattened, to bring the dots to it
    ink = []
    for i, c in enumerate(cs):
        if i not in dots:
            ink += _mma.outline_points_contour(c)
    for gr in clusters(g, dots):
        part = [cs[i] for i in gr]
        b0 = [cbounds(c) for c in part]
        lo, hi = min(b[1] for b in b0), max(b[3] for b in b0)
        x0, x1 = min(b[0] for b in b0), max(b[2] for b in b0)
        big = max(x1 - x0, hi - lo) > DOT_MAX + CLUSTER and len(part) <= 2
        move_rigid(part, MARK + 0.1 if big else DOT, anchor_edge)
        if big:   # a sign drawn as a stroke (wasla, kaf's sign): its stroke back
            grow = (MARK_STROKE - STEM_H * (MARK + 0.1)) / 2
            for c in part:
                ns = normals(c)
                for p, (nx, ny) in zip(list(c.points), ns):
                    p.x += nx * grow
                    p.y += ny * grow
        # then as near the letter as DOT_GAP allows, never further away
        b1 = [cbounds(c) for c in part]
        nlo, nhi = min(b[1] for b in b1), max(b[3] for b in b1)
        nx0, nx1 = min(b[0] for b in b1), max(b[2] for b in b1)
        # the ink under (over) the cluster and a little either side: a dot
        # comes down between two horns (teh), not into a curve beside it (zain)
        col = [y for x, y in ink if nx0 - DOT_SIDE <= x <= nx1 + DOT_SIDE]
        dy = 0
        up = (lo + hi) / 2 > (BODY_LO + BODY_HI) / 2
        if lo >= BODY_HI and col:            # above the letter
            under = [y for y in col if y < nlo]
            if under:
                dy = min(0, max(under) + DOT_GAP - nlo)
        elif hi <= BODY_LO and col:          # below it
            over = [y for y in col if y > nhi]
            if over:
                dy = max(0, min(over) - DOT_GAP - nhi)
        # and never closer to the letter than it was, or than DOT_GAP: the
        # map shortens the gap with the zone, and the Bold takes 68 more
        want = min(gap0[tuple(gr)], DOT_GAP)
        base = [q for c in part for q in _mma.outline_points_contour(c, 6)]

        def dist(off):
            return min_dist([(x, y + off) for x, y in base], ink) if ink else want
        for _ in range(6):
            d = dist(dy)
            if d >= want - 2:
                break
            step = want - d + 4     # move away from the ink, whichever way that is
            dy += step if dist(dy + step) >= dist(dy - step) else -step
        if dy:
            for c in part:
                for p in c.points:
                    p.y += dy


def fit_mark(g):
    cs = list(g.contours)
    if not cs:
        return
    xs, ys = [], []
    for c in cs:
        b = cbounds(c)
        xs += [b[0], b[2]]
        ys += [b[1], b[3]]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    ny = F(cy)
    grow = (MARK_STROKE - STEM_H * MARK) / 2
    dots = dots_of(g) if len(cs) > 1 else set()
    for i, c in enumerate(cs):
        ns = normals(c) if i not in dots else [(0, 0)] * len(c.points)
        new = []
        for p, (nx, nyy) in zip(c.points, ns):
            new.append((cx + (p.x - cx) * MARK + nx * grow, ny + (p.y - cy) * MARK + nyy * grow))
        for p, (x, y) in zip(c.points, new):
            p.x, p.y = x, y


def extents(font):
    rows = []
    for g in font:
        k = kind(g)
        if not k:
            continue
        bp = BoundsPen(font)
        g.draw(bp)
        if bp.bounds:
            rows.append((k, bp.bounds[1], bp.bounds[3], g.name))
    return rows


def check(font):
    rows = extents(font)
    for k in ("letter", "mark"):
        r = [x for x in rows if x[0] == k]
        lo = min(r, key=lambda x: x[1])
        hi = max(r, key=lambda x: x[2])
        print(f"{k}s: {len(r)}, lowest {lo[1]:.0f} ({lo[3]}), highest {hi[2]:.0f} ({hi[3]})")
    unfitted = [g.name for g in font if kind(g) and g.lib.get(ARABIC_KEY) != "fitted"
                and (g.contours or g.components)]
    print(f"not fitted: {unfitted or 'none'}")
    return not unfitted


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    font = ufoLib2.Font.open(args.ufo)
    if args.check:
        sys.exit(0 if check(font) else 1)
    n = {"letter": 0, "mark": 0}
    for g in font:
        k = kind(g)
        if not k or g.lib.get(ARABIC_KEY) == "fitted":
            continue
        (fit_letter if k == "letter" else fit_mark)(g)
        g.lib[ARABIC_KEY] = "fitted"
        n[k] += 1
    font.save()
    print(f"{args.ufo}: fitted {n['letter']} Arabic letters, {n['mark']} marks")
    check(font)


if __name__ == "__main__":
    main()
