#!/usr/bin/env python3
"""Import Devanagari from the donor (Noto Sans Devanagari) into the Regular UFO.

This is the *raw* import, as import-hebrew.py is for Hebrew: outlines in the
donor's coordinates (components decomposed, canonical PostScript winding via
skia-pathops), the donor's anchors and glyph categories, and the donor's
OpenType substitution code. Fitting to Courier Badi's cells, line and stroke
is a separate step (scripts/fit-devanagari.py).

Donor: Noto Sans Devanagari (SIL OFL 1.1; Copyright 2022 The Noto Project
Authors, https://github.com/notofonts/devanagari). Its source, not its binary,
is the donor, because the source carries the feature code in readable form
(classes, named lookups) and the anchors from which ufo2ft builds the mark
positioning; the binary has ~300 compiled contextual lookups. Take the source
at a pinned commit:
  git clone https://github.com/notofonts/devanagari
  git -C devanagari checkout 7810f785f3e530048852cd14c226e8b3d3b4654f
and pass sources/NotoSansDevanagari.glyphspackage. The donor is a variable
design (wght 100-900, wdth 62.5-100); glyphsLib + fontmake's instantiator make
one instance at --wght (default 475: its stem, scaled to Courier Badi's line,
is the Latin's 150; see fit-devanagari.py), full width.

What is imported:
  - every donor glyph the Devanagari needs: the Devanagari and Vedic letters,
    signs, digits and all their unencoded forms (half forms, conjuncts, matra
    variants, reph and rakar forms), the few other glyphs the donor's feature
    code names that Courier Badi lacks (U+200B, NullMark, the Common Indic
    Number Forms U+A830-A839, U+20F0) and the rupee sign U+20B9 (an Indic
    font must have it). The donor's names (ka-deva) are no valid production
    names: they become kaDeva, anudattaVedic, quarterMarkCinf, with a few
    long words shortened (candraBindu cBindu, anusvara anusv; ABBREV), so a
    name stays within 31 characters. A donor glyph whose codepoint
    Courier Badi already has (space, digits, U+25CC, the joiners, ...) is not
    imported: the feature code is pointed at Courier Badi's glyph instead.
  - anchors, renamed with "Deva" (top -> topDeva, _bottom -> _bottomDeva,
    nukta.sat -> nuktaDeva.sat), so they never pair with the Hebrew "top" or
    the fallback anchors of the other scripts. The prefix (top, bottom, nukta)
    is kept: ufo2ft sorts a mark into abvm or blwm by it.
  - the donor's glyph categories (base, mark, ligature) into the font lib's
    public.openTypeCategories; scripts/arabic-features puts the unencoded
    marks among them into the GDEF mark class.
  - the donor's feature code, between markers after the generated Arabic
    block: glyph names mapped to Courier Badi's, the languagesystem
    statements left out (scripts/arabic-features declares deva/dev2 and the
    languages), the donor's ss01 (Nepali nine) renamed ss02, since ss01 is
    the dotless kaf.

Every imported glyph is tagged in its lib with DEVA_KEY = "imported";
fit-devanagari.py fits only glyphs in that state and retags them "fitted", so
the pair is idempotent: re-running the import resets the Devanagari.

Usage:
  python3 scripts/import-devanagari.py --source .../NotoSansDevanagari.glyphspackage \
      [--wght 475] [--ufo sources/CourierBadi-Regular.ufo]
"""
import argparse
import os
import re
import tempfile

import pathops
import ufoLib2
from fontTools.pens.qu2cuPen import Qu2CuPen
from fontTools.pens.recordingPen import DecomposingRecordingPen

DEVA_KEY = "org.courierbadi.devanagari"
BEGIN = "# >>> BEGIN DEVANAGARI FEATURES (scripts/import-devanagari.py, fit-devanagari.py) >>>"
END = "# <<< END DEVANAGARI FEATURES <<<"
ARABIC_END = "# <<< END GENERATED ARABIC FEATURES <<<"
SKIP = {".notdef", "NULL", "CR"}
NAME_RE = re.compile(r"(?<![@\w.\-])([A-Za-z_.][A-Za-z0-9_.\-]*)")


def build_donor(source, wght):
    import glyphsLib
    from fontTools.designspaceLib import DesignSpaceDocument, InstanceDescriptor
    from fontmake.instantiator import Instantiator
    tmp = tempfile.mkdtemp(prefix="deva-donor-")
    res = glyphsLib.build_masters(source, os.path.join(tmp, "masters"),
                                  designspace_instance_dir=tmp, minimal=False)
    ds = DesignSpaceDocument.fromfile(res.designspace_path)
    ds.loadSourceFonts(ufoLib2.Font.open)
    desc = InstanceDescriptor()
    desc.familyName, desc.styleName = "Noto Sans Devanagari", f"W{wght:g}"
    desc.designLocation = {a.name: a.map_forward(wght if a.tag == "wght" else a.default)
                           for a in ds.axes}
    inst = Instantiator.from_designspace(ds).generate_instance(desc)
    # glyphs the source does not export (components of others) stay out
    inst.lib["public.skipExportGlyphs"] = ds.sources[0].font.lib.get("public.skipExportGlyphs", [])
    return inst


