## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[26] CourierBadi-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-glyf-non-transformed-duplicate-components">opentype/glyf_non_transformed_duplicate_components</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs have duplicate components which have the same x,y coordinates:
* {'glyph': 'second', 'component': 'minute', 'x': 0, 'y': 0}</p>
 [code: found-duplicates]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+03DF: GREEK SMALL LETTER KOPPA</td>
<td align="left">U+03DE: GREEK LETTER KOPPA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs have no contours even though they were expected to have some:</p>
<pre><code>- Glyph name: minute	Expected: 1

- Glyph name: second	Expected: 2
</code></pre>
 [code: no-contour]



* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

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

- Glyph name: uni1EE1	Contours detected: 2	Expected: 3

- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

- Glyph name: uni1EED	Contours detected: 3	Expected: 2

- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

- Glyph name: uni202F	Contours detected: 28	Expected: 0

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: lira	Contours detected: 2	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2

- Glyph name: uniFEFF	Contours detected: 25	Expected: 0

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

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

- Glyph name: uni1EE1	Contours detected: 2	Expected: 3

- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

- Glyph name: uni1EED	Contours detected: 3	Expected: 2

- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

- Glyph name: uni202F	Contours detected: 28	Expected: 0

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2

- Glyph name: uniFEFF	Contours detected: 25	Expected: 0
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 2087, but got 1827 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 1364, but got 838 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Font contains '.notdef' as its first glyph? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-glyphs">mandatory_glyphs</a></summary>
    <div>







* 🔥 **FAIL** <p>The '.notdef' glyph should contain a drawing, but it is blank.</p>
 [code: notdef-is-blank]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 Metrics match hhea Metrics. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#os2-metrics-match-hhea">os2_metrics_match_hhea</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 sTypoAscender (1638) and hhea ascent (1827) must be equal.</p>
 [code: ascender]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: doublestroke-ar, fourabove-ar, fourbelow-ar, gafsarkashabove-ar, kafDotless-ar, kafDotless-ar.fina, miniKeheh-ar, rehabove-ar, stroke-ar, threeabove-ar, threedotshorizontalbelow-ar, twoabove-ar and wasla-ar</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Whitespace glyphs have ink? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-ink">whitespace_ink</a></summary>
    <div>







* 🔥 **FAIL** <p>Glyph 'uni202F' has ink. It needs to be replaced by an empty glyph.</p>
 [code: has-ink]



* 🔥 **FAIL** <p>Glyph 'uniFEFF' has ink. It needs to be replaced by an empty glyph.</p>
 [code: has-ink]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ʼ</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following mark characters are missing from the font: ̛</td>
