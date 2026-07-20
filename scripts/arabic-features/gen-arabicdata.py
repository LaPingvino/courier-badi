#!/usr/bin/env python3
"""Regenerate arabicdata.go from the Unicode Character Database.

The mapping from an Arabic base codepoint to its isolated/initial/medial/final
presentation forms is derived directly from the canonical decomposition data
that ships with Python's unicodedata module, so it always matches the Unicode
version Python was built against. Run:

    python3 gen-arabicdata.py > arabicdata.go
"""
import unicodedata as ud

POS = {"isolated": "Isol", "initial": "Init", "medial": "Medi", "final": "Fina"}


def build():
    posmap = {}   # base -> {pos: form}
    ligmap = {}   # (a, b) -> {pos: form}
    for cp in list(range(0xFB50, 0xFE00)) + list(range(0xFE70, 0xFF00)):
        d = ud.decomposition(chr(cp))
        if not d.startswith("<"):
            continue
        tag = d[1:d.index(">")]
        if tag not in POS:
            continue
        comps = [int(x, 16) for x in d[d.index(">") + 1:].split()]
        if len(comps) == 1:
            posmap.setdefault(comps[0], {})[POS[tag]] = cp
        elif len(comps) == 2:
            ligmap.setdefault(tuple(comps), {})[POS[tag]] = cp
    return posmap, ligmap


def main():
    posmap, ligmap = build()
    out = []
    out.append("// Code generated from Unicode Character Database (Python unicodedata). DO NOT EDIT.")
    out.append("// Regenerate with: python3 gen-arabicdata.py > arabicdata.go")
    out.append("package main")
    out.append("")
    out.append("// arabicForms maps an Arabic base codepoint to its Unicode presentation-form")
    out.append("// codepoints per joining position (isolated/initial/medial/final).")
    out.append("type formSet struct{ Isol, Init, Medi, Fina rune }")
    out.append("")
    out.append("var arabicForms = map[rune]formSet{")
    for base in sorted(posmap):
        m = posmap[base]
        fields = ", ".join(f"{p}: 0x{m[p]:04X}" for p in ("Isol", "Init", "Medi", "Fina") if p in m)
        out.append(f"\t0x{base:04X}: {{{fields}}},")
    out.append("}")
    out.append("")
    out.append("// lamAlefLig lists the mandatory lam-alef ligatures: lam(0644)+alef variant.")
    out.append("type lamAlef struct{ Alef, LigIsol, LigFina rune }")
    out.append("")
    out.append("var lamAlefLigs = []lamAlef{")
    for (a, b), m in sorted(ligmap.items()):
        if a != 0x0644:
            continue
        if "Isol" in m and "Fina" in m and b in (0x0627, 0x0623, 0x0625, 0x0622):
            out.append(f"\t{{Alef: 0x{b:04X}, LigIsol: 0x{m['Isol']:04X}, LigFina: 0x{m['Fina']:04X}}},")
    out.append("}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
