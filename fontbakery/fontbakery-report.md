## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[23] CourierBadi-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


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


* 🔥 **FAIL** Glyph "uni202F" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
* 🔥 **FAIL** Glyph "uniFEFF" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
</div></details><details><summary>🔥 <b>FAIL:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* 🔥 **FAIL** The following glyph names do not comply with naming conventions: doublestroke-ar, fourabove-ar, fourbelow-ar, gafsarkashabove-ar, kafDotless-ar, kafDotless-ar.fina, miniKeheh-ar, rehabove-ar, stroke-ar, threeabove-ar, threedotshorizontalbelow-ar, twoabove-ar and wasla-ar

 A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not. [code: found-invalid-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ȋ i̒ i҃ i҄ i҅ i҆ i̦̇ i̦̊ i̦̋ ȋ̦ i̦̒ i̦҃ i̦҄ i̦҅ i̦҆ i̧̇ i̧̊ i̧̋ ȋ̧ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
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

	- acute.case

	- arabic_root.comp

	- bigcircle

	- breve.case

	- caron.cap

	- caron.case

	- cedilla.case

	- charbox.comp

	- circumflex.cap

	- circumflex.case

	- circumflexcomb_acutecomb.cap

	- circumflexcomb_gravecomb.cap

	- circumflexcomb_hookabovecomb.cap

	- circumflexcomb_tildecomb.cap

	- colon.alt

	- colon.arabic

	- comma.alt

	- commaaccent.case

	- dieresis.cap

	- dieresis.case

	- dotaccent.case

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

	- fourabove-ar

	- fourbelow-ar

	- gafsarkashabove-ar

	- grave.case

	- hungarumlaut.case

	- hyphen.alt

	- idotaccent

	- ittisal.comp

	- kafDotless-ar

	- kafDotless-ar.fina

	- macron.case

	- miniKeheh-ar

	- ogonek.case

	- percent.arabic.comp

	- period.alt

	- period.arabic

	- perthousandzero

	- rehabove-ar

	- ring.case

	- semicolon.alt

	- stroke-ar

	- tail.comp

	- threeabove-ar

	- threedotshorizontalbelow-ar

	- tilde.case

	- twoabove-ar

	- uni0326.case

	- uni0620.fina

	- uni0620.init

	- uni0620.medi

	- uni0622.fina.alt

	- uni0623.fina.alt

	- uni0625.fina.alt

	- uni0627.fina.alt

	- uni0627.fina.short

	- uni0627.fina.shorter

	- uni0627.short

	- uni0627.shorter

	- uni0629.alt

	- uni063B.fina

	- uni063B.init

	- uni063B.medi

	- uni063C.fina

	- uni063C.init

	- uni063C.medi

	- uni063D.fina

	- uni063D.init

	- uni063D.medi

	- uni063E.fina

	- uni063E.init

	- uni063E.medi

	- uni063F.fina

	- uni063F.init

	- uni063F.medi

	- uni0644.medi.short

	- uni066E.fina

	- uni066E.hah

	- uni066E.init

	- uni066E.medi

	- uni066F.fina

	- uni066F.init

	- uni066F.medi

	- uni0671.fina.alt

	- uni0672.fina

	- uni0672.fina.alt

	- uni0673.fina

	- uni0673.fina.alt

	- uni0674.narrow

	- uni0678.init

	- uni067C.fina

	- uni067C.init

	- uni067C.medi

	- uni067D.fina

	- uni067D.init

	- uni067D.medi

	- uni0681.fina

	- uni0681.init

	- uni0681.medi

	- uni0682.fina

	- uni0682.init

	- uni0682.medi

	- uni0685.fina

	- uni0685.init

	- uni0685.medi

	- uni0689.fina

	- uni068A.fina

	- uni068B.fina

	- uni068F.fina

	- uni0690.fina

	- uni0692.fina

	- uni0693.fina

	- uni0694.fina

	- uni0695.fina

	- uni0696.fina

	- uni0697.fina

	- uni0699.fina

	- uni069A.fina

	- uni069A.init

	- uni069A.medi

	- uni069B.fina

	- uni069B.init

	- uni069B.medi

	- uni069C.fina

	- uni069C.init

	- uni069C.medi

	- uni069D.fina

	- uni069D.init

	- uni069D.medi

	- uni069E.fina

	- uni069E.init

	- uni069E.medi

	- uni069F.fina

	- uni069F.init

	- uni069F.medi

	- uni06A0.fina

	- uni06A0.init

	- uni06A0.medi

	- uni06A1.fina

	- uni06A1.init

	- uni06A1.medi

	- uni06A2.fina

	- uni06A2.init

	- uni06A2.medi

	- uni06A3.fina

	- uni06A3.init

	- uni06A3.medi

	- uni06A5.fina

	- uni06A5.init

	- uni06A5.medi

	- uni06A7.fina

	- uni06A7.init

	- uni06A7.medi

	- uni06A8.fina

	- uni06A8.init

	- uni06A8.medi

	- uni06AA.fina

	- uni06AA.init

	- uni06AA.medi

	- uni06AB.fina

	- uni06AB.init

	- uni06AB.medi

	- uni06AC.fina

	- uni06AC.init

	- uni06AC.medi

	- uni06AE.fina

	- uni06AE.init

	- uni06AE.medi

	- uni06B0.fina

	- uni06B0.init

	- uni06B0.medi

	- uni06B2.fina

	- uni06B2.init

	- uni06B2.medi

	- uni06B4.fina

	- uni06B4.init

	- uni06B4.medi

	- uni06B5.fina

	- uni06B5.init

	- uni06B5.medi

	- uni06B6.fina

	- uni06B6.init

	- uni06B6.medi

	- uni06B7.fina

	- uni06B7.init

	- uni06B7.medi

	- uni06B8.fina

	- uni06B8.init

	- uni06B8.medi

	- uni06B9.fina

	- uni06B9.init

	- uni06B9.medi

	- uni06BA.init

	- uni06BA.medi

	- uni06BC.fina

	- uni06BC.init

	- uni06BC.medi

	- uni06BD.fina

	- uni06BD.init

	- uni06BD.medi

	- uni06BE.init.comp

	- uni06BF.fina

	- uni06BF.init

	- uni06BF.medi

	- uni06C2.fina

	- uni06C3.fina

	- uni06C4.fina

	- uni06CA.fina

	- uni06CD.fina

	- uni06CE.fina

	- uni06CE.init

	- uni06CE.medi

	- uni06CF.fina

	- uni06D1.fina

	- uni06D1.init

	- uni06D1.medi

	- uni06D5.fina

	- uni06EE.fina

	- uni06EF.fina

	- uni06F4.urdu

	- uni06F7.urdu

	- uni06FA.fina

	- uni06FA.init

	- uni06FA.medi

	- uni06FB.fina

	- uni06FB.init

	- uni06FB.medi

	- uni06FC.fina

	- uni06FC.init

	- uni06FC.medi

	- uni06FE.fina

	- uni06FE.init

	- uni06FE.medi

	- uni06FF.fina

	- uni06FF.init

	- uni06FF.medi

	- uni0750.fina

	- uni0750.init

	- uni0750.medi

	- uni0751.fina

	- uni0751.init

	- uni0751.medi

	- uni0752.fina

	- uni0752.init

	- uni0752.medi

	- uni0753.fina

	- uni0753.init

	- uni0753.medi

	- uni0754.fina

	- uni0754.init

	- uni0754.medi

	- uni0755.fina

	- uni0755.init

	- uni0755.medi

	- uni0756.fina

	- uni0756.init

	- uni0756.medi

	- uni0757.fina

	- uni0757.init

	- uni0757.medi

	- uni0758.fina

	- uni0758.init

	- uni0758.medi

	- uni0759.fina

	- uni075A.fina

	- uni075B.fina

	- uni075C.fina

	- uni075C.init

	- uni075C.medi

	- uni075D.fina

	- uni075D.init

	- uni075D.medi

	- uni075E.fina

	- uni075E.init

	- uni075E.medi

	- uni075F.fina

	- uni075F.init

	- uni075F.medi

	- uni0760.fina

	- uni0760.init

	- uni0760.medi

	- uni0761.fina

	- uni0761.init

	- uni0761.medi

	- uni0762.fina

	- uni0762.init

	- uni0762.medi

	- uni0763.fina

	- uni0763.init

	- uni0763.medi

	- uni0764.fina

	- uni0764.init

	- uni0764.medi

	- uni0765.fina

	- uni0765.init

	- uni0765.medi

	- uni0766.fina

	- uni0766.init

	- uni0766.medi

	- uni0767.fina

	- uni0767.init

	- uni0767.medi

	- uni0768.fina

	- uni0768.init

	- uni0768.medi

	- uni0769.fina

	- uni0769.init

	- uni0769.medi

	- uni076A.fina

	- uni076A.init

	- uni076A.medi

	- uni076B.fina

	- uni076C.fina

	- uni076D.fina

	- uni076D.init

	- uni076D.medi

	- uni076E.fina

	- uni076E.init

	- uni076E.medi

	- uni076F.fina

	- uni076F.init

	- uni076F.medi

	- uni0770.fina

	- uni0770.init

	- uni0770.medi

	- uni0771.fina

	- uni0772.fina

	- uni0772.init

	- uni0772.medi

	- uni0773.fina

	- uni0773.fina.alt

	- uni0774.fina

	- uni0774.fina.alt

	- uni0775.fina

	- uni0775.init

	- uni0775.medi

	- uni0776.fina

	- uni0776.init

	- uni0776.medi

	- uni0777.fina

	- uni0777.init

	- uni0777.medi

	- uni0778.fina

	- uni0779.fina

	- uni077A.fina

	- uni077B.fina

	- uni077C.fina

	- uni077C.init

	- uni077C.medi

	- uni077D.fina

	- uni077D.init

	- uni077D.medi

	- uni077E.fina

	- uni077E.init

	- uni077E.medi

	- uni077F.fina

	- uni077F.init

	- uni077F.medi

	- uni08A0.fina

	- uni08A0.init

	- uni08A0.medi

	- uni08A1.fina

	- uni08A1.init

	- uni08A1.medi

	- uni08A2.fina

	- uni08A2.init

	- uni08A2.medi

	- uni08A3.fina

	- uni08A3.init

	- uni08A3.medi

	- uni08A4.fina

	- uni08A4.init

	- uni08A4.medi

	- uni08A5.fina

	- uni08A5.init

	- uni08A5.medi

	- uni08A6.fina

	- uni08A6.init

	- uni08A6.medi

	- uni08A7.fina

	- uni08A7.init

	- uni08A7.medi

	- uni08A8.fina

	- uni08A8.init

	- uni08A8.medi

	- uni08A9.fina

	- uni08A9.init

	- uni08A9.medi

	- uni08AA.fina

	- uni08AB.fina

	- uni08AC.comp

	- uni08AC.fina

	- uni08AE.fina

	- uni08AF.fina

	- uni08AF.init

	- uni08AF.medi

	- uni08B0.fina

	- uni08B0.init

	- uni08B0.medi

	- uni08B1.fina

	- uni08B2.fina

	- uni08B3.fina

	- uni08B3.init

	- uni08B3.medi

	- uni08B4.fina

	- uni08B4.init

	- uni08B4.medi

	- uni08B6.fina

	- uni08B6.init

	- uni08B6.medi

	- uni08B7.fina

	- uni08B7.init

	- uni08B7.medi

	- uni08B8.fina

	- uni08B8.init

	- uni08B8.medi

	- uni08B9.fina

	- uni08BA.fina

	- uni08BA.init

	- uni08BA.medi

	- uni08BB.fina

	- uni08BB.init

	- uni08BB.medi

	- uni08BC.fina

	- uni08BC.init

	- uni08BC.medi

	- uni08BD.fina

	- uni08BD.init

	- uni08BD.medi

	- uni08BE.fina

	- uni08BE.init

	- uni08BE.medi

	- uni08BF.fina

	- uni08BF.init

	- uni08BF.medi

	- uni08C0.fina

	- uni08C0.init

	- uni08C0.medi

	- uni08C1.fina

	- uni08C1.init

	- uni08C1.medi

	- uni08C2.fina

	- uni08C2.init

	- uni08C2.medi

	- uni08C3.fina

	- uni08C3.init

	- uni08C3.medi

	- uni08C4.fina

	- uni08C4.init

	- uni08C4.medi

	- uni08C5.fina

	- uni08C5.init

	- uni08C5.medi

	- uni08C6.fina

	- uni08C6.init

	- uni08C6.medi

	- uni08C7.fina

	- uni08C7.init

	- uni08C7.medi

	- wasla-ar 

	- zero.slash
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: sigma1	Contours detected: 2	Expected: 1

	- Glyph name: uni0469	Contours detected: 5	Expected: 2

	- Glyph name: uni046D	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2

	- Glyph name: uni046F	Contours detected: 1	Expected: 2

	- Glyph name: uni0476	Contours detected: 2	Expected: 3

	- Glyph name: uni0478	Contours detected: 2	Expected: 3

	- Glyph name: uni0479	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

	- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB4	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

	- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

	- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

	- Glyph name: uni1EE0	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 2	Expected: 3

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 1	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni202F	Contours detected: 28	Expected: 0

	- Glyph name: minute	Contours detected: 0	Expected: 1

	- Glyph name: second	Contours detected: 0	Expected: 2

	- Glyph name: uni203D	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2

	- Glyph name: uniFEFF	Contours detected: 25	Expected: 0

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni0469	Contours detected: 5	Expected: 2

	- Glyph name: uni046D	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2

	- Glyph name: uni046F	Contours detected: 1	Expected: 2

	- Glyph name: uni0476	Contours detected: 2	Expected: 3

	- Glyph name: uni0478	Contours detected: 2	Expected: 3

	- Glyph name: uni0479	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

	- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB4	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

	- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

	- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

	- Glyph name: uni1EE0	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 2	Expected: 3

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 1	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni202F	Contours detected: 28	Expected: 0

	- Glyph name: uni203D	Contours detected: 3	Expected: 2

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2 

	- Glyph name: uniFEFF	Contours detected: 25	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* angleright (U+232A): L<<313.0,1348.0>--<487.0,1079.0>> -> L<<487.0,1079.0>--<690.0,768.0>>

	* angleright (U+232A): L<<741.0,563.0>--<371.0,-6.0>> -> L<<371.0,-6.0>--<303.0,-111.0>>

	* psi (U+03C8): L<<471.0,-424.0>--<467.0,-215.0>> -> L<<467.0,-215.0>--<467.0,-6.0>>

	* uni0466 (U+0466): L<<537.0,1108.0>--<492.0,887.0>> -> L<<492.0,887.0>--<412.0,553.0>>

	* uni0466 (U+0466): L<<582.0,891.0>--<555.0,1014.0>> -> L<<555.0,1014.0>--<537.0,1108.0>>

	* uni0466 (U+0466): L<<678.0,489.0>--<582.0,891.0>> -> L<<582.0,891.0>--<555.0,1014.0>>

	* uni046B (U+046B): L<<379.0,756.0>--<485.0,621.0>> -> L<<485.0,621.0>--<528.0,563.0>>

	* uni046C (U+046C): L<<350.0,127.0>--<426.0,479.0>> -> L<<426.0,479.0>--<440.0,543.0>>

	* uni046D (U+046D): L<<346.0,127.0>--<412.0,338.0>> -> L<<412.0,338.0>--<426.0,379.0>>

	* uni046D (U+046D): L<<412.0,338.0>--<426.0,379.0>> -> L<<426.0,379.0>--<446.0,424.0>>

	* uni0475 (U+0475): L<<330.0,756.0>--<487.0,225.0>> -> L<<487.0,225.0>--<510.0,143.0>>

	* uni0477 (U+0477): L<<332.0,756.0>--<492.0,225.0>> -> L<<492.0,225.0>--<512.0,143.0>>

	* uni0478 (U+0478): L<<344.0,1124.0>--<504.0,840.0>> -> L<<504.0,840.0>--<539.0,768.0>>

	* uni0482 (U+0482): L<<432.0,227.0>--<518.0,250.0>> -> L<<518.0,250.0>--<614.0,268.0>>

	* uni0495 (U+0495): L<<428.0,547.0>--<545.0,547.0>> -> L<<545.0,547.0>--<625.0,545.0>>

	* uni0496 (U+0496): L<<479.0,127.0>--<479.0,365.0>> -> L<<479.0,365.0>--<477.0,399.0>>

	* uni0496 (U+0496): L<<598.0,401.0>--<596.0,365.0>> -> L<<596.0,365.0>--<596.0,127.0>>

	* uni0496 (U+0496): L<<700.0,598.0>--<610.0,430.0>> -> L<<610.0,430.0>--<598.0,401.0>>

	* uni0497 (U+0497): L<<477.0,127.0>--<477.0,266.0>> -> L<<477.0,266.0>--<475.0,293.0>>

	* uni0497 (U+0497): L<<594.0,756.0>--<594.0,539.0>> -> L<<594.0,539.0>--<596.0,492.0>>

	* uni0497 (U+0497): L<<684.0,418.0>--<610.0,315.0>> -> L<<610.0,315.0>--<598.0,295.0>>

	* uni0499 (U+0499): L<<444.0,117.0>--<483.0,117.0>> -> L<<483.0,117.0>--<508.0,115.0>>

	* uni049C (U+049C): L<<498.0,813.0>--<526.0,844.0>> -> L<<526.0,844.0>--<748.0,1124.0>>

	* uni049E (U+049E): L<<297.0,942.0>--<297.0,639.0>> -> L<<297.0,639.0>--<299.0,584.0>>

	* uni04A0 (U+04A0): L<<471.0,399.0>--<469.0,365.0>> -> L<<469.0,365.0>--<469.0,127.0>>

	* uni04A0 (U+04A0): L<<602.0,612.0>--<487.0,430.0>> -> L<<487.0,430.0>--<471.0,399.0>>

	* uni04C5 (U+04C5): L<<455.0,1028.0>--<455.0,764.0>> -> L<<455.0,764.0>--<453.0,733.0>>

	* uni04C5 (U+04C5): L<<455.0,764.0>--<453.0,733.0>> -> L<<453.0,733.0>--<453.0,696.0>>

	* uni04CD (U+04CD): L<<815.0,127.0>--<815.0,1055.0>> -> L<<815.0,1055.0>--<813.0,1108.0>>

	* uni0512 (U+0512): L<<455.0,1028.0>--<455.0,764.0>> -> L<<455.0,764.0>--<453.0,733.0>>

	* uni0512 (U+0512): L<<455.0,764.0>--<453.0,733.0>> -> L<<453.0,733.0>--<453.0,696.0>>

	* uni066D (U+066D): L<<469.0,471.0>--<479.0,831.0>> -> L<<479.0,831.0>--<479.0,842.0>>

	* uni06CD (U+06CD): L<<334.0,619.0>--<334.0,618.0>> -> L<<334.0,618.0>--<334.0,616.0>>

	* uni08D4 (U+08D4): L<<289.0,1092.0>--<354.0,1092.0>> -> L<<354.0,1092.0>--<354.0,1092.0>>

	* uni08D4 (U+08D4): L<<354.0,1092.0>--<354.0,1092.0>> -> L<<354.0,1092.0>--<455.0,1092.0>>

	* uni08D4 (U+08D4): L<<791.0,1092.0>--<805.0,1092.0>> -> L<<805.0,1092.0>--<805.0,1092.0>>

	* uni08D4 (U+08D4): L<<805.0,1092.0>--<805.0,1092.0>> -> L<<805.0,1092.0>--<834.0,1092.0>>

	* uni08DB (U+08DB): L<<874.0,1063.0>--<875.0,1063.0>> -> L<<875.0,1063.0>--<875.0,1063.0>>

	* uni08DB (U+08DB): L<<875.0,1063.0>--<875.0,1063.0>> -> L<<875.0,1063.0>--<883.0,1063.0>>

	* uni08DC (U+08DC): L<<337.0,1093.0>--<346.0,1093.0>> -> L<<346.0,1093.0>--<346.0,1093.0>>

	* uni08DC (U+08DC): L<<346.0,1093.0>--<346.0,1093.0>> -> L<<346.0,1093.0>--<348.0,1093.0>>

	* uni08DC (U+08DC): L<<346.0,1093.0>--<348.0,1093.0>> -> L<<348.0,1093.0>--<367.0,1093.0>>

	* uni08DC (U+08DC): L<<650.0,1093.0>--<698.0,1093.0>> -> L<<698.0,1093.0>--<698.0,1093.0>>

	* uni08DE (U+08DE): L<<521.0,1093.0>--<530.0,1093.0>> -> L<<530.0,1093.0>--<530.0,1093.0>>

	* uni08DE (U+08DE): L<<530.0,1093.0>--<530.0,1093.0>> -> L<<530.0,1093.0>--<532.0,1093.0>>

	* uni08DE (U+08DE): L<<530.0,1093.0>--<532.0,1093.0>> -> L<<532.0,1093.0>--<820.0,1093.0>>

	* uni1EC2 (U+1EC2): L<<668.0,1664.0>--<668.0,1661.0>> -> L<<668.0,1661.0>--<668.0,1624.0>>

	* uni203D (U+203D): L<<471.0,618.0>--<467.0,848.0>> -> L<<467.0,848.0>--<459.0,1137.0>>

	* uni203D (U+203D): L<<614.0,1135.0>--<612.0,999.0>> -> L<<612.0,999.0>--<608.0,829.0>>

	* uni2052 (U+2052): L<<156.0,162.0>--<229.0,297.0>> -> L<<229.0,297.0>--<688.0,1145.0>>

	* uni2052 (U+2052): L<<229.0,297.0>--<688.0,1145.0>> -> L<<688.0,1145.0>--<799.0,1348.0>>

	* uni2E18 (U+2E18): L<<428.0,-338.0>--<432.0,-203.0>> -> L<<432.0,-203.0>--<434.0,-33.0>> 

	* uni2E18 (U+2E18): L<<571.0,178.0>--<575.0,-51.0>> -> L<<575.0,-51.0>--<584.0,-340.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Mu (U+039C): L<<815.0,125.0>--<815.0,1102.0>>/B<<815.0,1102.0>-<808.0,1069.0>-<785.5,996.0>> = 11.976132444203333

	* Upsilontonos (U+038E): B<<604.0,1209.0>-<651.0,1144.0>-<670.0,983.0>>/B<<670.0,983.0>-<685.0,1134.0>-<731.0,1204.0>> = 12.40350607454098

	* uni0466 (U+0466): L<<662.0,553.0>--<678.0,489.0>>/L<<678.0,489.0>--<582.0,891.0>> = 0.6052145972453564

	* uni0468 (U+0468): B<<703.5,960.0>-<696.0,1042.0>-<696.0,1108.0>>/B<<696.0,1108.0>-<690.0,960.0>-<673.0,824.0>> = 2.3215305898326966

	* uni0474 (U+0474): B<<459.0,288.5>-<476.0,196.0>-<481.0,143.0>>/B<<481.0,143.0>-<483.0,187.0>-<501.0,286.0>> = 7.991873962473095

	* uni0476 (U+0476): B<<459.0,286.5>-<476.0,195.0>-<481.0,143.0>>/B<<481.0,143.0>-<483.0,180.0>-<497.5,263.5>> = 8.586382616044505

	* uni048A (U+048A): L<<283.0,1124.0>--<283.0,270.0>>/B<<283.0,270.0>-<294.0,329.0>-<412.5,529.5>> = 10.561010691196365

	* uni048A (U+048A): L<<788.0,127.0>--<788.0,981.0>>/B<<788.0,981.0>-<783.0,949.0>-<746.0,878.0>> = 8.880659150520234

	* uni04CD (U+04CD): B<<276.5,1044.0>-<265.0,1086.0>-<260.0,1108.0>>/L<<260.0,1108.0>--<260.0,127.0>> = 12.80426606528674

	* uni04CD (U+04CD): L<<815.0,1055.0>--<813.0,1108.0>>/B<<813.0,1108.0>-<810.0,1087.0>-<794.0,1032.0>> = 10.291181842382318

	* uni0620 (U+0620): B<<587.0,21.0>-<600.0,21.0>-<614.0,20.0>>/B<<614.0,20.0>-<570.0,14.0>-<520.0,12.0>> = 11.850782798400157

	* uni0620 (U+0620): B<<789.0,-81.0>-<726.0,9.0>-<614.0,20.0>>/B<<614.0,20.0>-<725.0,35.0>-<786.0,76.0>> = 13.30532616846234

	* uni08DB (U+08DB): L<<872.0,1028.0>--<872.0,1028.0>>/B<<872.0,1028.0>-<853.0,1029.0>-<841.5,1038.5>> = 3.012787504183286

	* uni08DC (U+08DC): L<<825.0,1044.0>--<825.0,1044.0>>/B<<825.0,1044.0>-<792.0,1045.0>-<778.0,1059.0>> = 1.735704588928346

	* uni08DD (U+08DD): L<<459.0,1047.0>--<459.0,1047.0>>/B<<459.0,1047.0>-<429.0,1049.0>-<415.0,1062.5>> = 3.8140748342903783

	* uni1F59 (U+1F59): B<<629.0,1209.0>-<672.0,1144.0>-<688.0,983.0>>/B<<688.0,983.0>-<702.0,1134.0>-<743.0,1204.0>> = 10.972403989765944

	* uni1F5B (U+1F5B): B<<659.5,1209.0>-<702.0,1144.0>-<719.0,983.0>>/B<<719.0,983.0>-<733.0,1134.0>-<774.0,1204.0>> = 11.324578400118025

	* uni1F5D (U+1F5D): B<<659.5,1209.0>-<702.0,1144.0>-<719.0,983.0>>/B<<719.0,983.0>-<733.0,1134.0>-<774.0,1204.0>> = 11.324578400118025

	* uni1F5F (U+1F5F): B<<649.5,1209.0>-<692.0,1144.0>-<709.0,983.0>>/B<<709.0,983.0>-<723.0,1134.0>-<763.5,1204.0>> = 11.324578400118025

	* uni1FEA (U+1FEA): B<<618.0,1209.0>-<665.0,1144.0>-<684.0,983.0>>/B<<684.0,983.0>-<700.0,1134.0>-<745.5,1204.0>> = 12.778990595616301

	* uni1FEB (U+1FEB): B<<604.0,1209.0>-<651.0,1144.0>-<670.0,983.0>>/B<<670.0,983.0>-<685.0,1134.0>-<731.0,1204.0>> = 12.40350607454098

	* uni200C (U+200C): B<<364.0,360.5>-<350.0,367.0>-<344.0,395.0>>/L<<344.0,395.0>--<344.0,393.0>> = 12.094757077012089 

	* uni202F (U+202F): L<<340.0,698.0>--<338.0,698.0>>/B<<338.0,698.0>-<356.0,694.0>-<376.5,686.5>> = 12.528807709151492 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* phi (U+03C6): L<<471.0,-424.0>--<469.0,-6.0>>

	* uni03DA (U+03DA): L<<471.0,4.0>--<469.0,342.0>>

	* uni03DA (U+03DB): L<<471.0,4.0>--<469.0,342.0>>

	* uni03DF (U+03DF): L<<817.0,-121.0>--<821.0,438.0>>

	* uni08DF (U+08DF): L<<623.0,1094.0>--<768.0,1093.0>>

	* uni08DF (U+08DF): L<<790.0,1046.0>--<643.0,1047.0>>

	* uni0E3F (U+0E3F): L<<459.0,125.0>--<457.0,588.0>>

	* uni0E3F (U+0E3F): L<<586.0,588.0>--<584.0,125.0>>

	* uni1F21 (U+1F21): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F22 (U+1F22): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F23 (U+1F23): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F24 (U+1F24): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F25 (U+1F25): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F26 (U+1F26): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F74 (U+1F74): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F75 (U+1F75): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F90 (U+1F90): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F91 (U+1F91): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F92 (U+1F92): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F93 (U+1F93): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F94 (U+1F94): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F95 (U+1F95): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F96 (U+1F96): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1F97 (U+1F97): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1FC2 (U+1FC2): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1FC3 (U+1FC3): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1FC4 (U+1FC4): L<<866.0,-424.0>--<864.0,516.0>>

	* uni1FC6 (U+1FC6): L<<866.0,-424.0>--<864.0,516.0>> 

	* uni1FC7 (U+1FC7): L<<866.0,-424.0>--<864.0,516.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[22] CourierBadi-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


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


* 🔥 **FAIL** Glyph "uni202F" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
* 🔥 **FAIL** Glyph "uniFEFF" has ink. It needs to be replaced by an empty glyph. [code: has-ink]
</div></details><details><summary>🔥 <b>FAIL:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* 🔥 **FAIL** The following glyph names do not comply with naming conventions: doublestroke-ar, fourabove-ar, fourbelow-ar, gafsarkashabove-ar, kafDotless-ar, kafDotless-ar.fina, miniKeheh-ar, rehabove-ar, stroke-ar, threeabove-ar, threedotshorizontalbelow-ar, twoabove-ar and wasla-ar

 A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not. [code: found-invalid-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ȋ i̒ i҃ i҄ i҅ i҆ i̦̇ i̦̊ i̦̋ ȋ̦ i̦̒ i̦҃ i̦҄ i̦҅ i̦҆ i̧̇ i̧̊ i̧̋ ȋ̧ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 2046 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
* ⚠ **WARN** Font is monospaced but 9 glyphs (0.39%) have a different width. You should check the widths of: ['ellipsis.alt2', 'ellipsis.alt5', 'emdash.alt2', 'emdash.alt3', 'minute', 'second', 'u1F7D9', 'uniFB01', 'uniFB02'] [code: mono-outliers]
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

	- acute.case

	- arabic_root.comp

	- bar.double

	- bigcircle

	- breve.case

	- caron.cap

	- caron.case

	- cedilla.case

	- charbox.comp

	- circumflex.cap

	- circumflex.case

	- colon.alt

	- colon.arabic

	- comma.alt

	- dieresis.cap

	- dieresis.case

	- dotaccent.case

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

	- fourabove-ar

	- fourbelow-ar

	- gafsarkashabove-ar

	- grave.case

	- hungarumlaut.case

	- hyphen.alt

	- idotaccent

	- ittisal.comp

	- kafDotless-ar

	- kafDotless-ar.fina

	- macron.case

	- miniKeheh-ar

	- ogonek.case

	- percent.arabic.comp

	- period.alt

	- period.arabic

	- perthousandzero

	- rehabove-ar

	- ring.case

	- semicolon.alt

	- stroke-ar

	- tail.comp

	- threeabove-ar

	- threedotshorizontalbelow-ar

	- tilde.case

	- twoabove-ar

	- uni0302_acutecomb.cap

	- uni0302_gravecomb.cap

	- uni0302_hookabovecomb.cap

	- uni0302_tildecomb.cap

	- uni0326.case

	- uni0620.fina

	- uni0620.init

	- uni0620.medi

	- uni0622.fina.alt

	- uni0623.fina.alt

	- uni0625.fina.alt

	- uni0627.fina.alt

	- uni0627.fina.short

	- uni0627.fina.shorter

	- uni0627.short

	- uni0627.shorter

	- uni0629.alt

	- uni063B.fina

	- uni063B.init

	- uni063B.medi

	- uni063C.fina

	- uni063C.init

	- uni063C.medi

	- uni063D.fina

	- uni063D.init

	- uni063D.medi

	- uni063E.fina

	- uni063E.init

	- uni063E.medi

	- uni063F.fina

	- uni063F.init

	- uni063F.medi

	- uni0644.medi.short

	- uni066E.fina

	- uni066E.hah

	- uni066E.init

	- uni066E.medi

	- uni066F.fina

	- uni066F.init

	- uni066F.medi

	- uni0671.fina.alt

	- uni0672.fina

	- uni0672.fina.alt

	- uni0673.fina

	- uni0673.fina.alt

	- uni0674.narrow

	- uni0678.init

	- uni067C.fina

	- uni067C.init

	- uni067C.medi

	- uni067D.fina

	- uni067D.init

	- uni067D.medi

	- uni0681.fina

	- uni0681.init

	- uni0681.medi

	- uni0682.fina

	- uni0682.init

	- uni0682.medi

	- uni0685.fina

	- uni0685.init

	- uni0685.medi

	- uni0689.fina

	- uni068A.fina

	- uni068B.fina

	- uni068F.fina

	- uni0690.fina

	- uni0692.fina

	- uni0693.fina

	- uni0694.fina

	- uni0695.fina

	- uni0696.fina

	- uni0697.fina

	- uni0699.fina

	- uni069A.fina

	- uni069A.init

	- uni069A.medi

	- uni069B.fina

	- uni069B.init

	- uni069B.medi

	- uni069C.fina

	- uni069C.init

	- uni069C.medi

	- uni069D.fina

	- uni069D.init

	- uni069D.medi

	- uni069E.fina

	- uni069E.init

	- uni069E.medi

	- uni069F.fina

	- uni069F.init

	- uni069F.medi

	- uni06A0.fina

	- uni06A0.init

	- uni06A0.medi

	- uni06A1.fina

	- uni06A1.init

	- uni06A1.medi

	- uni06A2.fina

	- uni06A2.init

	- uni06A2.medi

	- uni06A3.fina

	- uni06A3.init

	- uni06A3.medi

	- uni06A5.fina

	- uni06A5.init

	- uni06A5.medi

	- uni06A7.fina

	- uni06A7.init

	- uni06A7.medi

	- uni06A8.fina

	- uni06A8.init

	- uni06A8.medi

	- uni06AA.fina

	- uni06AA.init

	- uni06AA.medi

	- uni06AB.fina

	- uni06AB.init

	- uni06AB.medi

	- uni06AC.fina

	- uni06AC.init

	- uni06AC.medi

	- uni06AE.fina

	- uni06AE.init

	- uni06AE.medi

	- uni06B0.fina

	- uni06B0.init

	- uni06B0.medi

	- uni06B2.fina

	- uni06B2.init

	- uni06B2.medi

	- uni06B4.fina

	- uni06B4.init

	- uni06B4.medi

	- uni06B5.fina

	- uni06B5.init

	- uni06B5.medi

	- uni06B6.fina

	- uni06B6.init

	- uni06B6.medi

	- uni06B7.fina

	- uni06B7.init

	- uni06B7.medi

	- uni06B8.fina

	- uni06B8.init

	- uni06B8.medi

	- uni06B9.fina

	- uni06B9.init

	- uni06B9.medi

	- uni06BA.init

	- uni06BA.medi

	- uni06BC.fina

	- uni06BC.init

	- uni06BC.medi

	- uni06BD.fina

	- uni06BD.init

	- uni06BD.medi

	- uni06BE.init.comp

	- uni06BF.fina

	- uni06BF.init

	- uni06BF.medi

	- uni06C2.fina

	- uni06C3.fina

	- uni06C4.fina

	- uni06CA.fina

	- uni06CD.fina

	- uni06CE.fina

	- uni06CE.init

	- uni06CE.medi

	- uni06CF.fina

	- uni06D1.fina

	- uni06D1.init

	- uni06D1.medi

	- uni06D5.fina

	- uni06EE.fina

	- uni06EF.fina

	- uni06F4.urdu

	- uni06F7.urdu

	- uni06FA.fina

	- uni06FA.init

	- uni06FA.medi

	- uni06FB.fina

	- uni06FB.init

	- uni06FB.medi

	- uni06FC.fina

	- uni06FC.init

	- uni06FC.medi

	- uni06FE.fina

	- uni06FE.init

	- uni06FE.medi

	- uni06FF.fina

	- uni06FF.init

	- uni06FF.medi

	- uni0750.fina

	- uni0750.init

	- uni0750.medi

	- uni0751.fina

	- uni0751.init

	- uni0751.medi

	- uni0752.fina

	- uni0752.init

	- uni0752.medi

	- uni0753.fina

	- uni0753.init

	- uni0753.medi

	- uni0754.fina

	- uni0754.init

	- uni0754.medi

	- uni0755.fina

	- uni0755.init

	- uni0755.medi

	- uni0756.fina

	- uni0756.init

	- uni0756.medi

	- uni0757.fina

	- uni0757.init

	- uni0757.medi

	- uni0758.fina

	- uni0758.init

	- uni0758.medi

	- uni0759.fina

	- uni075A.fina

	- uni075B.fina

	- uni075C.fina

	- uni075C.init

	- uni075C.medi

	- uni075D.fina

	- uni075D.init

	- uni075D.medi

	- uni075E.fina

	- uni075E.init

	- uni075E.medi

	- uni075F.fina

	- uni075F.init

	- uni075F.medi

	- uni0760.fina

	- uni0760.init

	- uni0760.medi

	- uni0761.fina

	- uni0761.init

	- uni0761.medi

	- uni0762.fina

	- uni0762.init

	- uni0762.medi

	- uni0763.fina

	- uni0763.init

	- uni0763.medi

	- uni0764.fina

	- uni0764.init

	- uni0764.medi

	- uni0765.fina

	- uni0765.init

	- uni0765.medi

	- uni0766.fina

	- uni0766.init

	- uni0766.medi

	- uni0767.fina

	- uni0767.init

	- uni0767.medi

	- uni0768.fina

	- uni0768.init

	- uni0768.medi

	- uni0769.fina

	- uni0769.init

	- uni0769.medi

	- uni076A.fina

	- uni076A.init

	- uni076A.medi

	- uni076B.fina

	- uni076C.fina

	- uni076D.fina

	- uni076D.init

	- uni076D.medi

	- uni076E.fina

	- uni076E.init

	- uni076E.medi

	- uni076F.fina

	- uni076F.init

	- uni076F.medi

	- uni0770.fina

	- uni0770.init

	- uni0770.medi

	- uni0771.fina

	- uni0772.fina

	- uni0772.init

	- uni0772.medi

	- uni0773.fina

	- uni0773.fina.alt

	- uni0774.fina

	- uni0774.fina.alt

	- uni0775.fina

	- uni0775.init

	- uni0775.medi

	- uni0776.fina

	- uni0776.init

	- uni0776.medi

	- uni0777.fina

	- uni0777.init

	- uni0777.medi

	- uni0778.fina

	- uni0779.fina

	- uni077A.fina

	- uni077B.fina

	- uni077C.fina

	- uni077C.init

	- uni077C.medi

	- uni077D.fina

	- uni077D.init

	- uni077D.medi

	- uni077E.fina

	- uni077E.init

	- uni077E.medi

	- uni077F.fina

	- uni077F.init

	- uni077F.medi

	- uni08A0.fina

	- uni08A0.init

	- uni08A0.medi

	- uni08A1.fina

	- uni08A1.init

	- uni08A1.medi

	- uni08A2.fina

	- uni08A2.init

	- uni08A2.medi

	- uni08A3.fina

	- uni08A3.init

	- uni08A3.medi

	- uni08A4.fina

	- uni08A4.init

	- uni08A4.medi

	- uni08A5.fina

	- uni08A5.init

	- uni08A5.medi

	- uni08A6.fina

	- uni08A6.init

	- uni08A6.medi

	- uni08A7.fina

	- uni08A7.init

	- uni08A7.medi

	- uni08A8.fina

	- uni08A8.init

	- uni08A8.medi

	- uni08A9.fina

	- uni08A9.init

	- uni08A9.medi

	- uni08AA.fina

	- uni08AB.fina

	- uni08AC.comp

	- uni08AC.fina

	- uni08AE.fina

	- uni08AF.fina

	- uni08AF.init

	- uni08AF.medi

	- uni08B0.fina

	- uni08B0.init

	- uni08B0.medi

	- uni08B1.fina

	- uni08B2.fina

	- uni08B3.fina

	- uni08B3.init

	- uni08B3.medi

	- uni08B4.fina

	- uni08B4.init

	- uni08B4.medi

	- uni08B6.fina

	- uni08B6.init

	- uni08B6.medi

	- uni08B7.fina

	- uni08B7.init

	- uni08B7.medi

	- uni08B8.fina

	- uni08B8.init

	- uni08B8.medi

	- uni08B9.fina

	- uni08BA.fina

	- uni08BA.init

	- uni08BA.medi

	- uni08BB.fina

	- uni08BB.init

	- uni08BB.medi

	- uni08BC.fina

	- uni08BC.init

	- uni08BC.medi

	- uni08BD.fina

	- uni08BD.init

	- uni08BD.medi

	- uni08BE.fina

	- uni08BE.init

	- uni08BE.medi

	- uni08BF.fina

	- uni08BF.init

	- uni08BF.medi

	- uni08C0.fina

	- uni08C0.init

	- uni08C0.medi

	- uni08C1.fina

	- uni08C1.init

	- uni08C1.medi

	- uni08C2.fina

	- uni08C2.init

	- uni08C2.medi

	- uni08C3.fina

	- uni08C3.init

	- uni08C3.medi

	- uni08C4.fina

	- uni08C4.init

	- uni08C4.medi

	- uni08C5.fina

	- uni08C5.init

	- uni08C5.medi

	- uni08C6.fina

	- uni08C6.init

	- uni08C6.medi

	- uni08C7.fina

	- uni08C7.init

	- uni08C7.medi

	- wasla-ar 

	- zero.slash
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: sigma1	Contours detected: 2	Expected: 1

	- Glyph name: uni0469	Contours detected: 5	Expected: 2

	- Glyph name: uni046D	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2

	- Glyph name: uni046F	Contours detected: 1	Expected: 2

	- Glyph name: uni0476	Contours detected: 2	Expected: 3

	- Glyph name: uni0478	Contours detected: 2	Expected: 3

	- Glyph name: uni0479	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

	- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB4	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

	- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

	- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

	- Glyph name: uni1EE0	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 2	Expected: 3

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 1	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni202F	Contours detected: 28	Expected: 0

	- Glyph name: minute	Contours detected: 0	Expected: 1

	- Glyph name: second	Contours detected: 0	Expected: 2

	- Glyph name: uni203D	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2

	- Glyph name: uniFEFF	Contours detected: 25	Expected: 0

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni0469	Contours detected: 5	Expected: 2

	- Glyph name: uni046D	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2

	- Glyph name: uni046F	Contours detected: 1	Expected: 2

	- Glyph name: uni0476	Contours detected: 2	Expected: 3

	- Glyph name: uni0478	Contours detected: 2	Expected: 3

	- Glyph name: uni0479	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

	- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB4	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

	- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

	- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

	- Glyph name: uni1EE0	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 2	Expected: 3

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 1	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni202F	Contours detected: 28	Expected: 0

	- Glyph name: uni203D	Contours detected: 3	Expected: 2

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2 

	- Glyph name: uniFEFF	Contours detected: 25	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* angleright (U+232A): L<<551.0,1348.0>--<677.0,1079.0>> -> L<<677.0,1079.0>--<825.0,768.0>>

	* angleright (U+232A): L<<840.0,563.0>--<370.0,-6.0>> -> L<<370.0,-6.0>--<283.0,-111.0>>

	* psi (U+03C8): L<<396.0,-424.0>--<429.0,-215.0>> -> L<<429.0,-215.0>--<466.0,-6.0>>

	* uni0466 (U+0466): L<<732.0,1108.0>--<648.0,887.0>> -> L<<648.0,887.0>--<510.0,553.0>>

	* uni0466 (U+0466): L<<739.0,891.0>--<734.0,1014.0>> -> L<<734.0,1014.0>--<732.0,1108.0>>

	* uni0466 (U+0466): L<<764.0,489.0>--<739.0,891.0>> -> L<<739.0,891.0>--<734.0,1014.0>>

	* uni046B (U+046B): L<<512.0,756.0>--<594.0,621.0>> -> L<<594.0,621.0>--<627.0,563.0>>

	* uni046C (U+046C): L<<372.0,127.0>--<510.0,479.0>> -> L<<510.0,479.0>--<536.0,543.0>>

	* uni046D (U+046D): L<<368.0,127.0>--<472.0,338.0>> -> L<<472.0,338.0>--<493.0,379.0>>

	* uni046D (U+046D): L<<472.0,338.0>--<493.0,379.0>> -> L<<493.0,379.0>--<521.0,424.0>>

	* uni0475 (U+0475): L<<463.0,756.0>--<527.0,225.0>> -> L<<527.0,225.0>--<535.0,143.0>>

	* uni0477 (U+0477): L<<465.0,756.0>--<532.0,225.0>> -> L<<532.0,225.0>--<537.0,143.0>>

	* uni0478 (U+0478): L<<542.0,1124.0>--<652.0,840.0>> -> L<<652.0,840.0>--<674.0,768.0>>

	* uni0478 (U+0478): L<<674.0,768.0>--<717.0,838.0>> -> L<<717.0,838.0>--<929.0,1124.0>>

	* uni0482 (U+0482): L<<472.0,227.0>--<562.0,250.0>> -> L<<562.0,250.0>--<661.0,268.0>>

	* uni0495 (U+0495): L<<524.0,547.0>--<641.0,547.0>> -> L<<641.0,547.0>--<721.0,545.0>>

	* uni0496 (U+0496): L<<501.0,127.0>--<543.0,365.0>> -> L<<543.0,365.0>--<547.0,399.0>>

	* uni0496 (U+0496): L<<669.0,401.0>--<660.0,365.0>> -> L<<660.0,365.0>--<618.0,127.0>>

	* uni0496 (U+0496): L<<805.0,598.0>--<686.0,430.0>> -> L<<686.0,430.0>--<669.0,401.0>>

	* uni0497 (U+0497): L<<499.0,127.0>--<524.0,266.0>> -> L<<524.0,266.0>--<527.0,293.0>>

	* uni0497 (U+0497): L<<727.0,756.0>--<689.0,539.0>> -> L<<689.0,539.0>--<683.0,492.0>>

	* uni0497 (U+0497): L<<758.0,418.0>--<666.0,315.0>> -> L<<666.0,315.0>--<650.0,295.0>>

	* uni0499 (U+0499): L<<465.0,117.0>--<504.0,117.0>> -> L<<504.0,117.0>--<528.0,115.0>>

	* uni049C (U+049C): L<<641.0,813.0>--<675.0,844.0>> -> L<<675.0,844.0>--<946.0,1124.0>>

	* uni049E (U+049E): L<<463.0,942.0>--<410.0,639.0>> -> L<<410.0,639.0>--<402.0,584.0>>

	* uni04A0 (U+04A0): L<<541.0,399.0>--<533.0,365.0>> -> L<<533.0,365.0>--<491.0,127.0>>

	* uni04A0 (U+04A0): L<<710.0,612.0>--<563.0,430.0>> -> L<<563.0,430.0>--<541.0,399.0>>

	* uni04C5 (U+04C5): L<<590.0,764.0>--<582.0,733.0>> -> L<<582.0,733.0>--<576.0,696.0>>

	* uni04C5 (U+04C5): L<<636.0,1028.0>--<590.0,764.0>> -> L<<590.0,764.0>--<582.0,733.0>>

	* uni04CD (U+04CD): L<<837.0,127.0>--<1001.0,1055.0>> -> L<<1001.0,1055.0>--<1008.0,1108.0>>

	* uni0512 (U+0512): L<<590.0,764.0>--<582.0,733.0>> -> L<<582.0,733.0>--<576.0,696.0>>

	* uni0512 (U+0512): L<<636.0,1028.0>--<590.0,764.0>> -> L<<590.0,764.0>--<582.0,733.0>>

	* uni203D (U+203D): L<<580.0,618.0>--<617.0,848.0>> -> L<<617.0,848.0>--<659.0,1137.0>>

	* uni203D (U+203D): L<<814.0,1135.0>--<788.0,999.0>> -> L<<788.0,999.0>--<754.0,829.0>>

	* uni2052 (U+2052): L<<185.0,162.0>--<281.0,297.0>> -> L<<281.0,297.0>--<890.0,1145.0>>

	* uni2052 (U+2052): L<<281.0,297.0>--<890.0,1145.0>> -> L<<890.0,1145.0>--<1037.0,1348.0>>

	* uni2E18 (U+2E18): L<<368.0,-338.0>--<396.0,-203.0>> -> L<<396.0,-203.0>--<428.0,-33.0>> 

	* uni2E18 (U+2E18): L<<602.0,178.0>--<566.0,-51.0>> -> L<<566.0,-51.0>--<524.0,-340.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Mu (U+039C): L<<837.0,125.0>--<1009.0,1102.0>>/B<<1009.0,1102.0>-<999.0,1075.0>-<972.0,1018.5>> = 10.338577199564888

	* Upsilontonos (U+038E): B<<845.0,1044.0>-<845.0,1016.0>-<843.0,983.0>>/B<<843.0,983.0>-<885.0,1134.0>-<943.0,1204.0>> = 12.075449967784303

	* uni0466 (U+0466): L<<760.0,553.0>--<764.0,489.0>>/L<<764.0,489.0>--<739.0,891.0>> = 0.01774687243908398

	* uni0468 (U+0468): B<<872.5,960.0>-<880.0,1042.0>-<891.0,1108.0>>/B<<891.0,1108.0>-<859.0,960.0>-<818.0,824.0>> = 2.738146519354986

	* uni0474 (U+0474): B<<509.0,204.5>-<508.0,169.0>-<506.0,143.0>>/B<<506.0,143.0>-<516.0,187.0>-<551.5,286.0>> = 8.405560710291214

	* uni0476 (U+0476): B<<509.0,275.0>-<509.0,189.0>-<506.0,143.0>>/B<<506.0,143.0>-<515.0,180.0>-<544.0,263.5>> = 9.939910133035372

	* uni048A (U+048A): L<<481.0,1124.0>--<331.0,270.0>>/B<<331.0,270.0>-<351.0,329.0>-<505.5,529.5>> = 8.763742651450915

	* uni048A (U+048A): L<<810.0,127.0>--<961.0,981.0>>/B<<961.0,981.0>-<950.0,949.0>-<900.5,878.0>> = 8.943292419114242

	* uni04CD (U+04CD): B<<460.5,1044.0>-<456.0,1086.0>-<455.0,1108.0>>/L<<455.0,1108.0>--<282.0,127.0>> = 12.603878154295307

	* uni04CD (U+04CD): L<<1001.0,1055.0>--<1008.0,1108.0>>/B<<1008.0,1108.0>-<1001.0,1087.0>-<975.5,1032.0>> = 10.911128384283376

	* uni0620 (U+0620): B<<775.0,-81.0>-<727.0,8.0>-<618.0,20.0>>/B<<618.0,20.0>-<732.0,36.0>-<800.0,76.5>> = 14.271818854558248

	* uni1F59 (U+1F59): B<<864.0,1060.0>-<864.0,1025.0>-<861.0,983.0>>/B<<861.0,983.0>-<902.0,1134.0>-<955.5,1204.0>> = 11.10526901331856

	* uni1F5B (U+1F5B): B<<895.0,1058.0>-<895.0,1023.0>-<892.0,983.0>>/B<<892.0,983.0>-<932.0,1134.0>-<986.0,1204.0>> = 10.547755432741646

	* uni1F5D (U+1F5D): B<<895.0,1058.0>-<895.0,1023.0>-<892.0,983.0>>/B<<892.0,983.0>-<932.0,1134.0>-<986.0,1204.0>> = 10.547755432741646

	* uni1F5F (U+1F5F): B<<885.0,1058.0>-<885.0,1023.0>-<882.0,983.0>>/B<<882.0,983.0>-<922.0,1134.0>-<975.5,1204.0>> = 10.547755432741646

	* uni1FEA (U+1FEA): B<<859.0,1044.0>-<859.0,1016.0>-<857.0,983.0>>/B<<857.0,983.0>-<900.0,1134.0>-<957.5,1204.0>> = 12.427039113664158

	* uni1FEB (U+1FEB): B<<845.0,1044.0>-<845.0,1016.0>-<843.0,983.0>>/B<<843.0,983.0>-<885.0,1134.0>-<943.0,1204.0>> = 12.075449967784303

	* uni202F (U+202F): B<<765.0,996.0>-<756.0,1001.0>-<754.0,1026.0>>/L<<754.0,1026.0>--<754.0,1024.0>> = 4.573921259900818

	* uni202F (U+202F): L<<463.0,698.0>--<461.0,698.0>>/B<<461.0,698.0>-<478.0,694.0>-<497.5,686.5>> = 13.240519915187184 

	* uni202F (U+202F): L<<754.0,1026.0>--<754.0,1024.0>>/B<<754.0,1024.0>-<750.0,1055.0>-<747.0,1086.5>> = 7.352379359892374 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 22 | 23 | 248 | 13 | 169 | 0 |
| 0% | 5% | 5% | 52% | 3% | 36% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
