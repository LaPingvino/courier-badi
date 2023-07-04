## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[21] CourierBadi-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


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
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (1638) and hhea ascent (1827) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 378 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
* ⚠ **WARN** Font is monospaced but 8 glyphs (1.87%) have a different width. You should check the widths of: ['ellipsis.alt2', 'ellipsis.alt5', 'emdash.alt2', 'emdash.alt3', 'fi', 'fl', 'minute', 'second'] [code: mono-outliers]
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
</div></details><details><summary>⚠ <b>WARN:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* ⚠ **WARN** Glyph 0x00A0 is called "nbspace": Change to "uni00A0" [code: not-recommended-00a0]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- colon.alt

	- comma.alt

	- ellipsis.alt1

	- ellipsis.alt2

	- ellipsis.alt3

	- ellipsis.alt4

	- ellipsis.alt5

	- emdash.alt1

	- emdash.alt2

	- emdash.alt3

	- emdash.alt4

	- hyphen.alt

	- idotaccent

	- period.alt 

	- semicolon.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: minute	Contours detected: 0	Expected: 1

	- Glyph name: second	Contours detected: 0	Expected: 2

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: summation	Contours detected: 3	Expected: 1 

	- Glyph name: tbar	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acute.case (unencoded), breve.case (unencoded), caron.case (unencoded), circumflex.case (unencoded), dieresis.case (unencoded), dotaccent.case (unencoded), grave.case (unencoded), hungarumlaut.case (unencoded), macron.case (unencoded), ring.case (unencoded) and tilde.case (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 acutecomb (U+0301), brevecomb (U+0306), caroncomb (U+030C), cedillacmb (U+0327), circumflexcomb (U+0302), commaaccent (U+0326), commaturnedabovecmb (U+0312), diaeresiscomb (U+0308), dotaccentcmb (U+0307), gravecomb (U+0300), hungarumlautcmb (U+030B), macroncomb (U+0304), ogonekcmb (U+0328), ringcmb (U+030A) and tildecomb (U+0303) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* four (U+0034): X=818.0,Y=1187.5 (should be at cap-height 1187?)

	* A (U+0041): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* A (U+0041): X=157.0,Y=-2.0 (should be at baseline 0?)

	* G (U+0047): X=834.0,Y=1188.5 (should be at cap-height 1187?)

	* S (U+0053): X=795.0,Y=1185.0 (should be at cap-height 1187?)

	* V (U+0056): X=1067.0,Y=1189.0 (should be at cap-height 1187?)

	* V (U+0056): X=157.0,Y=1189.0 (should be at cap-height 1187?)

	* W (U+0057): X=1025.5,Y=1187.5 (should be at cap-height 1187?)

	* W (U+0057): X=195.0,Y=1187.5 (should be at cap-height 1187?)

	* r (U+0072): X=1036.0,Y=925.0 (should be at x-height 924?)

	* s (U+0073): X=423.0,Y=2.0 (should be at baseline 0?)

	* s (U+0073): X=773.0,Y=925.5 (should be at x-height 924?)

	* sterling (U+00A3): X=786.0,Y=1186.0 (should be at cap-height 1187?)

	* ordfeminine (U+00AA): X=486.5,Y=1188.0 (should be at cap-height 1187?)

	* Agrave (U+00C0): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Agrave (U+00C0): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Aacute (U+00C1): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Aacute (U+00C1): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Acircumflex (U+00C2): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Acircumflex (U+00C2): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Atilde (U+00C3): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Atilde (U+00C3): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Adieresis (U+00C4): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Adieresis (U+00C4): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Aring (U+00C5): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Aring (U+00C5): X=157.0,Y=-2.0 (should be at baseline 0?)

	* AE (U+00C6): X=76.0,Y=-2.0 (should be at baseline 0?)

	* Amacron (U+0100): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Amacron (U+0100): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Abreve (U+0102): X=888.0,Y=1639.0 (should be at ascender 1638?)

	* Abreve (U+0102): X=340.0,Y=1639.0 (should be at ascender 1638?)

	* Abreve (U+0102): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Abreve (U+0102): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Aogonek (U+0104): X=1067.0,Y=-2.0 (should be at baseline 0?)

	* Aogonek (U+0104): X=157.0,Y=-2.0 (should be at baseline 0?)

	* Ebreve (U+0114): X=898.0,Y=1639.0 (should be at ascender 1638?)

	* Ebreve (U+0114): X=350.0,Y=1639.0 (should be at ascender 1638?)

	* Gcircumflex (U+011C): X=834.0,Y=1188.5 (should be at cap-height 1187?)

	* Gbreve (U+011E): X=834.0,Y=1188.5 (should be at cap-height 1187?)

	* Gbreve (U+011E): X=918.0,Y=1639.0 (should be at ascender 1638?)

	* Gbreve (U+011E): X=370.0,Y=1639.0 (should be at ascender 1638?)

	* Gdotaccent (U+0120): X=834.0,Y=1188.5 (should be at cap-height 1187?)

	* Gcommaaccent (U+0122): X=834.0,Y=1188.5 (should be at cap-height 1187?)

	* Ibreve (U+012C): X=888.0,Y=1639.0 (should be at ascender 1638?)

	* Ibreve (U+012C): X=340.0,Y=1639.0 (should be at ascender 1638?)

	* lacute (U+013A): X=861.0,Y=1637.0 (should be at ascender 1638?)

	* Obreve (U+014E): X=888.0,Y=1639.0 (should be at ascender 1638?)

	* Obreve (U+014E): X=340.0,Y=1639.0 (should be at ascender 1638?)

	* Sacute (U+015A): X=795.0,Y=1185.0 (should be at cap-height 1187?)

	* sacute (U+015B): X=423.0,Y=2.0 (should be at baseline 0?)

	* Scircumflex (U+015C): X=795.0,Y=1185.0 (should be at cap-height 1187?)

	* scircumflex (U+015D): X=423.0,Y=2.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=795.0,Y=1185.0 (should be at cap-height 1187?)

	* scedilla (U+015F): X=423.0,Y=2.0 (should be at baseline 0?)

	* Scaron (U+0160): X=795.0,Y=1185.0 (should be at cap-height 1187?)

	* scaron (U+0161): X=423.0,Y=2.0 (should be at baseline 0?)

	* Ubreve (U+016C): X=888.0,Y=1639.0 (should be at ascender 1638?)

	* Ubreve (U+016C): X=340.0,Y=1639.0 (should be at ascender 1638?)

	* Wcircumflex (U+0174): X=1025.5,Y=1187.5 (should be at cap-height 1187?)

	* Wcircumflex (U+0174): X=195.0,Y=1187.5 (should be at cap-height 1187?)

	* Scommaaccent (U+0218): X=795.0,Y=1185.0 (should be at cap-height 1187?)

	* scommaaccent (U+0219): X=423.0,Y=2.0 (should be at baseline 0?)

	* Wgrave (U+1E80): X=1025.5,Y=1187.5 (should be at cap-height 1187?)

	* Wgrave (U+1E80): X=195.0,Y=1187.5 (should be at cap-height 1187?)

	* Wacute (U+1E82): X=1025.5,Y=1187.5 (should be at cap-height 1187?)

	* Wacute (U+1E82): X=195.0,Y=1187.5 (should be at cap-height 1187?)

	* Wdieresis (U+1E84): X=1025.5,Y=1187.5 (should be at cap-height 1187?)

	* Wdieresis (U+1E84): X=195.0,Y=1187.5 (should be at cap-height 1187?)

	* won (U+20A9): X=195.0,Y=1187.5 (should be at cap-height 1187?)

	* won (U+20A9): X=1025.5,Y=1187.5 (should be at cap-height 1187?)

	* radical (U+221A): X=1047.0,Y=1189.0 (should be at cap-height 1187?) 

	* integral (U+222B): X=689.0,Y=-2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* numbersign (U+0023) contains a short segment B<<502.0,1176.0>-<507.0,1193.0>-<522.5,1201.0>>

	* numbersign (U+0023) contains a short segment B<<522.5,1201.0>-<538.0,1209.0>-<556.0,1209.0>>

	* numbersign (U+0023) contains a short segment B<<896.0,1176.0>-<901.0,1193.0>-<916.5,1201.0>>

	* numbersign (U+0023) contains a short segment B<<916.5,1201.0>-<932.0,1209.0>-<950.0,1209.0>>

	* numbersign (U+0023) contains a short segment B<<726.0,11.0>-<722.0,-6.0>-<706.0,-14.0>>

	* numbersign (U+0023) contains a short segment B<<706.0,-14.0>-<690.0,-22.0>-<672.0,-22.0>>

	* numbersign (U+0023) contains a short segment B<<332.0,11.0>-<328.0,-6.0>-<312.0,-14.0>>

	* numbersign (U+0023) contains a short segment B<<312.0,-14.0>-<296.0,-22.0>-<278.0,-22.0>>

	* at (U+0040) contains a short segment B<<799.0,748.0>-<804.0,759.0>-<822.0,759.0>>

	* at (U+0040) contains a short segment B<<822.0,759.0>-<840.0,759.0>-<858.0,752.0>>

	* at (U+0040) contains a short segment B<<858.0,752.0>-<876.0,745.0>-<888.5,733.0>>

	* at (U+0040) contains a short segment B<<888.5,733.0>-<901.0,721.0>-<897.0,706.0>>

	* A (U+0041) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* N (U+004E) contains a short segment L<<325.0,921.0>--<321.0,921.0>>

	* N (U+004E) contains a short segment L<<903.0,287.0>--<907.0,287.0>>

	* Z (U+005A) contains a short segment B<<167.0,68.0>-<167.0,82.0>-<171.0,92.0>>

	* Z (U+005A) contains a short segment B<<171.0,92.0>-<175.0,102.0>-<181.0,111.0>>

	* Agrave (U+00C0) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Aacute (U+00C1) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Acircumflex (U+00C2) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Atilde (U+00C3) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Adieresis (U+00C4) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Aring (U+00C5) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Ntilde (U+00D1) contains a short segment L<<325.0,921.0>--<321.0,921.0>>

	* Ntilde (U+00D1) contains a short segment L<<903.0,287.0>--<907.0,287.0>>

	* Amacron (U+0100) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Abreve (U+0102) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* Aogonek (U+0104) contains a short segment L<<614.0,1043.0>--<610.0,1043.0>>

	* eogonek (U+0119) contains a short segment B<<1016.0,65.0>-<1007.0,61.0>-<987.5,46.5>>

	* Nacute (U+0143) contains a short segment L<<325.0,921.0>--<321.0,921.0>>

	* Nacute (U+0143) contains a short segment L<<903.0,287.0>--<907.0,287.0>>

	* Ncommaaccent (U+0145) contains a short segment L<<325.0,921.0>--<321.0,921.0>>

	* Ncommaaccent (U+0145) contains a short segment L<<903.0,287.0>--<907.0,287.0>>

	* Ncaron (U+0147) contains a short segment L<<325.0,921.0>--<321.0,921.0>>

	* Ncaron (U+0147) contains a short segment L<<903.0,287.0>--<907.0,287.0>>

	* Eng (U+014A) contains a short segment B<<560.0,-220.0>-<582.0,-215.0>-<604.0,-224.0>>

	* Eng (U+014A) contains a short segment L<<325.0,921.0>--<321.0,921.0>>

	* Eng (U+014A) contains a short segment L<<903.0,287.0>--<907.0,287.0>>

	* Zacute (U+0179) contains a short segment B<<167.0,68.0>-<167.0,82.0>-<171.0,92.0>>

	* Zacute (U+0179) contains a short segment B<<171.0,92.0>-<175.0,102.0>-<181.0,111.0>>

	* Zdotaccent (U+017B) contains a short segment B<<167.0,68.0>-<167.0,82.0>-<171.0,92.0>>

	* Zdotaccent (U+017B) contains a short segment B<<171.0,92.0>-<175.0,102.0>-<181.0,111.0>>

	* Zcaron (U+017D) contains a short segment B<<167.0,68.0>-<167.0,82.0>-<171.0,92.0>>

	* Zcaron (U+017D) contains a short segment B<<171.0,92.0>-<175.0,102.0>-<181.0,111.0>>

	* Delta (U+0394) contains a short segment L<<617.0,1022.0>--<615.0,1022.0>>

	* summation (U+2211) contains a short segment L<<613.0,1797.0>--<614.0,1797.0>>

	* summation (U+2211) contains a short segment L<<614.0,1797.0>--<614.0,1796.0>>

	* summation (U+2211) contains a short segment L<<614.0,1796.0>--<613.0,1796.0>>

	* summation (U+2211) contains a short segment L<<613.0,1796.0>--<613.0,1797.0>>

	* summation (U+2211) contains a short segment B<<197.0,1070.0>-<190.0,1079.0>-<187.5,1091.5>>

	* summation (U+2211) contains a short segment B<<187.5,1091.5>-<185.0,1104.0>-<185.0,1119.0>>

	* summation (U+2211) contains a short segment L<<613.0,-837.0>--<614.0,-837.0>>

	* summation (U+2211) contains a short segment L<<614.0,-837.0>--<614.0,-838.0>>

	* summation (U+2211) contains a short segment L<<614.0,-838.0>--<613.0,-838.0>> 

	* summation (U+2211) contains a short segment L<<613.0,-838.0>--<613.0,-837.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[21] CourierBadi-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


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
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (1638) and hhea ascent (1827) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̊ j̦̋ ǰ̦ j̦̒ j̧̀ j̧́ j̧̃ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** The OpenType spec recomments at https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table that hhea.numberOfHMetrics be set to 3 but this font has 399 instead.
Please read https://github.com/fonttools/fonttools/issues/3014 to decide whether this makes sense for your font. [code: bad-numberOfHMetrics]
* ⚠ **WARN** Font is monospaced but 9 glyphs (2.10%) have a different width. You should check the widths of: ['ellipsis.alt2', 'ellipsis.alt5', 'emdash.alt2', 'emdash.alt3', 'fi', 'fl', 'minute', 'second', 'u1F7D9'] [code: mono-outliers]
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
</div></details><details><summary>⚠ <b>WARN:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* ⚠ **WARN** Glyph 0x00A0 is called "nbspace": Change to "uni00A0" [code: not-recommended-00a0]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- bar.double

	- colon.alt

	- comma.alt

	- ellipsis.alt1

	- ellipsis.alt2

	- ellipsis.alt3

	- ellipsis.alt4

	- ellipsis.alt5

	- emdash.alt1

	- emdash.alt2

	- emdash.alt3

	- emdash.alt4

	- hyphen.alt

	- period.alt 

	- semicolon.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: minute	Contours detected: 0	Expected: 1

	- Glyph name: second	Contours detected: 0	Expected: 2

	- Glyph name: summation	Contours detected: 3	Expected: 1

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2 

	- Glyph name: summation	Contours detected: 3	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acute.case (unencoded), breve.case (unencoded), caron.case (unencoded), circumflex.case (unencoded), dieresis.case (unencoded), dotaccent.case (unencoded), grave.case (unencoded), hungarumlaut.case (unencoded), macron.case (unencoded), ring.case (unencoded) and tilde.case (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 acutecomb (U+0301), brevecomb (U+0306), caroncomb (U+030C), cedillacmb (U+0327), circumflexcomb (U+0302), commaaccent (U+0326), commaturnedabovecmb (U+0312), diaeresiscomb (U+0308), dotaccentcmb (U+0307), gravecomb (U+0300), hungarumlautcmb (U+030B), macroncomb (U+0304), ogonekcmb (U+0328), ringcmb (U+030A) and tildecomb (U+0303) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three (U+0033): X=539.0,Y=1188.0 (should be at cap-height 1187?)

	* four (U+0034): X=956.0,Y=1187.5 (should be at cap-height 1187?)

	* seven (U+0037): X=382.0,Y=-1.5 (should be at baseline 0?)

	* G (U+0047): X=957.0,Y=1186.5 (should be at cap-height 1187?)

	* G (U+0047): X=792.5,Y=-0.5 (should be at baseline 0?)

	* Q (U+0051): X=723.0,Y=2.0 (should be at baseline 0?)

	* r (U+0072): X=1119.0,Y=925.0 (should be at x-height 924?)

	* s (U+0073): X=850.0,Y=925.5 (should be at x-height 924?)

	* s (U+0073): X=361.5,Y=1.5 (should be at baseline 0?)

	* sterling (U+00A3): X=917.5,Y=1186.0 (should be at cap-height 1187?)

	* ordfeminine (U+00AA): X=961.5,Y=1188.0 (should be at cap-height 1187?)

	* ordfeminine (U+00AA): X=1065.5,Y=1188.0 (should be at cap-height 1187?)

	* twosuperior (U+00B2): X=456.0,Y=1188.0 (should be at cap-height 1187?)

	* aring (U+00E5): X=651.5,Y=1185.5 (should be at cap-height 1187?)

	* Dcaron (U+010E): X=1071.5,Y=1636.0 (should be at ascender 1638?)

	* Dcaron (U+010E): X=445.0,Y=1637.0 (should be at ascender 1638?)

	* Ecaron (U+011A): X=1126.5,Y=1636.0 (should be at ascender 1638?)

	* Ecaron (U+011A): X=500.0,Y=1637.0 (should be at ascender 1638?)

	* Gcircumflex (U+011C): X=957.0,Y=1186.5 (should be at cap-height 1187?)

	* Gcircumflex (U+011C): X=792.5,Y=-0.5 (should be at baseline 0?)

	* Gbreve (U+011E): X=957.0,Y=1186.5 (should be at cap-height 1187?)

	* Gbreve (U+011E): X=792.5,Y=-0.5 (should be at baseline 0?)

	* Gdotaccent (U+0120): X=957.0,Y=1186.5 (should be at cap-height 1187?)

	* Gdotaccent (U+0120): X=792.5,Y=-0.5 (should be at baseline 0?)

	* Gcommaaccent (U+0122): X=957.0,Y=1186.5 (should be at cap-height 1187?)

	* Gcommaaccent (U+0122): X=792.5,Y=-0.5 (should be at baseline 0?)

	* Ncaron (U+0147): X=1121.5,Y=1636.0 (should be at ascender 1638?)

	* Ncaron (U+0147): X=495.0,Y=1637.0 (should be at ascender 1638?)

	* Rcaron (U+0158): X=1116.5,Y=1636.0 (should be at ascender 1638?)

	* Rcaron (U+0158): X=490.0,Y=1637.0 (should be at ascender 1638?)

	* sacute (U+015B): X=361.5,Y=1.5 (should be at baseline 0?)

	* scircumflex (U+015D): X=361.5,Y=1.5 (should be at baseline 0?)

	* scedilla (U+015F): X=361.5,Y=1.5 (should be at baseline 0?)

	* scaron (U+0161): X=361.5,Y=1.5 (should be at baseline 0?)

	* Tcaron (U+0164): X=1111.5,Y=1636.0 (should be at ascender 1638?)

	* Tcaron (U+0164): X=485.0,Y=1637.0 (should be at ascender 1638?)

	* uring (U+016F): X=723.0,Y=1185.0 (should be at cap-height 1187?)

	* uogonek (U+0173): X=937.0,Y=1.0 (should be at baseline 0?)

	* Zcaron (U+017D): X=1121.5,Y=1636.0 (should be at ascender 1638?)

	* Zcaron (U+017D): X=495.0,Y=1637.0 (should be at ascender 1638?)

	* scommaaccent (U+0219): X=361.5,Y=1.5 (should be at baseline 0?)

	* ring (U+02DA): X=755.0,Y=1185.0 (should be at cap-height 1187?)

	* ringcmb (U+030A): X=755.0,Y=1185.0 (should be at cap-height 1187?) 

	* radical (U+221A): X=1187.0,Y=1185.0 (should be at cap-height 1187?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* seven (U+0037) contains a short segment B<<1156.0,1119.0>-<1154.0,1106.0>-<1150.0,1095.5>>

	* seven (U+0037) contains a short segment B<<1150.0,1095.5>-<1146.0,1085.0>-<1143.0,1079.0>>

	* A (U+0041) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* N (U+004E) contains a short segment L<<419.0,931.0>--<415.0,931.0>>

	* N (U+004E) contains a short segment L<<882.0,277.0>--<886.0,277.0>>

	* W (U+0057) contains a short segment B<<610.0,845.0>-<621.0,865.0>-<638.5,875.0>>

	* Z (U+005A) contains a short segment B<<118.0,68.0>-<120.0,81.0>-<126.5,91.5>>

	* Z (U+005A) contains a short segment B<<126.5,91.5>-<133.0,102.0>-<140.0,111.0>>

	* Agrave (U+00C0) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Aacute (U+00C1) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Acircumflex (U+00C2) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Atilde (U+00C3) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Adieresis (U+00C4) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Aring (U+00C5) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Ntilde (U+00D1) contains a short segment L<<419.0,931.0>--<415.0,931.0>>

	* Ntilde (U+00D1) contains a short segment L<<882.0,277.0>--<886.0,277.0>>

	* Amacron (U+0100) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* Abreve (U+0102) contains a short segment L<<733.0,1043.0>--<729.0,1043.0>>

	* lslash (U+0142) contains a short segment B<<592.0,274.5>-<590.0,258.0>-<590.0,243.0>>

	* Nacute (U+0143) contains a short segment L<<419.0,931.0>--<415.0,931.0>>

	* Nacute (U+0143) contains a short segment L<<882.0,277.0>--<886.0,277.0>>

	* Ncommaaccent (U+0145) contains a short segment L<<419.0,931.0>--<415.0,931.0>>

	* Ncommaaccent (U+0145) contains a short segment L<<882.0,277.0>--<886.0,277.0>>

	* Ncaron (U+0147) contains a short segment L<<419.0,931.0>--<415.0,931.0>>

	* Ncaron (U+0147) contains a short segment L<<882.0,277.0>--<886.0,277.0>>

	* Eng (U+014A) contains a short segment B<<425.0,-360.0>-<399.0,-347.0>-<393.0,-325.5>>

	* Eng (U+014A) contains a short segment B<<445.0,-223.0>-<468.0,-215.0>-<488.0,-224.0>>

	* Eng (U+014A) contains a short segment L<<419.0,931.0>--<415.0,931.0>>

	* Eng (U+014A) contains a short segment L<<882.0,277.0>--<886.0,277.0>>

	* Wcircumflex (U+0174) contains a short segment B<<610.0,845.0>-<621.0,865.0>-<638.5,875.0>>

	* Zacute (U+0179) contains a short segment B<<118.0,68.0>-<120.0,81.0>-<126.5,91.5>>

	* Zacute (U+0179) contains a short segment B<<126.5,91.5>-<133.0,102.0>-<140.0,111.0>>

	* Zdotaccent (U+017B) contains a short segment B<<118.0,68.0>-<120.0,81.0>-<126.5,91.5>>

	* Zdotaccent (U+017B) contains a short segment B<<126.5,91.5>-<133.0,102.0>-<140.0,111.0>>

	* Zcaron (U+017D) contains a short segment B<<118.0,68.0>-<120.0,81.0>-<126.5,91.5>>

	* Zcaron (U+017D) contains a short segment B<<126.5,91.5>-<133.0,102.0>-<140.0,111.0>>

	* Delta (U+0394) contains a short segment L<<732.0,1022.0>--<730.0,1022.0>>

	* Omega (U+03A9) contains a short segment B<<624.0,78.0>-<628.0,101.0>-<634.5,118.0>>

	* Omega (U+03A9) contains a short segment B<<634.5,118.0>-<641.0,135.0>-<652.0,142.0>>

	* Omega (U+03A9) contains a short segment B<<472.0,143.0>-<480.0,136.0>-<481.0,118.5>>

	* Omega (U+03A9) contains a short segment B<<481.0,118.5>-<482.0,101.0>-<478.0,78.0>>

	* Wgrave (U+1E80) contains a short segment B<<610.0,845.0>-<621.0,865.0>-<638.5,875.0>>

	* Wacute (U+1E82) contains a short segment B<<610.0,845.0>-<621.0,865.0>-<638.5,875.0>>

	* Wdieresis (U+1E84) contains a short segment B<<610.0,845.0>-<621.0,865.0>-<638.5,875.0>>

	* summation (U+2211) contains a short segment L<<860.0,1797.0>--<861.0,1797.0>>

	* summation (U+2211) contains a short segment L<<861.0,1797.0>--<861.0,1796.0>>

	* summation (U+2211) contains a short segment L<<861.0,1796.0>--<860.0,1796.0>>

	* summation (U+2211) contains a short segment L<<860.0,1796.0>--<860.0,1797.0>>

	* summation (U+2211) contains a short segment B<<316.0,1070.0>-<310.0,1079.0>-<310.0,1091.5>>

	* summation (U+2211) contains a short segment B<<310.0,1091.5>-<310.0,1104.0>-<312.0,1119.0>>

	* summation (U+2211) contains a short segment L<<395.0,-837.0>--<396.0,-837.0>>

	* summation (U+2211) contains a short segment L<<396.0,-837.0>--<396.0,-838.0>>

	* summation (U+2211) contains a short segment L<<396.0,-838.0>--<395.0,-838.0>> 

	* summation (U+2211) contains a short segment L<<395.0,-838.0>--<395.0,-837.0>> [code: found-short-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 16 | 26 | 242 | 13 | 178 | 0 |
| 0% | 3% | 5% | 51% | 3% | 37% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