<td align="left">vi_Latn (Vietnamese)</td>
</tr>
<tr>
<td align="left">Positional forms for Arabic letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ځ‍' with features: -init and shaping the text 'ځ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'څ‍' with features: -init and shaping the text 'څ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ځ‍' with features: -medi and shaping the text '‍ځ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍څ‍' with features: -medi and shaping the text '‍څ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ځ' with features: -fina and shaping the text '‍ځ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍څ' with features: -fina and shaping the text '‍څ', the output is expected to be different, but was the same</td>
<td align="left">ps_Arab (Pashto)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ꙗ, ꙗ, ꙋ, ꙍ, ꙃ, Ꙍ, Ꙃ, ꙁ, Ꙁ, Ꙋ</td>
<td align="left">cu_Cyrl (Church Slavic)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ʻ</td>
<td align="left">en_Latn (English)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ȟ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǩ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ʒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǯ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ȟ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǩ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ʒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǯ</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Copyright notices match canonical pattern in fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-copyright">googlefonts/font_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>Name Table entry: Copyright notices should match a pattern similar to:</p>
<p>&quot;Copyright 2020 The Familyname Project Authors (git url)&quot;</p>
<p>But instead we have got:</p>
<p>&quot;Copyright 2023 Joop Kiefte (<a href="https://github.com/LaPingvino/courier-badi">https://github.com/LaPingvino/courier-badi</a>)&quot;</p>
 [code: bad-notice-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 1 meaning that:</p>
<ul>
<li>There are reserved bits set, which indicates an invalid setting.</li>
</ul>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;Version 0.601; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* sigma1 (U+03C2): B&lt;&lt;978.5,854.0&gt;-&lt;980.0,845.0&gt;-&lt;977.0,852.0&gt;&gt; has the same coordinates as a previous segment.

* uni203B (U+203B): B&lt;&lt;459.0,839.0&gt;-&lt;471.0,820.0&gt;-&lt;490.0,808.0&gt;&gt; has the same coordinates as a previous segment.

* uni203B (U+203B): B&lt;&lt;719.0,579.0&gt;-&lt;730.0,562.0&gt;-&lt;747.0,551.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#typoascender-exceeds-Agrave">typoascender_exceeds_Agrave</a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2.sTypoAscender value should be greater than 1685.1363636363637, but got 1638 instead</p>
 [code: typoAscender]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Threedotsinverted.alt.comp

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

- uni066E.hah

- uni0671.fina.alt

- uni0672.fina.alt

- uni0673.fina.alt

- uni0674.narrow

- uni0678.init

- uni0681.fina

- uni0681.init

- uni0681.medi

- uni0682.fina

- uni0682.init

- uni0682.medi

- uni0685.fina

- uni0685.init

- uni0685.medi

- uni06BE.init.comp

- uni06BF.fina

- uni06BF.init

- uni06BF.medi

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
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, cherokee, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, syriac, duployan, coptic, canadian-aboriginal, hebrew, tifinagh, old-permic, tai-le, todhri, malayalam</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: sunuwar, caucasian-albanian, syriac, gothic, tifinagh, cherokee, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+034F COMBINING GRAPHEME JOINER: not included in any glyphset definition</li>
<li>U+0600 ARABIC NUMBER SIGN: try adding arabic</li>
<li>U+0601 ARABIC SIGN SANAH: try adding arabic</li>
<li>U+0602 ARABIC FOOTNOTE MARKER: try adding arabic</li>
<li>U+0603 ARABIC SIGN SAFHA: try adding arabic</li>
<li>U+0604 ARABIC SIGN SAMVAT: try adding arabic</li>
<li>U+0605 ARABIC NUMBER MARK ABOVE: try adding arabic</li>
<li>U+0606 ARABIC-INDIC CUBE ROOT: try adding arabic</li>
<li>U+0607 ARABIC-INDIC FOURTH ROOT: try adding arabic</li>
<li>U+0608 ARABIC RAY: try adding arabic</li>
<li>U+0609 ARABIC-INDIC PER MILLE SIGN: try adding arabic</li>
<li>U+060A ARABIC-INDIC PER TEN THOUSAND SIGN: try adding arabic</li>
<li>U+060B AFGHANI SIGN: try adding arabic</li>
<li>U+060C ARABIC COMMA: try adding one of: syriac, arabic, nko, yezidi, hanifi-rohingya, garay, thaana</li>
<li>U+060D ARABIC DATE SEPARATOR: try adding arabic</li>
<li>U+060E ARABIC POETIC VERSE SIGN: try adding arabic</li>
<li>U+060F ARABIC SIGN MISRA: try adding arabic</li>
<li>U+0610 ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM: try adding arabic</li>
<li>U+0611 ARABIC SIGN ALAYHE ASSALLAM: try adding arabic</li>
<li>U+0612 ARABIC SIGN RAHMATULLAH ALAYHE: try adding arabic</li>
<li>U+0613 ARABIC SIGN RADI ALLAHOU ANHU: try adding arabic</li>
<li>U+0614 ARABIC SIGN TAKHALLUS: try adding arabic</li>
<li>U+0615 ARABIC SMALL HIGH TAH: try adding arabic</li>
<li>U+0616 ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH: try adding arabic</li>
<li>U+0617 ARABIC SMALL HIGH ZAIN: try adding arabic</li>
<li>U+0618 ARABIC SMALL FATHA: try adding arabic</li>
<li>U+0619 ARABIC SMALL DAMMA: try adding arabic</li>
<li>U+061A ARABIC SMALL KASRA: try adding arabic</li>
<li>U+061B ARABIC SEMICOLON: try adding one of: syriac, arabic, nko, yezidi, hanifi-rohingya, garay, thaana</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: syriac, arabic, thaana</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: syriac, arabic, nko, yezidi, hanifi-rohingya, adlam, garay, thaana</li>
<li>U+0620 ARABIC LETTER KASHMIRI YEH: try adding arabic</li>
<li>U+0621 ARABIC LETTER HAMZA: try adding one of: syriac, arabic</li>
<li>U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE: try adding arabic</li>
<li>U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW: try adding arabic</li>
<li>U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0627 ARABIC LETTER ALEF: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+0628 ARABIC LETTER BEH: try adding arabic</li>
<li>U+0629 ARABIC LETTER TEH MARBUTA: try adding arabic</li>
<li>U+062A ARABIC LETTER TEH: try adding arabic</li>
<li>U+062B ARABIC LETTER THEH: try adding arabic</li>
<li>U+062C ARABIC LETTER JEEM: try adding arabic</li>
<li>U+062D ARABIC LETTER HAH: try adding arabic</li>
<li>U+062E ARABIC LETTER KHAH: try adding arabic</li>
<li>U+062F ARABIC LETTER DAL: try adding arabic</li>
<li>U+0630 ARABIC LETTER THAL: try adding arabic</li>
<li>U+0631 ARABIC LETTER REH: try adding arabic</li>
<li>U+0632 ARABIC LETTER ZAIN: try adding arabic</li>
<li>U+0633 ARABIC LETTER SEEN: try adding arabic</li>
<li>U+0634 ARABIC LETTER SHEEN: try adding arabic</li>
<li>U+0635 ARABIC LETTER SAD: try adding arabic</li>
<li>U+0636 ARABIC LETTER DAD: try adding arabic</li>
<li>U+0637 ARABIC LETTER TAH: try adding arabic</li>
<li>U+0638 ARABIC LETTER ZAH: try adding arabic</li>
<li>U+0639 ARABIC LETTER AIN: try adding arabic</li>
<li>U+063A ARABIC LETTER GHAIN: try adding arabic</li>
<li>U+063B ARABIC LETTER KEHEH WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+063C ARABIC LETTER KEHEH WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+063D ARABIC LETTER FARSI YEH WITH INVERTED V: try adding arabic</li>
<li>U+063E ARABIC LETTER FARSI YEH WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+063F ARABIC LETTER FARSI YEH WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+0640 ARABIC TATWEEL: try adding one of: syriac, arabic, sogdian, manichaean, hanifi-rohingya, psalter-pahlavi, adlam, old-uyghur, mandaic</li>
<li>U+0641 ARABIC LETTER FEH: try adding arabic</li>
<li>U+0642 ARABIC LETTER QAF: try adding arabic</li>
<li>U+0643 ARABIC LETTER KAF: try adding arabic</li>
<li>U+0644 ARABIC LETTER LAM: try adding arabic</li>
<li>U+0645 ARABIC LETTER MEEM: try adding arabic</li>
<li>U+0646 ARABIC LETTER NOON: try adding arabic</li>
<li>U+0647 ARABIC LETTER HEH: try adding arabic</li>
<li>U+0648 ARABIC LETTER WAW: try adding arabic</li>
<li>U+0649 ARABIC LETTER ALEF MAKSURA: try adding arabic</li>
<li>U+064A ARABIC LETTER YEH: try adding arabic</li>
<li>U+064B ARABIC FATHATAN: try adding one of: syriac, arabic</li>
<li>U+064C ARABIC DAMMATAN: try adding one of: syriac, arabic</li>
<li>U+064D ARABIC KASRATAN: try adding one of: syriac, arabic</li>
<li>U+064E ARABIC FATHA: try adding one of: syriac, arabic</li>
<li>U+064F ARABIC DAMMA: try adding one of: syriac, arabic</li>
<li>U+0650 ARABIC KASRA: try adding one of: syriac, arabic</li>
<li>U+0651 ARABIC SHADDA: try adding one of: syriac, arabic</li>
<li>U+0652 ARABIC SUKUN: try adding one of: syriac, arabic</li>
<li>U+0653 ARABIC MADDAH ABOVE: try adding one of: syriac, arabic</li>
<li>U+0654 ARABIC HAMZA ABOVE: try adding one of: syriac, arabic</li>
<li>U+0655 ARABIC HAMZA BELOW: try adding one of: syriac, arabic</li>
<li>U+0656 ARABIC SUBSCRIPT ALEF: try adding arabic</li>
<li>U+0657 ARABIC INVERTED DAMMA: try adding arabic</li>
<li>U+0658 ARABIC MARK NOON GHUNNA: try adding arabic</li>
<li>U+0659 ARABIC ZWARAKAY: try adding arabic</li>
<li>U+065A ARABIC VOWEL SIGN SMALL V ABOVE: try adding arabic</li>
<li>U+065B ARABIC VOWEL SIGN INVERTED SMALL V ABOVE: try adding arabic</li>
<li>U+065C ARABIC VOWEL SIGN DOT BELOW: try adding arabic</li>
<li>U+065D ARABIC REVERSED DAMMA: try adding arabic</li>
<li>U+065E ARABIC FATHA WITH TWO DOTS: try adding arabic</li>
<li>U+065F ARABIC WAVY HAMZA BELOW: try adding arabic</li>
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, hanifi-rohingya, thaana</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: syriac, arabic, indic-siyaq-numbers, yezidi, thaana</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: nko, arabic, syriac, thaana</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: syriac, arabic, thaana</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: syriac, arabic, thaana</li>
<li>U+066D ARABIC FIVE POINTED STAR: try adding arabic</li>
<li>U+066E ARABIC LETTER DOTLESS BEH: try adding arabic</li>
<li>U+066F ARABIC LETTER DOTLESS QAF: try adding arabic</li>
<li>U+0670 ARABIC LETTER SUPERSCRIPT ALEF: try adding one of: syriac, arabic</li>
<li>U+0671 ARABIC LETTER ALEF WASLA: try adding arabic</li>
<li>U+0672 ARABIC LETTER ALEF WITH WAVY HAMZA ABOVE: try adding arabic</li>
<li>U+0673 ARABIC LETTER ALEF WITH WAVY HAMZA BELOW: try adding arabic</li>
<li>U+0674 ARABIC LETTER HIGH HAMZA: try adding arabic</li>
<li>U+0675 ARABIC LETTER HIGH HAMZA ALEF: try adding arabic</li>
<li>U+0676 ARABIC LETTER HIGH HAMZA WAW: try adding arabic</li>
<li>U+0677 ARABIC LETTER U WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0678 ARABIC LETTER HIGH HAMZA YEH: try adding arabic</li>
<li>U+0679 ARABIC LETTER TTEH: try adding arabic</li>
<li>U+067A ARABIC LETTER TTEHEH: try adding arabic</li>
<li>U+067B ARABIC LETTER BEEH: try adding arabic</li>
<li>U+067C ARABIC LETTER TEH WITH RING: try adding arabic</li>
<li>U+067D ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS: try adding arabic</li>
<li>U+067E ARABIC LETTER PEH: try adding arabic</li>
<li>U+067F ARABIC LETTER TEHEH: try adding arabic</li>
<li>U+0680 ARABIC LETTER BEHEH: try adding arabic</li>
<li>U+0681 ARABIC LETTER HAH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0682 ARABIC LETTER HAH WITH TWO DOTS VERTICAL ABOVE: try adding arabic</li>
<li>U+0683 ARABIC LETTER NYEH: try adding arabic</li>
<li>U+0684 ARABIC LETTER DYEH: try adding arabic</li>
<li>U+0685 ARABIC LETTER HAH WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+0686 ARABIC LETTER TCHEH: try adding arabic</li>
<li>U+0687 ARABIC LETTER TCHEHEH: try adding arabic</li>
<li>U+0688 ARABIC LETTER DDAL: try adding arabic</li>
<li>U+0689 ARABIC LETTER DAL WITH RING: try adding arabic</li>
<li>U+068A ARABIC LETTER DAL WITH DOT BELOW: try adding arabic</li>
<li>U+068B ARABIC LETTER DAL WITH DOT BELOW AND SMALL TAH: try adding arabic</li>
<li>U+068C ARABIC LETTER DAHAL: try adding arabic</li>
<li>U+068D ARABIC LETTER DDAHAL: try adding arabic</li>
<li>U+068E ARABIC LETTER DUL: try adding arabic</li>
<li>U+068F ARABIC LETTER DAL WITH THREE DOTS ABOVE DOWNWARDS: try adding arabic</li>
<li>U+0690 ARABIC LETTER DAL WITH FOUR DOTS ABOVE: try adding arabic</li>
<li>U+0691 ARABIC LETTER RREH: try adding arabic</li>
<li>U+0692 ARABIC LETTER REH WITH SMALL V: try adding arabic</li>
<li>U+0693 ARABIC LETTER REH WITH RING: try adding arabic</li>
<li>U+0694 ARABIC LETTER REH WITH DOT BELOW: try adding arabic</li>
<li>U+0695 ARABIC LETTER REH WITH SMALL V BELOW: try adding arabic</li>
<li>U+0696 ARABIC LETTER REH WITH DOT BELOW AND DOT ABOVE: try adding arabic</li>
<li>U+0697 ARABIC LETTER REH WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+0698 ARABIC LETTER JEH: try adding arabic</li>
<li>U+0699 ARABIC LETTER REH WITH FOUR DOTS ABOVE: try adding arabic</li>
<li>U+069A ARABIC LETTER SEEN WITH DOT BELOW AND DOT ABOVE: try adding arabic</li>
<li>U+069B ARABIC LETTER SEEN WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+069C ARABIC LETTER SEEN WITH THREE DOTS BELOW AND THREE DOTS ABOVE: try adding arabic</li>
<li>U+069D ARABIC LETTER SAD WITH TWO DOTS BELOW: try adding arabic</li>
<li>U+069E ARABIC LETTER SAD WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+069F ARABIC LETTER TAH WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+06A0 ARABIC LETTER AIN WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+06A1 ARABIC LETTER DOTLESS FEH: try adding arabic</li>
<li>U+06A2 ARABIC LETTER FEH WITH DOT MOVED BELOW: try adding arabic</li>
<li>U+06A3 ARABIC LETTER FEH WITH DOT BELOW: try adding arabic</li>
<li>U+06A4 ARABIC LETTER VEH: try adding arabic</li>
<li>U+06A5 ARABIC LETTER FEH WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+06A6 ARABIC LETTER PEHEH: try adding arabic</li>
<li>U+06A7 ARABIC LETTER QAF WITH DOT ABOVE: try adding arabic</li>
<li>U+06A8 ARABIC LETTER QAF WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+06A9 ARABIC LETTER KEHEH: try adding arabic</li>
<li>U+06AA ARABIC LETTER SWASH KAF: try adding arabic</li>
<li>U+06AB ARABIC LETTER KAF WITH RING: try adding arabic</li>
<li>U+06AC ARABIC LETTER KAF WITH DOT ABOVE: try adding arabic</li>
<li>U+06AD ARABIC LETTER NG: try adding arabic</li>
<li>U+06AE ARABIC LETTER KAF WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+06AF ARABIC LETTER GAF: try adding arabic</li>
<li>U+06B0 ARABIC LETTER GAF WITH RING: try adding arabic</li>
<li>U+06B1 ARABIC LETTER NGOEH: try adding arabic</li>
<li>U+06B2 ARABIC LETTER GAF WITH TWO DOTS BELOW: try adding arabic</li>
<li>U+06B3 ARABIC LETTER GUEH: try adding arabic</li>
<li>U+06B4 ARABIC LETTER GAF WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+06B5 ARABIC LETTER LAM WITH SMALL V: try adding arabic</li>
<li>U+06B6 ARABIC LETTER LAM WITH DOT ABOVE: try adding arabic</li>
<li>U+06B7 ARABIC LETTER LAM WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+06B8 ARABIC LETTER LAM WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+06B9 ARABIC LETTER NOON WITH DOT BELOW: try adding arabic</li>
<li>U+06BA ARABIC LETTER NOON GHUNNA: try adding arabic</li>
<li>U+06BB ARABIC LETTER RNOON: try adding arabic</li>
<li>U+06BC ARABIC LETTER NOON WITH RING: try adding arabic</li>
<li>U+06BD ARABIC LETTER NOON WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+06BE ARABIC LETTER HEH DOACHASHMEE: try adding arabic</li>
<li>U+06BF ARABIC LETTER TCHEH WITH DOT ABOVE: try adding arabic</li>
<li>U+06C0 ARABIC LETTER HEH WITH YEH ABOVE: try adding arabic</li>
<li>U+06C1 ARABIC LETTER HEH GOAL: try adding arabic</li>
<li>U+06C2 ARABIC LETTER HEH GOAL WITH HAMZA ABOVE: try adding arabic</li>
<li>U+06C3 ARABIC LETTER TEH MARBUTA GOAL: try adding arabic</li>
<li>U+06C4 ARABIC LETTER WAW WITH RING: try adding arabic</li>
<li>U+06C5 ARABIC LETTER KIRGHIZ OE: try adding arabic</li>
<li>U+06C6 ARABIC LETTER OE: try adding arabic</li>
<li>U+06C7 ARABIC LETTER U: try adding arabic</li>
<li>U+06C8 ARABIC LETTER YU: try adding arabic</li>
<li>U+06C9 ARABIC LETTER KIRGHIZ YU: try adding arabic</li>
<li>U+06CA ARABIC LETTER WAW WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+06CB ARABIC LETTER VE: try adding arabic</li>
<li>U+06CC ARABIC LETTER FARSI YEH: try adding arabic</li>
<li>U+06CD ARABIC LETTER YEH WITH TAIL: try adding arabic</li>
<li>U+06CE ARABIC LETTER YEH WITH SMALL V: try adding arabic</li>
<li>U+06CF ARABIC LETTER WAW WITH DOT ABOVE: try adding arabic</li>
<li>U+06D0 ARABIC LETTER E: try adding arabic</li>
<li>U+06D1 ARABIC LETTER YEH WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+06D2 ARABIC LETTER YEH BARREE: try adding arabic</li>
<li>U+06D3 ARABIC LETTER YEH BARREE WITH HAMZA ABOVE: try adding arabic</li>
<li>U+06D4 ARABIC FULL STOP: try adding one of: yezidi, arabic, hanifi-rohingya</li>
<li>U+06D5 ARABIC LETTER AE: try adding arabic</li>
<li>U+06D6 ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA: try adding arabic</li>
<li>U+06D7 ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA: try adding arabic</li>
<li>U+06D8 ARABIC SMALL HIGH MEEM INITIAL FORM: try adding arabic</li>
<li>U+06D9 ARABIC SMALL HIGH LAM ALEF: try adding arabic</li>
<li>U+06DA ARABIC SMALL HIGH JEEM: try adding arabic</li>
<li>U+06DB ARABIC SMALL HIGH THREE DOTS: try adding arabic</li>
<li>U+06DC ARABIC SMALL HIGH SEEN: try adding arabic</li>
<li>U+06DD ARABIC END OF AYAH: try adding arabic</li>
<li>U+06DE ARABIC START OF RUB EL HIZB: try adding arabic</li>
<li>U+06DF ARABIC SMALL HIGH ROUNDED ZERO: try adding arabic</li>
<li>U+06E0 ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO: try adding arabic</li>
<li>U+06E1 ARABIC SMALL HIGH DOTLESS HEAD OF KHAH: try adding arabic</li>
<li>U+06E2 ARABIC SMALL HIGH MEEM ISOLATED FORM: try adding arabic</li>
<li>U+06E3 ARABIC SMALL LOW SEEN: try adding arabic</li>
<li>U+06E4 ARABIC SMALL HIGH MADDA: try adding arabic</li>
<li>U+06E5 ARABIC SMALL WAW: try adding arabic</li>
<li>U+06E6 ARABIC SMALL YEH: try adding arabic</li>
<li>U+06E7 ARABIC SMALL HIGH YEH: try adding arabic</li>
<li>U+06E8 ARABIC SMALL HIGH NOON: try adding arabic</li>
<li>U+06E9 ARABIC PLACE OF SAJDAH: try adding arabic</li>
<li>U+06EA ARABIC EMPTY CENTRE LOW STOP: try adding arabic</li>
<li>U+06EB ARABIC EMPTY CENTRE HIGH STOP: try adding arabic</li>
<li>U+06EC ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE: try adding arabic</li>
<li>U+06ED ARABIC SMALL LOW MEEM: try adding arabic</li>
<li>U+06EE ARABIC LETTER DAL WITH INVERTED V: try adding arabic</li>
<li>U+06EF ARABIC LETTER REH WITH INVERTED V: try adding arabic</li>
<li>U+06F0 EXTENDED ARABIC-INDIC DIGIT ZERO: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F1 EXTENDED ARABIC-INDIC DIGIT ONE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F2 EXTENDED ARABIC-INDIC DIGIT TWO: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F3 EXTENDED ARABIC-INDIC DIGIT THREE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F4 EXTENDED ARABIC-INDIC DIGIT FOUR: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F5 EXTENDED ARABIC-INDIC DIGIT FIVE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F6 EXTENDED ARABIC-INDIC DIGIT SIX: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F7 EXTENDED ARABIC-INDIC DIGIT SEVEN: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F8 EXTENDED ARABIC-INDIC DIGIT EIGHT: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F9 EXTENDED ARABIC-INDIC DIGIT NINE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06FA ARABIC LETTER SHEEN WITH DOT BELOW: try adding arabic</li>
<li>U+06FB ARABIC LETTER DAD WITH DOT BELOW: try adding arabic</li>
<li>U+06FC ARABIC LETTER GHAIN WITH DOT BELOW: try adding arabic</li>
<li>U+06FD ARABIC SIGN SINDHI AMPERSAND: try adding arabic</li>
<li>U+06FE ARABIC SIGN SINDHI POSTPOSITION MEN: try adding arabic</li>
<li>U+06FF ARABIC LETTER HEH WITH INVERTED V: try adding arabic</li>
<li>U+0750 ARABIC LETTER BEH WITH THREE DOTS HORIZONTALLY BELOW: try adding arabic</li>
<li>U+0751 ARABIC LETTER BEH WITH DOT BELOW AND THREE DOTS ABOVE: try adding arabic</li>
<li>U+0752 ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW: try adding arabic</li>
<li>U+0753 ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW AND TWO DOTS ABOVE: try adding arabic</li>
<li>U+0754 ARABIC LETTER BEH WITH TWO DOTS BELOW AND DOT ABOVE: try adding arabic</li>
<li>U+0755 ARABIC LETTER BEH WITH INVERTED SMALL V BELOW: try adding arabic</li>
<li>U+0756 ARABIC LETTER BEH WITH SMALL V: try adding arabic</li>
<li>U+0757 ARABIC LETTER HAH WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+0758 ARABIC LETTER HAH WITH THREE DOTS POINTING UPWARDS BELOW: try adding arabic</li>
<li>U+0759 ARABIC LETTER DAL WITH TWO DOTS VERTICALLY BELOW AND SMALL TAH: try adding arabic</li>
<li>U+075A ARABIC LETTER DAL WITH INVERTED SMALL V BELOW: try adding arabic</li>
<li>U+075B ARABIC LETTER REH WITH STROKE: try adding arabic</li>
<li>U+075C ARABIC LETTER SEEN WITH FOUR DOTS ABOVE: try adding arabic</li>
<li>U+075D ARABIC LETTER AIN WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+075E ARABIC LETTER AIN WITH THREE DOTS POINTING DOWNWARDS ABOVE: try adding arabic</li>
<li>U+075F ARABIC LETTER AIN WITH TWO DOTS VERTICALLY ABOVE: try adding arabic</li>
<li>U+0760 ARABIC LETTER FEH WITH TWO DOTS BELOW: try adding arabic</li>
<li>U+0761 ARABIC LETTER FEH WITH THREE DOTS POINTING UPWARDS BELOW: try adding arabic</li>
<li>U+0762 ARABIC LETTER KEHEH WITH DOT ABOVE: try adding arabic</li>
<li>U+0763 ARABIC LETTER KEHEH WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+0764 ARABIC LETTER KEHEH WITH THREE DOTS POINTING UPWARDS BELOW: try adding arabic</li>
<li>U+0765 ARABIC LETTER MEEM WITH DOT ABOVE: try adding arabic</li>
<li>U+0766 ARABIC LETTER MEEM WITH DOT BELOW: try adding arabic</li>
<li>U+0767 ARABIC LETTER NOON WITH TWO DOTS BELOW: try adding arabic</li>
<li>U+0768 ARABIC LETTER NOON WITH SMALL TAH: try adding arabic</li>
<li>U+0769 ARABIC LETTER NOON WITH SMALL V: try adding arabic</li>
<li>U+076A ARABIC LETTER LAM WITH BAR: try adding arabic</li>
<li>U+076B ARABIC LETTER REH WITH TWO DOTS VERTICALLY ABOVE: try adding arabic</li>
<li>U+076C ARABIC LETTER REH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+076D ARABIC LETTER SEEN WITH TWO DOTS VERTICALLY ABOVE: try adding arabic</li>
<li>U+076E ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH BELOW: try adding arabic</li>
<li>U+076F ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH AND TWO DOTS: try adding arabic</li>
<li>U+0770 ARABIC LETTER SEEN WITH SMALL ARABIC LETTER TAH AND TWO DOTS: try adding arabic</li>
<li>U+0771 ARABIC LETTER REH WITH SMALL ARABIC LETTER TAH AND TWO DOTS: try adding arabic</li>
<li>U+0772 ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH ABOVE: try adding arabic</li>
<li>U+0773 ARABIC LETTER ALEF WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE: try adding arabic</li>
<li>U+0774 ARABIC LETTER ALEF WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE: try adding arabic</li>
<li>U+0775 ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE: try adding arabic</li>
<li>U+0776 ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE: try adding arabic</li>
<li>U+0777 ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT FOUR BELOW: try adding arabic</li>
<li>U+0778 ARABIC LETTER WAW WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE: try adding arabic</li>
<li>U+0779 ARABIC LETTER WAW WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE: try adding arabic</li>
<li>U+077A ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE: try adding arabic</li>
<li>U+077B ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE: try adding arabic</li>
<li>U+077C ARABIC LETTER HAH WITH EXTENDED ARABIC-INDIC DIGIT FOUR BELOW: try adding arabic</li>
<li>U+077D ARABIC LETTER SEEN WITH EXTENDED ARABIC-INDIC DIGIT FOUR ABOVE: try adding arabic</li>
<li>U+077E ARABIC LETTER SEEN WITH INVERTED V: try adding arabic</li>
<li>U+077F ARABIC LETTER KAF WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+08A0 ARABIC LETTER BEH WITH SMALL V BELOW: try adding arabic</li>
<li>U+08A1 ARABIC LETTER BEH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+08A2 ARABIC LETTER JEEM WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+08A3 ARABIC LETTER TAH WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+08A4 ARABIC LETTER FEH WITH DOT BELOW AND THREE DOTS ABOVE: try adding arabic</li>
<li>U+08A5 ARABIC LETTER QAF WITH DOT BELOW: try adding arabic</li>
<li>U+08A6 ARABIC LETTER LAM WITH DOUBLE BAR: try adding arabic</li>
<li>U+08A7 ARABIC LETTER MEEM WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+08A8 ARABIC LETTER YEH WITH TWO DOTS BELOW AND HAMZA ABOVE: try adding arabic</li>
<li>U+08A9 ARABIC LETTER YEH WITH TWO DOTS BELOW AND DOT ABOVE: try adding arabic</li>
<li>U+08AA ARABIC LETTER REH WITH LOOP: try adding arabic</li>
<li>U+08AB ARABIC LETTER WAW WITH DOT WITHIN: try adding arabic</li>
<li>U+08AC ARABIC LETTER ROHINGYA YEH: try adding arabic</li>
<li>U+08AD ARABIC LETTER LOW ALEF: try adding arabic</li>
<li>U+08AE ARABIC LETTER DAL WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+08AF ARABIC LETTER SAD WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+08B0 ARABIC LETTER GAF WITH INVERTED STROKE: try adding arabic</li>
<li>U+08B1 ARABIC LETTER STRAIGHT WAW: try adding arabic</li>
<li>U+08B2 ARABIC LETTER ZAIN WITH INVERTED V ABOVE: try adding arabic</li>
<li>U+08B3 ARABIC LETTER AIN WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+08B4 ARABIC LETTER KAF WITH DOT BELOW: try adding arabic</li>
<li>U+08B6 ARABIC LETTER BEH WITH SMALL MEEM ABOVE: try adding arabic</li>
<li>U+08B7 ARABIC LETTER PEH WITH SMALL MEEM ABOVE: try adding arabic</li>
<li>U+08B8 ARABIC LETTER TEH WITH SMALL TEH ABOVE: try adding arabic</li>
<li>U+08B9 ARABIC LETTER REH WITH SMALL NOON ABOVE: try adding arabic</li>
<li>U+08BA ARABIC LETTER YEH WITH TWO DOTS BELOW AND SMALL NOON ABOVE: try adding arabic</li>
<li>U+08BB ARABIC LETTER AFRICAN FEH: try adding arabic</li>
<li>U+08BC ARABIC LETTER AFRICAN QAF: try adding arabic</li>
<li>U+08BD ARABIC LETTER AFRICAN NOON: try adding arabic</li>
<li>U+08BE ARABIC LETTER PEH WITH SMALL V: try adding arabic</li>
<li>U+08BF ARABIC LETTER TEH WITH SMALL V: try adding arabic</li>
<li>U+08C0 ARABIC LETTER TTEH WITH SMALL V: try adding arabic</li>
<li>U+08C1 ARABIC LETTER TCHEH WITH SMALL V: try adding arabic</li>
<li>U+08C2 ARABIC LETTER KEHEH WITH SMALL V: try adding arabic</li>
<li>U+08C3 ARABIC LETTER GHAIN WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+08C4 ARABIC LETTER AFRICAN QAF WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+08C5 ARABIC LETTER JEEM WITH THREE DOTS ABOVE: try adding arabic</li>
<li>U+08C6 ARABIC LETTER JEEM WITH THREE DOTS BELOW: try adding arabic</li>
<li>U+08C7 ARABIC LETTER LAM WITH SMALL ARABIC LETTER TAH ABOVE: try adding arabic</li>
<li>U+08CC ARABIC SMALL HIGH WORD SAH: try adding arabic</li>
<li>U+08CF ARABIC LARGE ROUND DOT BELOW: try adding arabic</li>
<li>U+08D3 ARABIC SMALL LOW WAW: try adding arabic</li>
<li>U+08D4 ARABIC SMALL HIGH WORD AR-RUB: try adding arabic</li>
<li>U+08D5 ARABIC SMALL HIGH SAD: try adding arabic</li>
<li>U+08D6 ARABIC SMALL HIGH AIN: try adding arabic</li>
<li>U+08D7 ARABIC SMALL HIGH QAF: try adding arabic</li>
<li>U+08D8 ARABIC SMALL HIGH NOON WITH KASRA: try adding arabic</li>
<li>U+08D9 ARABIC SMALL LOW NOON WITH KASRA: try adding arabic</li>
<li>U+08DA ARABIC SMALL HIGH WORD ATH-THALATHA: try adding arabic</li>
<li>U+08DB ARABIC SMALL HIGH WORD AS-SAJDA: try adding arabic</li>
<li>U+08DC ARABIC SMALL HIGH WORD AN-NISF: try adding arabic</li>
<li>U+08DD ARABIC SMALL HIGH WORD SAKTA: try adding arabic</li>
<li>U+08DE ARABIC SMALL HIGH WORD QIF: try adding arabic</li>
<li>U+08DF ARABIC SMALL HIGH WORD WAQFA: try adding arabic</li>
<li>U+08E0 ARABIC SMALL HIGH FOOTNOTE MARKER: try adding arabic</li>
<li>U+08E1 ARABIC SMALL HIGH SIGN SAFHA: try adding arabic</li>
<li>U+08E2 ARABIC DISPUTED END OF AYAH: not included in any glyphset definition</li>
<li>U+08E3 ARABIC TURNED DAMMA BELOW: try adding arabic</li>
<li>U+08E4 ARABIC CURLY FATHA: try adding arabic</li>
<li>U+08E5 ARABIC CURLY DAMMA: try adding arabic</li>
<li>U+08E6 ARABIC CURLY KASRA: try adding arabic</li>
<li>U+08E7 ARABIC CURLY FATHATAN: try adding arabic</li>
<li>U+08E8 ARABIC CURLY DAMMATAN: try adding arabic</li>
<li>U+08E9 ARABIC CURLY KASRATAN: try adding arabic</li>
<li>U+08EA ARABIC TONE ONE DOT ABOVE: try adding arabic</li>
<li>U+08EB ARABIC TONE TWO DOTS ABOVE: try adding arabic</li>
<li>U+08EC ARABIC TONE LOOP ABOVE: try adding arabic</li>
<li>U+08ED ARABIC TONE ONE DOT BELOW: try adding arabic</li>
<li>U+08EE ARABIC TONE TWO DOTS BELOW: try adding arabic</li>
<li>U+08EF ARABIC TONE LOOP BELOW: try adding arabic</li>
<li>U+08F0 ARABIC OPEN FATHATAN: try adding arabic</li>
<li>U+08F1 ARABIC OPEN DAMMATAN: try adding arabic</li>
<li>U+08F2 ARABIC OPEN KASRATAN: try adding arabic</li>
<li>U+08F3 ARABIC SMALL HIGH WAW: try adding arabic</li>
<li>U+08F4 ARABIC FATHA WITH RING: try adding arabic</li>
<li>U+08F5 ARABIC FATHA WITH DOT ABOVE: try adding arabic</li>
<li>U+08F6 ARABIC KASRA WITH DOT BELOW: try adding arabic</li>
<li>U+08F7 ARABIC LEFT ARROWHEAD ABOVE: try adding arabic</li>
<li>U+08F8 ARABIC RIGHT ARROWHEAD ABOVE: try adding arabic</li>
<li>U+08F9 ARABIC LEFT ARROWHEAD BELOW: try adding arabic</li>
<li>U+08FA ARABIC RIGHT ARROWHEAD BELOW: try adding arabic</li>
<li>U+08FB ARABIC DOUBLE RIGHT ARROWHEAD ABOVE: try adding arabic</li>
<li>U+08FC ARABIC DOUBLE RIGHT ARROWHEAD ABOVE WITH DOT: try adding arabic</li>
<li>U+08FD ARABIC RIGHT ARROWHEAD ABOVE WITH DOT: try adding arabic</li>
<li>U+08FE ARABIC DAMMA WITH DOT: try adding arabic</li>
<li>U+08FF ARABIC MARK SIDEWAYS NOON GHUNNA: try adding arabic</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: hatran, balinese, arabic, modi, telugu, meetei-mayek, tagalog, tibetan, mahajani, chakma, hanifi-rohingya, gunjala-gondi, khudawadi, batak, kaithi, kannada, tai-le, bengali, malayalam, mandaic, phags-pa, syloti-nagri, sinhala, bhaiksuki, grantha, kayah-li, takri, manichaean, zanabazar-square, hebrew, psalter-pahlavi, devanagari, khojki, mongolian, javanese, brahmi, new-tai-lue, buginese, newa, sharada, syriac, masaram-gondi, tagbanwa, gurmukhi, duployan, khmer, tamil, buhid, kharoshthi, avestan, tifinagh, hanunoo, saurashtra, lao, warang-citi, gujarati, thai, sogdian, nko, tirhuta, tai-tham, cham, lepcha, oriya, limbu, tai-viet, myanmar, dogra, sundanese, rejang, yi, siddham, pahawh-hmong, thaana</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: balinese, arabic, modi, telugu, meetei-mayek, tagalog, tibetan, mahajani, old-hungarian, chakma, hanifi-rohingya, gunjala-gondi, khudawadi, batak, kaithi, kannada, tai-le, bengali, malayalam, mandaic, phags-pa, syloti-nagri, sinhala, bhaiksuki, grantha, kayah-li, takri, manichaean, zanabazar-square, hebrew, psalter-pahlavi, devanagari, khojki, mongolian, javanese, brahmi, new-tai-lue, buginese, newa, sharada, syriac, masaram-gondi, tagbanwa, gurmukhi, duployan, khmer, tamil, buhid, kharoshthi, avestan, tifinagh, hanunoo, saurashtra, lao, warang-citi, gujarati, thai, sogdian, nko, tirhuta, tai-tham, cham, lepcha, oriya, limbu, tai-viet, myanmar, dogra, sundanese, rejang, yi, siddham, pahawh-hmong, thaana</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: syriac, arabic, nko, hebrew, phags-pa, thaana</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: syriac, nko, hebrew, phags-pa, thaana</li>
<li>U+2010 HYPHEN: try adding one of: arabic, kayah-li, coptic, hebrew, cham, kharoshthi, kaithi, sundanese, armenian, lisu, sora-sompeng, yi, syloti-nagri</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition</li>
<li>U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition</li>
<li>U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition</li>
<li>U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition</li>
<li>U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh</li>
<li>U+202F NARROW NO-BREAK SPACE: try adding one of: yi, mongolian, phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+203F UNDERTIE: not included in any glyphset definition</li>
<li>U+2040 CHARACTER TIE: try adding math</li>
<li>U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition</li>
<li>U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition</li>
<li>U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition</li>
<li>U+2054 INVERTED UNDERTIE: not included in any glyphset definition</li>
<li>U+2061 FUNCTION APPLICATION: not included in any glyphset definition</li>
<li>U+2062 INVISIBLE TIMES: not included in any glyphset definition</li>
<li>U+2063 INVISIBLE SEPARATOR: not included in any glyphset definition</li>
<li>U+2064 INVISIBLE PLUS: not included in any glyphset definition</li>
<li>U+2066 LEFT-TO-RIGHT ISOLATE: not included in any glyphset definition</li>
<li>U+2067 RIGHT-TO-LEFT ISOLATE: not included in any glyphset definition</li>
<li>U+2068 FIRST STRONG ISOLATE: not included in any glyphset definition</li>
<li>U+2069 POP DIRECTIONAL ISOLATE: not included in any glyphset definition</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+211E PRESCRIPTION TAKE: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2127 INVERTED OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2217 ASTERISK OPERATOR: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2222 SPHERICAL ANGLE: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2422 BLANK SYMBOL: try adding symbols</li>
<li>U+2423 OPEN BOX: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: balinese, caucasian-albanian, modi, symbols, chakma, soyombo, bengali, malayalam, grantha, kayah-li, canadian-aboriginal, devanagari, ahom, tagbanwa, gurmukhi, duployan, elbasan, saurashtra, warang-citi, nko, oriya, pahawh-hmong, thaana, telugu, tagalog, hanifi-rohingya, gunjala-gondi, khudawadi, mandaic, phags-pa, syloti-nagri, bhaiksuki, bassa-vah, takri, hebrew, mende-kikakui, khojki, javanese, buginese, osage, masaram-gondi, tamil, buhid, lao, thai, math, tirhuta, limbu, wancho, myanmar, dogra, sundanese, mahajani, coptic, kannada, old-permic, marchen, music, sinhala, manichaean, zanabazar-square, psalter-pahlavi, sharada, khmer, kharoshthi, tifinagh, sogdian, cham, siddham, meetei-mayek, tibetan, batak, kaithi, tai-le, mongolian, brahmi, new-tai-lue, newa, syriac, adlam, hanunoo, armenian, gujarati, miao, tai-tham, lepcha, tai-viet, rejang, yi</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: symbols, music</li>
<li>U+26AD MARRIAGE SYMBOL: try adding symbols</li>
<li>U+26AE DIVORCE SYMBOL: try adding symbols</li>
<li>U+27E6 MATHEMATICAL LEFT WHITE SQUARE BRACKET: try adding math</li>
<li>U+27E7 MATHEMATICAL RIGHT WHITE SQUARE BRACKET: try adding math</li>
<li>U+2E18 INVERTED INTERROBANG: not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
<li>U+FB50 ARABIC LETTER ALEF WASLA ISOLATED FORM: try adding arabic</li>
<li>U+FB51 ARABIC LETTER ALEF WASLA FINAL FORM: try adding arabic</li>
<li>U+FB52 ARABIC LETTER BEEH ISOLATED FORM: try adding arabic</li>
<li>U+FB53 ARABIC LETTER BEEH FINAL FORM: try adding arabic</li>
<li>U+FB54 ARABIC LETTER BEEH INITIAL FORM: try adding arabic</li>
<li>U+FB55 ARABIC LETTER BEEH MEDIAL FORM: try adding arabic</li>
<li>U+FB56 ARABIC LETTER PEH ISOLATED FORM: try adding arabic</li>
<li>U+FB57 ARABIC LETTER PEH FINAL FORM: try adding arabic</li>
<li>U+FB58 ARABIC LETTER PEH INITIAL FORM: try adding arabic</li>
<li>U+FB59 ARABIC LETTER PEH MEDIAL FORM: try adding arabic</li>
<li>U+FB5A ARABIC LETTER BEHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB5B ARABIC LETTER BEHEH FINAL FORM: try adding arabic</li>
<li>U+FB5C ARABIC LETTER BEHEH INITIAL FORM: try adding arabic</li>
<li>U+FB5D ARABIC LETTER BEHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB5E ARABIC LETTER TTEHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB5F ARABIC LETTER TTEHEH FINAL FORM: try adding arabic</li>
<li>U+FB60 ARABIC LETTER TTEHEH INITIAL FORM: try adding arabic</li>
<li>U+FB61 ARABIC LETTER TTEHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB62 ARABIC LETTER TEHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB63 ARABIC LETTER TEHEH FINAL FORM: try adding arabic</li>
<li>U+FB64 ARABIC LETTER TEHEH INITIAL FORM: try adding arabic</li>
<li>U+FB65 ARABIC LETTER TEHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB66 ARABIC LETTER TTEH ISOLATED FORM: try adding arabic</li>
<li>U+FB67 ARABIC LETTER TTEH FINAL FORM: try adding arabic</li>
<li>U+FB68 ARABIC LETTER TTEH INITIAL FORM: try adding arabic</li>
<li>U+FB69 ARABIC LETTER TTEH MEDIAL FORM: try adding arabic</li>
<li>U+FB6A ARABIC LETTER VEH ISOLATED FORM: try adding arabic</li>
<li>U+FB6B ARABIC LETTER VEH FINAL FORM: try adding arabic</li>
<li>U+FB6C ARABIC LETTER VEH INITIAL FORM: try adding arabic</li>
<li>U+FB6D ARABIC LETTER VEH MEDIAL FORM: try adding arabic</li>
<li>U+FB6E ARABIC LETTER PEHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB6F ARABIC LETTER PEHEH FINAL FORM: try adding arabic</li>
<li>U+FB70 ARABIC LETTER PEHEH INITIAL FORM: try adding arabic</li>
<li>U+FB71 ARABIC LETTER PEHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB72 ARABIC LETTER DYEH ISOLATED FORM: try adding arabic</li>
<li>U+FB73 ARABIC LETTER DYEH FINAL FORM: try adding arabic</li>
<li>U+FB74 ARABIC LETTER DYEH INITIAL FORM: try adding arabic</li>
<li>U+FB75 ARABIC LETTER DYEH MEDIAL FORM: try adding arabic</li>
<li>U+FB76 ARABIC LETTER NYEH ISOLATED FORM: try adding arabic</li>
<li>U+FB77 ARABIC LETTER NYEH FINAL FORM: try adding arabic</li>
<li>U+FB78 ARABIC LETTER NYEH INITIAL FORM: try adding arabic</li>
<li>U+FB79 ARABIC LETTER NYEH MEDIAL FORM: try adding arabic</li>
<li>U+FB7A ARABIC LETTER TCHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB7B ARABIC LETTER TCHEH FINAL FORM: try adding arabic</li>
<li>U+FB7C ARABIC LETTER TCHEH INITIAL FORM: try adding arabic</li>
<li>U+FB7D ARABIC LETTER TCHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB7E ARABIC LETTER TCHEHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB7F ARABIC LETTER TCHEHEH FINAL FORM: try adding arabic</li>
<li>U+FB80 ARABIC LETTER TCHEHEH INITIAL FORM: try adding arabic</li>
<li>U+FB81 ARABIC LETTER TCHEHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB82 ARABIC LETTER DDAHAL ISOLATED FORM: try adding arabic</li>
<li>U+FB83 ARABIC LETTER DDAHAL FINAL FORM: try adding arabic</li>
<li>U+FB84 ARABIC LETTER DAHAL ISOLATED FORM: try adding arabic</li>
<li>U+FB85 ARABIC LETTER DAHAL FINAL FORM: try adding arabic</li>
<li>U+FB86 ARABIC LETTER DUL ISOLATED FORM: try adding arabic</li>
<li>U+FB87 ARABIC LETTER DUL FINAL FORM: try adding arabic</li>
<li>U+FB88 ARABIC LETTER DDAL ISOLATED FORM: try adding arabic</li>
<li>U+FB89 ARABIC LETTER DDAL FINAL FORM: try adding arabic</li>
<li>U+FB8A ARABIC LETTER JEH ISOLATED FORM: try adding arabic</li>
<li>U+FB8B ARABIC LETTER JEH FINAL FORM: try adding arabic</li>
<li>U+FB8C ARABIC LETTER RREH ISOLATED FORM: try adding arabic</li>
<li>U+FB8D ARABIC LETTER RREH FINAL FORM: try adding arabic</li>
<li>U+FB8E ARABIC LETTER KEHEH ISOLATED FORM: try adding arabic</li>
<li>U+FB8F ARABIC LETTER KEHEH FINAL FORM: try adding arabic</li>
<li>U+FB90 ARABIC LETTER KEHEH INITIAL FORM: try adding arabic</li>
<li>U+FB91 ARABIC LETTER KEHEH MEDIAL FORM: try adding arabic</li>
<li>U+FB92 ARABIC LETTER GAF ISOLATED FORM: try adding arabic</li>
<li>U+FB93 ARABIC LETTER GAF FINAL FORM: try adding arabic</li>
<li>U+FB94 ARABIC LETTER GAF INITIAL FORM: try adding arabic</li>
<li>U+FB95 ARABIC LETTER GAF MEDIAL FORM: try adding arabic</li>
<li>U+FB96 ARABIC LETTER GUEH ISOLATED FORM: try adding arabic</li>
<li>U+FB97 ARABIC LETTER GUEH FINAL FORM: try adding arabic</li>
<li>U+FB98 ARABIC LETTER GUEH INITIAL FORM: try adding arabic</li>
<li>U+FB99 ARABIC LETTER GUEH MEDIAL FORM: try adding arabic</li>
<li>U+FB9A ARABIC LETTER NGOEH ISOLATED FORM: try adding arabic</li>
<li>U+FB9B ARABIC LETTER NGOEH FINAL FORM: try adding arabic</li>
<li>U+FB9C ARABIC LETTER NGOEH INITIAL FORM: try adding arabic</li>
<li>U+FB9D ARABIC LETTER NGOEH MEDIAL FORM: try adding arabic</li>
<li>U+FB9E ARABIC LETTER NOON GHUNNA ISOLATED FORM: try adding arabic</li>
<li>U+FB9F ARABIC LETTER NOON GHUNNA FINAL FORM: try adding arabic</li>
<li>U+FBA0 ARABIC LETTER RNOON ISOLATED FORM: try adding arabic</li>
<li>U+FBA1 ARABIC LETTER RNOON FINAL FORM: try adding arabic</li>
<li>U+FBA2 ARABIC LETTER RNOON INITIAL FORM: try adding arabic</li>
<li>U+FBA3 ARABIC LETTER RNOON MEDIAL FORM: try adding arabic</li>
<li>U+FBA4 ARABIC LETTER HEH WITH YEH ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FBA5 ARABIC LETTER HEH WITH YEH ABOVE FINAL FORM: try adding arabic</li>
<li>U+FBA6 ARABIC LETTER HEH GOAL ISOLATED FORM: try adding arabic</li>
<li>U+FBA7 ARABIC LETTER HEH GOAL FINAL FORM: try adding arabic</li>
<li>U+FBA8 ARABIC LETTER HEH GOAL INITIAL FORM: try adding arabic</li>
<li>U+FBA9 ARABIC LETTER HEH GOAL MEDIAL FORM: try adding arabic</li>
<li>U+FBAA ARABIC LETTER HEH DOACHASHMEE ISOLATED FORM: try adding arabic</li>
<li>U+FBAB ARABIC LETTER HEH DOACHASHMEE FINAL FORM: try adding arabic</li>
<li>U+FBAC ARABIC LETTER HEH DOACHASHMEE INITIAL FORM: try adding arabic</li>
<li>U+FBAD ARABIC LETTER HEH DOACHASHMEE MEDIAL FORM: try adding arabic</li>
<li>U+FBAE ARABIC LETTER YEH BARREE ISOLATED FORM: try adding arabic</li>
<li>U+FBAF ARABIC LETTER YEH BARREE FINAL FORM: try adding arabic</li>
<li>U+FBB0 ARABIC LETTER YEH BARREE WITH HAMZA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FBB1 ARABIC LETTER YEH BARREE WITH HAMZA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FBB2 ARABIC SYMBOL DOT ABOVE: try adding arabic</li>
<li>U+FBB3 ARABIC SYMBOL DOT BELOW: try adding arabic</li>
<li>U+FBB4 ARABIC SYMBOL TWO DOTS ABOVE: try adding arabic</li>
<li>U+FBB5 ARABIC SYMBOL TWO DOTS BELOW: try adding arabic</li>
<li>U+FBB6 ARABIC SYMBOL THREE DOTS ABOVE: try adding arabic</li>
<li>U+FBB7 ARABIC SYMBOL THREE DOTS BELOW: try adding arabic</li>
<li>U+FBB8 ARABIC SYMBOL THREE DOTS POINTING DOWNWARDS ABOVE: try adding arabic</li>
<li>U+FBB9 ARABIC SYMBOL THREE DOTS POINTING DOWNWARDS BELOW: try adding arabic</li>
<li>U+FBBA ARABIC SYMBOL FOUR DOTS ABOVE: try adding arabic</li>
<li>U+FBBB ARABIC SYMBOL FOUR DOTS BELOW: try adding arabic</li>
<li>U+FBBC ARABIC SYMBOL DOUBLE VERTICAL BAR BELOW: try adding arabic</li>
<li>U+FBBD ARABIC SYMBOL TWO DOTS VERTICALLY ABOVE: try adding arabic</li>
<li>U+FBBE ARABIC SYMBOL TWO DOTS VERTICALLY BELOW: try adding arabic</li>
<li>U+FBBF ARABIC SYMBOL RING: try adding arabic</li>
<li>U+FBC0 ARABIC SYMBOL SMALL TAH ABOVE: try adding arabic</li>
<li>U+FBC1 ARABIC SYMBOL SMALL TAH BELOW: try adding arabic</li>
<li>U+FBD3 ARABIC LETTER NG ISOLATED FORM: try adding arabic</li>
<li>U+FBD4 ARABIC LETTER NG FINAL FORM: try adding arabic</li>
<li>U+FBD5 ARABIC LETTER NG INITIAL FORM: try adding arabic</li>
<li>U+FBD6 ARABIC LETTER NG MEDIAL FORM: try adding arabic</li>
<li>U+FBD7 ARABIC LETTER U ISOLATED FORM: try adding arabic</li>
<li>U+FBD8 ARABIC LETTER U FINAL FORM: try adding arabic</li>
<li>U+FBD9 ARABIC LETTER OE ISOLATED FORM: try adding arabic</li>
<li>U+FBDA ARABIC LETTER OE FINAL FORM: try adding arabic</li>
<li>U+FBDB ARABIC LETTER YU ISOLATED FORM: try adding arabic</li>
<li>U+FBDC ARABIC LETTER YU FINAL FORM: try adding arabic</li>
<li>U+FBDD ARABIC LETTER U WITH HAMZA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FBDE ARABIC LETTER VE ISOLATED FORM: try adding arabic</li>
<li>U+FBDF ARABIC LETTER VE FINAL FORM: try adding arabic</li>
<li>U+FBE0 ARABIC LETTER KIRGHIZ OE ISOLATED FORM: try adding arabic</li>
<li>U+FBE1 ARABIC LETTER KIRGHIZ OE FINAL FORM: try adding arabic</li>
<li>U+FBE2 ARABIC LETTER KIRGHIZ YU ISOLATED FORM: try adding arabic</li>
<li>U+FBE3 ARABIC LETTER KIRGHIZ YU FINAL FORM: try adding arabic</li>
<li>U+FBE4 ARABIC LETTER E ISOLATED FORM: try adding arabic</li>
<li>U+FBE5 ARABIC LETTER E FINAL FORM: try adding arabic</li>
<li>U+FBE6 ARABIC LETTER E INITIAL FORM: try adding arabic</li>
<li>U+FBE7 ARABIC LETTER E MEDIAL FORM: try adding arabic</li>
<li>U+FBE8 ARABIC LETTER UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA INITIAL FORM: try adding arabic</li>
<li>U+FBE9 ARABIC LETTER UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA MEDIAL FORM: try adding arabic</li>
<li>U+FBFC ARABIC LETTER FARSI YEH ISOLATED FORM: try adding arabic</li>
<li>U+FBFD ARABIC LETTER FARSI YEH FINAL FORM: try adding arabic</li>
<li>U+FBFE ARABIC LETTER FARSI YEH INITIAL FORM: try adding arabic</li>
<li>U+FBFF ARABIC LETTER FARSI YEH MEDIAL FORM: try adding arabic</li>
<li>U+FC94 ARABIC LIGATURE YEH WITH NOON FINAL FORM: try adding arabic</li>
<li>U+FC9F ARABIC LIGATURE BEH WITH MEEM INITIAL FORM: try adding arabic</li>
<li>U+FCA1 ARABIC LIGATURE TEH WITH JEEM INITIAL FORM: try adding arabic</li>
<li>U+FCA2 ARABIC LIGATURE TEH WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FCC9 ARABIC LIGATURE LAM WITH JEEM INITIAL FORM: try adding arabic</li>
<li>U+FCCA ARABIC LIGATURE LAM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FCCB ARABIC LIGATURE LAM WITH KHAH INITIAL FORM: try adding arabic</li>
<li>U+FCCC ARABIC LIGATURE LAM WITH MEEM INITIAL FORM: try adding arabic</li>
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: nko, arabic</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: nko, arabic</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: arabic, thaana</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: arabic, thaana</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: yi, manichaean, phags-pa</li>
<li>U+FE01 VARIATION SELECTOR-2: not included in any glyphset definition</li>
<li>U+FE02 VARIATION SELECTOR-3: not included in any glyphset definition</li>
<li>U+FE03 VARIATION SELECTOR-4: not included in any glyphset definition</li>
<li>U+FE04 VARIATION SELECTOR-5: not included in any glyphset definition</li>
<li>U+FE05 VARIATION SELECTOR-6: not included in any glyphset definition</li>
<li>U+FE06 VARIATION SELECTOR-7: not included in any glyphset definition</li>
<li>U+FE07 VARIATION SELECTOR-8: not included in any glyphset definition</li>
<li>U+FE08 VARIATION SELECTOR-9: not included in any glyphset definition</li>
<li>U+FE09 VARIATION SELECTOR-10: not included in any glyphset definition</li>
<li>U+FE0A VARIATION SELECTOR-11: not included in any glyphset definition</li>
<li>U+FE0B VARIATION SELECTOR-12: not included in any glyphset definition</li>
<li>U+FE0C VARIATION SELECTOR-13: not included in any glyphset definition</li>
<li>U+FE0D VARIATION SELECTOR-14: not included in any glyphset definition</li>
<li>U+FE0E VARIATION SELECTOR-15: not included in any glyphset definition</li>
<li>U+FE0F VARIATION SELECTOR-16: not included in any glyphset definition</li>
<li>U+FE70 ARABIC FATHATAN ISOLATED FORM: try adding arabic</li>
<li>U+FE71 ARABIC TATWEEL WITH FATHATAN ABOVE: try adding arabic</li>
<li>U+FE72 ARABIC DAMMATAN ISOLATED FORM: try adding arabic</li>
<li>U+FE73 ARABIC TAIL FRAGMENT: try adding arabic</li>
<li>U+FE74 ARABIC KASRATAN ISOLATED FORM: try adding arabic</li>
<li>U+FE76 ARABIC FATHA ISOLATED FORM: try adding arabic</li>
<li>U+FE77 ARABIC FATHA MEDIAL FORM: try adding arabic</li>
<li>U+FE78 ARABIC DAMMA ISOLATED FORM: try adding arabic</li>
<li>U+FE79 ARABIC DAMMA MEDIAL FORM: try adding arabic</li>
<li>U+FE7A ARABIC KASRA ISOLATED FORM: try adding arabic</li>
<li>U+FE7B ARABIC KASRA MEDIAL FORM: try adding arabic</li>
<li>U+FE7C ARABIC SHADDA ISOLATED FORM: try adding arabic</li>
<li>U+FE7D ARABIC SHADDA MEDIAL FORM: try adding arabic</li>
<li>U+FE7E ARABIC SUKUN ISOLATED FORM: try adding arabic</li>
<li>U+FE7F ARABIC SUKUN MEDIAL FORM: try adding arabic</li>
<li>U+FE80 ARABIC LETTER HAMZA ISOLATED FORM: try adding arabic</li>
<li>U+FE81 ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FE82 ARABIC LETTER ALEF WITH MADDA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FE83 ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FE84 ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FE85 ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FE86 ARABIC LETTER WAW WITH HAMZA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FE87 ARABIC LETTER ALEF WITH HAMZA BELOW ISOLATED FORM: try adding arabic</li>
<li>U+FE88 ARABIC LETTER ALEF WITH HAMZA BELOW FINAL FORM: try adding arabic</li>
<li>U+FE89 ARABIC LETTER YEH WITH HAMZA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FE8A ARABIC LETTER YEH WITH HAMZA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FE8B ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM: try adding arabic</li>
<li>U+FE8C ARABIC LETTER YEH WITH HAMZA ABOVE MEDIAL FORM: try adding arabic</li>
<li>U+FE8D ARABIC LETTER ALEF ISOLATED FORM: try adding arabic</li>
<li>U+FE8E ARABIC LETTER ALEF FINAL FORM: try adding arabic</li>
<li>U+FE8F ARABIC LETTER BEH ISOLATED FORM: try adding arabic</li>
<li>U+FE90 ARABIC LETTER BEH FINAL FORM: try adding arabic</li>
<li>U+FE91 ARABIC LETTER BEH INITIAL FORM: try adding arabic</li>
<li>U+FE92 ARABIC LETTER BEH MEDIAL FORM: try adding arabic</li>
<li>U+FE93 ARABIC LETTER TEH MARBUTA ISOLATED FORM: try adding arabic</li>
<li>U+FE94 ARABIC LETTER TEH MARBUTA FINAL FORM: try adding arabic</li>
<li>U+FE95 ARABIC LETTER TEH ISOLATED FORM: try adding arabic</li>
<li>U+FE96 ARABIC LETTER TEH FINAL FORM: try adding arabic</li>
<li>U+FE97 ARABIC LETTER TEH INITIAL FORM: try adding arabic</li>
<li>U+FE98 ARABIC LETTER TEH MEDIAL FORM: try adding arabic</li>
<li>U+FE99 ARABIC LETTER THEH ISOLATED FORM: try adding arabic</li>
<li>U+FE9A ARABIC LETTER THEH FINAL FORM: try adding arabic</li>
<li>U+FE9B ARABIC LETTER THEH INITIAL FORM: try adding arabic</li>
<li>U+FE9C ARABIC LETTER THEH MEDIAL FORM: try adding arabic</li>
<li>U+FE9D ARABIC LETTER JEEM ISOLATED FORM: try adding arabic</li>
<li>U+FE9E ARABIC LETTER JEEM FINAL FORM: try adding arabic</li>
<li>U+FE9F ARABIC LETTER JEEM INITIAL FORM: try adding arabic</li>
<li>U+FEA0 ARABIC LETTER JEEM MEDIAL FORM: try adding arabic</li>
<li>U+FEA1 ARABIC LETTER HAH ISOLATED FORM: try adding arabic</li>
<li>U+FEA2 ARABIC LETTER HAH FINAL FORM: try adding arabic</li>
<li>U+FEA3 ARABIC LETTER HAH INITIAL FORM: try adding arabic</li>
<li>U+FEA4 ARABIC LETTER HAH MEDIAL FORM: try adding arabic</li>
<li>U+FEA5 ARABIC LETTER KHAH ISOLATED FORM: try adding arabic</li>
<li>U+FEA6 ARABIC LETTER KHAH FINAL FORM: try adding arabic</li>
<li>U+FEA7 ARABIC LETTER KHAH INITIAL FORM: try adding arabic</li>
<li>U+FEA8 ARABIC LETTER KHAH MEDIAL FORM: try adding arabic</li>
<li>U+FEA9 ARABIC LETTER DAL ISOLATED FORM: try adding arabic</li>
<li>U+FEAA ARABIC LETTER DAL FINAL FORM: try adding arabic</li>
<li>U+FEAB ARABIC LETTER THAL ISOLATED FORM: try adding arabic</li>
<li>U+FEAC ARABIC LETTER THAL FINAL FORM: try adding arabic</li>
<li>U+FEAD ARABIC LETTER REH ISOLATED FORM: try adding arabic</li>
<li>U+FEAE ARABIC LETTER REH FINAL FORM: try adding arabic</li>
<li>U+FEAF ARABIC LETTER ZAIN ISOLATED FORM: try adding arabic</li>
<li>U+FEB0 ARABIC LETTER ZAIN FINAL FORM: try adding arabic</li>
<li>U+FEB1 ARABIC LETTER SEEN ISOLATED FORM: try adding arabic</li>
<li>U+FEB2 ARABIC LETTER SEEN FINAL FORM: try adding arabic</li>
<li>U+FEB3 ARABIC LETTER SEEN INITIAL FORM: try adding arabic</li>
<li>U+FEB4 ARABIC LETTER SEEN MEDIAL FORM: try adding arabic</li>
<li>U+FEB5 ARABIC LETTER SHEEN ISOLATED FORM: try adding arabic</li>
<li>U+FEB6 ARABIC LETTER SHEEN FINAL FORM: try adding arabic</li>
<li>U+FEB7 ARABIC LETTER SHEEN INITIAL FORM: try adding arabic</li>
<li>U+FEB8 ARABIC LETTER SHEEN MEDIAL FORM: try adding arabic</li>
<li>U+FEB9 ARABIC LETTER SAD ISOLATED FORM: try adding arabic</li>
<li>U+FEBA ARABIC LETTER SAD FINAL FORM: try adding arabic</li>
<li>U+FEBB ARABIC LETTER SAD INITIAL FORM: try adding arabic</li>
<li>U+FEBC ARABIC LETTER SAD MEDIAL FORM: try adding arabic</li>
<li>U+FEBD ARABIC LETTER DAD ISOLATED FORM: try adding arabic</li>
<li>U+FEBE ARABIC LETTER DAD FINAL FORM: try adding arabic</li>
<li>U+FEBF ARABIC LETTER DAD INITIAL FORM: try adding arabic</li>
<li>U+FEC0 ARABIC LETTER DAD MEDIAL FORM: try adding arabic</li>
<li>U+FEC1 ARABIC LETTER TAH ISOLATED FORM: try adding arabic</li>
<li>U+FEC2 ARABIC LETTER TAH FINAL FORM: try adding arabic</li>
<li>U+FEC3 ARABIC LETTER TAH INITIAL FORM: try adding arabic</li>
<li>U+FEC4 ARABIC LETTER TAH MEDIAL FORM: try adding arabic</li>
<li>U+FEC5 ARABIC LETTER ZAH ISOLATED FORM: try adding arabic</li>
<li>U+FEC6 ARABIC LETTER ZAH FINAL FORM: try adding arabic</li>
<li>U+FEC7 ARABIC LETTER ZAH INITIAL FORM: try adding arabic</li>
<li>U+FEC8 ARABIC LETTER ZAH MEDIAL FORM: try adding arabic</li>
<li>U+FEC9 ARABIC LETTER AIN ISOLATED FORM: try adding arabic</li>
<li>U+FECA ARABIC LETTER AIN FINAL FORM: try adding arabic</li>
<li>U+FECB ARABIC LETTER AIN INITIAL FORM: try adding arabic</li>
<li>U+FECC ARABIC LETTER AIN MEDIAL FORM: try adding arabic</li>
<li>U+FECD ARABIC LETTER GHAIN ISOLATED FORM: try adding arabic</li>
<li>U+FECE ARABIC LETTER GHAIN FINAL FORM: try adding arabic</li>
<li>U+FECF ARABIC LETTER GHAIN INITIAL FORM: try adding arabic</li>
<li>U+FED0 ARABIC LETTER GHAIN MEDIAL FORM: try adding arabic</li>
<li>U+FED1 ARABIC LETTER FEH ISOLATED FORM: try adding arabic</li>
<li>U+FED2 ARABIC LETTER FEH FINAL FORM: try adding arabic</li>
<li>U+FED3 ARABIC LETTER FEH INITIAL FORM: try adding arabic</li>
<li>U+FED4 ARABIC LETTER FEH MEDIAL FORM: try adding arabic</li>
<li>U+FED5 ARABIC LETTER QAF ISOLATED FORM: try adding arabic</li>
<li>U+FED6 ARABIC LETTER QAF FINAL FORM: try adding arabic</li>
<li>U+FED7 ARABIC LETTER QAF INITIAL FORM: try adding arabic</li>
<li>U+FED8 ARABIC LETTER QAF MEDIAL FORM: try adding arabic</li>
<li>U+FED9 ARABIC LETTER KAF ISOLATED FORM: try adding arabic</li>
<li>U+FEDA ARABIC LETTER KAF FINAL FORM: try adding arabic</li>
<li>U+FEDB ARABIC LETTER KAF INITIAL FORM: try adding arabic</li>
<li>U+FEDC ARABIC LETTER KAF MEDIAL FORM: try adding arabic</li>
<li>U+FEDD ARABIC LETTER LAM ISOLATED FORM: try adding arabic</li>
<li>U+FEDE ARABIC LETTER LAM FINAL FORM: try adding arabic</li>
<li>U+FEDF ARABIC LETTER LAM INITIAL FORM: try adding arabic</li>
<li>U+FEE0 ARABIC LETTER LAM MEDIAL FORM: try adding arabic</li>
<li>U+FEE1 ARABIC LETTER MEEM ISOLATED FORM: try adding arabic</li>
<li>U+FEE2 ARABIC LETTER MEEM FINAL FORM: try adding arabic</li>
<li>U+FEE3 ARABIC LETTER MEEM INITIAL FORM: try adding arabic</li>
<li>U+FEE4 ARABIC LETTER MEEM MEDIAL FORM: try adding arabic</li>
<li>U+FEE5 ARABIC LETTER NOON ISOLATED FORM: try adding arabic</li>
<li>U+FEE6 ARABIC LETTER NOON FINAL FORM: try adding arabic</li>
<li>U+FEE7 ARABIC LETTER NOON INITIAL FORM: try adding arabic</li>
<li>U+FEE8 ARABIC LETTER NOON MEDIAL FORM: try adding arabic</li>
<li>U+FEE9 ARABIC LETTER HEH ISOLATED FORM: try adding arabic</li>
<li>U+FEEA ARABIC LETTER HEH FINAL FORM: try adding arabic</li>
<li>U+FEEB ARABIC LETTER HEH INITIAL FORM: try adding arabic</li>
<li>U+FEEC ARABIC LETTER HEH MEDIAL FORM: try adding arabic</li>
<li>U+FEED ARABIC LETTER WAW ISOLATED FORM: try adding arabic</li>
<li>U+FEEE ARABIC LETTER WAW FINAL FORM: try adding arabic</li>
<li>U+FEEF ARABIC LETTER ALEF MAKSURA ISOLATED FORM: try adding arabic</li>
<li>U+FEF0 ARABIC LETTER ALEF MAKSURA FINAL FORM: try adding arabic</li>
<li>U+FEF1 ARABIC LETTER YEH ISOLATED FORM: try adding arabic</li>
<li>U+FEF2 ARABIC LETTER YEH FINAL FORM: try adding arabic</li>
<li>U+FEF3 ARABIC LETTER YEH INITIAL FORM: try adding arabic</li>
<li>U+FEF4 ARABIC LETTER YEH MEDIAL FORM: try adding arabic</li>
<li>U+FEF5 ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FEF6 ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FEF7 ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM: try adding arabic</li>
<li>U+FEF8 ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE FINAL FORM: try adding arabic</li>
<li>U+FEF9 ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW ISOLATED FORM: try adding arabic</li>
<li>U+FEFA ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW FINAL FORM: try adding arabic</li>
<li>U+FEFB ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM: try adding arabic</li>
<li>U+FEFC ARABIC LIGATURE LAM WITH ALEF FINAL FORM: try adding arabic</li>
<li>U+1F7D9 NINE POINTED WHITE STAR: try adding symbols</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ȋ i̒ i҃ i҄ i҅ i҆ i̦̇ i̦̊ i̦̋ ȋ̦ i̦̒ i̦҃ i̦҄ i̦҅ i̦҆ i̧̇ i̧̊ i̧̋ ȋ̧</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* angleright (U+232A): L&lt;&lt;313.0,1348.0&gt;--&lt;487.0,1079.0&gt;&gt; -&gt; L&lt;&lt;487.0,1079.0&gt;--&lt;690.0,768.0&gt;&gt;

* angleright (U+232A): L&lt;&lt;741.0,563.0&gt;--&lt;371.0,-6.0&gt;&gt; -&gt; L&lt;&lt;371.0,-6.0&gt;--&lt;303.0,-111.0&gt;&gt;

* psi (U+03C8): L&lt;&lt;471.0,-424.0&gt;--&lt;467.0,-215.0&gt;&gt; -&gt; L&lt;&lt;467.0,-215.0&gt;--&lt;467.0,-6.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;537.0,1108.0&gt;--&lt;492.0,887.0&gt;&gt; -&gt; L&lt;&lt;492.0,887.0&gt;--&lt;412.0,553.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;582.0,891.0&gt;--&lt;555.0,1014.0&gt;&gt; -&gt; L&lt;&lt;555.0,1014.0&gt;--&lt;537.0,1108.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;678.0,489.0&gt;--&lt;582.0,891.0&gt;&gt; -&gt; L&lt;&lt;582.0,891.0&gt;--&lt;555.0,1014.0&gt;&gt;

* uni046B (U+046B): L&lt;&lt;379.0,756.0&gt;--&lt;485.0,621.0&gt;&gt; -&gt; L&lt;&lt;485.0,621.0&gt;--&lt;528.0,563.0&gt;&gt;

* uni046C (U+046C): L&lt;&lt;350.0,127.0&gt;--&lt;426.0,479.0&gt;&gt; -&gt; L&lt;&lt;426.0,479.0&gt;--&lt;440.0,543.0&gt;&gt;

* uni046D (U+046D): L&lt;&lt;346.0,127.0&gt;--&lt;412.0,338.0&gt;&gt; -&gt; L&lt;&lt;412.0,338.0&gt;--&lt;426.0,379.0&gt;&gt;

* uni046D (U+046D): L&lt;&lt;412.0,338.0&gt;--&lt;426.0,379.0&gt;&gt; -&gt; L&lt;&lt;426.0,379.0&gt;--&lt;446.0,424.0&gt;&gt;

* uni0475 (U+0475): L&lt;&lt;330.0,756.0&gt;--&lt;487.0,225.0&gt;&gt; -&gt; L&lt;&lt;487.0,225.0&gt;--&lt;510.0,143.0&gt;&gt;

* uni0477 (U+0477): L&lt;&lt;332.0,756.0&gt;--&lt;492.0,225.0&gt;&gt; -&gt; L&lt;&lt;492.0,225.0&gt;--&lt;512.0,143.0&gt;&gt;

* uni0478 (U+0478): L&lt;&lt;344.0,1124.0&gt;--&lt;504.0,840.0&gt;&gt; -&gt; L&lt;&lt;504.0,840.0&gt;--&lt;539.0,768.0&gt;&gt;

* uni0482 (U+0482): L&lt;&lt;432.0,227.0&gt;--&lt;518.0,250.0&gt;&gt; -&gt; L&lt;&lt;518.0,250.0&gt;--&lt;614.0,268.0&gt;&gt;

* uni0495 (U+0495): L&lt;&lt;428.0,547.0&gt;--&lt;545.0,547.0&gt;&gt; -&gt; L&lt;&lt;545.0,547.0&gt;--&lt;625.0,545.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;479.0,127.0&gt;--&lt;479.0,365.0&gt;&gt; -&gt; L&lt;&lt;479.0,365.0&gt;--&lt;477.0,399.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;598.0,401.0&gt;--&lt;596.0,365.0&gt;&gt; -&gt; L&lt;&lt;596.0,365.0&gt;--&lt;596.0,127.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;700.0,598.0&gt;--&lt;610.0,430.0&gt;&gt; -&gt; L&lt;&lt;610.0,430.0&gt;--&lt;598.0,401.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;477.0,127.0&gt;--&lt;477.0,266.0&gt;&gt; -&gt; L&lt;&lt;477.0,266.0&gt;--&lt;475.0,293.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;594.0,756.0&gt;--&lt;594.0,539.0&gt;&gt; -&gt; L&lt;&lt;594.0,539.0&gt;--&lt;596.0,492.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;684.0,418.0&gt;--&lt;610.0,315.0&gt;&gt; -&gt; L&lt;&lt;610.0,315.0&gt;--&lt;598.0,295.0&gt;&gt;

* uni0499 (U+0499): L&lt;&lt;444.0,117.0&gt;--&lt;483.0,117.0&gt;&gt; -&gt; L&lt;&lt;483.0,117.0&gt;--&lt;508.0,115.0&gt;&gt;

* uni049C (U+049C): L&lt;&lt;498.0,813.0&gt;--&lt;526.0,844.0&gt;&gt; -&gt; L&lt;&lt;526.0,844.0&gt;--&lt;748.0,1124.0&gt;&gt;

* uni049E (U+049E): L&lt;&lt;297.0,942.0&gt;--&lt;297.0,639.0&gt;&gt; -&gt; L&lt;&lt;297.0,639.0&gt;--&lt;299.0,584.0&gt;&gt;

* uni04A0 (U+04A0): L&lt;&lt;471.0,399.0&gt;--&lt;469.0,365.0&gt;&gt; -&gt; L&lt;&lt;469.0,365.0&gt;--&lt;469.0,127.0&gt;&gt;

* uni04A0 (U+04A0): L&lt;&lt;602.0,612.0&gt;--&lt;487.0,430.0&gt;&gt; -&gt; L&lt;&lt;487.0,430.0&gt;--&lt;471.0,399.0&gt;&gt;

* uni04C5 (U+04C5): L&lt;&lt;455.0,1028.0&gt;--&lt;455.0,764.0&gt;&gt; -&gt; L&lt;&lt;455.0,764.0&gt;--&lt;453.0,733.0&gt;&gt;

* uni04C5 (U+04C5): L&lt;&lt;455.0,764.0&gt;--&lt;453.0,733.0&gt;&gt; -&gt; L&lt;&lt;453.0,733.0&gt;--&lt;453.0,696.0&gt;&gt;

* uni04CD (U+04CD): L&lt;&lt;815.0,127.0&gt;--&lt;815.0,1055.0&gt;&gt; -&gt; L&lt;&lt;815.0,1055.0&gt;--&lt;813.0,1108.0&gt;&gt;

* uni0512 (U+0512): L&lt;&lt;455.0,1028.0&gt;--&lt;455.0,764.0&gt;&gt; -&gt; L&lt;&lt;455.0,764.0&gt;--&lt;453.0,733.0&gt;&gt;

* uni0512 (U+0512): L&lt;&lt;455.0,764.0&gt;--&lt;453.0,733.0&gt;&gt; -&gt; L&lt;&lt;453.0,733.0&gt;--&lt;453.0,696.0&gt;&gt;

* uni066D (U+066D): L&lt;&lt;469.0,471.0&gt;--&lt;479.0,831.0&gt;&gt; -&gt; L&lt;&lt;479.0,831.0&gt;--&lt;479.0,842.0&gt;&gt;

* uni06CD (U+06CD): L&lt;&lt;334.0,619.0&gt;--&lt;334.0,618.0&gt;&gt; -&gt; L&lt;&lt;334.0,618.0&gt;--&lt;334.0,616.0&gt;&gt;

* uni06CD.fina: L&lt;&lt;334.0,283.0&gt;--&lt;334.0,282.0&gt;&gt; -&gt; L&lt;&lt;334.0,282.0&gt;--&lt;334.0,281.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;289.0,1092.0&gt;--&lt;354.0,1092.0&gt;&gt; -&gt; L&lt;&lt;354.0,1092.0&gt;--&lt;354.0,1092.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;354.0,1092.0&gt;--&lt;354.0,1092.0&gt;&gt; -&gt; L&lt;&lt;354.0,1092.0&gt;--&lt;455.0,1092.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;791.0,1092.0&gt;--&lt;805.0,1092.0&gt;&gt; -&gt; L&lt;&lt;805.0,1092.0&gt;--&lt;805.0,1092.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;805.0,1092.0&gt;--&lt;805.0,1092.0&gt;&gt; -&gt; L&lt;&lt;805.0,1092.0&gt;--&lt;834.0,1092.0&gt;&gt;

* uni08DB (U+08DB): L&lt;&lt;874.0,1063.0&gt;--&lt;875.0,1063.0&gt;&gt; -&gt; L&lt;&lt;875.0,1063.0&gt;--&lt;875.0,1063.0&gt;&gt;

* uni08DB (U+08DB): L&lt;&lt;875.0,1063.0&gt;--&lt;875.0,1063.0&gt;&gt; -&gt; L&lt;&lt;875.0,1063.0&gt;--&lt;883.0,1063.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;337.0,1093.0&gt;--&lt;346.0,1093.0&gt;&gt; -&gt; L&lt;&lt;346.0,1093.0&gt;--&lt;346.0,1093.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;346.0,1093.0&gt;--&lt;346.0,1093.0&gt;&gt; -&gt; L&lt;&lt;346.0,1093.0&gt;--&lt;348.0,1093.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;346.0,1093.0&gt;--&lt;348.0,1093.0&gt;&gt; -&gt; L&lt;&lt;348.0,1093.0&gt;--&lt;367.0,1093.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;650.0,1093.0&gt;--&lt;698.0,1093.0&gt;&gt; -&gt; L&lt;&lt;698.0,1093.0&gt;--&lt;698.0,1093.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;521.0,1093.0&gt;--&lt;530.0,1093.0&gt;&gt; -&gt; L&lt;&lt;530.0,1093.0&gt;--&lt;530.0,1093.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;530.0,1093.0&gt;--&lt;530.0,1093.0&gt;&gt; -&gt; L&lt;&lt;530.0,1093.0&gt;--&lt;532.0,1093.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;530.0,1093.0&gt;--&lt;532.0,1093.0&gt;&gt; -&gt; L&lt;&lt;532.0,1093.0&gt;--&lt;820.0,1093.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;668.0,1664.0&gt;--&lt;668.0,1661.0&gt;&gt; -&gt; L&lt;&lt;668.0,1661.0&gt;--&lt;668.0,1624.0&gt;&gt;

* uni203D (U+203D): L&lt;&lt;471.0,618.0&gt;--&lt;467.0,848.0&gt;&gt; -&gt; L&lt;&lt;467.0,848.0&gt;--&lt;459.0,1137.0&gt;&gt;

* uni203D (U+203D): L&lt;&lt;614.0,1135.0&gt;--&lt;612.0,999.0&gt;&gt; -&gt; L&lt;&lt;612.0,999.0&gt;--&lt;608.0,829.0&gt;&gt;

* uni2052 (U+2052): L&lt;&lt;156.0,162.0&gt;--&lt;229.0,297.0&gt;&gt; -&gt; L&lt;&lt;229.0,297.0&gt;--&lt;688.0,1145.0&gt;&gt;

* uni2052 (U+2052): L&lt;&lt;229.0,297.0&gt;--&lt;688.0,1145.0&gt;&gt; -&gt; L&lt;&lt;688.0,1145.0&gt;--&lt;799.0,1348.0&gt;&gt;

* uni2E18 (U+2E18): L&lt;&lt;428.0,-338.0&gt;--&lt;432.0,-203.0&gt;&gt; -&gt; L&lt;&lt;432.0,-203.0&gt;--&lt;434.0,-33.0&gt;&gt;

* uni2E18 (U+2E18): L&lt;&lt;571.0,178.0&gt;--&lt;575.0,-51.0&gt;&gt; -&gt; L&lt;&lt;575.0,-51.0&gt;--&lt;584.0,-340.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* Mu (U+039C): L&lt;&lt;815.0,125.0&gt;--&lt;815.0,1102.0&gt;&gt;/B&lt;&lt;815.0,1102.0&gt;-&lt;808.0,1069.0&gt;-&lt;785.5,996.0&gt;&gt; = 11.976132444203333

* uni0466 (U+0466): L&lt;&lt;662.0,553.0&gt;--&lt;678.0,489.0&gt;&gt;/L&lt;&lt;678.0,489.0&gt;--&lt;582.0,891.0&gt;&gt; = 0.6052145972453564

* uni0468 (U+0468): B&lt;&lt;703.5,960.0&gt;-&lt;696.0,1042.0&gt;-&lt;696.0,1108.0&gt;&gt;/B&lt;&lt;696.0,1108.0&gt;-&lt;690.0,960.0&gt;-&lt;673.0,824.0&gt;&gt; = 2.3215305898326966

* uni0474 (U+0474): B&lt;&lt;459.0,288.5&gt;-&lt;476.0,196.0&gt;-&lt;481.0,143.0&gt;&gt;/B&lt;&lt;481.0,143.0&gt;-&lt;483.0,187.0&gt;-&lt;501.0,286.0&gt;&gt; = 7.991873962473095

* uni0476 (U+0476): B&lt;&lt;459.0,286.5&gt;-&lt;476.0,195.0&gt;-&lt;481.0,143.0&gt;&gt;/B&lt;&lt;481.0,143.0&gt;-&lt;483.0,180.0&gt;-&lt;497.5,263.5&gt;&gt; = 8.586382616044505

* uni048A (U+048A): L&lt;&lt;283.0,1124.0&gt;--&lt;283.0,270.0&gt;&gt;/B&lt;&lt;283.0,270.0&gt;-&lt;294.0,329.0&gt;-&lt;412.5,529.5&gt;&gt; = 10.561010691196365

* uni048A (U+048A): L&lt;&lt;788.0,127.0&gt;--&lt;788.0,981.0&gt;&gt;/B&lt;&lt;788.0,981.0&gt;-&lt;783.0,949.0&gt;-&lt;746.0,878.0&gt;&gt; = 8.880659150520234

* uni04CD (U+04CD): B&lt;&lt;276.5,1044.0&gt;-&lt;265.0,1086.0&gt;-&lt;260.0,1108.0&gt;&gt;/L&lt;&lt;260.0,1108.0&gt;--&lt;260.0,127.0&gt;&gt; = 12.80426606528674

* uni04CD (U+04CD): L&lt;&lt;815.0,1055.0&gt;--&lt;813.0,1108.0&gt;&gt;/B&lt;&lt;813.0,1108.0&gt;-&lt;810.0,1087.0&gt;-&lt;794.0,1032.0&gt;&gt; = 10.291181842382318

* uni0620 (U+0620): B&lt;&lt;587.0,21.0&gt;-&lt;600.0,21.0&gt;-&lt;614.0,20.0&gt;&gt;/B&lt;&lt;614.0,20.0&gt;-&lt;570.0,14.0&gt;-&lt;520.0,12.0&gt;&gt; = 11.850782798400157

* uni0620 (U+0620): B&lt;&lt;789.0,-81.0&gt;-&lt;726.0,9.0&gt;-&lt;614.0,20.0&gt;&gt;/B&lt;&lt;614.0,20.0&gt;-&lt;725.0,35.0&gt;-&lt;786.0,76.0&gt;&gt; = 13.30532616846234

* uni08DB (U+08DB): L&lt;&lt;872.0,1028.0&gt;--&lt;872.0,1028.0&gt;&gt;/B&lt;&lt;872.0,1028.0&gt;-&lt;853.0,1029.0&gt;-&lt;841.5,1038.5&gt;&gt; = 3.012787504183286

* uni08DC (U+08DC): L&lt;&lt;825.0,1044.0&gt;--&lt;825.0,1044.0&gt;&gt;/B&lt;&lt;825.0,1044.0&gt;-&lt;792.0,1045.0&gt;-&lt;778.0,1059.0&gt;&gt; = 1.735704588928346

* uni08DD (U+08DD): L&lt;&lt;459.0,1047.0&gt;--&lt;459.0,1047.0&gt;&gt;/B&lt;&lt;459.0,1047.0&gt;-&lt;429.0,1049.0&gt;-&lt;415.0,1062.5&gt;&gt; = 3.8140748342903783

* uni200C (U+200C): B&lt;&lt;364.0,360.5&gt;-&lt;350.0,367.0&gt;-&lt;344.0,395.0&gt;&gt;/L&lt;&lt;344.0,395.0&gt;--&lt;344.0,393.0&gt;&gt; = 12.094757077012089

* uni202F (U+202F): L&lt;&lt;340.0,698.0&gt;--&lt;338.0,698.0&gt;&gt;/B&lt;&lt;338.0,698.0&gt;-&lt;356.0,694.0&gt;-&lt;376.5,686.5&gt;&gt; = 12.528807709151492
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* phi (U+03C6): L&lt;&lt;471.0,-424.0&gt;--&lt;469.0,-6.0&gt;&gt;

* uni03DA (U+03DB): L&lt;&lt;471.0,4.0&gt;--&lt;469.0,342.0&gt;&gt;

* uni03DF (U+03DF): L&lt;&lt;817.0,-121.0&gt;--&lt;821.0,438.0&gt;&gt;

* uni0622.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0623.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0625.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0627.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0671.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0672.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0673.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0773.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0774.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni08DF (U+08DF): L&lt;&lt;623.0,1094.0&gt;--&lt;768.0,1093.0&gt;&gt;

* uni08DF (U+08DF): L&lt;&lt;790.0,1046.0&gt;--&lt;643.0,1047.0&gt;&gt;

* uni0E3F (U+0E3F): L&lt;&lt;459.0,125.0&gt;--&lt;457.0,588.0&gt;&gt;

* uni0E3F (U+0E3F): L&lt;&lt;586.0,588.0&gt;--&lt;584.0,125.0&gt;&gt;

* uni1F21 (U+1F21): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F22 (U+1F22): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F23 (U+1F23): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F24 (U+1F24): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F25 (U+1F25): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F26 (U+1F26): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F74 (U+1F74): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F75 (U+1F75): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F90 (U+1F90): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F91 (U+1F91): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F92 (U+1F92): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F93 (U+1F93): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F94 (U+1F94): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F95 (U+1F95): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F96 (U+1F96): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1F97 (U+1F97): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1FC2 (U+1FC2): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1FC3 (U+1FC3): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1FC4 (U+1FC4): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1FC6 (U+1FC6): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;

* uni1FC7 (U+1FC7): L&lt;&lt;866.0,-424.0&gt;--&lt;864.0,516.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'JOOP' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 13 | 13 | 109 | 6 | 95 | 0 | 
| 0% | 0% | 6% | 6% | 46% | 3% | 40% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
