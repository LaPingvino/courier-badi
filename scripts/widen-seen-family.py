#!/usr/bin/env python3
"""Widen the cramped teeth of the seen/sheen (and sad/dad) family in the UFO.

The seen/sheen/sad letters merged from No Name Fixed have their tooth/loop
cluster scrunched into a narrow band with a large empty bowl, which reads poorly
(see google/fonts#6491). This spreads the teeth so they fill the cell, WITHOUT
fattening the strokes and WITHOUT letting the tooth-cluster leave the box.

Only the ISOLATED and FINAL forms are touched: those have the free terminal
tail, so the teeth can spread into the freed space and the tail smuggles out of
the box on the left (word-end / margin). Initial and medial forms are left
alone -- their teeth are pinned between joins with no room to grow inside the
box, and widening them would overhang into the previous letter.

Two steps per glyph:
  1. Horizontal scale by `scale`, anchored at the rightmost point so the right
     side (the join for final forms / the word start) stays put; the teeth
     spread left and the terminal tail extends past the left edge.
  2. An x-direction inset by `delta` that thins the now-fattened vertical stems
     back to their original width, restoring a constant (monolinear) stroke.
     Horizontal strokes (normal.x ~ 0) are untouched, so only the vertical
     stems are corrected.

Run once from pristine glyphs. Usage:
  python3 scripts/widen-seen-family.py [--scale 1.5] [--delta 29] [--apply]
"""
import argparse
import math
import os
import re
import unicodedata as ud

# seen/sheen teeth family + sad/dad loop family (same rough treatment).
FAMILY = [0x0633, 0x0634, 0x069A, 0x069B, 0x069C, 0x06FA, 0x0770, 0x077D, 0x077E,
          0x0635, 0x0636, 0x069D, 0x069E, 0x06FB]
POS_TAGS = {"final": "fina"}  # isolated handled separately; init/medi skipped


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
    for bcp in FAMILY:
        isol = cp2name.get(bcp)
        if isol:
            out.append((isol, "widen"))
        for pos, op in (("fina", "widen"), ("init", "lower"), ("medi", "lower")):
            g = form_glyph(contents, cp2name, fp, isol, bcp, pos)
            if g:
                out.append((g, op))
    return out


def widen_glyph(text, scale, delta):
    allx = [float(x) for x, y in re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', text)]
    if not allx:
        return text
    anchor = max(allx)

    contours = re.findall(r"<contour>.*?</contour>", text, re.S)
    # The main body is the contour with the most points; the rest are dots
    # (nukat) that must keep their shape and only be repositioned.
    def npts(c):
        return len(re.findall(r"<point ", c))
    body_idx = max(range(len(contours)), key=lambda i: npts(contours[i])) if contours else -1

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
            nx = sx[i] + delta * (ty / L)  # x-inset -> thin fattened vertical stems
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

    idx = -1

    def repl(m):
        nonlocal idx
        idx += 1
        inner = m.group(0)[len("<contour>"):-len("</contour>")]
        processed = proc_body(inner) if idx == body_idx else proc_dot(inner)
        return "<contour>" + processed + "</contour>"

    return re.sub(r"<contour>.*?</contour>", repl, text, flags=re.S)


def lower_glyph(text, k):
    """Lower the teeth of initial/medial forms (scale y above the baseline by k,
    keeping the join baseline fixed) so their proportions match the widened
    isolated/final teeth. Dots are shifted down to stay above the lower teeth."""
    contours = re.findall(r"<contour>.*?</contour>", text, re.S)
    if not contours:
        return text
    def npts(c):
        return len(re.findall(r"<point ", c))
    body_idx = max(range(len(contours)), key=lambda i: npts(contours[i]))
    body_ys = [float(y) for x, y in
               re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', contours[body_idx])]
    ybase = min(body_ys)
    ytop = max(body_ys)
    ddy = -(1 - k) * (ytop - ybase)  # how far the tops drop; dots follow

    def proc_body(cbody):
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        out = cbody
        for x, y, e in pts:
            yv = float(y)
            ny = ybase + (yv - ybase) * k if yv > ybase else yv
            out = out.replace(f'<point x="{x}" y="{y}"{e}/>',
                              f'<point x="{x}" y="{ny:.0f}"{e}/>', 1)
        return out

    def proc_dot(cbody):
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        out = cbody
        for x, y, e in pts:
            out = out.replace(f'<point x="{x}" y="{y}"{e}/>',
                              f'<point x="{x}" y="{float(y) + ddy:.0f}"{e}/>', 1)
        return out

    idx = -1

    def repl(m):
        nonlocal idx
        idx += 1
        inner = m.group(0)[len("<contour>"):-len("</contour>")]
        return "<contour>" + (proc_body(inner) if idx == body_idx else proc_dot(inner)) + "</contour>"

    return re.sub(r"<contour>.*?</contour>", repl, text, flags=re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--scale", type=float, default=1.5)
    ap.add_argument("--delta", type=float, default=29.0)
    ap.add_argument("--lower", type=float, default=0.85, help="y-scale for init/medial teeth")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    gdir, contents, cp2name = load(args.ufo)
    items = plan(contents, cp2name)
    for name, op in items:
        if args.apply:
            p = os.path.join(gdir, contents[name])
            src = open(p).read()
            out = widen_glyph(src, args.scale, args.delta) if op == "widen" \
                else lower_glyph(src, args.lower)
            with open(p, "w") as fh:
                fh.write(out)
        print(f"  {op:5} {name}")
    print(f"{'Applied' if args.apply else 'Planned'}: {len(items)} glyphs "
          f"(widen isolated/final, lower initial/medial)")


if __name__ == "__main__":
    main()
