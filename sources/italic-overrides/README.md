# Italic overrides

Glyphs here replace the sheared-roman version when `scripts/make-italic.py`
generates the Italic. Use them for genuine cursive italic forms that differ
from a plain slant of the roman.

Currently:
- `f.glif` — the descending italic `f` (from the original Courier Prime italic).

Candidates for future hand-drawn additions: a single-story italic `a`, a
single-story `g`, etc. Drop a `.glif` here (named after the glyph) and it will
be grafted in on the next `make arabic-features && make-italic` / build.
