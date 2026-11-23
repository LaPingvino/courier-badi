#!/usr/bin/env python3
"""Fit the glyphs merged from No Name Fixed in 0.500 to Courier Badi.

The 2023 merge (0.500) brought Arabic, Greek and extended Latin from No Name
Fixed as they were. The Hebrew (1.100) and Devanagari (1.103) were fitted to
the Courier Prime-derived Latin; this does the same for the 2023 glyphs. Like
fit-hebrew.py it is run once on the Regular (`make masters` carries it to
Italic, Bold and the contrast masters); every glyph it touches is tagged
org.courierbadi.merge = "fitted" in its lib, so a second run changes nothing.

Arabic (after fit-arabic.py, whose vertical fit and the 1.103 language
systems are kept): the letters' stroke is 141 where the Latin's verticals are
150, and their ends are cut square where the Latin's are rounded.
  - every letter contour (not the dots) is thickened 4.5 units each side,
    horizontally only, so no height changes (the 12 pt screenplay fit of
    1.102 stays exactly as it was); a point on the cell's edge (x = 0 or
    1228, the joins) is never moved;
  - the stem ends fit-arabic.py's map flattened (ascenders x0.32, deep
    descenders x0.2) get their depth back (restore_caps: the end point and
    so the heights stay, the shoulders slide along the stem);
  - convex corners are rounded like the Latin's terminals (fit-hebrew.py's
    rounding), except at the cell's edges, where the joins are; the square
    dots and the marks get the same rounding, scaled to their size.

Greek: No Name Fixed's cell was 1075 units, and its Greek came over at that
size, centred on x = 537 instead of 614, its capitals slab-serifed (the
Latin is not) and 1251-1276 tall (the Latin's 1187-1209), its lowercase on
an x-height of 883 (the Latin's 924), the stroke 125-145.
  - capitals the Latin has (A B E Z H I K M N O P T Y X, and F for digamma)
    are the Latin letters (components), so Greek and Latin capitals match;
  - the others are built from the Latin's parts: Gamma is L turned over,
    Lambda V turned over, Pi H's stems under a bar, Xi three bars, Sigma two
    bars and two diagonals, Theta the O with a bar, Phi and Psi a stem with
    O's or U's curve (scaled, stroke restored), koppa the O on a stem, the
    prosgegrammeni a short stem; Delta and Omega already were Courier's;
  - the lowercase (and the archaic small letters) are recentred, scaled to
    the Latin (x by the width of o, y piecewise: x-height to 924, ascenders
    to the Latin's 1322, descenders to its -400), their convex corners
    rounded, and their stroke brought to 150 / 144 by a normal offset
    measured from the scaled letters;
  - accents (tonos, breathings, perispomeni, dialytika, the spacing forms
    U+1FBD-1FFE) are moved with the x-height and their stroke brought to the
    Latin accents' weight; the precomposed lowercase forms are rebuilt from
    the fitted letter (a component) and their own accents, fitted the same
    way; the polytonic capitals put their accent beside the (Latin) letter
    with at least ACC_GAP to its ink, the letter narrowed (stems restored)
    when there is no room in the cell.

Extended Latin: 145 of the 161 merged letters already use the Latin letter
and carry only No Name Fixed's accents (thinner, other shapes); the rest
(the horned o, o with ogonek, the hook above, ...) use No Name Fixed's o and
i. They are rebuilt as Courier composites, the way Courier Prime builds its
own (aacute = a + acute): the Latin letter and the Latin's accents placed as
in its own accented letters (the same x offset per letter, +270 over
capitals, +370 over ascenders), a second accent stacked above with ACC_GAP
clearance, and Vietnamese acute, grave and hook after a circumflex at its
upper right. New accents, drawn from the Latin's: hook above (No Name Fixed's
hook at the Latin accents' weight), horn (the Latin comma, 0.75, stroke
restored), double grave (the Latin's double acute turned round), inverted
breve (the breve turned over), the below forms (dot, macron, breve). No
Name Fixed's combining marks (U+0309, 030F, 0311, 031B, 032E, 032F, 0331,
0332) become components of these, where they were drawn.

Usage:
  python3 scripts/fit-merge.py [--ufo sources/CourierBadi-Regular.ufo] [--check]
then `make arabic-features` and `make masters`.
"""
import argparse
import importlib.util
import math
import os
import statistics
import sys
import unicodedata as ud

import numpy as np
import pathops
import ufoLib2
from fontTools.misc.transform import Transform
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.freetypePen import FreeTypePen
from fontTools.pens.perimeterPen import PerimeterPen
from fontTools.pens.qu2cuPen import Qu2CuPen
from fontTools.pens.recordingPen import DecomposingRecordingPen, RecordingPen
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen


def _load(name, file):
    spec = importlib.util.spec_from_file_location(name, os.path.join(os.path.dirname(__file__), file))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_heb = _load("fit_hebrew", "fit-hebrew.py")
_ara = _load("fit_arabic", "fit-arabic.py")

KEY = "org.courierbadi.merge"
CELL = 1228
STEM_V, STEM_H = 150.0, 144.0
XH, CAP, CAP_TOP = 924, 1187, 1197     # x-height, cap height, a stem's rounded end
ACC_GAP = 60                            # clearance between an accent and the ink it goes with
CORNER = 64.0                           # corner rounding (fit-hebrew.py, cf. L)


# --- outline helpers ----------------------------------------------------------

def bounds(font, g):
    bp = BoundsPen(font)
    g.draw(bp)
    return bp.bounds


def rec(font, name, t=Transform(), reverse=False):
    """the decomposed outline of a glyph, transformed (a RecordingPen)."""
    rp = DecomposingRecordingPen(font)
    font[name].draw(rp)
    out = RecordingPen()
    pen = TransformPen(out, t)
    rp.replay(ReverseContourPen(pen) if reverse else pen)
    return out


def flips(t):
    a, b, c, d = t[:4]
    return a * d - b * c < 0


def set_outline(g, *recs):
    """replace g's outline by the union of the recorded outlines (skia-pathops,
    canonical winding, back to cubics)."""
    path = None
    for r in recs:            # each part on its own (its winding is its own), then the union
        p = pathops.Path()
        r.replay(p.getPen())
        p.simplify(fix_winding=True, keep_starting_points=False)
        path = p if path is None else pathops.op(path, p, pathops.PathOp.UNION)
    if path is None:
        path = pathops.Path()
    g.clearContours()
    g.clearComponents()
    path.draw(Qu2CuPen(g.getPen(), max_err=0.5, all_cubic=True))


def rect(x0, y0, x1, y1):
    r = RecordingPen()
    r.moveTo((x0, y0))
    r.lineTo((x1, y0))
    r.lineTo((x1, y1))
    r.lineTo((x0, y1))
    r.closePath()
    return r


def poly(points):
    r = RecordingPen()
    r.moveTo(points[0])
    for p in points[1:]:
        r.lineTo(p)
    r.closePath()
    return r


def contour_rec(c):
    r = RecordingPen()
    c.draw(r)
    return r


