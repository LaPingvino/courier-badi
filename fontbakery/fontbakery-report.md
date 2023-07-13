## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[26] CourierBadi-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "Copyright (c) 2023 Joop Kiefte (https://github.com/LaPingvino/courier-badi)

Derived from Courier Prime with original copyright:
Copyright (c) 2015
Quote-Unquote Apps (https://quoteunquoteapps.com)
with Reserved Font Name Courier Prime Source.

This Font Software is licensed under the SIL Open Font License
Version 1.1. This license is copied below
and is also available with a FAQ at: https://scripts.sil.org/OFL


-----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
-----------------------------------------------------------

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide development of collaborative font projects
to support the font creation efforts of academic and linguistic communities
and to provide a free and open framework in which fonts may be shared and improved in partnership with others.

The OFL allows the licensed fonts to be used
studied
modified and redistributed freely as long as they are not sold by themselves. The fonts
including any derivative works
can be bundled
embedded
redistributed and/or sold with any software provided that any reserved names are not used by derivative works. The fonts and derivatives
however
cannot be released under any other type of license. The requirement for fonts to remain under this license does not apply to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright Holder(s) under this license and clearly marked as such. This may include source files
build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the copyright statement(s).

"Original Version" refers to the collection of Font Software components as distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to
deleting
or substituting -- in part or in whole -- any of the components of the Original Version
by changing formats or by porting the Font Software to a new environment.

"Author" refers to any designer
engineer
programmer
technical writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted
free of charge
to any person obtaining a copy of the Font Software
to use
study
copy
merge
embed
modify
redistribute
and sell modified and unmodified copies of the Font Software
subject to the following conditions:

1) Neither the Font Software nor any of its individual components
in Original or Modified Versions
may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled
redistributed and/or sold with any software
provided that each copy contains the above copyright notice and this license. These can be included either as stand-alone text files
human-readable headers or in the appropriate machine-readable metadata fields within text or binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font Name(s) unless explicit written permission is granted by the corresponding Copyright Holder. This restriction only applies to the primary font name as presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font Software shall not be used to promote
endorse or advertise any Modified Version
except to acknowledge the contribution(s) of the Copyright Holder(s) and the Author(s) or with their explicit written permission.

5) The Font Software
modified or unmodified
in part or in whole
must be distributed entirely under this license
and must not be distributed under any other license. The requirement for fonts to remain under this license does not apply to any document created using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS"
WITHOUT WARRANTY OF ANY KIND
EXPRESS OR IMPLIED
INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF COPYRIGHT
PATENT
TRADEMARK
OR OTHER RIGHT. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM
DAMAGES OR OTHER LIABILITY
INCLUDING ANY GENERAL
SPECIAL
INDIRECT
INCIDENTAL
OR CONSEQUENTIAL DAMAGES
WHETHER IN AN ACTION OF CONTRACT
TORT OR OTHERWISE
ARISING FROM
OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM OTHER DEALINGS IN THE FONT SOFTWARE." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2023 Joop Kiefte, Copyright (c) 2015 Quote-Unquote Apps." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/CourierBadi-Regular.ttf', 'fonts/ttf/CourierBadi-Italic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2087, but got 1827 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1364, but got 838 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (1638) and hhea ascent (1827) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Whitespace glyphs have ink? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_ink">com.google.fonts/check/whitespace_ink</a>)</summary><div>


