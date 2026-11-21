#!/usr/bin/env python3
"""Check that the GPOS mark positioning matches HarfBuzz's fallback.

For each built font, shape every base x mark pair of each script twice with
HarfBuzz: as built (GPOS mark/mkmk), and with the GPOS table removed (so
HarfBuzz uses its fallback mark positioning, which is how Courier Badi's
marks were placed before it had a GPOS; see scripts/make-mark-anchors.py).
Reports, per script, how many pairs differ and by how much, and lists the
worst. Hebrew is not compared (its anchors come from the donor, not from the
fallback).

Pairs: every encoded base of the script x every encoded mark of the script
(Latin/Greek/Cyrillic combining marks are tried on Latin, Greek and Cyrillic
bases), plus two-mark stacks. Arabic bases are shaped in isolated and medial
position (between two behs), so the positional forms are covered.

Usage: python3 scripts/check-mark-parity.py [--tol 20] fonts/ttf/*.ttf
"""
import argparse
import io
import unicodedata as ud

import uharfbuzz as hb
from fontTools.ttLib import TTFont

SCRIPTS = {
    "Latn": [(0x0041, 0x024F), (0x1E00, 0x1EFF)],
    "Grek": [(0x0370, 0x03FF), (0x1F00, 0x1FFF)],
    "Cyrl": [(0x0400, 0x052F)],
    "Arab": [(0x0620, 0x064A), (0x066E, 0x06D3), (0x0750, 0x077F)],
}


def hbfont(data):
    return hb.Font(hb.Face(hb.Blob(data)))


def shape(font, text):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {})
    return [(i.codepoint, p.x_offset, p.y_offset) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]


def is_mark(cp):
    return ud.category(chr(cp)) in ("Mn", "Me")


def positioned(cp):
    # marks HarfBuzz's fallback positions at all (it skips class 0 and overlays)
    return ud.combining(chr(cp)) > 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fonts", nargs="+")
    ap.add_argument("--tol", type=int, default=20)
    ap.add_argument("--show", type=int, default=8)
    args = ap.parse_args()
    ok = True
    for path in args.fonts:
        tt = TTFont(path)
        cmap = tt.getBestCmap()
        with open(path, "rb") as fh:
            built = hbfont(fh.read())
        nogpos = TTFont(path)
        if "GPOS" in nogpos:
            del nogpos["GPOS"]
        bio = io.BytesIO()
        nogpos.save(bio)
        fallback = hbfont(bio.getvalue())

        arab_marks = [c for c in cmap if is_mark(c) and positioned(c)
                      and (0x0610 <= c <= 0x06ED or 0x08D3 <= c <= 0x08FF)]
        other_marks = [c for c in cmap if is_mark(c) and positioned(c)
                       and (0x0300 <= c <= 0x036F or 0x0483 <= c <= 0x0487)]
        print(path)
        for script, ranges in SCRIPTS.items():
            bases = [c for c in cmap if any(a <= c <= b for a, b in ranges)
                     and not is_mark(c) and ud.category(chr(c)).startswith("L")]
            if script == "Arab":
                marks = arab_marks
                texts = []
                for b in bases:
                    for m in marks:
                        texts.append(chr(b) + chr(m))
                        texts.append("ب" + chr(b) + chr(m) + "ب")
                    texts.append(chr(b) + "َّ")  # shadda + fatha stack
            else:
                marks = other_marks
                texts = [chr(b) + chr(m) for b in bases for m in marks]
                texts += [chr(b) + "̂́" for b in bases]       # stack above
                texts += [chr(b) + "̣̱" for b in bases]       # stack below
            diffs = []
            for t in texts:
                a, f = shape(built, t), shape(fallback, t)
                if len(a) != len(f):
                    diffs.append((10 ** 6, t, "different glyph count"))
                    continue
                d = max((abs(x1 - x2) + abs(y1 - y2) for (g1, x1, y1), (g2, x2, y2) in zip(a, f)), default=0)
                if d:
                    diffs.append((d, t, [(x1 - x2, y1 - y2) for (g1, x1, y1), (g2, x2, y2) in zip(a, f) if (x1, y1) != (x2, y2)]))
            big = [d for d in diffs if d[0] > args.tol]
            worst = max((d[0] for d in diffs), default=0)
            ok &= not big
            print(f"  {script}: {len(texts)} sequences, {len(diffs)} differ, "
                  f"{len(big)} by more than {args.tol} units (worst {worst})")
            if big:
                # which marks, and which way: the fallback's clamps show up as
                # a below mark moved up / an above mark not moved down
                by = {}
                for d, t, info in big:
                    ms = [c for c in t if is_mark(ord(c))]
                    k = "+".join("U+%04X" % ord(c) for c in ms)  # stacks show both marks
                    up = isinstance(info, list) and all(dy > 0 for dx, dy in info)
                    n, w, u = by.get(k, (0, 0, 0))
                    by[k] = (n + 1, max(w, d), u + up)
                print("     by mark (pairs, worst, of which GPOS higher):",
                      ", ".join(f"{k} {n}/{w}/{u}" for k, (n, w, u) in
                                sorted(by.items(), key=lambda kv: -kv[1][0])[:12]))
            for d, t, info in sorted(big, reverse=True)[:args.show]:
                print(f"     {d:5d}  {' '.join('U+%04X' % ord(c) for c in t)}  {info}")
    print("PARITY", "OK" if ok else "DIFFERS")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
