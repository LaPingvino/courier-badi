#!/usr/bin/env python3
"""Widen the cramped teeth of the seen/sheen (and sad/dad) family in the UFO.

The seen/sheen/sad letters merged from No Name Fixed have their tooth/loop
cluster scrunched into a narrow band with a large empty bowl, which reads poorly
(see google/fonts#6491). This spreads the teeth so they fill the cell, WITHOUT
fattening the strokes and WITHOUT letting the tooth-cluster leave the box.

The teeth cluster is widened to the SAME width in every positional form, and
always kept inside the cell -- only the connectors/tail change per position:
  - isolated / final: teeth spread left, anchored at the right; the free
    terminal tail smuggles out past the left edge (word-end / margin).
  - initial / medial: only the teeth *cluster* is stretched (the tall uprights);
    the baseline connector(s) that reach the cell edge are held and compress to
    make room, so the join strokes stay pinned to the edge and nothing overhangs
    into the neighbouring letter.
In all cases an x-direction inset thins the now-fattened vertical stems back to
their original width, restoring a constant (monolinear) stroke; horizontal
strokes (normal.x ~ 0) are untouched. Dots (nukat) keep their shape and are only
repositioned to stay over the spread teeth.

Run once from pristine glyphs. Usage:
  python3 scripts/widen-seen-family.py [--scale 1.5] [--delta 29] [--apply]
"""
import argparse
import math
import os
import re
import unicodedata as ud

# The seen/sheen (teeth) and sad/dad (loop) family, derived from the font's
# cmap by Unicode letter name so every dotted variant (two-dot, four-dot, ...)
# is covered automatically.
FAMILY_RE = re.compile(r"ARABIC LETTER (SEEN|SHEEN|SAD|DAD)\b")


def family_codepoints(cp2name):
    out = []
    for cp in sorted(cp2name):
        try:
            name = ud.name(chr(cp))
        except ValueError:
            continue
        # base letters only, not the FBxx/FExx presentation forms
        if FAMILY_RE.search(name) and "FORM" not in name:
            out.append(cp)
    return out


def is_accent_dot(pts):
    """A contour is a diacritic dot (to be translated, not scaled) only if it is
    a small mark sitting well ABOVE or BELOW the letter body. Structural
    counters inside the body (e.g. the sad/dad loop) are NOT dots and must be
    scaled with the body."""
    ys = [p[1] for p in pts]
    return len(pts) < 15 and (min(ys) >= 1000 or max(ys) <= 150)


def load(ufo):
    import plistlib
    gdir = os.path.join(ufo, "glyphs")
    contents = plistlib.load(open(os.path.join(gdir, "contents.plist"), "rb"))
    cp2name = {}
    for n, fn in contents.items():
        for m in re.findall(r'<unicode hex="([0-9A-Fa-f]+)"', open(os.path.join(gdir, fn)).read()):
            cp2name.setdefault(int(m, 16), n)
    return gdir, contents, cp2name


def forms_by_position():
    """(base_cp, pos) -> presentation-form cp, from the Unicode database."""
    tags = {"initial": "init", "medial": "medi", "final": "fina"}
    out = {}
    for cp in list(range(0xFB50, 0xFE00)) + list(range(0xFE70, 0xFF00)):
        d = ud.decomposition(chr(cp))
        if d.startswith("<"):
            tag = d[1:d.index(">")]
            if tag in tags:
                comps = d[d.index(">") + 1:].split()
                if len(comps) == 1:
                    out.setdefault((int(comps[0], 16), tags[tag]), cp)
    return out


def form_glyph(contents, cp2name, fp, isol, bcp, pos):
    fcp = fp.get((bcp, pos))
    if fcp and cp2name.get(fcp):
        return cp2name[fcp]
    if fcp and ("uni%04X" % fcp) in contents:
        return "uni%04X" % fcp
    if isol and f"{isol}.{pos}" in contents:
        return f"{isol}.{pos}"
    return None


