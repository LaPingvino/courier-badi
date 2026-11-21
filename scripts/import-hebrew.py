#!/usr/bin/env python3
"""Import the Hebrew block from the donor font (Cousine) into the Regular UFO.

This is the *raw* import: outlines in donor coordinates (only converted to
cubics with canonical PostScript winding, outer CCW / holes CW, via
skia-pathops -- the same normalisation as normalize-winding.py), plus the
donor's mark-attachment data turned into named UFO anchors. Fitting to Courier
Badi's metrics and stroke is a separate step (scripts/fit-hebrew.py), so the
two can be checked independently.

Donor: Cousine Regular (SIL OFL 1.1; Copyright 2026 The Cousine Project
Authors, https://github.com/googlefonts/cousine; Hebrew outlines identical to
Liberation Mono 2.1.5, designed by Steve Matteson / Monotype). Fetch it from
google/fonts:
  https://raw.githubusercontent.com/google/fonts/main/ofl/cousine/Cousine-Regular.ttf

What is imported:
  - letters U+05D0-05EA, Yiddish ligatures U+05F0-05F2, punctuation
    (maqaf, paseq, sof pasuq, nun hafukha, geresh, gershayim) as outlines;
  - points and cantillation marks U+0591-05C7 and U+FB1E as zero-width
    outlines (advance 0);
  - U+FB20 (alternative ayin), U+FB29 (alternative plus) and U+FB4F
    (alef-lamed) as outlines;
  - the presentation forms U+FB1D-FB4E are NOT imported as outlines: they are
    composites (base + mark components) built here and positioned from the
    anchors by fit-hebrew.py. The "wide" letters U+FB21-FB28 cannot be wider in
    a monospace, so they are plain references to their base letter.
U+05EF (yod triangle) is not in the donor and is not drawn.

Anchors. The donor positions marks with ten single-class mark-to-base lookups
(plus ccmp compositions into the presentation forms). Each class becomes one
anchor name; a base's anchor comes from the donor's GPOS, or -- for the classes
the donor handles by composition instead (dagesh, shin/sin dot, holam on vav,
rafe) -- from the offset of the mark component in the donor's precomposed form.
Mark-to-mark anchors (for stacking cantillation) are added by fit-hebrew.py.

Every imported glyph is tagged in its lib with HEBREW_KEY = "imported";
fit-hebrew.py fits only glyphs in that state and retags them "fitted", so the
pair is idempotent: re-running the import resets the Hebrew to pristine.

Usage:
  python3 scripts/import-hebrew.py --donor Cousine-Regular.ttf \
      [--ufo sources/CourierBadi-Regular.ufo]
"""
import argparse
import unicodedata as ud

import pathops
import ufoLib2
from fontTools.pens.basePen import BasePen
from fontTools.pens.qu2cuPen import Qu2CuPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.ttLib import TTFont

HEBREW_KEY = "org.courierbadi.hebrew"

# Donor GPOS 'mark' lookups (indices in Cousine-Regular.ttf 1.241) -> anchor
# name. 8 (Masoretic lower dot) and 16 (upper dot) have base anchors of their
# own, so they keep their own classes. 13 (shin dot) covers only the dotted
# circle; the donor puts it on shin by composition, see COMPOSED_CLASSES.
# (merge_classes folds lookups mapped to the same name, checking their base
# anchors differ by a constant; none currently do.)
LOOKUP_ANCHOR = {
    7: "bottom", 8: "lowerdot",
    9: "topleft",        # pashta, telisha qetana, zinor (post-positive)
    10: "holam",
    11: "topright",      # geresh muqdam, telisha gedola (pre-positive)
    12: "bottomright",   # yetiv, dehi (pre-positive)
    13: "shindot",
    14: "center",        # dagesh / mapiq / shuruq dot
    15: "top", 16: "upperdot",
}
# classes whose base anchors the donor supplies (also) through precomposed
# forms; those fill in bases the GPOS lookup does not cover.
COMPOSED_CLASSES = {"center", "shindot", "sindot", "holam", "top"}

CELL = 1228


def cp_name(cp):
    return "uni%04X" % cp


def is_mark(cp):
    return ud.category(chr(cp)) in ("Mn", "Me")


def full_decomposition(cp):
    d = ud.decomposition(chr(cp))
    if not d or d.startswith("<"):
        return None
    out = []
    for h in d.split():
        sub = full_decomposition(int(h, 16))
        out += sub if sub else [int(h, 16)]
    return out


def outline_codepoints(cmap):
    cps = [c for c in range(0x0591, 0x05C8) if c in cmap]
    cps += [c for c in range(0x05D0, 0x05EB) if c in cmap]
    cps += [c for c in range(0x05F0, 0x05F5) if c in cmap]
    cps += [c for c in (0xFB1E, 0xFB20, 0xFB29, 0xFB4F) if c in cmap]
    return cps


