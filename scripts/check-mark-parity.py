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

Hebrew instead: --hebrew-against DIR compares each font's HarfBuzz (GPOS)
Hebrew ink positions with the same-named font in DIR (an earlier build):
every letter, the dotted circle and the presentation forms x every point and
cantillation mark, plus dagesh/shin dot/sin dot + vowel stacks (a mark the
GPOS does not place in either build, such as a shin dot on bet, is skipped). A change to
the marks' default outlines (scripts/place-default-marks.py) must leave these
unchanged, except where a position was moved on purpose.

Usage: python3 scripts/check-mark-parity.py [--tol 20] fonts/ttf/*.ttf
       python3 scripts/check-mark-parity.py --hebrew-against OLD/ fonts/ttf/*.ttf
"""
import os
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


def ink(font, text):
    """Absolute ink boxes of a shaped string's glyphs (None for blank ones)."""
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {})
    out, x = [], 0
    for i, p in zip(buf.glyph_infos, buf.glyph_positions):
        e = font.get_glyph_extents(i.codepoint)
        box = (x + p.x_offset + e.x_bearing, p.y_offset + e.y_bearing,
               e.width, e.height) if e and e.width else None
        # a mark the GPOS leaves where it is drawn (a shin dot on bet)
        unplaced = p.x_advance == 0 and not p.x_offset and not p.y_offset
        out.append((box, unplaced))
        x += p.x_advance
    return out


def placed_differently(a, b):
    """Two builds' ink() of one string differ in a glyph either GPOS places."""
    return len(a) != len(b) or any(
        ba != bb and not (ua and ub) for (ba, ua), (bb, ub) in zip(a, b))


def hebrew_against(paths, old_dir, show):
    marks = [chr(c) for c in range(0x0591, 0x05C8) if is_mark(c)]
    bases = [chr(c) for c in range(0x05D0, 0x05EB)] + ["\u25CC"]
    bases += [chr(c) for c in range(0xFB1D, 0xFB50) if c != 0xFB1E]
    texts = [b + m for b in bases for m in marks]
    texts += [chr(b) + m1 + m2 for b in range(0x05D0, 0x05EB)
              for m1 in "\u05BC\u05C1\u05C2" for m2 in "\u05B0\u05B4\u05B7\u05B8"]
    same = True
    for path in paths:
        with open(path, "rb") as fh:
            new = hbfont(fh.read())
        with open(os.path.join(old_dir, os.path.basename(path)), "rb") as fh:
            old = hbfont(fh.read())
        by = {}
        for t in texts:
            if placed_differently(ink(old, t), ink(new, t)):
                k = "+".join("U+%04X" % ord(c) for c in t[1:])
                by.setdefault(k, []).append(t)
        n = sum(len(v) for v in by.values())
        same &= not n
        print(f"{path}: {len(texts)} Hebrew sequences, {n} placed differently")
        for k, ts in sorted(by.items(), key=lambda kv: -len(kv[1]))[:show]:
            bs = " ".join("U+%04X" % ord(t[0]) for t in ts[:6])
            print(f"     {k}: {len(ts)} (on {bs}{' ...' if len(ts) > 6 else ''})")
    print("HEBREW", "SAME" if same else "DIFFERS")
    raise SystemExit(0 if same else 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fonts", nargs="+")
    ap.add_argument("--tol", type=int, default=20)
    ap.add_argument("--show", type=int, default=8)
    ap.add_argument("--hebrew-against", metavar="DIR")
    args = ap.parse_args()
    if args.hebrew_against:
        hebrew_against(args.fonts, args.hebrew_against, args.show)
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
