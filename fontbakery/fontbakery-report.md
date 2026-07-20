## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[12] CourierBadi[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 2193 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



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
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 2 start point differs in glyph 'uni1EBB' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni2103' between location wght=400 and location wght=700

- Contour 2 in glyph 'uni2103': becomes underweight between wght=400 and wght=700.

- Contour 3 start point differs in glyph 'uni0469' between location wght=400 and location wght=700

- Contour 4 start point differs in glyph 'uni0469' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni1ECF' between location wght=400 and location wght=700

- Contour 3 start point differs in glyph 'uni08DC' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni08DE' between location wght=400 and location wght=700

- Contour 17 start point differs in glyph 'uniFDFA' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni1EA3' between location wght=400 and location wght=700

- Contour 3 start point differs in glyph 'uni0620.medi' between location wght=400 and location wght=700

- Contour 4 start point differs in glyph 'uni0620.medi' between location wght=400 and location wght=700

- Contour 4 in glyph 'uni0620.medi': becomes underweight between wght=400 and wght=700.

- Contour 22 start point differs in glyph 'uni2061' between location wght=400 and location wght=700
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* sigma1 (U+03C2): B&lt;&lt;978.0,851.0&gt;-&lt;977.0,851.0&gt;-&lt;977.0,852.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;124.0,842.0&gt;-&lt;124.0,842.0&gt;-&lt;124.0,842.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;124.0,842.0&gt;-&lt;124.0,842.0&gt;-&lt;124.0,842.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;106.0,1165.0&gt;-&lt;106.0,1165.0&gt;-&lt;106.0,1165.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;106.0,1165.0&gt;-&lt;106.0,1165.0&gt;-&lt;106.0,1165.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;124.0,553.0&gt;-&lt;124.0,553.0&gt;-&lt;124.0,553.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;124.0,553.0&gt;-&lt;124.0,553.0&gt;-&lt;124.0,553.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;124.0,553.0&gt;-&lt;124.0,553.0&gt;-&lt;124.0,553.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;106.0,876.0&gt;-&lt;106.0,876.0&gt;-&lt;106.0,876.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;106.0,876.0&gt;-&lt;106.0,876.0&gt;-&lt;106.0,876.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;106.0,876.0&gt;-&lt;106.0,876.0&gt;-&lt;106.0,876.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.medi: B&lt;&lt;684.0,1525.0&gt;-&lt;684.0,1525.0&gt;-&lt;684.0,1525.0&gt;&gt; has the same coordinates as a previous segment.

* uni08DB (U+08DB): L&lt;&lt;160.0,1221.0&gt;--&lt;160.0,1221.0&gt;&gt; has the same coordinates as a previous segment.
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

- circumflexcomb_hookabove.cap

- circumflexcomb_tildecomb.cap

- colon.alt

- comma.alt

- commaaccent.case

- dieresis.cap

- dieresis.case

- dotaccent.case

- doublestroke_ar

- ellipsis.alt1

- ellipsis.alt2

- ellipsis.alt3

- ellipsis.alt4

- ellipsis.alt5

- emdash.alt1

- emdash.alt2

- emdash.alt3

- emdash.alt4

- fourabove_ar

- fourbelow_ar

- gafsarkashabove_ar

- grave.case

- hungarumlaut.case

- hyphen.alt

- idotaccent

- ittisal.comp

- macron.case

- miniKeheh_ar

- ogonek.case

- percent.arabic.comp

- period.alt

- perthousandzero

- rehabove_ar

- ring.case

- semicolon.alt

- stroke_ar

- tail.comp

- threeabove_ar

- threedotshorizontalbelow_ar

- tilde.case

- twoabove_ar

- uni0326.case

- uni0622.fina.alt

- uni0623.fina.alt

- uni0625.fina.alt

- uni0627.fina.alt

- uni0627.fina.short

- uni0627.fina.shorter

- uni0627.short

- uni0627.shorter

- uni0629.alt

- uni0644.medi.short

- uni066E.hah

- uni0671.fina.alt

- uni0672.fina.alt

- uni0673.fina.alt

- uni0674.narrow

- uni06BE.init.comp

- uni0773.fina.alt

- uni0774.fina.alt