def plan(contents, cp2name):
    """Return [(glyph, op)] where op is 'widen' (isolated/final) or 'lower'
    (initial/medial)."""
    fp = forms_by_position()
    out = []
    seen_names = set()
    def add(g, op):
        if g and g not in seen_names:
            seen_names.add(g)
            out.append((g, op))
    for bcp in family_codepoints(cp2name):
        isol = cp2name.get(bcp)
        add(isol, "widen")
        for pos, op in (("fina", "widen"), ("init", "init"), ("medi", "medi")):
            add(form_glyph(contents, cp2name, fp, isol, bcp, pos), op)
    return out


CELL = 1228.0
EDGE_EPS = 0.5  # a point mapped exactly onto a cell edge is a join connector


def _pinned_to_edge(x):
    """True if x sits on a cell boundary (0 or CELL) -- i.e. it is a join
    connector point that must stay put, not be pulled in by the stem inset."""
    return abs(x) < EDGE_EPS or abs(x - CELL) < EDGE_EPS


def widen_glyph(text, scale, delta):
    allx = [float(x) for x, y in re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', text)]
    if not allx:
        return text
    anchor = max(allx)

    # Every structural contour (body + internal counters like the sad loop) is
    # scaled; only accent dots (nukat, far above/below) are translated.
    def spread(x):
        return anchor - (anchor - x) * scale

    def proc_body(cbody):
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        P = [(float(x), float(y)) for x, y, e in pts]
        n = len(P)
        sx = [spread(x) for x, y in P]
        sy = [y for x, y in P]
        out = cbody
        for i in range(n):
            x0, y0 = sx[(i - 1) % n], sy[(i - 1) % n]
            x1, y1 = sx[(i + 1) % n], sy[(i + 1) % n]
            tx, ty = x1 - x0, y1 - y0
            L = math.hypot(tx, ty) or 1.0
            # x-inset -> thin fattened vertical stems, but never move a connector
            # point off the cell edge (that is a join and must stay pinned).
            nx = sx[i] if _pinned_to_edge(sx[i]) else sx[i] + delta * (ty / L)
            old = f'<point x="{pts[i][0]}" y="{pts[i][1]}"{pts[i][2]}/>'
            new = f'<point x="{nx:.0f}" y="{pts[i][1]}"{pts[i][2]}/>'
            out = out.replace(old, new, 1)
        return out

    def proc_dot(cbody):
        # Keep the dot's shape; translate it by the same horizontal displacement
        # the teeth got at the dot's center, so it stays over its tooth.
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        xs = [float(x) for x, y, e in pts]
        cx = (min(xs) + max(xs)) / 2
        dx = spread(cx) - cx  # rigid shift, no scaling
        out = cbody
        for x, y, e in pts:
            old = f'<point x="{x}" y="{y}"{e}/>'
            new = f'<point x="{float(x) + dx:.0f}" y="{y}"{e}/>'
            out = out.replace(old, new, 1)
        return out

    def repl(m):
        inner = m.group(0)[len("<contour>"):-len("</contour>")]
        pts = [(float(x), float(y)) for x, y in
               re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', inner)]
        processed = proc_dot(inner) if is_accent_dot(pts) else proc_body(inner)
        return "<contour>" + processed + "</contour>"

    return re.sub(r"<contour>.*?</contour>", repl, text, flags=re.S)


def widen_inbox(text, scale, delta, hold_both):
    """Widen the teeth of a connecting form while keeping the whole glyph inside
    the cell [0,1228]. Only the teeth cluster (the tall uprights) is stretched;
    the baseline connector(s) that reach the cell edge are held and compress to
    make room, so the join strokes stay pinned to the edge. `hold_both` is True
    for medial (both edges are joins) and False for initial (only the left edge
    is a join; the teeth grow toward the right/word-start edge)."""
    CELL = 1228.0
    MARGIN = 28.0
    contours = re.findall(r"<contour>.*?</contour>", text, re.S)
    if not contours:
        return text
    def npts(c):
        return len(re.findall(r"<point ", c))
    body_idx = max(range(len(contours)), key=lambda i: npts(contours[i]))
    bpts = [(float(x), float(y)) for x, y in
            re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', contours[body_idx])]
    teeth = [x for x, y in bpts if y > 500]
    if not teeth:
        return text
    ta, tb = min(teeth), max(teeth)
    new_w = (tb - ta) * scale
    if hold_both:
        center = CELL / 2
        na, nb = center - new_w / 2, center + new_w / 2
    else:  # initial: teeth grow toward the right/word-start edge
        nb = CELL - MARGIN
        na = nb - new_w
    na = max(na, MARGIN)
    nb = min(nb, CELL - MARGIN)
    knots = sorted({0.0: 0.0, ta: na, tb: nb, CELL: CELL}.items())

    def M(x):
        if x <= knots[0][0]:
            return x
        for i in range(len(knots) - 1):
            x0, y0 = knots[i]
            x1, y1 = knots[i + 1]
            if x <= x1:
                if x1 == x0:
                    return y0
                return y0 + (x - x0) / (x1 - x0) * (y1 - y0)
        return x

    def proc_body(cbody):
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        sx = [M(float(x)) for x, y, e in pts]
        sy = [float(y) for x, y, e in pts]
        n = len(pts)
        out = cbody
        for i in range(n):
            x0, y0 = sx[(i - 1) % n], sy[(i - 1) % n]
            x1, y1 = sx[(i + 1) % n], sy[(i + 1) % n]
            tx, ty = x1 - x0, y1 - y0
            L = math.hypot(tx, ty) or 1.0
            # inset -> restore monolinear stroke, but keep join connectors pinned
            # to the cell edge so adjacent letters stay flush (no gap at the join).
            nx = sx[i] if _pinned_to_edge(sx[i]) else sx[i] + delta * (ty / L)
            out = out.replace(f'<point x="{pts[i][0]}" y="{pts[i][1]}"{pts[i][2]}/>',
                              f'<point x="{nx:.0f}" y="{pts[i][1]}"{pts[i][2]}/>', 1)
        return out

    def proc_dot(cbody):
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        xs = [float(x) for x, y, e in pts]
        cx = (min(xs) + max(xs)) / 2
        dx = M(cx) - cx
        out = cbody
        for x, y, e in pts:
            out = out.replace(f'<point x="{x}" y="{y}"{e}/>',
                              f'<point x="{float(x) + dx:.0f}" y="{y}"{e}/>', 1)
        return out

    def repl(m):
        inner = m.group(0)[len("<contour>"):-len("</contour>")]
        pts = [(float(x), float(y)) for x, y in
               re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', inner)]
        return "<contour>" + (proc_dot(inner) if is_accent_dot(pts) else proc_body(inner)) + "</contour>"

    return re.sub(r"<contour>.*?</contour>", repl, text, flags=re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--scale", type=float, default=1.5)
    ap.add_argument("--delta", type=float, default=29.0)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    gdir, contents, cp2name = load(args.ufo)
    items = plan(contents, cp2name)
    for name, op in items:
        if args.apply:
            p = os.path.join(gdir, contents[name])
            src = open(p).read()
            if op == "widen":
                out = widen_glyph(src, args.scale, args.delta)
            elif op == "init":
                out = widen_inbox(src, args.scale, args.delta, hold_both=False)
            else:  # medi
                out = widen_inbox(src, args.scale, args.delta, hold_both=True)
            with open(p, "w") as fh:
                fh.write(out)
        print(f"  {op:5} {name}")
    print(f"{'Applied' if args.apply else 'Planned'}: {len(items)} glyphs "
          f"(teeth widened consistently across all forms, kept in-box)")


if __name__ == "__main__":
    main()