def stroke_estimate(recs):
    """a monoline stroke's width, 2 * area / perimeter (ends make it a little low)."""
    a, p = AreaPen(), PerimeterPen()
    for r in recs:
        r.replay(a)
        r.replay(p)
    return 2 * abs(a.value) / p.value if p.value else 0


def offset_contour(contour, dx, dy, pin=None):
    """grow (dx, dy > 0) or thin (< 0) the ink along the normal: fit-hebrew.py's
    miter inset with the sign turned; points for which pin(p) holds stay."""
    keep = [(p.x, p.y) for p in contour.points] if pin else None
    _heb.inset_contour(contour, -dx, -dy)
    if pin:
        for p, (x, y) in zip(contour.points, keep):
            if pin(x, y):
                p.x, p.y = x, y


def round_contour(contour, radius, skip=None):
    """fit-hebrew.py's rounding of convex line-line corners, with a radius and
    corners to leave sharp (skip(x, y))."""
    from ufoLib2.objects import Point
    pts = list(contour.points)
    n = len(pts)
    if n < 3:
        return 0
    out, done = [], 0
    for i, p in enumerate(pts):
        prv, nxt = pts[i - 1], pts[(i + 1) % n]
        if (p.type == "line" and nxt.type == "line" and prv.type is not None
                and not (skip and skip(p.x, p.y))):
            ix, iy = p.x - prv.x, p.y - prv.y
            ox, oy = nxt.x - p.x, nxt.y - p.y
            li, lo = math.hypot(ix, iy), math.hypot(ox, oy)
            if li > 1 and lo > 1:
                ix, iy, ox, oy = ix / li, iy / li, ox / lo, oy / lo
                cross, dot = ix * oy - iy * ox, ix * ox + iy * oy
                if cross > 0 and math.atan2(cross, dot) > _heb.MIN_TURN:
                    d = min(radius, 0.45 * li, 0.45 * lo)
                    ax, ay = p.x - d * ix, p.y - d * iy
                    bx, by = p.x + d * ox, p.y + d * oy
                    h = _heb.HANDLE
                    out += [Point(ax, ay, "line"),
                            Point(ax + h * d * ix, ay + h * d * iy),
                            Point(bx - h * d * ox, by - h * d * oy),
                            Point(bx, by, "curve")]
                    done += 1
                    continue
        out.append(Point(p.x, p.y, p.type, p.smooth))
    contour.points[:] = out
    return done


def round_all(g):
    for c in g.contours:
        for p in c.points:
            p.x, p.y = round(p.x), round(p.y)


def restroke(g, dx, dy):
    for c in g.contours:
        offset_contour(c, dx, dy)


def rounded(g, radius=CORNER):
    n = 0
    for c in g.contours:
        n += round_contour(c, radius)
    return n


# --- raster clearance (placing accents) -----------------------------------------

RS = 8                       # units per pixel
RX0, RY0, RW, RH = -1600, -1400, 4500, 4400