def composite_codepoints(cmap):
    return [c for c in range(0xFB1D, 0xFB50)
            if c in cmap and c not in (0xFB1E, 0xFB20, 0xFB29, 0xFB4F)]


class QuadToCubicPen(BasePen):
    """Exact degree elevation of every quadratic segment, so the TrueType
    donor (including its on-curve-less dots) reaches pathops as cubics."""

    def __init__(self, out):
        super().__init__(None)
        self.out = out

    def _moveTo(self, p):
        self.out.moveTo(p)

    def _lineTo(self, p):
        self.out.lineTo(p)

    def _curveToOne(self, a, b, c):
        self.out.curveTo(a, b, c)

    def _qCurveToOne(self, a, b):
        p0 = self._getCurrentPoint()
        c1 = (p0[0] + 2 / 3 * (a[0] - p0[0]), p0[1] + 2 / 3 * (a[1] - p0[1]))
        c2 = (b[0] + 2 / 3 * (a[0] - b[0]), b[1] + 2 / 3 * (a[1] - b[1]))
        self.out.curveTo(c1, c2, b)

    def _closePath(self):
        self.out.closePath()


def donor_outline(gs, gname):
    """Donor glyph -> skia path with canonical winding (outer CCW)."""
    rp = DecomposingRecordingPen(gs)
    gs[gname].draw(rp)
    path = pathops.Path()
    rp.replay(QuadToCubicPen(path.getPen()))
    path.simplify()
    return path


def read_gpos_anchors(font):
    """{anchorName: {'bases': {donorGlyph: (x, y)}, 'marks': {donorGlyph: (x, y)}}}"""
    gpos = font["GPOS"].table
    out = {}
    for idx, name in LOOKUP_ANCHOR.items():
        lk = gpos.LookupList.Lookup[idx]
        assert lk.LookupType == 4, (idx, lk.LookupType)
        st = lk.SubTable[0]
        bases = {b: (r.BaseAnchor[0].XCoordinate, r.BaseAnchor[0].YCoordinate)
                 for b, r in zip(st.BaseCoverage.glyphs, st.BaseArray.BaseRecord)
                 if r.BaseAnchor[0] is not None}
        marks = {m: (r.MarkAnchor.XCoordinate, r.MarkAnchor.YCoordinate)
                 for m, r in zip(st.MarkCoverage.glyphs, st.MarkArray.MarkRecord)}
        out.setdefault(name, []).append((idx, bases, marks))
    return out