- uni08AC.comp

- wasla_ar
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, hebrew, tifinagh, syriac, duployan, malayalam, todhri, canadian-aboriginal, tai-le, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: cherokee, math, syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, thai, tifinagh, syriac, cherokee, sunuwar, gothic</li>
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
<li>U+060C ARABIC COMMA: try adding one of: hanifi-rohingya, syriac, thaana, arabic, garay, yezidi, nko</li>
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
<li>U+061B ARABIC SEMICOLON: try adding one of: hanifi-rohingya, syriac, thaana, arabic, garay, yezidi, nko</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: thaana, arabic, syriac</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: hanifi-rohingya, syriac, thaana, arabic, garay, yezidi, adlam, nko</li>
<li>U+0620 ARABIC LETTER KASHMIRI YEH: try adding arabic</li>
<li>U+0621 ARABIC LETTER HAMZA: try adding one of: arabic, syriac</li>
<li>U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE: try adding arabic</li>
<li>U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW: try adding arabic</li>
<li>U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0627 ARABIC LETTER ALEF: try adding one of: arabic, indic-siyaq-numbers</li>
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
<li>U+0640 ARABIC TATWEEL: try adding one of: hanifi-rohingya, old-uyghur, mandaic, syriac, manichaean, arabic, psalter-pahlavi, adlam, sogdian</li>
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
<li>U+064B ARABIC FATHATAN: try adding one of: arabic, syriac</li>
<li>U+064C ARABIC DAMMATAN: try adding one of: arabic, syriac</li>
<li>U+064D ARABIC KASRATAN: try adding one of: arabic, syriac</li>
<li>U+064E ARABIC FATHA: try adding one of: arabic, syriac</li>
<li>U+064F ARABIC DAMMA: try adding one of: arabic, syriac</li>
<li>U+0650 ARABIC KASRA: try adding one of: arabic, syriac</li>
<li>U+0651 ARABIC SHADDA: try adding one of: arabic, syriac</li>
<li>U+0652 ARABIC SUKUN: try adding one of: arabic, syriac</li>
<li>U+0653 ARABIC MADDAH ABOVE: try adding one of: arabic, syriac</li>
<li>U+0654 ARABIC HAMZA ABOVE: try adding one of: arabic, syriac</li>
<li>U+0655 ARABIC HAMZA BELOW: try adding one of: arabic, syriac</li>
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
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: hanifi-rohingya, indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: thaana, syriac, arabic, nko</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: thaana, arabic, syriac</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: thaana, arabic, syriac</li>
<li>U+066D ARABIC FIVE POINTED STAR: try adding arabic</li>
<li>U+066E ARABIC LETTER DOTLESS BEH: try adding arabic</li>
<li>U+066F ARABIC LETTER DOTLESS QAF: try adding arabic</li>
<li>U+0670 ARABIC LETTER SUPERSCRIPT ALEF: try adding one of: arabic, syriac</li>
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
<li>U+06D4 ARABIC FULL STOP: try adding one of: hanifi-rohingya, yezidi, arabic</li>
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
<li>U+06F0 EXTENDED ARABIC-INDIC DIGIT ZERO: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F1 EXTENDED ARABIC-INDIC DIGIT ONE: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F2 EXTENDED ARABIC-INDIC DIGIT TWO: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F3 EXTENDED ARABIC-INDIC DIGIT THREE: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F4 EXTENDED ARABIC-INDIC DIGIT FOUR: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F5 EXTENDED ARABIC-INDIC DIGIT FIVE: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F6 EXTENDED ARABIC-INDIC DIGIT SIX: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F7 EXTENDED ARABIC-INDIC DIGIT SEVEN: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F8 EXTENDED ARABIC-INDIC DIGIT EIGHT: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F9 EXTENDED ARABIC-INDIC DIGIT NINE: try adding one of: arabic, indic-siyaq-numbers</li>
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
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: hanifi-rohingya, takri, yi, saurashtra, zanabazar-square, khudawadi, sinhala, lao, myanmar, tamil, phags-pa, hanunoo, dogra, duployan, kayah-li, brahmi, manichaean, balinese, bhaiksuki, tai-le, mahajani, psalter-pahlavi, tagbanwa, new-tai-lue, rejang, tibetan, gunjala-gondi, sharada, thai, oriya, chakma, syloti-nagri, tifinagh, cham, kaithi, sogdian, nko, gurmukhi, bengali, kannada, mandaic, tirhuta, buginese, siddham, kharoshthi, malayalam, thaana, arabic, devanagari, tai-viet, javanese, grantha, masaram-gondi, avestan, mongolian, sundanese, pahawh-hmong, tai-tham, warang-citi, limbu, hatran, modi, batak, buhid, tagalog, hebrew, khojki, lepcha, syriac, telugu, meetei-mayek, newa, khmer, gujarati</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: hanifi-rohingya, takri, yi, saurashtra, zanabazar-square, khudawadi, sinhala, lao, myanmar, tamil, phags-pa, hanunoo, dogra, duployan, kayah-li, brahmi, manichaean, balinese, bhaiksuki, tai-le, mahajani, psalter-pahlavi, tagbanwa, new-tai-lue, rejang, tibetan, gunjala-gondi, sharada, old-hungarian, thai, oriya, chakma, syloti-nagri, tifinagh, cham, kaithi, sogdian, nko, gurmukhi, bengali, kannada, mandaic, tirhuta, buginese, siddham, kharoshthi, malayalam, thaana, arabic, devanagari, tai-viet, javanese, grantha, masaram-gondi, avestan, mongolian, sundanese, pahawh-hmong, tai-tham, warang-citi, limbu, modi, batak, buhid, tagalog, hebrew, khojki, lepcha, syriac, telugu, meetei-mayek, newa, khmer, gujarati</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: hebrew, phags-pa, syriac, thaana, arabic, nko</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: phags-pa, hebrew, syriac, thaana, nko</li>
<li>U+2010 HYPHEN: try adding one of: armenian, lisu, yi, sora-sompeng, hebrew, kayah-li, syloti-nagri, kharoshthi, cham, arabic, kaithi, coptic, sundanese</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition</li>
<li>U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition</li>
<li>U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition</li>
<li>U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition</li>
<li>U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh</li>
<li>U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: yi, saurashtra, lao, hanunoo, duployan, manichaean, tai-le, coptic, psalter-pahlavi, new-tai-lue, sharada, kaithi, nko, bengali, buginese, music, siddham, kharoshthi, thaana, elbasan, tai-viet, sundanese, armenian, pahawh-hmong, tai-tham, limbu, canadian-aboriginal, khmer, hanifi-rohingya, zanabazar-square, sinhala, myanmar, math, rejang, ahom, marchen, thai, bassa-vah, chakma, cham, mende-kikakui, kannada, mandaic, wancho, old-permic, masaram-gondi, modi, batak, buhid, tagalog, adlam, khudawadi, miao, phags-pa, dogra, osage, brahmi, balinese, bhaiksuki, tibetan, caucasian-albanian, malayalam, devanagari, javanese, hebrew, lepcha, symbols, syriac, newa, gujarati, takri, tamil, soyombo, kayah-li, mahajani, tagbanwa, gunjala-gondi, oriya, tifinagh, syloti-nagri, sogdian, gurmukhi, tirhuta, grantha, mongolian, warang-citi, khojki, telugu, meetei-mayek</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
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
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: thaana, arabic</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: thaana, arabic</li>
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
<li>U+FE71 ARABIC TATWEEL WITH FATHATAN ABOVE: try adding arabic</li>
<li>U+FE73 ARABIC TAIL FRAGMENT: try adding arabic</li>
<li>U+FE77 ARABIC FATHA MEDIAL FORM: try adding arabic</li>
<li>U+FE79 ARABIC DAMMA MEDIAL FORM: try adding arabic</li>
<li>U+FE7B ARABIC KASRA MEDIAL FORM: try adding arabic</li>
<li>U+FE7D ARABIC SHADDA MEDIAL FORM: try adding arabic</li>
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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







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
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ȋ i̒ i҃ i҄ i҅ i҆ i̛̇ i̛̊ i̛̋ ȋ̛ i̛̒ i̛҃ i̛҄ i̛҅ i̛҆ i̦̇ i̦̊ i̦̋ ȋ̦</p>
 [code: soft-dotted]



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

