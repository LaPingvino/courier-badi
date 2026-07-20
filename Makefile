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

build.stamp: venv sources/config.yaml $(SOURCES)
	rm -rf fonts
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)
	# Post-build: add a 'meta' table (dlng/slng ScriptLangTags) and a STAT table
	# (italic axis for the Regular+Italic family), then refresh the webfonts.
	. venv/bin/activate; python3 scripts/add-meta-table.py $$(find fonts -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	. venv/bin/activate; python3 scripts/add-stat.py $$(find fonts -name '*.ttf' -o -name '*.otf' 2>/dev/null)
	. venv/bin/activate; for ttf in fonts/ttf/*.ttf; do [ -f "$$ttf" ] && rm -f fonts/webfonts/$$(basename $${ttf%.ttf}).woff2 && fonttools ttLib.woff2 compress -o fonts/webfonts/$$(basename $${ttf%.ttf}).woff2 $$ttf; done
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
	# CNTR=100 masters: contrasted bold (thick verticals, thin horizontals)
	. venv/bin/activate; python3 scripts/make-bold.py --src sources/CourierBadi-Regular.ufo --out sources/CourierBadi-BoldContrast.ufo --weight 48 --contrast 2.4
	. venv/bin/activate; python3 scripts/make-bold.py --src sources/CourierBadi-Italic.ufo --out sources/CourierBadi-BoldItalicContrast.ufo --weight 48 --contrast 2.4

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
