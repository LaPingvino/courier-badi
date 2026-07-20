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


def final_forms():
    out = {}
    for cp in list(range(0xFB50, 0xFE00)) + list(range(0xFE70, 0xFF00)):
        d = ud.decomposition(chr(cp))
        if d.startswith("<"):
            tag = d[1:d.index(">")]
            if tag == "final":
                comps = d[d.index(">") + 1:].split()
                if len(comps) == 1:
                    out.setdefault(int(comps[0], 16), cp)
    return out


def plan(contents, cp2name):
    ff = final_forms()
    glyphs = []
    for bcp in FAMILY:
        isol = cp2name.get(bcp)
        if isol:
            glyphs.append(isol)
        fcp = ff.get(bcp)
        g = None
        if fcp and cp2name.get(fcp):
            g = cp2name[fcp]
        elif fcp and ("uni%04X" % fcp) in contents:
            g = "uni%04X" % fcp
        elif isol and f"{isol}.fina" in contents:
            g = f"{isol}.fina"
        if g:
            glyphs.append(g)
    return glyphs


def widen_glyph(text, scale, delta):
    allx = [float(x) for x, y in re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"', text)]
    if not allx:
        return text
    anchor = max(allx)

    def proc(cbody):
        pts = re.findall(r'<point x="(-?[0-9.]+)" y="(-?[0-9.]+)"([^/]*)/>', cbody)
        P = [(float(x), float(y)) for x, y, e in pts]
        n = len(P)
        sx = [anchor - (anchor - x) * scale for x, y in P]  # step 1: spread
        sy = [y for x, y in P]
        body = cbody
        for i in range(n):
            x0, y0 = sx[(i - 1) % n], sy[(i - 1) % n]
            x1, y1 = sx[(i + 1) % n], sy[(i + 1) % n]
            tx, ty = x1 - x0, y1 - y0
            L = math.hypot(tx, ty) or 1.0
            nx = sx[i] + delta * (ty / L)  # step 2: x-inset -> thin vertical stems
            old = f'<point x="{pts[i][0]}" y="{pts[i][1]}"{pts[i][2]}/>'
            new = f'<point x="{nx:.0f}" y="{pts[i][1]}"{pts[i][2]}/>'
            body = body.replace(old, new, 1)
        return body

    return re.sub(r"<contour>(.*?)</contour>",
                  lambda m: "<contour>" + proc(m.group(1)) + "</contour>", text, flags=re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    ap.add_argument("--scale", type=float, default=1.5)
    ap.add_argument("--delta", type=float, default=29.0)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    gdir, contents, cp2name = load(args.ufo)
    glyphs = plan(contents, cp2name)
    for name in glyphs:
        if args.apply:
            p = os.path.join(gdir, contents[name])
            src = open(p).read()
            out = widen_glyph(src, args.scale, args.delta)
            with open(p, "w") as fh:
                fh.write(out)
        print(f"  {'widen' if args.apply else 'plan':5} {name}")
    print(f"{'Applied' if args.apply else 'Planned'}: {len(glyphs)} glyphs (isolated+final only)")


if __name__ == "__main__":
    main()
