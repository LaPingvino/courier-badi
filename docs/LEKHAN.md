# Lekhan monospace

*How many cells Devanagari takes on a monospace grid.*

Version 1.0, 2026-11-23. The text of this page, the test vectors
([`lekhan-vectors.txt`](lekhan-vectors.txt)) and the reference function
below are dedicated to the public domain (CC0 1.0): use them, copy them,
change them, without asking. The font that follows it, Courier Badi, is
under the SIL Open Font License like the rest of this repository.

## Why

We were building a screenplay editor, Accolade, that already supported
Arabic and Hebrew monospace. Adding Hindi monospace was a logical next step.
Because of the nature of the script, this is not as clear as it is for
other scripts, and the approach of the old typewriters gave us a nice
middle ground: an acceptable font that follows their spirit and is allowed
to look nice.

A screenplay is written on a grid. Its page count stands for screen time
because every character takes the same width, so a script in Hindi needs a
grid too. But Devanagari is not written letter by letter. A syllable is a
cluster: a consonant with its vowel sign (कि, with the sign drawn *before*
the letter), or several consonants melted into one shape (क्ष, स्त्र).
Counting code points gives nonsense (कि would be two cells, its sign on a
cell of its own), and counting grapheme clusters gives everything one cell
(स्क्री squeezed into the width of क).

## The typewriter

Devanagari has been typed on monospace machines before. The Hindi
typewriters that followed the script reforms of the 1950s (the Lucknow
conference of 1953 settled forms a machine could type), the Nagari Lekhan
Yantra among them, gave every key the same step. A conjunct was struck as
pieces, the half form of the first consonant and then the next letter, so
it took more room on the line than a simple letter did. Lekhan monospace
keeps that proportion and lets a cluster look like itself: a simple
syllable takes one cell, a syllable that joins consonants takes two, drawn
as one wide glyph. The rule is named after the machine.

## The rule

Split the text into **extended grapheme clusters** (Unicode Standard Annex
#29) with the **virama rule** of Unicode 15.1 (GB9c): a consonant that
follows a virama (U+094D) which follows a consonant stays in the cluster,
also with a nukta or a zero-width joiner between them. A zero-width
non-joiner after the virama ends the cluster.

Then a Devanagari cluster (one that starts with a Devanagari letter, sign
or digit) takes:

- **1 cell** if it has at most one consonant: a consonant or an independent
  vowel with its vowel signs and marks (क का कि कः कं क़ि आ ॐ), a consonant
  with a final virama (the न् of श्रीमान्), a digit, a danda, the avagraha;
- **2 cells** if it has two or more consonants (Indic_Conjunct_Break =
  Consonant: U+0915–0939, U+0958–095F, U+0978–097F): every conjunct,
  however it is drawn: a ligature (क्ष ज्ञ त्र), a half form and a full one
  (त्न स्क), a stack or a visible virama (ट्ट ड्ड), reph and rakar (र्य प्र),
  with three or four consonants (स्त्र न्त्र्य स्क्री) still 2.

A Devanagari vowel sign or mark with no letter before it in its cluster
(at the start of a line, after a space) is drawn on a dotted circle and
takes 1 cell. Every other character keeps its terminal width: 1, 2 for East
Asian wide and fullwidth characters and emoji, 0 for combining marks,
joiners and direction controls.

Where an implementation stores widths per character (a terminal's cell
array, an editor grid), a cluster's cells go on its first character and,
for a conjunct, the second on its second consonant; all others take 0. So
typing क्ष grows the cluster from one cell to two as the ष is typed.

## For a font

A font follows Lekhan monospace when it draws every cluster exactly as wide
as its cells: shaped (HarfBuzz and the like apply the Indic features one
syllable at a time), a simple cluster advances one cell, a conjunct two. A
conjunct is **one double-width glyph**, its parts condensed or widened
together to fill its two cells, never a narrow glyph with a stretched
headline between its parts. A simple cluster is condensed into its cell
when it is wider than one (का, कौ, औ).

Courier Badi (from 1.105) does this with its own glyphs: the donor's
(Noto Sans Devanagari) proportional cluster, scaled across to the nearest
of a few widths that fits, the stems kept, the remainder shared out as
headline before and after it. The counting is done in the font's features
(`scripts/fit-devanagari.py` explains how); `scripts/check-devanagari.py`
shapes every vector, 6000 other clusters and a Hindi text and checks their
widths, and `documentation/lekhan-specimen.py` draws them on the grid.

## For a terminal or an editor

Count cells by the rule (the reference function below, or a port), wrap
lines and place the cursor by clusters, and draw each cluster from its
first cell, shaped, with a font that follows the rule. Accolade (its
editor grid and cursor) and Lexington (its PDF line wrap) use the same
function, Lexington's package `lekhan`.

## Test vectors

[`lekhan-vectors.txt`](lekhan-vectors.txt): one text per line, its clusters
split by `|`, a tab, each cluster's cells, a tab, a note. A conforming
width function finds those clusters and those cells; a conforming font
shapes each text exactly that many cells wide. Some of them:

| text | clusters | cells |
|---|---|---|
| का | का | 1 |
| कि | कि | 1 |
| कः | कः | 1 |
| आ | आ | 1 |
| क् | क् | 1 |
| क्ष | क्ष | 2 |
| त्न | त्न | 2 |
| र्य | र्य | 2 |
| स्क्री | स्क्री | 2 |
| न्त्र्य | न्त्र्य | 2 |
| क्‌ष (with ZWNJ) | क्‌ · ष | 1 1 |
| श्रीमान् | श्री · मा · न् | 2 1 1 |
| हिन्दी | हि · न्दी | 1 2 |

## Reference function (Go)

The reference is Lexington's package
[`lekhan`](https://github.com/LaPingvino/lexington/tree/master/lekhan)
(`Width`, `Cells`, `ClusterEnd`, `ClusterCells`), tested against the
vectors. Its core, for a single cluster:

```go
// Consonant: Indic_Conjunct_Break = Consonant (Devanagari).
func Consonant(r rune) bool {
	return r >= 0x0915 && r <= 0x0939 || r >= 0x0958 && r <= 0x095F || r >= 0x0978 && r <= 0x097F
}

// ClusterCells is how many cells an extended grapheme cluster (with
// GB9c) takes: a Devanagari one 2 with two or more consonants, else 1;
// another the sum of its characters' terminal widths.
func ClusterCells(c []rune) int {
	if len(c) == 0 {
		return 0
	}
	if !Devanagari(c[0]) {
		n := 0
		for _, r := range c {
			n += RuneWidth(r) // wcwidth-like: 0, 1 or 2
		}
		return n
	}
	consonants := 0
	for _, r := range c {
		if Consonant(r) {
			consonants++
		}
	}
	if consonants >= 2 {
		return 2
	}
	return 1
}
```

The cluster boundary (GB9c): a cluster continues before a combining mark,
a joiner or a character after a zero-width joiner, and before a consonant
after a virama when, looking back over viramas, nukta, joiners and other
nonspacing marks, a consonant comes before that virama.

## Other scripts

The rule is written for Devanagari. The other Brahmic scripts that GB9c
covers (Bengali, Gujarati, Oriya, Telugu, Malayalam) have the same shape of
problem and could take the same rule; that is left for whoever sets them.
