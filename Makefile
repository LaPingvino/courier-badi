SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(shell ls documentation/*.py)
DRAWBOT_OUTPUT=$(shell ls documentation/*.py | sed 's/\.py/.png/g')

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

venv-test: venv-test/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

# Regenerate the managed Arabic OpenType features (init/medi/fina, lam-alef
# ligatures, GDEF marks) directly from the UFO glyph set. Requires Go. The
# generated block is written between markers in features.fea; hand-written
# features outside the markers are preserved. Run this after adding or removing
# Arabic glyphs. Use `arabic-features-check` in CI to verify it is up to date.
arabic-features:
	cd scripts/arabic-features && go run . --ufo ../../sources/CourierBadi-Regular.ufo

arabic-features-check:
	cd scripts/arabic-features && go run . --ufo ../../sources/CourierBadi-Regular.ufo --check

# Shape the built fonts' Devanagari: every text as wide as its Lekhan width
# (docs/LEKHAN.md), no dotted circles, no stretched headline, the ink against the 12 pt line, the headline (documentation/
# design-notes.md, "Devanagari"). The Devanagari itself is made by
# scripts/import-devanagari.py and scripts/fit-devanagari.py (see there).
check-devanagari: venv build.stamp
	. venv/bin/activate; python3 scripts/check-devanagari.py --sample documentation/sample.hi-Deva.fountain fonts/ttf/*.ttf

# Lekhan monospace specimen (docs/LEKHAN.md): every cluster type on the
# cell grid, the four styles, a Hindi screenplay; PDF and 600 dpi pages.
lekhan-specimen: venv build.stamp
	mkdir -p out
	. venv/bin/activate; python3 documentation/lekhan-specimen.py --sample documentation/sample.hi-Deva.fountain --out out/lekhan-specimen.pdf
	pdftoppm -r 600 -png out/lekhan-specimen.pdf out/lekhan-specimen

build.stamp: venv sources/config.yaml $(SOURCES)
	rm -rf fonts
	# gftools only rebuilds the static instances when the designspace changes,
	# not when a master's glyphs do; drop them so every build is current.
	rm -f sources/instance_ufos/*.json
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)
	# Post-build: add a 'meta' table (dlng/slng ScriptLangTags) and a STAT table
	# (italic axis for the Regular+Italic family), then refresh the webfonts.
	. venv/bin/activate; python3 scripts/add-meta-table.py $$(find fonts -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	. venv/bin/activate; python3 scripts/add-stat.py $$(find fonts -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	# Contextual lookups as one format-2 subtable instead of a format-3 one
	# per rule (the Lekhan counters: 1453): the same, shaped several times
	# faster (see the script).
	. venv/bin/activate; python3 scripts/context-format2.py $$(find fonts -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	# Coverage tables as glyph lists: go-text (Lexington, Accolade) skips
	# glyphs of large range coverages (see the script).
	. venv/bin/activate; python3 scripts/coverage-format1.py $$(find fonts -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	. venv/bin/activate; for ttf in fonts/ttf/*.ttf; do [ -f "$$ttf" ] && rm -f fonts/webfonts/$$(basename $${ttf%.ttf}).woff2 && fonttools ttLib.woff2 compress -o fonts/webfonts/$$(basename $${ttf%.ttf}).woff2 $$ttf; done
	# The static TTFs without hinting, for programs that embed the font
	# (Lexington, Accolade): their rasterizers do not hint.
	. venv/bin/activate; python3 scripts/unhinted.py fonts/unhinted/ttf fonts/ttf/*.ttf
	touch build.stamp

# Regenerate the Italic UFO as a sheared oblique of the Regular, with the
# cursive overrides from sources/italic-overrides grafted on. Run after changing
# the Regular so the Italic inherits all corrections.
italic:
	. venv/bin/activate; python3 scripts/make-italic.py

# Regenerate all derived masters (Italic, Bold, Bold Italic) from the Regular.
# The Bold is an outward outline dilation (emboldening); Bold Italic is the
# emboldened Italic. Run after changing the Regular.
masters:
	. venv/bin/activate; python3 scripts/make-italic.py
	. venv/bin/activate; python3 scripts/make-bold.py --src sources/CourierBadi-Regular.ufo --out sources/CourierBadi-Bold.ufo
	. venv/bin/activate; python3 scripts/make-bold.py --src sources/CourierBadi-Italic.ufo --out sources/CourierBadi-BoldItalic.ufo
	# Contrast siblings for the XOPQ axis: a weight-neutral modulation (thick
	# verticals, thin horizontals) of EACH weight, so XOPQ reads at every weight,
	# not just Bold. Same point structure -> interpolates with its base master.
	. venv/bin/activate; python3 scripts/make-contrast-master.py --src sources/CourierBadi-Regular.ufo    --out sources/CourierBadi-RegularContrast.ufo
	. venv/bin/activate; python3 scripts/make-contrast-master.py --src sources/CourierBadi-Italic.ufo     --out sources/CourierBadi-ItalicContrast.ufo
	. venv/bin/activate; python3 scripts/make-contrast-master.py --src sources/CourierBadi-Bold.ufo       --out sources/CourierBadi-BoldContrast.ufo
	. venv/bin/activate; python3 scripts/make-contrast-master.py --src sources/CourierBadi-BoldItalic.ufo --out sources/CourierBadi-BoldItalicContrast.ufo
	# Hebrew dots drawn where they read without GPOS (shin/sin dot on their
	# arm, holam male beside the vav's head), each
	# master on its own ink. The GPOS places them as before, except the holam
	# male, which moves off the stem with its default.
	. venv/bin/activate; python3 scripts/place-default-marks.py sources/CourierBadi-*.ufo
	# Mark anchors reproducing HarfBuzz's fallback mark positioning (needed
	# since the font has a GPOS; see design-notes), measured on each master's
	# own ink.
	. venv/bin/activate; python3 scripts/make-mark-anchors.py sources/CourierBadi-*.ufo

# Bonus/experimental variable font: the contrast (XOPQ) axis, shipped as a
# release-only extra separate from the GF-clean submission. Outputs to
# fonts-contrast/ so it never mixes with the main fonts/ that CI tests.
contrast-vf: venv masters
	rm -rf fonts-contrast
	. venv/bin/activate; gftools builder sources/contrast.yaml
	. venv/bin/activate; python3 scripts/add-meta-table.py $$(find fonts-contrast -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	. venv/bin/activate; python3 scripts/add-stat.py $$(find fonts-contrast -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	. venv/bin/activate; python3 scripts/coverage-format1.py $$(find fonts-contrast -name '*.ttf' -o -name '*.otf' 2>/dev/null)

# Standalone "Contrast" sample preview (its own family name).
contrast:
	. venv/bin/activate; python3 scripts/make-bold.py --src sources/CourierBadi-Regular.ufo --out /tmp/CourierBadiContrast-Regular.ufo --weight 40 --contrast 4

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv-test/touchfile: requirements-test.txt
	test -d venv-test || python3 -m venv venv-test
	. venv-test/bin/activate; pip install -Ur requirements-test.txt
	touch venv-test/touchfile

test: venv-test build.stamp
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv-test/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --full-lists --succinct --badges out/badges --html out/fontbakery/fontbakery-report.html --ghmarkdown out/fontbakery/fontbakery-report.md $$TOCHECK  || echo '::warning file=sources/config.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv venv-test
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	venv-test/bin/pip install --upgrade pip-tools
	venv-test/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements-test.in
	venv-test/bin/pip-sync requirements-test.txt

	git commit -m "Update requirements" requirements.txt requirements-test.txt
	git push