class Ink:
    """a bitmap of placed outlines, to place an accent clear of them."""

    def __init__(self):
        self.a = np.zeros((RH // RS, RW // RS), bool)

    @staticmethod
    def raster(r, dx=0, dy=0):
        pen = FreeTypePen(None)
        r.replay(TransformPen(pen, (1 / RS, 0, 0, 1 / RS, (dx - RX0) / RS, (dy - RY0) / RS)))
        return pen.array(width=RW // RS, height=RH // RS, contain=False)[::-1] > 0.3

    def add(self, r, dx=0, dy=0):
        self.a |= self.raster(r, dx, dy)

    def grown(self, gap):
        a = self.a.copy()
        k = int(round(gap / RS))
        yy, xx = np.mgrid[-k:k + 1, -k:k + 1]
        disk = xx * xx + yy * yy <= k * k
        out = np.zeros_like(a)
        for oy, ox in zip(*np.nonzero(disk)):
            sy, sx = oy - k, ox - k
            out |= np.roll(np.roll(a, sy, 0), sx, 1)
        return out

    def clear(self, grown, r, dx, dy):
        return not (grown & self.raster(r, dx, dy)).any()


def lowest_clear(ink, r, dx, y_from, gap=ACC_GAP, step=8, limit=1200):
    """the lowest dy >= y_from at which r (moved by dx, dy) keeps gap from ink."""
    g = ink.grown(gap)
    dy = y_from
    while dy < y_from + limit:
        if ink.clear(g, r, dx, dy):
            return dy
        dy += step
    return dy


def rightmost_clear(ink, r, dy, x_from, x_to, gap=ACC_GAP, step=8):
    """the largest dx in [x_to, x_from] (searching leftwards) at which r keeps gap."""
    g = ink.grown(gap)
    dx = x_from
    while dx >= x_to:
        if ink.clear(g, r, dx, dy):
            return dx
        dx -= step
    return None


def leftmost_clear(ink, r, dy, x_from, x_to, gap=ACC_GAP, step=8):
    g = ink.grown(gap)
    dx = x_from
    while dx <= x_to:
        if ink.clear(g, r, dx, dy):
            return dx
        dx += step
    return None


def rec_bounds(r):
    bp = BoundsPen(None)
    r.replay(bp)
    return bp.bounds


def tag(g):
    g.lib[KEY] = "fitted"


def fitted(g):
    return g.lib.get(KEY) == "fitted"


def new_glyph(font, name, width=CELL):
    if name in font:
        g = font[name]
        g.clearContours()
        g.clearComponents()
        g.clearAnchors()
    else:
        g = font.newGlyph(name)
    g.width = width
    return g


def cmap(font):
    return {u: g.name for g in font for u in g.unicodes}


# --- extended Latin ---------------------------------------------------------------

TOP = {0x300: "grave", 0x301: "acute", 0x302: "circumflex", 0x303: "tilde",
       0x304: "macron", 0x306: "breve", 0x307: "dotaccent", 0x308: "dieresis",
       0x309: "hookabove", 0x30A: "ring", 0x30B: "hungarumlaut", 0x30C: "caron",
       0x30F: "dblgrave", 0x311: "breveinverted"}
BELOW = {0x323: "dotbelowcomb", 0x331: "macron", 0x332: "macron", 0x32E: "breve",
         0x32F: "breveinverted", 0x328: "ogonek", 0x327: "cedilla"}
HORN = 0x31B
HORN_SCALE = 0.75                             # the horn: the Latin comma at this size
VIET_SIDE = {"acute", "grave", "hookabove"}   # after a circumflex: at its upper right
VIET_SHIFT = 110                              # ... and the circumflex moves left this much
VIET_SIDE_X = 170                             # the accent's left end this far right of the circumflex's tip
VIET_GAP = 50
# a stack that would rise past the font's winAscent (2130) over a capital:
# the acute on the ring's upper right, nearly touching it (as Danish Ǻ is drawn); kept under 2100
# (over a capital the ring also comes down to RING_CAP, 41 over A's apex)
TIGHT_STACK = {("ring", "acute"): (290, 12)}
RING_CAP = 185
BELOW_GAP = 110                               # a macron or breve below: under the ink
DOT_GAP = 144                                 # Courier's dot below: its top this far under the letter


def accent_weight(font):
    return stroke_estimate([rec(font, n) for n in ("acute", "circumflex", "breve", "macron", "tilde")]) 


def make_accents(font):
    """the new spacing accents, drawn from the Latin's own (unencoded; used as
    components). Re-made on every run (they depend only on Latin glyphs and
    No Name Fixed's hook)."""
    w = accent_weight(font)
    # double grave: the double acute turned round
    g = new_glyph(font, "dblgrave")
    set_outline(g, rec(font, "hungarumlaut", Transform(-1, 0, 0, 1, CELL, 0), reverse=True))
    # inverted breve: the breve turned over (about its own middle)
    b = bounds(font, font["breve"])
    g = new_glyph(font, "breveinverted")
    set_outline(g, rec(font, "breve", Transform(1, 0, 0, -1, 0, b[1] + b[3]), reverse=True))
    # hook above: No Name Fixed's, centred where the Latin accents are, at their weight
    src = font["hookabovecomb"]
    if not fitted(src) or "hookabove" not in font:
        hb_ = bounds(font, src)
        ab = bounds(font, font["acute"])
        r = rec(font, "hookabovecomb", Transform(1, 0, 0, 1, CELL / 2 - (hb_[0] + hb_[2]) / 2, ab[1] - hb_[1]))
        g = new_glyph(font, "hookabove")
        set_outline(g, r)
        grow = max(0.0, (w - stroke_estimate([r])) / 2)
        restroke(g, grow, grow)
        round_all(g)
    # horn: the Latin comma at 0.6, its stroke restored
    r = rec(font, "comma", Transform(HORN_SCALE, 0, 0, HORN_SCALE, 0, 0))
    g = new_glyph(font, "horn")
    set_outline(g, r)
    grow = max(0.0, min(30.0, (w - stroke_estimate([r])) / 2))
    restroke(g, grow, grow)
    round_all(g)
    return w


def precedents(font, merged):
    """Courier's own placement of an accent per letter: base -> (dx, dy) of the
    top accent, and base -> (dx, dy) of the dot below / ogonek."""
    top, below = {}, {}
    names = set(TOP.values())
    for g in font:
        if g.name in merged or g.contours or len(g.components) != 2:
            continue
        cs = {c.baseGlyph: c.transformation for c in g.components}
        marks = [n for n in cs if n in names or n in ("dotbelowcomb", "ogonek")]
        bases = [n for n in cs if n not in marks]
        if len(marks) != 1 or len(bases) != 1 or cs[bases[0]] != (1, 0, 0, 1, 0, 0):
            continue
        t = cs[marks[0]]
        if tuple(t[:4]) != (1, 0, 0, 1):
            continue
        if marks[0] in names and t[5] < -50:
            continue         # an accent used as a bar (t-bar = t + macron)
        d = top if marks[0] in names else below
        d.setdefault((bases[0], marks[0] if marks[0] in ("dotbelowcomb", "ogonek") else "*"), []).append((t[4], t[5]))
    med = lambda v: (statistics.median(x for x, _ in v), statistics.median(y for _, y in v))
    return ({k[0]: med(v) for k, v in top.items()},
            {k: med(v) for k, v in below.items()})


def band_centre(font, name, top=True, band=220):
    """x-centre of a glyph's ink in its top (bottom) band."""
    a = Ink.raster(rec(font, name))       # row 0 is the bottom
    rows = np.nonzero(a.any(axis=1))[0]
    if not len(rows):
        return CELL / 2
    if top:
        sel = a[rows[-1] - band // RS:rows[-1] + 1]
    else:
        sel = a[rows[0]:rows[0] + band // RS]
    cols = np.nonzero(sel.any(axis=0))[0]
    return RX0 + (cols[0] + cols[-1] + 1) / 2 * RS


def decompose(ch):
    s = ud.normalize("NFD", ch)
    return s[0], [ord(c) for c in s[1:]]


def build_latin(font, g, cm, top_prec, below_prec):
    ch = chr(g.unicodes[0])
    base_ch, marks = decompose(ch)
    if not marks or any(m not in TOP and m not in BELOW and m != HORN for m in marks):
        return False
    tops = [TOP[m] for m in marks if m in TOP]
    belows = [BELOW[m] for m in marks if m in BELOW]
    base = cm.get(ord(base_ch))
    if tops and base_ch == "i":
        base = "dotlessi"
    if tops and base_ch == "j":
        base = "uni0237"
    if base is None:
        return False
    upper = base_ch.isupper()
    bb = bounds(font, font[base])
    comps = [(base, 0, 0)]
    ink = Ink()
    ink.add(rec(font, base))
    if HORN in marks:
        hb_ = bounds(font, font["horn"])
        # the horn's tail on the letter's upper right, its blob beside it
        right = band_centre(font, base, top=True, band=260)
        a = Ink.raster(rec(font, base))
        rows = np.nonzero(a.any(axis=1))[0]
        sel = a[rows[-1] - 300 // RS:rows[-1] + 1]
        xr = RX0 + (np.nonzero(sel.any(axis=0))[0][-1] + 1) * RS
        hx = xr - 60 - hb_[0]
        hx = min(hx, CELL - 10 - hb_[2])
        hy = bb[3] - 250 - hb_[1]
        comps.append(("horn", round(hx), round(hy)))
        ink.add(rec(font, "horn"), hx, hy)
    if tops:
        if base in top_prec:
            dx, dy = top_prec[base]
        else:
            dx = 0
            dy = max(0, bb[3] - 946) + (19 if upper else 4) if bb[3] > 960 else 0
            if upper:
                dy = 270
        prev = None
        for i, m in enumerate(tops):
            r = rec(font, m)
            if prev is None:
                mdx, mdy = dx, dy
                if m == "circumflex" and len(tops) > 1 and tops[1] in VIET_SIDE:
                    mdx -= VIET_SHIFT
                if upper and tuple(tops[:2]) in TIGHT_STACK and m == "ring":
                    mdy = RING_CAP
            elif prev[0] == "circumflex" and m in VIET_SIDE:
                pb = rec_bounds(rec(font, "circumflex"))
                mb = rec_bounds(r)
                ccx = (pb[0] + pb[2]) / 2 + prev[1]
                mdx = ccx + VIET_SIDE_X - mb[0]
                mdx = min(mdx, CELL - 10 - mb[2])
                mdy = lowest_clear(ink, r, mdx, prev[2] - 300, gap=VIET_GAP)
            elif (prev[0], m) in TIGHT_STACK:
                sx, gap = TIGHT_STACK[(prev[0], m)]
                mdx = dx + sx
                mdy = lowest_clear(ink, r, mdx, prev[2] + 250, gap=gap)   # above the ring's middle
            else:
                mdx = dx
                mdy = lowest_clear(ink, r, mdx, prev[2])
            comps.append((m, round(mdx), round(mdy)))
            ink.add(r, mdx, mdy)
            prev = (m, mdx, mdy)
    for m in belows:
        r = rec(font, m)
        mb = rec_bounds(r)
        if m in ("dotbelowcomb", "ogonek") and (base, m) in below_prec:
            mdx, mdy = below_prec[(base, m)]
        elif m == "dotbelowcomb":
            mdx = (bb[0] + bb[2]) / 2 - (mb[0] + mb[2]) / 2
            mdy = bb[1] - DOT_GAP - mb[3]
        elif m == "ogonek":
            # the ogonek's top on the letter's bottom, a little right of its middle
            mdx = (bb[0] + bb[2]) / 2 + 60 - (mb[0] + mb[2]) / 2
            mdy = bb[1] + 22 if bb[1] < 0 else 0
        else:
            mdx = (bb[0] + bb[2]) / 2 - (mb[0] + mb[2]) / 2
            mdy = bb[1] - BELOW_GAP - mb[3]
        comps.append((m, round(mdx), round(mdy)))
    g.clearContours()
    g.clearComponents()
    for n, x, y in comps:
        g.components.append(ufoLib2.objects.Component(baseGlyph=n, transformation=(1, 0, 0, 1, x, y)))
    g.width = CELL
    tag(g)
    return True


# No Name Fixed's combining marks -> a component of the new accent, where it was drawn
COMBINING = {0x0309: "hookabove", 0x030F: "dblgrave", 0x0311: "breveinverted",
             0x031B: "horn", 0x032E: "breve", 0x032F: "breveinverted",
             0x0331: "macron", 0x0332: "macron"}


def refit_combining(font, cm):
    n = 0
    for u, acc in COMBINING.items():
        name = cm.get(u)
        if not name or fitted(font[name]):
            continue
        g = font[name]
        ob = bounds(font, g)
        ab = bounds(font, font[acc])
        dx = (ob[0] + ob[2]) / 2 - (ab[0] + ab[2]) / 2
        if u == 0x031B:      # the horn: where the old one was (on u), by its tail
            dx, dy = ob[0] - 60 - ab[0], ob[1] - ab[1]
        elif u in (0x0331, 0x0332, 0x032E, 0x032F):
            dy = ob[3] - ab[3]
        else:
            dy = ob[1] - ab[1]
        g.clearContours()
        g.clearComponents()
        g.components.append(ufoLib2.objects.Component(baseGlyph=acc, transformation=(1, 0, 0, 1, round(dx), round(dy))))
        g.width = 0
        tag(g)
        n += 1
    return n


# the extended Latin that came with the 2023 merge (commit 3f1a85e1)
LATIN_MERGED = ("ſƎƠơƯưǍǎǏǐǑǒǓǔǗǘǙǚǛǜǝǦǧǪǫǰǴǵǺǻǼǽǾǿȀȁȄȅȈȉȌȍȐȑȔȕḎḏḦḧḪḫḮḯḶḷḸḹṂṃṄṅṆṇ"
                "ṘṙṚṛṜṝṮṯẗẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớ"
                "ỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỴỵỶỷỸỹ")


# turned e and reversed E are outlines (drawn from e and E); long s was No Name
# Fixed's own, already the Latin's f without its bar, and is kept
OUTLINE_LATIN = (0x01DD, 0x018E, 0x017F)


def merged_latin(font):
    cm = cmap(font)
    return [font[cm[ord(c)]] for c in LATIN_MERGED if ord(c) in cm]


def turned(font, cm):
    """turned e (U+01DD) and reversed E (U+018E), from the Latin's e and E."""
    for u, src, t in ((0x01DD, "e", None), (0x018E, "E", None)):
        g = font[cm[u]]
        if fitted(g):
            continue
        b = bounds(font, font[src])
        if u == 0x01DD:      # turned: rotated half a turn about the ink's middle
            tr = Transform(-1, 0, 0, -1, b[0] + b[2], b[1] + b[3])
            set_outline(g, rec(font, src, tr))
        else:                # reversed: mirrored left-right in the cell
            set_outline(g, rec(font, src, Transform(-1, 0, 0, 1, CELL, 0), reverse=True))
        round_all(g)
        tag(g)


def fit_latin(font):
    cm = cmap(font)
    make_accents(font)
    lat = merged_latin(font)
    top_prec, below_prec = precedents(font, {g.name for g in lat})
    built, kept = [], []
    turned(font, cm)
    for g in lat:
        if fitted(g):
            continue
        if build_latin(font, g, cm, top_prec, below_prec):
            built.append(g.name)
        else:
            kept.append(g.name)
    nc = refit_combining(font, cm)
    return built, kept, nc


# --- Greek -------------------------------------------------------------------

NNF_CX = 1075 / 2           # No Name Fixed's cell was 1075 units; its Greek is centred there
NNF_XH, NNF_CAP = 883, 1251
LAT_ASC, LAT_DESC = 1322, -398      # b, p
# capitals the Latin has
AS_LATIN = {0x0391: "A", 0x0392: "B", 0x0395: "E", 0x0396: "Z", 0x0397: "H",
            0x0399: "I", 0x039A: "K", 0x039C: "M", 0x039D: "N", 0x039F: "O",
            0x03A1: "P", 0x03A4: "T", 0x03A5: "Y", 0x03A7: "X", 0x03DC: "F"}
# Courier's own (not from the merge): pi, mu, Delta, Omega
COURIER_GREEK = {0x03C0, 0x03BC, 0x0394, 0x03A9}
# accented capitals the Latin has: the same composite
AS_LATIN_ACCENTED = {0x03AA: ("I", "dieresis"), 0x03AB: ("Y", "dieresis"), 0x1FD9: ("I", "macron"),
                     0x1FD8: ("I", "breve"), 0x1FB9: ("A", "macron"), 0x1FB8: ("A", "breve"),
                     0x1FE9: ("Y", "macron"), 0x1FE8: ("Y", "breve")}
# canonically the same as a Latin punctuation mark
GREEK_PUNCT = {0x037E: "semicolon", 0x0387: "periodcentered"}
GREEK_SMALL = [u for u in range(0x03B1, 0x03CA) if u not in COURIER_GREEK and u != 0x03A2] + \
    [0x03D9, 0x03DB, 0x03DD, 0x03DF, 0x03E1]
ARCHAIC_CAPS = [0x03DA, 0x03DE, 0x03E0]      # stigma, koppa (later), sampi: scaled like the capitals
SPACING_MARKS = [0x0374, 0x0375, 0x037A, 0x0384, 0x0385, 0x1FBD, 0x1FBF, 0x1FC0, 0x1FC1,
                 0x1FCD, 0x1FCE, 0x1FCF, 0x1FDD, 0x1FDE, 0x1FDF, 0x1FED, 0x1FEE, 0x1FEF,
                 0x1FFD, 0x1FFE]
PROSGEGRAMMENI = 0x1FBE
OVER_CAPITAL = {"dieresis", "macron", "breve", "uni0308", "uni0304", "uni0306"}
LEFT_MIN = -40      # an accent beside a capital may reach this far into the cell before
                    # (where a letter's side bearing is); No Name Fixed's reached -108


class GreekMap:
    """No Name Fixed's Greek -> the Latin's proportions."""

    def __init__(self, font, cm):
        lo, om = bounds(font, font["o"]), bounds(font, font[cm[0x03BF]])
        self.sx = (lo[2] - lo[0]) / (om[2] - om[0])
        self.k = XH / NNF_XH
        tops = [bounds(font, font[cm[u]])[3] for u in (0x03B2, 0x03B4, 0x03B6, 0x03B8, 0x03BB, 0x03BE, 0x03C8)]
        bots = [bounds(font, font[cm[u]])[1] for u in (0x03B2, 0x03B7, 0x03C1, 0x03C6, 0x03C7, 0x03C8)]
        self.asc, self.desc = statistics.median(tops), statistics.median(bots)
        self.ka = (LAT_ASC - XH) / (self.asc - NNF_XH)
        self.kd = LAT_DESC / self.desc
        self.mark_dy = self.y(NNF_XH) - NNF_XH

    def x(self, x):
        return CELL / 2 + (x - NNF_CX) * self.sx

    def y(self, y):
        if y > NNF_XH:
            return XH + (y - NNF_XH) * self.ka
        if y < 0:
            return y * self.kd
        return y * self.k

    def letter(self, g):
        for c in g.contours:
            for p in c.points:
                p.x, p.y = self.x(p.x), self.y(p.y)

    def mark_contours(self, contours, below=False):
        """an accent: x like the letters, moved rigidly with the x-height
        (below the line: with the descender's map of its top)."""
        for c in contours:
            ys = [p.y for p in c.points]
            dy = (self.y(max(ys)) - max(ys)) if below else self.mark_dy
            for p in c.points:
                p.x, p.y = self.x(p.x), p.y + dy


def runs1(line):
    out, s = [], None
    for i, v in enumerate(line):
        if v and s is None:
            s = i
        if not v and s is not None:
            out.append(i - s)
            s = None
    return out


def bitmap1(r):
    pen = FreeTypePen(None)
    r.replay(TransformPen(pen, (1, 0, 0, 1, 1000, 1200)))
    return pen.array(width=3300, height=3600, contain=False)[::-1] > 0.5


def row_widths(r, y):
    B = bitmap1(r)
    return runs1(B[1200 + y])


def col_widths(r, x):
    B = bitmap1(r)
    return runs1(B[:, 1000 + x])


# measuring sites in the fitted lowercase: rows through vertical strokes,
# columns through horizontal ones (y / x in the fitted letter)
G_V = [(0x03B7, 450), (0x03BF, 470), (0x03C5, 600), (0x03B9, 500), (0x03BD, 700), (0x03C3, 470),
       (0x03C0, 450)]
G_H = [(0x03BF, 614), (0x03C3, 520), (0x03C4, 450), (0x03C9, 330), (0x03B5, 614)]


def greek_strokes(font, cm):
    v, h = [], []
    for u, y in G_V:
        v += [w for w in row_widths(rec(font, cm[u]), y) if 90 < w < 230]
    for u, x in G_H:
        h += [w for w in col_widths(rec(font, cm[u]), x) if 80 < w < 230]
    return v, h


TERMINAL = 70      # a constructed stem's or bar's end: as round as the Latin's


def finish(g, radius=TERMINAL):
    for c in g.contours:
        round_contour(c, radius)
    round_all(g)
    tag(g)


def scaled(font, name, box, stroke=True):
    """a Latin glyph scaled into box (x0, y0, x1, y1), its stroke brought back
    to 150 / 144 (an outline RecordingPen)."""
    b = bounds(font, font[name])
    sx, sy = (box[2] - box[0]) / (b[2] - b[0]), (box[3] - box[1]) / (b[3] - b[1])
    tmp = ufoLib2.Font()
    t = tmp.newGlyph("t")
    set_outline(t, rec(font, name, Transform(sx, 0, 0, sy, box[0] - b[0] * sx, box[1] - b[1] * sy)))
    if stroke:
        restroke(t, STEM_V * (1 - sx) / 2, STEM_H * (1 - sy) / 2)
    out = RecordingPen()
    t.draw(out)
    return out


def stroke_seg(a, b, w, ext=0):
    """a straight stroke of width w from a to b (a quadrilateral)."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy * w / 2, ux * w / 2
    a = (a[0] - ux * ext, a[1] - uy * ext)
    b = (b[0] + ux * ext, b[1] + uy * ext)
    return poly([(a[0] + nx, a[1] + ny), (b[0] + nx, b[1] + ny), (b[0] - nx, b[1] - ny), (a[0] - nx, a[1] - ny)])


def build_capitals(font, cm):
    """the capitals: the Latin's where it has them, the rest from its parts."""
    done = []
    for u, latin in AS_LATIN.items():
        g = font[cm[u]]
        if fitted(g):
            continue
        g.clearContours()
        g.clearComponents()
        g.components.append(ufoLib2.objects.Component(baseGlyph=latin))
        g.width = CELL
        tag(g)
        done.append(chr(u))
    H = bounds(font, font["H"])
    s0, s1 = H[0], H[2]                      # the stems' outer edges, 175 / 1053
    mid = CELL / 2
    lo, hi = H[1], H[3]                      # -10 / 1197: a stem's rounded ends
    build = {}
    build[0x0393] = lambda: [rec(font, "L", Transform(1, 0, 0, -1, 0, CAP), reverse=True)]       # Gamma
    build[0x039B] = lambda: [rec(font, "V", Transform(1, 0, 0, -1, 0, CAP), reverse=True)]       # Lambda
    build[0x03A0] = lambda: [rect(s0, lo, s0 + STEM_V, CAP), rect(s1 - STEM_V, lo, s1, CAP),     # Pi
                             rect(s0, CAP - STEM_H, s1, CAP)]
    build[0x039E] = lambda: [rect(190, CAP - STEM_H, 1038, CAP), rect(330, CAP / 2 - STEM_H / 2, 898, CAP / 2 + STEM_H / 2),
                             rect(190, 0, 1038, STEM_H)]                                          # Xi
    vx, hd = 700, 184      # Sigma's point; a diagonal's horizontal width (the Latin Z's)
    build[0x03A3] = lambda: [rect(190, CAP - STEM_H, 1038, CAP), rect(190, 0, 1038, STEM_H),      # Sigma
                             poly([(190, CAP), (190 + hd, CAP), (vx, CAP / 2), (190 + hd, 0),
                                   (190, 0), (vx - hd, CAP / 2)])]
    build[0x0398] = lambda: [rec(font, "O"), rect(380, CAP / 2 - STEM_H / 2 + 11, 848, CAP / 2 + STEM_H / 2 + 11)]  # Theta
    build[0x03A6] = lambda: [scaled(font, "O", (140, 190, 1088, 1010)),                        # Phi
                             rect(mid - STEM_V / 2, lo, mid + STEM_V / 2, hi)]
    U = bounds(font, font["U"])
    build[0x03A8] = lambda: [scaled(font, "U", (U[0] + 30, 330, U[2] - 30, U[3])),            # Psi
                             rect(mid - STEM_V / 2, lo, mid + STEM_V / 2, hi)]
    build[0x03D8] = lambda: [scaled(font, "O", (235, 430, 993, 1209)),                         # archaic koppa
                             rect(mid - STEM_V / 2, lo, mid + STEM_V / 2, 500)]
    o = bounds(font, font["o"])
    build[0x03D9] = lambda: [scaled(font, "o", (265, 160, 963, o[3])),                         # small archaic koppa
                             rect(mid - STEM_V / 2, LAT_DESC, mid + STEM_V / 2, 230)]
    build[PROSGEGRAMMENI] = lambda: [rect(mid - STEM_V / 2, lo, mid + STEM_V / 2, 700)]        # iota adscript
    for u, f in build.items():
        if u not in cm or fitted(font[cm[u]]):
            continue
        g = font[cm[u]]
        set_outline(g, *f())
        g.width = CELL
        if u in (0x0393, 0x039B):
            round_all(g)
            tag(g)
        else:
            finish(g)
        done.append(chr(u))
    return done


def split_marks(font, g, base, orig):
    """an outline-built accented small letter: its accents are the contours
    wholly above the x-height or wholly under the line (these letters have no
    ascender, and their descender hangs from the letter); the rest is the
    letter, which must have the size of the unaccented one (orig, its contours
    before fitting). Returns the accents and the letter's offset."""
    marks, letter = [], []
    for c in g.contours:
        ys = [p.y for p in c.points]
        (marks if min(ys) > NNF_XH - 30 or max(ys) < -30 else letter).append(c)

    def box(cs):
        xs = [p.x for c in cs for p in c.points]
        ys = [p.y for c in cs for p in c.points]
        return min(xs), min(ys), max(xs), max(ys)
    if not letter:
        return marks, None
    a, b = box(letter), box(orig)
    if any(abs((a[i + 2] - a[i]) - (b[i + 2] - b[i])) > 12 for i in (0, 1)) or abs(a[1] - b[1]) > 12:
        return marks, None
    return marks, (round(a[0] - b[0]), 0)


def mark_weight(font, cm):
    names = [cm[u] for u in (0x0384, 0x1FBF, 0x1FFE, 0x1FC0, 0x1FEF, 0x1FFD) if u in cm]
    return stroke_estimate([rec(font, n) for n in names])


def place_capital(font, g, gm, flat, below_names):
    """a polytonic / tonos capital: its accent beside the letter (left), the
    iota adscript after it (right), a dialytika over it; the letter narrowed
    (stems restored) when the cell has no room."""
    base, rest = flat[0], flat[1:]
    bname = base[0]
    bb = bounds(font, font[bname])
    bc = (bb[0] + bb[2]) / 2
    left, right, centre = [], [], []
    for n, x, y in rest:
        mb = bounds(font, font[n])
        cx = (mb[0] + mb[2]) / 2 + x
        if n == cm_name(font, PROSGEGRAMMENI):
            right.append(n)
        elif n in OVER_CAPITAL:
            centre.append(n)
        else:
            left.append(n)
    # a lone tonos (modern Greek, at every sentence start) narrows the letter
    # little, then goes up at its left instead; the polytonic accents more
    tonos = left == [cm_name(font, 0x0384)] and not right
    ks = [1.0] + [1 - 0.03 * i for i in range(1, 4 if tonos else 7)]
    for k in ks:
        last = k == ks[-1]
        if k == 1.0:
            brec = rec(font, bname)
        else:
            xa = bb[2] if left and not right else bb[0] if right and not left else bc
            tmp = ufoLib2.Font()
            t = tmp.newGlyph("t")
            set_outline(t, rec(font, bname, Transform(k, 0, 0, 1, xa * (1 - k), 0)))
            restroke(t, STEM_V * (1 - k) / 2, 0)
            brec = RecordingPen()
            t.draw(brec)
        ink = Ink()
        ink.add(brec)
        b2 = rec_bounds(brec)
        comps, ok = [], True
        for n in left:
            r = rec(font, n)
            mb = rec_bounds(r)
            dy = CAP_TOP - mb[3]
            dx = rightmost_clear(ink, r, dy, (b2[0] + b2[2]) / 2 - mb[2], -mb[0] - 200)
            if dx is None or mb[0] + dx < LEFT_MIN:
                if not last:
                    ok = False
                    break
                # no room beside it: at the cell's left, as low as it clears the letter
                dx = LEFT_MIN - mb[0]
                dy = lowest_clear(ink, r, dx, dy)
            ink.add(r, dx, dy)
            comps.append((n, dx, dy))
        if ok:
            for n in right:
                r = rec(font, n)
                mb = rec_bounds(r)
                dx = leftmost_clear(ink, r, 0, (b2[0] + b2[2]) / 2 - mb[0], CELL - mb[2])
                if dx is None or mb[2] + dx > CELL - 10:
                    if not last:
                        ok = False
                        break
                    dx = CELL - 10 - mb[2]
                ink.add(r, dx, 0)
                comps.append((n, dx, 0))
        if ok:
            break
    for n in centre:
        r = rec(font, n)
        mb = rec_bounds(r)
        top_c = band_centre(font, bname, top=True)
        dx = top_c - (mb[0] + mb[2]) / 2
        dy = lowest_clear(ink, r, dx, b2[3] - mb[1] - 200, gap=90)
        ink.add(r, dx, dy)
        comps.append((n, dx, dy))
    g.clearContours()
    g.clearComponents()
    if k == 1.0:
        g.components.append(ufoLib2.objects.Component(baseGlyph=bname))
    else:
        brec.replay(g.getPen())
        round_all(g)
    for n, x, y in comps:
        g.components.append(ufoLib2.objects.Component(baseGlyph=n, transformation=(1, 0, 0, 1, round(x), round(y))))
    g.width = CELL
    tag(g)
    return k


def cm_name(font, u):
    for g in font:
        if u in g.unicodes:
            return g.name
    return None


def flatten(font, g, t=(0, 0)):
    out = []
    for c in g.components:
        x, y = c.transformation[4] + t[0], c.transformation[5] + t[1]
        sub = font[c.baseGlyph]
        if sub.components and not sub.contours and sub.unicodes and \
                0x1F00 <= sub.unicodes[0] <= 0x1FFF:
            out += flatten(font, sub, (x, y))
        else:
            out.append((c.baseGlyph, x, y))
    return out


def fit_greek(font):
    cm = cmap(font)
    if all(fitted(font[cm[u]]) for u in GREEK_SMALL if u in cm):
        print("Greek: already fitted")
        return
    gm = GreekMap(font, cm)
    acc_w = accent_weight(font)
    grow_m = max(0.0, (acc_w - mark_weight(font, cm)) / 2)
    # snapshot of the unfitted letters' outlines, to find them in the accented forms
    small = {cm[u] for u in GREEK_SMALL if u in cm}
    orig = {n: [c for c in font[n].contours] for n in small}
    orig = {n: [type("C", (), {"points": [type("P", (), {"x": p.x, "y": p.y, "type": p.type})() for p in c.points]})()
                for c in cs] for n, cs in orig.items()}
    # 1. the small letters: map, round, then the stroke measured and restored
    for n in small:
        g = font[n]
        if not g.contours:
            continue
        gm.letter(g)
        rounded(g)
        g.width = CELL
    v, h = greek_strokes(font, cm)
    dx = (STEM_V - statistics.median(v)) / 2
    dy = (STEM_H - statistics.median(h)) / 2
    for n in small:
        g = font[n]
        restroke(g, dx, dy)
        round_all(g)
        tag(g)
    # archaic capitals without a Latin model: scaled like the capitals
    capk = CAP / NNF_CAP
    for u in ARCHAIC_CAPS:
        if u not in cm or not font[cm[u]].contours:
            continue
        g = font[cm[u]]
        for c in g.contours:
            for p in c.points:
                p.x, p.y = gm.x(p.x), p.y * capk
        rounded(g)
        restroke(g, dx, dy)
        round_all(g)
        tag(g)
    # 2. capitals
    caps = build_capitals(font, cm)
    # 3. punctuation and spacing accents
    for u, latin in GREEK_PUNCT.items():
        g = font[cm[u]]
        g.clearContours()
        g.clearComponents()
        g.components.append(ufoLib2.objects.Component(baseGlyph=latin))
        tag(g)
    for u in SPACING_MARKS:
        if u not in cm:
            continue
        g = font[cm[u]]
        if not g.contours or fitted(g):
            continue
        b = bounds(font, g)
        gm.mark_contours(g.contours, below=b[3] < 300)
        restroke(g, grow_m, grow_m)
        rounded(g, CORNER * 0.8)
        round_all(g)
        tag(g)
    # 4. the accented small letters: the fitted letter + their own accents, fitted
    unmatched = []
    nacc = 0
    for g in font:
        if not g.unicodes or fitted(g) or not g.contours:
            continue
        u = g.unicodes[0]
        if not (0x0370 <= u <= 0x03FF or 0x1F00 <= u <= 0x1FFF):
            continue
        base = ud.normalize("NFD", chr(u))[0]
        bn = cm.get(ord(base))
        if bn not in small:
            continue
        marks, shift = split_marks(font, g, bn, orig[bn])
        if shift is None:
            unmatched.append(g.name)
            continue
        below = [c for c in marks if max(p.y for p in c.points) < 200]
        above = [c for c in marks if c not in below]
        gm.mark_contours(above)
        gm.mark_contours(below, below=True)
        keep = []
        for c in marks:
            r = contour_rec(c)
            keep.append(r)
        g.clearContours()
        tmp = ufoLib2.Font()
        t = tmp.newGlyph("t")
        set_outline(t, *keep)
        restroke(t, grow_m, grow_m)
        rounded(t, CORNER * 0.8)
        round_all(t)
        t.draw(g.getPen())
        g.components.insert(0, ufoLib2.objects.Component(
            baseGlyph=bn, transformation=(1, 0, 0, 1, round(shift[0] * gm.sx), round(gm.y(shift[1]) if shift[1] else 0))))
        g.width = CELL
        tag(g)
        nacc += 1
    # 5. the capitals with accents: as the Latin's where it has them, ...
    top_prec, _ = precedents(font, set())
    for u, (b, acc) in AS_LATIN_ACCENTED.items():
        if u not in cm or fitted(font[cm[u]]):
            continue
        g = font[cm[u]]
        adx, ady = top_prec.get(b, (0, 270))
        g.clearContours()
        g.clearComponents()
        g.components.append(ufoLib2.objects.Component(baseGlyph=b))
        g.components.append(ufoLib2.objects.Component(baseGlyph=acc, transformation=(1, 0, 0, 1, adx, ady)))
        g.width = CELL
        tag(g)
    # ... rho with dasia (an outline) as the others: the letter and the accent beside it
    if 0x1FEC in cm and not fitted(font[cm[0x1FEC]]):
        g = font[cm[0x1FEC]]
        g.clearContours()
        place_capital(font, g, gm, [("P", 0, 0), (cm[0x1FFE], -400, 0)], ())
    # ... and the polytonic ones beside the letter (composites)
    squeezed = []
    ncap = 0
    todo = []
    for g in font:
        if not g.unicodes or fitted(g) or not g.components or g.contours:
            continue
        u = g.unicodes[0]
        if 0x0370 <= u <= 0x03FF or 0x1F00 <= u <= 0x1FFF:
            todo.append((g, flatten(font, g)))     # before any of them is rebuilt
    for g, flat in todo:
        flat.sort(key=lambda c: 0 if font[c[0]].unicodes and ud.category(chr(font[c[0]].unicodes[0])) == "Lu" else 1)
        k = place_capital(font, g, gm, flat, ())
        ncap += 1
        if k < 1:
            squeezed.append((g.name, round(k, 2)))
    print(f"Greek: x {gm.sx:.3f} about {NNF_CX}, y {gm.k:.3f} to the x-height, ascenders {gm.ka:.3f}, "
          f"descenders {gm.kd:.3f}; stroke {statistics.median(v):.0f}/{statistics.median(h):.0f} -> "
          f"offset {dx:.1f}/{dy:.1f}; accents +{grow_m:.1f}")
    print(f"  capitals: {''.join(caps)}; {nacc} accented small letters, {ncap} accented capitals "
          f"({len(squeezed)} narrowed: {squeezed})")
    if unmatched:
        print(f"  NOT rebuilt (letter not found in the outline): {unmatched}")


# --- Arabic -------------------------------------------------------------------

DOT_ROUND = 80        # a square dot's corners: like the Latin's dot (190 wide, rounded 76)
MARK_ROUND = 52       # a vowel mark's ends (stroke 124): the Latin's terminal, scaled


def on_edge(x, y):
    return abs(x) < 0.5 or abs(x - CELL) < 0.5


def arabic_glyphs(font):
    """every Arabic glyph with an outline (letters, marks, digits, punctuation)."""
    for g in font:
        if g.contours and _ara._mma.family_of_glyph(g) == "Arab":
            yield g


def arabic_stem(font, cm):
    """the alef's stem (it is a plain vertical stroke)."""
    r = rec(font, cm[0x0627])
    b = rec_bounds(r)
    return statistics.median(w for y in range(int(b[1]) + 150, int(b[3]) - 150, 50)
                             for w in row_widths(r, y))


CAP_DEPTH = 0.45      # a stem's round end: this deep for its width (the Latin's 65 / 150)
CAP_FLAT = 50         # an end flatter than this was flattened by fit-arabic.py's map
KAPPA = 0.55


def restore_caps(c):
    """fit-arabic.py's vertical map shortened the ascenders (0.32) and the deep
    descenders (0.2) and so flattened the round ends of their stems (beh's
    horn: 83 deep in the donor, 27 after). Give such an end back its depth:
    the extreme point stays (so do the heights), the two shoulder points move
    down (up) their stem's straight sides, the handles make a quarter ellipse
    each side."""
    pts = list(c.points)
    n = len(pts)
    done = 0
    for i, t in enumerate(pts):
        if t.type != "curve" or n < 9:
            continue
        s1, s2 = pts[(i - 3) % n], pts[(i + 3) % n]
        offs = [pts[(i + k) % n] for k in (-2, -1, 1, 2)]
        if any(o.type is not None for o in offs) or s1.type is None or pts[(i + 3) % n].type != "curve":
            continue
        top = t.y > s1.y
        if abs(s1.y - s2.y) > 3 or not (t.y > 800 or t.y < 225):
            continue
        if (t.y - s1.y) * (1 if top else -1) <= 0:
            continue
        w = abs(s1.x - s2.x)
        d = abs(t.y - s1.y)
        if not (90 <= w <= 230) or d >= CAP_FLAT or not min(s1.x, s2.x) < t.x < max(s1.x, s2.x):
            continue
        # the straight sides the shoulders slide along
        a, b = pts[(i - 4) % n], pts[(i + 4) % n]
        if s1.type != "line" or b.type != "line" or abs(a.x - s1.x) > 1 or abs(b.x - s2.x) > 1:
            continue
        D = CAP_DEPTH * w
        sgn = -1 if top else 1                   # from the end into the stem
        ny = t.y + sgn * D
        if (ny - a.y) * sgn >= -10 or (ny - b.y) * sgn >= -10:
            continue                             # the side is too short
        s1.y = s2.y = ny
        h1, h2, h3, h4 = offs
        h1.x, h1.y = s1.x, ny - sgn * KAPPA * D
        h2.x, h2.y = t.x + KAPPA * (s1.x - t.x), t.y
        h3.x, h3.y = t.x + KAPPA * (s2.x - t.x), t.y
        h4.x, h4.y = s2.x, ny - sgn * KAPPA * D
        done += 1
    return done


def fit_arabic(font):
    cm = cmap(font)
    todo = [g for g in arabic_glyphs(font) if not fitted(g)]
    if not todo:
        print("Arabic: already fitted")
        return
    stem = arabic_stem(font, cm)
    dx = (STEM_V - stem) / 2
    nl = nd = nm = corners = caps = 0
    for g in todo:
        mark = _ara.is_mark(g)
        dots = set() if mark else _ara.dots_of(g)
        for i, c in enumerate(g.contours):
            if mark:
                corners += round_contour(c, MARK_ROUND)
                continue
            if i in dots:
                xs = [p.x for p in c.points]
                ys = [p.y for p in c.points]
                if max(xs) - min(xs) < 300 and max(ys) - min(ys) < 300:
                    corners += round_contour(c, DOT_ROUND)
                    nd += 1
                else:          # a hamza, wasla or kaf's sign: a stroke
                    corners += round_contour(c, MARK_ROUND)
                continue
            caps += restore_caps(c)
            offset_contour(c, dx, 0, pin=on_edge)
            corners += round_contour(c, CORNER, skip=on_edge)
        round_all(g)
        tag(g)
        nm += mark
        nl += not mark
    print(f"Arabic: stem {stem:.0f} -> +{dx:.1f} each side (x only, the cell's edges kept); "
          f"{nl} letters/signs, {nm} marks, {nd} dots; {caps} flattened stem ends made round again, "
          f"{corners} corners rounded")


def check(font, against=None):
    """the fit, measured: Latin composites, Greek strokes and cell, Arabic edges
    and heights (against: the UFO before the fit)."""
    ok = True
    cm = cmap(font)
    # Latin
    lat = merged_latin(font)
    bad = [g.name for g in lat if (not fitted(g) and g.unicodes[0] != 0x017F) or (g.contours and g.unicodes[0] not in OUTLINE_LATIN)]
    out = []
    for g in lat:
        b = bounds(font, g)
        if b[0] < -5 or b[2] > CELL + 5:
            out.append((g.name, round(b[0]), round(b[2])))
    print(f"Latin: {len(lat)} merged letters; not Courier composites: {bad or 'none'}; "
          f"ink outside the cell: {out or 'none'}")
    ok &= not bad
    # Greek
    v, h = greek_strokes(font, cm)
    mv, mh = statistics.median(v), statistics.median(h)
    print(f"Greek small letters: vertical strokes median {mv:.0f} (target {STEM_V:.0f}), "
          f"horizontal {mh:.0f} (target {STEM_H:.0f})")
    ok &= abs(mv - STEM_V) <= 6 and abs(mh - STEM_H) <= 8
    greek = [g for g in font if g.unicodes and (0x0370 <= g.unicodes[0] <= 0x03FF or 0x1F00 <= g.unicodes[0] <= 0x1FFF)]
    unf = [g.name for g in greek if not fitted(g) and g.unicodes[0] not in COURIER_GREEK and (g.contours or g.components)]
    out = []
    for g in greek:
        b = bounds(font, g)
        if b and g.width and (b[0] < LEFT_MIN - 5 or b[2] > CELL + 5):
            out.append((g.name, round(b[0]), round(b[2])))
    print(f"Greek: {len(greek)} glyphs; not fitted: {unf or 'none'}; ink outside [{LEFT_MIN}, {CELL}]: {out or 'none'}")
    ok &= not unf and not out
    caps = [g.name for g in greek if g.unicodes[0] in AS_LATIN and
            [c.baseGlyph for c in g.components] != [AS_LATIN[g.unicodes[0]]]]
    print(f"Greek capitals the Latin has, not the Latin's: {caps or 'none'}")
    ok &= not caps
    # Arabic
    ar = list(arabic_glyphs(font))
    unf = [g.name for g in ar if not fitted(g)]
    print(f"Arabic: {len(ar)} glyphs, not fitted: {unf or 'none'}")
    ok &= not unf
    if against:
        old = ufoLib2.Font.open(against)
        moved, taller = [], []
        for g in ar:
            if g.name not in old or _ara.kind(g) != "letter":
                continue
            o = old[g.name]
            e1 = sorted((round(p.x), round(p.y)) for c in g.contours for p in c.points if on_edge(p.x, p.y))
            e0 = sorted((round(p.x), round(p.y)) for c in o.contours for p in c.points if on_edge(p.x, p.y))
            if e1 != e0:
                moved.append(g.name)
            b1, b0 = bounds(font, g), bounds(old, o)
            if b0 and (b1[1] < b0[1] - 1 or b1[3] > b0[3] + 1):
                taller.append((g.name, round(b0[1]), round(b0[3]), round(b1[1]), round(b1[3])))
        print(f"Arabic against {against}: join points moved: {moved or 'none'}; "
              f"taller or deeper: {taller or 'none'}")
        ok &= not moved and not taller
    print("CHECK", "OK" if ok else "FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--against", default=None, help="with --check: the UFO before the fit")
    ap.add_argument("--only", default="latin,greek,arabic")
    args = ap.parse_args()
    font = ufoLib2.Font.open(args.ufo)
    if args.check:
        sys.exit(0 if check(font, args.against) else 1)
    only = set(args.only.split(","))
    if "latin" in only:
        built, kept, nc = fit_latin(font)
        print(f"Latin: rebuilt {len(built)} as Courier composites, {nc} combining marks; "
              f"left: {' '.join(kept) or 'none'}")
    if "greek" in only:
        fit_greek(font)
    if "arabic" in only:
        fit_arabic(font)
    font.save()


if __name__ == "__main__":
    main()
