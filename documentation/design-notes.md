# Courier Badi — design & engineering notes

This document records a few non-obvious design decisions, mainly so reviewers
(including Google Fonts onboarding) don't have to reverse-engineer them.

## Monospace model

Every glyph advances **1228 units** (UPM 2048). The font is strictly
monospaced: `post.isFixedPitch` is set, the PANOSE proportion byte is 9
(monospaced), and `hhea.numberOfHMetrics` is 1 (all glyphs share one width — a
valid and compact choice for a monospaced font; see
fonttools/fonttools#3014).

### Combining marks are zero-width overlays

Spacing/base glyphs advance 1228; **combining marks (Unicode categories Mn/Me)
advance 0**. They are drawn as overlays positioned to sit over the *preceding*
base cell, which is the standard model for combining marks and lets sequences
like `i` + U+0301 stack correctly instead of consuming a second cell.

The common accented letters used for Bahá'í and European orthographies
(á í ú ñ …) are **precomposed** single glyphs at the normal 1228 width, so the
zero-width marks matter only for arbitrary base+mark combinations.

The Arabic tashkil **isolated presentation forms** in U+FE70–U+FE7F are *not*
combining marks — they are standalone spacing forms and keep the 1228 width and
are excluded from the GDEF mark class.

> Note: this zero-width model was introduced deliberately. If a fontbakery run
> or a reviewer flags mark widths, this is the intended design, not an artifact.

## Arabic shaping

Arabic OpenType features are **generated**, not hand-written, by
`scripts/arabic-features` (Go). See its package doc for details. In short:

- `init` / `medi` / `fina` single substitutions are emitted for every base
  letter whose positional-form glyph exists in the UFO — either the Unicode
  presentation form (from the Unicode Character Database) or the
  `<base>.init/.medi/.fina` naming convention used for extended letters that
  have no Unicode presentation form (e.g. Pashto U+0681, U+0685).
- The mandatory **lam-alef** ligatures are matched against the *positional*
  forms (`lam.init`/`lam.medi` + `alef.fina`), because HarfBuzz applies
  init/medi/fina **before** `rlig`; rules written against the base letters
  never match and the ligature silently fails to form.
- The `GDEF` mark class is built from Unicode categories (Mn/Me), excluding the
  U+FE70–FE7F isolated forms noted above.

Regenerate after adding/removing Arabic glyphs:

```
make arabic-features         # rewrite the managed block in features.fea
make arabic-features-check   # verify it is up to date (CI-friendly)
```

The generated block lives between markers in
`sources/CourierBadi-Regular.ufo/features.fea`; hand-written features outside
the markers (see below) are preserved.

## Stylistic sets

- **ss01 — Dotless kaf.** Isolated and final kaf carry a small internal stroke;
  the initial/medial forms are already strokeless. ss01 swaps only the isolated
  (`uni0643` → `kafDotless_ar`) and final (`uniFEDA` → `kafDotless_ar.fina`)
  forms to their dotless variants.
- **zero — Slashed zero.**

## seen/sheen/sad teeth widening

`scripts/widen-seen-family.py` spreads the scrunched teeth of the seen/sheen/sad
family so they fill the cell. It only touches the **isolated and final** forms —
those have the free terminal tail, so the teeth can spread while the tail
smuggles out of the box on the left; the tooth-cluster itself stays inside the
cell. Initial/medial forms are pinned between joins and left unchanged (widening
them would overhang into the neighbouring letter). A horizontal scale spreads
the teeth, then an x-direction inset thins the (now fattened) vertical stems
back to a constant, monolinear stroke width. Run once from pristine glyphs.

## Cyrillic diacritic centering

The Cyrillic merged from Novikov's fork stored accented letters as standalone
outlines, several with the top mark shifted off-center. `scripts/
center-cyrillic-marks.py` recenters the safe cases (symmetric marks —
breve/dieresis/macron/double-acute — over non-dotted bases). It is idempotent
and can be re-run if Cyrillic is re-imported.
