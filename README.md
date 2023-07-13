# Courier Badi

[![][Fontbakery]](https://LaPingvino.github.io/courier-badi/fontbakery/fontbakery-report.html)
[![][Universal]](https://LaPingvino.github.io/courier-badi/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://LaPingvino.github.io/courier-badi/fontbakery/fontbakery-report.html)
[![][Outline Correctness]](https://LaPingvino.github.io/courier-badi/fontbakery/fontbakery-report.html)
[![][Shaping]](https://LaPingvino.github.io/courier-badi/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FLaPingvino%2Fcourier-badi%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FLaPingvino%2Fcourier-badi%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FLaPingvino%2Fcourier-badi%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FLaPingvino%2Fcourier-badi%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FLaPingvino%2Fcourier-badi%2Fgh-pages%2Fbadges%2FUniversal.json

Courier Badi is an adapted version of the amazing Courier Prime font made by Quote-Unquote Apps. The purpose here is to add
missing characters that can be relevant to Bahá'í usage in a very wide sense. This font has been adapted under the terms of
the OFL and as it hasn't been made originally for Google Fonts, it might miss some of the requirements at least at first.
I am correcting the Google Fonts and other Fontbakery requirements over time, probably fixing some bugs here and there.

## About

I am a Bahá'í, customer support agent by trade and programmer in my free time and former jobs. I am a long time big fan of the Fountain screenplay markup language and have written a command line tool for this that uses Courier Prime to generate screenplay PDFs.

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://LaPingvino.github.io/courier-badi.

## Changelog

When you update your font (new version or new release), please report all notable changes here, with a date.
[Font Versioning](https://github.com/googlefonts/gf-docs/tree/main/Spec#font-versioning) is based on semver. 
Changelog example:

**13 July 2023. Version 0.400**
- Cyrillic merged in from Novikov's Courier Prime fork

**4 July 2023. Version 0.300**
- Dot below letters added

**4 July 2023. Version 0.200**
- Combining diacritics and capital sharp s added

**4 July 2023. Version 0.100**
- Bahá'í star added

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

Note that this project is a derivative of Courier Prime, also released under this same license
but with the reserved name Courier Prime Source. Courier itself is a public domain name and
Badi is a name from Bahá'í history.

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.