# shorter words, so every name (with fit-devanagari.py's .q12 / .init / .fina)
# keeps within the 31 characters of legacy systems
ABBREV = [("candraBindu", "cBindu"), ("anusvara", "anusv"), ("VocalicMatra", "VocMatra"),
          ("eCandra", "eCand"), ("eShort", "eSh"), ("yajurvedic", "yv"), ("atharvavedic", "av"),
          ("rigvedic", "rv"), ("Independent", "Ind"), ("Svarita", "Svar"),
          ("Aggravated", "Aggr"), ("Kashmiri", "Kash"), ("Schroeder", "Schr"), ("Kathaka", "Kath")]


def new_name(n):
    for a, b in ABBREV:
        n = n.replace(a, b)
    return n.replace("-deva", "Deva").replace("-vedic", "Vedic").replace("-cinf", "Cinf")


def anchor_name(n):
    under = n.startswith("_")
    core = n[1:] if under else n
    head, dot, tail = core.partition(".")
    return ("_" if under else "") + head + "Deva" + dot + tail


def outline(donor, g):
    rp = DecomposingRecordingPen(donor)
    g.draw(rp)
    path = pathops.Path()
    rp.replay(path.getPen())
    path.simplify()
    return path


def referenced_names(fea):
    return set(NAME_RE.findall(fea))


def transform_fea(fea, rename):
    out = []
    for line in fea.splitlines():
        if line.strip().startswith("languagesystem"):
            continue
        code, hash_, comment = line.partition("#")
        code = NAME_RE.sub(lambda m: rename.get(m.group(1), m.group(1)), code)
        out.append(code + hash_ + comment)
    text = "\n".join(out)
    text = re.sub(r"\bfeature ss01\b", "feature ss02", text)
    text = re.sub(r"\}\s*ss01\s*;", "} ss02;", text)
    return text


def splice(existing, block):
    if BEGIN in existing:
        a = existing.index(BEGIN)
        b = existing.index(END) + len(END)
        return existing[:a] + block + existing[b:]
    i = existing.index(ARABIC_END) + len(ARABIC_END)
    return existing[:i] + "\n\n" + block + existing[i:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--wght", type=float, default=475)
    ap.add_argument("--ufo", default="sources/CourierBadi-Regular.ufo")
    args = ap.parse_args()

    donor = build_donor(args.source, args.wght)
    font = ufoLib2.Font.open(args.ufo)
    for g in list(font):
        if g.lib.get(DEVA_KEY) in ("imported", "fitted"):
            del font[g.name]
        elif g.lib.get(DEVA_KEY):           # a glyph that only has Devanagari anchors
            for a in [a for a in g.anchors if "Deva" in a.name]:
                g.anchors.remove(a)
            del g.lib[DEVA_KEY]
            g.lib.pop(DEVA_KEY + ".donorbox", None)
    cats = dict(font.lib.get("public.openTypeCategories", {}))
    for n in list(cats):
        if n not in font:
            del cats[n]

    cmap = {}
    for g in font:
        for u in g.unicodes:
            cmap.setdefault(u, g.name)
    fea = donor.features.text
    used = referenced_names(fea)
    rename, take = {}, []
    skip = SKIP | set(donor.lib.get("public.skipExportGlyphs", []))
    for g in donor:
        if g.name in skip or g.name.startswith("_"):  # Glyphs: "_" = not exported
            continue
        mapped = next((cmap[u] for u in g.unicodes if u in cmap), None)
        if mapped:
            rename[g.name] = mapped
            continue
        deva = "-deva" in g.name or "-vedic" in g.name
        if not deva and g.name not in used and 0x20B9 not in g.unicodes:
            continue
        assert g.name not in font, g.name
        take.append(g)

    # glyph names: the donor's "ka-deva" is no valid production name
    for dg in take:
        n = new_name(dg.name)
        assert re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]{0,62}", n) and n not in font, n
        rename[dg.name] = n
    dcats = donor.lib.get("public.openTypeCategories", {})
    for dg in take:
        g = font.newGlyph(rename[dg.name])
        g.unicodes = list(dg.unicodes)
        g.width = dg.width
        outline(donor, dg).draw(Qu2CuPen(g.getPen(), max_err=0.5, all_cubic=True))
        for a in dg.anchors:
            g.appendAnchor({"name": anchor_name(a.name), "x": a.x, "y": a.y})
        g.lib[DEVA_KEY] = "imported"
        if dg.name in dcats:
            cats[g.name] = dcats[dg.name]
    font.lib["public.openTypeCategories"] = cats

    # Courier Badi's own dotted circle takes the donor circle's anchors, so a
    # Devanagari sign shown on U+25CC sits on it (fit-devanagari.py maps them
    # from the donor's circle onto this one)
    dc = next((g for g in donor if 0x25CC in g.unicodes), None)
    if dc is not None and "uni25CC" in font:
        from fontTools.pens.boundsPen import BoundsPen
        bp = BoundsPen(donor)
        dc.draw(bp)
        g = font["uni25CC"]
        for a in dc.anchors:
            g.appendAnchor({"name": anchor_name(a.name), "x": a.x, "y": a.y})
        g.lib[DEVA_KEY] = "anchors"
        g.lib[DEVA_KEY + ".donorbox"] = list(bp.bounds)

    block = (BEGIN + "\n# Adapted from Noto Sans Devanagari's feature code (OFL; see\n"
             "# scripts/import-devanagari.py). Regenerate; do not edit by hand.\n"
             "# state: raw\n\n" + transform_fea(fea, rename) + "\n" + END)
    font.features.text = splice(font.features.text, block)
    font.save()
    print(f"{args.ufo}: imported {len(take)} Devanagari glyphs; "
          f"{len(rename)} donor names mapped to Courier Badi's")


if __name__ == "__main__":
    main()