def merge_classes(raw):
    """Fold the duplicate lookups (7+8, 15+16) into one anchor class each, by
    expressing the second lookup's marks relative to the first's base anchors.
    Checks that the base-anchor difference is constant."""
    merged = {}
    for name, parts in raw.items():
        _, bases, marks = parts[0]
        bases, marks = dict(bases), dict(marks)
        for idx, b2, m2 in parts[1:]:
            diffs = {(b2[g][0] - bases[g][0], b2[g][1] - bases[g][1])
                     for g in b2 if g in bases}
            assert len(diffs) == 1, (name, idx, diffs)
            ddx, ddy = diffs.pop()
            for m, (x, y) in m2.items():
                marks[m] = (x - ddx, y - ddy)
        merged[name] = {"bases": bases, "marks": marks}
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--donor", required=True)
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    args = ap.parse_args()

    donor = TTFont(args.donor)
    dcmap = donor.getBestCmap()
    dname2cp = {}
    for c, n in dcmap.items():
        dname2cp.setdefault(n, c)
    gs = donor.getGlyphSet()
    glyf = donor["glyf"]
    classes = merge_classes(read_gpos_anchors(donor))

    # mark -> its (single) anchor class
    mark_class = {}
    for name, d in classes.items():
        for m in d["marks"]:
            assert m not in mark_class, m
            mark_class[m] = name
    # sin dot: same class geometry as the shin dot (the donor positions it only
    # by composition); holam haser for vav (U+05BA) behaves like holam, with
    # its anchor raised by the difference in how high the two are drawn.
    # The donor draws the sin dot higher than the shin dot and, in its
    # precomposed sin forms, uses the *shin dot* glyph moved left; so the sin
    # dot's anchor is the shin dot's raised by the drawing difference, and a
    # shin-dot component in a form that decomposes to U+05C2 means "sin dot".
    shindot, sindot = dcmap[0x05C1], dcmap[0x05C2]
    sx_, sy_ = classes["shindot"]["marks"][shindot]
    lift = donor_outline(gs, sindot).bounds[1] - donor_outline(gs, shindot).bounds[1]
    classes["sindot"] = {"bases": {}, "marks": {sindot: (sx_, sy_ + lift)}}
    mark_class[sindot] = "sindot"
    if 0x05BA in dcmap:
        hol = dcmap[0x05B9]
        hx, hy = classes["holam"]["marks"][hol]
        b1 = donor_outline(gs, hol).bounds
        b2 = donor_outline(gs, dcmap[0x05BA]).bounds
        classes["holam"]["marks"][dcmap[0x05BA]] = (hx, hy + (b2[1] - b1[1]))
        mark_class[dcmap[0x05BA]] = "holam"
    # dotted circle: sin dot mirrors the shin dot
    circle = dcmap.get(0x25CC)
    if circle and circle in classes["shindot"]["bases"]:
        x, y = classes["shindot"]["bases"][circle]
        classes["sindot"]["bases"][circle] = (donor["hmtx"][circle][0] - x, y)

    # Fill-in base anchors from the donor's precomposed forms (ccmp targets).
    for cp in range(0xFB1D, 0xFB50):
        if cp not in dcmap:
            continue
        g = glyf[dcmap[cp]]
        if not g.isComposite():
            continue
        comps = g.components
        base = comps[0]
        if base.glyphName in mark_class:
            # e.g. yodyod+patah lists the mark first
            bases = [c for c in comps if c.glyphName not in mark_class]
            if len(bases) != 1:
                continue
            base = bases[0]
        sin_form = 0x05C2 in (full_decomposition(cp) or [])
        for c in comps:
            cls = mark_class.get(c.glyphName)
            if cls is None or cls not in COMPOSED_CLASSES:
                continue
            mx, my = classes[cls]["marks"][c.glyphName]
            if sin_form and cls == "shindot":
                cls = "sindot"
            ax, ay = mx + c.x - base.x, my + c.y - base.y
            classes[cls]["bases"].setdefault(base.glyphName, (ax, ay))

    font = ufoLib2.Font.open(args.ufo)
    # reset: drop any earlier Hebrew import (idempotent)
    for g in list(font):
        if g.lib.get(HEBREW_KEY) in ("imported", "fitted"):
            del font[g.name]

    # donor name -> our glyph name
    ourname = {dcmap[c]: cp_name(c) for c in outline_codepoints(dcmap)}

    n_out = 0
    for cp in outline_codepoints(dcmap):
        dn = dcmap[cp]
        name = cp_name(cp)
        if name in font:
            del font[name]
        g = font.newGlyph(name)
        g.unicodes = [cp]
        g.width = 0 if is_mark(cp) else CELL
        path = donor_outline(gs, dn)
        path.draw(Qu2CuPen(g.getPen(), max_err=0.5, all_cubic=True))
        if is_mark(cp):
            cls = mark_class.get(dn)
            if cls:
                x, y = classes[cls]["marks"][dn]
                g.appendAnchor({"name": "_" + cls, "x": x, "y": y})
        else:
            for cls, d in sorted(classes.items()):
                if dn in d["bases"]:
                    x, y = d["bases"][dn]
                    g.appendAnchor({"name": cls, "x": x, "y": y})
        g.lib[HEBREW_KEY] = "imported"
        n_out += 1

    # Presentation forms: base + mark components (offsets set by fit-hebrew.py).
    n_comp = 0
    for cp in composite_codepoints(dcmap):
        parts = full_decomposition(cp)
        if parts is None:
            # wide letters FB21-FB28: <font> compatibility forms of one letter
            d = ud.decomposition(chr(cp))
            parts = [int(d.split()[-1], 16)]
        names = [cp_name(p) for p in parts]
        if not all(n in font for n in names):
            print(f"skip {cp:04X}: missing {names}")
            continue
        name = cp_name(cp)
        if name in font:
            del font[name]
        g = font.newGlyph(name)
        g.unicodes = [cp]
        g.width = CELL
        pen = g.getPen()
        for n in names:
            pen.addComponent(n, (1, 0, 0, 1, 0, 0))
        g.lib[HEBREW_KEY] = "imported"
        n_comp += 1

    # anchors on Courier Badi's own dotted circle, mapped from the donor's
    # circle by bounding box (so marks shown on U+25CC sit on it)
    if circle and "uni25CC" in font:
        from fontTools.pens.boundsPen import BoundsPen
        db = donor_outline(gs, circle).bounds
        bp = BoundsPen(font)
        font["uni25CC"].draw(bp)
        ob = bp.bounds
        g = font["uni25CC"]
        g.anchors.clear()
        for cls, d in sorted(classes.items()):
            if circle in d["bases"]:
                x, y = d["bases"][circle]
                # x: map circle to circle; y: keep the donor height (the
                # anchors sit at letter height, not circle height)
                nx = ob[0] + (x - db[0]) * (ob[2] - ob[0]) / (db[2] - db[0])
                g.appendAnchor({"name": cls, "x": round(nx), "y": y})
        # "anchors": only the anchors are Hebrew (fit-hebrew.py scales their y)
        g.lib[HEBREW_KEY] = "anchors"

    font.save()
    print(f"{args.ufo}: imported {n_out} outline glyphs and {n_comp} composites "
          f"from {args.donor}; anchor classes: {', '.join(sorted(classes))}")


if __name__ == "__main__":
    main()
