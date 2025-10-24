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

**24 October 2025. Version 0.600**
- Complete Arabic features enhancement through 5 incremental levels
- Extended Arabic character support (Unicode 075x range)
- Comprehensive contextual forms (.fina, .init, .medi) for Arabic script
- Enhanced language support for Arabic (ARA), Farsi (FAR), and Urdu (URD)
- 625 lines of OpenType features with 320 optimized substitution rules
- Added incremental enhancement automation tool
- Production-ready Arabic typography with backward compatibility

**13 October 2024. Version 0.529**
- Prerelease Greek improvements

**22 July 2023. Version 0.520**
- Fixed the gaps in Italic. Corrected skew for Italic. Corrected position of Bahá'í star in Italic.

**14 July 2023. Version 0.510**
- Corrected the width of the merge so it is actually true monospace. Kinda breaks the catalan middle dot,
  not sure what to do about that, might add a ligature for that later.

**13 July 2023. Version 0.500**
- Merged in Arabic, Greek and extended Latin from No Name Fixed, thanks for the suggestion @Eli Hauser.
  The fit is surprisingly good, but I will probably fix up some characters like the u used for Vietnamese
  and some Greek characters that look too thin, if the monospace limitations permit this.

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