* 🔥 **FAIL** Glyph "narrownbspace" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
* 🔥 **FAIL** Glyph "zeroWidthNoBreakSpace" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
</div></details><details><summary>🔥 <b>FAIL:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* 🔥 **FAIL** The following glyph names do not comply with naming conventions: Abreve-cy, Adieresis-cy, Aie-cy, Cheabkhasian-cy, Chedescender-cy, Chedescenderabkhasian-cy, Chedieresis-cy, Chekhakassian-cy, Cheverticalstroke-cy, Dzeabkhasian-cy, Edieresis-cy, Eiotified-cy, Elhook-cy, Eltail-cy, Emtail-cy, Enghe-cy, Enhook-cy, Entail-cy, Ertick-cy, Esdescender-cy, Fita-cy, Gedescender-cy, Ghemiddlehook-cy, Haabkhasian-cy, Hadescender-cy, Hahook-cy, Hastroke-cy, Idieresis-cy, Iebreve-cy, Iegrave-cy, Iishorttail-cy, Imacron-cy, Izhitsa-cy, Izhitsadblgrave-cy, Kabashkir-cy, Kahook-cy, Kastroke-cy, Kaverticalstroke-cy, Koppa-cy, Ksi-cy, Obarreddieresis-cy, Odieresis-cy, Omega-cy, Palochka-cy, Pemiddlehook-cy, Psi-cy, Schwadieresis-cy, Semisoftsign-cy, Tedescender-cy, Tetse-cy, Udieresis-cy, Uhungarumlaut-cy, Uk-cy, Umacron-cy, Yat-cy, Yerudieresis-cy, Yusbig-cy, Yusbigiotified-cy, Yuslittle-cy, Yuslittleiotified-cy, Zedescender-cy, Zedieresis-cy, Zhebreve-cy, Zhedescender-cy, Zhedieresis-cy, abreve-cy, adieresis-cy, ae-ar, ae-ar.fina, afghani-ar, aie-cy, ain-ar, ain-ar.fina, ain-ar.init, ain-ar.medi, ainThreedots-ar, ainThreedots-ar.fina, ainThreedots-ar.init, ainThreedots-ar.medi, ainThreedotsbelow-ar, ainThreedotsbelow-ar.fina, ainThreedotsbelow-ar.init, ainThreedotsbelow-ar.medi, ainThreedotsdownabove-ar, ainThreedotsdownabove-ar.fina, ainThreedotsdownabove-ar.init, ainThreedotsdownabove-ar.medi, ainTwodotshorizontalabove-ar, ainTwodotshorizontalabove-ar.fina, ainTwodotshorizontalabove-ar.init, ainTwodotshorizontalabove-ar.medi, ainTwodotsverticalabove-ar, ainTwodotsverticalabove-ar.fina, ainTwodotsverticalabove-ar.init, ainTwodotsverticalabove-ar.medi, ainabove-ar, alef-ar, alef-ar.fina, alef-ar.fina.alt, alef-ar.fina.short, alef-ar.fina.shorter, alef-ar.short, alef-ar.shorter, alefHamzaabove-ar, alefHamzaabove-ar.fina, alefHamzaabove-ar.fina.alt, alefHamzabelow-ar, alefHamzabelow-ar.fina, alefHamzabelow-ar.fina.alt, alefLamYehabove-ar, alefMadda-ar, alefMadda-ar.fina, alefMadda-ar.fina.alt, alefMaksura-ar, alefMaksura-ar.fina, alefMaksura-ar.init, alefMaksura-ar.medi, alefThreeabove-ar, alefThreeabove-ar.fina, alefThreeabove-ar.fina.alt, alefTwoabove-ar, alefTwoabove-ar.fina, alefTwoabove-ar.fina.alt, alefWasla-ar, alefWasla-ar.fina, alefWasla-ar.fina.alt, alefWavyhamzaabove-ar, alefWavyhamzaabove-ar.fina, alefWavyhamzaabove-ar.fina.alt, alefWavyhamzabelow-ar, alefWavyhamzabelow-ar.fina, alefWavyhamzabelow-ar.fina.alt, alefabove-ar, alefbelow-ar, aleflow-ar, allah-ar, allahlong-ar, annisfabove-ar, arrubabove-ar, assajdaabove-ar, asterisk-ar, aththalathaabove-ar, beeh-ar, beeh-ar.fina, beeh-ar.init, beeh-ar.medi, beh-ar, beh-ar.fina, beh-ar.init, beh-ar.medi, behDotless-ar, behDotless-ar.fina, behDotless-ar.hah, behDotless-ar.init, behDotless-ar.medi, behMeemabove-ar, behMeemabove-ar.fina, behMeemabove-ar.init, behMeemabove-ar.medi, behThreedotshorizontalbelow-ar, behThreedotshorizontalbelow-ar.fina, behThreedotshorizontalbelow-ar.init, behThreedotshorizontalbelow-ar.medi, behThreedotsupabove-ar, behThreedotsupabove-ar.fina, behThreedotsupabove-ar.init, behThreedotsupabove-ar.medi, behThreedotsupbelow-ar, behThreedotsupbelow-ar.fina, behThreedotsupbelow-ar.init, behThreedotsupbelow-ar.medi, behTwodotsbelowDotabove-ar, behTwodotsbelowDotabove-ar.fina, behTwodotsbelowDotabove-ar.init, behTwodotsbelowDotabove-ar.medi, behVabove-ar, behVabove-ar.fina, behVabove-ar.init, behVabove-ar.medi, behVbelow-ar, behVbelow-ar.fina, behVbelow-ar.init, behVbelow-ar.medi, behVinvertedbelow-ar, behVinvertedbelow-ar.fina, behVinvertedbelow-ar.init, behVinvertedbelow-ar.medi, beh_meem-ar.init, beheh-ar, beheh-ar.fina, beheh-ar.init, beheh-ar.medi, behhamzaabove-ar, behhamzaabove-ar.fina, behhamzaabove-ar.init, behhamzaabove-ar.medi, bismillah-ar, cheabkhasian-cy, chedescender-cy, chedescenderabkhasian-cy, chedieresis-cy, chekhakassian-cy, cheverticalstroke-cy, comma-ar, cuberoot-ar, dad-ar, dad-ar.fina, dad-ar.init, dad-ar.medi, dadDotbelow-ar, dadDotbelow-ar.fina, dadDotbelow-ar.init, dadDotbelow-ar.medi, dahal-ar, dahal-ar.fina, dal-ar, dal-ar.fina, dalDotbelow-ar, dalDotbelow-ar.fina, dalDotbelowTah-ar, dalDotbelowTah-ar.fina, dalFourdots-ar, dalFourdots-ar.fina, dalRing-ar, dalRing-ar.fina, dalThreedotsbelow-ar, dalThreedotsbelow-ar.fina, dalThreedotsdown-ar, dalThreedotsdown-ar.fina, dalTwodotsverticalbelowTah-ar, dalTwodotsverticalbelowTah-ar.fina, dalVinvertedabove-ar, dalVinvertedabove-ar.fina, dalVinvertedbelow-ar, dalVinvertedbelow-ar.fina, damma-ar, damma-ar.medi, dammaCurly-ar, dammaDot-ar, dammainverted-ar, dammareversed-ar, dammasmall-ar, dammatan-ar, dammatanCurly-ar, dammaturnedbelow-ar, dasiapneumatacomb-cy, dateseparator-ar, ddahal-ar, ddahal-ar.fina, ddal-ar, ddal-ar.fina, decimalseparator-ar, disputedendofayah-ar, dotStopabove-ar, dotaboveSymbol-ar, dotbelowSymbol-ar, dotvowelbelow-ar, doublerightarrowheadDotabove-ar, doublerightarrowheadabove-ar, doublestroke-ar, doubleverticalbarbelowSymbol-ar, dul-ar, dul-ar.fina, dyeh-ar, dyeh-ar.fina, dyeh-ar.init, dyeh-ar.medi, dzeabkhasian-cy, e-ar, e-ar.fina, e-ar.init, e-ar.medi, edieresis-cy, eight-ar, eiotified-cy, elhook-cy, eltail-cy, emtail-cy, endofayah-ar, enghe-cy, enhook-cy, entail-cy, ertick-cy, esdescender-cy, fatha-ar, fatha-ar.medi, fathaCurly-ar, fathaDotabove-ar, fathaHorizont-ar, fathaRing-ar, fathasmall-ar, fathatan-ar, fathatan-ar.medi, fathatanCurly-ar, fathatwodots-ar, feh-ar, feh-ar.fina, feh-ar.init, feh-ar.medi, fehAfrican-ar, fehAfrican-ar.fina, fehAfrican-ar.init, fehAfrican-ar.medi, fehDotbelow-ar, fehDotbelow-ar.fina, fehDotbelow-ar.init, fehDotbelow-ar.medi, fehDotbelowThreedotsabove-ar, fehDotbelowThreedotsabove-ar.fina, fehDotbelowThreedotsabove-ar.init, fehDotbelowThreedotsabove-ar.medi, fehDotless-ar, fehDotless-ar.fina, fehDotless-ar.init, fehDotless-ar.medi, fehDotmovedbelow-ar, fehDotmovedbelow-ar.fina, fehDotmovedbelow-ar.init, fehDotmovedbelow-ar.medi, fehThreedotsbelow-ar, fehThreedotsbelow-ar.fina, fehThreedotsbelow-ar.init, fehThreedotsbelow-ar.medi, fehThreedotsupbelow-ar, fehThreedotsupbelow-ar.fina, fehThreedotsupbelow-ar.init, fehThreedotsupbelow-ar.medi, fehTwodotsbelow-ar, fehTwodotsbelow-ar.fina, fehTwodotsbelow-ar.init, fehTwodotsbelow-ar.medi, fita-cy, five-ar, five-persian, footnotemarker-ar, footnotemarkerabove-ar, four-ar, four-persian, four-persian.urdu, fourabove-ar, fourbelow-ar, fourdotsaboveSymbol-ar, fourdotsbelowSymbol-ar, fourthroot-ar, fullstop-ar, gaf-ar, gaf-ar.fina, gaf-ar.init, gaf-ar.medi, gafInvertedstroke-ar, gafInvertedstroke-ar.fina, gafInvertedstroke-ar.init, gafInvertedstroke-ar.medi, gafRing-ar, gafRing-ar.fina, gafRing-ar.init, gafRing-ar.medi, gafThreedots-ar, gafThreedots-ar.fina, gafThreedots-ar.init, gafThreedots-ar.medi, gafTwodotsbelow-ar, gafTwodotsbelow-ar.fina, gafTwodotsbelow-ar.init, gafTwodotsbelow-ar.medi, gafsarkashabove-ar, gedescender-cy, ghain-ar, ghain-ar.fina, ghain-ar.init, ghain-ar.medi, ghainDotbelow-ar, ghainDotbelow-ar.fina, ghainDotbelow-ar.init, ghainDotbelow-ar.medi, ghainThreedotsabove-ar, ghainThreedotsabove-ar.fina, ghainThreedotsabove-ar.init, ghainThreedotsabove-ar.medi, ghemiddlehook-cy, gueh-ar, gueh-ar.fina, gueh-ar.init, gueh-ar.medi, haabkhasian-cy, hadescender-cy, hah-ar, hah-ar.fina, hah-ar.init, hah-ar.medi, hahFourbelow-ar, hahFourbelow-ar.fina, hahFourbelow-ar.init, hahFourbelow-ar.medi, hahHamzaabove-ar, hahHamzaabove-ar.fina, hahHamzaabove-ar.init, hahHamzaabove-ar.medi, hahTahTwodotshorizontalbelow-ar, hahTahTwodotshorizontalbelow-ar.fina, hahTahTwodotshorizontalbelow-ar.init, hahTahTwodotshorizontalbelow-ar.medi, hahTahabove-ar, hahTahabove-ar.fina, hahTahabove-ar.init, hahTahabove-ar.medi, hahTahbelow-ar, hahTahbelow-ar.fina, hahTahbelow-ar.init, hahTahbelow-ar.medi, hahThreedotsabove-ar, hahThreedotsabove-ar.fina, hahThreedotsabove-ar.init, hahThreedotsabove-ar.medi, hahThreedotsupbelow-ar, hahThreedotsupbelow-ar.fina, hahThreedotsupbelow-ar.init, hahThreedotsupbelow-ar.medi, hahTwodotshorizontalabove-ar, hahTwodotshorizontalabove-ar.fina, hahTwodotshorizontalabove-ar.init, hahTwodotshorizontalabove-ar.medi, hahTwodotsverticalabove-ar, hahTwodotsverticalabove-ar.fina, hahTwodotsverticalabove-ar.init, hahTwodotsverticalabove-ar.medi, hahabove-ar, hahook-cy, hamza-ar, hamzaabove-ar, hamzabelow-ar, hastroke-cy, heh-ar, heh-ar.fina, heh-ar.init, heh-ar.medi, hehDoachashmee-ar, hehDoachashmee-ar.fina, hehDoachashmee-ar.init, hehDoachashmee-ar.init.comp, hehDoachashmee-ar.medi, hehHamzaabove-ar, hehHamzaabove-ar.fina, hehVinvertedabove-ar, hehVinvertedabove-ar.fina, hehVinvertedabove-ar.init, hehVinvertedabove-ar.medi, hehgoal-ar, hehgoal-ar.fina, hehgoal-ar.init, hehgoal-ar.medi, hehgoalHamzaabove-ar, hehgoalHamzaabove-ar.fina, highhamza-ar, highhamza-ar.narrow, highhamzaAlef-ar, highhamzaWaw-ar, highhamzaYeh-ar, highhamzaYeh-ar.init, highwaw-ar, hizb-ar, hundredthousandssigncomb-cy, idieresis-cy, iebreve-cy, iegrave-cy, iishorttail-cy, imacron-cy, izhitsa-cy, izhitsadblgrave-cy, jallajalalouhou-ar, jeem-ar, jeem-ar.fina, jeem-ar.init, jeem-ar.medi, jeemThreedotsabove-ar, jeemThreedotsabove-ar.fina, jeemThreedotsabove-ar.init, jeemThreedotsabove-ar.medi, jeemThreedotsbelow-ar, jeemThreedotsbelow-ar.fina, jeemThreedotsbelow-ar.init, jeemThreedotsbelow-ar.medi, jeemTwodotsabove-ar, jeemTwodotsabove-ar.fina, jeemTwodotsabove-ar.init, jeemTwodotsabove-ar.medi, jeemabove-ar, jeh-ar, jeh-ar.fina, kabashkir-cy, kaf-ar, kaf-ar.fina, kaf-ar.init, kaf-ar.medi, kafDotabove-ar, kafDotabove-ar.fina, kafDotabove-ar.init, kafDotabove-ar.medi, kafDotbelow-ar, kafDotbelow-ar.fina, kafDotbelow-ar.init, kafDotbelow-ar.medi, kafDotless-ar, kafDotless-ar.fina, kafRing-ar, kafRing-ar.fina, kafRing-ar.init, kafRing-ar.medi, kafThreedotsbelow-ar, kafThreedotsbelow-ar.fina, kafThreedotsbelow-ar.init, kafThreedotsbelow-ar.medi, kafTwodotshorizontalabove-ar, kafTwodotshorizontalabove-ar.fina, kafTwodotshorizontalabove-ar.init, kafTwodotshorizontalabove-ar.medi, kafswash-ar, kafswash-ar.fina, kafswash-ar.init, kafswash-ar.medi, kahook-cy, kashida-ar, kashidaFina-ar, kasra-ar, kasra-ar.medi, kasraCurly-ar, kasraDotbelow-ar, kasrasmall-ar, kasratan-ar, kasratanCurly-ar, kastroke-cy, kaverticalstroke-cy, keheh-ar, keheh-ar.fina, keheh-ar.init, keheh-ar.medi, kehehDotabove-ar, kehehDotabove-ar.fina, kehehDotabove-ar.init, kehehDotabove-ar.medi, kehehThreedotsabove-ar, kehehThreedotsabove-ar.fina, kehehThreedotsabove-ar.init, kehehThreedotsabove-ar.medi, kehehThreedotsbelow-ar, kehehThreedotsbelow-ar.fina, kehehThreedotsbelow-ar.init, kehehThreedotsbelow-ar.medi, kehehThreedotsupbelow-ar, kehehThreedotsupbelow-ar.fina, kehehThreedotsupbelow-ar.init, kehehThreedotsupbelow-ar.medi, kehehTwodotshorizontalabove-ar, kehehTwodotshorizontalabove-ar.fina, kehehTwodotshorizontalabove-ar.init, kehehTwodotshorizontalabove-ar.medi, kehehVabove-ar, kehehVabove-ar.fina, kehehVabove-ar.init, kehehVabove-ar.medi, khah-ar, khah-ar.fina, khah-ar.init, khah-ar.medi, kirghizoe-ar, kirghizoe-ar.fina, kirghizyu-ar, kirghizyu-ar.fina, koppa-cy, ksi-cy, lam-ar, lam-ar.fina, lam-ar.init, lam-ar.medi, lam-ar.medi.short, lamAlefabove-ar, lamBar-ar, lamBar-ar.fina, lamBar-ar.init, lamBar-ar.medi, lamDotabove-ar, lamDotabove-ar.fina, lamDotabove-ar.init, lamDotabove-ar.medi, lamDoublebar-ar, lamDoublebar-ar.fina, lamDoublebar-ar.init, lamDoublebar-ar.medi, lamTahabove-ar, lamTahabove-ar.fina, lamTahabove-ar.init, lamTahabove-ar.medi, lamThreedotsabove-ar, lamThreedotsabove-ar.fina, lamThreedotsabove-ar.init, lamThreedotsabove-ar.medi, lamThreedotsbelow-ar, lamThreedotsbelow-ar.fina, lamThreedotsbelow-ar.init, lamThreedotsbelow-ar.medi, lamVabove-ar, lamVabove-ar.fina, lamVabove-ar.init, lamVabove-ar.medi, lam_alef-ar, lam_alef-ar.fina, lam_alefHamzaabove-ar, lam_alefHamzaabove-ar.fina, lam_alefHamzabelow-ar, lam_alefHamzabelow-ar.fina, lam_alefMadda-ar, lam_alefMadda-ar.fina, lam_hah-ar.init, lam_jeem-ar.init, lam_khah-ar.init, lam_meem-ar.init, lam_meem_hah-ar.init, largerounddotbelow-ar, leftarrowheadabove-ar, leftarrowheadbelow-ar, lowernumeral-greek, madda-ar, maddalong-ar, mark-ar, marksidewaysnoonghunna-ar, meem-ar, meem-ar.fina, meem-ar.init, meem-ar.medi, meemDotabove-ar, meemDotabove-ar.fina, meemDotabove-ar.init, meemDotabove-ar.medi, meemDotbelow-ar, meemDotbelow-ar.fina, meemDotbelow-ar.init, meemDotbelow-ar.medi, meemStopabove-ar, meemThreedotsabove-ar, meemThreedotsabove-ar.fina, meemThreedotsabove-ar.init, meemThreedotsabove-ar.medi, meemabove-ar, meembelow-ar, millionssigncomb-cy, miniKeheh-ar, misraComma-ar, mohammad-ar, ng-ar, ng-ar.fina, ng-ar.init, ng-ar.medi, ngoeh-ar, ngoeh-ar.fina, ngoeh-ar.init, ngoeh-ar.medi, nine-ar, noon-ar, noon-ar.fina, noon-ar.init, noon-ar.medi, noonAfrican-ar, noonAfrican-ar.fina, noonAfrican-ar.init, noonAfrican-ar.medi, noonDotbelow-ar, noonDotbelow-ar.fina, noonDotbelow-ar.init, noonDotbelow-ar.medi, noonKasraabove-ar, noonKasrabelow-ar, noonRing-ar, noonRing-ar.fina, noonRing-ar.init, noonRing-ar.medi, noonTahabove-ar, noonTahabove-ar.fina, noonTahabove-ar.init, noonTahabove-ar.medi, noonThreedotsabove-ar, noonThreedotsabove-ar.fina, noonThreedotsabove-ar.init, noonThreedotsabove-ar.medi, noonTwodotsbelow-ar, noonTwodotsbelow-ar.fina, noonTwodotsbelow-ar.init, noonTwodotsbelow-ar.medi, noonVabove-ar, noonVabove-ar.fina, noonVabove-ar.init, noonVabove-ar.medi, noonabove-ar, noonghunna-ar, noonghunna-ar.fina, noonghunna-ar.init, noonghunna-ar.medi, noonghunnaabove-ar, note-musical, number-ar, numbermark-ar, numeral-greek, nyeh-ar, nyeh-ar.fina, nyeh-ar.init, nyeh-ar.medi, obarreddieresis-cy, odieresis-cy, oe-ar, oe-ar.fina, omega-cy, one-ar, opendammatan-ar, openfathatan-ar, openkasratan-ar, pagenumber-ar, palatalizationcomb-cy, parenleft-ar, parenright-ar, peh-ar, peh-ar.fina, peh-ar.init, peh-ar.medi, pehMeemabove-ar, pehMeemabove-ar.fina, pehMeemabove-ar.init, pehMeemabove-ar.medi, pehVabove-ar, pehVabove-ar.fina, pehVabove-ar.init, pehVabove-ar.medi, peheh-ar, peheh-ar.fina, peheh-ar.init, peheh-ar.medi, pemiddlehook-cy, percent-ar, pertenthousand-ar, perthousand-ar, psi-cy, psilipneumatacomb-cy, qaf-ar, qaf-ar.fina, qaf-ar.init, qaf-ar.medi, qafAfrican-ar, qafAfrican-ar.fina, qafAfrican-ar.init, qafAfrican-ar.medi, qafDotabove-ar, qafDotabove-ar.fina, qafDotabove-ar.init, qafDotabove-ar.medi, qafDotbelow-ar, qafDotbelow-ar.fina, qafDotbelow-ar.init, qafDotbelow-ar.medi, qafDotless-ar, qafDotless-ar.fina, qafDotless-ar.init, qafDotless-ar.medi, qafLamAlefMaksuraabove-ar, qafThreedotsabove-ar, qafThreedotsabove-ar.fina, qafThreedotsabove-ar.init, qafThreedotsabove-ar.medi, qafThreedotsaboveAfrican-ar, qafThreedotsaboveAfrican-ar.fina, qafThreedotsaboveAfrican-ar.init, qafThreedotsaboveAfrican-ar.medi, qafabove-ar, qifabove-ar, question-ar, ray-ar, reh-ar, reh-ar.fina, rehDadabove-ar, rehDotbelow-ar, rehDotbelow-ar.fina, rehDotbelowdotabove-ar, rehDotbelowdotabove-ar.fina, rehFourdots-ar, rehFourdots-ar.fina, rehHahabove-ar, rehHamzaabove-ar, rehHamzaabove-ar.fina, rehLoop-ar, rehLoop-ar.fina, rehNoonabove-ar, rehNoonabove-ar.fina, rehRing-ar, rehRing-ar.fina, rehStroke-ar, rehStroke-ar.fina, rehTwodots-ar, rehTwodots-ar.fina, rehTwodotshorizontalaboveTahabove-ar, rehTwodotshorizontalaboveTahabove-ar.fina, rehTwodotsverticalabove-ar, rehTwodotsverticalabove-ar.fina, rehVbelow-ar, rehVbelow-ar.fina, rehVinvertedabove-ar, rehVinvertedabove-ar.fina, rehabove-ar, rehv-ar, rehv-ar.fina, rhombusStopabove-ar, rhombusStopbelow-ar, rightarrowheadDotabove-ar, rightarrowheadabove-ar, rightarrowheadbelow-ar, ringSymbol-ar, rnoon-ar, rnoon-ar.fina, rnoon-ar.init, rnoon-ar.medi, rreh-ar, rreh-ar.fina, sad-ar, sad-ar.fina, sad-ar.init, sad-ar.medi, sadLamAlefMaksuraabove-ar, sadThreedots-ar, sadThreedots-ar.fina, sadThreedots-ar.init, sadThreedots-ar.medi, sadThreedotsbelow-ar, sadThreedotsbelow-ar.fina, sadThreedotsbelow-ar.init, sadThreedotsbelow-ar.medi, sadTwodotsbelow-ar, sadTwodotsbelow-ar.fina, sadTwodotsbelow-ar.init, sadTwodotsbelow-ar.medi, sadabove-ar, safhaabove-ar, sahabove-ar, sajdah-ar, saktaabove-ar, samvat-ar, schwadieresis-cy, seen-ar, seen-ar.fina, seen-ar.init, seen-ar.medi, seenDotbelowDotabove-ar, seenDotbelowDotabove-ar.fina, seenDotbelowDotabove-ar.init, seenDotbelowDotabove-ar.medi, seenFourabove-ar, seenFourabove-ar.fina, seenFourabove-ar.init, seenFourabove-ar.medi, seenFourdotsabove-ar, seenFourdotsabove-ar.fina, seenFourdotsabove-ar.init, seenFourdotsabove-ar.medi, seenTahTwodotshorizontalabove-ar, seenTahTwodotshorizontalabove-ar.fina, seenTahTwodotshorizontalabove-ar.init, seenTahTwodotshorizontalabove-ar.medi, seenThreedotsbelow-ar, seenThreedotsbelow-ar.fina, seenThreedotsbelow-ar.init, seenThreedotsbelow-ar.medi, seenTwodotsverticalabove-ar, seenTwodotsverticalabove-ar.fina, seenTwodotsverticalabove-ar.init, seenTwodotsverticalabove-ar.medi, seenVinvertedabove-ar, seenVinvertedabove-ar.fina, seenVinvertedabove-ar.init, seenVinvertedabove-ar.medi, seenabove-ar, seenbelow-ar, semicolon-ar, semisoftsign-cy, seven-ar, seven-persian, seven-persian.urdu, shadda-ar, shadda-ar.medi, sheen-ar, sheen-ar.fina, sheen-ar.init, sheen-ar.medi, sheenDotbelow-ar, sheenDotbelow-ar.fina, sheenDotbelow-ar.init, sheenDotbelow-ar.medi, sheenThreedotsbelow-ar, sheenThreedotsbelow-ar.fina, sheenThreedotsbelow-ar.init, sheenThreedotsbelow-ar.medi, sindhiampersand-ar, sindhipostpositionmen-ar, sindhipostpositionmen-ar.fina, sindhipostpositionmen-ar.init, sindhipostpositionmen-ar.medi, six-ar, six-persian, smallainabove-ar, smallsadabove-ar, stroke-ar, sukun-ar, sukun-ar.medi, sukunoval-ar, sukunround-ar, tah-ar, tah-ar.fina, tah-ar.init, tah-ar.medi, tahThreedots-ar, tahThreedots-ar.fina, tahThreedots-ar.init, tahThreedots-ar.medi, tahTwodotsabove-ar, tahTwodotsabove-ar.fina, tahTwodotsabove-ar.init, tahTwodotsabove-ar.medi, tahabove-ar, tahbelowSymbol-ar, takhallusabove-ar, tcheh-ar, tcheh-ar.fina, tcheh-ar.init, tcheh-ar.medi, tchehDotabove-ar, tchehDotabove-ar.fina, tchehDotabove-ar.init, tchehDotabove-ar.medi, tchehVabove-ar, tchehVabove-ar.fina, tchehVabove-ar.init, tchehVabove-ar.medi, tcheheh-ar, tcheheh-ar.fina, tcheheh-ar.init, tcheheh-ar.medi, tedescender-cy, teh-ar, teh-ar.fina, teh-ar.init, teh-ar.medi, tehMarbuta-ar, tehMarbuta-ar.alt, tehMarbuta-ar.fina, tehMarbutagoal-ar, tehMarbutagoal-ar.fina, tehRing-ar, tehRing-ar.fina, tehRing-ar.init, tehRing-ar.medi, tehTehabove-ar, tehTehabove-ar.fina, tehTehabove-ar.init, tehTehabove-ar.medi, tehThreedotsdown-ar, tehThreedotsdown-ar.fina, tehThreedotsdown-ar.init, tehThreedotsdown-ar.medi, tehThreedotsupbelow-ar, tehThreedotsupbelow-ar.fina, tehThreedotsupbelow-ar.init, tehThreedotsupbelow-ar.medi, tehVabove-ar, tehVabove-ar.fina, tehVabove-ar.init, tehVabove-ar.medi, teh_hah-ar.init, teh_jeem-ar.init, teheh-ar, teheh-ar.fina, teheh-ar.init, teheh-ar.medi, tetse-cy, thal-ar, thal-ar.fina, theh-ar, theh-ar.fina, theh-ar.init, theh-ar.medi, thousand-cy, thousandseparator-ar, three-ar, threeabove-ar, threedots-ar, threedotsabove-ar, threedotsdownaboveSymbol-ar, threedotsdownbelowSymbol-ar, threedotshorizontalbelow-ar, threedotsupaboveSymbol-ar, threedotsupbelowSymbol-ar, titlocomb-cy, toneloopabove-ar, toneloopbelow-ar, toneonedotabove-ar, toneonedotbelow-ar, tonetwodotsabove-ar, tonetwodotsbelow-ar, tteh-ar, tteh-ar.fina, tteh-ar.init, tteh-ar.medi, ttehVabove-ar, ttehVabove-ar.fina, ttehVabove-ar.init, ttehVabove-ar.medi, tteheh-ar, tteheh-ar.fina, tteheh-ar.init, tteheh-ar.medi, two-ar, twoabove-ar, twodotshorizontalaboveSymbol-ar, twodotshorizontalbelowSymbol-ar, twodotsverticalaboveSymbol-ar, twodotsverticalbelowSymbol-ar, u-ar, u-ar.fina, uHamzaabove-ar, udieresis-cy, uhungarumlaut-cy, uk-cy, umacron-cy, vabove-ar, ve-ar, ve-ar.fina, veh-ar, veh-ar.fina, veh-ar.init, veh-ar.medi, verseComma-ar, vinvertedabove-ar, waqfaabove-ar, wasla-ar, wavyhamzabelow-ar, waw-ar, waw-ar.fina, wawDotabove-ar, wawDotabove-ar.fina, wawDotcenter-ar, wawDotcenter-ar.fina, wawHamzaabove-ar, wawHamzaabove-ar.fina, wawSmall-ar, wawStraight-ar, wawStraight-ar.fina, wawThreeAbove-ar, wawThreeAbove-ar.fina, wawTwoabove-ar, wawTwoabove-ar.fina, wawTwodots-ar, wawTwodots-ar.fina, wawbelow-ar, wawring-ar, wawring-ar.fina, yat-cy, year-ar, yeh-ar, yeh-ar.fina, yeh-ar.init, yeh-ar.medi, yeh-farsi, yeh-farsi.fina, yeh-farsi.init, yeh-farsi.medi, yehFourbelow-farsi, yehFourbelow-farsi.fina, yehFourbelow-farsi.init, yehFourbelow-farsi.medi, yehHamzaabove-ar, yehHamzaabove-ar.fina, yehHamzaabove-ar.init, yehHamzaabove-ar.medi, yehKashmiri-ar, yehKashmiri-ar.fina, yehKashmiri-ar.init, yehKashmiri-ar.medi, yehRohingya-ar, yehRohingya-ar.comp, yehRohingya-ar.fina, yehSmall-ar, yehTail-ar, yehTail-ar.fina, yehThreeabove-farsi, yehThreeabove-farsi.fina, yehThreeabove-farsi.init, yehThreeabove-farsi.medi, yehThreedotsabove-farsi, yehThreedotsabove-farsi.fina, yehThreedotsabove-farsi.init, yehThreedotsabove-farsi.medi, yehThreedotsbelow-ar, yehThreedotsbelow-ar.fina, yehThreedotsbelow-ar.init, yehThreedotsbelow-ar.medi, yehTwoabove-farsi, yehTwoabove-farsi.fina, yehTwoabove-farsi.init, yehTwoabove-farsi.medi, yehTwodotsabove-farsi, yehTwodotsabove-farsi.fina, yehTwodotsabove-farsi.init, yehTwodotsabove-farsi.medi, yehTwodotsbelowDotabove-ar, yehTwodotsbelowDotabove-ar.fina, yehTwodotsbelowDotabove-ar.init, yehTwodotsbelowDotabove-ar.medi, yehTwodotsbelowHamzaabove-ar, yehTwodotsbelowHamzaabove-ar.fina, yehTwodotsbelowHamzaabove-ar.init, yehTwodotsbelowHamzaabove-ar.medi, yehTwodotsbelowNoonabove-ar, yehTwodotsbelowNoonabove-ar.fina, yehTwodotsbelowNoonabove-ar.init, yehTwodotsbelowNoonabove-ar.medi, yehVabove-ar, yehVabove-ar.fina, yehVabove-ar.init, yehVabove-ar.medi, yehVinverted-farsi, yehVinverted-farsi.fina, yehVinverted-farsi.init, yehVinverted-farsi.medi, yeh_noon-ar.fina, yehabove-ar, yehbarree-ar, yehbarree-ar.fina, yehbarreeHamzaabove-ar, yehbarreeHamzaabove-ar.fina, yehbarreeThreeabove-ar, yehbarreeThreeabove-ar.fina, yehbarreeTwoabove-ar, yehbarreeTwoabove-ar.fina, yerudieresis-cy, yu-ar, yu-ar.fina, yusbig-cy, yusbigiotified-cy, yuslittle-cy, yuslittleiotified-cy, zah-ar, zah-ar.fina, zah-ar.init, zah-ar.medi, zain-ar, zain-ar.fina, zainVinvertedabove-ar, zainVinvertedabove-ar.fina, zainabove-ar, zedescender-cy, zedieresis-cy, zero-ar, zhebreve-cy, zhedescender-cy and zhedieresis-cy

 A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not. [code: found-invalid-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ȋ i̒ i҃ i҄ i҅ i҆ i̦̇ i̦̊ i̦̋ ȋ̦ i̦̒ i̦҃ i̦҄ i̦҅ i̦҆ i̧̇ i̧̊ i̧̋ ȋ̧ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 2297 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
* ⚠ **WARN** Font is monospaced but 555 glyphs (24.08%) have a different width. You should check the widths of: ['A', 'AE', 'Aacute', 'Abreve', 'Acircumflex', 'Adieresis', 'Agrave', 'Amacron', 'Aogonek', 'Aring', 'Atilde', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'Dcaron', 'Dcroat', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'Edieresis', 'Edotaccent', 'Egrave', 'Emacron', 'Eng', 'Eogonek', 'Eth', 'Euro', 'F', 'G', 'Gbreve', 'Gcircumflex', 'Gcommaaccent', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'IJ', 'Iacute', 'Ibreve', 'Icircumflex', 'Idieresis', 'Idotaccent', 'Igrave', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'Kcommaaccent', 'L', 'Lacute', 'Lcaron', 'Lcommaaccent', 'Ldot', 'Lslash', 'M', 'N', 'Nacute', 'Ncaron', 'Ncommaaccent', 'Ntilde', 'O', 'OE', 'Oacute', 'Obreve', 'Ocircumflex', 'Odieresis', 'Ograve', 'Ohungarumlaut', 'Omacron', 'Oslash', 'Otilde', 'P', 'Q', 'R', 'Racute', 'Rcaron', 'Rcommaaccent', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'Scommaaccent', 'T', 'Tbar', 'Tcaron', 'Tcommaaccent', 'Thorn', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'Udieresis', 'Ugrave', 'Uhungarumlaut', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'Ygrave', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'acircumflex', 'acute', 'acute.case', 'acutecomb', 'adieresis', 'ae', 'afii10017', 'afii10018', 'afii10019', 'afii10020', 'afii10021', 'afii10022', 'afii10023', 'afii10024', 'afii10025', 'afii10026', 'afii10027', 'afii10028', 'afii10029', 'afii10030', 'afii10031', 'afii10032', 'afii10033', 'afii10034', 'afii10035', 'afii10036', 'afii10037', 'afii10038', 'afii10039', 'afii10040', 'afii10041', 'afii10042', 'afii10043', 'afii10044', 'afii10045', 'afii10046', 'afii10047', 'afii10048', 'afii10049', 'afii10050', 'afii10051', 'afii10052', 'afii10053', 'afii10054', 'afii10055', 'afii10056', 'afii10057', 'afii10058', 'afii10059', 'afii10060', 'afii10061', 'afii10062', 'afii10065', 'afii10066', 'afii10067', 'afii10068', 'afii10069', 'afii10070', 'afii10071', 'afii10072', 'afii10073', 'afii10074', 'afii10075', 'afii10076', 'afii10077', 'afii10078', 'afii10079', 'afii10080', 'afii10081', 'afii10082', 'afii10083', 'afii10084', 'afii10085', 'afii10086', 'afii10087', 'afii10088', 'afii10089', 'afii10090', 'afii10091', 'afii10092', 'afii10093', 'afii10094', 'afii10095', 'afii10096', 'afii10097', 'afii10098', 'afii10099', 'afii10100', 'afii10101', 'afii10102', 'afii10103', 'afii10104', 'afii10105', 'afii10106', 'afii10107', 'afii10108', 'afii10109', 'afii10110', 'afii10145', 'afii10193', 'afii10846', 'afii61352', 'agrave', 'amacron', 'ampersand', 'aogonek', 'approxequal', 'aring', 'asciicircum', 'asciitilde', 'asterisk', 'at', 'atilde', 'b', 'backslash', 'bar', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'breve', 'breve.case', 'brokenbar', 'bullet', 'c', 'cacute', 'caron', 'caron.alt', 'caron.case', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'cedilla', 'cedilla.case', 'cent', 'circumflex', 'circumflex.case', 'colon', 'colon.alt', 'comma', 'comma.alt', 'commaaccent.case', 'copyright', 'currency', 'd', 'dagger', 'daggerdbl', 'dcaron', 'dcroat', 'degree', 'dieresis', 'dieresis.case', 'divide', 'dollar', 'dotaccent', 'dotaccent.case', 'dotbelowcomb', 'dotlessi', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'edieresis', 'edotaccent', 'egrave', 'eight', 'ellipsis', 'ellipsis.alt1', 'ellipsis.alt2', 'ellipsis.alt3', 'ellipsis.alt4', 'ellipsis.alt5', 'emacron', 'emdash', 'emdash.alt1', 'emdash.alt2', 'emdash.alt3', 'emdash.alt4', 'endash', 'eng', 'eogonek', 'equal', 'eth', 'exclam', 'exclamdown', 'f', 'five', 'florin', 'four', 'fraction', 'franc', 'g', 'gbreve', 'gcircumflex', 'gcommaaccent', 'gdotaccent', 'germandbls', 'grave', 'grave.case', 'gravecomb', 'greater', 'greaterequal', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'h', 'hbar', 'hcircumflex', 'hungarumlaut', 'hungarumlaut.case', 'hyphen', 'hyphen.alt', 'i', 'iacute', 'ibreve', 'icircumflex', 'idieresis', 'idotaccent', 'igrave', 'ij', 'imacron', 'infinity', 'integral', 'iogonek', 'itilde', 'j', 'jcircumflex', 'k', 'kcommaaccent', 'l', 'lacute', 'lcaron', 'lcommaaccent', 'ldot', 'less', 'lessequal', 'logicalnot', 'lozenge', 'lslash', 'm', 'macron', 'macron.case', 'minus', 'minute', 'multiply', 'n', 'nacute', 'ncaron', 'ncommaaccent', 'nine', 'notequal', 'ntilde', 'numbersign', 'o', 'oacute', 'obreve', 'ocircumflex', 'odieresis', 'oe', 'ogonek', 'ogonek.case', 'ograve', 'ohungarumlaut', 'omacron', 'one', 'onehalf', 'onequarter', 'ordfeminine', 'ordmasculine', 'oslash', 'otilde', 'p', 'paragraph', 'parenleft', 'parenright', 'partialdiff', 'percent', 'period', 'period.alt', 'period.squat', 'periodcentered', 'perthousand', 'pi', 'plus', 'plusminus', 'product', 'q', 'question', 'questiondown', 'quotedbl', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotesingle', 'r', 'racute', 'radical', 'rcaron', 'rcommaaccent', 'registered', 'ring', 'ring.case', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'scommaaccent', 'second', 'section', 'semicolon', 'semicolon.alt', 'seven', 'six', 'slash', 'space', 'sterling', 'summation', 't', 'tbar', 'tcaron', 'tcommaaccent', 'thorn', 'three', 'threequarters', 'tilde', 'tilde.case', 'tildecomb', 'trademark', 'two', 'u', 'u1F7D9', 'uacute', 'ubreve', 'ucircumflex', 'udieresis', 'ugrave', 'uhungarumlaut', 'umacron', 'underscore', 'uni000D', 'uni00A0', 'uni00B2', 'uni00B3', 'uni00B9', 'uni018F', 'uni021A', 'uni021B', 'uni0237', 'uni0259', 'uni0302', 'uni0304', 'uni0306', 'uni0307', 'uni0308', 'uni030A', 'uni030B', 'uni030C', 'uni0312', 'uni0326', 'uni0326.case', 'uni0327', 'uni0328', 'uni0394', 'uni03A9', 'uni03BC', 'uni040D', 'uni045D', 'uni0492', 'uni0493', 'uni049A', 'uni049B', 'uni04A2', 'uni04A3', 'uni04AE', 'uni04AF', 'uni04B0', 'uni04B1', 'uni04BA', 'uni04BB', 'uni04D8', 'uni04E8', 'uni04E9', 'uni1E0C', 'uni1E0D', 'uni1E24', 'uni1E25', 'uni1E62', 'uni1E63', 'uni1E6C', 'uni1E6D', 'uni1E92', 'uni1E93', 'uni1E9E', 'uni2011', 'uni2074', 'uni20A9', 'uni2215', 'uniFB01', 'uniFB02', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'yen', 'ygrave', 'z', 'zacute', 'zcaron', 'zdotaccent', 'zero'] [code: mono-outliers]
</div></details><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have duplicate components which have the same x,y coordinates. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components">com.google.fonts/check/glyf_non_transformed_duplicate_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have duplicate components which have the same x,y coordinates:
	* {'glyph': 'second', 'component': 'minute', 'x': 0, 'y': 0} [code: found-duplicates]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value '    ' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/rfn">com.google.fonts/check/name/rfn</a>)</summary><div>


* ⚠ **WARN** Name table entry contains "Reserved Font Name" for a family name (Courier Prime Source) that differs from the currently used family name (CourierBadi), which is fine. [code: legacy-familyname]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Threedotsinverted.alt.comp

	- ae-ar.fina

	- ainThreedots-ar.fina

	- ainThreedots-ar.init

	- ainThreedots-ar.medi

	- ainThreedotsbelow-ar.fina

	- ainThreedotsbelow-ar.init

	- ainThreedotsbelow-ar.medi

	- ainThreedotsdownabove-ar.fina

	- ainThreedotsdownabove-ar.init

	- ainThreedotsdownabove-ar.medi

	- ainTwodotshorizontalabove-ar.fina

	- ainTwodotshorizontalabove-ar.init

	- ainTwodotshorizontalabove-ar.medi

	- ainTwodotsverticalabove-ar.fina

	- ainTwodotsverticalabove-ar.init

	- ainTwodotsverticalabove-ar.medi

	- alef-ar.fina.alt

	- alef-ar.fina.short

	- alef-ar.fina.shorter

	- alef-ar.short

	- alef-ar.shorter

	- alefHamzaabove-ar.fina.alt

	- alefHamzabelow-ar.fina.alt

	- alefMadda-ar.fina.alt

	- alefThreeabove-ar.fina

	- alefThreeabove-ar.fina.alt

	- alefTwoabove-ar.fina

	- alefTwoabove-ar.fina.alt

	- alefWasla-ar.fina.alt

	- alefWavyhamzaabove-ar.fina

	- alefWavyhamzaabove-ar.fina.alt

	- alefWavyhamzabelow-ar.fina

	- alefWavyhamzabelow-ar.fina.alt

	- arabic_root.comp

	- behDotless-ar.fina

	- behDotless-ar.hah

	- behDotless-ar.init

	- behDotless-ar.medi

	- behMeemabove-ar.fina

	- behMeemabove-ar.init

	- behMeemabove-ar.medi

	- behThreedotshorizontalbelow-ar.fina

	- behThreedotshorizontalbelow-ar.init

	- behThreedotshorizontalbelow-ar.medi

	- behThreedotsupabove-ar.fina

	- behThreedotsupabove-ar.init

	- behThreedotsupabove-ar.medi

	- behThreedotsupbelow-ar.fina

	- behThreedotsupbelow-ar.init

	- behThreedotsupbelow-ar.medi

	- behTwodotsbelowDotabove-ar.fina

	- behTwodotsbelowDotabove-ar.init

	- behTwodotsbelowDotabove-ar.medi

	- behVabove-ar.fina

	- behVabove-ar.init

	- behVabove-ar.medi

	- behVbelow-ar.fina

	- behVbelow-ar.init

	- behVbelow-ar.medi

	- behVinvertedbelow-ar.fina

	- behVinvertedbelow-ar.init

	- behVinvertedbelow-ar.medi

	- behhamzaabove-ar.fina

	- behhamzaabove-ar.init

	- behhamzaabove-ar.medi

	- bigcircle

	- caron.cap

	- charbox.comp

	- circumflex.cap

	- circumflexcomb_acutecomb.cap

	- circumflexcomb_gravecomb.cap

	- circumflexcomb_hookabovecomb.cap

	- circumflexcomb_tildecomb.cap

	- colon.alt

	- colon.arabic

	- comma.alt

	- commaaccent.case

	- dadDotbelow-ar.fina

	- dadDotbelow-ar.init

	- dadDotbelow-ar.medi

	- dalDotbelow-ar.fina

	- dalDotbelowTah-ar.fina

	- dalFourdots-ar.fina

	- dalRing-ar.fina

	- dalThreedotsbelow-ar.fina

	- dalThreedotsdown-ar.fina

	- dalTwodotsverticalbelowTah-ar.fina

	- dalVinvertedabove-ar.fina

	- dalVinvertedbelow-ar.fina

	- dieresis.cap

	- doublestroke-ar

	- ellipsis.alt1

	- ellipsis.alt2

	- ellipsis.alt3

	- ellipsis.alt4

	- ellipsis.alt5

	- emdash.alt1

	- emdash.alt2

	- emdash.alt3

	- emdash.alt4

	- exclam.arabic

	- fehAfrican-ar.fina

	- fehAfrican-ar.init

	- fehAfrican-ar.medi

	- fehDotbelow-ar.fina

	- fehDotbelow-ar.init

	- fehDotbelow-ar.medi

	- fehDotbelowThreedotsabove-ar.fina

	- fehDotbelowThreedotsabove-ar.init

	- fehDotbelowThreedotsabove-ar.medi

	- fehDotless-ar.fina

	- fehDotless-ar.init

	- fehDotless-ar.medi

	- fehDotmovedbelow-ar.fina

	- fehDotmovedbelow-ar.init

	- fehDotmovedbelow-ar.medi

	- fehThreedotsbelow-ar.fina

	- fehThreedotsbelow-ar.init

	- fehThreedotsbelow-ar.medi

	- fehThreedotsupbelow-ar.fina

	- fehThreedotsupbelow-ar.init

	- fehThreedotsupbelow-ar.medi

	- fehTwodotsbelow-ar.fina

	- fehTwodotsbelow-ar.init

	- fehTwodotsbelow-ar.medi

	- four-persian.urdu

	- fourabove-ar

	- fourbelow-ar

	- gafInvertedstroke-ar.fina

	- gafInvertedstroke-ar.init

	- gafInvertedstroke-ar.medi

	- gafRing-ar.fina

	- gafRing-ar.init

	- gafRing-ar.medi

	- gafThreedots-ar.fina

	- gafThreedots-ar.init

	- gafThreedots-ar.medi

	- gafTwodotsbelow-ar.fina

	- gafTwodotsbelow-ar.init

	- gafTwodotsbelow-ar.medi

	- gafsarkashabove-ar

	- ghainDotbelow-ar.fina

	- ghainDotbelow-ar.init

	- ghainDotbelow-ar.medi

	- ghainThreedotsabove-ar.fina

	- ghainThreedotsabove-ar.init

	- ghainThreedotsabove-ar.medi

	- hahFourbelow-ar.fina

	- hahFourbelow-ar.init

	- hahFourbelow-ar.medi

	- hahHamzaabove-ar.fina

	- hahHamzaabove-ar.init

	- hahHamzaabove-ar.medi

	- hahTahTwodotshorizontalbelow-ar.fina

	- hahTahTwodotshorizontalbelow-ar.init

	- hahTahTwodotshorizontalbelow-ar.medi

	- hahTahabove-ar.fina

	- hahTahabove-ar.init

	- hahTahabove-ar.medi

	- hahTahbelow-ar.fina

	- hahTahbelow-ar.init

	- hahTahbelow-ar.medi

	- hahThreedotsabove-ar.fina

	- hahThreedotsabove-ar.init

	- hahThreedotsabove-ar.medi

	- hahThreedotsupbelow-ar.fina

	- hahThreedotsupbelow-ar.init

	- hahThreedotsupbelow-ar.medi

	- hahTwodotshorizontalabove-ar.fina

	- hahTwodotshorizontalabove-ar.init

	- hahTwodotshorizontalabove-ar.medi

	- hahTwodotsverticalabove-ar.fina

	- hahTwodotsverticalabove-ar.init

	- hahTwodotsverticalabove-ar.medi

	- hehDoachashmee-ar.init.comp

	- hehVinvertedabove-ar.fina

	- hehVinvertedabove-ar.init

	- hehVinvertedabove-ar.medi

	- hehgoalHamzaabove-ar.fina

	- highhamza-ar.narrow

	- highhamzaYeh-ar.init

	- hyphen.alt

	- idotaccent

	- ittisal.comp

	- jeemThreedotsabove-ar.fina

	- jeemThreedotsabove-ar.init

	- jeemThreedotsabove-ar.medi

	- jeemThreedotsbelow-ar.fina

	- jeemThreedotsbelow-ar.init

	- jeemThreedotsbelow-ar.medi

	- jeemTwodotsabove-ar.fina

	- jeemTwodotsabove-ar.init

	- jeemTwodotsabove-ar.medi

	- kafDotabove-ar.fina

	- kafDotabove-ar.init

	- kafDotabove-ar.medi

	- kafDotbelow-ar.fina

	- kafDotbelow-ar.init

	- kafDotbelow-ar.medi

	- kafDotless-ar

	- kafDotless-ar.fina

	- kafRing-ar.fina

	- kafRing-ar.init

	- kafRing-ar.medi

	- kafThreedotsbelow-ar.fina

	- kafThreedotsbelow-ar.init

	- kafThreedotsbelow-ar.medi

	- kafTwodotshorizontalabove-ar.fina

	- kafTwodotshorizontalabove-ar.init

	- kafTwodotshorizontalabove-ar.medi

	- kafswash-ar.fina

	- kafswash-ar.init

	- kafswash-ar.medi

	- kehehDotabove-ar.fina

	- kehehDotabove-ar.init

	- kehehDotabove-ar.medi

	- kehehThreedotsabove-ar.fina

	- kehehThreedotsabove-ar.init

	- kehehThreedotsabove-ar.medi

	- kehehThreedotsbelow-ar.fina

	- kehehThreedotsbelow-ar.init

	- kehehThreedotsbelow-ar.medi

	- kehehThreedotsupbelow-ar.fina

	- kehehThreedotsupbelow-ar.init

	- kehehThreedotsupbelow-ar.medi

	- kehehTwodotshorizontalabove-ar.fina

	- kehehTwodotshorizontalabove-ar.init

	- kehehTwodotshorizontalabove-ar.medi

	- kehehVabove-ar.fina

	- kehehVabove-ar.init

	- kehehVabove-ar.medi

	- lam-ar.medi.short

	- lamBar-ar.fina

	- lamBar-ar.init

	- lamBar-ar.medi

	- lamDotabove-ar.fina

	- lamDotabove-ar.init

	- lamDotabove-ar.medi

	- lamDoublebar-ar.fina

	- lamDoublebar-ar.init

	- lamDoublebar-ar.medi

	- lamTahabove-ar.fina

	- lamTahabove-ar.init

	- lamTahabove-ar.medi

	- lamThreedotsabove-ar.fina

	- lamThreedotsabove-ar.init

	- lamThreedotsabove-ar.medi

	- lamThreedotsbelow-ar.fina

	- lamThreedotsbelow-ar.init

	- lamThreedotsbelow-ar.medi

	- lamVabove-ar.fina

	- lamVabove-ar.init

	- lamVabove-ar.medi

	- meemDotabove-ar.fina

	- meemDotabove-ar.init

	- meemDotabove-ar.medi

	- meemDotbelow-ar.fina

	- meemDotbelow-ar.init

	- meemDotbelow-ar.medi

	- meemThreedotsabove-ar.fina

	- meemThreedotsabove-ar.init

	- meemThreedotsabove-ar.medi

	- miniKeheh-ar

	- noonAfrican-ar.fina

	- noonAfrican-ar.init

	- noonAfrican-ar.medi

	- noonDotbelow-ar.fina

	- noonDotbelow-ar.init

	- noonDotbelow-ar.medi

	- noonRing-ar.fina

	- noonRing-ar.init

	- noonRing-ar.medi

	- noonTahabove-ar.fina

	- noonTahabove-ar.init

	- noonTahabove-ar.medi

	- noonThreedotsabove-ar.fina

	- noonThreedotsabove-ar.init

	- noonThreedotsabove-ar.medi

	- noonTwodotsbelow-ar.fina

	- noonTwodotsbelow-ar.init

	- noonTwodotsbelow-ar.medi

	- noonVabove-ar.fina

	- noonVabove-ar.init

	- noonVabove-ar.medi

	- noonghunna-ar.init

	- noonghunna-ar.medi

	- pehMeemabove-ar.fina

	- pehMeemabove-ar.init

	- pehMeemabove-ar.medi

	- pehVabove-ar.fina

	- pehVabove-ar.init

	- pehVabove-ar.medi

	- percent.arabic.comp

	- period.alt

	- period.arabic

	- perthousandzero

	- qafAfrican-ar.fina

	- qafAfrican-ar.init

	- qafAfrican-ar.medi

	- qafDotabove-ar.fina

	- qafDotabove-ar.init

	- qafDotabove-ar.medi

	- qafDotbelow-ar.fina

	- qafDotbelow-ar.init

	- qafDotbelow-ar.medi

	- qafDotless-ar.fina

	- qafDotless-ar.init

	- qafDotless-ar.medi

	- qafThreedotsabove-ar.fina

	- qafThreedotsabove-ar.init

	- qafThreedotsabove-ar.medi

	- qafThreedotsaboveAfrican-ar.fina

	- qafThreedotsaboveAfrican-ar.init

	- qafThreedotsaboveAfrican-ar.medi

	- rehDotbelow-ar.fina

	- rehDotbelowdotabove-ar.fina

	- rehFourdots-ar.fina

	- rehHamzaabove-ar.fina

	- rehLoop-ar.fina

	- rehNoonabove-ar.fina

	- rehRing-ar.fina

	- rehStroke-ar.fina

	- rehTwodots-ar.fina

	- rehTwodotshorizontalaboveTahabove-ar.fina

	- rehTwodotsverticalabove-ar.fina

	- rehVbelow-ar.fina

	- rehVinvertedabove-ar.fina

	- rehabove-ar

	- rehv-ar.fina

	- sadThreedots-ar.fina

	- sadThreedots-ar.init

	- sadThreedots-ar.medi

	- sadThreedotsbelow-ar.fina

	- sadThreedotsbelow-ar.init

	- sadThreedotsbelow-ar.medi

	- sadTwodotsbelow-ar.fina

	- sadTwodotsbelow-ar.init

	- sadTwodotsbelow-ar.medi

	- seenDotbelowDotabove-ar.fina

	- seenDotbelowDotabove-ar.init

	- seenDotbelowDotabove-ar.medi

	- seenFourabove-ar.fina

	- seenFourabove-ar.init

	- seenFourabove-ar.medi

	- seenFourdotsabove-ar.fina

	- seenFourdotsabove-ar.init

	- seenFourdotsabove-ar.medi

	- seenTahTwodotshorizontalabove-ar.fina

	- seenTahTwodotshorizontalabove-ar.init

	- seenTahTwodotshorizontalabove-ar.medi

	- seenThreedotsbelow-ar.fina

	- seenThreedotsbelow-ar.init

	- seenThreedotsbelow-ar.medi

	- seenTwodotsverticalabove-ar.fina

	- seenTwodotsverticalabove-ar.init

	- seenTwodotsverticalabove-ar.medi

	- seenVinvertedabove-ar.fina

	- seenVinvertedabove-ar.init

	- seenVinvertedabove-ar.medi

	- semicolon.alt

	- seven-persian.urdu

	- sheenDotbelow-ar.fina

	- sheenDotbelow-ar.init

	- sheenDotbelow-ar.medi

	- sheenThreedotsbelow-ar.fina

	- sheenThreedotsbelow-ar.init

	- sheenThreedotsbelow-ar.medi

	- sindhipostpositionmen-ar.fina

	- sindhipostpositionmen-ar.init

	- sindhipostpositionmen-ar.medi

	- stroke-ar

	- tahThreedots-ar.fina

	- tahThreedots-ar.init

	- tahThreedots-ar.medi

	- tahTwodotsabove-ar.fina

	- tahTwodotsabove-ar.init

	- tahTwodotsabove-ar.medi

	- tail.comp

	- tchehDotabove-ar.fina

	- tchehDotabove-ar.init

	- tchehDotabove-ar.medi

	- tchehVabove-ar.fina

	- tchehVabove-ar.init

	- tchehVabove-ar.medi

	- tehMarbuta-ar.alt

	- tehMarbutagoal-ar.fina

	- tehRing-ar.fina

	- tehRing-ar.init

	- tehRing-ar.medi

	- tehTehabove-ar.fina

	- tehTehabove-ar.init

	- tehTehabove-ar.medi

	- tehThreedotsdown-ar.fina

	- tehThreedotsdown-ar.init

	- tehThreedotsdown-ar.medi

	- tehThreedotsupbelow-ar.fina

	- tehThreedotsupbelow-ar.init

	- tehThreedotsupbelow-ar.medi

	- tehVabove-ar.fina

	- tehVabove-ar.init

	- tehVabove-ar.medi

	- threeabove-ar

	- threedotshorizontalbelow-ar

	- ttehVabove-ar.fina

	- ttehVabove-ar.init

	- ttehVabove-ar.medi

	- twoabove-ar

	- wasla-ar

	- wawDotabove-ar.fina

	- wawDotcenter-ar.fina

	- wawStraight-ar.fina

	- wawThreeAbove-ar.fina

	- wawTwoabove-ar.fina

	- wawTwodots-ar.fina

	- wawring-ar.fina

	- yehFourbelow-farsi.fina

	- yehFourbelow-farsi.init

	- yehFourbelow-farsi.medi

	- yehKashmiri-ar.fina

	- yehKashmiri-ar.init

	- yehKashmiri-ar.medi

	- yehRohingya-ar.comp

	- yehRohingya-ar.fina

	- yehTail-ar.fina

	- yehThreeabove-farsi.fina

	- yehThreeabove-farsi.init

	- yehThreeabove-farsi.medi

	- yehThreedotsabove-farsi.fina

	- yehThreedotsabove-farsi.init

	- yehThreedotsabove-farsi.medi

	- yehThreedotsbelow-ar.fina

	- yehThreedotsbelow-ar.init

	- yehThreedotsbelow-ar.medi

	- yehTwoabove-farsi.fina

	- yehTwoabove-farsi.init

	- yehTwoabove-farsi.medi

	- yehTwodotsabove-farsi.fina

	- yehTwodotsabove-farsi.init

	- yehTwodotsabove-farsi.medi

	- yehTwodotsbelowDotabove-ar.fina

	- yehTwodotsbelowDotabove-ar.init

	- yehTwodotsbelowDotabove-ar.medi

	- yehTwodotsbelowHamzaabove-ar.fina

	- yehTwodotsbelowHamzaabove-ar.init

	- yehTwodotsbelowHamzaabove-ar.medi

	- yehTwodotsbelowNoonabove-ar.fina

	- yehTwodotsbelowNoonabove-ar.init

	- yehTwodotsbelowNoonabove-ar.medi

	- yehVabove-ar.fina

	- yehVabove-ar.init

	- yehVabove-ar.medi

	- yehVinverted-farsi.fina

	- yehVinverted-farsi.init

	- yehVinverted-farsi.medi

	- yehbarreeThreeabove-ar.fina

	- yehbarreeTwoabove-ar.fina

	- zainVinvertedabove-ar.fina 

	- zero.slash
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: sigmafinal	Contours detected: 2	Expected: 1

	- Glyph name: yuslittleiotified-cy	Contours detected: 5	Expected: 2

	- Glyph name: yusbigiotified-cy	Contours detected: 3	Expected: 2

	- Glyph name: Ksi-cy	Contours detected: 1	Expected: 2

	- Glyph name: ksi-cy	Contours detected: 1	Expected: 2

	- Glyph name: Izhitsadblgrave-cy	Contours detected: 2	Expected: 3

	- Glyph name: Uk-cy	Contours detected: 2	Expected: 3

	- Glyph name: uk-cy	Contours detected: 2	Expected: 3

	- Glyph name: ahookabove	Contours detected: 2	Expected: 3

	- Glyph name: Acircumflexhookabove	Contours detected: 3	Expected: 4

	- Glyph name: Acircumflextilde	Contours detected: 3	Expected: 4

	- Glyph name: Abrevetilde	Contours detected: 3	Expected: 4

	- Glyph name: abrevetilde	Contours detected: 3	Expected: 4

	- Glyph name: ehookabove	Contours detected: 2	Expected: 3

	- Glyph name: Ecircumflexhookabove	Contours detected: 2	Expected: 3

	- Glyph name: Ecircumflextilde	Contours detected: 2	Expected: 3

	- Glyph name: ihookabove	Contours detected: 1	Expected: 2

	- Glyph name: ohookabove	Contours detected: 2	Expected: 3

	- Glyph name: Ocircumflexhookabove	Contours detected: 3	Expected: 4

	- Glyph name: Ocircumflextilde	Contours detected: 3	Expected: 4

	- Glyph name: Ohorntilde	Contours detected: 2	Expected: 3 or 4

	- Glyph name: ohorntilde	Contours detected: 2	Expected: 3

	- Glyph name: Uhorntilde	Contours detected: 1	Expected: 2

	- Glyph name: uhorntilde	Contours detected: 1	Expected: 2

	- Glyph name: narrownbspace	Contours detected: 28	Expected: 0

	- Glyph name: minute	Contours detected: 0	Expected: 1

	- Glyph name: second	Contours detected: 0	Expected: 2

	- Glyph name: interrobang	Contours detected: 3	Expected: 2

	- Glyph name: colonsign	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: divorceSymbol	Contours detected: 5	Expected: 3

	- Glyph name: gnaborretni	Contours detected: 3	Expected: 2

	- Glyph name: zeroWidthNoBreakSpace	Contours detected: 25	Expected: 0

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1 

	- Glyph name: tbar	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 1228 among a set of 13 math glyphs.
The following math glyphs have a different width, though:

Width = 1075:
sphericalangle
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acute.case (unencoded), breve.case (unencoded), caron.case (unencoded), circumflex.case (unencoded), dieresis.case (unencoded), dotaccent.case (unencoded), grave.case (unencoded), hungarumlaut.case (unencoded), leftarrowheadabove-ar (U+08F7), macron.case (unencoded), ring.case (unencoded) and tilde.case (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 VS1 (U+FE00), VS10 (U+FE09), VS11 (U+FE0A), VS12 (U+FE0B), VS13 (U+FE0C), VS14 (U+FE0D), VS15 (U+FE0E), VS16 (U+FE0F), VS2 (U+FE01), VS3 (U+FE02), VS4 (U+FE03), VS5 (U+FE04), VS6 (U+FE05), VS7 (U+FE06), VS8 (U+FE07), VS9 (U+FE08), acutecomb (U+0301), ainabove-ar (U+0611), alefLamYehabove-ar (U+0616), alefabove-ar (U+0670), alefbelow-ar (U+0656), annisfabove-ar (U+08DC), arrubabove-ar (U+08D4), assajdaabove-ar (U+08DB), aththalathaabove-ar (U+08DA), brevebelowcomb (U+032E), breveinvertedbelowcomb (U+032F), breveinvertedcomb (U+0311), damma-ar (U+064F), dammaCurly-ar (U+08E5), dammaDot-ar (U+08FE), dammainverted-ar (U+0657), dammareversed-ar (U+065D), dammasmall-ar (U+0619), dammatan-ar (U+064C), dammatanCurly-ar (U+08E8), dammaturnedbelow-ar (U+08E3), dasiapneumatacomb-cy (U+0485), dblgravecomb (U+030F), dotStopabove-ar (U+06EC), dotbelowcomb (U+0323), dotvowelbelow-ar (U+065C), doublerightarrowheadDotabove-ar (U+08FC), doublerightarrowheadabove-ar (U+08FB), fatha-ar (U+064E), fathaCurly-ar (U+08E4), fathaDotabove-ar (U+08F5), fathaHorizont-ar (U+0659), fathaRing-ar (U+08F4), fathasmall-ar (U+0618), fathatan-ar (U+064B), fathatanCurly-ar (U+08E7), fathatwodots-ar (U+065E), footnotemarkerabove-ar (U+08E0), graphemejoinercomb (U+034F), gravecomb (U+0300), hahabove-ar (U+06E1), hamzaabove-ar (U+0654), hamzabelow-ar (U+0655), highwaw-ar (U+08F3), hookabovecomb (U+0309), hundredthousandssigncomb-cy (U+0488), jeemabove-ar (U+06DA), kasra-ar (U+0650), kasraCurly-ar (U+08E6), kasraDotbelow-ar (U+08F6), kasrasmall-ar (U+061A), kasratan-ar (U+064D), kasratanCurly-ar (U+08E9), lamAlefabove-ar (U+06D9), largerounddotbelow-ar (U+08CF), leftarrowheadbelow-ar (U+08F9), lowlinecomb (U+0332), macronbelowcomb (U+0331), madda-ar (U+0653), maddalong-ar (U+06E4), marksidewaysnoonghunna-ar (U+08FF), meemStopabove-ar (U+06E2), meemabove-ar (U+06D8), meembelow-ar (U+06ED), millionssigncomb-cy (U+0489), noonKasraabove-ar (U+08D8), noonKasrabelow-ar (U+08D9), noonabove-ar (U+06E8), noonghunnaabove-ar (U+0658), opendammatan-ar (U+08F1), openfathatan-ar (U+08F0), openkasratan-ar (U+08F2), palatalizationcomb-cy (U+0484), psilipneumatacomb-cy (U+0486), qafLamAlefMaksuraabove-ar (U+06D7), qafabove-ar (U+08D7), qifabove-ar (U+08DE), rehDadabove-ar (U+0613), rehHahabove-ar (U+0612), rhombusStopabove-ar (U+06EB), rhombusStopbelow-ar (U+06EA), rightarrowheadDotabove-ar (U+08FD), rightarrowheadabove-ar (U+08F8), rightarrowheadbelow-ar (U+08FA), sadLamAlefMaksuraabove-ar (U+06D6), sadabove-ar (U+0610), safhaabove-ar (U+08E1), sahabove-ar (U+08CC), saktaabove-ar (U+08DD), seenabove-ar (U+06DC), seenbelow-ar (U+06E3), shadda-ar (U+0651), smallainabove-ar (U+08D6), smallsadabove-ar (U+08D5), sukun-ar (U+0652), sukunoval-ar (U+06E0), sukunround-ar (U+06DF), tahabove-ar (U+0615), takhallusabove-ar (U+0614), threedotsabove-ar (U+06DB), tildebelowcomb (U+0330), tildecomb (U+0303), titlocomb-cy (U+0483), toneloopabove-ar (U+08EC), toneloopbelow-ar (U+08EF), toneonedotabove-ar (U+08EA), toneonedotbelow-ar (U+08ED), tonetwodotsabove-ar (U+08EB), tonetwodotsbelow-ar (U+08EE), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0312 (U+0312), uni0326 (U+0326), uni0327 (U+0327), uni0328 (U+0328), vabove-ar (U+065A), vinvertedabove-ar (U+065B), waqfaabove-ar (U+08DF), wavyhamzabelow-ar (U+065F), wawbelow-ar (U+08D3), yehabove-ar (U+06E7) and zainabove-ar (U+0617) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Ecircumflexhookabove (U+1EC2): L<<668.0,1664.0>--<668.0,1661.0>> -> L<<668.0,1661.0>--<668.0,1624.0>>

	* Elhook-cy (U+0512): L<<455.0,1028.0>--<455.0,764.0>> -> L<<455.0,764.0>--<453.0,733.0>>

	* Elhook-cy (U+0512): L<<455.0,764.0>--<453.0,733.0>> -> L<<453.0,733.0>--<453.0,696.0>>

	* Eltail-cy (U+04C5): L<<455.0,1028.0>--<455.0,764.0>> -> L<<455.0,764.0>--<453.0,733.0>>

	* Eltail-cy (U+04C5): L<<455.0,764.0>--<453.0,733.0>> -> L<<453.0,733.0>--<453.0,696.0>>

	* Emtail-cy (U+04CD): L<<815.0,127.0>--<815.0,1055.0>> -> L<<815.0,1055.0>--<813.0,1108.0>>

	* Kabashkir-cy (U+04A0): L<<471.0,399.0>--<469.0,365.0>> -> L<<469.0,365.0>--<469.0,127.0>>

	* Kabashkir-cy (U+04A0): L<<602.0,612.0>--<487.0,430.0>> -> L<<487.0,430.0>--<471.0,399.0>>

	* Kastroke-cy (U+049E): L<<297.0,942.0>--<297.0,639.0>> -> L<<297.0,639.0>--<299.0,584.0>>

	* Kaverticalstroke-cy (U+049C): L<<498.0,813.0>--<526.0,844.0>> -> L<<526.0,844.0>--<748.0,1124.0>>

	* Uk-cy (U+0478): L<<344.0,1124.0>--<504.0,840.0>> -> L<<504.0,840.0>--<539.0,768.0>>

	* Yusbigiotified-cy (U+046C): L<<350.0,127.0>--<426.0,479.0>> -> L<<426.0,479.0>--<440.0,543.0>>

	* Yuslittle-cy (U+0466): L<<537.0,1108.0>--<492.0,887.0>> -> L<<492.0,887.0>--<412.0,553.0>>

	* Yuslittle-cy (U+0466): L<<582.0,891.0>--<555.0,1014.0>> -> L<<555.0,1014.0>--<537.0,1108.0>>

	* Yuslittle-cy (U+0466): L<<678.0,489.0>--<582.0,891.0>> -> L<<582.0,891.0>--<555.0,1014.0>>

	* Zhedescender-cy (U+0496): L<<479.0,127.0>--<479.0,365.0>> -> L<<479.0,365.0>--<477.0,399.0>>

	* Zhedescender-cy (U+0496): L<<598.0,401.0>--<596.0,365.0>> -> L<<596.0,365.0>--<596.0,127.0>>

	* Zhedescender-cy (U+0496): L<<700.0,598.0>--<610.0,430.0>> -> L<<610.0,430.0>--<598.0,401.0>>

	* angleright (U+232A): L<<313.0,1348.0>--<487.0,1079.0>> -> L<<487.0,1079.0>--<690.0,768.0>>

	* angleright (U+232A): L<<741.0,563.0>--<371.0,-6.0>> -> L<<371.0,-6.0>--<303.0,-111.0>>

	* annisfabove-ar (U+08DC): L<<337.0,1093.0>--<346.0,1093.0>> -> L<<346.0,1093.0>--<346.0,1093.0>>

	* annisfabove-ar (U+08DC): L<<346.0,1093.0>--<346.0,1093.0>> -> L<<346.0,1093.0>--<348.0,1093.0>>

	* annisfabove-ar (U+08DC): L<<346.0,1093.0>--<348.0,1093.0>> -> L<<348.0,1093.0>--<367.0,1093.0>>

	* annisfabove-ar (U+08DC): L<<650.0,1093.0>--<698.0,1093.0>> -> L<<698.0,1093.0>--<698.0,1093.0>>

	* arrubabove-ar (U+08D4): L<<289.0,1092.0>--<354.0,1092.0>> -> L<<354.0,1092.0>--<354.0,1092.0>>

	* arrubabove-ar (U+08D4): L<<354.0,1092.0>--<354.0,1092.0>> -> L<<354.0,1092.0>--<455.0,1092.0>>

	* arrubabove-ar (U+08D4): L<<791.0,1092.0>--<805.0,1092.0>> -> L<<805.0,1092.0>--<805.0,1092.0>>

	* arrubabove-ar (U+08D4): L<<805.0,1092.0>--<805.0,1092.0>> -> L<<805.0,1092.0>--<834.0,1092.0>>

	* assajdaabove-ar (U+08DB): L<<874.0,1063.0>--<875.0,1063.0>> -> L<<875.0,1063.0>--<875.0,1063.0>>

	* assajdaabove-ar (U+08DB): L<<875.0,1063.0>--<875.0,1063.0>> -> L<<875.0,1063.0>--<883.0,1063.0>>

	* asterisk-ar (U+066D): L<<469.0,471.0>--<479.0,831.0>> -> L<<479.0,831.0>--<479.0,842.0>>

	* commercialMinusSign (U+2052): L<<156.0,162.0>--<229.0,297.0>> -> L<<229.0,297.0>--<688.0,1145.0>>

	* commercialMinusSign (U+2052): L<<229.0,297.0>--<688.0,1145.0>> -> L<<688.0,1145.0>--<799.0,1348.0>>

	* ghemiddlehook-cy (U+0495): L<<428.0,547.0>--<545.0,547.0>> -> L<<545.0,547.0>--<625.0,545.0>>

	* gnaborretni (U+2E18): L<<428.0,-338.0>--<432.0,-203.0>> -> L<<432.0,-203.0>--<434.0,-33.0>>

	* gnaborretni (U+2E18): L<<571.0,178.0>--<575.0,-51.0>> -> L<<575.0,-51.0>--<584.0,-340.0>>

	* interrobang (U+203D): L<<471.0,618.0>--<467.0,848.0>> -> L<<467.0,848.0>--<459.0,1137.0>>

	* interrobang (U+203D): L<<614.0,1135.0>--<612.0,999.0>> -> L<<612.0,999.0>--<608.0,829.0>>

	* izhitsa-cy (U+0475): L<<330.0,756.0>--<487.0,225.0>> -> L<<487.0,225.0>--<510.0,143.0>>

	* izhitsadblgrave-cy (U+0477): L<<332.0,756.0>--<492.0,225.0>> -> L<<492.0,225.0>--<512.0,143.0>>

	* psi (U+03C8): L<<471.0,-424.0>--<467.0,-215.0>> -> L<<467.0,-215.0>--<467.0,-6.0>>

	* qifabove-ar (U+08DE): L<<521.0,1093.0>--<530.0,1093.0>> -> L<<530.0,1093.0>--<530.0,1093.0>>

	* qifabove-ar (U+08DE): L<<530.0,1093.0>--<530.0,1093.0>> -> L<<530.0,1093.0>--<532.0,1093.0>>

	* qifabove-ar (U+08DE): L<<530.0,1093.0>--<532.0,1093.0>> -> L<<532.0,1093.0>--<820.0,1093.0>>

	* thousand-cy (U+0482): L<<432.0,227.0>--<518.0,250.0>> -> L<<518.0,250.0>--<614.0,268.0>>

	* yehTail-ar (U+06CD): L<<334.0,619.0>--<334.0,618.0>> -> L<<334.0,618.0>--<334.0,616.0>>

	* yusbig-cy (U+046B): L<<379.0,756.0>--<485.0,621.0>> -> L<<485.0,621.0>--<528.0,563.0>>

	* yusbigiotified-cy (U+046D): L<<346.0,127.0>--<412.0,338.0>> -> L<<412.0,338.0>--<426.0,379.0>>

	* yusbigiotified-cy (U+046D): L<<412.0,338.0>--<426.0,379.0>> -> L<<426.0,379.0>--<446.0,424.0>>

	* zedescender-cy (U+0499): L<<444.0,117.0>--<483.0,117.0>> -> L<<483.0,117.0>--<508.0,115.0>>

	* zhedescender-cy (U+0497): L<<477.0,127.0>--<477.0,266.0>> -> L<<477.0,266.0>--<475.0,293.0>>

	* zhedescender-cy (U+0497): L<<594.0,756.0>--<594.0,539.0>> -> L<<594.0,539.0>--<596.0,492.0>> 

	* zhedescender-cy (U+0497): L<<684.0,418.0>--<610.0,315.0>> -> L<<610.0,315.0>--<598.0,295.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Emtail-cy (U+04CD): B<<276.5,1044.0>-<265.0,1086.0>-<260.0,1108.0>>/L<<260.0,1108.0>--<260.0,127.0>> = 12.80426606528674

	* Emtail-cy (U+04CD): L<<815.0,1055.0>--<813.0,1108.0>>/B<<813.0,1108.0>-<810.0,1087.0>-<794.0,1032.0>> = 10.291181842382318

	* Iishorttail-cy (U+048A): L<<283.0,1124.0>--<283.0,270.0>>/B<<283.0,270.0>-<294.0,329.0>-<412.5,529.5>> = 10.561010691196365

	* Iishorttail-cy (U+048A): L<<788.0,127.0>--<788.0,981.0>>/B<<788.0,981.0>-<783.0,949.0>-<746.0,878.0>> = 8.880659150520234

	* Izhitsa-cy (U+0474): B<<459.0,288.5>-<476.0,196.0>-<481.0,143.0>>/B<<481.0,143.0>-<483.0,187.0>-<501.0,286.0>> = 7.991873962473095

	* Izhitsadblgrave-cy (U+0476): B<<459.0,286.5>-<476.0,195.0>-<481.0,143.0>>/B<<481.0,143.0>-<483.0,180.0>-<497.5,263.5>> = 8.586382616044505

	* Mu (U+039C): L<<815.0,125.0>--<815.0,1102.0>>/B<<815.0,1102.0>-<808.0,1069.0>-<785.5,996.0>> = 11.976132444203333

	* Upsilondasia (U+1F59): B<<629.0,1209.0>-<672.0,1144.0>-<688.0,983.0>>/B<<688.0,983.0>-<702.0,1134.0>-<743.0,1204.0>> = 10.972403989765944

	* Upsilondasiaoxia (U+1F5D): B<<659.5,1209.0>-<702.0,1144.0>-<719.0,983.0>>/B<<719.0,983.0>-<733.0,1134.0>-<774.0,1204.0>> = 11.324578400118025

	* Upsilondasiaperispomeni (U+1F5F): B<<649.5,1209.0>-<692.0,1144.0>-<709.0,983.0>>/B<<709.0,983.0>-<723.0,1134.0>-<763.5,1204.0>> = 11.324578400118025

	* Upsilondasiavaria (U+1F5B): B<<659.5,1209.0>-<702.0,1144.0>-<719.0,983.0>>/B<<719.0,983.0>-<733.0,1134.0>-<774.0,1204.0>> = 11.324578400118025

	* Upsilonoxia (U+1FEB): B<<604.0,1209.0>-<651.0,1144.0>-<670.0,983.0>>/B<<670.0,983.0>-<685.0,1134.0>-<731.0,1204.0>> = 12.40350607454098

	* Upsilontonos (U+038E): B<<604.0,1209.0>-<651.0,1144.0>-<670.0,983.0>>/B<<670.0,983.0>-<685.0,1134.0>-<731.0,1204.0>> = 12.40350607454098

	* Upsilonvaria (U+1FEA): B<<618.0,1209.0>-<665.0,1144.0>-<684.0,983.0>>/B<<684.0,983.0>-<700.0,1134.0>-<745.5,1204.0>> = 12.778990595616301

	* Yuslittle-cy (U+0466): L<<662.0,553.0>--<678.0,489.0>>/L<<678.0,489.0>--<582.0,891.0>> = 0.6052145972453564

	* Yuslittleiotified-cy (U+0468): B<<703.5,960.0>-<696.0,1042.0>-<696.0,1108.0>>/B<<696.0,1108.0>-<690.0,960.0>-<673.0,824.0>> = 2.3215305898326966

	* annisfabove-ar (U+08DC): L<<825.0,1044.0>--<825.0,1044.0>>/B<<825.0,1044.0>-<792.0,1045.0>-<778.0,1059.0>> = 1.735704588928346

	* assajdaabove-ar (U+08DB): L<<872.0,1028.0>--<872.0,1028.0>>/B<<872.0,1028.0>-<853.0,1029.0>-<841.5,1038.5>> = 3.012787504183286

	* narrownbspace (U+202F): L<<340.0,698.0>--<338.0,698.0>>/B<<338.0,698.0>-<356.0,694.0>-<376.5,686.5>> = 12.528807709151492

	* saktaabove-ar (U+08DD): L<<459.0,1047.0>--<459.0,1047.0>>/B<<459.0,1047.0>-<429.0,1049.0>-<415.0,1062.5>> = 3.8140748342903783

	* yehKashmiri-ar (U+0620): B<<587.0,21.0>-<600.0,21.0>-<614.0,20.0>>/B<<614.0,20.0>-<570.0,14.0>-<520.0,12.0>> = 11.850782798400157

	* yehKashmiri-ar (U+0620): B<<789.0,-81.0>-<726.0,9.0>-<614.0,20.0>>/B<<614.0,20.0>-<725.0,35.0>-<786.0,76.0>> = 13.30532616846234 

	* zerowidthnonjoiner (U+200C): B<<364.0,360.5>-<350.0,367.0>-<344.0,395.0>>/L<<344.0,395.0>--<344.0,393.0>> = 12.094757077012089 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Stigma (U+03DA): L<<471.0,4.0>--<469.0,342.0>>

	* Stigma (U+03DB): L<<471.0,4.0>--<469.0,342.0>>

	* baht (U+0E3F): L<<459.0,125.0>--<457.0,588.0>>

	* baht (U+0E3F): L<<586.0,588.0>--<584.0,125.0>>

	* etadasia (U+1F21): L<<866.0,-424.0>--<864.0,516.0>>

	* etadasiaoxia (U+1F25): L<<866.0,-424.0>--<864.0,516.0>>

	* etadasiaoxiaypogegrammeni (U+1F95): L<<866.0,-424.0>--<864.0,516.0>>

	* etadasiaperispomeniypogegrammeni (U+1F97): L<<866.0,-424.0>--<864.0,516.0>>

	* etadasiavaria (U+1F23): L<<866.0,-424.0>--<864.0,516.0>>

	* etadasiavariaypogegrammeni (U+1F93): L<<866.0,-424.0>--<864.0,516.0>>

	* etadasiaypogegrammeni (U+1F91): L<<866.0,-424.0>--<864.0,516.0>>

	* etaoxia (U+1F75): L<<866.0,-424.0>--<864.0,516.0>>

	* etaoxiaypogegrammeni (U+1FC4): L<<866.0,-424.0>--<864.0,516.0>>

	* etaperispomeni (U+1FC6): L<<866.0,-424.0>--<864.0,516.0>>

	* etaperispomeniypogegrammeni (U+1FC7): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsilioxia (U+1F24): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsilioxiaypogegrammeni (U+1F94): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsiliperispomeni (U+1F26): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsiliperispomeniypogegrammeni (U+1F96): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsilivaria (U+1F22): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsilivariaypogegrammeni (U+1F92): L<<866.0,-424.0>--<864.0,516.0>>

	* etapsiliypogegrammeni (U+1F90): L<<866.0,-424.0>--<864.0,516.0>>

	* etavaria (U+1F74): L<<866.0,-424.0>--<864.0,516.0>>

	* etavariaypogegrammeni (U+1FC2): L<<866.0,-424.0>--<864.0,516.0>>

	* etaypogegrammeni (U+1FC3): L<<866.0,-424.0>--<864.0,516.0>>

	* koppa (U+03DF): L<<817.0,-121.0>--<821.0,438.0>>

	* phi (U+03C6): L<<471.0,-424.0>--<469.0,-6.0>>

	* waqfaabove-ar (U+08DF): L<<623.0,1094.0>--<768.0,1093.0>> 

	* waqfaabove-ar (U+08DF): L<<790.0,1046.0>--<643.0,1047.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[26] CourierBadi-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "Copyright (c) 2023 Joop Kiefte (https://github.com/LaPingvino/courier-badi)

Derived from Courier Prime with original copyright:
Copyright (c) 2015
Quote-Unquote Apps (https://quoteunquoteapps.com)
with Reserved Font Name Courier Prime Source.

This Font Software is licensed under the SIL Open Font License
Version 1.1. This license is copied below
and is also available with a FAQ at: https://scripts.sil.org/OFL


-----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
-----------------------------------------------------------

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide development of collaborative font projects
to support the font creation efforts of academic and linguistic communities
and to provide a free and open framework in which fonts may be shared and improved in partnership with others.

The OFL allows the licensed fonts to be used
studied
modified and redistributed freely as long as they are not sold by themselves. The fonts
including any derivative works
can be bundled
embedded
redistributed and/or sold with any software provided that any reserved names are not used by derivative works. The fonts and derivatives
however
cannot be released under any other type of license. The requirement for fonts to remain under this license does not apply to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright Holder(s) under this license and clearly marked as such. This may include source files
build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the copyright statement(s).

"Original Version" refers to the collection of Font Software components as distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to
deleting
or substituting -- in part or in whole -- any of the components of the Original Version
by changing formats or by porting the Font Software to a new environment.

"Author" refers to any designer
engineer
programmer
technical writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted
free of charge
to any person obtaining a copy of the Font Software
to use
study
copy
merge
embed
modify
redistribute
and sell modified and unmodified copies of the Font Software
subject to the following conditions:

1) Neither the Font Software nor any of its individual components
in Original or Modified Versions
may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled
redistributed and/or sold with any software
provided that each copy contains the above copyright notice and this license. These can be included either as stand-alone text files
human-readable headers or in the appropriate machine-readable metadata fields within text or binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font Name(s) unless explicit written permission is granted by the corresponding Copyright Holder. This restriction only applies to the primary font name as presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font Software shall not be used to promote
endorse or advertise any Modified Version
except to acknowledge the contribution(s) of the Copyright Holder(s) and the Author(s) or with their explicit written permission.

5) The Font Software
modified or unmodified
in part or in whole
must be distributed entirely under this license
and must not be distributed under any other license. The requirement for fonts to remain under this license does not apply to any document created using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS"
WITHOUT WARRANTY OF ANY KIND
EXPRESS OR IMPLIED
INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF COPYRIGHT
PATENT
TRADEMARK
OR OTHER RIGHT. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM
DAMAGES OR OTHER LIABILITY
INCLUDING ANY GENERAL
SPECIAL
INDIRECT
INCIDENTAL
OR CONSEQUENTIAL DAMAGES
WHETHER IN AN ACTION OF CONTRACT
TORT OR OTHERWISE
ARISING FROM
OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM OTHER DEALINGS IN THE FONT SOFTWARE." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2023 Joop Kiefte, Copyright (c) 2015 Quote-Unquote Apps." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/CourierBadi-Regular.ttf', 'fonts/ttf/CourierBadi-Italic.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2087, but got 1827 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1364, but got 838 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (1638) and hhea ascent (1827) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Whitespace glyphs have ink? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_ink">com.google.fonts/check/whitespace_ink</a>)</summary><div>


* 🔥 **FAIL** Glyph "narrownbspace" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
* 🔥 **FAIL** Glyph "zeroWidthNoBreakSpace" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
</div></details><details><summary>🔥 <b>FAIL:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* 🔥 **FAIL** The following glyph names do not comply with naming conventions: Abreve-cy, Adieresis-cy, Aie-cy, Cheabkhasian-cy, Chedescender-cy, Chedescenderabkhasian-cy, Chedieresis-cy, Chekhakassian-cy, Cheverticalstroke-cy, Dzeabkhasian-cy, Edieresis-cy, Eiotified-cy, Elhook-cy, Eltail-cy, Emtail-cy, Enghe-cy, Enhook-cy, Entail-cy, Ertick-cy, Esdescender-cy, Fita-cy, Gedescender-cy, Ghemiddlehook-cy, Haabkhasian-cy, Hadescender-cy, Hahook-cy, Hastroke-cy, Idieresis-cy, Iebreve-cy, Iegrave-cy, Iishorttail-cy, Imacron-cy, Izhitsa-cy, Izhitsadblgrave-cy, Kabashkir-cy, Kahook-cy, Kastroke-cy, Kaverticalstroke-cy, Koppa-cy, Ksi-cy, Obarreddieresis-cy, Odieresis-cy, Omega-cy, Palochka-cy, Pemiddlehook-cy, Psi-cy, Schwadieresis-cy, Semisoftsign-cy, Tedescender-cy, Tetse-cy, Udieresis-cy, Uhungarumlaut-cy, Uk-cy, Umacron-cy, Yat-cy, Yerudieresis-cy, Yusbig-cy, Yusbigiotified-cy, Yuslittle-cy, Yuslittleiotified-cy, Zedescender-cy, Zedieresis-cy, Zhebreve-cy, Zhedescender-cy, Zhedieresis-cy, abreve-cy, adieresis-cy, ae-ar, ae-ar.fina, afghani-ar, aie-cy, ain-ar, ain-ar.fina, ain-ar.init, ain-ar.medi, ainThreedots-ar, ainThreedots-ar.fina, ainThreedots-ar.init, ainThreedots-ar.medi, ainThreedotsbelow-ar, ainThreedotsbelow-ar.fina, ainThreedotsbelow-ar.init, ainThreedotsbelow-ar.medi, ainThreedotsdownabove-ar, ainThreedotsdownabove-ar.fina, ainThreedotsdownabove-ar.init, ainThreedotsdownabove-ar.medi, ainTwodotshorizontalabove-ar, ainTwodotshorizontalabove-ar.fina, ainTwodotshorizontalabove-ar.init, ainTwodotshorizontalabove-ar.medi, ainTwodotsverticalabove-ar, ainTwodotsverticalabove-ar.fina, ainTwodotsverticalabove-ar.init, ainTwodotsverticalabove-ar.medi, ainabove-ar, alef-ar, alef-ar.fina, alef-ar.fina.alt, alef-ar.fina.short, alef-ar.fina.shorter, alef-ar.short, alef-ar.shorter, alefHamzaabove-ar, alefHamzaabove-ar.fina, alefHamzaabove-ar.fina.alt, alefHamzabelow-ar, alefHamzabelow-ar.fina, alefHamzabelow-ar.fina.alt, alefLamYehabove-ar, alefMadda-ar, alefMadda-ar.fina, alefMadda-ar.fina.alt, alefMaksura-ar, alefMaksura-ar.fina, alefMaksura-ar.init, alefMaksura-ar.medi, alefThreeabove-ar, alefThreeabove-ar.fina, alefThreeabove-ar.fina.alt, alefTwoabove-ar, alefTwoabove-ar.fina, alefTwoabove-ar.fina.alt, alefWasla-ar, alefWasla-ar.fina, alefWasla-ar.fina.alt, alefWavyhamzaabove-ar, alefWavyhamzaabove-ar.fina, alefWavyhamzaabove-ar.fina.alt, alefWavyhamzabelow-ar, alefWavyhamzabelow-ar.fina, alefWavyhamzabelow-ar.fina.alt, alefabove-ar, alefbelow-ar, aleflow-ar, allah-ar, allahlong-ar, annisfabove-ar, arrubabove-ar, assajdaabove-ar, asterisk-ar, aththalathaabove-ar, beeh-ar, beeh-ar.fina, beeh-ar.init, beeh-ar.medi, beh-ar, beh-ar.fina, beh-ar.init, beh-ar.medi, behDotless-ar, behDotless-ar.fina, behDotless-ar.hah, behDotless-ar.init, behDotless-ar.medi, behMeemabove-ar, behMeemabove-ar.fina, behMeemabove-ar.init, behMeemabove-ar.medi, behThreedotshorizontalbelow-ar, behThreedotshorizontalbelow-ar.fina, behThreedotshorizontalbelow-ar.init, behThreedotshorizontalbelow-ar.medi, behThreedotsupabove-ar, behThreedotsupabove-ar.fina, behThreedotsupabove-ar.init, behThreedotsupabove-ar.medi, behThreedotsupbelow-ar, behThreedotsupbelow-ar.fina, behThreedotsupbelow-ar.init, behThreedotsupbelow-ar.medi, behTwodotsbelowDotabove-ar, behTwodotsbelowDotabove-ar.fina, behTwodotsbelowDotabove-ar.init, behTwodotsbelowDotabove-ar.medi, behVabove-ar, behVabove-ar.fina, behVabove-ar.init, behVabove-ar.medi, behVbelow-ar, behVbelow-ar.fina, behVbelow-ar.init, behVbelow-ar.medi, behVinvertedbelow-ar, behVinvertedbelow-ar.fina, behVinvertedbelow-ar.init, behVinvertedbelow-ar.medi, beh_meem-ar.init, beheh-ar, beheh-ar.fina, beheh-ar.init, beheh-ar.medi, behhamzaabove-ar, behhamzaabove-ar.fina, behhamzaabove-ar.init, behhamzaabove-ar.medi, bismillah-ar, cheabkhasian-cy, chedescender-cy, chedescenderabkhasian-cy, chedieresis-cy, chekhakassian-cy, cheverticalstroke-cy, comma-ar, cuberoot-ar, dad-ar, dad-ar.fina, dad-ar.init, dad-ar.medi, dadDotbelow-ar, dadDotbelow-ar.fina, dadDotbelow-ar.init, dadDotbelow-ar.medi, dahal-ar, dahal-ar.fina, dal-ar, dal-ar.fina, dalDotbelow-ar, dalDotbelow-ar.fina, dalDotbelowTah-ar, dalDotbelowTah-ar.fina, dalFourdots-ar, dalFourdots-ar.fina, dalRing-ar, dalRing-ar.fina, dalThreedotsbelow-ar, dalThreedotsbelow-ar.fina, dalThreedotsdown-ar, dalThreedotsdown-ar.fina, dalTwodotsverticalbelowTah-ar, dalTwodotsverticalbelowTah-ar.fina, dalVinvertedabove-ar, dalVinvertedabove-ar.fina, dalVinvertedbelow-ar, dalVinvertedbelow-ar.fina, damma-ar, damma-ar.medi, dammaCurly-ar, dammaDot-ar, dammainverted-ar, dammareversed-ar, dammasmall-ar, dammatan-ar, dammatanCurly-ar, dammaturnedbelow-ar, dasiapneumatacomb-cy, dateseparator-ar, ddahal-ar, ddahal-ar.fina, ddal-ar, ddal-ar.fina, decimalseparator-ar, disputedendofayah-ar, dotStopabove-ar, dotaboveSymbol-ar, dotbelowSymbol-ar, dotvowelbelow-ar, doublerightarrowheadDotabove-ar, doublerightarrowheadabove-ar, doublestroke-ar, doubleverticalbarbelowSymbol-ar, dul-ar, dul-ar.fina, dyeh-ar, dyeh-ar.fina, dyeh-ar.init, dyeh-ar.medi, dzeabkhasian-cy, e-ar, e-ar.fina, e-ar.init, e-ar.medi, edieresis-cy, eight-ar, eiotified-cy, elhook-cy, eltail-cy, emtail-cy, endofayah-ar, enghe-cy, enhook-cy, entail-cy, ertick-cy, esdescender-cy, fatha-ar, fatha-ar.medi, fathaCurly-ar, fathaDotabove-ar, fathaHorizont-ar, fathaRing-ar, fathasmall-ar, fathatan-ar, fathatan-ar.medi, fathatanCurly-ar, fathatwodots-ar, feh-ar, feh-ar.fina, feh-ar.init, feh-ar.medi, fehAfrican-ar, fehAfrican-ar.fina, fehAfrican-ar.init, fehAfrican-ar.medi, fehDotbelow-ar, fehDotbelow-ar.fina, fehDotbelow-ar.init, fehDotbelow-ar.medi, fehDotbelowThreedotsabove-ar, fehDotbelowThreedotsabove-ar.fina, fehDotbelowThreedotsabove-ar.init, fehDotbelowThreedotsabove-ar.medi, fehDotless-ar, fehDotless-ar.fina, fehDotless-ar.init, fehDotless-ar.medi, fehDotmovedbelow-ar, fehDotmovedbelow-ar.fina, fehDotmovedbelow-ar.init, fehDotmovedbelow-ar.medi, fehThreedotsbelow-ar, fehThreedotsbelow-ar.fina, fehThreedotsbelow-ar.init, fehThreedotsbelow-ar.medi, fehThreedotsupbelow-ar, fehThreedotsupbelow-ar.fina, fehThreedotsupbelow-ar.init, fehThreedotsupbelow-ar.medi, fehTwodotsbelow-ar, fehTwodotsbelow-ar.fina, fehTwodotsbelow-ar.init, fehTwodotsbelow-ar.medi, fita-cy, five-ar, five-persian, footnotemarker-ar, footnotemarkerabove-ar, four-ar, four-persian, four-persian.urdu, fourabove-ar, fourbelow-ar, fourdotsaboveSymbol-ar, fourdotsbelowSymbol-ar, fourthroot-ar, fullstop-ar, gaf-ar, gaf-ar.fina, gaf-ar.init, gaf-ar.medi, gafInvertedstroke-ar, gafInvertedstroke-ar.fina, gafInvertedstroke-ar.init, gafInvertedstroke-ar.medi, gafRing-ar, gafRing-ar.fina, gafRing-ar.init, gafRing-ar.medi, gafThreedots-ar, gafThreedots-ar.fina, gafThreedots-ar.init, gafThreedots-ar.medi, gafTwodotsbelow-ar, gafTwodotsbelow-ar.fina, gafTwodotsbelow-ar.init, gafTwodotsbelow-ar.medi, gafsarkashabove-ar, gedescender-cy, ghain-ar, ghain-ar.fina, ghain-ar.init, ghain-ar.medi, ghainDotbelow-ar, ghainDotbelow-ar.fina, ghainDotbelow-ar.init, ghainDotbelow-ar.medi, ghainThreedotsabove-ar, ghainThreedotsabove-ar.fina, ghainThreedotsabove-ar.init, ghainThreedotsabove-ar.medi, ghemiddlehook-cy, gueh-ar, gueh-ar.fina, gueh-ar.init, gueh-ar.medi, haabkhasian-cy, hadescender-cy, hah-ar, hah-ar.fina, hah-ar.init, hah-ar.medi, hahFourbelow-ar, hahFourbelow-ar.fina, hahFourbelow-ar.init, hahFourbelow-ar.medi, hahHamzaabove-ar, hahHamzaabove-ar.fina, hahHamzaabove-ar.init, hahHamzaabove-ar.medi, hahTahTwodotshorizontalbelow-ar, hahTahTwodotshorizontalbelow-ar.fina, hahTahTwodotshorizontalbelow-ar.init, hahTahTwodotshorizontalbelow-ar.medi, hahTahabove-ar, hahTahabove-ar.fina, hahTahabove-ar.init, hahTahabove-ar.medi, hahTahbelow-ar, hahTahbelow-ar.fina, hahTahbelow-ar.init, hahTahbelow-ar.medi, hahThreedotsabove-ar, hahThreedotsabove-ar.fina, hahThreedotsabove-ar.init, hahThreedotsabove-ar.medi, hahThreedotsupbelow-ar, hahThreedotsupbelow-ar.fina, hahThreedotsupbelow-ar.init, hahThreedotsupbelow-ar.medi, hahTwodotshorizontalabove-ar, hahTwodotshorizontalabove-ar.fina, hahTwodotshorizontalabove-ar.init, hahTwodotshorizontalabove-ar.medi, hahTwodotsverticalabove-ar, hahTwodotsverticalabove-ar.fina, hahTwodotsverticalabove-ar.init, hahTwodotsverticalabove-ar.medi, hahabove-ar, hahook-cy, hamza-ar, hamzaabove-ar, hamzabelow-ar, hastroke-cy, heh-ar, heh-ar.fina, heh-ar.init, heh-ar.medi, hehDoachashmee-ar, hehDoachashmee-ar.fina, hehDoachashmee-ar.init, hehDoachashmee-ar.init.comp, hehDoachashmee-ar.medi, hehHamzaabove-ar, hehHamzaabove-ar.fina, hehVinvertedabove-ar, hehVinvertedabove-ar.fina, hehVinvertedabove-ar.init, hehVinvertedabove-ar.medi, hehgoal-ar, hehgoal-ar.fina, hehgoal-ar.init, hehgoal-ar.medi, hehgoalHamzaabove-ar, hehgoalHamzaabove-ar.fina, highhamza-ar, highhamza-ar.narrow, highhamzaAlef-ar, highhamzaWaw-ar, highhamzaYeh-ar, highhamzaYeh-ar.init, highwaw-ar, hizb-ar, hundredthousandssigncomb-cy, idieresis-cy, iebreve-cy, iegrave-cy, iishorttail-cy, imacron-cy, izhitsa-cy, izhitsadblgrave-cy, jallajalalouhou-ar, jeem-ar, jeem-ar.fina, jeem-ar.init, jeem-ar.medi, jeemThreedotsabove-ar, jeemThreedotsabove-ar.fina, jeemThreedotsabove-ar.init, jeemThreedotsabove-ar.medi, jeemThreedotsbelow-ar, jeemThreedotsbelow-ar.fina, jeemThreedotsbelow-ar.init, jeemThreedotsbelow-ar.medi, jeemTwodotsabove-ar, jeemTwodotsabove-ar.fina, jeemTwodotsabove-ar.init, jeemTwodotsabove-ar.medi, jeemabove-ar, jeh-ar, jeh-ar.fina, kabashkir-cy, kaf-ar, kaf-ar.fina, kaf-ar.init, kaf-ar.medi, kafDotabove-ar, kafDotabove-ar.fina, kafDotabove-ar.init, kafDotabove-ar.medi, kafDotbelow-ar, kafDotbelow-ar.fina, kafDotbelow-ar.init, kafDotbelow-ar.medi, kafDotless-ar, kafDotless-ar.fina, kafRing-ar, kafRing-ar.fina, kafRing-ar.init, kafRing-ar.medi, kafThreedotsbelow-ar, kafThreedotsbelow-ar.fina, kafThreedotsbelow-ar.init, kafThreedotsbelow-ar.medi, kafTwodotshorizontalabove-ar, kafTwodotshorizontalabove-ar.fina, kafTwodotshorizontalabove-ar.init, kafTwodotshorizontalabove-ar.medi, kafswash-ar, kafswash-ar.fina, kafswash-ar.init, kafswash-ar.medi, kahook-cy, kashida-ar, kashidaFina-ar, kasra-ar, kasra-ar.medi, kasraCurly-ar, kasraDotbelow-ar, kasrasmall-ar, kasratan-ar, kasratanCurly-ar, kastroke-cy, kaverticalstroke-cy, keheh-ar, keheh-ar.fina, keheh-ar.init, keheh-ar.medi, kehehDotabove-ar, kehehDotabove-ar.fina, kehehDotabove-ar.init, kehehDotabove-ar.medi, kehehThreedotsabove-ar, kehehThreedotsabove-ar.fina, kehehThreedotsabove-ar.init, kehehThreedotsabove-ar.medi, kehehThreedotsbelow-ar, kehehThreedotsbelow-ar.fina, kehehThreedotsbelow-ar.init, kehehThreedotsbelow-ar.medi, kehehThreedotsupbelow-ar, kehehThreedotsupbelow-ar.fina, kehehThreedotsupbelow-ar.init, kehehThreedotsupbelow-ar.medi, kehehTwodotshorizontalabove-ar, kehehTwodotshorizontalabove-ar.fina, kehehTwodotshorizontalabove-ar.init, kehehTwodotshorizontalabove-ar.medi, kehehVabove-ar, kehehVabove-ar.fina, kehehVabove-ar.init, kehehVabove-ar.medi, khah-ar, khah-ar.fina, khah-ar.init, khah-ar.medi, kirghizoe-ar, kirghizoe-ar.fina, kirghizyu-ar, kirghizyu-ar.fina, koppa-cy, ksi-cy, lam-ar, lam-ar.fina, lam-ar.init, lam-ar.medi, lam-ar.medi.short, lamAlefabove-ar, lamBar-ar, lamBar-ar.fina, lamBar-ar.init, lamBar-ar.medi, lamDotabove-ar, lamDotabove-ar.fina, lamDotabove-ar.init, lamDotabove-ar.medi, lamDoublebar-ar, lamDoublebar-ar.fina, lamDoublebar-ar.init, lamDoublebar-ar.medi, lamTahabove-ar, lamTahabove-ar.fina, lamTahabove-ar.init, lamTahabove-ar.medi, lamThreedotsabove-ar, lamThreedotsabove-ar.fina, lamThreedotsabove-ar.init, lamThreedotsabove-ar.medi, lamThreedotsbelow-ar, lamThreedotsbelow-ar.fina, lamThreedotsbelow-ar.init, lamThreedotsbelow-ar.medi, lamVabove-ar, lamVabove-ar.fina, lamVabove-ar.init, lamVabove-ar.medi, lam_alef-ar, lam_alef-ar.fina, lam_alefHamzaabove-ar, lam_alefHamzaabove-ar.fina, lam_alefHamzabelow-ar, lam_alefHamzabelow-ar.fina, lam_alefMadda-ar, lam_alefMadda-ar.fina, lam_hah-ar.init, lam_jeem-ar.init, lam_khah-ar.init, lam_meem-ar.init, lam_meem_hah-ar.init, largerounddotbelow-ar, leftarrowheadabove-ar, leftarrowheadbelow-ar, lowernumeral-greek, madda-ar, maddalong-ar, mark-ar, marksidewaysnoonghunna-ar, meem-ar, meem-ar.fina, meem-ar.init, meem-ar.medi, meemDotabove-ar, meemDotabove-ar.fina, meemDotabove-ar.init, meemDotabove-ar.medi, meemDotbelow-ar, meemDotbelow-ar.fina, meemDotbelow-ar.init, meemDotbelow-ar.medi, meemStopabove-ar, meemThreedotsabove-ar, meemThreedotsabove-ar.fina, meemThreedotsabove-ar.init, meemThreedotsabove-ar.medi, meemabove-ar, meembelow-ar, millionssigncomb-cy, miniKeheh-ar, misraComma-ar, mohammad-ar, ng-ar, ng-ar.fina, ng-ar.init, ng-ar.medi, ngoeh-ar, ngoeh-ar.fina, ngoeh-ar.init, ngoeh-ar.medi, nine-ar, noon-ar, noon-ar.fina, noon-ar.init, noon-ar.medi, noonAfrican-ar, noonAfrican-ar.fina, noonAfrican-ar.init, noonAfrican-ar.medi, noonDotbelow-ar, noonDotbelow-ar.fina, noonDotbelow-ar.init, noonDotbelow-ar.medi, noonKasraabove-ar, noonKasrabelow-ar, noonRing-ar, noonRing-ar.fina, noonRing-ar.init, noonRing-ar.medi, noonTahabove-ar, noonTahabove-ar.fina, noonTahabove-ar.init, noonTahabove-ar.medi, noonThreedotsabove-ar, noonThreedotsabove-ar.fina, noonThreedotsabove-ar.init, noonThreedotsabove-ar.medi, noonTwodotsbelow-ar, noonTwodotsbelow-ar.fina, noonTwodotsbelow-ar.init, noonTwodotsbelow-ar.medi, noonVabove-ar, noonVabove-ar.fina, noonVabove-ar.init, noonVabove-ar.medi, noonabove-ar, noonghunna-ar, noonghunna-ar.fina, noonghunna-ar.init, noonghunna-ar.medi, noonghunnaabove-ar, note-musical, number-ar, numbermark-ar, numeral-greek, nyeh-ar, nyeh-ar.fina, nyeh-ar.init, nyeh-ar.medi, obarreddieresis-cy, odieresis-cy, oe-ar, oe-ar.fina, omega-cy, one-ar, opendammatan-ar, openfathatan-ar, openkasratan-ar, pagenumber-ar, palatalizationcomb-cy, parenleft-ar, parenright-ar, peh-ar, peh-ar.fina, peh-ar.init, peh-ar.medi, pehMeemabove-ar, pehMeemabove-ar.fina, pehMeemabove-ar.init, pehMeemabove-ar.medi, pehVabove-ar, pehVabove-ar.fina, pehVabove-ar.init, pehVabove-ar.medi, peheh-ar, peheh-ar.fina, peheh-ar.init, peheh-ar.medi, pemiddlehook-cy, percent-ar, pertenthousand-ar, perthousand-ar, psi-cy, psilipneumatacomb-cy, qaf-ar, qaf-ar.fina, qaf-ar.init, qaf-ar.medi, qafAfrican-ar, qafAfrican-ar.fina, qafAfrican-ar.init, qafAfrican-ar.medi, qafDotabove-ar, qafDotabove-ar.fina, qafDotabove-ar.init, qafDotabove-ar.medi, qafDotbelow-ar, qafDotbelow-ar.fina, qafDotbelow-ar.init, qafDotbelow-ar.medi, qafDotless-ar, qafDotless-ar.fina, qafDotless-ar.init, qafDotless-ar.medi, qafLamAlefMaksuraabove-ar, qafThreedotsabove-ar, qafThreedotsabove-ar.fina, qafThreedotsabove-ar.init, qafThreedotsabove-ar.medi, qafThreedotsaboveAfrican-ar, qafThreedotsaboveAfrican-ar.fina, qafThreedotsaboveAfrican-ar.init, qafThreedotsaboveAfrican-ar.medi, qafabove-ar, qifabove-ar, question-ar, ray-ar, reh-ar, reh-ar.fina, rehDadabove-ar, rehDotbelow-ar, rehDotbelow-ar.fina, rehDotbelowdotabove-ar, rehDotbelowdotabove-ar.fina, rehFourdots-ar, rehFourdots-ar.fina, rehHahabove-ar, rehHamzaabove-ar, rehHamzaabove-ar.fina, rehLoop-ar, rehLoop-ar.fina, rehNoonabove-ar, rehNoonabove-ar.fina, rehRing-ar, rehRing-ar.fina, rehStroke-ar, rehStroke-ar.fina, rehTwodots-ar, rehTwodots-ar.fina, rehTwodotshorizontalaboveTahabove-ar, rehTwodotshorizontalaboveTahabove-ar.fina, rehTwodotsverticalabove-ar, rehTwodotsverticalabove-ar.fina, rehVbelow-ar, rehVbelow-ar.fina, rehVinvertedabove-ar, rehVinvertedabove-ar.fina, rehabove-ar, rehv-ar, rehv-ar.fina, rhombusStopabove-ar, rhombusStopbelow-ar, rightarrowheadDotabove-ar, rightarrowheadabove-ar, rightarrowheadbelow-ar, ringSymbol-ar, rnoon-ar, rnoon-ar.fina, rnoon-ar.init, rnoon-ar.medi, rreh-ar, rreh-ar.fina, sad-ar, sad-ar.fina, sad-ar.init, sad-ar.medi, sadLamAlefMaksuraabove-ar, sadThreedots-ar, sadThreedots-ar.fina, sadThreedots-ar.init, sadThreedots-ar.medi, sadThreedotsbelow-ar, sadThreedotsbelow-ar.fina, sadThreedotsbelow-ar.init, sadThreedotsbelow-ar.medi, sadTwodotsbelow-ar, sadTwodotsbelow-ar.fina, sadTwodotsbelow-ar.init, sadTwodotsbelow-ar.medi, sadabove-ar, safhaabove-ar, sahabove-ar, sajdah-ar, saktaabove-ar, samvat-ar, schwadieresis-cy, seen-ar, seen-ar.fina, seen-ar.init, seen-ar.medi, seenDotbelowDotabove-ar, seenDotbelowDotabove-ar.fina, seenDotbelowDotabove-ar.init, seenDotbelowDotabove-ar.medi, seenFourabove-ar, seenFourabove-ar.fina, seenFourabove-ar.init, seenFourabove-ar.medi, seenFourdotsabove-ar, seenFourdotsabove-ar.fina, seenFourdotsabove-ar.init, seenFourdotsabove-ar.medi, seenTahTwodotshorizontalabove-ar, seenTahTwodotshorizontalabove-ar.fina, seenTahTwodotshorizontalabove-ar.init, seenTahTwodotshorizontalabove-ar.medi, seenThreedotsbelow-ar, seenThreedotsbelow-ar.fina, seenThreedotsbelow-ar.init, seenThreedotsbelow-ar.medi, seenTwodotsverticalabove-ar, seenTwodotsverticalabove-ar.fina, seenTwodotsverticalabove-ar.init, seenTwodotsverticalabove-ar.medi, seenVinvertedabove-ar, seenVinvertedabove-ar.fina, seenVinvertedabove-ar.init, seenVinvertedabove-ar.medi, seenabove-ar, seenbelow-ar, semicolon-ar, semisoftsign-cy, seven-ar, seven-persian, seven-persian.urdu, shadda-ar, shadda-ar.medi, sheen-ar, sheen-ar.fina, sheen-ar.init, sheen-ar.medi, sheenDotbelow-ar, sheenDotbelow-ar.fina, sheenDotbelow-ar.init, sheenDotbelow-ar.medi, sheenThreedotsbelow-ar, sheenThreedotsbelow-ar.fina, sheenThreedotsbelow-ar.init, sheenThreedotsbelow-ar.medi, sindhiampersand-ar, sindhipostpositionmen-ar, sindhipostpositionmen-ar.fina, sindhipostpositionmen-ar.init, sindhipostpositionmen-ar.medi, six-ar, six-persian, smallainabove-ar, smallsadabove-ar, stroke-ar, sukun-ar, sukun-ar.medi, sukunoval-ar, sukunround-ar, tah-ar, tah-ar.fina, tah-ar.init, tah-ar.medi, tahThreedots-ar, tahThreedots-ar.fina, tahThreedots-ar.init, tahThreedots-ar.medi, tahTwodotsabove-ar, tahTwodotsabove-ar.fina, tahTwodotsabove-ar.init, tahTwodotsabove-ar.medi, tahabove-ar, tahbelowSymbol-ar, takhallusabove-ar, tcheh-ar, tcheh-ar.fina, tcheh-ar.init, tcheh-ar.medi, tchehDotabove-ar, tchehDotabove-ar.fina, tchehDotabove-ar.init, tchehDotabove-ar.medi, tchehVabove-ar, tchehVabove-ar.fina, tchehVabove-ar.init, tchehVabove-ar.medi, tcheheh-ar, tcheheh-ar.fina, tcheheh-ar.init, tcheheh-ar.medi, tedescender-cy, teh-ar, teh-ar.fina, teh-ar.init, teh-ar.medi, tehMarbuta-ar, tehMarbuta-ar.alt, tehMarbuta-ar.fina, tehMarbutagoal-ar, tehMarbutagoal-ar.fina, tehRing-ar, tehRing-ar.fina, tehRing-ar.init, tehRing-ar.medi, tehTehabove-ar, tehTehabove-ar.fina, tehTehabove-ar.init, tehTehabove-ar.medi, tehThreedotsdown-ar, tehThreedotsdown-ar.fina, tehThreedotsdown-ar.init, tehThreedotsdown-ar.medi, tehThreedotsupbelow-ar, tehThreedotsupbelow-ar.fina, tehThreedotsupbelow-ar.init, tehThreedotsupbelow-ar.medi, tehVabove-ar, tehVabove-ar.fina, tehVabove-ar.init, tehVabove-ar.medi, teh_hah-ar.init, teh_jeem-ar.init, teheh-ar, teheh-ar.fina, teheh-ar.init, teheh-ar.medi, tetse-cy, thal-ar, thal-ar.fina, theh-ar, theh-ar.fina, theh-ar.init, theh-ar.medi, thousand-cy, thousandseparator-ar, three-ar, threeabove-ar, threedots-ar, threedotsabove-ar, threedotsdownaboveSymbol-ar, threedotsdownbelowSymbol-ar, threedotshorizontalbelow-ar, threedotsupaboveSymbol-ar, threedotsupbelowSymbol-ar, titlocomb-cy, toneloopabove-ar, toneloopbelow-ar, toneonedotabove-ar, toneonedotbelow-ar, tonetwodotsabove-ar, tonetwodotsbelow-ar, tteh-ar, tteh-ar.fina, tteh-ar.init, tteh-ar.medi, ttehVabove-ar, ttehVabove-ar.fina, ttehVabove-ar.init, ttehVabove-ar.medi, tteheh-ar, tteheh-ar.fina, tteheh-ar.init, tteheh-ar.medi, two-ar, twoabove-ar, twodotshorizontalaboveSymbol-ar, twodotshorizontalbelowSymbol-ar, twodotsverticalaboveSymbol-ar, twodotsverticalbelowSymbol-ar, u-ar, u-ar.fina, uHamzaabove-ar, udieresis-cy, uhungarumlaut-cy, uk-cy, umacron-cy, vabove-ar, ve-ar, ve-ar.fina, veh-ar, veh-ar.fina, veh-ar.init, veh-ar.medi, verseComma-ar, vinvertedabove-ar, waqfaabove-ar, wasla-ar, wavyhamzabelow-ar, waw-ar, waw-ar.fina, wawDotabove-ar, wawDotabove-ar.fina, wawDotcenter-ar, wawDotcenter-ar.fina, wawHamzaabove-ar, wawHamzaabove-ar.fina, wawSmall-ar, wawStraight-ar, wawStraight-ar.fina, wawThreeAbove-ar, wawThreeAbove-ar.fina, wawTwoabove-ar, wawTwoabove-ar.fina, wawTwodots-ar, wawTwodots-ar.fina, wawbelow-ar, wawring-ar, wawring-ar.fina, yat-cy, year-ar, yeh-ar, yeh-ar.fina, yeh-ar.init, yeh-ar.medi, yeh-farsi, yeh-farsi.fina, yeh-farsi.init, yeh-farsi.medi, yehFourbelow-farsi, yehFourbelow-farsi.fina, yehFourbelow-farsi.init, yehFourbelow-farsi.medi, yehHamzaabove-ar, yehHamzaabove-ar.fina, yehHamzaabove-ar.init, yehHamzaabove-ar.medi, yehKashmiri-ar, yehKashmiri-ar.fina, yehKashmiri-ar.init, yehKashmiri-ar.medi, yehRohingya-ar, yehRohingya-ar.comp, yehRohingya-ar.fina, yehSmall-ar, yehTail-ar, yehTail-ar.fina, yehThreeabove-farsi, yehThreeabove-farsi.fina, yehThreeabove-farsi.init, yehThreeabove-farsi.medi, yehThreedotsabove-farsi, yehThreedotsabove-farsi.fina, yehThreedotsabove-farsi.init, yehThreedotsabove-farsi.medi, yehThreedotsbelow-ar, yehThreedotsbelow-ar.fina, yehThreedotsbelow-ar.init, yehThreedotsbelow-ar.medi, yehTwoabove-farsi, yehTwoabove-farsi.fina, yehTwoabove-farsi.init, yehTwoabove-farsi.medi, yehTwodotsabove-farsi, yehTwodotsabove-farsi.fina, yehTwodotsabove-farsi.init, yehTwodotsabove-farsi.medi, yehTwodotsbelowDotabove-ar, yehTwodotsbelowDotabove-ar.fina, yehTwodotsbelowDotabove-ar.init, yehTwodotsbelowDotabove-ar.medi, yehTwodotsbelowHamzaabove-ar, yehTwodotsbelowHamzaabove-ar.fina, yehTwodotsbelowHamzaabove-ar.init, yehTwodotsbelowHamzaabove-ar.medi, yehTwodotsbelowNoonabove-ar, yehTwodotsbelowNoonabove-ar.fina, yehTwodotsbelowNoonabove-ar.init, yehTwodotsbelowNoonabove-ar.medi, yehVabove-ar, yehVabove-ar.fina, yehVabove-ar.init, yehVabove-ar.medi, yehVinverted-farsi, yehVinverted-farsi.fina, yehVinverted-farsi.init, yehVinverted-farsi.medi, yeh_noon-ar.fina, yehabove-ar, yehbarree-ar, yehbarree-ar.fina, yehbarreeHamzaabove-ar, yehbarreeHamzaabove-ar.fina, yehbarreeThreeabove-ar, yehbarreeThreeabove-ar.fina, yehbarreeTwoabove-ar, yehbarreeTwoabove-ar.fina, yerudieresis-cy, yu-ar, yu-ar.fina, yusbig-cy, yusbigiotified-cy, yuslittle-cy, yuslittleiotified-cy, zah-ar, zah-ar.fina, zah-ar.init, zah-ar.medi, zain-ar, zain-ar.fina, zainVinvertedabove-ar, zainVinvertedabove-ar.fina, zainabove-ar, zedescender-cy, zedieresis-cy, zero-ar, zhebreve-cy, zhedescender-cy and zhedieresis-cy

 A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not. [code: found-invalid-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: j̆ j̇ j̉ j̊ j̋ j̏ j̒ j҃ j҄ j҅ j҆ j̣̀ j̣́ j̣̃ j̣̄ j̣̆ j̣̇ j̣̈ j̣̉ j̣̊ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 2297 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
* ⚠ **WARN** Font is monospaced but 555 glyphs (24.08%) have a different width. You should check the widths of: ['A', 'AE', 'Aacute', 'Abreve', 'Acircumflex', 'Adieresis', 'Agrave', 'Amacron', 'Aogonek', 'Aring', 'Atilde', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'Dcaron', 'Dcroat', 'Ddotbelow', 'Delta', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'Edieresis', 'Edotaccent', 'Egrave', 'Emacron', 'Eng', 'Eogonek', 'Eth', 'F', 'G', 'Gbreve', 'Gcircumflex', 'Gcommaaccent', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'Hdotbelow', 'I', 'IJ', 'Iacute', 'Ibreve', 'Icircumflex', 'Idieresis', 'Idotaccent', 'Igrave', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'Kcommaaccent', 'L', 'Lacute', 'Lcaron', 'Lcommaaccent', 'Ldot', 'Lslash', 'M', 'N', 'Nacute', 'Ncaron', 'Ncommaaccent', 'Ntilde', 'O', 'OE', 'Oacute', 'Obreve', 'Ocircumflex', 'Odieresis', 'Ograve', 'Ohungarumlaut', 'Omacron', 'Omega', 'Oslash', 'Otilde', 'P', 'Q', 'R', 'Racute', 'Rcaron', 'Rcommaaccent', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'Scommaaccent', 'Sdotbelow', 'T', 'Tbar', 'Tcaron', 'Tcedilla', 'Tcommaaccent', 'Tdotbelow', 'Thorn', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'Udieresis', 'Ugrave', 'Uhungarumlaut', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'Ygrave', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'Zdotbelow', 'a', 'aacute', 'abreve', 'acircumflex', 'acute', 'acute.case', 'acutecomb', 'adieresis', 'ae', 'afii10017', 'afii10018', 'afii10019', 'afii10020', 'afii10021', 'afii10022', 'afii10023', 'afii10024', 'afii10025', 'afii10026', 'afii10027', 'afii10028', 'afii10029', 'afii10030', 'afii10031', 'afii10032', 'afii10033', 'afii10034', 'afii10035', 'afii10036', 'afii10037', 'afii10038', 'afii10039', 'afii10040', 'afii10041', 'afii10042', 'afii10043', 'afii10044', 'afii10045', 'afii10046', 'afii10047', 'afii10048', 'afii10049', 'afii10050', 'afii10051', 'afii10052', 'afii10053', 'afii10054', 'afii10055', 'afii10056', 'afii10057', 'afii10058', 'afii10059', 'afii10060', 'afii10061', 'afii10062', 'afii10065', 'afii10066', 'afii10067', 'afii10068', 'afii10069', 'afii10070', 'afii10071', 'afii10072', 'afii10073', 'afii10074', 'afii10075', 'afii10076', 'afii10077', 'afii10078', 'afii10079', 'afii10080', 'afii10081', 'afii10082', 'afii10083', 'afii10084', 'afii10085', 'afii10086', 'afii10087', 'afii10088', 'afii10089', 'afii10090', 'afii10091', 'afii10092', 'afii10093', 'afii10094', 'afii10095', 'afii10096', 'afii10097', 'afii10098', 'afii10099', 'afii10100', 'afii10101', 'afii10102', 'afii10103', 'afii10104', 'afii10105', 'afii10106', 'afii10107', 'afii10108', 'afii10109', 'afii10110', 'afii10145', 'afii10193', 'afii10846', 'afii61352', 'agrave', 'amacron', 'ampersand', 'aogonek', 'approxequal', 'aring', 'asciicircum', 'asciitilde', 'asterisk', 'at', 'atilde', 'b', 'backslash', 'bar', 'bar.double', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'breve', 'breve.case', 'brevecomb', 'brokenbar', 'bullet', 'c', 'cacute', 'caron', 'caron.alt', 'caron.case', 'caroncomb', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'cedilla', 'cedilla.case', 'cedillacmb', 'cent', 'circumflex', 'circumflex.case', 'circumflexcomb', 'colon', 'colon.alt', 'comma', 'comma.alt', 'commaaccent', 'commaaccent.case', 'commaturnedabovecmb', 'copyright', 'currency', 'd', 'dagger', 'daggerdbl', 'dcaron', 'dcroat', 'ddotbelow', 'degree', 'diaeresiscomb', 'dieresis', 'dieresis.case', 'divide', 'dollar', 'dotaccent', 'dotaccent.case', 'dotaccentcmb', 'dotbelowcmb', 'dotlessi', 'dotlessj', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'edieresis', 'edotaccent', 'egrave', 'eight', 'ellipsis', 'ellipsis.alt1', 'ellipsis.alt2', 'ellipsis.alt3', 'ellipsis.alt4', 'ellipsis.alt5', 'emacron', 'emdash', 'emdash.alt1', 'emdash.alt2', 'emdash.alt3', 'emdash.alt4', 'endash', 'eng', 'eogonek', 'equal', 'eth', 'euro', 'exclam', 'exclamdown', 'f', 'fi', 'five', 'fl', 'florin', 'four', 'foursuperior', 'fraction', 'franc', 'g', 'gbreve', 'gcircumflex', 'gcommaaccent', 'gdotaccent', 'germandbls', 'grave', 'grave.case', 'gravecomb', 'greater', 'greaterequal', 'guillemetleft', 'guillemetright', 'guilsinglleft', 'guilsinglright', 'h', 'hbar', 'hcircumflex', 'hdotbelow', 'hungarumlaut', 'hungarumlaut.case', 'hungarumlautcmb', 'hyphen', 'hyphen.alt', 'i', 'iacute', 'ibreve', 'icircumflex', 'idieresis', 'idotaccent', 'igrave', 'ij', 'imacron', 'infinity', 'integral', 'iogonek', 'itilde', 'j', 'jcircumflex', 'k', 'kcommaaccent', 'l', 'lacute', 'lcaron', 'lcommaaccent', 'ldot', 'less', 'lessequal', 'logicalnot', 'lozenge', 'lslash', 'm', 'macron', 'macron.case', 'macroncomb', 'minus', 'minute', 'mu', 'multiply', 'n', 'nacute', 'nbspace', 'ncaron', 'ncommaaccent', 'nine', 'nonbreakinghyphen', 'nonmarkingreturn', 'notequal', 'ntilde', 'numbersign', 'o', 'oacute', 'obreve', 'ocircumflex', 'odieresis', 'oe', 'ogonek', 'ogonek.case', 'ogonekcmb', 'ograve', 'ohungarumlaut', 'omacron', 'one', 'onehalf', 'onequarter', 'onesuperior', 'ordfeminine', 'ordmasculine', 'oslash', 'otilde', 'p', 'paragraph', 'parenleft', 'parenright', 'partialdiff', 'percent', 'period', 'period.alt', 'period.squat', 'periodcentered', 'perthousand', 'pi', 'plus', 'plusminus', 'product', 'q', 'question', 'questiondown', 'quotedbl', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotesingle', 'r', 'racute', 'radical', 'rcaron', 'rcommaaccent', 'registered', 'ring', 'ring.case', 'ringcmb', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'scommaaccent', 'sdotbelow', 'second', 'section', 'semicolon', 'semicolon.alt', 'seven', 'six', 'slash', 'space', 'sterling', 'summation', 't', 'tbar', 'tcaron', 'tcedilla', 'tcommaaccent', 'tdotbelow', 'thorn', 'three', 'threequarters', 'threesuperior', 'tilde', 'tilde.case', 'tildecomb', 'trademark', 'two', 'twosuperior', 'u', 'u1F7D9', 'uacute', 'ubreve', 'ucircumflex', 'udieresis', 'ugrave', 'uhungarumlaut', 'umacron', 'underscore', 'uni018F', 'uni0259', 'uni040D', 'uni045D', 'uni0492', 'uni0493', 'uni049A', 'uni049B', 'uni04A2', 'uni04A3', 'uni04AE', 'uni04AF', 'uni04B0', 'uni04B1', 'uni04BA', 'uni04BB', 'uni04D8', 'uni04E8', 'uni04E9', 'uni1E9E', 'uni2215', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'won', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'yen', 'ygrave', 'z', 'zacute', 'zcaron', 'zdotaccent', 'zdotbelow', 'zero'] [code: mono-outliers]
</div></details><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have duplicate components which have the same x,y coordinates. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components">com.google.fonts/check/glyf_non_transformed_duplicate_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have duplicate components which have the same x,y coordinates:
	* {'glyph': 'second', 'component': 'minute', 'x': 0, 'y': 0} [code: found-duplicates]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value '    ' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/rfn">com.google.fonts/check/name/rfn</a>)</summary><div>


* ⚠ **WARN** Name table entry contains "Reserved Font Name" for a family name (Courier Prime Source) that differs from the currently used family name (CourierBadi), which is fine. [code: legacy-familyname]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* ⚠ **WARN** Glyph 0x00A0 is called "nbspace": Change to "uni00A0" [code: not-recommended-00a0]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Threedotsinverted.alt.comp

	- ae-ar.fina

	- ainThreedots-ar.fina

	- ainThreedots-ar.init

	- ainThreedots-ar.medi

	- ainThreedotsbelow-ar.fina

	- ainThreedotsbelow-ar.init

	- ainThreedotsbelow-ar.medi

	- ainThreedotsdownabove-ar.fina

	- ainThreedotsdownabove-ar.init

	- ainThreedotsdownabove-ar.medi

	- ainTwodotshorizontalabove-ar.fina

	- ainTwodotshorizontalabove-ar.init

	- ainTwodotshorizontalabove-ar.medi

	- ainTwodotsverticalabove-ar.fina

	- ainTwodotsverticalabove-ar.init

	- ainTwodotsverticalabove-ar.medi

	- alef-ar.fina.alt

	- alef-ar.fina.short

	- alef-ar.fina.shorter

	- alef-ar.short

	- alef-ar.shorter

	- alefHamzaabove-ar.fina.alt

	- alefHamzabelow-ar.fina.alt

	- alefMadda-ar.fina.alt

	- alefThreeabove-ar.fina

	- alefThreeabove-ar.fina.alt

	- alefTwoabove-ar.fina

	- alefTwoabove-ar.fina.alt

	- alefWasla-ar.fina.alt

	- alefWavyhamzaabove-ar.fina

	- alefWavyhamzaabove-ar.fina.alt

	- alefWavyhamzabelow-ar.fina

	- alefWavyhamzabelow-ar.fina.alt

	- arabic_root.comp

	- bar.double

	- behDotless-ar.fina

	- behDotless-ar.hah

	- behDotless-ar.init

	- behDotless-ar.medi

	- behMeemabove-ar.fina

	- behMeemabove-ar.init

	- behMeemabove-ar.medi

	- behThreedotshorizontalbelow-ar.fina

	- behThreedotshorizontalbelow-ar.init

	- behThreedotshorizontalbelow-ar.medi

	- behThreedotsupabove-ar.fina

	- behThreedotsupabove-ar.init

	- behThreedotsupabove-ar.medi

	- behThreedotsupbelow-ar.fina

	- behThreedotsupbelow-ar.init

	- behThreedotsupbelow-ar.medi

	- behTwodotsbelowDotabove-ar.fina

	- behTwodotsbelowDotabove-ar.init

	- behTwodotsbelowDotabove-ar.medi

	- behVabove-ar.fina

	- behVabove-ar.init

	- behVabove-ar.medi

	- behVbelow-ar.fina

	- behVbelow-ar.init

	- behVbelow-ar.medi

	- behVinvertedbelow-ar.fina

	- behVinvertedbelow-ar.init

	- behVinvertedbelow-ar.medi

	- behhamzaabove-ar.fina

	- behhamzaabove-ar.init

	- behhamzaabove-ar.medi

	- bigcircle

	- caron.cap

	- charbox.comp

	- circumflex.cap

	- circumflexcomb_acutecomb.cap

	- circumflexcomb_gravecomb.cap

	- circumflexcomb_hookabovecomb.cap

	- circumflexcomb_tildecomb.cap

	- colon.alt

	- colon.arabic

	- comma.alt

	- dadDotbelow-ar.fina

	- dadDotbelow-ar.init

	- dadDotbelow-ar.medi

	- dalDotbelow-ar.fina

	- dalDotbelowTah-ar.fina

	- dalFourdots-ar.fina

	- dalRing-ar.fina

	- dalThreedotsbelow-ar.fina

	- dalThreedotsdown-ar.fina

	- dalTwodotsverticalbelowTah-ar.fina

	- dalVinvertedabove-ar.fina

	- dalVinvertedbelow-ar.fina

	- dieresis.cap

	- doublestroke-ar

	- ellipsis.alt1

	- ellipsis.alt2

	- ellipsis.alt3

	- ellipsis.alt4

	- ellipsis.alt5

	- emdash.alt1

	- emdash.alt2

	- emdash.alt3

	- emdash.alt4

	- exclam.arabic

	- fehAfrican-ar.fina

	- fehAfrican-ar.init

	- fehAfrican-ar.medi

	- fehDotbelow-ar.fina

	- fehDotbelow-ar.init

	- fehDotbelow-ar.medi

	- fehDotbelowThreedotsabove-ar.fina

	- fehDotbelowThreedotsabove-ar.init

	- fehDotbelowThreedotsabove-ar.medi

	- fehDotless-ar.fina

	- fehDotless-ar.init

	- fehDotless-ar.medi

	- fehDotmovedbelow-ar.fina

	- fehDotmovedbelow-ar.init

	- fehDotmovedbelow-ar.medi

	- fehThreedotsbelow-ar.fina

	- fehThreedotsbelow-ar.init

	- fehThreedotsbelow-ar.medi

	- fehThreedotsupbelow-ar.fina

	- fehThreedotsupbelow-ar.init

	- fehThreedotsupbelow-ar.medi

	- fehTwodotsbelow-ar.fina

	- fehTwodotsbelow-ar.init

	- fehTwodotsbelow-ar.medi

	- four-persian.urdu

	- fourabove-ar

	- fourbelow-ar

	- gafInvertedstroke-ar.fina

	- gafInvertedstroke-ar.init

	- gafInvertedstroke-ar.medi

	- gafRing-ar.fina

	- gafRing-ar.init

	- gafRing-ar.medi

	- gafThreedots-ar.fina

	- gafThreedots-ar.init

	- gafThreedots-ar.medi

	- gafTwodotsbelow-ar.fina

	- gafTwodotsbelow-ar.init

	- gafTwodotsbelow-ar.medi

	- gafsarkashabove-ar

	- ghainDotbelow-ar.fina

	- ghainDotbelow-ar.init

	- ghainDotbelow-ar.medi

	- ghainThreedotsabove-ar.fina

	- ghainThreedotsabove-ar.init

	- ghainThreedotsabove-ar.medi

	- hahFourbelow-ar.fina

	- hahFourbelow-ar.init

	- hahFourbelow-ar.medi

	- hahHamzaabove-ar.fina

	- hahHamzaabove-ar.init

	- hahHamzaabove-ar.medi

	- hahTahTwodotshorizontalbelow-ar.fina

	- hahTahTwodotshorizontalbelow-ar.init

	- hahTahTwodotshorizontalbelow-ar.medi

	- hahTahabove-ar.fina

	- hahTahabove-ar.init

	- hahTahabove-ar.medi

	- hahTahbelow-ar.fina

	- hahTahbelow-ar.init

	- hahTahbelow-ar.medi

	- hahThreedotsabove-ar.fina

	- hahThreedotsabove-ar.init

	- hahThreedotsabove-ar.medi

	- hahThreedotsupbelow-ar.fina

	- hahThreedotsupbelow-ar.init

	- hahThreedotsupbelow-ar.medi

	- hahTwodotshorizontalabove-ar.fina

	- hahTwodotshorizontalabove-ar.init

	- hahTwodotshorizontalabove-ar.medi

	- hahTwodotsverticalabove-ar.fina

	- hahTwodotsverticalabove-ar.init

	- hahTwodotsverticalabove-ar.medi

	- hehDoachashmee-ar.init.comp

	- hehVinvertedabove-ar.fina

	- hehVinvertedabove-ar.init

	- hehVinvertedabove-ar.medi

	- hehgoalHamzaabove-ar.fina

	- highhamza-ar.narrow

	- highhamzaYeh-ar.init

	- hyphen.alt

	- ittisal.comp

	- jeemThreedotsabove-ar.fina

	- jeemThreedotsabove-ar.init

	- jeemThreedotsabove-ar.medi

	- jeemThreedotsbelow-ar.fina

	- jeemThreedotsbelow-ar.init

	- jeemThreedotsbelow-ar.medi

	- jeemTwodotsabove-ar.fina

	- jeemTwodotsabove-ar.init

	- jeemTwodotsabove-ar.medi

	- kafDotabove-ar.fina

	- kafDotabove-ar.init

	- kafDotabove-ar.medi

	- kafDotbelow-ar.fina

	- kafDotbelow-ar.init

	- kafDotbelow-ar.medi

	- kafDotless-ar

	- kafDotless-ar.fina

	- kafRing-ar.fina

	- kafRing-ar.init

	- kafRing-ar.medi

	- kafThreedotsbelow-ar.fina

	- kafThreedotsbelow-ar.init

	- kafThreedotsbelow-ar.medi

	- kafTwodotshorizontalabove-ar.fina

	- kafTwodotshorizontalabove-ar.init

	- kafTwodotshorizontalabove-ar.medi

	- kafswash-ar.fina

	- kafswash-ar.init

	- kafswash-ar.medi

	- kehehDotabove-ar.fina

	- kehehDotabove-ar.init

	- kehehDotabove-ar.medi

	- kehehThreedotsabove-ar.fina

	- kehehThreedotsabove-ar.init

	- kehehThreedotsabove-ar.medi

	- kehehThreedotsbelow-ar.fina

	- kehehThreedotsbelow-ar.init

	- kehehThreedotsbelow-ar.medi

	- kehehThreedotsupbelow-ar.fina

	- kehehThreedotsupbelow-ar.init

	- kehehThreedotsupbelow-ar.medi

	- kehehTwodotshorizontalabove-ar.fina

	- kehehTwodotshorizontalabove-ar.init

	- kehehTwodotshorizontalabove-ar.medi

	- kehehVabove-ar.fina

	- kehehVabove-ar.init

	- kehehVabove-ar.medi

	- lam-ar.medi.short

	- lamBar-ar.fina

	- lamBar-ar.init

	- lamBar-ar.medi

	- lamDotabove-ar.fina

	- lamDotabove-ar.init

	- lamDotabove-ar.medi

	- lamDoublebar-ar.fina

	- lamDoublebar-ar.init

	- lamDoublebar-ar.medi

	- lamTahabove-ar.fina

	- lamTahabove-ar.init

	- lamTahabove-ar.medi

	- lamThreedotsabove-ar.fina

	- lamThreedotsabove-ar.init

	- lamThreedotsabove-ar.medi

	- lamThreedotsbelow-ar.fina

	- lamThreedotsbelow-ar.init

	- lamThreedotsbelow-ar.medi

	- lamVabove-ar.fina

	- lamVabove-ar.init

	- lamVabove-ar.medi

	- meemDotabove-ar.fina

	- meemDotabove-ar.init

	- meemDotabove-ar.medi

	- meemDotbelow-ar.fina

	- meemDotbelow-ar.init

	- meemDotbelow-ar.medi

	- meemThreedotsabove-ar.fina

	- meemThreedotsabove-ar.init

	- meemThreedotsabove-ar.medi

	- miniKeheh-ar

	- noonAfrican-ar.fina

	- noonAfrican-ar.init

	- noonAfrican-ar.medi

	- noonDotbelow-ar.fina

	- noonDotbelow-ar.init

	- noonDotbelow-ar.medi

	- noonRing-ar.fina

	- noonRing-ar.init

	- noonRing-ar.medi

	- noonTahabove-ar.fina

	- noonTahabove-ar.init

	- noonTahabove-ar.medi

	- noonThreedotsabove-ar.fina

	- noonThreedotsabove-ar.init

	- noonThreedotsabove-ar.medi

	- noonTwodotsbelow-ar.fina

	- noonTwodotsbelow-ar.init

	- noonTwodotsbelow-ar.medi

	- noonVabove-ar.fina

	- noonVabove-ar.init

	- noonVabove-ar.medi

	- noonghunna-ar.init

	- noonghunna-ar.medi

	- pehMeemabove-ar.fina

	- pehMeemabove-ar.init

	- pehMeemabove-ar.medi

	- pehVabove-ar.fina

	- pehVabove-ar.init

	- pehVabove-ar.medi

	- percent.arabic.comp

	- period.alt

	- period.arabic

	- perthousandzero

	- qafAfrican-ar.fina

	- qafAfrican-ar.init

	- qafAfrican-ar.medi

	- qafDotabove-ar.fina

	- qafDotabove-ar.init

	- qafDotabove-ar.medi

	- qafDotbelow-ar.fina

	- qafDotbelow-ar.init

	- qafDotbelow-ar.medi

	- qafDotless-ar.fina

	- qafDotless-ar.init

	- qafDotless-ar.medi

	- qafThreedotsabove-ar.fina

	- qafThreedotsabove-ar.init

	- qafThreedotsabove-ar.medi

	- qafThreedotsaboveAfrican-ar.fina

	- qafThreedotsaboveAfrican-ar.init

	- qafThreedotsaboveAfrican-ar.medi

	- rehDotbelow-ar.fina

	- rehDotbelowdotabove-ar.fina

	- rehFourdots-ar.fina

	- rehHamzaabove-ar.fina

	- rehLoop-ar.fina

	- rehNoonabove-ar.fina

	- rehRing-ar.fina

	- rehStroke-ar.fina

	- rehTwodots-ar.fina

	- rehTwodotshorizontalaboveTahabove-ar.fina

	- rehTwodotsverticalabove-ar.fina

	- rehVbelow-ar.fina

	- rehVinvertedabove-ar.fina

	- rehabove-ar

	- rehv-ar.fina

	- sadThreedots-ar.fina

	- sadThreedots-ar.init

	- sadThreedots-ar.medi

	- sadThreedotsbelow-ar.fina

	- sadThreedotsbelow-ar.init

	- sadThreedotsbelow-ar.medi

	- sadTwodotsbelow-ar.fina

	- sadTwodotsbelow-ar.init

	- sadTwodotsbelow-ar.medi

	- seenDotbelowDotabove-ar.fina

	- seenDotbelowDotabove-ar.init

	- seenDotbelowDotabove-ar.medi

	- seenFourabove-ar.fina

	- seenFourabove-ar.init

	- seenFourabove-ar.medi

	- seenFourdotsabove-ar.fina

	- seenFourdotsabove-ar.init

	- seenFourdotsabove-ar.medi

	- seenTahTwodotshorizontalabove-ar.fina

	- seenTahTwodotshorizontalabove-ar.init

	- seenTahTwodotshorizontalabove-ar.medi

	- seenThreedotsbelow-ar.fina

	- seenThreedotsbelow-ar.init

	- seenThreedotsbelow-ar.medi

	- seenTwodotsverticalabove-ar.fina

	- seenTwodotsverticalabove-ar.init

	- seenTwodotsverticalabove-ar.medi

	- seenVinvertedabove-ar.fina

	- seenVinvertedabove-ar.init

	- seenVinvertedabove-ar.medi

	- semicolon.alt

	- seven-persian.urdu

	- sheenDotbelow-ar.fina

	- sheenDotbelow-ar.init

	- sheenDotbelow-ar.medi

	- sheenThreedotsbelow-ar.fina

	- sheenThreedotsbelow-ar.init

	- sheenThreedotsbelow-ar.medi

	- sindhipostpositionmen-ar.fina

	- sindhipostpositionmen-ar.init

	- sindhipostpositionmen-ar.medi

	- stroke-ar

	- tahThreedots-ar.fina

	- tahThreedots-ar.init

	- tahThreedots-ar.medi

	- tahTwodotsabove-ar.fina

	- tahTwodotsabove-ar.init

	- tahTwodotsabove-ar.medi

	- tail.comp

	- tchehDotabove-ar.fina

	- tchehDotabove-ar.init

	- tchehDotabove-ar.medi

	- tchehVabove-ar.fina

	- tchehVabove-ar.init

	- tchehVabove-ar.medi

	- tehMarbuta-ar.alt

	- tehMarbutagoal-ar.fina

	- tehRing-ar.fina

	- tehRing-ar.init

	- tehRing-ar.medi

	- tehTehabove-ar.fina

	- tehTehabove-ar.init

	- tehTehabove-ar.medi

	- tehThreedotsdown-ar.fina

	- tehThreedotsdown-ar.init

	- tehThreedotsdown-ar.medi

	- tehThreedotsupbelow-ar.fina

	- tehThreedotsupbelow-ar.init

	- tehThreedotsupbelow-ar.medi

	- tehVabove-ar.fina

	- tehVabove-ar.init

	- tehVabove-ar.medi

	- threeabove-ar

	- threedotshorizontalbelow-ar

	- ttehVabove-ar.fina

	- ttehVabove-ar.init

	- ttehVabove-ar.medi

	- twoabove-ar

	- wasla-ar

	- wawDotabove-ar.fina

	- wawDotcenter-ar.fina

	- wawStraight-ar.fina

	- wawThreeAbove-ar.fina

	- wawTwoabove-ar.fina

	- wawTwodots-ar.fina

	- wawring-ar.fina

	- yehFourbelow-farsi.fina

	- yehFourbelow-farsi.init

	- yehFourbelow-farsi.medi

	- yehKashmiri-ar.fina

	- yehKashmiri-ar.init

	- yehKashmiri-ar.medi

	- yehRohingya-ar.comp

	- yehRohingya-ar.fina

	- yehTail-ar.fina

	- yehThreeabove-farsi.fina

	- yehThreeabove-farsi.init

	- yehThreeabove-farsi.medi

	- yehThreedotsabove-farsi.fina

	- yehThreedotsabove-farsi.init

	- yehThreedotsabove-farsi.medi

	- yehThreedotsbelow-ar.fina

	- yehThreedotsbelow-ar.init

	- yehThreedotsbelow-ar.medi

	- yehTwoabove-farsi.fina

	- yehTwoabove-farsi.init

	- yehTwoabove-farsi.medi

	- yehTwodotsabove-farsi.fina

	- yehTwodotsabove-farsi.init

	- yehTwodotsabove-farsi.medi

	- yehTwodotsbelowDotabove-ar.fina

	- yehTwodotsbelowDotabove-ar.init

	- yehTwodotsbelowDotabove-ar.medi

	- yehTwodotsbelowHamzaabove-ar.fina

	- yehTwodotsbelowHamzaabove-ar.init

	- yehTwodotsbelowHamzaabove-ar.medi

	- yehTwodotsbelowNoonabove-ar.fina

	- yehTwodotsbelowNoonabove-ar.init

	- yehTwodotsbelowNoonabove-ar.medi

	- yehVabove-ar.fina

	- yehVabove-ar.init

	- yehVabove-ar.medi

	- yehVinverted-farsi.fina

	- yehVinverted-farsi.init

	- yehVinverted-farsi.medi

	- yehbarreeThreeabove-ar.fina

	- yehbarreeTwoabove-ar.fina

	- zainVinvertedabove-ar.fina 

	- zero.slash
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: sigmafinal	Contours detected: 2	Expected: 1

	- Glyph name: yuslittleiotified-cy	Contours detected: 5	Expected: 2

	- Glyph name: yusbigiotified-cy	Contours detected: 3	Expected: 2

	- Glyph name: Ksi-cy	Contours detected: 1	Expected: 2

	- Glyph name: ksi-cy	Contours detected: 1	Expected: 2

	- Glyph name: Izhitsadblgrave-cy	Contours detected: 2	Expected: 3

	- Glyph name: Uk-cy	Contours detected: 2	Expected: 3

	- Glyph name: uk-cy	Contours detected: 2	Expected: 3

	- Glyph name: ahookabove	Contours detected: 2	Expected: 3

	- Glyph name: Acircumflexhookabove	Contours detected: 3	Expected: 4

	- Glyph name: Acircumflextilde	Contours detected: 3	Expected: 4

	- Glyph name: Abrevetilde	Contours detected: 3	Expected: 4

	- Glyph name: abrevetilde	Contours detected: 3	Expected: 4

	- Glyph name: ehookabove	Contours detected: 2	Expected: 3

	- Glyph name: Ecircumflexhookabove	Contours detected: 2	Expected: 3

	- Glyph name: Ecircumflextilde	Contours detected: 2	Expected: 3

	- Glyph name: ihookabove	Contours detected: 1	Expected: 2

	- Glyph name: ohookabove	Contours detected: 2	Expected: 3

	- Glyph name: Ocircumflexhookabove	Contours detected: 3	Expected: 4

	- Glyph name: Ocircumflextilde	Contours detected: 3	Expected: 4

	- Glyph name: Ohorntilde	Contours detected: 2	Expected: 3 or 4

	- Glyph name: ohorntilde	Contours detected: 2	Expected: 3

	- Glyph name: Uhorntilde	Contours detected: 1	Expected: 2

	- Glyph name: uhorntilde	Contours detected: 1	Expected: 2

	- Glyph name: narrownbspace	Contours detected: 28	Expected: 0

	- Glyph name: minute	Contours detected: 0	Expected: 1

	- Glyph name: second	Contours detected: 0	Expected: 2

	- Glyph name: interrobang	Contours detected: 3	Expected: 2

	- Glyph name: colonsign	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: divorceSymbol	Contours detected: 5	Expected: 3

	- Glyph name: gnaborretni	Contours detected: 3	Expected: 2

	- Glyph name: zeroWidthNoBreakSpace	Contours detected: 25	Expected: 0

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: lira	Contours detected: 2	Expected: 1 

	- Glyph name: summation	Contours detected: 3	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 1228 among a set of 13 math glyphs.
The following math glyphs have a different width, though:

Width = 1075:
sphericalangle
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acute.case (unencoded), breve.case (unencoded), caron.case (unencoded), circumflex.case (unencoded), dieresis.case (unencoded), dotaccent.case (unencoded), grave.case (unencoded), hungarumlaut.case (unencoded), leftarrowheadabove-ar (U+08F7), macron.case (unencoded), ring.case (unencoded) and tilde.case (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 VS1 (U+FE00), VS10 (U+FE09), VS11 (U+FE0A), VS12 (U+FE0B), VS13 (U+FE0C), VS14 (U+FE0D), VS15 (U+FE0E), VS16 (U+FE0F), VS2 (U+FE01), VS3 (U+FE02), VS4 (U+FE03), VS5 (U+FE04), VS6 (U+FE05), VS7 (U+FE06), VS8 (U+FE07), VS9 (U+FE08), acutecomb (U+0301), ainabove-ar (U+0611), alefLamYehabove-ar (U+0616), alefabove-ar (U+0670), alefbelow-ar (U+0656), annisfabove-ar (U+08DC), arrubabove-ar (U+08D4), assajdaabove-ar (U+08DB), aththalathaabove-ar (U+08DA), brevebelowcomb (U+032E), brevecomb (U+0306), breveinvertedbelowcomb (U+032F), breveinvertedcomb (U+0311), caroncomb (U+030C), cedillacmb (U+0327), circumflexcomb (U+0302), commaaccent (U+0326), commaturnedabovecmb (U+0312), damma-ar (U+064F), dammaCurly-ar (U+08E5), dammaDot-ar (U+08FE), dammainverted-ar (U+0657), dammareversed-ar (U+065D), dammasmall-ar (U+0619), dammatan-ar (U+064C), dammatanCurly-ar (U+08E8), dammaturnedbelow-ar (U+08E3), dasiapneumatacomb-cy (U+0485), dblgravecomb (U+030F), diaeresiscomb (U+0308), dotStopabove-ar (U+06EC), dotaccentcmb (U+0307), dotbelowcmb (U+0323), dotvowelbelow-ar (U+065C), doublerightarrowheadDotabove-ar (U+08FC), doublerightarrowheadabove-ar (U+08FB), fatha-ar (U+064E), fathaCurly-ar (U+08E4), fathaDotabove-ar (U+08F5), fathaHorizont-ar (U+0659), fathaRing-ar (U+08F4), fathasmall-ar (U+0618), fathatan-ar (U+064B), fathatanCurly-ar (U+08E7), fathatwodots-ar (U+065E), footnotemarkerabove-ar (U+08E0), graphemejoinercomb (U+034F), gravecomb (U+0300), hahabove-ar (U+06E1), hamzaabove-ar (U+0654), hamzabelow-ar (U+0655), highwaw-ar (U+08F3), hookabovecomb (U+0309), hundredthousandssigncomb-cy (U+0488), hungarumlautcmb (U+030B), jeemabove-ar (U+06DA), kasra-ar (U+0650), kasraCurly-ar (U+08E6), kasraDotbelow-ar (U+08F6), kasrasmall-ar (U+061A), kasratan-ar (U+064D), kasratanCurly-ar (U+08E9), lamAlefabove-ar (U+06D9), largerounddotbelow-ar (U+08CF), leftarrowheadbelow-ar (U+08F9), lowlinecomb (U+0332), macronbelowcomb (U+0331), macroncomb (U+0304), madda-ar (U+0653), maddalong-ar (U+06E4), marksidewaysnoonghunna-ar (U+08FF), meemStopabove-ar (U+06E2), meemabove-ar (U+06D8), meembelow-ar (U+06ED), millionssigncomb-cy (U+0489), noonKasraabove-ar (U+08D8), noonKasrabelow-ar (U+08D9), noonabove-ar (U+06E8), noonghunnaabove-ar (U+0658), ogonekcmb (U+0328), opendammatan-ar (U+08F1), openfathatan-ar (U+08F0), openkasratan-ar (U+08F2), palatalizationcomb-cy (U+0484), psilipneumatacomb-cy (U+0486), qafLamAlefMaksuraabove-ar (U+06D7), qafabove-ar (U+08D7), qifabove-ar (U+08DE), rehDadabove-ar (U+0613), rehHahabove-ar (U+0612), rhombusStopabove-ar (U+06EB), rhombusStopbelow-ar (U+06EA), rightarrowheadDotabove-ar (U+08FD), rightarrowheadabove-ar (U+08F8), rightarrowheadbelow-ar (U+08FA), ringcmb (U+030A), sadLamAlefMaksuraabove-ar (U+06D6), sadabove-ar (U+0610), safhaabove-ar (U+08E1), sahabove-ar (U+08CC), saktaabove-ar (U+08DD), seenabove-ar (U+06DC), seenbelow-ar (U+06E3), shadda-ar (U+0651), smallainabove-ar (U+08D6), smallsadabove-ar (U+08D5), sukun-ar (U+0652), sukunoval-ar (U+06E0), sukunround-ar (U+06DF), tahabove-ar (U+0615), takhallusabove-ar (U+0614), threedotsabove-ar (U+06DB), tildebelowcomb (U+0330), tildecomb (U+0303), titlocomb-cy (U+0483), toneloopabove-ar (U+08EC), toneloopbelow-ar (U+08EF), toneonedotabove-ar (U+08EA), toneonedotbelow-ar (U+08ED), tonetwodotsabove-ar (U+08EB), tonetwodotsbelow-ar (U+08EE), vabove-ar (U+065A), vinvertedabove-ar (U+065B), waqfaabove-ar (U+08DF), wavyhamzabelow-ar (U+065F), wawbelow-ar (U+08D3), yehabove-ar (U+06E7) and zainabove-ar (U+0617) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Elhook-cy (U+0512): L<<520.0,764.0>--<513.0,733.0>> -> L<<513.0,733.0>--<506.0,696.0>>

	* Elhook-cy (U+0512): L<<567.0,1028.0>--<520.0,764.0>> -> L<<520.0,764.0>--<513.0,733.0>>

	* Eltail-cy (U+04C5): L<<509.0,764.0>--<502.0,733.0>> -> L<<502.0,733.0>--<495.0,696.0>>

	* Eltail-cy (U+04C5): L<<556.0,1028.0>--<509.0,764.0>> -> L<<509.0,764.0>--<502.0,733.0>>

	* Emtail-cy (U+04CD): L<<757.0,127.0>--<921.0,1055.0>> -> L<<921.0,1055.0>--<928.0,1108.0>>

	* Kabashkir-cy (U+04A0): L<<431.0,399.0>--<423.0,365.0>> -> L<<423.0,365.0>--<381.0,127.0>>

	* Kabashkir-cy (U+04A0): L<<600.0,612.0>--<453.0,430.0>> -> L<<453.0,430.0>--<431.0,399.0>>

	* Kastroke-cy (U+049E): L<<353.0,942.0>--<299.0,639.0>> -> L<<299.0,639.0>--<292.0,584.0>>

	* Kaverticalstroke-cy (U+049C): L<<531.0,813.0>--<565.0,844.0>> -> L<<565.0,844.0>--<836.0,1124.0>>

	* Uk-cy (U+0478): L<<434.0,1124.0>--<544.0,840.0>> -> L<<544.0,840.0>--<566.0,768.0>>

	* Uk-cy (U+0478): L<<566.0,768.0>--<608.0,838.0>> -> L<<608.0,838.0>--<821.0,1124.0>>

	* Yusbigiotified-cy (U+046C): L<<262.0,127.0>--<400.0,479.0>> -> L<<400.0,479.0>--<425.0,543.0>>

	* Yuslittle-cy (U+0466): L<<620.0,1108.0>--<536.0,887.0>> -> L<<536.0,887.0>--<397.0,553.0>>

	* Yuslittle-cy (U+0466): L<<627.0,891.0>--<621.0,1014.0>> -> L<<621.0,1014.0>--<620.0,1108.0>>

	* Yuslittle-cy (U+0466): L<<652.0,489.0>--<627.0,891.0>> -> L<<627.0,891.0>--<621.0,1014.0>>

	* Zhedescender-cy (U+0496): L<<421.0,127.0>--<463.0,365.0>> -> L<<463.0,365.0>--<467.0,399.0>>

	* Zhedescender-cy (U+0496): L<<588.0,401.0>--<580.0,365.0>> -> L<<580.0,365.0>--<538.0,127.0>>

	* Zhedescender-cy (U+0496): L<<725.0,598.0>--<606.0,430.0>> -> L<<606.0,430.0>--<588.0,401.0>>

	* angleright (U+232A): L<<440.0,1348.0>--<567.0,1079.0>> -> L<<567.0,1079.0>--<715.0,768.0>>

	* angleright (U+232A): L<<730.0,563.0>--<259.0,-6.0>> -> L<<259.0,-6.0>--<173.0,-111.0>>

	* annisfabove-ar (U+08DC): L<<322.0,1093.0>--<324.0,1093.0>> -> L<<324.0,1093.0>--<343.0,1093.0>>

	* annisfabove-ar (U+08DC): L<<626.0,1093.0>--<675.0,1093.0>> -> L<<675.0,1093.0>--<675.0,1093.0>>

	* arrubabove-ar (U+08D4): L<<282.0,1092.0>--<347.0,1092.0>> -> L<<347.0,1092.0>--<347.0,1092.0>>

	* arrubabove-ar (U+08D4): L<<347.0,1092.0>--<347.0,1092.0>> -> L<<347.0,1092.0>--<448.0,1092.0>>

	* arrubabove-ar (U+08D4): L<<783.0,1092.0>--<798.0,1092.0>> -> L<<798.0,1092.0>--<798.0,1092.0>>

	* arrubabove-ar (U+08D4): L<<798.0,1092.0>--<798.0,1092.0>> -> L<<798.0,1092.0>--<827.0,1092.0>>

	* assajdaabove-ar (U+08DB): L<<860.0,1063.0>--<861.0,1063.0>> -> L<<861.0,1063.0>--<861.0,1063.0>>

	* assajdaabove-ar (U+08DB): L<<861.0,1063.0>--<861.0,1063.0>> -> L<<861.0,1063.0>--<868.0,1063.0>>

	* asterisk-ar (U+066D): L<<477.0,471.0>--<551.0,831.0>> -> L<<551.0,831.0>--<553.0,842.0>>

	* commercialMinusSign (U+2052): L<<156.0,297.0>--<764.0,1145.0>> -> L<<764.0,1145.0>--<911.0,1348.0>>

	* commercialMinusSign (U+2052): L<<59.0,162.0>--<156.0,297.0>> -> L<<156.0,297.0>--<764.0,1145.0>>

	* ghemiddlehook-cy (U+0495): L<<488.0,547.0>--<605.0,547.0>> -> L<<605.0,547.0>--<685.0,545.0>>

	* gnaborretni (U+2E18): L<<344.0,-338.0>--<372.0,-203.0>> -> L<<372.0,-203.0>--<404.0,-33.0>>

	* gnaborretni (U+2E18): L<<578.0,178.0>--<542.0,-51.0>> -> L<<542.0,-51.0>--<500.0,-340.0>>

	* interrobang (U+203D): L<<447.0,618.0>--<483.0,848.0>> -> L<<483.0,848.0>--<526.0,1137.0>>

	* interrobang (U+203D): L<<681.0,1135.0>--<655.0,999.0>> -> L<<655.0,999.0>--<621.0,829.0>>

	* izhitsa-cy (U+0475): L<<386.0,756.0>--<449.0,225.0>> -> L<<449.0,225.0>--<458.0,143.0>>

	* izhitsadblgrave-cy (U+0477): L<<351.0,756.0>--<418.0,225.0>> -> L<<418.0,225.0>--<423.0,143.0>>

	* psi (U+03C8): L<<321.0,-424.0>--<354.0,-215.0>> -> L<<354.0,-215.0>--<390.0,-6.0>>

	* psi (U+03C8): L<<416.0,137.0>--<516.0,705.0>> -> L<<516.0,705.0>--<573.0,1030.0>>

	* qifabove-ar (U+08DE): L<<490.0,1093.0>--<499.0,1093.0>> -> L<<499.0,1093.0>--<499.0,1093.0>>

	* qifabove-ar (U+08DE): L<<499.0,1093.0>--<499.0,1093.0>> -> L<<499.0,1093.0>--<501.0,1093.0>>

	* qifabove-ar (U+08DE): L<<499.0,1093.0>--<501.0,1093.0>> -> L<<501.0,1093.0>--<789.0,1093.0>>

	* thousand-cy (U+0482): L<<453.0,227.0>--<543.0,250.0>> -> L<<543.0,250.0>--<643.0,268.0>>

	* yusbig-cy (U+046B): L<<435.0,756.0>--<517.0,621.0>> -> L<<517.0,621.0>--<550.0,563.0>>

	* yusbigiotified-cy (U+046D): L<<291.0,127.0>--<394.0,338.0>> -> L<<394.0,338.0>--<415.0,379.0>>

	* yusbigiotified-cy (U+046D): L<<394.0,338.0>--<415.0,379.0>> -> L<<415.0,379.0>--<443.0,424.0>>

	* zedescender-cy (U+0499): L<<428.0,117.0>--<467.0,117.0>> -> L<<467.0,117.0>--<492.0,115.0>>

	* zhedescender-cy (U+0497): L<<447.0,127.0>--<471.0,266.0>> -> L<<471.0,266.0>--<474.0,293.0>>

	* zhedescender-cy (U+0497): L<<675.0,756.0>--<636.0,539.0>> -> L<<636.0,539.0>--<630.0,492.0>> 

	* zhedescender-cy (U+0497): L<<705.0,418.0>--<613.0,315.0>> -> L<<613.0,315.0>--<597.0,295.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Emtail-cy (U+04CD): B<<380.5,1044.0>-<376.0,1086.0>-<375.0,1108.0>>/L<<375.0,1108.0>--<202.0,127.0>> = 12.603878154295307

	* Emtail-cy (U+04CD): L<<921.0,1055.0>--<928.0,1108.0>>/B<<928.0,1108.0>-<921.0,1087.0>-<895.5,1032.0>> = 10.911128384283376

	* Iishorttail-cy (U+048A): L<<360.0,1124.0>--<209.0,270.0>>/B<<209.0,270.0>-<230.0,329.0>-<384.0,529.5>> = 9.565166501679286

	* Iishorttail-cy (U+048A): L<<689.0,127.0>--<840.0,981.0>>/B<<840.0,981.0>-<829.0,949.0>-<779.5,878.0>> = 8.943292419114242

	* Izhitsa-cy (U+0474): B<<398.0,204.5>-<397.0,169.0>-<395.0,143.0>>/B<<395.0,143.0>-<405.0,187.0>-<440.5,286.0>> = 8.405560710291214

	* Izhitsadblgrave-cy (U+0476): B<<365.0,275.0>-<365.0,189.0>-<362.0,143.0>>/B<<362.0,143.0>-<370.0,180.0>-<399.5,263.5>> = 8.469071728220317

	* Mu (U+039C): L<<727.0,125.0>--<899.0,1102.0>>/B<<899.0,1102.0>-<888.0,1075.0>-<861.5,1018.5>> = 12.181786191984422

	* Upsilondasia (U+1F59): B<<752.0,1060.0>-<752.0,1025.0>-<749.0,983.0>>/B<<749.0,983.0>-<790.0,1134.0>-<843.0,1204.0>> = 11.10526901331856

	* Upsilondasiaoxia (U+1F5D): B<<783.0,1058.0>-<783.0,1023.0>-<780.0,983.0>>/B<<780.0,983.0>-<820.0,1134.0>-<873.5,1204.0>> = 10.547755432741646

	* Upsilondasiaperispomeni (U+1F5F): B<<764.0,1058.0>-<764.0,1023.0>-<761.0,983.0>>/B<<761.0,983.0>-<801.0,1134.0>-<854.5,1204.0>> = 10.547755432741646

	* Upsilondasiavaria (U+1F5B): B<<783.0,1058.0>-<783.0,1023.0>-<780.0,983.0>>/B<<780.0,983.0>-<820.0,1134.0>-<873.5,1204.0>> = 10.547755432741646

	* Upsilonoxia (U+1FEB): B<<730.0,1044.0>-<730.0,1016.0>-<728.0,983.0>>/B<<728.0,983.0>-<769.0,1134.0>-<827.0,1204.0>> = 11.722656534376283

	* Upsilontonos (U+038E): B<<730.0,1044.0>-<730.0,1016.0>-<728.0,983.0>>/B<<728.0,983.0>-<769.0,1134.0>-<827.0,1204.0>> = 11.722656534376283

	* Upsilonvaria (U+1FEA): B<<744.0,1044.0>-<744.0,1016.0>-<742.0,983.0>>/B<<742.0,983.0>-<784.0,1134.0>-<841.5,1204.0>> = 12.075449967784303

	* Yuslittle-cy (U+0466): L<<647.0,553.0>--<652.0,489.0>>/L<<652.0,489.0>--<627.0,891.0>> = 0.9085715588344316

	* Yuslittleiotified-cy (U+0468): B<<760.0,960.0>-<767.0,1042.0>-<779.0,1108.0>>/B<<779.0,1108.0>-<747.0,960.0>-<706.0,824.0>> = 1.895622258614662

	* alphadasiaperispomeniypogegrammeni (U+1F87): B<<692.5,639.5>-<707.0,578.0>-<715.0,530.0>>/L<<715.0,530.0>--<715.0,535.0>> = 9.462322208025613

	* alphamacron (U+1FB1): B<<677.5,639.5>-<692.0,578.0>-<700.0,530.0>>/L<<700.0,530.0>--<700.0,535.0>> = 9.462322208025613

	* alphapsiliperispomeniypogegrammeni (U+1F86): B<<692.5,639.5>-<707.0,578.0>-<715.0,530.0>>/L<<715.0,530.0>--<715.0,535.0>> = 9.462322208025613

	* annisfabove-ar (U+08DC): L<<792.0,1044.0>--<793.0,1044.0>>/B<<793.0,1044.0>-<760.0,1045.0>-<748.5,1059.0>> = 1.735704588928346

	* assajdaabove-ar (U+08DB): L<<851.0,1028.0>--<851.0,1028.0>>/B<<851.0,1028.0>-<832.0,1029.0>-<822.5,1038.5>> = 3.012787504183286

	* narrownbspace (U+202F): B<<597.0,996.0>-<588.0,1001.0>-<586.0,1026.0>>/L<<586.0,1026.0>--<586.0,1024.0>> = 4.573921259900818

	* narrownbspace (U+202F): L<<295.0,698.0>--<293.0,698.0>>/B<<293.0,698.0>-<310.0,694.0>-<329.5,686.5>> = 13.240519915187184

	* narrownbspace (U+202F): L<<586.0,1026.0>--<586.0,1024.0>>/B<<586.0,1024.0>-<582.0,1055.0>-<579.0,1086.5>> = 7.352379359892374

	* saktaabove-ar (U+08DD): L<<417.0,1047.0>--<417.0,1047.0>>/B<<417.0,1047.0>-<387.0,1049.0>-<375.5,1062.5>> = 3.8140748342903783

	* yehKashmiri-ar (U+0620): B<<542.0,21.0>-<556.0,21.0>-<569.0,20.0>>/B<<569.0,20.0>-<524.0,14.0>-<474.0,12.0>> = 11.993348723586953

	* yehKashmiri-ar (U+0620): B<<726.0,-81.0>-<679.0,9.0>-<569.0,20.0>>/B<<569.0,20.0>-<683.0,35.0>-<751.5,76.0>> = 13.206450777229495 

	* zerowidthnonjoiner (U+200C): B<<800.0,1159.0>-<800.0,1166.0>-<801.0,1171.0>>/B<<801.0,1171.0>-<788.0,1135.0>-<772.5,1094.5>> = 8.545281895300802 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 22 | 30 | 242 | 13 | 168 | 0 |
| 0% | 5% | 6% | 51% | 3% | 35% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