<details><summary>[12] CourierBadi-Italic[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 2193 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



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
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 2 start point differs in glyph 'uni1EBB' between location wght=400 and location wght=700

- Contour 2 in glyph 'uni2103': becomes underweight between wght=400 and wght=700.

- Contour 3 start point differs in glyph 'uni0469' between location wght=400 and location wght=700

- Contour 4 start point differs in glyph 'uni0469' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni1ECF' between location wght=400 and location wght=700

- Contour 3 start point differs in glyph 'uni08DC' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni08DE' between location wght=400 and location wght=700

- Contour 17 start point differs in glyph 'uniFDFA' between location wght=400 and location wght=700

- Contour 2 start point differs in glyph 'uni1EA3' between location wght=400 and location wght=700

- Contour 3 start point differs in glyph 'uni0620.medi' between location wght=400 and location wght=700

- Contour 4 start point differs in glyph 'uni0620.medi' between location wght=400 and location wght=700

- Contour 22 start point differs in glyph 'uni2061' between location wght=400 and location wght=700
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* sigma1 (U+03C2): B&lt;&lt;1128.0,851.0&gt;-&lt;1127.0,851.0&gt;-&lt;1127.0,852.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;272.0,842.0&gt;-&lt;272.0,842.0&gt;-&lt;272.0,842.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;272.0,842.0&gt;-&lt;272.0,842.0&gt;-&lt;272.0,842.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;311.0,1165.0&gt;-&lt;311.0,1165.0&gt;-&lt;311.0,1165.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;311.0,1165.0&gt;-&lt;311.0,1165.0&gt;-&lt;311.0,1165.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;260.0,876.0&gt;-&lt;260.0,876.0&gt;-&lt;260.0,876.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;260.0,876.0&gt;-&lt;260.0,876.0&gt;-&lt;260.0,876.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: B&lt;&lt;260.0,876.0&gt;-&lt;260.0,876.0&gt;-&lt;260.0,876.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.medi: B&lt;&lt;953.0,1525.0&gt;-&lt;953.0,1525.0&gt;-&lt;953.0,1525.0&gt;&gt; has the same coordinates as a previous segment.

* uni08DB (U+08DB): L&lt;&lt;375.0,1221.0&gt;--&lt;375.0,1221.0&gt;&gt; has the same coordinates as a previous segment.
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

- circumflexcomb_hookabove.cap

- circumflexcomb_tildecomb.cap

- colon.alt

- comma.alt

- commaaccent.case

- dieresis.cap

- dieresis.case

- dotaccent.case

- doublestroke_ar

- ellipsis.alt1

- ellipsis.alt2

- ellipsis.alt3

- ellipsis.alt4

- ellipsis.alt5

- emdash.alt1

- emdash.alt2

- emdash.alt3

- emdash.alt4

- fourabove_ar

- fourbelow_ar

- gafsarkashabove_ar

- grave.case

- hungarumlaut.case

- hyphen.alt

- idotaccent

- ittisal.comp

- macron.case

- miniKeheh_ar

- ogonek.case

- percent.arabic.comp

- period.alt

- perthousandzero

- rehabove_ar

- ring.case

- semicolon.alt

- stroke_ar

- tail.comp

- threeabove_ar

- threedotshorizontalbelow_ar

- tilde.case

- twoabove_ar

- uni0326.case

- uni0622.fina.alt

- uni0623.fina.alt

- uni0625.fina.alt

- uni0627.fina.alt

- uni0627.fina.short

- uni0627.fina.shorter

- uni0627.short

- uni0627.shorter

- uni0629.alt

- uni0644.medi.short

- uni066E.hah

- uni0671.fina.alt

- uni0672.fina.alt

- uni0673.fina.alt

- uni0674.narrow

- uni06BE.init.comp

- uni0773.fina.alt

- uni0774.fina.alt

- uni08AC.comp

- wasla_ar
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, hebrew, tifinagh, syriac, duployan, malayalam, todhri, canadian-aboriginal, tai-le, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: cherokee, math, syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, thai, tifinagh, syriac, cherokee, sunuwar, gothic</li>
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
<li>U+060C ARABIC COMMA: try adding one of: hanifi-rohingya, syriac, thaana, arabic, garay, yezidi, nko</li>
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
<li>U+061B ARABIC SEMICOLON: try adding one of: hanifi-rohingya, syriac, thaana, arabic, garay, yezidi, nko</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: thaana, arabic, syriac</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: hanifi-rohingya, syriac, thaana, arabic, garay, yezidi, adlam, nko</li>
<li>U+0620 ARABIC LETTER KASHMIRI YEH: try adding arabic</li>
<li>U+0621 ARABIC LETTER HAMZA: try adding one of: arabic, syriac</li>
<li>U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE: try adding arabic</li>
<li>U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW: try adding arabic</li>
<li>U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0627 ARABIC LETTER ALEF: try adding one of: arabic, indic-siyaq-numbers</li>
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
<li>U+0640 ARABIC TATWEEL: try adding one of: hanifi-rohingya, old-uyghur, mandaic, syriac, manichaean, arabic, psalter-pahlavi, adlam, sogdian</li>
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
<li>U+064B ARABIC FATHATAN: try adding one of: arabic, syriac</li>
<li>U+064C ARABIC DAMMATAN: try adding one of: arabic, syriac</li>
<li>U+064D ARABIC KASRATAN: try adding one of: arabic, syriac</li>
<li>U+064E ARABIC FATHA: try adding one of: arabic, syriac</li>
<li>U+064F ARABIC DAMMA: try adding one of: arabic, syriac</li>
<li>U+0650 ARABIC KASRA: try adding one of: arabic, syriac</li>
<li>U+0651 ARABIC SHADDA: try adding one of: arabic, syriac</li>
<li>U+0652 ARABIC SUKUN: try adding one of: arabic, syriac</li>
<li>U+0653 ARABIC MADDAH ABOVE: try adding one of: arabic, syriac</li>
<li>U+0654 ARABIC HAMZA ABOVE: try adding one of: arabic, syriac</li>
<li>U+0655 ARABIC HAMZA BELOW: try adding one of: arabic, syriac</li>
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
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: hanifi-rohingya, indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: indic-siyaq-numbers, syriac, thaana, arabic, yezidi</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: thaana, syriac, arabic, nko</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: thaana, arabic, syriac</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: thaana, arabic, syriac</li>
<li>U+066D ARABIC FIVE POINTED STAR: try adding arabic</li>
<li>U+066E ARABIC LETTER DOTLESS BEH: try adding arabic</li>
<li>U+066F ARABIC LETTER DOTLESS QAF: try adding arabic</li>
<li>U+0670 ARABIC LETTER SUPERSCRIPT ALEF: try adding one of: arabic, syriac</li>
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
<li>U+06D4 ARABIC FULL STOP: try adding one of: hanifi-rohingya, yezidi, arabic</li>
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
<li>U+06F0 EXTENDED ARABIC-INDIC DIGIT ZERO: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F1 EXTENDED ARABIC-INDIC DIGIT ONE: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F2 EXTENDED ARABIC-INDIC DIGIT TWO: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F3 EXTENDED ARABIC-INDIC DIGIT THREE: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F4 EXTENDED ARABIC-INDIC DIGIT FOUR: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F5 EXTENDED ARABIC-INDIC DIGIT FIVE: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F6 EXTENDED ARABIC-INDIC DIGIT SIX: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F7 EXTENDED ARABIC-INDIC DIGIT SEVEN: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F8 EXTENDED ARABIC-INDIC DIGIT EIGHT: try adding one of: arabic, indic-siyaq-numbers</li>
<li>U+06F9 EXTENDED ARABIC-INDIC DIGIT NINE: try adding one of: arabic, indic-siyaq-numbers</li>
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
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: hanifi-rohingya, takri, yi, saurashtra, zanabazar-square, khudawadi, sinhala, lao, myanmar, tamil, phags-pa, hanunoo, dogra, duployan, kayah-li, brahmi, manichaean, balinese, bhaiksuki, tai-le, mahajani, psalter-pahlavi, tagbanwa, new-tai-lue, rejang, tibetan, gunjala-gondi, sharada, thai, oriya, chakma, syloti-nagri, tifinagh, cham, kaithi, sogdian, nko, gurmukhi, bengali, kannada, mandaic, tirhuta, buginese, siddham, kharoshthi, malayalam, thaana, arabic, devanagari, tai-viet, javanese, grantha, masaram-gondi, avestan, mongolian, sundanese, pahawh-hmong, tai-tham, warang-citi, limbu, hatran, modi, batak, buhid, tagalog, hebrew, khojki, lepcha, syriac, telugu, meetei-mayek, newa, khmer, gujarati</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: hanifi-rohingya, takri, yi, saurashtra, zanabazar-square, khudawadi, sinhala, lao, myanmar, tamil, phags-pa, hanunoo, dogra, duployan, kayah-li, brahmi, manichaean, balinese, bhaiksuki, tai-le, mahajani, psalter-pahlavi, tagbanwa, new-tai-lue, rejang, tibetan, gunjala-gondi, sharada, old-hungarian, thai, oriya, chakma, syloti-nagri, tifinagh, cham, kaithi, sogdian, nko, gurmukhi, bengali, kannada, mandaic, tirhuta, buginese, siddham, kharoshthi, malayalam, thaana, arabic, devanagari, tai-viet, javanese, grantha, masaram-gondi, avestan, mongolian, sundanese, pahawh-hmong, tai-tham, warang-citi, limbu, modi, batak, buhid, tagalog, hebrew, khojki, lepcha, syriac, telugu, meetei-mayek, newa, khmer, gujarati</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: hebrew, phags-pa, syriac, thaana, arabic, nko</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: phags-pa, hebrew, syriac, thaana, nko</li>
<li>U+2010 HYPHEN: try adding one of: armenian, lisu, yi, sora-sompeng, hebrew, kayah-li, syloti-nagri, kharoshthi, cham, arabic, kaithi, coptic, sundanese</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition</li>
<li>U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition</li>
<li>U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition</li>
<li>U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition</li>
<li>U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh</li>
<li>U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: yi, saurashtra, lao, hanunoo, duployan, manichaean, tai-le, coptic, psalter-pahlavi, new-tai-lue, sharada, kaithi, nko, bengali, buginese, music, siddham, kharoshthi, thaana, elbasan, tai-viet, sundanese, armenian, pahawh-hmong, tai-tham, limbu, canadian-aboriginal, khmer, hanifi-rohingya, zanabazar-square, sinhala, myanmar, math, rejang, ahom, marchen, thai, bassa-vah, chakma, cham, mende-kikakui, kannada, mandaic, wancho, old-permic, masaram-gondi, modi, batak, buhid, tagalog, adlam, khudawadi, miao, phags-pa, dogra, osage, brahmi, balinese, bhaiksuki, tibetan, caucasian-albanian, malayalam, devanagari, javanese, hebrew, lepcha, symbols, syriac, newa, gujarati, takri, tamil, soyombo, kayah-li, mahajani, tagbanwa, gunjala-gondi, oriya, tifinagh, syloti-nagri, sogdian, gurmukhi, tirhuta, grantha, mongolian, warang-citi, khojki, telugu, meetei-mayek</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
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
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: thaana, arabic</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: thaana, arabic</li>
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
<li>U+FE71 ARABIC TATWEEL WITH FATHATAN ABOVE: try adding arabic</li>
<li>U+FE73 ARABIC TAIL FRAGMENT: try adding arabic</li>
<li>U+FE77 ARABIC FATHA MEDIAL FORM: try adding arabic</li>
<li>U+FE79 ARABIC DAMMA MEDIAL FORM: try adding arabic</li>
<li>U+FE7B ARABIC KASRA MEDIAL FORM: try adding arabic</li>
<li>U+FE7D ARABIC SHADDA MEDIAL FORM: try adding arabic</li>
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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







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
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ȋ i̒ i҃ i҄ i҅ i҆ i̛̇ i̛̊ i̛̋ ȋ̛ i̛̒ i̛҃ i̛҄ i̛҅ i̛҆ i̦̇ i̦̊ i̦̋ ȋ̦</p>
 [code: soft-dotted]



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
| 0 | 0 | 0 | 24 | 171 | 15 | 245 | 0 | 
| 0% | 0% | 0% | 5% | 38% | 3% | 54% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
