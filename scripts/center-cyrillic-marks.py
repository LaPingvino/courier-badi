#!/usr/bin/env python3
"""Recenter symmetric top diacritics on precomposed Cyrillic glyphs.

The Cyrillic set merged from Novikov's fork stores accented letters as
standalone outlines (not components), and several have their top mark shifted
horizontally off the base's center. This corrects only the SAFE cases:

  - the mark is a symmetric top mark (breve, dieresis/trema, macron, dot above,
    double acute) identified via the glyph's Unicode decomposition, and
  - the base is not a dotted i/j-type letter (whose own dot would be mistaken
    for the mark).

For each such glyph the mark contours (those sitting above the base) are shifted
horizontally so their center matches the standalone base glyph's center. Bases
are left untouched. Run once against the UFO; re-run safely (idempotent).

Usage: python3 scripts/center-cyrillic-marks.py [--apply] [--ufo PATH]
Without --apply it only reports what it would change.
"""
import argparse
import os
import re
import unicodedata as ud

SAFE_MARKS = {0x0304: "macron", 0x0306: "breve", 0x0308: "dieresis",
              0x0307: "dotabove", 0x030B: "dblacute"}
DOTTED_BASES = {0x0069, 0x006A, 0x0406, 0x0408, 0x0456, 0x0458}
TOL = 4  # don't bother shifting less than this many units


def load_cmap(gdir):
    import plistlib
    contents = plistlib.load(open(os.path.join(gdir, "contents.plist"), "rb"))
    cp2name, name2file = {}, {}
    for name, fn in contents.items():
        name2file[name] = fn
        d = open(os.path.join(gdir, fn), encoding="utf-8").read()
        for m in re.findall(r'<unicode hex="([0-9A-Fa-f]+)"', d):
            cp2name.setdefault(int(m, 16), name)
    return cp2name, name2file


def contour_bounds(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def parse_contours(text):
    """Return list of (raw_contour_string, points)."""
    out = []
    for ct in re.findall(r"<contour>.*?</contour>", text, re.S):
        pts = [(float(x), float(y)) for x, y in
               re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', ct)]
        if pts:
            out.append((ct, pts))
    return out


def glyph_bounds(gdir, name2file, name):
    d = open(os.path.join(gdir, name2file[name]), encoding="utf-8").read()
    cs = parse_contours(d)
    if not cs:
        return None
    xs = [b for _, pts in cs for b in (min(p[0] for p in pts), max(p[0] for p in pts))]
    ys = [b for _, pts in cs for b in (min(p[1] for p in pts), max(p[1] for p in pts))]
    return min(xs), min(ys), max(xs), max(ys)


def shift_contour_x(ct_text, dx):
    def repl(m):
        return f'x="{float(m.group(1)) + dx:g}"'
    return re.sub(r'x="(-?[0-9.]+)"', repl, ct_text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    gdir = os.path.join(args.ufo, "glyphs")
    cp2name, name2file = load_cmap(gdir)

    changed = 0
    for cp in range(0x0400, 0x0530):
        name = cp2name.get(cp)
        if not name:
            continue
        dec = ud.decomposition(chr(cp))
        if not dec or dec.startswith("<"):
            continue
        parts = [int(x, 16) for x in dec.split()]
        if len(parts) != 2:
            continue
        basecp, markcp = parts
        if markcp not in SAFE_MARKS or basecp in DOTTED_BASES:
            continue
        base_name = cp2name.get(basecp)
        if not base_name or base_name not in name2file:
            continue
        bb = glyph_bounds(gdir, name2file, base_name)
        if not bb:
            continue
        base_cx = (bb[0] + bb[2]) / 2
        base_top = bb[3]

        path = os.path.join(gdir, name2file[name])
        text = open(path, encoding="utf-8").read()
        if "<component" in text:
            continue  # already component-based, positioned elsewhere
        cs = parse_contours(text)
        if len(cs) < 2:
            continue
        # Mark contours: those sitting at/above the base's top.
        mark = [(ct, pts) for ct, pts in cs if min(p[1] for p in pts) >= base_top - 40]
        body = [(ct, pts) for ct, pts in cs if (ct, pts) not in mark]
        if not mark or not body:
            continue
        # Sanity: the body must actually line up with the standalone base center,
        # otherwise the base was repositioned and we should not trust it.
        body_xs = [b for _, pts in body for b in
                   (min(p[0] for p in pts), max(p[0] for p in pts))]
        body_cx = (min(body_xs) + max(body_xs)) / 2
        if abs(body_cx - base_cx) > 25:
            continue
        mark_xs = [b for _, pts in mark for b in
                   (min(p[0] for p in pts), max(p[0] for p in pts))]
        mark_cx = (min(mark_xs) + max(mark_xs)) / 2
        dx = base_cx - mark_cx
        if abs(dx) < TOL:
            continue
        print(f"U+{cp:04X} {name} ({SAFE_MARKS[markcp]} over {base_name}): shift {dx:+.0f}")
        if args.apply:
            new = text
            for ct, _ in mark:
                new = new.replace(ct, shift_contour_x(ct, dx), 1)
            open(path, "w", encoding="utf-8").write(new)
        changed += 1
    print(f"{'Applied' if args.apply else 'Would change'} {changed} glyphs")


if __name__ == "__main__":
    main()
