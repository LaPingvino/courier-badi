## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[14] CourierBadi-BoldItalic.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;Version 0.900; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: alphatonos	Contours detected: 4	Expected: 3

- Glyph name: iotatonos	Contours detected: 1	Expected: 2

- Glyph name: alpha	Contours detected: 3	Expected: 2

- Glyph name: kappa	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 4	Expected: 2

- Glyph name: uni0428	Contours detected: 3	Expected: 1

- Glyph name: uni0429	Contours detected: 3	Expected: 1

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni0436	Contours detected: 3	Expected: 1

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni0466	Contours detected: 4	Expected: 2

- Glyph name: uni0467	Contours detected: 4	Expected: 2

- Glyph name: uni0468	Contours detected: 3	Expected: 2

- Glyph name: uni0469	Contours detected: 5	Expected: 2

- Glyph name: uni046C	Contours detected: 3	Expected: 2

- Glyph name: uni046D	Contours detected: 3	Expected: 2

- Glyph name: uni046E	Contours detected: 1	Expected: 2

- Glyph name: uni046F	Contours detected: 1	Expected: 2

- Glyph name: uni0476	Contours detected: 2	Expected: 3

- Glyph name: uni0477	Contours detected: 2	Expected: 3

- Glyph name: uni0478	Contours detected: 2	Expected: 3

- Glyph name: uni0479	Contours detected: 2	Expected: 3

- Glyph name: uni048C	Contours detected: 4	Expected: 2

- Glyph name: uni0497	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni049D	Contours detected: 2	Expected: 1

- Glyph name: uni049E	Contours detected: 3	Expected: 1

- Glyph name: uni04A1	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 3	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C2	Contours detected: 4	Expected: 2

- Glyph name: uni04DD	Contours detected: 5	Expected: 3

- Glyph name: uni04F2	Contours detected: 2	Expected: 3

- Glyph name: uni04F3	Contours detected: 2	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

- Glyph name: uni1EA4	Contours detected: 3	Expected: 4

- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

- Glyph name: uni1EAD	Contours detected: 3	Expected: 4

- Glyph name: uni1EAF	Contours detected: 3	Expected: 4

- Glyph name: uni1EB7	Contours detected: 3	Expected: 4

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni1EBE	Contours detected: 2	Expected: 3

- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

- Glyph name: uni1ECC	Contours detected: 2	Expected: 3

- Glyph name: uni1ECD	Contours detected: 2	Expected: 3

- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

- Glyph name: uni1ED0	Contours detected: 3	Expected: 4

- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

- Glyph name: uni1ED8	Contours detected: 3	Expected: 4

- Glyph name: uni1ED9	Contours detected: 3	Expected: 4

- Glyph name: uni1EDD	Contours detected: 2	Expected: 3

- Glyph name: uni1EDF	Contours detected: 2	Expected: 3

- Glyph name: uni1EE4	Contours detected: 1	Expected: 2

- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

- Glyph name: uni1F00	Contours detected: 4	Expected: 3

- Glyph name: uni1F01	Contours detected: 4	Expected: 3

- Glyph name: uni1F03	Contours detected: 5	Expected: 4

- Glyph name: uni1F07	Contours detected: 5	Expected: 4

- Glyph name: uni1F0A	Contours detected: 3	Expected: 4

- Glyph name: uni1F0C	Contours detected: 3	Expected: 4

- Glyph name: uni1F0D	Contours detected: 3	Expected: 4

- Glyph name: uni1F0E	Contours detected: 3	Expected: 4

- Glyph name: uni1F12	Contours detected: 2	Expected: 3

- Glyph name: uni1F14	Contours detected: 2	Expected: 3

- Glyph name: uni1F15	Contours detected: 2	Expected: 3

- Glyph name: uni1F1A	Contours detected: 2	Expected: 3

- Glyph name: uni1F1C	Contours detected: 2	Expected: 3

- Glyph name: uni1F1D	Contours detected: 2	Expected: 3

- Glyph name: uni1F22	Contours detected: 2	Expected: 3

- Glyph name: uni1F24	Contours detected: 2	Expected: 3

- Glyph name: uni1F25	Contours detected: 2	Expected: 3

- Glyph name: uni1F26	Contours detected: 2	Expected: 3

- Glyph name: uni1F2A	Contours detected: 2	Expected: 3

- Glyph name: uni1F2C	Contours detected: 2	Expected: 3

- Glyph name: uni1F2D	Contours detected: 2	Expected: 3

- Glyph name: uni1F2E	Contours detected: 2	Expected: 3

- Glyph name: uni1F30	Contours detected: 1	Expected: 2

- Glyph name: uni1F32	Contours detected: 2	Expected: 3

- Glyph name: uni1F34	Contours detected: 2	Expected: 3

- Glyph name: uni1F35	Contours detected: 2	Expected: 3

- Glyph name: uni1F36	Contours detected: 1	Expected: 3

- Glyph name: uni1F3A	Contours detected: 2	Expected: 3

- Glyph name: uni1F3C	Contours detected: 2	Expected: 3

- Glyph name: uni1F3D	Contours detected: 2	Expected: 3

- Glyph name: uni1F3E	Contours detected: 2	Expected: 3

- Glyph name: uni1F42	Contours detected: 3	Expected: 4

- Glyph name: uni1F44	Contours detected: 3	Expected: 4

- Glyph name: uni1F45	Contours detected: 3	Expected: 4

- Glyph name: uni1F4A	Contours detected: 3	Expected: 4

- Glyph name: uni1F4C	Contours detected: 3	Expected: 4

- Glyph name: uni1F4D	Contours detected: 3	Expected: 4

- Glyph name: uni1F52	Contours detected: 2	Expected: 3

- Glyph name: uni1F54	Contours detected: 2	Expected: 3

- Glyph name: uni1F55	Contours detected: 2	Expected: 3

- Glyph name: uni1F56	Contours detected: 2	Expected: 3

- Glyph name: uni1F5D	Contours detected: 2	Expected: 3

- Glyph name: uni1F62	Contours detected: 2	Expected: 3

- Glyph name: uni1F64	Contours detected: 2	Expected: 3

- Glyph name: uni1F65	Contours detected: 2	Expected: 3

- Glyph name: uni1F66	Contours detected: 2	Expected: 3

- Glyph name: uni1F6A	Contours detected: 2	Expected: 3

- Glyph name: uni1F6C	Contours detected: 2	Expected: 3

- Glyph name: uni1F6D	Contours detected: 2	Expected: 3

- Glyph name: uni1F6E	Contours detected: 2	Expected: 3

- Glyph name: uni1F70	Contours detected: 4	Expected: 3

- Glyph name: uni1F71	Contours detected: 4	Expected: 3

- Glyph name: uni1F76	Contours detected: 1	Expected: 2

- Glyph name: uni1F77	Contours detected: 1	Expected: 2

- Glyph name: uni1F80	Contours detected: 5	Expected: 4

- Glyph name: uni1F81	Contours detected: 5	Expected: 4

- Glyph name: uni1F83	Contours detected: 6	Expected: 5

- Glyph name: uni1F87	Contours detected: 6	Expected: 5

- Glyph name: uni1F8A	Contours detected: 4	Expected: 5

- Glyph name: uni1F8C	Contours detected: 4	Expected: 5

- Glyph name: uni1F8D	Contours detected: 4	Expected: 5

- Glyph name: uni1F8E	Contours detected: 4	Expected: 5

- Glyph name: uni1F92	Contours detected: 3	Expected: 4

- Glyph name: uni1F94	Contours detected: 3	Expected: 4

- Glyph name: uni1F95	Contours detected: 3	Expected: 4

- Glyph name: uni1F96	Contours detected: 3	Expected: 4

- Glyph name: uni1F9A	Contours detected: 3	Expected: 4

- Glyph name: uni1F9C	Contours detected: 3	Expected: 4

- Glyph name: uni1F9D	Contours detected: 3	Expected: 4

- Glyph name: uni1F9E	Contours detected: 3	Expected: 4

- Glyph name: uni1FA2	Contours detected: 3	Expected: 4

- Glyph name: uni1FA4	Contours detected: 3	Expected: 4

- Glyph name: uni1FA5	Contours detected: 3	Expected: 4

- Glyph name: uni1FA6	Contours detected: 3	Expected: 4

- Glyph name: uni1FAA	Contours detected: 3	Expected: 4

- Glyph name: uni1FAC	Contours detected: 3	Expected: 4

- Glyph name: uni1FAD	Contours detected: 3	Expected: 4

- Glyph name: uni1FAE	Contours detected: 3	Expected: 4

- Glyph name: uni1FB0	Contours detected: 4	Expected: 3

- Glyph name: uni1FB1	Contours detected: 4	Expected: 3

- Glyph name: uni1FB2	Contours detected: 5	Expected: 4

- Glyph name: uni1FB3	Contours detected: 4	Expected: 3

- Glyph name: uni1FB4	Contours detected: 5	Expected: 4

- Glyph name: uni1FB6	Contours detected: 4	Expected: 3

- Glyph name: uni1FB7	Contours detected: 5	Expected: 4

- Glyph name: uni1FC1	Contours detected: 2	Expected: 3

- Glyph name: uni1FCD	Contours detected: 1	Expected: 2

- Glyph name: uni1FCE	Contours detected: 1	Expected: 2

- Glyph name: uni1FCF	Contours detected: 1	Expected: 2

- Glyph name: uni1FD7	Contours detected: 3	Expected: 4

- Glyph name: uni1FD9	Contours detected: 4	Expected: 2

- Glyph name: uni1FDE	Contours detected: 1	Expected: 2

- Glyph name: uni1FE7	Contours detected: 1	Expected: 4

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: lira	Contours detected: 3	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: uni26AD	Contours detected: 8	Expected: 4

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: alpha	Contours detected: 3	Expected: 2

- Glyph name: alphatonos	Contours detected: 4	Expected: 3

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: iotatonos	Contours detected: 1	Expected: 2

- Glyph name: kappa	Contours detected: 2	Expected: 1

- Glyph name: lira	Contours detected: 3	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 4	Expected: 2

- Glyph name: uni0428	Contours detected: 3	Expected: 1

- Glyph name: uni0429	Contours detected: 3	Expected: 1

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni0436	Contours detected: 3	Expected: 1

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni0466	Contours detected: 4	Expected: 2

- Glyph name: uni0467	Contours detected: 4	Expected: 2

- Glyph name: uni0468	Contours detected: 3	Expected: 2

- Glyph name: uni0469	Contours detected: 5	Expected: 2

- Glyph name: uni046C	Contours detected: 3	Expected: 2

- Glyph name: uni046D	Contours detected: 3	Expected: 2

- Glyph name: uni046E	Contours detected: 1	Expected: 2

- Glyph name: uni046F	Contours detected: 1	Expected: 2

- Glyph name: uni0476	Contours detected: 2	Expected: 3

- Glyph name: uni0477	Contours detected: 2	Expected: 3

- Glyph name: uni0478	Contours detected: 2	Expected: 3

- Glyph name: uni0479	Contours detected: 2	Expected: 3

- Glyph name: uni048C	Contours detected: 4	Expected: 2

- Glyph name: uni0497	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni049D	Contours detected: 2	Expected: 1

- Glyph name: uni049E	Contours detected: 3	Expected: 1

- Glyph name: uni04A1	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 3	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C2	Contours detected: 4	Expected: 2

- Glyph name: uni04DD	Contours detected: 5	Expected: 3

- Glyph name: uni04F2	Contours detected: 2	Expected: 3

- Glyph name: uni04F3	Contours detected: 2	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

- Glyph name: uni1EA4	Contours detected: 3	Expected: 4

- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

- Glyph name: uni1EAD	Contours detected: 3	Expected: 4

- Glyph name: uni1EAF	Contours detected: 3	Expected: 4

- Glyph name: uni1EB7	Contours detected: 3	Expected: 4

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni1EBE	Contours detected: 2	Expected: 3

- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

- Glyph name: uni1ECC	Contours detected: 2	Expected: 3

- Glyph name: uni1ECD	Contours detected: 2	Expected: 3

- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

- Glyph name: uni1ED0	Contours detected: 3	Expected: 4

- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

- Glyph name: uni1ED8	Contours detected: 3	Expected: 4

- Glyph name: uni1ED9	Contours detected: 3	Expected: 4

- Glyph name: uni1EDD	Contours detected: 2	Expected: 3

- Glyph name: uni1EDF	Contours detected: 2	Expected: 3

- Glyph name: uni1EE4	Contours detected: 1	Expected: 2

- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

- Glyph name: uni1F00	Contours detected: 4	Expected: 3

- Glyph name: uni1F01	Contours detected: 4	Expected: 3

- Glyph name: uni1F03	Contours detected: 5	Expected: 4

- Glyph name: uni1F07	Contours detected: 5	Expected: 4

- Glyph name: uni1F0A	Contours detected: 3	Expected: 4

- Glyph name: uni1F0C	Contours detected: 3	Expected: 4

- Glyph name: uni1F0D	Contours detected: 3	Expected: 4

- Glyph name: uni1F0E	Contours detected: 3	Expected: 4

- Glyph name: uni1F12	Contours detected: 2	Expected: 3

- Glyph name: uni1F14	Contours detected: 2	Expected: 3

- Glyph name: uni1F15	Contours detected: 2	Expected: 3

- Glyph name: uni1F1A	Contours detected: 2	Expected: 3

- Glyph name: uni1F1C	Contours detected: 2	Expected: 3

- Glyph name: uni1F1D	Contours detected: 2	Expected: 3

- Glyph name: uni1F22	Contours detected: 2	Expected: 3

- Glyph name: uni1F24	Contours detected: 2	Expected: 3

- Glyph name: uni1F25	Contours detected: 2	Expected: 3

- Glyph name: uni1F26	Contours detected: 2	Expected: 3

- Glyph name: uni1F2A	Contours detected: 2	Expected: 3

- Glyph name: uni1F2C	Contours detected: 2	Expected: 3

- Glyph name: uni1F2D	Contours detected: 2	Expected: 3

- Glyph name: uni1F2E	Contours detected: 2	Expected: 3

- Glyph name: uni1F30	Contours detected: 1	Expected: 2

- Glyph name: uni1F32	Contours detected: 2	Expected: 3

- Glyph name: uni1F34	Contours detected: 2	Expected: 3

- Glyph name: uni1F35	Contours detected: 2	Expected: 3

- Glyph name: uni1F36	Contours detected: 1	Expected: 3

- Glyph name: uni1F3A	Contours detected: 2	Expected: 3

- Glyph name: uni1F3C	Contours detected: 2	Expected: 3

- Glyph name: uni1F3D	Contours detected: 2	Expected: 3

- Glyph name: uni1F3E	Contours detected: 2	Expected: 3

- Glyph name: uni1F42	Contours detected: 3	Expected: 4

- Glyph name: uni1F44	Contours detected: 3	Expected: 4

- Glyph name: uni1F45	Contours detected: 3	Expected: 4

- Glyph name: uni1F4A	Contours detected: 3	Expected: 4

- Glyph name: uni1F4C	Contours detected: 3	Expected: 4

- Glyph name: uni1F4D	Contours detected: 3	Expected: 4

- Glyph name: uni1F52	Contours detected: 2	Expected: 3

- Glyph name: uni1F54	Contours detected: 2	Expected: 3

- Glyph name: uni1F55	Contours detected: 2	Expected: 3

- Glyph name: uni1F56	Contours detected: 2	Expected: 3

- Glyph name: uni1F5D	Contours detected: 2	Expected: 3

- Glyph name: uni1F62	Contours detected: 2	Expected: 3

- Glyph name: uni1F64	Contours detected: 2	Expected: 3

- Glyph name: uni1F65	Contours detected: 2	Expected: 3

- Glyph name: uni1F66	Contours detected: 2	Expected: 3

- Glyph name: uni1F6A	Contours detected: 2	Expected: 3

- Glyph name: uni1F6C	Contours detected: 2	Expected: 3

- Glyph name: uni1F6D	Contours detected: 2	Expected: 3

- Glyph name: uni1F6E	Contours detected: 2	Expected: 3

- Glyph name: uni1F70	Contours detected: 4	Expected: 3

- Glyph name: uni1F71	Contours detected: 4	Expected: 3

- Glyph name: uni1F76	Contours detected: 1	Expected: 2

- Glyph name: uni1F77	Contours detected: 1	Expected: 2

- Glyph name: uni1F80	Contours detected: 5	Expected: 4

- Glyph name: uni1F81	Contours detected: 5	Expected: 4

- Glyph name: uni1F83	Contours detected: 6	Expected: 5

- Glyph name: uni1F87	Contours detected: 6	Expected: 5

- Glyph name: uni1F8A	Contours detected: 4	Expected: 5

- Glyph name: uni1F8C	Contours detected: 4	Expected: 5

- Glyph name: uni1F8D	Contours detected: 4	Expected: 5

- Glyph name: uni1F8E	Contours detected: 4	Expected: 5

- Glyph name: uni1F92	Contours detected: 3	Expected: 4

- Glyph name: uni1F94	Contours detected: 3	Expected: 4

- Glyph name: uni1F95	Contours detected: 3	Expected: 4

- Glyph name: uni1F96	Contours detected: 3	Expected: 4

- Glyph name: uni1F9A	Contours detected: 3	Expected: 4

- Glyph name: uni1F9C	Contours detected: 3	Expected: 4

- Glyph name: uni1F9D	Contours detected: 3	Expected: 4

- Glyph name: uni1F9E	Contours detected: 3	Expected: 4

- Glyph name: uni1FA2	Contours detected: 3	Expected: 4

- Glyph name: uni1FA4	Contours detected: 3	Expected: 4

- Glyph name: uni1FA5	Contours detected: 3	Expected: 4

- Glyph name: uni1FA6	Contours detected: 3	Expected: 4

- Glyph name: uni1FAA	Contours detected: 3	Expected: 4

- Glyph name: uni1FAC	Contours detected: 3	Expected: 4

- Glyph name: uni1FAD	Contours detected: 3	Expected: 4

- Glyph name: uni1FAE	Contours detected: 3	Expected: 4

- Glyph name: uni1FB0	Contours detected: 4	Expected: 3

- Glyph name: uni1FB1	Contours detected: 4	Expected: 3

- Glyph name: uni1FB2	Contours detected: 5	Expected: 4

- Glyph name: uni1FB3	Contours detected: 4	Expected: 3

- Glyph name: uni1FB4	Contours detected: 5	Expected: 4

- Glyph name: uni1FB6	Contours detected: 4	Expected: 3

- Glyph name: uni1FB7	Contours detected: 5	Expected: 4

- Glyph name: uni1FC1	Contours detected: 2	Expected: 3

- Glyph name: uni1FCD	Contours detected: 1	Expected: 2

- Glyph name: uni1FCE	Contours detected: 1	Expected: 2

- Glyph name: uni1FCF	Contours detected: 1	Expected: 2

- Glyph name: uni1FD7	Contours detected: 3	Expected: 4

- Glyph name: uni1FD9	Contours detected: 4	Expected: 2

- Glyph name: uni1FDE	Contours detected: 1	Expected: 2

- Glyph name: uni1FE7	Contours detected: 1	Expected: 4

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: uni26AD	Contours detected: 8	Expected: 4

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* alpha (U+03B1): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* alphatonos (U+03AC): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni0605 (U+0605): B&lt;&lt;419.0,1469.0&gt;-&lt;419.0,1469.0&gt;-&lt;419.0,1469.0&gt;&gt; has the same coordinates as a previous segment.

* uni0663 (U+06F3): L&lt;&lt;801.0,1070.0&gt;--&lt;801.0,1070.0&gt;&gt; has the same coordinates as a previous segment.

* uni06C2.fina: B&lt;&lt;898.0,1248.0&gt;-&lt;897.0,1255.0&gt;-&lt;902.0,1248.0&gt;&gt; has the same coordinates as a previous segment.

* uni06E4 (U+06E4): B&lt;&lt;557.0,1600.0&gt;-&lt;555.0,1602.0&gt;-&lt;556.0,1600.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D (U+077D): L&lt;&lt;932.0,1503.0&gt;--&lt;932.0,1503.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.fina: L&lt;&lt;839.0,1503.0&gt;--&lt;839.0,1503.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.init: L&lt;&lt;1090.0,1503.0&gt;--&lt;1090.0,1503.0&gt;&gt; has the same coordinates as a previous segment.

* uni08D4 (U+08D4): B&lt;&lt;446.0,1237.0&gt;-&lt;446.0,1237.0&gt;-&lt;445.0,1238.0&gt;&gt; has the same coordinates as a previous segment.

* uni08DD (U+08DD): B&lt;&lt;820.0,1285.0&gt;-&lt;820.0,1285.0&gt;-&lt;820.0,1284.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F00 (U+1F00): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F01 (U+1F01): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F02 (U+1F02): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F03 (U+1F03): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F04 (U+1F04): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F05 (U+1F05): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F06 (U+1F06): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F07 (U+1F07): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F70 (U+1F70): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F71 (U+1F71): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F80 (U+1F80): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F81 (U+1F81): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F82 (U+1F82): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F83 (U+1F83): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F84 (U+1F84): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F85 (U+1F85): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F86 (U+1F86): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F87 (U+1F87): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB0 (U+1FB0): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB1 (U+1FB1): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB2 (U+1FB2): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB3 (U+1FB3): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB4 (U+1FB4): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB6 (U+1FB6): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB7 (U+1FB7): B&lt;&lt;915.0,160.0&gt;-&lt;915.0,160.0&gt;-&lt;915.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FD9 (U+1FD9): B&lt;&lt;478.0,1445.0&gt;-&lt;485.0,1451.0&gt;-&lt;484.0,1445.0&gt;&gt; has the same coordinates as a previous segment.

* uni203B (U+203B): L&lt;&lt;659.0,830.0&gt;--&lt;633.0,861.0&gt;&gt; has the same coordinates as a previous segment.

* uni26AD (U+26AD): B&lt;&lt;709.0,1019.0&gt;-&lt;710.0,1018.0&gt;-&lt;711.0,1019.0&gt;&gt; has the same coordinates as a previous segment.

* uni26AD (U+26AD): B&lt;&lt;554.0,884.0&gt;-&lt;554.0,884.0&gt;-&lt;554.0,885.0&gt;&gt; has the same coordinates as a previous segment.

* uni26AD (U+26AD): B&lt;&lt;467.0,386.0&gt;-&lt;467.0,386.0&gt;-&lt;466.0,389.0&gt;&gt; has the same coordinates as a previous segment.

* uni26AD (U+26AD): B&lt;&lt;586.0,236.0&gt;-&lt;585.0,237.0&gt;-&lt;585.0,236.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE00 (U+FE00): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE01 (U+FE01): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE02 (U+FE02): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE02 (U+FE02): B&lt;&lt;764.0,863.0&gt;-&lt;861.0,857.0&gt;-&lt;847.0,769.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE03 (U+FE03): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE04 (U+FE04): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE04 (U+FE04): B&lt;&lt;634.0,859.0&gt;-&lt;638.0,862.0&gt;-&lt;637.0,855.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE06 (U+FE06): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0A (U+FE0A): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0B (U+FE0B): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0C (U+FE0C): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0C (U+FE0C): B&lt;&lt;938.0,863.0&gt;-&lt;1035.0,857.0&gt;-&lt;1021.0,769.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0D (U+FE0D): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0E (U+FE0E): B&lt;&lt;512.5,1014.5&gt;-&lt;510.0,1017.0&gt;-&lt;516.0,1016.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0E (U+FE0E): B&lt;&lt;808.0,859.0&gt;-&lt;812.0,862.0&gt;-&lt;811.0,855.0&gt;&gt; has the same coordinates as a previous segment.
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
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, canadian-aboriginal, hebrew, tai-le, todhri, old-permic, malayalam, math, syriac, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
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
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, math, cherokee</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, thai, sunuwar, cherokee, gothic, syriac, caucasian-albanian</li>
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
<li>U+060C ARABIC COMMA: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
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
<li>U+061B ARABIC SEMICOLON: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: arabic, syriac, thaana</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: arabic, yezidi, hanifi-rohingya, garay, adlam, syriac, nko, thaana</li>
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
<li>U+0640 ARABIC TATWEEL: try adding one of: arabic, old-uyghur, mandaic, psalter-pahlavi, hanifi-rohingya, adlam, manichaean, syriac, sogdian</li>
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
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: arabic, yezidi, hanifi-rohingya, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: arabic, syriac, nko, thaana</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: arabic, syriac, thaana</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: arabic, syriac, thaana</li>
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
<li>U+06D4 ARABIC FULL STOP: try adding one of: arabic, hanifi-rohingya, yezidi</li>
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
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, dogra, tagbanwa, duployan, batak, hatran, mandaic, cham, khojki, hanunoo, hebrew, javanese, masaram-gondi, mongolian, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, siddham, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, old-hungarian, dogra, tagbanwa, duployan, batak, mandaic, masaram-gondi, cham, khojki, hanunoo, hebrew, javanese, mongolian, siddham, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: arabic, hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+2010 HYPHEN: try adding one of: arabic, cham, yi, hebrew, sundanese, lisu, kharoshthi, armenian, sora-sompeng, syloti-nagri, kaithi, kayah-li, coptic</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
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
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: telugu, math, manichaean, sharada, tamil, duployan, batak, kharoshthi, sogdian, gurmukhi, symbols, saurashtra, balinese, soyombo, khudawadi, gujarati, bhaiksuki, myanmar, nko, grantha, lepcha, khojki, caucasian-albanian, gunjala-gondi, bengali, mende-kikakui, buginese, tai-viet, dogra, tagbanwa, siddham, cham, mongolian, hanunoo, zanabazar-square, bassa-vah, limbu, tirhuta, tibetan, warang-citi, marchen, new-tai-lue, hanifi-rohingya, syloti-nagri, canadian-aboriginal, pahawh-hmong, tai-tham, masaram-gondi, mandaic, yi, javanese, hebrew, adlam, rejang, tifinagh, sundanese, phags-pa, malayalam, devanagari, elbasan, syriac, kayah-li, psalter-pahlavi, music, oriya, tai-le, armenian, tagalog, sinhala, mahajani, meetei-mayek, old-permic, brahmi, osage, thai, takri, modi, kaithi, newa, wancho, chakma, khmer, coptic, miao, buhid, ahom, lao, kannada, thaana</li>
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
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: arabic, thaana</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: arabic, thaana</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, phags-pa, yi</li>
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
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* uni2062 (U+2062) has a counter-clockwise outer contour

* uni2062 (U+2062) has a counter-clockwise outer contour

* uni2062 (U+2062) has a counter-clockwise outer contour

* uni2062 (U+2062) has a counter-clockwise outer contour

* uni2063 (U+2063) has a counter-clockwise outer contour

* uni2063 (U+2063) has a counter-clockwise outer contour

* uni2063 (U+2063) has a counter-clockwise outer contour

* uni2063 (U+2063) has a counter-clockwise outer contour

* uni2064 (U+2064) has a counter-clockwise outer contour

* uni2064 (U+2064) has a counter-clockwise outer contour

* uni2064 (U+2064) has a counter-clockwise outer contour

* uni2064 (U+2064) has a counter-clockwise outer contour

* uniFE05 (U+FE05) has a counter-clockwise outer contour

* uniFE05 (U+FE05) has a counter-clockwise outer contour

* uniFE05 (U+FE05) has a counter-clockwise outer contour

* uniFE05 (U+FE05) has a counter-clockwise outer contour

* uniFE07 (U+FE07) has a counter-clockwise outer contour

* uniFE07 (U+FE07) has a counter-clockwise outer contour

* uniFE07 (U+FE07) has a counter-clockwise outer contour

* uniFE07 (U+FE07) has a counter-clockwise outer contour

* uniFE08 (U+FE08) has a counter-clockwise outer contour

* uniFE08 (U+FE08) has a counter-clockwise outer contour

* uniFE08 (U+FE08) has a counter-clockwise outer contour

* uniFE08 (U+FE08) has a counter-clockwise outer contour

* uniFE09 (U+FE09) has a counter-clockwise outer contour

* uniFE09 (U+FE09) has a counter-clockwise outer contour

* uniFE09 (U+FE09) has a counter-clockwise outer contour

* uniFE09 (U+FE09) has a counter-clockwise outer contour

* uniFE0F (U+FE0F) has a counter-clockwise outer contour

* uniFE0F (U+FE0F) has a counter-clockwise outer contour

* uniFE0F (U+FE0F) has a counter-clockwise outer contour

* uniFE0F (U+FE0F) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* Alpha (U+0391): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* Alphatonos (U+0386): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* Eta (U+0397): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* Eta (U+0397): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* Etatonos (U+0389): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* Etatonos (U+0389): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* Mu (U+039C): L&lt;&lt;804.0,133.0&gt;--&lt;951.0,968.0&gt;&gt;/B&lt;&lt;951.0,968.0&gt;-&lt;927.0,893.0&gt;-&lt;889.5,804.5&gt;&gt; = 7.760180116716171

* Nu (U+039D): L&lt;&lt;496.0,1064.0&gt;--&lt;363.0,121.0&gt;&gt;/L&lt;&lt;363.0,121.0&gt;--&lt;378.0,159.0&gt;&gt; = 13.512974637501017

* OE (U+0152): L&lt;&lt;669.0,-24.0&gt;--&lt;624.0,-31.0&gt;&gt;/L&lt;&lt;624.0,-31.0&gt;--&lt;624.0,-31.0&gt;&gt; = 8.84181456019167

* Omega (U+2126): B&lt;&lt;231.0,181.5&gt;-&lt;228.0,160.0&gt;-&lt;213.0,157.0&gt;&gt;/L&lt;&lt;213.0,157.0&gt;--&lt;314.0,153.0&gt;&gt; = 13.577887009926041

* Pi (U+03A0): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* Threedotsinverted.alt.comp: B&lt;&lt;356.0,-558.0&gt;-&lt;393.0,-578.0&gt;-&lt;429.0,-626.0&gt;&gt;/B&lt;&lt;429.0,-626.0&gt;-&lt;416.0,-596.0&gt;-&lt;417.0,-574.0&gt;&gt; = 13.441204837098612

* Threedotsinverted.alt.comp: B&lt;&lt;511.0,-732.0&gt;-&lt;484.0,-710.0&gt;-&lt;462.0,-681.0&gt;&gt;/B&lt;&lt;462.0,-681.0&gt;-&lt;476.0,-713.0&gt;-&lt;475.0,-735.0&gt;&gt; = 13.55532872257627

* Xi (U+039E): B&lt;&lt;1031.0,1073.0&gt;-&lt;1033.0,1093.0&gt;-&lt;1053.0,1096.0&gt;&gt;/L&lt;&lt;1053.0,1096.0&gt;--&lt;419.0,1096.0&gt;&gt; = 8.530765609948139

* aogonek (U+0105): L&lt;&lt;854.0,54.0&gt;--&lt;895.0,89.0&gt;&gt;/B&lt;&lt;895.0,89.0&gt;-&lt;818.0,26.0&gt;-&lt;713.0,-15.0&gt;&gt; = 1.1966046794981087

* arrowdown (U+2193): L&lt;&lt;850.0,1174.0&gt;--&lt;695.0,296.0&gt;&gt;/B&lt;&lt;695.0,296.0&gt;-&lt;724.0,371.0&gt;-&lt;797.5,410.0&gt;&gt; = 11.128122326465709

* arrowleft (U+2190): B&lt;&lt;514.0,802.0&gt;-&lt;475.0,743.0&gt;-&lt;418.0,732.0&gt;&gt;/L&lt;&lt;418.0,732.0&gt;--&lt;1034.0,732.0&gt;&gt; = 10.922804719869259

* arrowright (U+2192): B&lt;&lt;780.5,451.5&gt;-&lt;819.0,510.0&gt;-&lt;876.0,521.0&gt;&gt;/L&lt;&lt;876.0,521.0&gt;--&lt;260.0,521.0&gt;&gt; = 10.922804719869259

* arrowup (U+2191): L&lt;&lt;442.0,78.0&gt;--&lt;597.0,955.0&gt;&gt;/B&lt;&lt;597.0,955.0&gt;-&lt;568.0,880.0&gt;-&lt;494.5,841.5&gt;&gt; = 11.116937818919084

* asteriskmath (U+2217): B&lt;&lt;783.0,847.0&gt;-&lt;769.0,795.0&gt;-&lt;748.0,766.0&gt;&gt;/B&lt;&lt;748.0,766.0&gt;-&lt;774.0,796.0&gt;-&lt;821.5,823.5&gt;&gt; = 5.004660140847415

* at (U+0040): L&lt;&lt;890.0,730.0&gt;--&lt;889.0,728.0&gt;&gt;/L&lt;&lt;889.0,728.0&gt;--&lt;903.0,767.0&gt;&gt; = 6.818214571651848

* b (U+0062): B&lt;&lt;467.5,-6.5&gt;-&lt;386.0,42.0&gt;-&lt;352.0,115.0&gt;&gt;/L&lt;&lt;352.0,115.0&gt;--&lt;375.0,49.0&gt;&gt; = 5.761239088697751

* b (U+0062): L&lt;&lt;597.0,1251.0&gt;--&lt;514.0,782.0&gt;&gt;/B&lt;&lt;514.0,782.0&gt;-&lt;546.0,878.0&gt;-&lt;633.0,928.5&gt;&gt; = 8.39909464785244

* d (U+0064): B&lt;&lt;915.0,928.5&gt;-&lt;988.0,878.0&gt;-&lt;992.0,793.0&gt;&gt;/L&lt;&lt;992.0,793.0&gt;--&lt;1074.0,1263.0&gt;&gt; = 12.59095625752517

* dcaron (U+010F): B&lt;&lt;841.0,930.5&gt;-&lt;898.0,882.0&gt;-&lt;891.0,803.0&gt;&gt;/L&lt;&lt;891.0,803.0&gt;--&lt;972.0,1263.0&gt;&gt; = 4.923044911624951

* eng (U+014B): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* five (U+0035): L&lt;&lt;630.0,1010.0&gt;--&lt;569.0,730.0&gt;&gt;/B&lt;&lt;569.0,730.0&gt;-&lt;587.0,781.0&gt;-&lt;642.0,800.5&gt;&gt; = 7.149777434278611

* fourbelow_ar: B&lt;&lt;834.0,1674.5&gt;-&lt;870.0,1638.0&gt;-&lt;864.0,1613.0&gt;&gt;/B&lt;&lt;864.0,1613.0&gt;-&lt;875.0,1642.0&gt;-&lt;895.0,1662.0&gt;&gt; = 7.2765214012499815

* g (U+0067): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* g (U+0067): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* gamma (U+03B3): B&lt;&lt;550.5,813.5&gt;-&lt;619.0,703.0&gt;-&lt;661.0,458.0&gt;&gt;/B&lt;&lt;661.0,458.0&gt;-&lt;657.0,501.0&gt;-&lt;679.5,557.0&gt;&gt; = 4.413032881456779

* gbreve (U+011F): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* gbreve (U+011F): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* gcaron (U+01E7): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* gcaron (U+01E7): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* gcircumflex (U+011D): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* gcircumflex (U+011D): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* gdotaccent (U+0121): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* gdotaccent (U+0121): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* h (U+0068): L&lt;&lt;607.0,1251.0&gt;--&lt;513.0,722.0&gt;&gt;/B&lt;&lt;513.0,722.0&gt;-&lt;543.0,802.0&gt;-&lt;605.5,859.5&gt;&gt; = 10.480113582115342

* hcircumflex (U+0125): L&lt;&lt;607.0,1251.0&gt;--&lt;513.0,722.0&gt;&gt;/B&lt;&lt;513.0,722.0&gt;-&lt;543.0,802.0&gt;-&lt;605.5,859.5&gt;&gt; = 10.480113582115342

* kappa (U+03BA): L&lt;&lt;416.0,686.0&gt;--&lt;392.0,584.0&gt;&gt;/B&lt;&lt;392.0,584.0&gt;-&lt;405.0,621.0&gt;-&lt;451.0,678.0&gt;&gt; = 6.118474260507514

* lira (U+20A4): B&lt;&lt;197.5,358.0&gt;-&lt;259.0,386.0&gt;-&lt;324.0,392.0&gt;&gt;/L&lt;&lt;324.0,392.0&gt;--&lt;245.0,392.0&gt;&gt; = 5.273895957351716

* lira (U+20A4): B&lt;&lt;351.5,164.5&gt;-&lt;396.0,174.0&gt;-&lt;408.0,190.0&gt;&gt;/B&lt;&lt;408.0,190.0&gt;-&lt;399.0,179.0&gt;-&lt;380.0,181.0&gt;&gt; = 2.419509216656149

* lira (U+20A4): B&lt;&lt;422.0,384.0&gt;-&lt;425.0,391.0&gt;-&lt;435.0,392.0&gt;&gt;/L&lt;&lt;435.0,392.0&gt;--&lt;387.0,392.0&gt;&gt; = 5.710593137499633

* lira (U+20A4): L&lt;&lt;270.0,603.0&gt;--&lt;373.0,601.0&gt;&gt;/B&lt;&lt;373.0,601.0&gt;-&lt;354.0,605.0&gt;-&lt;348.0,623.5&gt;&gt; = 10.776258423330173

* lira (U+20A4): L&lt;&lt;435.0,392.0&gt;--&lt;387.0,392.0&gt;&gt;/B&lt;&lt;387.0,392.0&gt;-&lt;409.0,390.0&gt;-&lt;422.0,384.0&gt;&gt; = 5.1944289077348

* lira (U+20A4): L&lt;&lt;703.0,650.0&gt;--&lt;520.0,651.0&gt;&gt;/B&lt;&lt;520.0,651.0&gt;-&lt;542.0,649.0&gt;-&lt;548.5,630.5&gt;&gt; = 4.881340332714145

* m (U+006D): B&lt;&lt;801.5,890.5&gt;-&lt;821.0,850.0&gt;-&lt;807.0,799.0&gt;&gt;/B&lt;&lt;807.0,799.0&gt;-&lt;850.0,882.0&gt;-&lt;921.0,930.5&gt;&gt; = 12.037285664651744

* musicalnote (U+266A): B&lt;&lt;859.0,509.5&gt;-&lt;844.0,563.0&gt;-&lt;850.0,619.0&gt;&gt;/L&lt;&lt;850.0,619.0&gt;--&lt;787.0,260.0&gt;&gt; = 3.837839462607157

* n (U+006E): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* nacute (U+0144): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* ncaron (U+0148): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* nine (U+0039): B&lt;&lt;724.0,284.5&gt;-&lt;874.0,397.0&gt;-&lt;936.0,579.0&gt;&gt;/B&lt;&lt;936.0,579.0&gt;-&lt;906.0,499.0&gt;-&lt;826.5,461.0&gt;&gt; = 1.7441559170643288

* ntilde (U+00F1): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* ohorn (U+01A1): B&lt;&lt;694.0,933.0&gt;-&lt;803.0,933.0&gt;-&lt;886.0,881.0&gt;&gt;/B&lt;&lt;886.0,881.0&gt;-&lt;883.0,884.0&gt;-&lt;892.0,887.0&gt;&gt; = 12.932608396739491

* p (U+0070): B&lt;&lt;476.0,-4.5&gt;-&lt;403.0,46.0&gt;-&lt;399.0,131.0&gt;&gt;/L&lt;&lt;399.0,131.0&gt;--&lt;317.0,-339.0&gt;&gt; = 12.5909562575252

* partialdiff (U+2202): B&lt;&lt;877.5,716.0&gt;-&lt;957.0,668.0&gt;-&lt;989.0,589.0&gt;&gt;/B&lt;&lt;989.0,589.0&gt;-&lt;983.0,625.0&gt;-&lt;989.5,660.5&gt;&gt; = 12.588740511051117

* prescription (U+211E): B&lt;&lt;937.5,468.0&gt;-&lt;937.0,451.0&gt;-&lt;924.0,436.0&gt;&gt;/L&lt;&lt;924.0,436.0&gt;--&lt;1031.0,516.0&gt;&gt; = 12.301491195077974

* prescription (U+211E): L&lt;&lt;167.0,133.0&gt;--&lt;343.0,1130.0&gt;&gt;/L&lt;&lt;343.0,1130.0&gt;--&lt;326.0,1092.0&gt;&gt; = 14.090976346486968

* q (U+0071): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* q (U+0071): L&lt;&lt;794.0,-327.0&gt;--&lt;877.0,142.0&gt;&gt;/B&lt;&lt;877.0,142.0&gt;-&lt;845.0,46.0&gt;-&lt;758.0,-4.5&gt;&gt; = 8.39909464785244

* r (U+0072): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* racute (U+0155): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* rcaron (U+0159): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* rho (U+03C1): B&lt;&lt;365.5,-10.5&gt;-&lt;289.0,24.0&gt;-&lt;234.0,85.0&gt;&gt;/B&lt;&lt;234.0,85.0&gt;-&lt;245.0,67.0&gt;-&lt;243.0,7.0&gt;&gt; = 10.609498250997696

* six (U+0036): B&lt;&lt;713.0,902.5&gt;-&lt;563.0,790.0&gt;-&lt;502.0,608.0&gt;&gt;/B&lt;&lt;502.0,608.0&gt;-&lt;532.0,688.0&gt;-&lt;611.5,726.0&gt;&gt; = 2.0267047530402036

* thorn (U+00FE): B&lt;&lt;476.0,-4.5&gt;-&lt;403.0,46.0&gt;-&lt;399.0,131.0&gt;&gt;/L&lt;&lt;399.0,131.0&gt;--&lt;317.0,-339.0&gt;&gt; = 12.5909562575252

* thorn (U+00FE): L&lt;&lt;597.0,1251.0&gt;--&lt;515.0,788.0&gt;&gt;/B&lt;&lt;515.0,788.0&gt;-&lt;548.0,882.0&gt;-&lt;636.0,930.5&gt;&gt; = 9.301055783192934

* threequarters (U+00BE): B&lt;&lt;717.5,1089.0&gt;-&lt;682.0,1048.0&gt;-&lt;644.0,1045.0&gt;&gt;/B&lt;&lt;644.0,1045.0&gt;-&lt;684.0,1046.0&gt;-&lt;713.0,996.0&gt;&gt; = 3.0818922738363885

* trademark (U+2122): L&lt;&lt;1261.0,817.0&gt;--&lt;1303.0,1044.0&gt;&gt;/L&lt;&lt;1303.0,1044.0&gt;--&lt;1224.0,861.0&gt;&gt; = 12.867128787769872

* u (U+0075): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uacute (U+00FA): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* ubreve (U+016D): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* ucircumflex (U+00FB): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* udieresis (U+00FC): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* ugrave (U+00F9): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uhorn (U+01B0): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uhungarumlaut (U+0171): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* umacron (U+016B): L&lt;&lt;865.0,61.0&gt;--&lt;917.0,186.0&gt;&gt;/B&lt;&lt;917.0,186.0&gt;-&lt;877.0,121.0&gt;-&lt;809.0,66.5&gt;&gt; = 9.020191714883174

* uni00B3 (U+00B3): B&lt;&lt;1071.5,972.0&gt;-&lt;1030.0,923.0&gt;-&lt;982.0,916.0&gt;&gt;/B&lt;&lt;982.0,916.0&gt;-&lt;1032.0,914.0&gt;-&lt;1066.0,855.5&gt;&gt; = 10.587755012475341

* uni0123 (U+0123): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* uni0123 (U+0123): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* uni0146 (U+0146): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* uni0157 (U+0157): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* uni01D4 (U+01D4): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni01D8 (U+01D8): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni01DA (U+01DA): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni01DC (U+01DC): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni01EB (U+01EB): B&lt;&lt;343.5,-90.0&gt;-&lt;394.0,-34.0&gt;-&lt;452.0,-33.0&gt;&gt;/B&lt;&lt;452.0,-33.0&gt;-&lt;357.0,-17.0&gt;-&lt;283.5,50.0&gt;&gt; = 10.547856880526076

* uni01F5 (U+01F5): B&lt;&lt;923.5,930.5&gt;-&lt;1005.0,882.0&gt;-&lt;1039.0,809.0&gt;&gt;/L&lt;&lt;1039.0,809.0&gt;--&lt;1016.0,875.0&gt;&gt; = 5.761239088697751

* uni01F5 (U+01F5): L&lt;&lt;850.0,-11.0&gt;--&lt;889.0,167.0&gt;&gt;/B&lt;&lt;889.0,167.0&gt;-&lt;854.0,85.0&gt;-&lt;766.5,40.0&gt;&gt; = 10.755922924009178

* uni0211 (U+0211): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* uni0215 (U+0215): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni034F (U+034F): L&lt;&lt;1128.0,1211.0&gt;--&lt;1138.0,1211.0&gt;&gt;/L&lt;&lt;1138.0,1211.0&gt;--&lt;1013.0,1208.0&gt;&gt; = 1.3748347805694

* uni034F (U+034F): L&lt;&lt;1157.0,1222.0&gt;--&lt;1126.0,1054.0&gt;&gt;/L&lt;&lt;1126.0,1054.0&gt;--&lt;1128.0,1065.0&gt;&gt; = 0.14998860898616947

* uni03BC (U+03BC): B&lt;&lt;438.5,-40.0&gt;-&lt;398.0,-24.0&gt;-&lt;405.0,15.0&gt;&gt;/L&lt;&lt;405.0,15.0&gt;--&lt;343.0,-339.0&gt;&gt; = 0.24141337268377072

* uni03BC (U+03BC): L&lt;&lt;856.0,61.0&gt;--&lt;907.0,165.0&gt;&gt;/B&lt;&lt;907.0,165.0&gt;-&lt;871.0,107.0&gt;-&lt;811.5,57.0&gt;&gt; = 5.7048250576346025

* uni03DA (U+03DB): L&lt;&lt;438.0,8.0&gt;--&lt;495.0,344.0&gt;&gt;/L&lt;&lt;495.0,344.0&gt;--&lt;489.0,312.0&gt;&gt; = 0.9914991476679391

* uni03DE (U+03DE): B&lt;&lt;470.0,1030.0&gt;-&lt;469.0,1013.0&gt;-&lt;469.0,1014.0&gt;&gt;/B&lt;&lt;469.0,1014.0&gt;-&lt;461.0,969.0&gt;-&lt;446.5,893.5&gt;&gt; = 10.08059798754231

* uni03DF (U+03DF): B&lt;&lt;470.0,1030.0&gt;-&lt;469.0,1013.0&gt;-&lt;469.0,1014.0&gt;&gt;/B&lt;&lt;469.0,1014.0&gt;-&lt;461.0,969.0&gt;-&lt;446.5,893.5&gt;&gt; = 10.08059798754231

* uni03E0 (U+03E0): B&lt;&lt;384.0,153.5&gt;-&lt;413.0,150.0&gt;-&lt;407.0,140.0&gt;&gt;/L&lt;&lt;407.0,140.0&gt;--&lt;594.0,636.0&gt;&gt; = 10.306504476680358

* uni03E0 (U+03E0): L&lt;&lt;407.0,140.0&gt;--&lt;594.0,636.0&gt;&gt;/B&lt;&lt;594.0,636.0&gt;-&lt;592.0,631.0&gt;-&lt;581.0,663.0&gt;&gt; = 1.1441574309585407

* uni0409 (U+0409): L&lt;&lt;909.0,544.0&gt;--&lt;908.0,570.0&gt;&gt;/L&lt;&lt;908.0,570.0&gt;--&lt;837.0,170.0&gt;&gt; = 12.267767514525653

* uni040A (U+040A): L&lt;&lt;111.0,144.0&gt;--&lt;272.0,1055.0&gt;&gt;/L&lt;&lt;272.0,1055.0&gt;--&lt;258.0,1017.0&gt;&gt; = 10.202528777299715

* uni040A (U+040A): L&lt;&lt;877.0,544.0&gt;--&lt;876.0,570.0&gt;&gt;/L&lt;&lt;876.0,570.0&gt;--&lt;805.0,170.0&gt;&gt; = 12.267767514525653

* uni0416 (U+0416): L&lt;&lt;530.0,145.0&gt;--&lt;603.0,556.0&gt;&gt;/L&lt;&lt;603.0,556.0&gt;--&lt;587.0,520.0&gt;&gt; = 13.890900229507837

* uni0416 (U+0416): L&lt;&lt;629.0,705.0&gt;--&lt;690.0,1053.0&gt;&gt;/L&lt;&lt;690.0,1053.0&gt;--&lt;682.0,1017.0&gt;&gt; = 2.586587914347925

* uni0416 (U+0416): L&lt;&lt;819.0,544.0&gt;--&lt;747.0,133.0&gt;&gt;/L&lt;&lt;747.0,133.0&gt;--&lt;755.0,170.0&gt;&gt; = 2.264078783952361

* uni041C (U+041C): L&lt;&lt;138.0,145.0&gt;--&lt;324.0,1056.0&gt;&gt;/L&lt;&lt;324.0,1056.0&gt;--&lt;308.0,1017.0&gt;&gt; = 10.766655626074428

* uni0425 (U+0425): L&lt;&lt;703.0,467.0&gt;--&lt;406.0,117.0&gt;&gt;/L&lt;&lt;406.0,117.0&gt;--&lt;461.0,170.0&gt;&gt; = 5.743927417239676

* uni0428 (U+0428): L&lt;&lt;946.0,150.0&gt;--&lt;1105.0,1055.0&gt;&gt;/L&lt;&lt;1105.0,1055.0&gt;--&lt;1096.0,1017.0&gt;&gt; = 3.3598971434017373

* uni0429 (U+0429): L&lt;&lt;946.0,150.0&gt;--&lt;1105.0,1055.0&gt;&gt;/L&lt;&lt;1105.0,1055.0&gt;--&lt;1096.0,1017.0&gt;&gt; = 3.3598971434017373

* uni0436 (U+0436): B&lt;&lt;535.0,855.0&gt;-&lt;544.0,834.0&gt;-&lt;551.0,812.0&gt;&gt;/B&lt;&lt;551.0,812.0&gt;-&lt;546.0,836.0&gt;-&lt;550.0,862.0&gt;&gt; = 5.881835287909446

* uni0436 (U+0436): L&lt;&lt;608.0,587.0&gt;--&lt;644.0,788.0&gt;&gt;/L&lt;&lt;644.0,788.0&gt;--&lt;635.0,754.0&gt;&gt; = 4.672213390155418

* uni0436 (U+0436): L&lt;&lt;793.0,399.0&gt;--&lt;747.0,135.0&gt;&gt;/L&lt;&lt;747.0,135.0&gt;--&lt;756.0,170.0&gt;&gt; = 4.536649119988902

* uni0436 (U+0436): L&lt;&lt;978.0,842.0&gt;--&lt;977.0,840.0&gt;&gt;/B&lt;&lt;977.0,840.0&gt;-&lt;985.0,851.0&gt;-&lt;994.0,863.0&gt;&gt; = 9.462322208025574

* uni0440 (U+0440): L&lt;&lt;409.0,127.0&gt;--&lt;409.0,130.0&gt;&gt;/L&lt;&lt;409.0,130.0&gt;--&lt;339.0,-246.0&gt;&gt; = 10.546034013090223

* uni0441 (U+0441): L&lt;&lt;1021.0,891.0&gt;--&lt;1021.0,890.0&gt;&gt;/B&lt;&lt;1021.0,890.0&gt;-&lt;1031.0,934.0&gt;-&lt;1059.0,958.0&gt;&gt; = 12.80426606528674

* uni0444 (U+0444): L&lt;&lt;671.0,944.0&gt;--&lt;671.0,940.0&gt;&gt;/L&lt;&lt;671.0,940.0&gt;--&lt;718.0,1157.0&gt;&gt; = 12.220919331930418

* uni0445 (U+0445): L&lt;&lt;626.0,754.0&gt;--&lt;581.0,801.0&gt;&gt;/L&lt;&lt;581.0,801.0&gt;--&lt;721.0,592.0&gt;&gt; = 9.938227112104135

* uni0447 (U+0447): L&lt;&lt;851.0,154.0&gt;--&lt;879.0,318.0&gt;&gt;/B&lt;&lt;879.0,318.0&gt;-&lt;868.0,290.0&gt;-&lt;837.5,274.0&gt;&gt; = 11.758949766738523

* uni0448 (U+0448): L&lt;&lt;1280.0,754.0&gt;--&lt;1281.0,781.0&gt;&gt;/L&lt;&lt;1281.0,781.0&gt;--&lt;1167.0,132.0&gt;&gt; = 7.841550489789624

* uni0448 (U+0448): L&lt;&lt;1281.0,781.0&gt;--&lt;1167.0,132.0&gt;&gt;/L&lt;&lt;1167.0,132.0&gt;--&lt;1175.0,170.0&gt;&gt; = 1.9260111531767365

* uni0448 (U+0448): L&lt;&lt;440.0,754.0&gt;--&lt;441.0,781.0&gt;&gt;/L&lt;&lt;441.0,781.0&gt;--&lt;326.0,144.0&gt;&gt; = 8.112496548575002

* uni0448 (U+0448): L&lt;&lt;539.0,153.0&gt;--&lt;649.0,792.0&gt;&gt;/L&lt;&lt;649.0,792.0&gt;--&lt;641.0,754.0&gt;&gt; = 2.1212648378613297

* uni0448 (U+0448): L&lt;&lt;865.0,754.0&gt;--&lt;866.0,781.0&gt;&gt;/L&lt;&lt;866.0,781.0&gt;--&lt;751.0,144.0&gt;&gt; = 8.112496548575002

* uni0449 (U+0449): L&lt;&lt;1280.0,754.0&gt;--&lt;1281.0,781.0&gt;&gt;/L&lt;&lt;1281.0,781.0&gt;--&lt;1167.0,135.0&gt;&gt; = 7.886883404779876

* uni0449 (U+0449): L&lt;&lt;440.0,754.0&gt;--&lt;441.0,781.0&gt;&gt;/L&lt;&lt;441.0,781.0&gt;--&lt;326.0,144.0&gt;&gt; = 8.112496548575002

* uni0449 (U+0449): L&lt;&lt;539.0,153.0&gt;--&lt;649.0,792.0&gt;&gt;/L&lt;&lt;649.0,792.0&gt;--&lt;641.0,754.0&gt;&gt; = 2.1212648378613297

* uni0449 (U+0449): L&lt;&lt;865.0,754.0&gt;--&lt;866.0,781.0&gt;&gt;/L&lt;&lt;866.0,781.0&gt;--&lt;751.0,144.0&gt;&gt; = 8.112496548575002

* uni044B (U+044B): L&lt;&lt;133.0,144.0&gt;--&lt;247.0,792.0&gt;&gt;/L&lt;&lt;247.0,792.0&gt;--&lt;239.0,754.0&gt;&gt; = 1.9109454194774027

* uni044B (U+044B): L&lt;&lt;927.0,144.0&gt;--&lt;1041.0,792.0&gt;&gt;/L&lt;&lt;1041.0,792.0&gt;--&lt;1033.0,754.0&gt;&gt; = 1.9109454194774027

* uni044D (U+044D): B&lt;&lt;944.0,331.0&gt;-&lt;956.0,346.0&gt;-&lt;973.0,350.0&gt;&gt;/L&lt;&lt;973.0,350.0&gt;--&lt;601.0,350.0&gt;&gt; = 13.240519915187184

* uni044D (U+044D): L&lt;&lt;625.0,554.0&gt;--&lt;1027.0,554.0&gt;&gt;/B&lt;&lt;1027.0,554.0&gt;-&lt;1005.0,557.0&gt;-&lt;997.5,577.5&gt;&gt; = 7.765166018425308

* uni044E (U+044E): L&lt;&lt;133.0,144.0&gt;--&lt;247.0,792.0&gt;&gt;/L&lt;&lt;247.0,792.0&gt;--&lt;239.0,754.0&gt;&gt; = 1.9109454194774027

* uni0452 (U+0452): L&lt;&lt;577.0,938.0&gt;--&lt;546.0,747.0&gt;&gt;/B&lt;&lt;546.0,747.0&gt;-&lt;561.0,787.0&gt;-&lt;594.0,815.5&gt;&gt; = 11.337119081476002

* uni0454 (U+0454): L&lt;&lt;1021.0,891.0&gt;--&lt;1021.0,890.0&gt;&gt;/B&lt;&lt;1021.0,890.0&gt;-&lt;1031.0,934.0&gt;-&lt;1059.0,958.0&gt;&gt; = 12.80426606528674

* uni0454 (U+0454): L&lt;&lt;763.0,350.0&gt;--&lt;363.0,350.0&gt;&gt;/B&lt;&lt;363.0,350.0&gt;-&lt;386.0,349.0&gt;-&lt;394.0,331.0&gt;&gt; = 2.4895529219991284

* uni045A (U+045A): L&lt;&lt;133.0,144.0&gt;--&lt;247.0,792.0&gt;&gt;/L&lt;&lt;247.0,792.0&gt;--&lt;239.0,754.0&gt;&gt; = 1.9109454194774027

* uni045A (U+045A): L&lt;&lt;682.0,553.0&gt;--&lt;714.0,789.0&gt;&gt;/L&lt;&lt;714.0,789.0&gt;--&lt;706.0,754.0&gt;&gt; = 5.153175759481367

* uni045B (U+045B): L&lt;&lt;577.0,938.0&gt;--&lt;546.0,747.0&gt;&gt;/B&lt;&lt;546.0,747.0&gt;-&lt;561.0,787.0&gt;-&lt;594.0,815.5&gt;&gt; = 11.337119081476002

* uni0463 (U+0463): B&lt;&lt;282.0,915.0&gt;-&lt;286.0,914.0&gt;-&lt;282.0,915.0&gt;&gt;/L&lt;&lt;282.0,915.0&gt;--&lt;347.0,894.0&gt;&gt; = 3.868204038321649

* uni0465 (U+0465): B&lt;&lt;969.0,919.5&gt;-&lt;1004.0,906.0&gt;-&lt;1018.0,892.0&gt;&gt;/B&lt;&lt;1018.0,892.0&gt;-&lt;1013.0,898.0&gt;-&lt;1033.0,911.5&gt;&gt; = 5.1944289077347285

* uni0466 (U+0466): L&lt;&lt;483.0,408.0&gt;--&lt;360.0,117.0&gt;&gt;/B&lt;&lt;360.0,117.0&gt;-&lt;366.0,130.0&gt;-&lt;375.0,128.0&gt;&gt; = 1.862312172060252

* uni0468 (U+0468): B&lt;&lt;828.5,648.5&gt;-&lt;828.0,697.0&gt;-&lt;833.0,760.0&gt;&gt;/B&lt;&lt;833.0,760.0&gt;-&lt;817.0,709.0&gt;-&lt;800.5,660.0&gt;&gt; = 12.880198284296151

* uni0468 (U+0468): L&lt;&lt;322.0,404.0&gt;--&lt;279.0,126.0&gt;&gt;/B&lt;&lt;279.0,126.0&gt;-&lt;287.0,146.0&gt;-&lt;308.5,138.0&gt;&gt; = 13.00879119653384

* uni0468 (U+0468): L&lt;&lt;353.0,563.0&gt;--&lt;590.0,587.0&gt;&gt;/B&lt;&lt;590.0,587.0&gt;-&lt;573.0,588.0&gt;-&lt;575.5,602.5&gt;&gt; = 9.148852985793845

* uni0468 (U+0468): L&lt;&lt;73.0,158.0&gt;--&lt;244.0,1128.0&gt;&gt;/B&lt;&lt;244.0,1128.0&gt;-&lt;236.0,1109.0&gt;-&lt;218.0,1113.0&gt;&gt; = 12.835783612302572

* uni0469 (U+0469): B&lt;&lt;586.0,148.0&gt;-&lt;592.0,147.0&gt;-&lt;592.0,138.0&gt;&gt;/L&lt;&lt;592.0,138.0&gt;--&lt;604.0,193.0&gt;&gt; = 12.308015817427924

* uni0469 (U+0469): L&lt;&lt;401.0,722.0&gt;--&lt;404.0,748.0&gt;&gt;/L&lt;&lt;404.0,748.0&gt;--&lt;335.0,382.0&gt;&gt; = 4.094411027517732

* uni0469 (U+0469): L&lt;&lt;592.0,138.0&gt;--&lt;604.0,193.0&gt;&gt;/L&lt;&lt;604.0,193.0&gt;--&lt;586.0,148.0&gt;&gt; = 9.49339366892388

* uni0469 (U+0469): L&lt;&lt;807.0,215.0&gt;--&lt;795.0,139.0&gt;&gt;/B&lt;&lt;795.0,139.0&gt;-&lt;798.0,146.0&gt;-&lt;810.0,143.0&gt;&gt; = 14.225963898751806

* uni0469 (U+0469): L&lt;&lt;810.0,143.0&gt;--&lt;807.0,215.0&gt;&gt;/L&lt;&lt;807.0,215.0&gt;--&lt;795.0,139.0&gt;&gt; = 11.358570645285178

* uni046A (U+046A): L&lt;&lt;425.0,396.0&gt;--&lt;273.0,115.0&gt;&gt;/B&lt;&lt;273.0,115.0&gt;-&lt;289.0,135.0&gt;-&lt;303.5,127.5&gt;&gt; = 10.249732710709438

* uni046B (U+046B): B&lt;&lt;396.5,258.5&gt;-&lt;362.0,201.0&gt;-&lt;292.0,98.0&gt;&gt;/B&lt;&lt;292.0,98.0&gt;-&lt;303.0,111.0&gt;-&lt;309.0,93.0&gt;&gt; = 6.035874179005283

* uni046B (U+046B): B&lt;&lt;723.5,686.0&gt;-&lt;767.0,718.0&gt;-&lt;819.0,723.0&gt;&gt;/L&lt;&lt;819.0,723.0&gt;--&lt;529.0,727.0&gt;&gt; = 6.282561059556548

* uni046B (U+046B): L&lt;&lt;118.0,161.0&gt;--&lt;116.0,154.0&gt;&gt;/B&lt;&lt;116.0,154.0&gt;-&lt;119.0,160.0&gt;-&lt;140.0,195.5&gt;&gt; = 10.619655276155106

* uni046C (U+046C): L&lt;&lt;505.0,558.0&gt;--&lt;556.0,555.0&gt;&gt;/L&lt;&lt;556.0,555.0&gt;--&lt;346.0,568.0&gt;&gt; = 0.17590052876524775

* uni046C (U+046C): L&lt;&lt;610.0,135.0&gt;--&lt;660.0,414.0&gt;&gt;/B&lt;&lt;660.0,414.0&gt;-&lt;639.0,367.0&gt;-&lt;614.5,310.5&gt;&gt; = 13.915292134184238

* uni046E (U+046E): B&lt;&lt;992.5,697.5&gt;-&lt;948.0,670.0&gt;-&lt;926.0,678.0&gt;&gt;/B&lt;&lt;926.0,678.0&gt;-&lt;1009.0,634.0&gt;-&lt;1045.0,568.0&gt;&gt; = 7.945872186780907

* uni046F (U+046F): B&lt;&lt;482.5,899.5&gt;-&lt;538.0,892.0&gt;-&lt;563.0,872.0&gt;&gt;/L&lt;&lt;563.0,872.0&gt;--&lt;314.0,1092.0&gt;&gt; = 2.801887220307923

* uni046F (U+046F): B&lt;&lt;974.5,545.0&gt;-&lt;928.0,505.0&gt;-&lt;898.0,516.0&gt;&gt;/B&lt;&lt;898.0,516.0&gt;-&lt;960.0,489.0&gt;-&lt;994.5,420.0&gt;&gt; = 3.3960451326528314

* uni0474 (U+0474): B&lt;&lt;539.0,502.5&gt;-&lt;543.0,401.0&gt;-&lt;543.0,315.0&gt;&gt;/B&lt;&lt;543.0,315.0&gt;-&lt;568.0,421.0&gt;-&lt;634.5,596.5&gt;&gt; = 13.27064387640367

* uni0476 (U+0476): B&lt;&lt;540.5,418.0&gt;-&lt;543.0,311.0&gt;-&lt;542.0,233.0&gt;&gt;/B&lt;&lt;542.0,233.0&gt;-&lt;552.0,296.0&gt;-&lt;577.0,384.5&gt;&gt; = 8.284801397126827

* uni0478 (U+0478): L&lt;&lt;684.0,852.0&gt;--&lt;675.0,802.0&gt;&gt;/L&lt;&lt;675.0,802.0&gt;--&lt;689.0,858.0&gt;&gt; = 3.8322697461948283

* uni048A (U+048A): L&lt;&lt;514.0,1116.0&gt;--&lt;383.0,373.0&gt;&gt;/B&lt;&lt;383.0,373.0&gt;-&lt;430.0,479.0&gt;-&lt;565.0,655.0&gt;&gt; = 13.913136242180387

* uni048A (U+048A): L&lt;&lt;777.0,135.0&gt;--&lt;918.0,932.0&gt;&gt;/B&lt;&lt;918.0,932.0&gt;-&lt;897.0,872.0&gt;-&lt;843.0,784.5&gt;&gt; = 9.257461876096444

* uni048C (U+048C): L&lt;&lt;663.0,1101.0&gt;--&lt;632.0,1097.0&gt;&gt;/L&lt;&lt;632.0,1097.0&gt;--&lt;671.0,1097.0&gt;&gt; = 7.352379359892325

* uni048D (U+048D): B&lt;&lt;280.5,915.5&gt;-&lt;285.0,914.0&gt;-&lt;282.0,915.0&gt;&gt;/L&lt;&lt;282.0,915.0&gt;--&lt;348.0,896.0&gt;&gt; = 2.374961515761179

* uni048F (U+048F): B&lt;&lt;441.0,-9.5&gt;-&lt;389.0,24.0&gt;-&lt;388.0,80.0&gt;&gt;/L&lt;&lt;388.0,80.0&gt;--&lt;316.0,-326.0&gt;&gt; = 11.079306505374262

* uni0496 (U+0496): L&lt;&lt;501.0,568.0&gt;--&lt;502.0,571.0&gt;&gt;/L&lt;&lt;502.0,571.0&gt;--&lt;255.0,124.0&gt;&gt; = 10.488892978620525

* uni0496 (U+0496): L&lt;&lt;593.0,681.0&gt;--&lt;642.0,1119.0&gt;&gt;/B&lt;&lt;642.0,1119.0&gt;-&lt;638.0,1106.0&gt;-&lt;620.0,1109.5&gt;&gt; = 10.719468491956071

* uni0496 (U+0496): L&lt;&lt;710.0,683.0&gt;--&lt;1021.0,1142.0&gt;&gt;/B&lt;&lt;1021.0,1142.0&gt;-&lt;1001.0,1112.0&gt;-&lt;985.0,1138.0&gt;&gt; = 0.42992524396017084

* uni0497 (U+0497): B&lt;&lt;474.0,333.0&gt;-&lt;464.0,357.0&gt;-&lt;476.0,381.0&gt;&gt;/L&lt;&lt;476.0,381.0&gt;--&lt;308.0,143.0&gt;&gt; = 8.652541791114704

* uni0497 (U+0497): B&lt;&lt;484.0,772.0&gt;-&lt;461.0,743.0&gt;-&lt;448.0,766.0&gt;&gt;/L&lt;&lt;448.0,766.0&gt;--&lt;564.0,523.0&gt;&gt; = 3.9576541805711405

* uni0497 (U+0497): L&lt;&lt;564.0,523.0&gt;--&lt;576.0,757.0&gt;&gt;/L&lt;&lt;576.0,757.0&gt;--&lt;569.0,722.0&gt;&gt; = 8.374259027599026

* uni0497 (U+0497): L&lt;&lt;675.0,261.0&gt;--&lt;650.0,131.0&gt;&gt;/L&lt;&lt;650.0,131.0&gt;--&lt;657.0,161.0&gt;&gt; = 2.2484952517373937

* uni0497 (U+0497): L&lt;&lt;734.0,599.0&gt;--&lt;895.0,776.0&gt;&gt;/B&lt;&lt;895.0,776.0&gt;-&lt;883.0,762.0&gt;-&lt;870.0,773.0&gt;&gt; = 1.688502254821007

* uni0499 (U+0499): B&lt;&lt;391.5,916.0&gt;-&lt;413.0,902.0&gt;-&lt;403.0,900.0&gt;&gt;/B&lt;&lt;403.0,900.0&gt;-&lt;429.0,911.0&gt;-&lt;480.5,922.0&gt;&gt; = 11.62216796356958

* uni049A (U+049A): L&lt;&lt;973.0,-220.0&gt;--&lt;1011.0,-5.0&gt;&gt;/B&lt;&lt;1011.0,-5.0&gt;-&lt;1006.0,-25.0&gt;-&lt;985.0,-20.5&gt;&gt; = 4.013061815020936

* uni049C (U+049C): L&lt;&lt;147.0,134.0&gt;--&lt;322.0,1129.0&gt;&gt;/L&lt;&lt;322.0,1129.0&gt;--&lt;315.0,1090.0&gt;&gt; = 0.20038412258308974

* uni049C (U+049C): L&lt;&lt;424.0,669.0&gt;--&lt;328.0,124.0&gt;&gt;/L&lt;&lt;328.0,124.0&gt;--&lt;335.0,161.0&gt;&gt; = 0.7231362426926076

* uni049C (U+049C): L&lt;&lt;677.0,895.0&gt;--&lt;905.0,1130.0&gt;&gt;/B&lt;&lt;905.0,1130.0&gt;-&lt;881.0,1113.0&gt;-&lt;865.5,1139.0&gt;&gt; = 10.55496345491868

* uni049C (U+049C): L&lt;&lt;749.0,728.0&gt;--&lt;976.0,140.0&gt;&gt;/L&lt;&lt;976.0,140.0&gt;--&lt;972.0,161.0&gt;&gt; = 10.325004164216951

* uni049C (U+049C): L&lt;&lt;778.0,118.0&gt;--&lt;575.0,653.0&gt;&gt;/L&lt;&lt;575.0,653.0&gt;--&lt;605.0,486.0&gt;&gt; = 10.59467807597784

* uni049D (U+049D): L&lt;&lt;825.0,530.0&gt;--&lt;999.0,143.0&gt;&gt;/L&lt;&lt;999.0,143.0&gt;--&lt;995.0,161.0&gt;&gt; = 11.680467016433756

* uni04A0 (U+04A0): L&lt;&lt;578.0,655.0&gt;--&lt;946.0,1138.0&gt;&gt;/B&lt;&lt;946.0,1138.0&gt;-&lt;930.0,1118.0&gt;-&lt;915.5,1124.5&gt;&gt; = 1.3558599761066843

* uni04A0 (U+04A0): L&lt;&lt;696.0,1090.0&gt;--&lt;700.0,1116.0&gt;&gt;/L&lt;&lt;700.0,1116.0&gt;--&lt;578.0,655.0&gt;&gt; = 6.076901551143823

* uni04A4 (U+04A4): L&lt;&lt;118.0,161.0&gt;--&lt;114.0,134.0&gt;&gt;/L&lt;&lt;114.0,134.0&gt;--&lt;283.0,1091.0&gt;&gt; = 1.5878414641809127

* uni04A4 (U+04A4): L&lt;&lt;495.0,1090.0&gt;--&lt;499.0,1116.0&gt;&gt;/L&lt;&lt;499.0,1116.0&gt;--&lt;423.0,730.0&gt;&gt; = 2.3923975036284992

* uni04A4 (U+04A4): L&lt;&lt;575.0,161.0&gt;--&lt;571.0,135.0&gt;&gt;/L&lt;&lt;571.0,135.0&gt;--&lt;655.0,573.0&gt;&gt; = 2.1102510855068175

* uni04A7 (U+04A7): L&lt;&lt;794.0,390.0&gt;--&lt;798.0,415.0&gt;&gt;/L&lt;&lt;798.0,415.0&gt;--&lt;746.0,128.0&gt;&gt; = 1.1794295465152018

* uni04A9 (U+04A9): B&lt;&lt;373.0,233.0&gt;-&lt;401.0,165.0&gt;-&lt;502.0,153.0&gt;&gt;/B&lt;&lt;502.0,153.0&gt;-&lt;479.0,157.0&gt;-&lt;478.5,202.5&gt;&gt; = 3.090150773685319

* uni04A9 (U+04A9): B&lt;&lt;673.0,196.5&gt;-&lt;669.0,163.0&gt;-&lt;653.0,156.0&gt;&gt;/B&lt;&lt;653.0,156.0&gt;-&lt;683.0,165.0&gt;-&lt;725.0,187.5&gt;&gt; = 6.9301334966631245

* uni04BB (U+04BB): L&lt;&lt;635.0,1238.0&gt;--&lt;560.0,812.0&gt;&gt;/B&lt;&lt;560.0,812.0&gt;-&lt;575.0,850.0&gt;-&lt;607.0,877.5&gt;&gt; = 11.55601571389509

* uni04BC (U+04BC): B&lt;&lt;372.0,812.5&gt;-&lt;373.0,796.0&gt;-&lt;372.0,780.0&gt;&gt;/B&lt;&lt;372.0,780.0&gt;-&lt;414.0,916.0&gt;-&lt;492.5,1035.5&gt;&gt; = 13.585584427867914

* uni04BD (U+04BD): B&lt;&lt;354.5,595.0&gt;-&lt;344.0,580.0&gt;-&lt;340.0,586.0&gt;&gt;/B&lt;&lt;340.0,586.0&gt;-&lt;347.0,577.0&gt;-&lt;350.5,568.5&gt;&gt; = 4.184916125118406

* uni04BE (U+04BE): B&lt;&lt;372.0,812.5&gt;-&lt;373.0,796.0&gt;-&lt;372.0,780.0&gt;&gt;/B&lt;&lt;372.0,780.0&gt;-&lt;414.0,916.0&gt;-&lt;492.5,1035.5&gt;&gt; = 13.585584427867914

* uni04BF (U+04BF): B&lt;&lt;354.5,595.0&gt;-&lt;344.0,580.0&gt;-&lt;340.0,586.0&gt;&gt;/B&lt;&lt;340.0,586.0&gt;-&lt;347.0,577.0&gt;-&lt;350.5,568.5&gt;&gt; = 4.184916125118406

* uni04C1 (U+04C1): L&lt;&lt;530.0,145.0&gt;--&lt;603.0,556.0&gt;&gt;/L&lt;&lt;603.0,556.0&gt;--&lt;587.0,520.0&gt;&gt; = 13.890900229507837

* uni04C1 (U+04C1): L&lt;&lt;629.0,705.0&gt;--&lt;690.0,1053.0&gt;&gt;/L&lt;&lt;690.0,1053.0&gt;--&lt;682.0,1017.0&gt;&gt; = 2.586587914347925

* uni04C1 (U+04C1): L&lt;&lt;819.0,544.0&gt;--&lt;747.0,133.0&gt;&gt;/L&lt;&lt;747.0,133.0&gt;--&lt;755.0,170.0&gt;&gt; = 2.264078783952361

* uni04C2 (U+04C2): B&lt;&lt;535.0,855.0&gt;-&lt;544.0,834.0&gt;-&lt;551.0,812.0&gt;&gt;/B&lt;&lt;551.0,812.0&gt;-&lt;546.0,836.0&gt;-&lt;550.0,862.0&gt;&gt; = 5.881835287909446

* uni04C2 (U+04C2): L&lt;&lt;608.0,587.0&gt;--&lt;644.0,788.0&gt;&gt;/L&lt;&lt;644.0,788.0&gt;--&lt;635.0,754.0&gt;&gt; = 4.672213390155418

* uni04C2 (U+04C2): L&lt;&lt;793.0,399.0&gt;--&lt;747.0,135.0&gt;&gt;/L&lt;&lt;747.0,135.0&gt;--&lt;756.0,170.0&gt;&gt; = 4.536649119988902

* uni04C2 (U+04C2): L&lt;&lt;978.0,842.0&gt;--&lt;977.0,840.0&gt;&gt;/B&lt;&lt;977.0,840.0&gt;-&lt;985.0,851.0&gt;-&lt;994.0,863.0&gt;&gt; = 9.462322208025574

* uni04C5 (U+04C5): L&lt;&lt;1138.0,1116.0&gt;--&lt;963.0,123.0&gt;&gt;/L&lt;&lt;963.0,123.0&gt;--&lt;978.0,161.0&gt;&gt; = 11.546163020120076

* uni04C5 (U+04C5): L&lt;&lt;281.0,151.0&gt;--&lt;279.0,147.0&gt;&gt;/B&lt;&lt;279.0,147.0&gt;-&lt;312.0,186.0&gt;-&lt;344.5,318.0&gt;&gt; = 13.671307132195786

* uni04C7 (U+04C7): L&lt;&lt;155.0,135.0&gt;--&lt;330.0,1128.0&gt;&gt;/L&lt;&lt;330.0,1128.0&gt;--&lt;313.0,1090.0&gt;&gt; = 14.107421602742775

* uni04C9 (U+04C9): L&lt;&lt;155.0,135.0&gt;--&lt;330.0,1128.0&gt;&gt;/L&lt;&lt;330.0,1128.0&gt;--&lt;313.0,1090.0&gt;&gt; = 14.107421602742775

* uni04CD (U+04CD): L&lt;&lt;1163.0,1117.0&gt;--&lt;988.0,123.0&gt;&gt;/L&lt;&lt;988.0,123.0&gt;--&lt;997.0,161.0&gt;&gt; = 3.3395710572474435

* uni04CD (U+04CD): L&lt;&lt;1165.0,1090.0&gt;--&lt;1163.0,1117.0&gt;&gt;/L&lt;&lt;1163.0,1117.0&gt;--&lt;988.0,123.0&gt;&gt; = 14.221355003702163

* uni04CD (U+04CD): L&lt;&lt;131.0,161.0&gt;--&lt;132.0,134.0&gt;&gt;/L&lt;&lt;132.0,134.0&gt;--&lt;301.0,1090.0&gt;&gt; = 12.146170230507211

* uni04CD (U+04CD): L&lt;&lt;658.0,618.0&gt;--&lt;658.0,617.0&gt;&gt;/B&lt;&lt;658.0,617.0&gt;-&lt;665.0,657.0&gt;-&lt;692.5,726.5&gt;&gt; = 9.926245506651705

* uni04CD (U+04CD): L&lt;&lt;802.0,161.0&gt;--&lt;804.0,134.0&gt;&gt;/L&lt;&lt;804.0,134.0&gt;--&lt;933.0,867.0&gt;&gt; = 14.217617544764853

* uni04CE (U+04CE): L&lt;&lt;783.0,137.0&gt;--&lt;872.0,641.0&gt;&gt;/B&lt;&lt;872.0,641.0&gt;-&lt;848.0,580.0&gt;-&lt;813.0,513.5&gt;&gt; = 11.462326087066934

* uni04D4 (U+04D4): L&lt;&lt;136.0,140.0&gt;--&lt;512.0,1135.0&gt;&gt;/B&lt;&lt;512.0,1135.0&gt;-&lt;503.0,1113.0&gt;-&lt;484.5,1114.5&gt;&gt; = 1.547974023532823

* uni04D4 (U+04D4): L&lt;&lt;141.0,161.0&gt;--&lt;136.0,140.0&gt;&gt;/L&lt;&lt;136.0,140.0&gt;--&lt;512.0,1135.0&gt;&gt; = 7.308551879928194

* uni04D5 (U+04D5): B&lt;&lt;504.5,330.5&gt;-&lt;513.0,357.0&gt;-&lt;530.0,358.0&gt;&gt;/B&lt;&lt;530.0,358.0&gt;-&lt;512.0,355.0&gt;-&lt;469.0,350.0&gt;&gt; = 6.095861544595815

* uni04D5 (U+04D5): B&lt;&lt;613.5,39.5&gt;-&lt;585.0,72.0&gt;-&lt;578.0,97.0&gt;&gt;/B&lt;&lt;578.0,97.0&gt;-&lt;579.0,82.0&gt;-&lt;545.0,48.5&gt;&gt; = 11.828171622918383

* uni04D5 (U+04D5): B&lt;&lt;672.0,839.0&gt;-&lt;692.0,805.0&gt;-&lt;686.0,789.0&gt;&gt;/B&lt;&lt;686.0,789.0&gt;-&lt;699.0,813.0&gt;-&lt;734.5,846.5&gt;&gt; = 7.88688340477983

* uni04DA (U+04DA): B&lt;&lt;419.5,1265.5&gt;-&lt;435.0,1229.0&gt;-&lt;421.0,1212.0&gt;&gt;/B&lt;&lt;421.0,1212.0&gt;-&lt;471.0,1249.0&gt;-&lt;547.0,1278.5&gt;&gt; = 14.02609903114982

* uni04DC (U+04DC): L&lt;&lt;530.0,145.0&gt;--&lt;603.0,556.0&gt;&gt;/L&lt;&lt;603.0,556.0&gt;--&lt;587.0,520.0&gt;&gt; = 13.890900229507837

* uni04DC (U+04DC): L&lt;&lt;629.0,705.0&gt;--&lt;690.0,1053.0&gt;&gt;/L&lt;&lt;690.0,1053.0&gt;--&lt;682.0,1017.0&gt;&gt; = 2.586587914347925

* uni04DC (U+04DC): L&lt;&lt;819.0,544.0&gt;--&lt;747.0,133.0&gt;&gt;/L&lt;&lt;747.0,133.0&gt;--&lt;755.0,170.0&gt;&gt; = 2.264078783952361

* uni04DD (U+04DD): B&lt;&lt;535.0,855.0&gt;-&lt;544.0,834.0&gt;-&lt;551.0,812.0&gt;&gt;/B&lt;&lt;551.0,812.0&gt;-&lt;546.0,836.0&gt;-&lt;550.0,862.0&gt;&gt; = 5.881835287909446

* uni04DD (U+04DD): L&lt;&lt;608.0,587.0&gt;--&lt;644.0,788.0&gt;&gt;/L&lt;&lt;644.0,788.0&gt;--&lt;635.0,754.0&gt;&gt; = 4.672213390155418

* uni04DD (U+04DD): L&lt;&lt;793.0,399.0&gt;--&lt;747.0,135.0&gt;&gt;/L&lt;&lt;747.0,135.0&gt;--&lt;756.0,170.0&gt;&gt; = 4.536649119988902

* uni04DD (U+04DD): L&lt;&lt;978.0,842.0&gt;--&lt;977.0,840.0&gt;&gt;/B&lt;&lt;977.0,840.0&gt;-&lt;985.0,851.0&gt;-&lt;994.0,863.0&gt;&gt; = 9.462322208025574

* uni04E9 (U+04E9): B&lt;&lt;434.5,584.0&gt;-&lt;422.0,568.0&gt;-&lt;402.0,564.0&gt;&gt;/L&lt;&lt;402.0,564.0&gt;--&lt;1035.0,564.0&gt;&gt; = 11.309932474020195

* uni04E9 (U+04E9): B&lt;&lt;954.5,340.0&gt;-&lt;967.0,356.0&gt;-&lt;987.0,360.0&gt;&gt;/L&lt;&lt;987.0,360.0&gt;--&lt;355.0,360.0&gt;&gt; = 11.309932474020195

* uni04E9 (U+04E9): L&lt;&lt;402.0,564.0&gt;--&lt;1035.0,564.0&gt;&gt;/B&lt;&lt;1035.0,564.0&gt;-&lt;1011.0,566.0&gt;-&lt;1003.0,585.0&gt;&gt; = 4.763641690726143

* uni04E9 (U+04E9): L&lt;&lt;987.0,360.0&gt;--&lt;355.0,360.0&gt;&gt;/B&lt;&lt;355.0,360.0&gt;-&lt;378.0,358.0&gt;-&lt;386.0,339.0&gt;&gt; = 4.969740728110289

* uni04EB (U+04EB): B&lt;&lt;434.5,584.0&gt;-&lt;422.0,568.0&gt;-&lt;402.0,564.0&gt;&gt;/L&lt;&lt;402.0,564.0&gt;--&lt;1035.0,564.0&gt;&gt; = 11.309932474020195

* uni04EB (U+04EB): B&lt;&lt;954.5,340.0&gt;-&lt;967.0,356.0&gt;-&lt;987.0,360.0&gt;&gt;/L&lt;&lt;987.0,360.0&gt;--&lt;355.0,360.0&gt;&gt; = 11.309932474020195

* uni04EB (U+04EB): L&lt;&lt;402.0,564.0&gt;--&lt;1035.0,564.0&gt;&gt;/B&lt;&lt;1035.0,564.0&gt;-&lt;1011.0,566.0&gt;-&lt;1003.0,585.0&gt;&gt; = 4.763641690726143

* uni04EB (U+04EB): L&lt;&lt;987.0,360.0&gt;--&lt;355.0,360.0&gt;&gt;/B&lt;&lt;355.0,360.0&gt;-&lt;378.0,358.0&gt;-&lt;386.0,339.0&gt;&gt; = 4.969740728110289

* uni04F5 (U+04F5): L&lt;&lt;851.0,154.0&gt;--&lt;879.0,318.0&gt;&gt;/B&lt;&lt;879.0,318.0&gt;-&lt;868.0,290.0&gt;-&lt;837.5,274.0&gt;&gt; = 11.758949766738523

* uni04F9 (U+04F9): L&lt;&lt;133.0,144.0&gt;--&lt;247.0,792.0&gt;&gt;/L&lt;&lt;247.0,792.0&gt;--&lt;239.0,754.0&gt;&gt; = 1.9109454194774027

* uni04F9 (U+04F9): L&lt;&lt;927.0,144.0&gt;--&lt;1041.0,792.0&gt;&gt;/L&lt;&lt;1041.0,792.0&gt;--&lt;1033.0,754.0&gt;&gt; = 1.9109454194774027

* uni0512 (U+0512): L&lt;&lt;281.0,151.0&gt;--&lt;279.0,147.0&gt;&gt;/B&lt;&lt;279.0,147.0&gt;-&lt;312.0,186.0&gt;-&lt;344.5,318.0&gt;&gt; = 13.671307132195786

* uni0600 (U+0600): L&lt;&lt;121.0,442.0&gt;--&lt;619.0,442.0&gt;&gt;/B&lt;&lt;619.0,442.0&gt;-&lt;595.0,443.0&gt;-&lt;592.0,472.0&gt;&gt; = 2.3859440303887243

* uni0603 (U+0603): B&lt;&lt;579.5,196.5&gt;-&lt;517.0,227.0&gt;-&lt;494.0,279.0&gt;&gt;/B&lt;&lt;494.0,279.0&gt;-&lt;499.0,257.0&gt;-&lt;474.0,234.0&gt;&gt; = 11.055909126055553

* uni0604 (U+0604): B&lt;&lt;924.0,486.5&gt;-&lt;892.0,510.0&gt;-&lt;897.0,531.0&gt;&gt;/B&lt;&lt;897.0,531.0&gt;-&lt;888.0,507.0&gt;-&lt;851.5,485.0&gt;&gt; = 7.16354746583234

* uni0604 (U+0604): L&lt;&lt;109.0,407.0&gt;--&lt;287.0,406.0&gt;&gt;/B&lt;&lt;287.0,406.0&gt;-&lt;258.0,406.0&gt;-&lt;254.0,439.0&gt;&gt; = 0.32188301539887176

* uni0608 (U+0608): B&lt;&lt;1077.5,781.0&gt;-&lt;1080.0,792.0&gt;-&lt;1083.0,807.0&gt;&gt;/L&lt;&lt;1083.0,807.0&gt;--&lt;1073.0,761.0&gt;&gt; = 0.9548412538719732

* uni0608 (U+0608): L&lt;&lt;1083.0,807.0&gt;--&lt;1073.0,761.0&gt;&gt;/B&lt;&lt;1073.0,761.0&gt;-&lt;1075.0,770.0&gt;-&lt;1077.5,781.0&gt;&gt; = 0.26403398125927363

* uni0608 (U+0608): L&lt;&lt;1089.0,837.0&gt;--&lt;1088.0,833.0&gt;&gt;/B&lt;&lt;1088.0,833.0&gt;-&lt;1092.0,853.0&gt;-&lt;1097.0,878.5&gt;&gt; = 2.726310993906212

* uni0608 (U+0608): L&lt;&lt;859.0,679.0&gt;--&lt;859.0,677.0&gt;&gt;/L&lt;&lt;859.0,677.0&gt;--&lt;887.0,837.0&gt;&gt; = 9.926245506651705

* uni060A (U+060A): B&lt;&lt;503.0,225.0&gt;-&lt;530.0,201.0&gt;-&lt;553.0,169.0&gt;&gt;/B&lt;&lt;553.0,169.0&gt;-&lt;538.0,195.0&gt;-&lt;530.5,221.5&gt;&gt; = 5.725052031753534

* uni060A (U+060A): B&lt;&lt;622.0,81.0&gt;-&lt;595.0,104.0&gt;-&lt;573.0,136.0&gt;&gt;/B&lt;&lt;573.0,136.0&gt;-&lt;604.0,78.0&gt;-&lt;601.0,41.0&gt;&gt; = 6.384787604379598

* uni060F (U+060F): B&lt;&lt;259.0,3.0&gt;-&lt;267.0,24.0&gt;-&lt;284.0,20.0&gt;&gt;/B&lt;&lt;284.0,20.0&gt;-&lt;177.0,75.0&gt;-&lt;134.5,195.0&gt;&gt; = 13.963491160882395

* uni060F (U+060F): B&lt;&lt;470.0,-32.0&gt;-&lt;451.0,-28.0&gt;-&lt;455.0,-12.0&gt;&gt;/B&lt;&lt;455.0,-12.0&gt;-&lt;449.0,-41.0&gt;-&lt;457.5,-65.5&gt;&gt; = 2.3468742924873256

* uni0610 (U+0610): B&lt;&lt;644.0,1558.0&gt;-&lt;668.0,1513.0&gt;-&lt;641.0,1448.0&gt;&gt;/B&lt;&lt;641.0,1448.0&gt;-&lt;669.0,1493.0&gt;-&lt;723.5,1537.5&gt;&gt; = 9.333545167140048

* uni0610 (U+0610): B&lt;&lt;673.0,1132.0&gt;-&lt;630.0,1147.0&gt;-&lt;628.0,1183.0&gt;&gt;/B&lt;&lt;628.0,1183.0&gt;-&lt;606.0,1056.0&gt;-&lt;573.0,999.5&gt;&gt; = 13.007554131027335

* uni0611 (U+0611): L&lt;&lt;643.0,1252.0&gt;--&lt;718.0,1259.0&gt;&gt;/B&lt;&lt;718.0,1259.0&gt;-&lt;700.0,1260.0&gt;-&lt;699.0,1284.5&gt;&gt; = 8.511989001523766

* uni0612 (U+0612): L&lt;&lt;572.0,1479.0&gt;--&lt;440.0,1436.0&gt;&gt;/B&lt;&lt;440.0,1436.0&gt;-&lt;452.0,1438.0&gt;-&lt;453.5,1434.5&gt;&gt; = 8.581089797305685

* uni0613 (U+0613): B&lt;&lt;451.0,1558.0&gt;-&lt;475.0,1513.0&gt;-&lt;448.0,1448.0&gt;&gt;/B&lt;&lt;448.0,1448.0&gt;-&lt;476.0,1493.0&gt;-&lt;530.5,1537.5&gt;&gt; = 9.333545167140048

* uni0613 (U+0613): B&lt;&lt;476.0,1134.0&gt;-&lt;437.0,1149.0&gt;-&lt;435.0,1183.0&gt;&gt;/B&lt;&lt;435.0,1183.0&gt;-&lt;413.0,1056.0&gt;-&lt;380.0,999.5&gt;&gt; = 13.194184674592922

* uni0615 (U+0615): L&lt;&lt;823.0,1614.0&gt;--&lt;760.0,1264.0&gt;&gt;/B&lt;&lt;760.0,1264.0&gt;-&lt;783.0,1365.0&gt;-&lt;846.0,1418.0&gt;&gt; = 2.624809149723495

* uni061C (U+061C): B&lt;&lt;775.5,851.5&gt;-&lt;751.0,907.0&gt;-&lt;765.0,992.0&gt;&gt;/B&lt;&lt;765.0,992.0&gt;-&lt;756.0,959.0&gt;-&lt;750.0,924.0&gt;&gt; = 5.9021394529644216

* uni061C (U+061C): B&lt;&lt;776.0,1290.0&gt;-&lt;811.0,1327.0&gt;-&lt;852.0,1359.0&gt;&gt;/L&lt;&lt;852.0,1359.0&gt;--&lt;767.0,1314.0&gt;&gt; = 10.074332730102727

* uni061C (U+061C): B&lt;&lt;911.5,1229.5&gt;-&lt;861.0,1189.0&gt;-&lt;819.0,1119.0&gt;&gt;/B&lt;&lt;819.0,1119.0&gt;-&lt;860.0,1174.0&gt;-&lt;915.0,1203.5&gt;&gt; = 5.739098498089571

* uni061E (U+061E): B&lt;&lt;569.0,640.0&gt;-&lt;611.0,593.0&gt;-&lt;628.0,548.0&gt;&gt;/B&lt;&lt;628.0,548.0&gt;-&lt;627.0,555.0&gt;-&lt;627.0,561.0&gt;&gt; = 12.565348379907297

* uni061E (U+061E): B&lt;&lt;694.0,428.0&gt;-&lt;652.0,473.0&gt;-&lt;635.0,518.0&gt;&gt;/B&lt;&lt;635.0,518.0&gt;-&lt;636.0,512.0&gt;-&lt;636.0,506.0&gt;&gt; = 11.233128526037627

* uni0621 (U+FE80): B&lt;&lt;397.0,349.0&gt;-&lt;459.0,394.0&gt;-&lt;523.0,441.0&gt;&gt;/B&lt;&lt;523.0,441.0&gt;-&lt;498.0,424.0&gt;-&lt;460.5,449.5&gt;&gt; = 2.076927596042315

* uni0622.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0623 (U+FE83): B&lt;&lt;653.5,1380.0&gt;-&lt;709.0,1407.0&gt;-&lt;766.0,1424.0&gt;&gt;/B&lt;&lt;766.0,1424.0&gt;-&lt;716.0,1416.0&gt;-&lt;684.0,1470.5&gt;&gt; = 7.5167036577946975

* uni0623.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0623.fina.alt: B&lt;&lt;891.5,1380.0&gt;-&lt;947.0,1407.0&gt;-&lt;1004.0,1424.0&gt;&gt;/B&lt;&lt;1004.0,1424.0&gt;-&lt;954.0,1416.0&gt;-&lt;922.0,1470.5&gt;&gt; = 7.5167036577946975

* uni0624 (U+FE85): B&lt;&lt;460.0,1071.0&gt;-&lt;515.0,1098.0&gt;-&lt;572.0,1115.0&gt;&gt;/B&lt;&lt;572.0,1115.0&gt;-&lt;523.0,1107.0&gt;-&lt;490.5,1161.5&gt;&gt; = 7.334378801416706

* uni0625 (U+FE87): B&lt;&lt;360.0,-297.0&gt;-&lt;415.0,-270.0&gt;-&lt;472.0,-253.0&gt;&gt;/B&lt;&lt;472.0,-253.0&gt;-&lt;423.0,-261.0&gt;-&lt;390.5,-206.5&gt;&gt; = 7.334378801416706

* uni0625.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0625.fina.alt: B&lt;&lt;599.5,-289.0&gt;-&lt;655.0,-262.0&gt;-&lt;711.0,-245.0&gt;&gt;/B&lt;&lt;711.0,-245.0&gt;-&lt;662.0,-253.0&gt;-&lt;630.0,-198.5&gt;&gt; = 7.614189346743762

* uni0626 (U+FE89): B&lt;&lt;555.5,1312.0&gt;-&lt;611.0,1339.0&gt;-&lt;668.0,1356.0&gt;&gt;/B&lt;&lt;668.0,1356.0&gt;-&lt;618.0,1348.0&gt;-&lt;586.0,1402.5&gt;&gt; = 7.5167036577946975

* uni0627.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0628 (U+FE8F): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0629 (U+FE93): B&lt;&lt;691.0,1645.0&gt;-&lt;733.0,1598.0&gt;-&lt;750.0,1553.0&gt;&gt;/B&lt;&lt;750.0,1553.0&gt;-&lt;749.0,1560.0&gt;-&lt;750.0,1566.0&gt;&gt; = 12.565348379907297

* uni062A (U+FE95): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni062A (U+FE95): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni062B (U+FE99): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni062B (U+FE99): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0637 (U+FEC1): L&lt;&lt;714.0,1503.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.163478407146162

* uni0638 (U+FEC5): L&lt;&lt;714.0,1503.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.163478407146162

* uni063B (U+063B): B&lt;&lt;506.5,1657.0&gt;-&lt;548.0,1610.0&gt;-&lt;565.0,1565.0&gt;&gt;/B&lt;&lt;565.0,1565.0&gt;-&lt;564.0,1572.0&gt;-&lt;565.0,1578.0&gt;&gt; = 12.565348379907297

* uni063B.fina: B&lt;&lt;528.5,1782.0&gt;-&lt;570.0,1735.0&gt;-&lt;587.0,1690.0&gt;&gt;/B&lt;&lt;587.0,1690.0&gt;-&lt;586.0,1697.0&gt;-&lt;587.0,1703.0&gt;&gt; = 12.565348379907297

* uni063B.init: B&lt;&lt;506.5,1657.0&gt;-&lt;548.0,1610.0&gt;-&lt;565.0,1565.0&gt;&gt;/B&lt;&lt;565.0,1565.0&gt;-&lt;564.0,1572.0&gt;-&lt;565.0,1578.0&gt;&gt; = 12.565348379907297

* uni063B.medi: B&lt;&lt;557.5,1782.0&gt;-&lt;599.0,1735.0&gt;-&lt;616.0,1690.0&gt;&gt;/B&lt;&lt;616.0,1690.0&gt;-&lt;615.0,1697.0&gt;-&lt;616.0,1703.0&gt;&gt; = 12.565348379907297

* uni063C (U+063C): B&lt;&lt;577.5,-272.0&gt;-&lt;535.0,-226.0&gt;-&lt;519.0,-180.0&gt;&gt;/B&lt;&lt;519.0,-180.0&gt;-&lt;520.0,-189.0&gt;-&lt;520.0,-197.0&gt;&gt; = 12.83881627990079

* uni063C.fina: B&lt;&lt;577.5,-272.0&gt;-&lt;535.0,-226.0&gt;-&lt;519.0,-180.0&gt;&gt;/B&lt;&lt;519.0,-180.0&gt;-&lt;520.0,-189.0&gt;-&lt;520.0,-197.0&gt;&gt; = 12.83881627990079

* uni063C.init: B&lt;&lt;577.5,-272.0&gt;-&lt;535.0,-226.0&gt;-&lt;519.0,-180.0&gt;&gt;/B&lt;&lt;519.0,-180.0&gt;-&lt;520.0,-189.0&gt;-&lt;520.0,-197.0&gt;&gt; = 12.83881627990079

* uni063C.medi: B&lt;&lt;606.5,-272.0&gt;-&lt;564.0,-226.0&gt;-&lt;548.0,-180.0&gt;&gt;/B&lt;&lt;548.0,-180.0&gt;-&lt;549.0,-189.0&gt;-&lt;549.0,-197.0&gt;&gt; = 12.83881627990079

* uni063E (U+063E): B&lt;&lt;641.0,1514.0&gt;-&lt;683.0,1467.0&gt;-&lt;700.0,1422.0&gt;&gt;/B&lt;&lt;700.0,1422.0&gt;-&lt;699.0,1429.0&gt;-&lt;699.0,1435.0&gt;&gt; = 12.565348379907297

* uni063E (U+063E): B&lt;&lt;766.5,1302.0&gt;-&lt;725.0,1347.0&gt;-&lt;707.0,1392.0&gt;&gt;/B&lt;&lt;707.0,1392.0&gt;-&lt;708.0,1386.0&gt;-&lt;708.0,1380.0&gt;&gt; = 12.33908727832621

* uni063E.fina: B&lt;&lt;543.0,957.0&gt;-&lt;585.0,910.0&gt;-&lt;602.0,865.0&gt;&gt;/B&lt;&lt;602.0,865.0&gt;-&lt;601.0,872.0&gt;-&lt;601.0,878.0&gt;&gt; = 12.565348379907297

* uni063E.fina: B&lt;&lt;668.0,745.0&gt;-&lt;626.0,790.0&gt;-&lt;609.0,835.0&gt;&gt;/B&lt;&lt;609.0,835.0&gt;-&lt;610.0,829.0&gt;-&lt;610.0,823.0&gt;&gt; = 11.233128526037627

* uni063E.init: B&lt;&lt;912.5,1379.0&gt;-&lt;954.0,1332.0&gt;-&lt;971.0,1287.0&gt;&gt;/B&lt;&lt;971.0,1287.0&gt;-&lt;970.0,1294.0&gt;-&lt;971.0,1300.0&gt;&gt; = 12.565348379907297

* uni063E.medi: B&lt;&lt;904.5,1379.0&gt;-&lt;946.0,1332.0&gt;-&lt;963.0,1287.0&gt;&gt;/B&lt;&lt;963.0,1287.0&gt;-&lt;962.0,1294.0&gt;-&lt;963.0,1300.0&gt;&gt; = 12.565348379907297

* uni063F (U+063F): B&lt;&lt;638.5,1510.0&gt;-&lt;680.0,1463.0&gt;-&lt;697.0,1418.0&gt;&gt;/B&lt;&lt;697.0,1418.0&gt;-&lt;696.0,1425.0&gt;-&lt;697.0,1431.0&gt;&gt; = 12.565348379907297

* uni063F (U+063F): B&lt;&lt;764.0,1298.0&gt;-&lt;722.0,1343.0&gt;-&lt;705.0,1388.0&gt;&gt;/B&lt;&lt;705.0,1388.0&gt;-&lt;706.0,1382.0&gt;-&lt;705.0,1376.0&gt;&gt; = 11.233128526037627

* uni063F.fina: B&lt;&lt;543.0,957.0&gt;-&lt;585.0,910.0&gt;-&lt;602.0,865.0&gt;&gt;/B&lt;&lt;602.0,865.0&gt;-&lt;601.0,872.0&gt;-&lt;601.0,878.0&gt;&gt; = 12.565348379907297

* uni063F.fina: B&lt;&lt;668.0,745.0&gt;-&lt;626.0,790.0&gt;-&lt;609.0,835.0&gt;&gt;/B&lt;&lt;609.0,835.0&gt;-&lt;610.0,829.0&gt;-&lt;610.0,823.0&gt;&gt; = 11.233128526037627

* uni063F.init: B&lt;&lt;912.5,1379.0&gt;-&lt;954.0,1332.0&gt;-&lt;971.0,1287.0&gt;&gt;/B&lt;&lt;971.0,1287.0&gt;-&lt;970.0,1294.0&gt;-&lt;971.0,1300.0&gt;&gt; = 12.565348379907297

* uni063F.medi: B&lt;&lt;904.5,1379.0&gt;-&lt;946.0,1332.0&gt;-&lt;963.0,1287.0&gt;&gt;/B&lt;&lt;963.0,1287.0&gt;-&lt;962.0,1294.0&gt;-&lt;963.0,1300.0&gt;&gt; = 12.565348379907297

* uni0641 (U+FED1): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni0642 (U+FED5): B&lt;&lt;1076.0,1386.0&gt;-&lt;1034.0,1431.0&gt;-&lt;1017.0,1476.0&gt;&gt;/B&lt;&lt;1017.0,1476.0&gt;-&lt;1018.0,1470.0&gt;-&lt;1018.0,1464.0&gt;&gt; = 11.233128526037627

* uni0642 (U+FED5): B&lt;&lt;951.0,1598.0&gt;-&lt;993.0,1551.0&gt;-&lt;1010.0,1506.0&gt;&gt;/B&lt;&lt;1010.0,1506.0&gt;-&lt;1009.0,1513.0&gt;-&lt;1009.0,1519.0&gt;&gt; = 12.565348379907297

* uni064A (U+FEF1): B&lt;&lt;473.0,-629.0&gt;-&lt;431.0,-584.0&gt;-&lt;414.0,-539.0&gt;&gt;/B&lt;&lt;414.0,-539.0&gt;-&lt;415.0,-545.0&gt;-&lt;414.0,-551.0&gt;&gt; = 11.233128526037627

* uni0654 (U+0654): B&lt;&lt;568.5,1386.0&gt;-&lt;624.0,1413.0&gt;-&lt;681.0,1430.0&gt;&gt;/B&lt;&lt;681.0,1430.0&gt;-&lt;631.0,1422.0&gt;-&lt;599.0,1476.5&gt;&gt; = 7.5167036577946975

* uni0655 (U+0655): B&lt;&lt;158.5,-873.0&gt;-&lt;214.0,-846.0&gt;-&lt;270.0,-829.0&gt;&gt;/B&lt;&lt;270.0,-829.0&gt;-&lt;221.0,-837.0&gt;-&lt;189.0,-782.5&gt;&gt; = 7.614189346743762

* uni065E (U+065E): B&lt;&lt;779.5,1229.0&gt;-&lt;794.0,1250.0&gt;-&lt;815.0,1271.0&gt;&gt;/L&lt;&lt;815.0,1271.0&gt;--&lt;644.0,1139.0&gt;&gt; = 7.334378801416657

* uni065E (U+065E): L&lt;&lt;1111.0,1499.0&gt;--&lt;922.0,1354.0&gt;&gt;/B&lt;&lt;922.0,1354.0&gt;-&lt;942.0,1364.0&gt;-&lt;956.0,1365.0&gt;&gt; = 10.930216372309987

* uni0663 (U+06F3): B&lt;&lt;805.5,1013.0&gt;-&lt;799.0,1050.0&gt;-&lt;800.0,1066.0&gt;&gt;/B&lt;&lt;800.0,1066.0&gt;-&lt;797.0,1051.0&gt;-&lt;782.5,1012.0&gt;&gt; = 7.733598099022774

* uni0666 (U+0666): B&lt;&lt;772.5,872.5&gt;-&lt;788.0,925.0&gt;-&lt;811.0,949.0&gt;&gt;/B&lt;&lt;811.0,949.0&gt;-&lt;787.0,927.0&gt;-&lt;765.0,921.5&gt;&gt; = 3.708428157130501

* uni066D (U+066D): B&lt;&lt;350.5,232.0&gt;-&lt;407.0,293.0&gt;-&lt;453.0,347.0&gt;&gt;/B&lt;&lt;453.0,347.0&gt;-&lt;433.0,327.0&gt;-&lt;401.0,337.5&gt;&gt; = 4.573921259900818

* uni066E (U+066E): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni066E.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni066F.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni0671 (U+FB50): B&lt;&lt;829.0,1620.5&gt;-&lt;836.0,1597.0&gt;-&lt;832.0,1587.0&gt;&gt;/B&lt;&lt;832.0,1587.0&gt;-&lt;887.0,1697.0&gt;-&lt;987.5,1773.0&gt;&gt; = 4.763641690726066

* uni0671.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0671.fina.alt: B&lt;&lt;1067.0,1620.5&gt;-&lt;1074.0,1597.0&gt;-&lt;1070.0,1587.0&gt;&gt;/B&lt;&lt;1070.0,1587.0&gt;-&lt;1125.0,1697.0&gt;-&lt;1225.5,1773.0&gt;&gt; = 4.763641690726066

* uni0672.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0673.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0674 (U+0674): B&lt;&lt;487.0,861.0&gt;-&lt;549.0,906.0&gt;-&lt;614.0,953.0&gt;&gt;/B&lt;&lt;614.0,953.0&gt;-&lt;589.0,936.0&gt;-&lt;551.0,961.5&gt;&gt; = 1.6541213852836039

* uni0675 (U+0675): B&lt;&lt;727.0,861.0&gt;-&lt;789.0,906.0&gt;-&lt;854.0,953.0&gt;&gt;/B&lt;&lt;854.0,953.0&gt;-&lt;829.0,936.0&gt;-&lt;791.0,961.5&gt;&gt; = 1.6541213852836039

* uni0679 (U+FB66): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0679 (U+FB66): L&lt;&lt;867.0,1710.0&gt;--&lt;804.0,1360.0&gt;&gt;/B&lt;&lt;804.0,1360.0&gt;-&lt;827.0,1461.0&gt;-&lt;890.0,1514.0&gt;&gt; = 2.624809149723495

* uni067A (U+FB5E): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067B (U+FB52): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067C (U+067C): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067C (U+067C): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni067C.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067C.fina: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni067C.init: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni067C.medi: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni067D (U+067D): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067D (U+067D): B&lt;&lt;950.5,1446.0&gt;-&lt;908.0,1492.0&gt;-&lt;892.0,1538.0&gt;&gt;/B&lt;&lt;892.0,1538.0&gt;-&lt;893.0,1529.0&gt;-&lt;893.0,1521.0&gt;&gt; = 12.83881627990079

* uni067D.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067D.fina: B&lt;&lt;950.5,1446.0&gt;-&lt;908.0,1492.0&gt;-&lt;892.0,1538.0&gt;&gt;/B&lt;&lt;892.0,1538.0&gt;-&lt;893.0,1529.0&gt;-&lt;893.0,1521.0&gt;&gt; = 12.83881627990079

* uni067D.init: B&lt;&lt;950.5,1446.0&gt;-&lt;908.0,1492.0&gt;-&lt;892.0,1538.0&gt;&gt;/B&lt;&lt;892.0,1538.0&gt;-&lt;893.0,1529.0&gt;-&lt;893.0,1521.0&gt;&gt; = 12.83881627990079

* uni067D.medi: B&lt;&lt;907.5,1446.0&gt;-&lt;865.0,1492.0&gt;-&lt;849.0,1538.0&gt;&gt;/B&lt;&lt;849.0,1538.0&gt;-&lt;850.0,1529.0&gt;-&lt;850.0,1521.0&gt;&gt; = 12.83881627990079

* uni067E (U+FB56): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067E (U+FB56): B&lt;&lt;626.5,-272.0&gt;-&lt;584.0,-226.0&gt;-&lt;568.0,-180.0&gt;&gt;/B&lt;&lt;568.0,-180.0&gt;-&lt;569.0,-189.0&gt;-&lt;569.0,-197.0&gt;&gt; = 12.83881627990079

* uni067F (U+FB62): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni067F (U+FB62): B&lt;&lt;738.0,1365.5&gt;-&lt;771.0,1325.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.094757077012089

* uni067F (U+FB62): B&lt;&lt;787.5,1725.0&gt;-&lt;829.0,1678.0&gt;-&lt;846.0,1633.0&gt;&gt;/B&lt;&lt;846.0,1633.0&gt;-&lt;845.0,1640.0&gt;-&lt;846.0,1646.0&gt;&gt; = 12.565348379907297

* uni0680 (U+FB5A): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0680 (U+FB5A): B&lt;&lt;423.0,-420.5&gt;-&lt;456.0,-461.0&gt;-&lt;470.0,-499.0&gt;&gt;/B&lt;&lt;470.0,-499.0&gt;-&lt;469.0,-492.0&gt;-&lt;470.0,-486.0&gt;&gt; = 12.094757077012089

* uni0680 (U+FB5A): B&lt;&lt;472.5,-61.0&gt;-&lt;514.0,-108.0&gt;-&lt;531.0,-153.0&gt;&gt;/B&lt;&lt;531.0,-153.0&gt;-&lt;530.0,-146.0&gt;-&lt;531.0,-140.0&gt;&gt; = 12.565348379907297

* uni0681 (U+0681): B&lt;&lt;526.0,1144.0&gt;-&lt;581.0,1171.0&gt;-&lt;638.0,1188.0&gt;&gt;/B&lt;&lt;638.0,1188.0&gt;-&lt;589.0,1180.0&gt;-&lt;556.5,1234.5&gt;&gt; = 7.334378801416706

* uni0681.fina: B&lt;&lt;526.0,1144.0&gt;-&lt;581.0,1171.0&gt;-&lt;638.0,1188.0&gt;&gt;/B&lt;&lt;638.0,1188.0&gt;-&lt;589.0,1180.0&gt;-&lt;556.5,1234.5&gt;&gt; = 7.334378801416706

* uni0681.init: B&lt;&lt;556.5,1316.0&gt;-&lt;612.0,1343.0&gt;-&lt;668.0,1360.0&gt;&gt;/B&lt;&lt;668.0,1360.0&gt;-&lt;619.0,1352.0&gt;-&lt;587.0,1406.5&gt;&gt; = 7.614189346743762

* uni0681.medi: B&lt;&lt;556.5,1316.0&gt;-&lt;612.0,1343.0&gt;-&lt;668.0,1360.0&gt;&gt;/B&lt;&lt;668.0,1360.0&gt;-&lt;619.0,1352.0&gt;-&lt;587.0,1406.5&gt;&gt; = 7.614189346743762

* uni0683 (U+FB76): B&lt;&lt;544.0,175.0&gt;-&lt;586.0,128.0&gt;-&lt;603.0,83.0&gt;&gt;/B&lt;&lt;603.0,83.0&gt;-&lt;602.0,90.0&gt;-&lt;602.0,96.0&gt;&gt; = 12.565348379907297

* uni0683 (U+FB76): B&lt;&lt;669.0,-37.0&gt;-&lt;627.0,8.0&gt;-&lt;610.0,53.0&gt;&gt;/B&lt;&lt;610.0,53.0&gt;-&lt;611.0,47.0&gt;-&lt;611.0,41.0&gt;&gt; = 11.233128526037627

* uni0685 (U+0685): B&lt;&lt;685.0,1265.0&gt;-&lt;727.0,1218.0&gt;-&lt;744.0,1173.0&gt;&gt;/B&lt;&lt;744.0,1173.0&gt;-&lt;743.0,1180.0&gt;-&lt;744.0,1186.0&gt;&gt; = 12.565348379907297

* uni0685.fina: B&lt;&lt;685.0,1265.0&gt;-&lt;727.0,1218.0&gt;-&lt;744.0,1173.0&gt;&gt;/B&lt;&lt;744.0,1173.0&gt;-&lt;743.0,1180.0&gt;-&lt;744.0,1186.0&gt;&gt; = 12.565348379907297

* uni0685.init: B&lt;&lt;837.0,1225.0&gt;-&lt;795.0,1270.0&gt;-&lt;778.0,1315.0&gt;&gt;/B&lt;&lt;778.0,1315.0&gt;-&lt;779.0,1309.0&gt;-&lt;778.0,1303.0&gt;&gt; = 11.233128526037627

* uni0685.medi: B&lt;&lt;837.0,1225.0&gt;-&lt;795.0,1270.0&gt;-&lt;778.0,1315.0&gt;&gt;/B&lt;&lt;778.0,1315.0&gt;-&lt;779.0,1309.0&gt;-&lt;778.0,1303.0&gt;&gt; = 11.233128526037627

* uni0686 (U+FB7A): B&lt;&lt;563.0,396.5&gt;-&lt;476.0,335.0&gt;-&lt;400.0,262.0&gt;&gt;/B&lt;&lt;400.0,262.0&gt;-&lt;438.0,288.0&gt;-&lt;461.0,290.0&gt;&gt; = 9.466204825049774

* uni0686 (U+FB7A): B&lt;&lt;661.5,29.0&gt;-&lt;619.0,75.0&gt;-&lt;603.0,121.0&gt;&gt;/B&lt;&lt;603.0,121.0&gt;-&lt;604.0,112.0&gt;-&lt;604.0,104.0&gt;&gt; = 12.83881627990079

* uni0687 (U+FB7E): B&lt;&lt;505.0,-55.5&gt;-&lt;538.0,-96.0&gt;-&lt;553.0,-134.0&gt;&gt;/B&lt;&lt;553.0,-134.0&gt;-&lt;552.0,-127.0&gt;-&lt;552.0,-121.0&gt;&gt; = 13.410873564382426

* uni0687 (U+FB7E): B&lt;&lt;565.5,291.5&gt;-&lt;599.0,251.0&gt;-&lt;614.0,212.0&gt;&gt;/B&lt;&lt;614.0,212.0&gt;-&lt;613.0,219.0&gt;-&lt;613.0,225.0&gt;&gt; = 12.90740867126579

* uni0687 (U+FB7E): B&lt;&lt;598.0,-229.5&gt;-&lt;572.0,-196.0&gt;-&lt;560.0,-164.0&gt;&gt;/B&lt;&lt;560.0,-164.0&gt;-&lt;561.0,-170.0&gt;-&lt;561.0,-176.0&gt;&gt; = 11.093723011557817

* uni0687 (U+FB7E): B&lt;&lt;668.0,105.0&gt;-&lt;635.0,144.0&gt;-&lt;621.0,182.0&gt;&gt;/B&lt;&lt;621.0,182.0&gt;-&lt;622.0,176.0&gt;-&lt;622.0,170.0&gt;&gt; = 10.762537223142443

* uni0688 (U+FB88): L&lt;&lt;709.0,1778.0&gt;--&lt;646.0,1428.0&gt;&gt;/B&lt;&lt;646.0,1428.0&gt;-&lt;669.0,1529.0&gt;-&lt;732.0,1582.0&gt;&gt; = 2.624809149723495

* uni068B (U+068B): L&lt;&lt;709.0,1778.0&gt;--&lt;646.0,1428.0&gt;&gt;/B&lt;&lt;646.0,1428.0&gt;-&lt;669.0,1529.0&gt;-&lt;732.0,1582.0&gt;&gt; = 2.624809149723495

* uni068B.fina: L&lt;&lt;649.0,1778.0&gt;--&lt;586.0,1428.0&gt;&gt;/B&lt;&lt;586.0,1428.0&gt;-&lt;609.0,1529.0&gt;-&lt;672.0,1582.0&gt;&gt; = 2.624809149723495

* uni068C (U+FB84): B&lt;&lt;741.5,1573.0&gt;-&lt;783.0,1526.0&gt;-&lt;800.0,1481.0&gt;&gt;/B&lt;&lt;800.0,1481.0&gt;-&lt;799.0,1488.0&gt;-&lt;800.0,1494.0&gt;&gt; = 12.565348379907297

* uni068C (U+FB84): B&lt;&lt;867.0,1361.0&gt;-&lt;825.0,1406.0&gt;-&lt;808.0,1451.0&gt;&gt;/B&lt;&lt;808.0,1451.0&gt;-&lt;809.0,1445.0&gt;-&lt;808.0,1439.0&gt;&gt; = 11.233128526037627

* uni068D (U+FB82): B&lt;&lt;445.5,-106.0&gt;-&lt;487.0,-153.0&gt;-&lt;504.0,-198.0&gt;&gt;/B&lt;&lt;504.0,-198.0&gt;-&lt;503.0,-191.0&gt;-&lt;504.0,-185.0&gt;&gt; = 12.565348379907297

* uni068D (U+FB82): B&lt;&lt;571.0,-318.0&gt;-&lt;529.0,-273.0&gt;-&lt;512.0,-228.0&gt;&gt;/B&lt;&lt;512.0,-228.0&gt;-&lt;513.0,-234.0&gt;-&lt;512.0,-240.0&gt;&gt; = 11.233128526037627

* uni068E (U+FB86): B&lt;&lt;730.0,1508.0&gt;-&lt;772.0,1461.0&gt;-&lt;789.0,1416.0&gt;&gt;/B&lt;&lt;789.0,1416.0&gt;-&lt;788.0,1423.0&gt;-&lt;788.0,1429.0&gt;&gt; = 12.565348379907297

* uni068E (U+FB86): B&lt;&lt;855.5,1296.0&gt;-&lt;814.0,1341.0&gt;-&lt;796.0,1386.0&gt;&gt;/B&lt;&lt;796.0,1386.0&gt;-&lt;797.0,1380.0&gt;-&lt;797.0,1374.0&gt;&gt; = 12.33908727832621

* uni068F (U+068F): B&lt;&lt;902.5,1571.0&gt;-&lt;860.0,1617.0&gt;-&lt;844.0,1663.0&gt;&gt;/B&lt;&lt;844.0,1663.0&gt;-&lt;845.0,1654.0&gt;-&lt;845.0,1646.0&gt;&gt; = 12.83881627990079

* uni068F.fina: B&lt;&lt;828.5,1571.0&gt;-&lt;786.0,1617.0&gt;-&lt;770.0,1663.0&gt;&gt;/B&lt;&lt;770.0,1663.0&gt;-&lt;771.0,1654.0&gt;-&lt;771.0,1646.0&gt;&gt; = 12.83881627990079

* uni0690 (U+0690): B&lt;&lt;396.0,-465.5&gt;-&lt;429.0,-506.0&gt;-&lt;443.0,-544.0&gt;&gt;/B&lt;&lt;443.0,-544.0&gt;-&lt;442.0,-537.0&gt;-&lt;443.0,-531.0&gt;&gt; = 12.094757077012089

* uni0690 (U+0690): B&lt;&lt;445.5,-106.0&gt;-&lt;487.0,-153.0&gt;-&lt;504.0,-198.0&gt;&gt;/B&lt;&lt;504.0,-198.0&gt;-&lt;503.0,-191.0&gt;-&lt;504.0,-185.0&gt;&gt; = 12.565348379907297

* uni0690 (U+0690): B&lt;&lt;510.0,-664.0&gt;-&lt;468.0,-619.0&gt;-&lt;451.0,-574.0&gt;&gt;/B&lt;&lt;451.0,-574.0&gt;-&lt;452.0,-580.0&gt;-&lt;451.0,-586.0&gt;&gt; = 11.233128526037627

* uni0690 (U+0690): B&lt;&lt;559.0,-305.0&gt;-&lt;526.0,-266.0&gt;-&lt;512.0,-228.0&gt;&gt;/B&lt;&lt;512.0,-228.0&gt;-&lt;513.0,-234.0&gt;-&lt;512.0,-240.0&gt;&gt; = 10.762537223142443

* uni0690.fina: B&lt;&lt;322.0,-465.5&gt;-&lt;355.0,-506.0&gt;-&lt;369.0,-544.0&gt;&gt;/B&lt;&lt;369.0,-544.0&gt;-&lt;368.0,-537.0&gt;-&lt;369.0,-531.0&gt;&gt; = 12.094757077012089

* uni0690.fina: B&lt;&lt;371.5,-106.0&gt;-&lt;413.0,-153.0&gt;-&lt;430.0,-198.0&gt;&gt;/B&lt;&lt;430.0,-198.0&gt;-&lt;429.0,-191.0&gt;-&lt;430.0,-185.0&gt;&gt; = 12.565348379907297

* uni0690.fina: B&lt;&lt;436.0,-664.0&gt;-&lt;394.0,-619.0&gt;-&lt;377.0,-574.0&gt;&gt;/B&lt;&lt;377.0,-574.0&gt;-&lt;378.0,-580.0&gt;-&lt;377.0,-586.0&gt;&gt; = 11.233128526037627

* uni0690.fina: B&lt;&lt;485.0,-305.0&gt;-&lt;452.0,-266.0&gt;-&lt;438.0,-228.0&gt;&gt;/B&lt;&lt;438.0,-228.0&gt;-&lt;439.0,-234.0&gt;-&lt;438.0,-240.0&gt;&gt; = 10.762537223142443

* uni0691 (U+FB8C): L&lt;&lt;820.0,1596.0&gt;--&lt;757.0,1246.0&gt;&gt;/B&lt;&lt;757.0,1246.0&gt;-&lt;780.0,1347.0&gt;-&lt;843.0,1400.0&gt;&gt; = 2.624809149723495

* uni0697 (U+0697): B&lt;&lt;708.0,1264.0&gt;-&lt;750.0,1217.0&gt;-&lt;767.0,1172.0&gt;&gt;/B&lt;&lt;767.0,1172.0&gt;-&lt;766.0,1179.0&gt;-&lt;766.0,1185.0&gt;&gt; = 12.565348379907297

* uni0697 (U+0697): B&lt;&lt;833.0,1052.0&gt;-&lt;791.0,1097.0&gt;-&lt;774.0,1142.0&gt;&gt;/B&lt;&lt;774.0,1142.0&gt;-&lt;775.0,1136.0&gt;-&lt;775.0,1130.0&gt;&gt; = 11.233128526037627

* uni0697.fina: B&lt;&lt;698.0,1207.0&gt;-&lt;740.0,1160.0&gt;-&lt;757.0,1115.0&gt;&gt;/B&lt;&lt;757.0,1115.0&gt;-&lt;756.0,1122.0&gt;-&lt;756.0,1128.0&gt;&gt; = 12.565348379907297

* uni0697.fina: B&lt;&lt;823.0,995.0&gt;-&lt;781.0,1040.0&gt;-&lt;764.0,1085.0&gt;&gt;/B&lt;&lt;764.0,1085.0&gt;-&lt;765.0,1079.0&gt;-&lt;765.0,1073.0&gt;&gt; = 11.233128526037627

* uni0698 (U+FB8A): B&lt;&lt;710.0,1265.0&gt;-&lt;752.0,1218.0&gt;-&lt;769.0,1173.0&gt;&gt;/B&lt;&lt;769.0,1173.0&gt;-&lt;768.0,1180.0&gt;-&lt;769.0,1186.0&gt;&gt; = 12.565348379907297

* uni0699 (U+0699): B&lt;&lt;721.5,1250.5&gt;-&lt;754.0,1210.0&gt;-&lt;769.0,1172.0&gt;&gt;/B&lt;&lt;769.0,1172.0&gt;-&lt;768.0,1179.0&gt;-&lt;768.0,1185.0&gt;&gt; = 13.410873564382426

* uni0699 (U+0699): B&lt;&lt;771.0,1610.0&gt;-&lt;813.0,1563.0&gt;-&lt;830.0,1518.0&gt;&gt;/B&lt;&lt;830.0,1518.0&gt;-&lt;829.0,1525.0&gt;-&lt;829.0,1531.0&gt;&gt; = 12.565348379907297

* uni0699 (U+0699): B&lt;&lt;835.0,1052.0&gt;-&lt;793.0,1097.0&gt;-&lt;776.0,1142.0&gt;&gt;/B&lt;&lt;776.0,1142.0&gt;-&lt;777.0,1136.0&gt;-&lt;777.0,1130.0&gt;&gt; = 11.233128526037627

* uni0699 (U+0699): B&lt;&lt;884.5,1411.0&gt;-&lt;852.0,1450.0&gt;-&lt;837.0,1488.0&gt;&gt;/B&lt;&lt;837.0,1488.0&gt;-&lt;838.0,1482.0&gt;-&lt;838.0,1476.0&gt;&gt; = 12.078653710512796

* uni0699.fina: B&lt;&lt;711.5,1193.5&gt;-&lt;744.0,1153.0&gt;-&lt;759.0,1115.0&gt;&gt;/B&lt;&lt;759.0,1115.0&gt;-&lt;758.0,1122.0&gt;-&lt;758.0,1128.0&gt;&gt; = 13.410873564382426

* uni0699.fina: B&lt;&lt;761.0,1553.0&gt;-&lt;803.0,1506.0&gt;-&lt;820.0,1461.0&gt;&gt;/B&lt;&lt;820.0,1461.0&gt;-&lt;819.0,1468.0&gt;-&lt;819.0,1474.0&gt;&gt; = 12.565348379907297

* uni0699.fina: B&lt;&lt;825.0,995.0&gt;-&lt;783.0,1040.0&gt;-&lt;766.0,1085.0&gt;&gt;/B&lt;&lt;766.0,1085.0&gt;-&lt;767.0,1079.0&gt;-&lt;767.0,1073.0&gt;&gt; = 11.233128526037627

* uni0699.fina: B&lt;&lt;874.5,1354.0&gt;-&lt;842.0,1393.0&gt;-&lt;827.0,1431.0&gt;&gt;/B&lt;&lt;827.0,1431.0&gt;-&lt;828.0,1425.0&gt;-&lt;828.0,1419.0&gt;&gt; = 12.078653710512796

* uni069D.fina: B&lt;&lt;999.5,504.5&gt;-&lt;929.0,415.0&gt;-&lt;817.0,395.0&gt;&gt;/L&lt;&lt;817.0,395.0&gt;--&lt;1295.0,402.0&gt;&gt; = 9.285672095801052

* uni069E.fina: B&lt;&lt;999.5,504.5&gt;-&lt;929.0,415.0&gt;-&lt;817.0,395.0&gt;&gt;/L&lt;&lt;817.0,395.0&gt;--&lt;1295.0,402.0&gt;&gt; = 9.285672095801052

* uni069F (U+069F): B&lt;&lt;1077.0,1225.0&gt;-&lt;1035.0,1270.0&gt;-&lt;1018.0,1315.0&gt;&gt;/B&lt;&lt;1018.0,1315.0&gt;-&lt;1019.0,1309.0&gt;-&lt;1018.0,1303.0&gt;&gt; = 11.233128526037627

* uni069F (U+069F): B&lt;&lt;702.0,1242.5&gt;-&lt;678.0,1284.0&gt;-&lt;680.0,1315.0&gt;&gt;/L&lt;&lt;680.0,1315.0&gt;--&lt;555.0,602.0&gt;&gt; = 6.252402027412666

* uni069F (U+069F): L&lt;&lt;680.0,1315.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.2276701947233275

* uni069F (U+069F): L&lt;&lt;714.0,1503.0&gt;--&lt;680.0,1315.0&gt;&gt;/B&lt;&lt;680.0,1315.0&gt;-&lt;688.0,1345.0&gt;-&lt;725.0,1384.5&gt;&gt; = 4.680218427320063

* uni069F.fina: B&lt;&lt;1077.0,1225.0&gt;-&lt;1035.0,1270.0&gt;-&lt;1018.0,1315.0&gt;&gt;/B&lt;&lt;1018.0,1315.0&gt;-&lt;1019.0,1309.0&gt;-&lt;1018.0,1303.0&gt;&gt; = 11.233128526037627

* uni069F.fina: B&lt;&lt;702.0,1242.5&gt;-&lt;678.0,1284.0&gt;-&lt;680.0,1315.0&gt;&gt;/L&lt;&lt;680.0,1315.0&gt;--&lt;555.0,602.0&gt;&gt; = 6.252402027412666

* uni069F.fina: L&lt;&lt;680.0,1315.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.2276701947233275

* uni069F.fina: L&lt;&lt;714.0,1503.0&gt;--&lt;680.0,1315.0&gt;&gt;/B&lt;&lt;680.0,1315.0&gt;-&lt;688.0,1345.0&gt;-&lt;725.0,1384.5&gt;&gt; = 4.680218427320063

* uni069F.init: B&lt;&lt;951.0,1435.0&gt;-&lt;993.0,1388.0&gt;-&lt;1010.0,1343.0&gt;&gt;/B&lt;&lt;1010.0,1343.0&gt;-&lt;1009.0,1350.0&gt;-&lt;1010.0,1356.0&gt;&gt; = 12.565348379907297

* uni069F.init: L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uni069F.medi: B&lt;&lt;1077.0,1225.0&gt;-&lt;1035.0,1270.0&gt;-&lt;1018.0,1315.0&gt;&gt;/B&lt;&lt;1018.0,1315.0&gt;-&lt;1019.0,1309.0&gt;-&lt;1018.0,1303.0&gt;&gt; = 11.233128526037627

* uni069F.medi: L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uni06A0 (U+06A0): B&lt;&lt;546.5,1510.0&gt;-&lt;588.0,1463.0&gt;-&lt;605.0,1418.0&gt;&gt;/B&lt;&lt;605.0,1418.0&gt;-&lt;604.0,1425.0&gt;-&lt;605.0,1431.0&gt;&gt; = 12.565348379907297

* uni06A0 (U+06A0): B&lt;&lt;672.0,1298.0&gt;-&lt;630.0,1343.0&gt;-&lt;613.0,1388.0&gt;&gt;/B&lt;&lt;613.0,1388.0&gt;-&lt;614.0,1382.0&gt;-&lt;613.0,1376.0&gt;&gt; = 11.233128526037627

* uni06A0.fina: B&lt;&lt;689.0,1508.0&gt;-&lt;731.0,1461.0&gt;-&lt;748.0,1416.0&gt;&gt;/B&lt;&lt;748.0,1416.0&gt;-&lt;747.0,1423.0&gt;-&lt;747.0,1429.0&gt;&gt; = 12.565348379907297

* uni06A0.fina: B&lt;&lt;814.5,1296.0&gt;-&lt;773.0,1341.0&gt;-&lt;755.0,1386.0&gt;&gt;/B&lt;&lt;755.0,1386.0&gt;-&lt;756.0,1380.0&gt;-&lt;756.0,1374.0&gt;&gt; = 12.33908727832621

* uni06A0.init: B&lt;&lt;844.0,1435.0&gt;-&lt;886.0,1388.0&gt;-&lt;903.0,1343.0&gt;&gt;/B&lt;&lt;903.0,1343.0&gt;-&lt;902.0,1350.0&gt;-&lt;903.0,1356.0&gt;&gt; = 12.565348379907297

* uni06A0.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni06A0.medi: B&lt;&lt;719.5,1482.0&gt;-&lt;761.0,1435.0&gt;-&lt;778.0,1390.0&gt;&gt;/B&lt;&lt;778.0,1390.0&gt;-&lt;777.0,1397.0&gt;-&lt;778.0,1403.0&gt;&gt; = 12.565348379907297

* uni06A0.medi: B&lt;&lt;845.0,1270.0&gt;-&lt;803.0,1315.0&gt;-&lt;786.0,1360.0&gt;&gt;/B&lt;&lt;786.0,1360.0&gt;-&lt;787.0,1354.0&gt;-&lt;786.0,1348.0&gt;&gt; = 11.233128526037627

* uni06A1 (U+06A1): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni06A1.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni06A2 (U+06A2): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni06A2.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni06A3 (U+06A3): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni06A3.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni06A4 (U+FB6A): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni06A4 (U+FB6A): B&lt;&lt;851.0,1508.0&gt;-&lt;893.0,1461.0&gt;-&lt;910.0,1416.0&gt;&gt;/B&lt;&lt;910.0,1416.0&gt;-&lt;909.0,1423.0&gt;-&lt;909.0,1429.0&gt;&gt; = 12.565348379907297

* uni06A4 (U+FB6A): B&lt;&lt;976.5,1296.0&gt;-&lt;935.0,1341.0&gt;-&lt;917.0,1386.0&gt;&gt;/B&lt;&lt;917.0,1386.0&gt;-&lt;918.0,1380.0&gt;-&lt;918.0,1374.0&gt;&gt; = 12.33908727832621

* uni06A5 (U+06A5): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni06A5 (U+06A5): B&lt;&lt;698.5,-272.0&gt;-&lt;656.0,-226.0&gt;-&lt;640.0,-180.0&gt;&gt;/B&lt;&lt;640.0,-180.0&gt;-&lt;641.0,-189.0&gt;-&lt;641.0,-197.0&gt;&gt; = 12.83881627990079

* uni06A5.fina: B&lt;&lt;675.5,-272.0&gt;-&lt;633.0,-226.0&gt;-&lt;617.0,-180.0&gt;&gt;/B&lt;&lt;617.0,-180.0&gt;-&lt;618.0,-189.0&gt;-&lt;618.0,-197.0&gt;&gt; = 12.83881627990079

* uni06A5.init: B&lt;&lt;698.5,-272.0&gt;-&lt;656.0,-226.0&gt;-&lt;640.0,-180.0&gt;&gt;/B&lt;&lt;640.0,-180.0&gt;-&lt;641.0,-189.0&gt;-&lt;641.0,-197.0&gt;&gt; = 12.83881627990079

* uni06A5.medi: B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uni06A5.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni06A6 (U+FB6E): B&lt;&lt;1012.5,1581.0&gt;-&lt;980.0,1620.0&gt;-&lt;965.0,1658.0&gt;&gt;/B&lt;&lt;965.0,1658.0&gt;-&lt;966.0,1652.0&gt;-&lt;966.0,1646.0&gt;&gt; = 12.078653710512796

* uni06A6 (U+FB6E): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni06A6 (U+FB6E): B&lt;&lt;849.5,1420.5&gt;-&lt;882.0,1380.0&gt;-&lt;897.0,1342.0&gt;&gt;/B&lt;&lt;897.0,1342.0&gt;-&lt;896.0,1349.0&gt;-&lt;896.0,1355.0&gt;&gt; = 13.410873564382426

* uni06A6 (U+FB6E): B&lt;&lt;899.0,1780.0&gt;-&lt;941.0,1733.0&gt;-&lt;958.0,1688.0&gt;&gt;/B&lt;&lt;958.0,1688.0&gt;-&lt;957.0,1695.0&gt;-&lt;957.0,1701.0&gt;&gt; = 12.565348379907297

* uni06A6 (U+FB6E): B&lt;&lt;963.0,1222.0&gt;-&lt;921.0,1267.0&gt;-&lt;904.0,1312.0&gt;&gt;/B&lt;&lt;904.0,1312.0&gt;-&lt;905.0,1306.0&gt;-&lt;905.0,1300.0&gt;&gt; = 11.233128526037627

* uni06A7.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni06A8 (U+06A8): B&lt;&lt;1062.5,1296.0&gt;-&lt;1021.0,1341.0&gt;-&lt;1003.0,1386.0&gt;&gt;/B&lt;&lt;1003.0,1386.0&gt;-&lt;1004.0,1380.0&gt;-&lt;1004.0,1374.0&gt;&gt; = 12.33908727832621

* uni06A8 (U+06A8): B&lt;&lt;937.0,1508.0&gt;-&lt;979.0,1461.0&gt;-&lt;996.0,1416.0&gt;&gt;/B&lt;&lt;996.0,1416.0&gt;-&lt;995.0,1423.0&gt;-&lt;995.0,1429.0&gt;&gt; = 12.565348379907297

* uni06A8.fina: B&lt;&lt;1027.0,1094.0&gt;-&lt;985.0,1139.0&gt;-&lt;968.0,1184.0&gt;&gt;/B&lt;&lt;968.0,1184.0&gt;-&lt;969.0,1178.0&gt;-&lt;968.0,1172.0&gt;&gt; = 11.233128526037627

* uni06A8.fina: B&lt;&lt;901.5,1306.0&gt;-&lt;943.0,1259.0&gt;-&lt;960.0,1214.0&gt;&gt;/B&lt;&lt;960.0,1214.0&gt;-&lt;959.0,1221.0&gt;-&lt;960.0,1227.0&gt;&gt; = 12.565348379907297

* uni06A8.init: B&lt;&lt;1062.5,1296.0&gt;-&lt;1021.0,1341.0&gt;-&lt;1003.0,1386.0&gt;&gt;/B&lt;&lt;1003.0,1386.0&gt;-&lt;1004.0,1380.0&gt;-&lt;1004.0,1374.0&gt;&gt; = 12.33908727832621

* uni06A8.init: B&lt;&lt;937.0,1508.0&gt;-&lt;979.0,1461.0&gt;-&lt;996.0,1416.0&gt;&gt;/B&lt;&lt;996.0,1416.0&gt;-&lt;995.0,1423.0&gt;-&lt;995.0,1429.0&gt;&gt; = 12.565348379907297

* uni06A8.medi: B&lt;&lt;725.0,1492.0&gt;-&lt;767.0,1445.0&gt;-&lt;784.0,1400.0&gt;&gt;/B&lt;&lt;784.0,1400.0&gt;-&lt;783.0,1407.0&gt;-&lt;784.0,1413.0&gt;&gt; = 12.565348379907297

* uni06A8.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni06AD (U+FBD3): B&lt;&lt;706.0,1508.0&gt;-&lt;748.0,1461.0&gt;-&lt;765.0,1416.0&gt;&gt;/B&lt;&lt;765.0,1416.0&gt;-&lt;764.0,1423.0&gt;-&lt;764.0,1429.0&gt;&gt; = 12.565348379907297

* uni06AD (U+FBD3): B&lt;&lt;831.5,1296.0&gt;-&lt;790.0,1341.0&gt;-&lt;772.0,1386.0&gt;&gt;/B&lt;&lt;772.0,1386.0&gt;-&lt;773.0,1380.0&gt;-&lt;773.0,1374.0&gt;&gt; = 12.33908727832621

* uni06AD (U+FBD3): L&lt;&lt;1102.0,1429.0&gt;--&lt;1102.0,1426.0&gt;&gt;/L&lt;&lt;1102.0,1426.0&gt;--&lt;1118.0,1515.0&gt;&gt; = 10.191501850027691

* uni06AD (U+FBD3): L&lt;&lt;992.0,790.0&gt;--&lt;1099.0,1407.0&gt;&gt;/B&lt;&lt;1099.0,1407.0&gt;-&lt;1086.0,1376.0&gt;-&lt;1049.5,1339.5&gt;&gt; = 12.912604273903883

* uni06AD (U+FBD3): L&lt;&lt;992.0,793.0&gt;--&lt;992.0,790.0&gt;&gt;/L&lt;&lt;992.0,790.0&gt;--&lt;1099.0,1407.0&gt;&gt; = 9.838372068883682

* uni06AE (U+06AE): B&lt;&lt;688.0,-190.0&gt;-&lt;646.0,-144.0&gt;-&lt;629.0,-98.0&gt;&gt;/B&lt;&lt;629.0,-98.0&gt;-&lt;631.0,-107.0&gt;-&lt;630.0,-115.0&gt;&gt; = 7.753751379765042

* uni06AE (U+06AE): L&lt;&lt;623.0,-75.0&gt;--&lt;623.0,-76.0&gt;&gt;/B&lt;&lt;623.0,-76.0&gt;-&lt;622.0,-67.0&gt;-&lt;622.0,-58.0&gt;&gt; = 6.340191745909908

* uni06AE.fina: B&lt;&lt;673.5,-272.0&gt;-&lt;631.0,-226.0&gt;-&lt;615.0,-180.0&gt;&gt;/B&lt;&lt;615.0,-180.0&gt;-&lt;616.0,-189.0&gt;-&lt;616.0,-197.0&gt;&gt; = 12.83881627990079

* uni06AE.init: B&lt;&lt;673.5,-272.0&gt;-&lt;631.0,-226.0&gt;-&lt;615.0,-180.0&gt;&gt;/B&lt;&lt;615.0,-180.0&gt;-&lt;616.0,-189.0&gt;-&lt;616.0,-197.0&gt;&gt; = 12.83881627990079

* uni06AE.medi: B&lt;&lt;673.5,-272.0&gt;-&lt;631.0,-226.0&gt;-&lt;615.0,-180.0&gt;&gt;/B&lt;&lt;615.0,-180.0&gt;-&lt;616.0,-189.0&gt;-&lt;616.0,-197.0&gt;&gt; = 12.83881627990079

* uni06B1 (U+FB9A): B&lt;&lt;528.5,1782.0&gt;-&lt;570.0,1735.0&gt;-&lt;587.0,1690.0&gt;&gt;/B&lt;&lt;587.0,1690.0&gt;-&lt;586.0,1697.0&gt;-&lt;587.0,1703.0&gt;&gt; = 12.565348379907297

* uni06B2 (U+06B2): B&lt;&lt;453.5,-61.0&gt;-&lt;495.0,-108.0&gt;-&lt;512.0,-153.0&gt;&gt;/B&lt;&lt;512.0,-153.0&gt;-&lt;511.0,-146.0&gt;-&lt;512.0,-140.0&gt;&gt; = 12.565348379907297

* uni06B2.fina: B&lt;&lt;453.5,-61.0&gt;-&lt;495.0,-108.0&gt;-&lt;512.0,-153.0&gt;&gt;/B&lt;&lt;512.0,-153.0&gt;-&lt;511.0,-146.0&gt;-&lt;512.0,-140.0&gt;&gt; = 12.565348379907297

* uni06B2.init: B&lt;&lt;453.5,-61.0&gt;-&lt;495.0,-108.0&gt;-&lt;512.0,-153.0&gt;&gt;/B&lt;&lt;512.0,-153.0&gt;-&lt;511.0,-146.0&gt;-&lt;512.0,-140.0&gt;&gt; = 12.565348379907297

* uni06B2.medi: B&lt;&lt;482.5,-61.0&gt;-&lt;524.0,-108.0&gt;-&lt;541.0,-153.0&gt;&gt;/B&lt;&lt;541.0,-153.0&gt;-&lt;540.0,-146.0&gt;-&lt;541.0,-140.0&gt;&gt; = 12.565348379907297

* uni06B4 (U+06B4): B&lt;&lt;234.5,869.0&gt;-&lt;276.0,822.0&gt;-&lt;293.0,777.0&gt;&gt;/B&lt;&lt;293.0,777.0&gt;-&lt;292.0,784.0&gt;-&lt;293.0,790.0&gt;&gt; = 12.565348379907297

* uni06B4.fina: B&lt;&lt;1002.0,799.0&gt;-&lt;960.0,844.0&gt;-&lt;943.0,889.0&gt;&gt;/B&lt;&lt;943.0,889.0&gt;-&lt;944.0,883.0&gt;-&lt;943.0,877.0&gt;&gt; = 11.233128526037627

* uni06B4.fina: B&lt;&lt;876.5,1011.0&gt;-&lt;918.0,964.0&gt;-&lt;935.0,919.0&gt;&gt;/B&lt;&lt;935.0,919.0&gt;-&lt;934.0,926.0&gt;-&lt;935.0,932.0&gt;&gt; = 12.565348379907297

* uni06B4.init: B&lt;&lt;331.5,665.0&gt;-&lt;373.0,618.0&gt;-&lt;390.0,573.0&gt;&gt;/B&lt;&lt;390.0,573.0&gt;-&lt;389.0,580.0&gt;-&lt;390.0,586.0&gt;&gt; = 12.565348379907297

* uni06B4.init: B&lt;&lt;457.0,453.0&gt;-&lt;415.0,498.0&gt;-&lt;398.0,543.0&gt;&gt;/B&lt;&lt;398.0,543.0&gt;-&lt;399.0,537.0&gt;-&lt;398.0,531.0&gt;&gt; = 11.233128526037627

* uni06B4.init: B&lt;&lt;626.5,740.0&gt;-&lt;649.0,723.0&gt;-&lt;669.0,699.0&gt;&gt;/L&lt;&lt;669.0,699.0&gt;--&lt;604.0,780.0&gt;&gt; = 1.0596038361818578

* uni06B4.init: L&lt;&lt;908.0,403.0&gt;--&lt;678.0,687.0&gt;&gt;/B&lt;&lt;678.0,687.0&gt;-&lt;700.0,659.0&gt;-&lt;714.5,628.0&gt;&gt; = 0.8453728387151459

* uni06B4.medi: B&lt;&lt;865.5,1011.0&gt;-&lt;907.0,964.0&gt;-&lt;924.0,919.0&gt;&gt;/B&lt;&lt;924.0,919.0&gt;-&lt;923.0,926.0&gt;-&lt;924.0,932.0&gt;&gt; = 12.565348379907297

* uni06B4.medi: B&lt;&lt;991.0,799.0&gt;-&lt;949.0,844.0&gt;-&lt;932.0,889.0&gt;&gt;/B&lt;&lt;932.0,889.0&gt;-&lt;933.0,883.0&gt;-&lt;932.0,877.0&gt;&gt; = 11.233128526037627

* uni06B7 (U+06B7): B&lt;&lt;1058.0,1492.0&gt;-&lt;1082.0,1450.0&gt;-&lt;1080.0,1419.0&gt;&gt;/L&lt;&lt;1080.0,1419.0&gt;--&lt;1097.0,1515.0&gt;&gt; = 6.350637649078193

* uni06B7 (U+06B7): B&lt;&lt;683.5,1510.0&gt;-&lt;725.0,1463.0&gt;-&lt;742.0,1418.0&gt;&gt;/B&lt;&lt;742.0,1418.0&gt;-&lt;741.0,1425.0&gt;-&lt;742.0,1431.0&gt;&gt; = 12.565348379907297

* uni06B7 (U+06B7): B&lt;&lt;809.0,1298.0&gt;-&lt;767.0,1343.0&gt;-&lt;750.0,1388.0&gt;&gt;/B&lt;&lt;750.0,1388.0&gt;-&lt;751.0,1382.0&gt;-&lt;750.0,1376.0&gt;&gt; = 11.233128526037627

* uni06B7 (U+06B7): L&lt;&lt;869.0,227.0&gt;--&lt;1080.0,1419.0&gt;&gt;/B&lt;&lt;1080.0,1419.0&gt;-&lt;1071.0,1388.0&gt;-&lt;1034.0,1349.0&gt;&gt; = 6.151066455756333

* uni06B7.fina: B&lt;&lt;1058.0,1492.0&gt;-&lt;1082.0,1450.0&gt;-&lt;1080.0,1419.0&gt;&gt;/L&lt;&lt;1080.0,1419.0&gt;--&lt;1097.0,1515.0&gt;&gt; = 6.350637649078193

* uni06B7.fina: B&lt;&lt;683.5,1510.0&gt;-&lt;725.0,1463.0&gt;-&lt;742.0,1418.0&gt;&gt;/B&lt;&lt;742.0,1418.0&gt;-&lt;741.0,1425.0&gt;-&lt;742.0,1431.0&gt;&gt; = 12.565348379907297

* uni06B7.fina: B&lt;&lt;809.0,1298.0&gt;-&lt;767.0,1343.0&gt;-&lt;750.0,1388.0&gt;&gt;/B&lt;&lt;750.0,1388.0&gt;-&lt;751.0,1382.0&gt;-&lt;750.0,1376.0&gt;&gt; = 11.233128526037627

* uni06B7.fina: L&lt;&lt;869.0,227.0&gt;--&lt;1080.0,1419.0&gt;&gt;/B&lt;&lt;1080.0,1419.0&gt;-&lt;1071.0,1388.0&gt;-&lt;1034.0,1349.0&gt;&gt; = 6.151066455756333

* uni06B7.init: B&lt;&lt;580.0,1258.0&gt;-&lt;622.0,1211.0&gt;-&lt;639.0,1166.0&gt;&gt;/B&lt;&lt;639.0,1166.0&gt;-&lt;638.0,1173.0&gt;-&lt;638.0,1179.0&gt;&gt; = 12.565348379907297

* uni06B7.init: B&lt;&lt;705.0,1046.0&gt;-&lt;663.0,1091.0&gt;-&lt;646.0,1136.0&gt;&gt;/B&lt;&lt;646.0,1136.0&gt;-&lt;647.0,1130.0&gt;-&lt;647.0,1124.0&gt;&gt; = 11.233128526037627

* uni06B8 (U+06B8): B&lt;&lt;101.0,-267.0&gt;-&lt;114.0,-269.0&gt;-&lt;130.0,-279.0&gt;&gt;/B&lt;&lt;130.0,-279.0&gt;-&lt;56.0,-215.0&gt;-&lt;25.0,-113.0&gt;&gt; = 8.849993050812152

* uni06B8 (U+06B8): B&lt;&lt;119.0,-591.0&gt;-&lt;156.0,-611.0&gt;-&lt;192.0,-659.0&gt;&gt;/B&lt;&lt;192.0,-659.0&gt;-&lt;179.0,-629.0&gt;-&lt;180.0,-607.0&gt;&gt; = 13.441204837098612

* uni06B8 (U+06B8): B&lt;&lt;274.5,-765.0&gt;-&lt;247.0,-743.0&gt;-&lt;225.0,-714.0&gt;&gt;/B&lt;&lt;225.0,-714.0&gt;-&lt;239.0,-746.0&gt;-&lt;238.0,-768.0&gt;&gt; = 13.55532872257627

* uni06B8 (U+06B8): B&lt;&lt;449.0,-380.0&gt;-&lt;272.0,-379.0&gt;-&lt;159.0,-301.0&gt;&gt;/B&lt;&lt;159.0,-301.0&gt;-&lt;193.0,-332.0&gt;-&lt;219.5,-377.0&gt;&gt; = 7.741475393555365

* uni06B8.fina: B&lt;&lt;101.0,-267.0&gt;-&lt;114.0,-269.0&gt;-&lt;130.0,-279.0&gt;&gt;/B&lt;&lt;130.0,-279.0&gt;-&lt;56.0,-215.0&gt;-&lt;25.0,-113.0&gt;&gt; = 8.849993050812152

* uni06B8.fina: B&lt;&lt;119.0,-591.0&gt;-&lt;156.0,-611.0&gt;-&lt;192.0,-659.0&gt;&gt;/B&lt;&lt;192.0,-659.0&gt;-&lt;179.0,-629.0&gt;-&lt;180.0,-607.0&gt;&gt; = 13.441204837098612

* uni06B8.fina: B&lt;&lt;274.5,-765.0&gt;-&lt;247.0,-743.0&gt;-&lt;225.0,-714.0&gt;&gt;/B&lt;&lt;225.0,-714.0&gt;-&lt;239.0,-746.0&gt;-&lt;238.0,-768.0&gt;&gt; = 13.55532872257627

* uni06B8.fina: B&lt;&lt;449.0,-380.0&gt;-&lt;272.0,-379.0&gt;-&lt;159.0,-301.0&gt;&gt;/B&lt;&lt;159.0,-301.0&gt;-&lt;193.0,-332.0&gt;-&lt;219.5,-377.0&gt;&gt; = 7.741475393555365

* uni06B8.init: B&lt;&lt;673.5,-272.0&gt;-&lt;631.0,-226.0&gt;-&lt;615.0,-180.0&gt;&gt;/B&lt;&lt;615.0,-180.0&gt;-&lt;616.0,-189.0&gt;-&lt;616.0,-197.0&gt;&gt; = 12.83881627990079

* uni06B8.medi: B&lt;&lt;598.5,-272.0&gt;-&lt;556.0,-226.0&gt;-&lt;540.0,-180.0&gt;&gt;/B&lt;&lt;540.0,-180.0&gt;-&lt;541.0,-189.0&gt;-&lt;541.0,-197.0&gt;&gt; = 12.83881627990079

* uni06BB (U+FBA0): L&lt;&lt;814.0,1563.0&gt;--&lt;751.0,1213.0&gt;&gt;/B&lt;&lt;751.0,1213.0&gt;-&lt;774.0,1314.0&gt;-&lt;837.0,1367.0&gt;&gt; = 2.624809149723495

* uni06BD (U+06BD): B&lt;&lt;683.0,1263.0&gt;-&lt;725.0,1216.0&gt;-&lt;742.0,1171.0&gt;&gt;/B&lt;&lt;742.0,1171.0&gt;-&lt;741.0,1178.0&gt;-&lt;741.0,1184.0&gt;&gt; = 12.565348379907297

* uni06BD (U+06BD): B&lt;&lt;808.0,1051.0&gt;-&lt;766.0,1096.0&gt;-&lt;749.0,1141.0&gt;&gt;/B&lt;&lt;749.0,1141.0&gt;-&lt;750.0,1135.0&gt;-&lt;750.0,1129.0&gt;&gt; = 11.233128526037627

* uni06BD.fina: B&lt;&lt;629.5,962.0&gt;-&lt;671.0,915.0&gt;-&lt;689.0,870.0&gt;&gt;/B&lt;&lt;689.0,870.0&gt;-&lt;688.0,877.0&gt;-&lt;688.0,883.0&gt;&gt; = 13.67130713219584

* uni06BD.fina: B&lt;&lt;755.0,750.0&gt;-&lt;713.0,795.0&gt;-&lt;696.0,840.0&gt;&gt;/B&lt;&lt;696.0,840.0&gt;-&lt;697.0,834.0&gt;-&lt;697.0,828.0&gt;&gt; = 11.233128526037627

* uni06BD.init: B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uni06BD.init: L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uni06BD.medi: B&lt;&lt;611.5,-208.0&gt;-&lt;569.0,-162.0&gt;-&lt;553.0,-116.0&gt;&gt;/B&lt;&lt;553.0,-116.0&gt;-&lt;555.0,-125.0&gt;-&lt;554.0,-133.0&gt;&gt; = 6.650200316659149

* uni06BD.medi: L&lt;&lt;547.0,-93.0&gt;--&lt;547.0,-94.0&gt;&gt;/B&lt;&lt;547.0,-94.0&gt;-&lt;546.0,-85.0&gt;-&lt;546.0,-76.0&gt;&gt; = 6.340191745909908

* uni06BE.init.comp: B&lt;&lt;268.5,402.0&gt;-&lt;312.0,401.0&gt;-&lt;332.0,393.0&gt;&gt;/B&lt;&lt;332.0,393.0&gt;-&lt;314.0,403.0&gt;-&lt;307.0,439.5&gt;&gt; = 7.253194612725265

* uni06BE.init.comp: B&lt;&lt;515.5,466.0&gt;-&lt;522.0,450.0&gt;-&lt;539.0,437.0&gt;&gt;/B&lt;&lt;539.0,437.0&gt;-&lt;537.0,439.0&gt;-&lt;554.0,447.0&gt;&gt; = 7.594643368591447

* uni06BE.init.comp: B&lt;&lt;935.5,677.5&gt;-&lt;934.0,735.0&gt;-&lt;940.0,777.0&gt;&gt;/B&lt;&lt;940.0,777.0&gt;-&lt;917.0,648.0&gt;-&lt;883.0,550.0&gt;&gt; = 1.9791961383390095

* uni06BF (U+06BF): B&lt;&lt;563.0,396.5&gt;-&lt;476.0,335.0&gt;-&lt;400.0,262.0&gt;&gt;/B&lt;&lt;400.0,262.0&gt;-&lt;438.0,288.0&gt;-&lt;461.0,290.0&gt;&gt; = 9.466204825049774

* uni06BF (U+06BF): B&lt;&lt;661.5,29.0&gt;-&lt;619.0,75.0&gt;-&lt;603.0,121.0&gt;&gt;/B&lt;&lt;603.0,121.0&gt;-&lt;604.0,112.0&gt;-&lt;604.0,104.0&gt;&gt; = 12.83881627990079

* uni06BF.fina: B&lt;&lt;490.0,221.5&gt;-&lt;531.0,175.0&gt;-&lt;548.0,129.0&gt;&gt;/B&lt;&lt;548.0,129.0&gt;-&lt;546.0,138.0&gt;-&lt;546.0,147.0&gt;&gt; = 7.753751379765042

* uni06BF.fina: B&lt;&lt;612.5,15.0&gt;-&lt;570.0,61.0&gt;-&lt;553.0,107.0&gt;&gt;/B&lt;&lt;553.0,107.0&gt;-&lt;555.0,98.0&gt;-&lt;554.0,90.0&gt;&gt; = 7.753751379765042

* uni06BF.init: B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uni06BF.medi: B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uni06C0 (U+FBA4): B&lt;&lt;558.0,1325.0&gt;-&lt;613.0,1352.0&gt;-&lt;670.0,1369.0&gt;&gt;/B&lt;&lt;670.0,1369.0&gt;-&lt;621.0,1361.0&gt;-&lt;588.5,1415.5&gt;&gt; = 7.334378801416706

* uni06C2 (U+06C2): B&lt;&lt;694.0,1378.0&gt;-&lt;749.0,1405.0&gt;-&lt;806.0,1422.0&gt;&gt;/B&lt;&lt;806.0,1422.0&gt;-&lt;757.0,1414.0&gt;-&lt;724.5,1468.5&gt;&gt; = 7.334378801416706

* uni06C3 (U+06C3): B&lt;&lt;822.0,1645.0&gt;-&lt;864.0,1598.0&gt;-&lt;881.0,1553.0&gt;&gt;/B&lt;&lt;881.0,1553.0&gt;-&lt;880.0,1560.0&gt;-&lt;881.0,1566.0&gt;&gt; = 12.565348379907297

* uni06CA (U+06CA): B&lt;&lt;805.0,1112.0&gt;-&lt;763.0,1157.0&gt;-&lt;746.0,1202.0&gt;&gt;/B&lt;&lt;746.0,1202.0&gt;-&lt;747.0,1196.0&gt;-&lt;746.0,1190.0&gt;&gt; = 11.233128526037627

* uni06CA.fina: B&lt;&lt;764.0,1112.0&gt;-&lt;722.0,1157.0&gt;-&lt;705.0,1202.0&gt;&gt;/B&lt;&lt;705.0,1202.0&gt;-&lt;706.0,1196.0&gt;-&lt;705.0,1190.0&gt;&gt; = 11.233128526037627

* uni06CB (U+FBDE): B&lt;&lt;805.0,1112.0&gt;-&lt;763.0,1157.0&gt;-&lt;746.0,1202.0&gt;&gt;/B&lt;&lt;746.0,1202.0&gt;-&lt;747.0,1196.0&gt;-&lt;746.0,1190.0&gt;&gt; = 11.233128526037627

* uni06D1 (U+06D1): B&lt;&lt;472.5,-626.0&gt;-&lt;430.0,-580.0&gt;-&lt;413.0,-534.0&gt;&gt;/B&lt;&lt;413.0,-534.0&gt;-&lt;415.0,-543.0&gt;-&lt;414.0,-551.0&gt;&gt; = 7.753751379765042

* uni06D1.fina: B&lt;&lt;234.5,-884.0&gt;-&lt;207.0,-862.0&gt;-&lt;185.0,-833.0&gt;&gt;/B&lt;&lt;185.0,-833.0&gt;-&lt;199.0,-865.0&gt;-&lt;198.0,-887.0&gt;&gt; = 13.55532872257627

* uni06D1.fina: B&lt;&lt;79.0,-710.0&gt;-&lt;116.0,-730.0&gt;-&lt;152.0,-778.0&gt;&gt;/B&lt;&lt;152.0,-778.0&gt;-&lt;139.0,-748.0&gt;-&lt;140.0,-726.0&gt;&gt; = 13.441204837098612

* uni06D1.init: B&lt;&lt;600.5,-272.0&gt;-&lt;558.0,-226.0&gt;-&lt;542.0,-180.0&gt;&gt;/B&lt;&lt;542.0,-180.0&gt;-&lt;543.0,-189.0&gt;-&lt;543.0,-197.0&gt;&gt; = 12.83881627990079

* uni06D1.medi: B&lt;&lt;611.5,-208.0&gt;-&lt;569.0,-162.0&gt;-&lt;553.0,-116.0&gt;&gt;/B&lt;&lt;553.0,-116.0&gt;-&lt;555.0,-125.0&gt;-&lt;554.0,-133.0&gt;&gt; = 6.650200316659149

* uni06D1.medi: L&lt;&lt;547.0,-93.0&gt;--&lt;547.0,-94.0&gt;&gt;/B&lt;&lt;547.0,-94.0&gt;-&lt;546.0,-85.0&gt;-&lt;546.0,-76.0&gt;&gt; = 6.340191745909908

* uni06D3 (U+FBB0): B&lt;&lt;309.0,1212.0&gt;-&lt;364.0,1239.0&gt;-&lt;421.0,1256.0&gt;&gt;/B&lt;&lt;421.0,1256.0&gt;-&lt;372.0,1248.0&gt;-&lt;339.5,1302.5&gt;&gt; = 7.334378801416706

* uni06D6 (U+06D6): B&lt;&lt;586.5,1139.5&gt;-&lt;560.0,1155.0&gt;-&lt;563.0,1164.0&gt;&gt;/B&lt;&lt;563.0,1164.0&gt;-&lt;556.0,1153.0&gt;-&lt;526.0,1138.5&gt;&gt; = 14.036243467926457

* uni06D7 (U+06D7): B&lt;&lt;668.5,1139.5&gt;-&lt;642.0,1155.0&gt;-&lt;645.0,1164.0&gt;&gt;/B&lt;&lt;645.0,1164.0&gt;-&lt;638.0,1153.0&gt;-&lt;608.0,1138.5&gt;&gt; = 14.036243467926457

* uni06D7 (U+06D7): L&lt;&lt;993.0,1298.0&gt;--&lt;1013.0,1298.0&gt;&gt;/L&lt;&lt;1013.0,1298.0&gt;--&lt;992.0,1299.0&gt;&gt; = 2.726310993906212

* uni06D9 (U+06D9): L&lt;&lt;877.0,1072.0&gt;--&lt;887.0,1073.0&gt;&gt;/B&lt;&lt;887.0,1073.0&gt;-&lt;882.0,1072.0&gt;-&lt;879.0,1074.0&gt;&gt; = 5.599339336520484

* uni06DA (U+06DA): B&lt;&lt;622.0,1486.0&gt;-&lt;674.0,1527.0&gt;-&lt;740.0,1567.0&gt;&gt;/L&lt;&lt;740.0,1567.0&gt;--&lt;631.0,1532.0&gt;&gt; = 13.41653071285549

* uni06DA (U+06DA): B&lt;&lt;661.0,1286.0&gt;-&lt;667.0,1309.0&gt;-&lt;694.0,1342.0&gt;&gt;/B&lt;&lt;694.0,1342.0&gt;-&lt;666.0,1315.0&gt;-&lt;647.5,1289.5&gt;&gt; = 6.75221981350956

* uni06DA (U+06DA): B&lt;&lt;875.0,1196.0&gt;-&lt;833.0,1152.0&gt;-&lt;796.0,1133.0&gt;&gt;/B&lt;&lt;796.0,1133.0&gt;-&lt;831.0,1141.0&gt;-&lt;851.0,1156.5&gt;&gt; = 14.306109525864734

* uni06DB (U+06DB): B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni06DB (U+06DB): B&lt;&lt;818.0,1130.0&gt;-&lt;776.0,1175.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.233128526037627

* uni06DC (U+06DC): L&lt;&lt;1024.0,1436.0&gt;--&lt;1025.0,1438.0&gt;&gt;/B&lt;&lt;1025.0,1438.0&gt;-&lt;1018.0,1425.0&gt;-&lt;988.5,1410.5&gt;&gt; = 1.735704588928346

* uni06DD (U+06DD): B&lt;&lt;426.5,179.5&gt;-&lt;408.0,182.0&gt;-&lt;385.0,186.0&gt;&gt;/B&lt;&lt;385.0,186.0&gt;-&lt;418.0,172.0&gt;-&lt;438.5,139.0&gt;&gt; = 13.122909858996245

* uni06DE (U+06DE): B&lt;&lt;515.0,568.0&gt;-&lt;546.0,591.0&gt;-&lt;579.0,609.0&gt;&gt;/L&lt;&lt;579.0,609.0&gt;--&lt;511.0,575.0&gt;&gt; = 2.0454084888871935

* uni06DE (U+06DE): L&lt;&lt;1016.0,492.0&gt;--&lt;997.0,405.0&gt;&gt;/L&lt;&lt;997.0,405.0&gt;--&lt;1017.0,457.0&gt;&gt; = 8.7180657687852

* uni06DE (U+06DE): L&lt;&lt;1017.0,457.0&gt;--&lt;1016.0,492.0&gt;&gt;/L&lt;&lt;1016.0,492.0&gt;--&lt;997.0,405.0&gt;&gt; = 13.956022298253302

* uni06DE (U+06DE): L&lt;&lt;215.0,445.0&gt;--&lt;216.0,409.0&gt;&gt;/L&lt;&lt;216.0,409.0&gt;--&lt;235.0,496.0&gt;&gt; = 13.910585527831186

* uni06DE (U+06DE): L&lt;&lt;216.0,409.0&gt;--&lt;235.0,496.0&gt;&gt;/L&lt;&lt;235.0,496.0&gt;--&lt;215.0,445.0&gt;&gt; = 9.093524218235117

* uni06DE (U+06DE): L&lt;&lt;346.0,698.0&gt;--&lt;424.0,764.0&gt;&gt;/L&lt;&lt;424.0,764.0&gt;--&lt;385.0,732.0&gt;&gt; = 0.8670410669090247

* uni06DE (U+06DE): L&lt;&lt;385.0,732.0&gt;--&lt;346.0,698.0&gt;&gt;/L&lt;&lt;346.0,698.0&gt;--&lt;424.0,764.0&gt;&gt; = 0.8453928266586264

* uni06DE (U+06DE): L&lt;&lt;540.0,50.0&gt;--&lt;593.0,62.0&gt;&gt;/L&lt;&lt;593.0,62.0&gt;--&lt;506.0,58.0&gt;&gt; = 10.125097291890148

* uni06DE (U+06DE): L&lt;&lt;693.0,851.0&gt;--&lt;639.0,838.0&gt;&gt;/L&lt;&lt;639.0,838.0&gt;--&lt;726.0,843.0&gt;&gt; = 10.246613690642405

* uni06DE (U+06DE): L&lt;&lt;847.0,169.0&gt;--&lt;886.0,204.0&gt;&gt;/L&lt;&lt;886.0,204.0&gt;--&lt;809.0,137.0&gt;&gt; = 0.8784378818337604

* uni06DE (U+06DE): L&lt;&lt;886.0,204.0&gt;--&lt;809.0,137.0&gt;&gt;/L&lt;&lt;809.0,137.0&gt;--&lt;847.0,169.0&gt;&gt; = 0.9265965130367743

* uni06E6 (U+06E6): B&lt;&lt;378.0,-21.5&gt;-&lt;344.0,-62.0&gt;-&lt;326.0,-66.0&gt;&gt;/L&lt;&lt;326.0,-66.0&gt;--&lt;758.0,-66.0&gt;&gt; = 12.528807709151492

* uni06E7 (U+06E7): B&lt;&lt;595.0,1207.5&gt;-&lt;561.0,1167.0&gt;-&lt;542.0,1163.0&gt;&gt;/L&lt;&lt;542.0,1163.0&gt;--&lt;975.0,1163.0&gt;&gt; = 11.888658039627968

* uni06F4 (U+06F4): B&lt;&lt;749.0,595.5&gt;-&lt;687.0,626.0&gt;-&lt;680.0,678.0&gt;&gt;/B&lt;&lt;680.0,678.0&gt;-&lt;691.0,552.0&gt;-&lt;682.0,397.0&gt;&gt; = 2.677441692171966

* uni06FB.fina: B&lt;&lt;999.5,504.5&gt;-&lt;929.0,415.0&gt;-&lt;817.0,395.0&gt;&gt;/L&lt;&lt;817.0,395.0&gt;--&lt;1295.0,402.0&gt;&gt; = 9.285672095801052

* uni06FC.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni06FD (U+06FD): B&lt;&lt;397.0,480.0&gt;-&lt;459.0,525.0&gt;-&lt;523.0,572.0&gt;&gt;/B&lt;&lt;523.0,572.0&gt;-&lt;498.0,555.0&gt;-&lt;460.5,580.5&gt;&gt; = 2.076927596042315

* uni06FF.init: B&lt;&lt;413.0,401.0&gt;-&lt;457.0,399.0&gt;-&lt;493.0,390.0&gt;&gt;/B&lt;&lt;493.0,390.0&gt;-&lt;405.0,414.0&gt;-&lt;360.5,488.5&gt;&gt; = 1.2188752351313326

* uni06FF.init: B&lt;&lt;967.0,824.5&gt;-&lt;960.0,882.0&gt;-&lt;965.0,924.0&gt;&gt;/B&lt;&lt;965.0,924.0&gt;-&lt;947.0,810.0&gt;-&lt;903.0,703.5&gt;&gt; = 2.18365204045764

* uni06FF.medi: B&lt;&lt;925.0,473.5&gt;-&lt;866.0,410.0&gt;-&lt;786.0,403.0&gt;&gt;/L&lt;&lt;786.0,403.0&gt;--&lt;1303.0,402.0&gt;&gt; = 5.111468017404124

* uni0750 (U+0750): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0750.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0751 (U+0751): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0751 (U+0751): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0751.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0751.fina: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0751.init: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0751.medi: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0752 (U+0752): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0752 (U+0752): B&lt;&lt;454.0,-335.0&gt;-&lt;496.0,-382.0&gt;-&lt;513.0,-427.0&gt;&gt;/B&lt;&lt;513.0,-427.0&gt;-&lt;512.0,-420.0&gt;-&lt;512.0,-414.0&gt;&gt; = 12.565348379907297

* uni0752 (U+0752): B&lt;&lt;579.5,-547.0&gt;-&lt;538.0,-502.0&gt;-&lt;520.0,-457.0&gt;&gt;/B&lt;&lt;520.0,-457.0&gt;-&lt;521.0,-463.0&gt;-&lt;521.0,-469.0&gt;&gt; = 12.33908727832621

* uni0752.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0752.fina: B&lt;&lt;454.0,-335.0&gt;-&lt;496.0,-382.0&gt;-&lt;513.0,-427.0&gt;&gt;/B&lt;&lt;513.0,-427.0&gt;-&lt;512.0,-420.0&gt;-&lt;512.0,-414.0&gt;&gt; = 12.565348379907297

* uni0752.fina: B&lt;&lt;579.5,-547.0&gt;-&lt;538.0,-502.0&gt;-&lt;520.0,-457.0&gt;&gt;/B&lt;&lt;520.0,-457.0&gt;-&lt;521.0,-463.0&gt;-&lt;521.0,-469.0&gt;&gt; = 12.33908727832621

* uni0752.init: B&lt;&lt;454.0,-335.0&gt;-&lt;496.0,-382.0&gt;-&lt;513.0,-427.0&gt;&gt;/B&lt;&lt;513.0,-427.0&gt;-&lt;512.0,-420.0&gt;-&lt;512.0,-414.0&gt;&gt; = 12.565348379907297

* uni0752.init: B&lt;&lt;579.5,-547.0&gt;-&lt;538.0,-502.0&gt;-&lt;520.0,-457.0&gt;&gt;/B&lt;&lt;520.0,-457.0&gt;-&lt;521.0,-463.0&gt;-&lt;521.0,-469.0&gt;&gt; = 12.33908727832621

* uni0752.medi: B&lt;&lt;432.0,-335.0&gt;-&lt;474.0,-382.0&gt;-&lt;491.0,-427.0&gt;&gt;/B&lt;&lt;491.0,-427.0&gt;-&lt;490.0,-420.0&gt;-&lt;490.0,-414.0&gt;&gt; = 12.565348379907297

* uni0752.medi: B&lt;&lt;557.5,-547.0&gt;-&lt;516.0,-502.0&gt;-&lt;498.0,-457.0&gt;&gt;/B&lt;&lt;498.0,-457.0&gt;-&lt;499.0,-463.0&gt;-&lt;499.0,-469.0&gt;&gt; = 12.33908727832621

* uni0753 (U+0753): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0753 (U+0753): B&lt;&lt;454.0,-335.0&gt;-&lt;496.0,-382.0&gt;-&lt;513.0,-427.0&gt;&gt;/B&lt;&lt;513.0,-427.0&gt;-&lt;512.0,-420.0&gt;-&lt;512.0,-414.0&gt;&gt; = 12.565348379907297

* uni0753 (U+0753): B&lt;&lt;579.5,-547.0&gt;-&lt;538.0,-502.0&gt;-&lt;520.0,-457.0&gt;&gt;/B&lt;&lt;520.0,-457.0&gt;-&lt;521.0,-463.0&gt;-&lt;521.0,-469.0&gt;&gt; = 12.33908727832621

* uni0753 (U+0753): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0753.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0753.fina: B&lt;&lt;454.0,-335.0&gt;-&lt;496.0,-382.0&gt;-&lt;513.0,-427.0&gt;&gt;/B&lt;&lt;513.0,-427.0&gt;-&lt;512.0,-420.0&gt;-&lt;512.0,-414.0&gt;&gt; = 12.565348379907297

* uni0753.fina: B&lt;&lt;579.5,-547.0&gt;-&lt;538.0,-502.0&gt;-&lt;520.0,-457.0&gt;&gt;/B&lt;&lt;520.0,-457.0&gt;-&lt;521.0,-463.0&gt;-&lt;521.0,-469.0&gt;&gt; = 12.33908727832621

* uni0753.fina: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0753.init: B&lt;&lt;454.0,-335.0&gt;-&lt;496.0,-382.0&gt;-&lt;513.0,-427.0&gt;&gt;/B&lt;&lt;513.0,-427.0&gt;-&lt;512.0,-420.0&gt;-&lt;512.0,-414.0&gt;&gt; = 12.565348379907297

* uni0753.init: B&lt;&lt;579.5,-547.0&gt;-&lt;538.0,-502.0&gt;-&lt;520.0,-457.0&gt;&gt;/B&lt;&lt;520.0,-457.0&gt;-&lt;521.0,-463.0&gt;-&lt;521.0,-469.0&gt;&gt; = 12.33908727832621

* uni0753.init: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0753.medi: B&lt;&lt;432.0,-335.0&gt;-&lt;474.0,-382.0&gt;-&lt;491.0,-427.0&gt;&gt;/B&lt;&lt;491.0,-427.0&gt;-&lt;490.0,-420.0&gt;-&lt;490.0,-414.0&gt;&gt; = 12.565348379907297

* uni0753.medi: B&lt;&lt;557.5,-547.0&gt;-&lt;516.0,-502.0&gt;-&lt;498.0,-457.0&gt;&gt;/B&lt;&lt;498.0,-457.0&gt;-&lt;499.0,-463.0&gt;-&lt;499.0,-469.0&gt;&gt; = 12.33908727832621

* uni0753.medi: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni0754 (U+0754): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0754 (U+0754): B&lt;&lt;529.5,-61.0&gt;-&lt;571.0,-108.0&gt;-&lt;588.0,-153.0&gt;&gt;/B&lt;&lt;588.0,-153.0&gt;-&lt;587.0,-146.0&gt;-&lt;588.0,-140.0&gt;&gt; = 12.565348379907297

* uni0754.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0754.fina: B&lt;&lt;529.5,-61.0&gt;-&lt;571.0,-108.0&gt;-&lt;588.0,-153.0&gt;&gt;/B&lt;&lt;588.0,-153.0&gt;-&lt;587.0,-146.0&gt;-&lt;588.0,-140.0&gt;&gt; = 12.565348379907297

* uni0754.init: B&lt;&lt;359.5,-61.0&gt;-&lt;401.0,-108.0&gt;-&lt;418.0,-153.0&gt;&gt;/B&lt;&lt;418.0,-153.0&gt;-&lt;417.0,-146.0&gt;-&lt;418.0,-140.0&gt;&gt; = 12.565348379907297

* uni0754.medi: B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uni0755 (U+0755): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0755.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0756 (U+0756): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0756.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni0757 (U+0757): B&lt;&lt;487.5,36.0&gt;-&lt;529.0,-11.0&gt;-&lt;546.0,-56.0&gt;&gt;/B&lt;&lt;546.0,-56.0&gt;-&lt;545.0,-49.0&gt;-&lt;546.0,-43.0&gt;&gt; = 12.565348379907297

* uni0757 (U+0757): B&lt;&lt;613.0,-176.0&gt;-&lt;571.0,-131.0&gt;-&lt;554.0,-86.0&gt;&gt;/B&lt;&lt;554.0,-86.0&gt;-&lt;555.0,-92.0&gt;-&lt;554.0,-98.0&gt;&gt; = 11.233128526037627

* uni0757.fina: B&lt;&lt;487.5,36.0&gt;-&lt;529.0,-11.0&gt;-&lt;546.0,-56.0&gt;&gt;/B&lt;&lt;546.0,-56.0&gt;-&lt;545.0,-49.0&gt;-&lt;546.0,-43.0&gt;&gt; = 12.565348379907297

* uni0757.fina: B&lt;&lt;613.0,-176.0&gt;-&lt;571.0,-131.0&gt;-&lt;554.0,-86.0&gt;&gt;/B&lt;&lt;554.0,-86.0&gt;-&lt;555.0,-92.0&gt;-&lt;554.0,-98.0&gt;&gt; = 11.233128526037627

* uni0757.init: B&lt;&lt;422.0,-335.0&gt;-&lt;464.0,-382.0&gt;-&lt;481.0,-427.0&gt;&gt;/B&lt;&lt;481.0,-427.0&gt;-&lt;480.0,-420.0&gt;-&lt;480.0,-414.0&gt;&gt; = 12.565348379907297

* uni0757.init: B&lt;&lt;547.5,-547.0&gt;-&lt;506.0,-502.0&gt;-&lt;488.0,-457.0&gt;&gt;/B&lt;&lt;488.0,-457.0&gt;-&lt;489.0,-463.0&gt;-&lt;489.0,-469.0&gt;&gt; = 12.33908727832621

* uni0757.medi: B&lt;&lt;422.0,-335.0&gt;-&lt;464.0,-382.0&gt;-&lt;481.0,-427.0&gt;&gt;/B&lt;&lt;481.0,-427.0&gt;-&lt;480.0,-420.0&gt;-&lt;480.0,-414.0&gt;&gt; = 12.565348379907297

* uni0757.medi: B&lt;&lt;547.5,-547.0&gt;-&lt;506.0,-502.0&gt;-&lt;488.0,-457.0&gt;&gt;/B&lt;&lt;488.0,-457.0&gt;-&lt;489.0,-463.0&gt;-&lt;489.0,-469.0&gt;&gt; = 12.33908727832621

* uni0758 (U+0758): B&lt;&lt;706.0,1264.0&gt;-&lt;748.0,1217.0&gt;-&lt;765.0,1172.0&gt;&gt;/B&lt;&lt;765.0,1172.0&gt;-&lt;764.0,1179.0&gt;-&lt;764.0,1185.0&gt;&gt; = 12.565348379907297

* uni0758 (U+0758): B&lt;&lt;831.0,1052.0&gt;-&lt;789.0,1097.0&gt;-&lt;772.0,1142.0&gt;&gt;/B&lt;&lt;772.0,1142.0&gt;-&lt;773.0,1136.0&gt;-&lt;773.0,1130.0&gt;&gt; = 11.233128526037627

* uni0758.fina: B&lt;&lt;706.0,1264.0&gt;-&lt;748.0,1217.0&gt;-&lt;765.0,1172.0&gt;&gt;/B&lt;&lt;765.0,1172.0&gt;-&lt;764.0,1179.0&gt;-&lt;764.0,1185.0&gt;&gt; = 12.565348379907297

* uni0758.fina: B&lt;&lt;831.0,1052.0&gt;-&lt;789.0,1097.0&gt;-&lt;772.0,1142.0&gt;&gt;/B&lt;&lt;772.0,1142.0&gt;-&lt;773.0,1136.0&gt;-&lt;773.0,1130.0&gt;&gt; = 11.233128526037627

* uni0758.init: B&lt;&lt;654.5,1436.0&gt;-&lt;696.0,1389.0&gt;-&lt;713.0,1344.0&gt;&gt;/B&lt;&lt;713.0,1344.0&gt;-&lt;712.0,1351.0&gt;-&lt;713.0,1357.0&gt;&gt; = 12.565348379907297

* uni0758.medi: B&lt;&lt;654.5,1436.0&gt;-&lt;696.0,1389.0&gt;-&lt;713.0,1344.0&gt;&gt;/B&lt;&lt;713.0,1344.0&gt;-&lt;712.0,1351.0&gt;-&lt;713.0,1357.0&gt;&gt; = 12.565348379907297

* uni0759 (U+0759): L&lt;&lt;709.0,1778.0&gt;--&lt;646.0,1428.0&gt;&gt;/B&lt;&lt;646.0,1428.0&gt;-&lt;669.0,1529.0&gt;-&lt;732.0,1582.0&gt;&gt; = 2.624809149723495

* uni0759.fina: L&lt;&lt;649.0,1778.0&gt;--&lt;586.0,1428.0&gt;&gt;/B&lt;&lt;586.0,1428.0&gt;-&lt;609.0,1529.0&gt;-&lt;672.0,1582.0&gt;&gt; = 2.624809149723495

* uni075A (U+075A): L&lt;&lt;709.0,1778.0&gt;--&lt;646.0,1428.0&gt;&gt;/B&lt;&lt;646.0,1428.0&gt;-&lt;669.0,1529.0&gt;-&lt;732.0,1582.0&gt;&gt; = 2.624809149723495

* uni075A.fina: L&lt;&lt;649.0,1778.0&gt;--&lt;586.0,1428.0&gt;&gt;/B&lt;&lt;586.0,1428.0&gt;-&lt;609.0,1529.0&gt;-&lt;672.0,1582.0&gt;&gt; = 2.624809149723495

* uni075D (U+075D): B&lt;&lt;575.0,1592.0&gt;-&lt;617.0,1545.0&gt;-&lt;634.0,1500.0&gt;&gt;/B&lt;&lt;634.0,1500.0&gt;-&lt;633.0,1507.0&gt;-&lt;633.0,1513.0&gt;&gt; = 12.565348379907297

* uni075D (U+075D): B&lt;&lt;700.0,1380.0&gt;-&lt;658.0,1425.0&gt;-&lt;641.0,1470.0&gt;&gt;/B&lt;&lt;641.0,1470.0&gt;-&lt;642.0,1464.0&gt;-&lt;642.0,1458.0&gt;&gt; = 11.233128526037627

* uni075D.fina: B&lt;&lt;681.5,1510.0&gt;-&lt;723.0,1463.0&gt;-&lt;740.0,1418.0&gt;&gt;/B&lt;&lt;740.0,1418.0&gt;-&lt;739.0,1425.0&gt;-&lt;740.0,1431.0&gt;&gt; = 12.565348379907297

* uni075D.fina: B&lt;&lt;807.0,1298.0&gt;-&lt;765.0,1343.0&gt;-&lt;748.0,1388.0&gt;&gt;/B&lt;&lt;748.0,1388.0&gt;-&lt;749.0,1382.0&gt;-&lt;748.0,1376.0&gt;&gt; = 11.233128526037627

* uni075D.init: B&lt;&lt;955.0,1220.0&gt;-&lt;913.0,1265.0&gt;-&lt;896.0,1310.0&gt;&gt;/B&lt;&lt;896.0,1310.0&gt;-&lt;897.0,1304.0&gt;-&lt;896.0,1298.0&gt;&gt; = 11.233128526037627

* uni075D.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni075D.medi: B&lt;&lt;843.0,1271.0&gt;-&lt;801.0,1316.0&gt;-&lt;784.0,1361.0&gt;&gt;/B&lt;&lt;784.0,1361.0&gt;-&lt;785.0,1355.0&gt;-&lt;784.0,1349.0&gt;&gt; = 11.233128526037627

* uni075E (U+075E): B&lt;&lt;732.5,1571.0&gt;-&lt;690.0,1617.0&gt;-&lt;674.0,1663.0&gt;&gt;/B&lt;&lt;674.0,1663.0&gt;-&lt;675.0,1654.0&gt;-&lt;675.0,1646.0&gt;&gt; = 12.83881627990079

* uni075E.fina: B&lt;&lt;845.5,1526.0&gt;-&lt;803.0,1572.0&gt;-&lt;787.0,1618.0&gt;&gt;/B&lt;&lt;787.0,1618.0&gt;-&lt;788.0,1609.0&gt;-&lt;788.0,1601.0&gt;&gt; = 12.83881627990079

* uni075E.init: B&lt;&lt;1002.5,1500.0&gt;-&lt;960.0,1546.0&gt;-&lt;944.0,1592.0&gt;&gt;/B&lt;&lt;944.0,1592.0&gt;-&lt;946.0,1583.0&gt;-&lt;945.0,1575.0&gt;&gt; = 6.650200316659149

* uni075E.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni075E.init: L&lt;&lt;938.0,1615.0&gt;--&lt;938.0,1614.0&gt;&gt;/B&lt;&lt;938.0,1614.0&gt;-&lt;937.0,1623.0&gt;-&lt;937.0,1632.0&gt;&gt; = 6.340191745909908

* uni075E.medi: B&lt;&lt;886.5,1551.0&gt;-&lt;844.0,1597.0&gt;-&lt;828.0,1643.0&gt;&gt;/B&lt;&lt;828.0,1643.0&gt;-&lt;830.0,1634.0&gt;-&lt;829.0,1626.0&gt;&gt; = 6.650200316659149

* uni075E.medi: L&lt;&lt;822.0,1666.0&gt;--&lt;822.0,1665.0&gt;&gt;/B&lt;&lt;822.0,1665.0&gt;-&lt;821.0,1674.0&gt;-&lt;821.0,1683.0&gt;&gt; = 6.340191745909908

* uni075F.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni0760 (U+0760): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni0760 (U+0760): B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uni0760.fina: B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uni0760.init: B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uni0760.medi: B&lt;&lt;447.5,-61.0&gt;-&lt;489.0,-108.0&gt;-&lt;506.0,-153.0&gt;&gt;/B&lt;&lt;506.0,-153.0&gt;-&lt;505.0,-146.0&gt;-&lt;506.0,-140.0&gt;&gt; = 12.565348379907297

* uni0760.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni0761 (U+0761): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni0761 (U+0761): B&lt;&lt;428.0,-335.0&gt;-&lt;470.0,-382.0&gt;-&lt;487.0,-427.0&gt;&gt;/B&lt;&lt;487.0,-427.0&gt;-&lt;486.0,-420.0&gt;-&lt;486.0,-414.0&gt;&gt; = 12.565348379907297

* uni0761 (U+0761): B&lt;&lt;553.5,-547.0&gt;-&lt;512.0,-502.0&gt;-&lt;494.0,-457.0&gt;&gt;/B&lt;&lt;494.0,-457.0&gt;-&lt;495.0,-463.0&gt;-&lt;495.0,-469.0&gt;&gt; = 12.33908727832621

* uni0761.fina: B&lt;&lt;428.0,-335.0&gt;-&lt;470.0,-382.0&gt;-&lt;487.0,-427.0&gt;&gt;/B&lt;&lt;487.0,-427.0&gt;-&lt;486.0,-420.0&gt;-&lt;486.0,-414.0&gt;&gt; = 12.565348379907297

* uni0761.fina: B&lt;&lt;553.5,-547.0&gt;-&lt;512.0,-502.0&gt;-&lt;494.0,-457.0&gt;&gt;/B&lt;&lt;494.0,-457.0&gt;-&lt;495.0,-463.0&gt;-&lt;495.0,-469.0&gt;&gt; = 12.33908727832621

* uni0761.init: B&lt;&lt;428.0,-335.0&gt;-&lt;470.0,-382.0&gt;-&lt;487.0,-427.0&gt;&gt;/B&lt;&lt;487.0,-427.0&gt;-&lt;486.0,-420.0&gt;-&lt;486.0,-414.0&gt;&gt; = 12.565348379907297

* uni0761.init: B&lt;&lt;553.5,-547.0&gt;-&lt;512.0,-502.0&gt;-&lt;494.0,-457.0&gt;&gt;/B&lt;&lt;494.0,-457.0&gt;-&lt;495.0,-463.0&gt;-&lt;495.0,-469.0&gt;&gt; = 12.33908727832621

* uni0761.medi: B&lt;&lt;399.0,-335.0&gt;-&lt;441.0,-382.0&gt;-&lt;458.0,-427.0&gt;&gt;/B&lt;&lt;458.0,-427.0&gt;-&lt;457.0,-420.0&gt;-&lt;457.0,-414.0&gt;&gt; = 12.565348379907297

* uni0761.medi: B&lt;&lt;524.5,-547.0&gt;-&lt;483.0,-502.0&gt;-&lt;465.0,-457.0&gt;&gt;/B&lt;&lt;465.0,-457.0&gt;-&lt;466.0,-463.0&gt;-&lt;466.0,-469.0&gt;&gt; = 12.33908727832621

* uni0761.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni0763 (U+0763): B&lt;&lt;480.0,1508.0&gt;-&lt;522.0,1461.0&gt;-&lt;539.0,1416.0&gt;&gt;/B&lt;&lt;539.0,1416.0&gt;-&lt;538.0,1423.0&gt;-&lt;538.0,1429.0&gt;&gt; = 12.565348379907297

* uni0763 (U+0763): B&lt;&lt;605.5,1296.0&gt;-&lt;564.0,1341.0&gt;-&lt;546.0,1386.0&gt;&gt;/B&lt;&lt;546.0,1386.0&gt;-&lt;547.0,1380.0&gt;-&lt;547.0,1374.0&gt;&gt; = 12.33908727832621

* uni0763.fina: B&lt;&lt;1030.0,799.0&gt;-&lt;988.0,844.0&gt;-&lt;971.0,889.0&gt;&gt;/B&lt;&lt;971.0,889.0&gt;-&lt;972.0,883.0&gt;-&lt;971.0,877.0&gt;&gt; = 11.233128526037627

* uni0763.fina: B&lt;&lt;904.5,1011.0&gt;-&lt;946.0,964.0&gt;-&lt;963.0,919.0&gt;&gt;/B&lt;&lt;963.0,919.0&gt;-&lt;962.0,926.0&gt;-&lt;963.0,932.0&gt;&gt; = 12.565348379907297

* uni0763.fina: L&lt;&lt;824.0,1206.0&gt;--&lt;825.0,1207.0&gt;&gt;/L&lt;&lt;825.0,1207.0&gt;--&lt;645.0,1055.0&gt;&gt; = 4.820766078092687

* uni0763.init: B&lt;&lt;480.0,1508.0&gt;-&lt;522.0,1461.0&gt;-&lt;539.0,1416.0&gt;&gt;/B&lt;&lt;539.0,1416.0&gt;-&lt;538.0,1423.0&gt;-&lt;538.0,1429.0&gt;&gt; = 12.565348379907297

* uni0763.init: B&lt;&lt;605.5,1296.0&gt;-&lt;564.0,1341.0&gt;-&lt;546.0,1386.0&gt;&gt;/B&lt;&lt;546.0,1386.0&gt;-&lt;547.0,1380.0&gt;-&lt;547.0,1374.0&gt;&gt; = 12.33908727832621

* uni0763.medi: B&lt;&lt;865.5,1011.0&gt;-&lt;907.0,964.0&gt;-&lt;924.0,919.0&gt;&gt;/B&lt;&lt;924.0,919.0&gt;-&lt;923.0,926.0&gt;-&lt;924.0,932.0&gt;&gt; = 12.565348379907297

* uni0763.medi: B&lt;&lt;991.0,799.0&gt;-&lt;949.0,844.0&gt;-&lt;932.0,889.0&gt;&gt;/B&lt;&lt;932.0,889.0&gt;-&lt;933.0,883.0&gt;-&lt;932.0,877.0&gt;&gt; = 11.233128526037627

* uni0764 (U+0764): B&lt;&lt;405.0,-335.0&gt;-&lt;447.0,-382.0&gt;-&lt;464.0,-427.0&gt;&gt;/B&lt;&lt;464.0,-427.0&gt;-&lt;463.0,-420.0&gt;-&lt;463.0,-414.0&gt;&gt; = 12.565348379907297

* uni0764 (U+0764): B&lt;&lt;530.5,-547.0&gt;-&lt;489.0,-502.0&gt;-&lt;471.0,-457.0&gt;&gt;/B&lt;&lt;471.0,-457.0&gt;-&lt;472.0,-463.0&gt;-&lt;472.0,-469.0&gt;&gt; = 12.33908727832621

* uni0764.fina: B&lt;&lt;405.0,-335.0&gt;-&lt;447.0,-382.0&gt;-&lt;464.0,-427.0&gt;&gt;/B&lt;&lt;464.0,-427.0&gt;-&lt;463.0,-420.0&gt;-&lt;463.0,-414.0&gt;&gt; = 12.565348379907297

* uni0764.fina: B&lt;&lt;530.5,-547.0&gt;-&lt;489.0,-502.0&gt;-&lt;471.0,-457.0&gt;&gt;/B&lt;&lt;471.0,-457.0&gt;-&lt;472.0,-463.0&gt;-&lt;472.0,-469.0&gt;&gt; = 12.33908727832621

* uni0764.init: B&lt;&lt;405.0,-335.0&gt;-&lt;447.0,-382.0&gt;-&lt;464.0,-427.0&gt;&gt;/B&lt;&lt;464.0,-427.0&gt;-&lt;463.0,-420.0&gt;-&lt;463.0,-414.0&gt;&gt; = 12.565348379907297

* uni0764.init: B&lt;&lt;530.5,-547.0&gt;-&lt;489.0,-502.0&gt;-&lt;471.0,-457.0&gt;&gt;/B&lt;&lt;471.0,-457.0&gt;-&lt;472.0,-463.0&gt;-&lt;472.0,-469.0&gt;&gt; = 12.33908727832621

* uni0764.medi: B&lt;&lt;434.0,-335.0&gt;-&lt;476.0,-382.0&gt;-&lt;493.0,-427.0&gt;&gt;/B&lt;&lt;493.0,-427.0&gt;-&lt;492.0,-420.0&gt;-&lt;492.0,-414.0&gt;&gt; = 12.565348379907297

* uni0764.medi: B&lt;&lt;559.5,-547.0&gt;-&lt;518.0,-502.0&gt;-&lt;500.0,-457.0&gt;&gt;/B&lt;&lt;500.0,-457.0&gt;-&lt;501.0,-463.0&gt;-&lt;501.0,-469.0&gt;&gt; = 12.33908727832621

* uni0767 (U+0767): B&lt;&lt;578.0,-652.0&gt;-&lt;536.0,-607.0&gt;-&lt;519.0,-562.0&gt;&gt;/B&lt;&lt;519.0,-562.0&gt;-&lt;520.0,-568.0&gt;-&lt;519.0,-574.0&gt;&gt; = 11.233128526037627

* uni0767.fina: B&lt;&lt;399.5,-741.0&gt;-&lt;441.0,-788.0&gt;-&lt;458.0,-833.0&gt;&gt;/B&lt;&lt;458.0,-833.0&gt;-&lt;457.0,-826.0&gt;-&lt;458.0,-820.0&gt;&gt; = 12.565348379907297

* uni0767.fina: B&lt;&lt;525.0,-953.0&gt;-&lt;483.0,-908.0&gt;-&lt;466.0,-863.0&gt;&gt;/B&lt;&lt;466.0,-863.0&gt;-&lt;467.0,-869.0&gt;-&lt;466.0,-875.0&gt;&gt; = 11.233128526037627

* uni0767.init: B&lt;&lt;492.5,-61.0&gt;-&lt;534.0,-108.0&gt;-&lt;551.0,-153.0&gt;&gt;/B&lt;&lt;551.0,-153.0&gt;-&lt;550.0,-146.0&gt;-&lt;551.0,-140.0&gt;&gt; = 12.565348379907297

* uni0767.medi: B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uni0768 (U+0768): L&lt;&lt;887.0,1778.0&gt;--&lt;824.0,1428.0&gt;&gt;/B&lt;&lt;824.0,1428.0&gt;-&lt;847.0,1529.0&gt;-&lt;910.0,1582.0&gt;&gt; = 2.624809149723495

* uni0768.fina: L&lt;&lt;848.0,1614.0&gt;--&lt;785.0,1264.0&gt;&gt;/B&lt;&lt;785.0,1264.0&gt;-&lt;808.0,1365.0&gt;-&lt;871.0,1418.0&gt;&gt; = 2.624809149723495

* uni0768.init: L&lt;&lt;795.0,1778.0&gt;--&lt;732.0,1428.0&gt;&gt;/B&lt;&lt;732.0,1428.0&gt;-&lt;755.0,1529.0&gt;-&lt;818.0,1582.0&gt;&gt; = 2.624809149723495

* uni0768.medi: L&lt;&lt;875.0,1710.0&gt;--&lt;812.0,1360.0&gt;&gt;/B&lt;&lt;812.0,1360.0&gt;-&lt;835.0,1461.0&gt;-&lt;898.0,1514.0&gt;&gt; = 2.624809149723495

* uni076C (U+076C): B&lt;&lt;411.0,1048.0&gt;-&lt;466.0,1075.0&gt;-&lt;523.0,1092.0&gt;&gt;/B&lt;&lt;523.0,1092.0&gt;-&lt;474.0,1084.0&gt;-&lt;441.5,1138.5&gt;&gt; = 7.334378801416706

* uni076C.fina: B&lt;&lt;401.0,991.0&gt;-&lt;456.0,1018.0&gt;-&lt;513.0,1035.0&gt;&gt;/B&lt;&lt;513.0,1035.0&gt;-&lt;464.0,1027.0&gt;-&lt;431.5,1081.5&gt;&gt; = 7.334378801416706

* uni076E (U+076E): B&lt;&lt;639.5,-288.0&gt;-&lt;700.0,-267.0&gt;-&lt;739.0,-236.0&gt;&gt;/B&lt;&lt;739.0,-236.0&gt;-&lt;690.0,-258.0&gt;-&lt;631.5,-271.0&gt;&gt; = 14.301091101653821

* uni076E (U+076E): L&lt;&lt;646.0,352.0&gt;--&lt;582.0,2.0&gt;&gt;/B&lt;&lt;582.0,2.0&gt;-&lt;606.0,103.0&gt;-&lt;669.0,156.0&gt;&gt; = 3.0044715978849434

* uni076E.fina: B&lt;&lt;639.5,-288.0&gt;-&lt;700.0,-267.0&gt;-&lt;739.0,-236.0&gt;&gt;/B&lt;&lt;739.0,-236.0&gt;-&lt;690.0,-258.0&gt;-&lt;631.5,-271.0&gt;&gt; = 14.301091101653821

* uni076E.fina: L&lt;&lt;646.0,352.0&gt;--&lt;582.0,2.0&gt;&gt;/B&lt;&lt;582.0,2.0&gt;-&lt;606.0,103.0&gt;-&lt;669.0,156.0&gt;&gt; = 3.0044715978849434

* uni076E.init: L&lt;&lt;490.0,-65.0&gt;--&lt;427.0,-415.0&gt;&gt;/B&lt;&lt;427.0,-415.0&gt;-&lt;450.0,-314.0&gt;-&lt;513.0,-261.0&gt;&gt; = 2.624809149723495

* uni076E.medi: L&lt;&lt;490.0,-65.0&gt;--&lt;427.0,-415.0&gt;&gt;/B&lt;&lt;427.0,-415.0&gt;-&lt;450.0,-314.0&gt;-&lt;513.0,-261.0&gt;&gt; = 2.624809149723495

* uni076F (U+076F): B&lt;&lt;373.0,-514.0&gt;-&lt;428.0,-563.0&gt;-&lt;452.0,-626.0&gt;&gt;/B&lt;&lt;452.0,-626.0&gt;-&lt;451.0,-619.0&gt;-&lt;451.0,-613.0&gt;&gt; = 12.724355685422363

* uni076F (U+076F): B&lt;&lt;406.0,-296.0&gt;-&lt;361.0,-296.0&gt;-&lt;315.0,-278.0&gt;&gt;/B&lt;&lt;315.0,-278.0&gt;-&lt;376.0,-310.0&gt;-&lt;477.0,-308.0&gt;&gt; = 6.310439299142033

* uni076F (U+076F): B&lt;&lt;518.0,-746.0&gt;-&lt;476.0,-701.0&gt;-&lt;459.0,-656.0&gt;&gt;/B&lt;&lt;459.0,-656.0&gt;-&lt;460.0,-662.0&gt;-&lt;460.0,-668.0&gt;&gt; = 11.233128526037627

* uni076F (U+076F): B&lt;&lt;597.0,-298.0&gt;-&lt;647.0,-288.0&gt;-&lt;683.0,-270.0&gt;&gt;/B&lt;&lt;683.0,-270.0&gt;-&lt;601.0,-295.0&gt;-&lt;507.0,-296.0&gt;&gt; = 9.609738125052719

* uni076F (U+076F): L&lt;&lt;647.0,340.0&gt;--&lt;584.0,-10.0&gt;&gt;/B&lt;&lt;584.0,-10.0&gt;-&lt;608.0,91.0&gt;-&lt;671.0,144.0&gt;&gt; = 3.162956974585004

* uni076F.fina: B&lt;&lt;372.0,-514.0&gt;-&lt;428.0,-563.0&gt;-&lt;452.0,-626.0&gt;&gt;/B&lt;&lt;452.0,-626.0&gt;-&lt;451.0,-619.0&gt;-&lt;451.0,-613.0&gt;&gt; = 12.724355685422363

* uni076F.fina: B&lt;&lt;406.0,-296.0&gt;-&lt;365.0,-296.0&gt;-&lt;322.0,-281.0&gt;&gt;/B&lt;&lt;322.0,-281.0&gt;-&lt;382.0,-310.0&gt;-&lt;479.0,-308.0&gt;&gt; = 6.565354118838647

* uni076F.fina: B&lt;&lt;518.0,-746.0&gt;-&lt;476.0,-701.0&gt;-&lt;459.0,-656.0&gt;&gt;/B&lt;&lt;459.0,-656.0&gt;-&lt;460.0,-662.0&gt;-&lt;460.0,-668.0&gt;&gt; = 11.233128526037627

* uni076F.fina: B&lt;&lt;601.5,-297.0&gt;-&lt;652.0,-286.0&gt;-&lt;688.0,-268.0&gt;&gt;/B&lt;&lt;688.0,-268.0&gt;-&lt;604.0,-295.0&gt;-&lt;507.0,-296.0&gt;&gt; = 8.74616226255517

* uni076F.fina: L&lt;&lt;647.0,340.0&gt;--&lt;584.0,-10.0&gt;&gt;/B&lt;&lt;584.0,-10.0&gt;-&lt;608.0,91.0&gt;-&lt;671.0,144.0&gt;&gt; = 3.162956974585004

* uni076F.init: B&lt;&lt;292.5,-753.0&gt;-&lt;334.0,-800.0&gt;-&lt;351.0,-845.0&gt;&gt;/B&lt;&lt;351.0,-845.0&gt;-&lt;350.0,-838.0&gt;-&lt;351.0,-832.0&gt;&gt; = 12.565348379907297

* uni076F.init: L&lt;&lt;494.0,-43.0&gt;--&lt;431.0,-393.0&gt;&gt;/B&lt;&lt;431.0,-393.0&gt;-&lt;454.0,-292.0&gt;-&lt;517.0,-239.0&gt;&gt; = 2.624809149723495

* uni076F.medi: B&lt;&lt;292.5,-753.0&gt;-&lt;334.0,-800.0&gt;-&lt;351.0,-845.0&gt;&gt;/B&lt;&lt;351.0,-845.0&gt;-&lt;350.0,-838.0&gt;-&lt;351.0,-832.0&gt;&gt; = 12.565348379907297

* uni076F.medi: L&lt;&lt;494.0,-43.0&gt;--&lt;431.0,-393.0&gt;&gt;/B&lt;&lt;431.0,-393.0&gt;-&lt;454.0,-292.0&gt;-&lt;517.0,-239.0&gt;&gt; = 2.624809149723495

* uni0771 (U+0771): B&lt;&lt;427.5,511.0&gt;-&lt;469.0,464.0&gt;-&lt;486.0,419.0&gt;&gt;/B&lt;&lt;486.0,419.0&gt;-&lt;485.0,426.0&gt;-&lt;486.0,432.0&gt;&gt; = 12.565348379907297

* uni0771 (U+0771): L&lt;&lt;820.0,1598.0&gt;--&lt;757.0,1248.0&gt;&gt;/B&lt;&lt;757.0,1248.0&gt;-&lt;780.0,1349.0&gt;-&lt;843.5,1402.0&gt;&gt; = 2.624809149723495

* uni0771.fina: B&lt;&lt;417.0,453.0&gt;-&lt;459.0,406.0&gt;-&lt;476.0,361.0&gt;&gt;/B&lt;&lt;476.0,361.0&gt;-&lt;475.0,368.0&gt;-&lt;475.0,374.0&gt;&gt; = 12.565348379907297

* uni0771.fina: B&lt;&lt;542.0,241.0&gt;-&lt;500.0,286.0&gt;-&lt;483.0,331.0&gt;&gt;/B&lt;&lt;483.0,331.0&gt;-&lt;484.0,325.0&gt;-&lt;484.0,319.0&gt;&gt; = 11.233128526037627

* uni0771.fina: L&lt;&lt;810.0,1540.0&gt;--&lt;747.0,1190.0&gt;&gt;/B&lt;&lt;747.0,1190.0&gt;-&lt;770.0,1291.0&gt;-&lt;833.0,1344.0&gt;&gt; = 2.624809149723495

* uni0772 (U+0772): L&lt;&lt;808.0,1596.0&gt;--&lt;745.0,1246.0&gt;&gt;/B&lt;&lt;745.0,1246.0&gt;-&lt;768.0,1347.0&gt;-&lt;831.0,1400.0&gt;&gt; = 2.624809149723495

* uni0772.fina: L&lt;&lt;808.0,1596.0&gt;--&lt;745.0,1246.0&gt;&gt;/B&lt;&lt;745.0,1246.0&gt;-&lt;768.0,1347.0&gt;-&lt;831.0,1400.0&gt;&gt; = 2.624809149723495

* uni0772.init: L&lt;&lt;756.0,1768.0&gt;--&lt;693.0,1418.0&gt;&gt;/B&lt;&lt;693.0,1418.0&gt;-&lt;716.0,1519.0&gt;-&lt;779.5,1572.0&gt;&gt; = 2.624809149723495

* uni0772.medi: L&lt;&lt;756.0,1768.0&gt;--&lt;693.0,1418.0&gt;&gt;/B&lt;&lt;693.0,1418.0&gt;-&lt;716.0,1519.0&gt;-&lt;779.5,1572.0&gt;&gt; = 2.624809149723495

* uni0773.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0774.fina.alt: B&lt;&lt;1034.5,433.5&gt;-&lt;1020.0,401.0&gt;-&lt;990.0,400.0&gt;&gt;/L&lt;&lt;990.0,400.0&gt;--&lt;1164.0,393.0&gt;&gt; = 4.212912757596552

* uni0777 (U+0777): B&lt;&lt;489.5,-279.5&gt;-&lt;526.0,-316.0&gt;-&lt;519.0,-341.0&gt;&gt;/B&lt;&lt;519.0,-341.0&gt;-&lt;530.0,-312.0&gt;-&lt;550.5,-292.0&gt;&gt; = 5.130008224837082

* uni0777.fina: B&lt;&lt;465.0,-514.0&gt;-&lt;486.0,-539.0&gt;-&lt;480.0,-560.0&gt;&gt;/B&lt;&lt;480.0,-560.0&gt;-&lt;491.0,-533.0&gt;-&lt;513.0,-511.0&gt;&gt; = 6.220949921159548

* uni0777.init: B&lt;&lt;552.5,77.5&gt;-&lt;589.0,41.0&gt;-&lt;582.0,16.0&gt;&gt;/B&lt;&lt;582.0,16.0&gt;-&lt;593.0,45.0&gt;-&lt;613.5,65.0&gt;&gt; = 5.130008224837082

* uni0777.medi: B&lt;&lt;583.5,77.5&gt;-&lt;620.0,41.0&gt;-&lt;613.0,16.0&gt;&gt;/B&lt;&lt;613.0,16.0&gt;-&lt;624.0,45.0&gt;-&lt;644.5,65.0&gt;&gt; = 5.130008224837082

* uni077C (U+077C): B&lt;&lt;617.0,257.5&gt;-&lt;653.0,221.0&gt;-&lt;647.0,196.0&gt;&gt;/B&lt;&lt;647.0,196.0&gt;-&lt;658.0,225.0&gt;-&lt;678.5,245.0&gt;&gt; = 7.2765214012499815

* uni077C.fina: B&lt;&lt;588.0,257.5&gt;-&lt;624.0,221.0&gt;-&lt;618.0,196.0&gt;&gt;/B&lt;&lt;618.0,196.0&gt;-&lt;629.0,225.0&gt;-&lt;649.5,245.0&gt;&gt; = 7.2765214012499815

* uni077C.init: B&lt;&lt;571.0,-4.5&gt;-&lt;607.0,-41.0&gt;-&lt;600.0,-66.0&gt;&gt;/B&lt;&lt;600.0,-66.0&gt;-&lt;611.0,-37.0&gt;-&lt;631.5,-17.0&gt;&gt; = 5.130008224837082

* uni077C.medi: B&lt;&lt;571.0,-4.5&gt;-&lt;607.0,-41.0&gt;-&lt;600.0,-66.0&gt;&gt;/B&lt;&lt;600.0,-66.0&gt;-&lt;611.0,-37.0&gt;-&lt;631.5,-17.0&gt;&gt; = 5.130008224837082

* uni077D (U+077D): L&lt;&lt;881.0,1527.0&gt;--&lt;881.0,1528.0&gt;&gt;/B&lt;&lt;881.0,1528.0&gt;-&lt;880.0,1522.0&gt;-&lt;875.0,1512.0&gt;&gt; = 9.462322208025613

* uni077D.fina: L&lt;&lt;788.0,1527.0&gt;--&lt;788.0,1528.0&gt;&gt;/B&lt;&lt;788.0,1528.0&gt;-&lt;787.0,1522.0&gt;-&lt;782.0,1512.0&gt;&gt; = 9.462322208025613

* uni077D.init: L&lt;&lt;1039.0,1527.0&gt;--&lt;1039.0,1528.0&gt;&gt;/B&lt;&lt;1039.0,1528.0&gt;-&lt;1038.0,1522.0&gt;-&lt;1033.0,1512.0&gt;&gt; = 9.462322208025613

* uni077D.medi: L&lt;&lt;926.0,1524.0&gt;--&lt;926.0,1526.0&gt;&gt;/B&lt;&lt;926.0,1526.0&gt;-&lt;925.0,1521.0&gt;-&lt;921.0,1512.0&gt;&gt; = 11.309932474020195

* uni077F (U+077F): B&lt;&lt;688.5,1782.0&gt;-&lt;730.0,1735.0&gt;-&lt;747.0,1690.0&gt;&gt;/B&lt;&lt;747.0,1690.0&gt;-&lt;746.0,1697.0&gt;-&lt;747.0,1703.0&gt;&gt; = 12.565348379907297

* uni077F.fina: B&lt;&lt;688.5,1782.0&gt;-&lt;730.0,1735.0&gt;-&lt;747.0,1690.0&gt;&gt;/B&lt;&lt;747.0,1690.0&gt;-&lt;746.0,1697.0&gt;-&lt;747.0,1703.0&gt;&gt; = 12.565348379907297

* uni077F.init: B&lt;&lt;506.0,1655.0&gt;-&lt;548.0,1608.0&gt;-&lt;565.0,1563.0&gt;&gt;/B&lt;&lt;565.0,1563.0&gt;-&lt;564.0,1570.0&gt;-&lt;564.0,1576.0&gt;&gt; = 12.565348379907297

* uni077F.init: B&lt;&lt;631.0,1443.0&gt;-&lt;589.0,1488.0&gt;-&lt;572.0,1533.0&gt;&gt;/B&lt;&lt;572.0,1533.0&gt;-&lt;573.0,1527.0&gt;-&lt;573.0,1521.0&gt;&gt; = 11.233128526037627

* uni077F.medi: B&lt;&lt;1006.0,919.0&gt;-&lt;964.0,964.0&gt;-&lt;947.0,1009.0&gt;&gt;/B&lt;&lt;947.0,1009.0&gt;-&lt;948.0,1003.0&gt;-&lt;947.0,997.0&gt;&gt; = 11.233128526037627

* uni08A0 (U+08A0): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08A0.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08A1 (U+08A1): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08A1 (U+08A1): B&lt;&lt;632.5,1259.0&gt;-&lt;688.0,1286.0&gt;-&lt;744.0,1303.0&gt;&gt;/B&lt;&lt;744.0,1303.0&gt;-&lt;695.0,1295.0&gt;-&lt;662.5,1349.5&gt;&gt; = 7.614189346743762

* uni08A1.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08A1.fina: B&lt;&lt;632.5,1259.0&gt;-&lt;688.0,1286.0&gt;-&lt;744.0,1303.0&gt;&gt;/B&lt;&lt;744.0,1303.0&gt;-&lt;695.0,1295.0&gt;-&lt;662.5,1349.5&gt;&gt; = 7.614189346743762

* uni08A1.init: B&lt;&lt;460.5,1259.0&gt;-&lt;516.0,1286.0&gt;-&lt;572.0,1303.0&gt;&gt;/B&lt;&lt;572.0,1303.0&gt;-&lt;523.0,1295.0&gt;-&lt;490.5,1349.5&gt;&gt; = 7.614189346743762

* uni08A1.medi: B&lt;&lt;452.5,1259.0&gt;-&lt;508.0,1286.0&gt;-&lt;564.0,1303.0&gt;&gt;/B&lt;&lt;564.0,1303.0&gt;-&lt;515.0,1295.0&gt;-&lt;482.5,1349.5&gt;&gt; = 7.614189346743762

* uni08A2 (U+08A2): B&lt;&lt;685.0,1264.0&gt;-&lt;727.0,1217.0&gt;-&lt;744.0,1172.0&gt;&gt;/B&lt;&lt;744.0,1172.0&gt;-&lt;743.0,1179.0&gt;-&lt;743.0,1185.0&gt;&gt; = 12.565348379907297

* uni08A2 (U+08A2): B&lt;&lt;810.0,1052.0&gt;-&lt;768.0,1097.0&gt;-&lt;751.0,1142.0&gt;&gt;/B&lt;&lt;751.0,1142.0&gt;-&lt;752.0,1136.0&gt;-&lt;752.0,1130.0&gt;&gt; = 11.233128526037627

* uni08A2.fina: B&lt;&lt;685.0,1264.0&gt;-&lt;727.0,1217.0&gt;-&lt;744.0,1172.0&gt;&gt;/B&lt;&lt;744.0,1172.0&gt;-&lt;743.0,1179.0&gt;-&lt;743.0,1185.0&gt;&gt; = 12.565348379907297

* uni08A2.fina: B&lt;&lt;810.0,1052.0&gt;-&lt;768.0,1097.0&gt;-&lt;751.0,1142.0&gt;&gt;/B&lt;&lt;751.0,1142.0&gt;-&lt;752.0,1136.0&gt;-&lt;752.0,1130.0&gt;&gt; = 11.233128526037627

* uni08A2.init: B&lt;&lt;711.5,1436.0&gt;-&lt;753.0,1389.0&gt;-&lt;770.0,1344.0&gt;&gt;/B&lt;&lt;770.0,1344.0&gt;-&lt;769.0,1351.0&gt;-&lt;770.0,1357.0&gt;&gt; = 12.565348379907297

* uni08A2.medi: B&lt;&lt;711.5,1436.0&gt;-&lt;753.0,1389.0&gt;-&lt;770.0,1344.0&gt;&gt;/B&lt;&lt;770.0,1344.0&gt;-&lt;769.0,1351.0&gt;-&lt;770.0,1357.0&gt;&gt; = 12.565348379907297

* uni08A3 (U+08A3): B&lt;&lt;702.0,1241.5&gt;-&lt;678.0,1283.0&gt;-&lt;680.0,1314.0&gt;&gt;/L&lt;&lt;680.0,1314.0&gt;--&lt;555.0,602.0&gt;&gt; = 6.266088693473364

* uni08A3 (U+08A3): B&lt;&lt;951.5,1436.0&gt;-&lt;993.0,1389.0&gt;-&lt;1010.0,1344.0&gt;&gt;/B&lt;&lt;1010.0,1344.0&gt;-&lt;1009.0,1351.0&gt;-&lt;1010.0,1357.0&gt;&gt; = 12.565348379907297

* uni08A3 (U+08A3): L&lt;&lt;680.0,1314.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.213983528662467

* uni08A3 (U+08A3): L&lt;&lt;714.0,1503.0&gt;--&lt;680.0,1314.0&gt;&gt;/B&lt;&lt;680.0,1314.0&gt;-&lt;688.0,1344.0&gt;-&lt;725.0,1383.5&gt;&gt; = 4.733316332514113

* uni08A3.fina: B&lt;&lt;702.0,1241.5&gt;-&lt;678.0,1283.0&gt;-&lt;680.0,1314.0&gt;&gt;/L&lt;&lt;680.0,1314.0&gt;--&lt;555.0,602.0&gt;&gt; = 6.266088693473364

* uni08A3.fina: B&lt;&lt;951.5,1436.0&gt;-&lt;993.0,1389.0&gt;-&lt;1010.0,1344.0&gt;&gt;/B&lt;&lt;1010.0,1344.0&gt;-&lt;1009.0,1351.0&gt;-&lt;1010.0,1357.0&gt;&gt; = 12.565348379907297

* uni08A3.fina: L&lt;&lt;680.0,1314.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.213983528662467

* uni08A3.fina: L&lt;&lt;714.0,1503.0&gt;--&lt;680.0,1314.0&gt;&gt;/B&lt;&lt;680.0,1314.0&gt;-&lt;688.0,1344.0&gt;-&lt;725.0,1383.5&gt;&gt; = 4.733316332514113

* uni08A3.init: B&lt;&lt;951.5,1436.0&gt;-&lt;993.0,1389.0&gt;-&lt;1010.0,1344.0&gt;&gt;/B&lt;&lt;1010.0,1344.0&gt;-&lt;1009.0,1351.0&gt;-&lt;1010.0,1357.0&gt;&gt; = 12.565348379907297

* uni08A3.init: L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uni08A3.medi: B&lt;&lt;951.5,1436.0&gt;-&lt;993.0,1389.0&gt;-&lt;1010.0,1344.0&gt;&gt;/B&lt;&lt;1010.0,1344.0&gt;-&lt;1009.0,1351.0&gt;-&lt;1010.0,1357.0&gt;&gt; = 12.565348379907297

* uni08A3.medi: L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uni08A4 (U+08A4): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni08A4 (U+08A4): B&lt;&lt;851.0,1508.0&gt;-&lt;893.0,1461.0&gt;-&lt;910.0,1416.0&gt;&gt;/B&lt;&lt;910.0,1416.0&gt;-&lt;909.0,1423.0&gt;-&lt;909.0,1429.0&gt;&gt; = 12.565348379907297

* uni08A4 (U+08A4): B&lt;&lt;976.5,1296.0&gt;-&lt;935.0,1341.0&gt;-&lt;917.0,1386.0&gt;&gt;/B&lt;&lt;917.0,1386.0&gt;-&lt;918.0,1380.0&gt;-&lt;918.0,1374.0&gt;&gt; = 12.33908727832621

* uni08A4.fina: B&lt;&lt;818.5,1453.0&gt;-&lt;860.0,1406.0&gt;-&lt;877.0,1361.0&gt;&gt;/B&lt;&lt;877.0,1361.0&gt;-&lt;876.0,1368.0&gt;-&lt;877.0,1374.0&gt;&gt; = 12.565348379907297

* uni08A4.init: B&lt;&lt;851.0,1508.0&gt;-&lt;893.0,1461.0&gt;-&lt;910.0,1416.0&gt;&gt;/B&lt;&lt;910.0,1416.0&gt;-&lt;909.0,1423.0&gt;-&lt;909.0,1429.0&gt;&gt; = 12.565348379907297

* uni08A4.init: B&lt;&lt;976.5,1296.0&gt;-&lt;935.0,1341.0&gt;-&lt;917.0,1386.0&gt;&gt;/B&lt;&lt;917.0,1386.0&gt;-&lt;918.0,1380.0&gt;-&lt;918.0,1374.0&gt;&gt; = 12.33908727832621

* uni08A4.medi: B&lt;&lt;721.0,1492.0&gt;-&lt;763.0,1445.0&gt;-&lt;780.0,1400.0&gt;&gt;/B&lt;&lt;780.0,1400.0&gt;-&lt;779.0,1407.0&gt;-&lt;780.0,1413.0&gt;&gt; = 12.565348379907297

* uni08A4.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni08A5 (U+08A5): B&lt;&lt;1076.0,1386.0&gt;-&lt;1034.0,1431.0&gt;-&lt;1017.0,1476.0&gt;&gt;/B&lt;&lt;1017.0,1476.0&gt;-&lt;1018.0,1470.0&gt;-&lt;1018.0,1464.0&gt;&gt; = 11.233128526037627

* uni08A5 (U+08A5): B&lt;&lt;951.0,1598.0&gt;-&lt;993.0,1551.0&gt;-&lt;1010.0,1506.0&gt;&gt;/B&lt;&lt;1010.0,1506.0&gt;-&lt;1009.0,1513.0&gt;-&lt;1009.0,1519.0&gt;&gt; = 12.565348379907297

* uni08A5.fina: B&lt;&lt;899.5,1305.0&gt;-&lt;941.0,1258.0&gt;-&lt;958.0,1213.0&gt;&gt;/B&lt;&lt;958.0,1213.0&gt;-&lt;957.0,1220.0&gt;-&lt;958.0,1226.0&gt;&gt; = 12.565348379907297

* uni08A5.init: B&lt;&lt;1066.0,1329.0&gt;-&lt;1024.0,1374.0&gt;-&lt;1007.0,1419.0&gt;&gt;/B&lt;&lt;1007.0,1419.0&gt;-&lt;1008.0,1413.0&gt;-&lt;1008.0,1407.0&gt;&gt; = 11.233128526037627

* uni08A5.init: B&lt;&lt;941.0,1541.0&gt;-&lt;983.0,1494.0&gt;-&lt;1000.0,1449.0&gt;&gt;/B&lt;&lt;1000.0,1449.0&gt;-&lt;999.0,1456.0&gt;-&lt;999.0,1462.0&gt;&gt; = 12.565348379907297

* uni08A5.medi: B&lt;&lt;721.0,1492.0&gt;-&lt;763.0,1445.0&gt;-&lt;780.0,1400.0&gt;&gt;/B&lt;&lt;780.0,1400.0&gt;-&lt;779.0,1407.0&gt;-&lt;780.0,1413.0&gt;&gt; = 12.565348379907297

* uni08A5.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni08A7 (U+08A7): B&lt;&lt;1032.0,995.0&gt;-&lt;990.0,1040.0&gt;-&lt;973.0,1085.0&gt;&gt;/B&lt;&lt;973.0,1085.0&gt;-&lt;974.0,1079.0&gt;-&lt;974.0,1073.0&gt;&gt; = 11.233128526037627

* uni08A7 (U+08A7): B&lt;&lt;907.0,1207.0&gt;-&lt;949.0,1160.0&gt;-&lt;966.0,1115.0&gt;&gt;/B&lt;&lt;966.0,1115.0&gt;-&lt;965.0,1122.0&gt;-&lt;965.0,1128.0&gt;&gt; = 12.565348379907297

* uni08A7.fina: B&lt;&lt;701.0,1224.0&gt;-&lt;743.0,1177.0&gt;-&lt;760.0,1132.0&gt;&gt;/B&lt;&lt;760.0,1132.0&gt;-&lt;759.0,1139.0&gt;-&lt;759.0,1145.0&gt;&gt; = 12.565348379907297

* uni08A7.fina: B&lt;&lt;826.0,1012.0&gt;-&lt;784.0,1057.0&gt;-&lt;767.0,1102.0&gt;&gt;/B&lt;&lt;767.0,1102.0&gt;-&lt;768.0,1096.0&gt;-&lt;768.0,1090.0&gt;&gt; = 11.233128526037627

* uni08A7.init: B&lt;&lt;882.5,1209.0&gt;-&lt;924.0,1162.0&gt;-&lt;941.0,1117.0&gt;&gt;/B&lt;&lt;941.0,1117.0&gt;-&lt;940.0,1124.0&gt;-&lt;941.0,1130.0&gt;&gt; = 12.565348379907297

* uni08A7.medi: B&lt;&lt;674.0,1224.0&gt;-&lt;716.0,1177.0&gt;-&lt;733.0,1132.0&gt;&gt;/B&lt;&lt;733.0,1132.0&gt;-&lt;732.0,1139.0&gt;-&lt;732.0,1145.0&gt;&gt; = 12.565348379907297

* uni08A7.medi: B&lt;&lt;799.0,1012.0&gt;-&lt;757.0,1057.0&gt;-&lt;740.0,1102.0&gt;&gt;/B&lt;&lt;740.0,1102.0&gt;-&lt;741.0,1096.0&gt;-&lt;741.0,1090.0&gt;&gt; = 11.233128526037627

* uni08A8 (U+08A8): B&lt;&lt;473.0,-629.0&gt;-&lt;431.0,-584.0&gt;-&lt;414.0,-539.0&gt;&gt;/B&lt;&lt;414.0,-539.0&gt;-&lt;415.0,-545.0&gt;-&lt;414.0,-551.0&gt;&gt; = 11.233128526037627

* uni08A8 (U+08A8): B&lt;&lt;867.0,1394.0&gt;-&lt;922.0,1421.0&gt;-&lt;979.0,1438.0&gt;&gt;/B&lt;&lt;979.0,1438.0&gt;-&lt;930.0,1430.0&gt;-&lt;897.5,1484.5&gt;&gt; = 7.334378801416706

* uni08A8.fina: B&lt;&lt;288.5,-753.0&gt;-&lt;330.0,-800.0&gt;-&lt;347.0,-845.0&gt;&gt;/B&lt;&lt;347.0,-845.0&gt;-&lt;346.0,-838.0&gt;-&lt;347.0,-832.0&gt;&gt; = 12.565348379907297

* uni08A8.fina: B&lt;&lt;769.0,837.0&gt;-&lt;824.0,864.0&gt;-&lt;881.0,881.0&gt;&gt;/B&lt;&lt;881.0,881.0&gt;-&lt;832.0,873.0&gt;-&lt;799.5,927.5&gt;&gt; = 7.334378801416706

* uni08A8.init: B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uni08A8.init: B&lt;&lt;843.5,1259.0&gt;-&lt;899.0,1286.0&gt;-&lt;955.0,1303.0&gt;&gt;/B&lt;&lt;955.0,1303.0&gt;-&lt;906.0,1295.0&gt;-&lt;873.5,1349.5&gt;&gt; = 7.614189346743762

* uni08A8.medi: B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uni08A8.medi: B&lt;&lt;843.0,1257.0&gt;-&lt;898.0,1284.0&gt;-&lt;955.0,1301.0&gt;&gt;/B&lt;&lt;955.0,1301.0&gt;-&lt;906.0,1293.0&gt;-&lt;873.5,1347.5&gt;&gt; = 7.334378801416706

* uni08A9 (U+08A9): B&lt;&lt;473.0,-629.0&gt;-&lt;431.0,-584.0&gt;-&lt;414.0,-539.0&gt;&gt;/B&lt;&lt;414.0,-539.0&gt;-&lt;415.0,-545.0&gt;-&lt;414.0,-551.0&gt;&gt; = 11.233128526037627

* uni08A9.fina: B&lt;&lt;288.5,-753.0&gt;-&lt;330.0,-800.0&gt;-&lt;347.0,-845.0&gt;&gt;/B&lt;&lt;347.0,-845.0&gt;-&lt;346.0,-838.0&gt;-&lt;347.0,-832.0&gt;&gt; = 12.565348379907297

* uni08A9.init: B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uni08A9.medi: B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uni08AC (U+08AC): B&lt;&lt;397.0,403.0&gt;-&lt;434.0,405.0&gt;-&lt;454.0,391.0&gt;&gt;/B&lt;&lt;454.0,391.0&gt;-&lt;409.0,438.0&gt;-&lt;385.0,512.0&gt;&gt; = 11.253344068209653

* uni08AC (U+08AC): B&lt;&lt;443.5,-61.0&gt;-&lt;485.0,-108.0&gt;-&lt;502.0,-153.0&gt;&gt;/B&lt;&lt;502.0,-153.0&gt;-&lt;501.0,-146.0&gt;-&lt;502.0,-140.0&gt;&gt; = 12.565348379907297

* uni08AC.comp: B&lt;&lt;397.0,403.0&gt;-&lt;434.0,405.0&gt;-&lt;454.0,391.0&gt;&gt;/B&lt;&lt;454.0,391.0&gt;-&lt;409.0,438.0&gt;-&lt;385.0,512.0&gt;&gt; = 11.253344068209653

* uni08AC.fina: B&lt;&lt;397.0,403.0&gt;-&lt;434.0,405.0&gt;-&lt;454.0,391.0&gt;&gt;/B&lt;&lt;454.0,391.0&gt;-&lt;409.0,438.0&gt;-&lt;385.0,512.0&gt;&gt; = 11.253344068209653

* uni08AC.fina: B&lt;&lt;443.5,-61.0&gt;-&lt;485.0,-108.0&gt;-&lt;502.0,-153.0&gt;&gt;/B&lt;&lt;502.0,-153.0&gt;-&lt;501.0,-146.0&gt;-&lt;502.0,-140.0&gt;&gt; = 12.565348379907297

* uni08AE (U+08AE): B&lt;&lt;564.5,-346.0&gt;-&lt;522.0,-300.0&gt;-&lt;506.0,-254.0&gt;&gt;/B&lt;&lt;506.0,-254.0&gt;-&lt;507.0,-263.0&gt;-&lt;507.0,-271.0&gt;&gt; = 12.83881627990079

* uni08AE.fina: B&lt;&lt;564.5,-346.0&gt;-&lt;522.0,-300.0&gt;-&lt;506.0,-254.0&gt;&gt;/B&lt;&lt;506.0,-254.0&gt;-&lt;507.0,-263.0&gt;-&lt;507.0,-271.0&gt;&gt; = 12.83881627990079

* uni08AF.fina: B&lt;&lt;999.5,504.5&gt;-&lt;929.0,415.0&gt;-&lt;817.0,395.0&gt;&gt;/L&lt;&lt;817.0,395.0&gt;--&lt;1295.0,402.0&gt;&gt; = 9.285672095801052

* uni08B3 (U+08B3): B&lt;&lt;767.5,109.0&gt;-&lt;725.0,155.0&gt;-&lt;709.0,201.0&gt;&gt;/B&lt;&lt;709.0,201.0&gt;-&lt;710.0,192.0&gt;-&lt;710.0,184.0&gt;&gt; = 12.83881627990079

* uni08B3 (U+08B3): L&lt;&lt;703.0,224.0&gt;--&lt;703.0,223.0&gt;&gt;/B&lt;&lt;703.0,223.0&gt;-&lt;701.0,232.0&gt;-&lt;702.0,241.0&gt;&gt; = 12.528807709151492

* uni08B3.init: B&lt;&lt;711.5,-210.0&gt;-&lt;669.0,-164.0&gt;-&lt;653.0,-118.0&gt;&gt;/B&lt;&lt;653.0,-118.0&gt;-&lt;654.0,-127.0&gt;-&lt;654.0,-135.0&gt;&gt; = 12.83881627990079

* uni08B3.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni08B3.medi: B&lt;&lt;609.5,-210.0&gt;-&lt;567.0,-164.0&gt;-&lt;551.0,-118.0&gt;&gt;/B&lt;&lt;551.0,-118.0&gt;-&lt;552.0,-127.0&gt;-&lt;552.0,-135.0&gt;&gt; = 12.83881627990079

* uni08B6 (U+08B6): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08B6.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08B7 (U+08B7): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08B7 (U+08B7): B&lt;&lt;626.5,-272.0&gt;-&lt;584.0,-226.0&gt;-&lt;568.0,-180.0&gt;&gt;/B&lt;&lt;568.0,-180.0&gt;-&lt;569.0,-189.0&gt;-&lt;569.0,-197.0&gt;&gt; = 12.83881627990079

* uni08B7.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08B7.fina: B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uni08B7.fina: L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uni08B7.init: B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uni08B7.init: L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uni08B7.medi: B&lt;&lt;611.5,-208.0&gt;-&lt;569.0,-162.0&gt;-&lt;553.0,-116.0&gt;&gt;/B&lt;&lt;553.0,-116.0&gt;-&lt;555.0,-125.0&gt;-&lt;554.0,-133.0&gt;&gt; = 6.650200316659149

* uni08B7.medi: L&lt;&lt;547.0,-93.0&gt;--&lt;547.0,-94.0&gt;&gt;/B&lt;&lt;547.0,-94.0&gt;-&lt;546.0,-85.0&gt;-&lt;546.0,-76.0&gt;&gt; = 6.340191745909908

* uni08B8 (U+08B8): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08B8 (U+08B8): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08B8.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08B8.fina: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08B8.init: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08B8.medi: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08BA (U+08BA): B&lt;&lt;473.0,-629.0&gt;-&lt;431.0,-584.0&gt;-&lt;414.0,-539.0&gt;&gt;/B&lt;&lt;414.0,-539.0&gt;-&lt;415.0,-545.0&gt;-&lt;414.0,-551.0&gt;&gt; = 11.233128526037627

* uni08BA.fina: B&lt;&lt;288.5,-753.0&gt;-&lt;330.0,-800.0&gt;-&lt;347.0,-845.0&gt;&gt;/B&lt;&lt;347.0,-845.0&gt;-&lt;346.0,-838.0&gt;-&lt;347.0,-832.0&gt;&gt; = 12.565348379907297

* uni08BA.init: B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uni08BA.medi: B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uni08BB (U+08BB): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;941.0,402.0&gt;&gt; = 3.4542029830680403

* uni08BB.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni08BC.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni08BE (U+08BE): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08BE (U+08BE): B&lt;&lt;626.5,-272.0&gt;-&lt;584.0,-226.0&gt;-&lt;568.0,-180.0&gt;&gt;/B&lt;&lt;568.0,-180.0&gt;-&lt;569.0,-189.0&gt;-&lt;569.0,-197.0&gt;&gt; = 12.83881627990079

* uni08BE.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08BE.fina: B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uni08BE.fina: L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uni08BE.init: B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uni08BE.init: L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uni08BE.medi: B&lt;&lt;611.5,-208.0&gt;-&lt;569.0,-162.0&gt;-&lt;553.0,-116.0&gt;&gt;/B&lt;&lt;553.0,-116.0&gt;-&lt;555.0,-125.0&gt;-&lt;554.0,-133.0&gt;&gt; = 6.650200316659149

* uni08BE.medi: L&lt;&lt;547.0,-93.0&gt;--&lt;547.0,-94.0&gt;&gt;/B&lt;&lt;547.0,-94.0&gt;-&lt;546.0,-85.0&gt;-&lt;546.0,-76.0&gt;&gt; = 6.340191745909908

* uni08BF (U+08BF): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08BF (U+08BF): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08BF.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08BF.fina: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08BF.init: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08BF.medi: B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uni08C0 (U+08C0): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08C0 (U+08C0): L&lt;&lt;801.0,1491.0&gt;--&lt;738.0,1141.0&gt;&gt;/B&lt;&lt;738.0,1141.0&gt;-&lt;762.0,1242.0&gt;-&lt;825.0,1295.0&gt;&gt; = 3.162956974585004

* uni08C0.fina: B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uni08C0.fina: L&lt;&lt;801.0,1491.0&gt;--&lt;738.0,1141.0&gt;&gt;/B&lt;&lt;738.0,1141.0&gt;-&lt;762.0,1242.0&gt;-&lt;825.0,1295.0&gt;&gt; = 3.162956974585004

* uni08C0.init: L&lt;&lt;801.0,1491.0&gt;--&lt;738.0,1141.0&gt;&gt;/B&lt;&lt;738.0,1141.0&gt;-&lt;762.0,1242.0&gt;-&lt;825.0,1295.0&gt;&gt; = 3.162956974585004

* uni08C0.medi: L&lt;&lt;801.0,1491.0&gt;--&lt;738.0,1141.0&gt;&gt;/B&lt;&lt;738.0,1141.0&gt;-&lt;762.0,1242.0&gt;-&lt;825.0,1295.0&gt;&gt; = 3.162956974585004

* uni08C1 (U+08C1): B&lt;&lt;563.0,396.5&gt;-&lt;476.0,335.0&gt;-&lt;400.0,262.0&gt;&gt;/B&lt;&lt;400.0,262.0&gt;-&lt;438.0,288.0&gt;-&lt;461.0,290.0&gt;&gt; = 9.466204825049774

* uni08C1 (U+08C1): B&lt;&lt;661.5,29.0&gt;-&lt;619.0,75.0&gt;-&lt;603.0,121.0&gt;&gt;/B&lt;&lt;603.0,121.0&gt;-&lt;604.0,112.0&gt;-&lt;604.0,104.0&gt;&gt; = 12.83881627990079

* uni08C1.fina: B&lt;&lt;488.5,221.0&gt;-&lt;529.0,175.0&gt;-&lt;546.0,129.0&gt;&gt;/B&lt;&lt;546.0,129.0&gt;-&lt;544.0,138.0&gt;-&lt;544.0,147.0&gt;&gt; = 7.753751379765042

* uni08C1.fina: B&lt;&lt;610.5,15.0&gt;-&lt;568.0,61.0&gt;-&lt;551.0,107.0&gt;&gt;/B&lt;&lt;551.0,107.0&gt;-&lt;553.0,98.0&gt;-&lt;552.0,90.0&gt;&gt; = 7.753751379765042

* uni08C1.init: B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uni08C1.medi: B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uni08C2.medi: L&lt;&lt;462.0,1208.0&gt;--&lt;723.0,1429.0&gt;&gt;/L&lt;&lt;723.0,1429.0&gt;--&lt;617.0,1368.0&gt;&gt; = 10.33682536840194

* uni08C3 (U+08C3): B&lt;&lt;594.0,1787.0&gt;-&lt;595.0,1787.0&gt;-&lt;596.0,1786.0&gt;&gt;/B&lt;&lt;596.0,1786.0&gt;-&lt;574.0,1818.0&gt;-&lt;575.0,1844.0&gt;&gt; = 10.491477012331565

* uni08C3.fina: B&lt;&lt;709.0,1711.0&gt;-&lt;711.0,1711.0&gt;-&lt;712.0,1710.0&gt;&gt;/B&lt;&lt;712.0,1710.0&gt;-&lt;690.0,1742.0&gt;-&lt;690.0,1768.0&gt;&gt; = 10.491477012331565

* uni08C3.fina: B&lt;&lt;774.0,1560.0&gt;-&lt;790.0,1556.0&gt;-&lt;809.0,1542.0&gt;&gt;/B&lt;&lt;809.0,1542.0&gt;-&lt;794.0,1554.0&gt;-&lt;783.0,1571.0&gt;&gt; = 2.275456438254266

* uni08C3.fina: B&lt;&lt;849.0,1520.0&gt;-&lt;834.0,1523.0&gt;-&lt;818.0,1534.0&gt;&gt;/B&lt;&lt;818.0,1534.0&gt;-&lt;854.0,1504.0&gt;-&lt;883.0,1456.5&gt;&gt; = 5.297048104596702

* uni08C3.init: L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uni08C3.medi: B&lt;&lt;748.0,1677.0&gt;-&lt;750.0,1677.0&gt;-&lt;751.0,1676.0&gt;&gt;/B&lt;&lt;751.0,1676.0&gt;-&lt;729.0,1708.0&gt;-&lt;729.0,1734.0&gt;&gt; = 10.491477012331565

* uni08C3.medi: B&lt;&lt;815.0,1529.0&gt;-&lt;828.0,1524.0&gt;-&lt;841.0,1514.0&gt;&gt;/B&lt;&lt;841.0,1514.0&gt;-&lt;831.0,1524.0&gt;-&lt;822.0,1537.0&gt;&gt; = 7.431407971172489

* uni08C3.medi: B&lt;&lt;888.0,1486.0&gt;-&lt;874.0,1489.0&gt;-&lt;860.0,1498.0&gt;&gt;/B&lt;&lt;860.0,1498.0&gt;-&lt;894.0,1467.0&gt;-&lt;920.0,1422.5&gt;&gt; = 9.62222843382764

* uni08C4 (U+08C4): B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni08C4 (U+08C4): B&lt;&lt;803.5,1146.0&gt;-&lt;773.0,1183.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.263236657534897

* uni08C4.fina: B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni08C4.fina: B&lt;&lt;818.0,1130.0&gt;-&lt;776.0,1175.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.233128526037627

* uni08C4.init: B&lt;&lt;874.0,1773.0&gt;-&lt;876.0,1773.0&gt;-&lt;877.0,1772.0&gt;&gt;/B&lt;&lt;877.0,1772.0&gt;-&lt;855.0,1804.0&gt;-&lt;855.0,1830.0&gt;&gt; = 10.491477012331565

* uni08C4.medi: B&lt;&lt;750.0,1689.0&gt;-&lt;752.0,1689.0&gt;-&lt;753.0,1688.0&gt;&gt;/B&lt;&lt;753.0,1688.0&gt;-&lt;731.0,1720.0&gt;-&lt;731.0,1746.0&gt;&gt; = 10.491477012331565

* uni08C4.medi: B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uni08C5 (U+08C5): B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni08C5 (U+08C5): B&lt;&lt;818.0,1130.0&gt;-&lt;776.0,1175.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.233128526037627

* uni08C5.fina: B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni08C5.fina: B&lt;&lt;818.0,1130.0&gt;-&lt;776.0,1175.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.233128526037627

* uni08C5.init: B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni08C5.init: B&lt;&lt;818.0,1130.0&gt;-&lt;776.0,1175.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.233128526037627

* uni08C5.medi: B&lt;&lt;692.5,1342.0&gt;-&lt;734.0,1295.0&gt;-&lt;752.0,1250.0&gt;&gt;/B&lt;&lt;752.0,1250.0&gt;-&lt;751.0,1257.0&gt;-&lt;751.0,1263.0&gt;&gt; = 13.67130713219584

* uni08C5.medi: B&lt;&lt;818.0,1130.0&gt;-&lt;776.0,1175.0&gt;-&lt;759.0,1220.0&gt;&gt;/B&lt;&lt;759.0,1220.0&gt;-&lt;760.0,1214.0&gt;-&lt;760.0,1208.0&gt;&gt; = 11.233128526037627

* uni08C6.fina: B&lt;&lt;537.0,105.0&gt;-&lt;549.0,102.0&gt;-&lt;563.0,92.0&gt;&gt;/B&lt;&lt;563.0,92.0&gt;-&lt;527.0,121.0&gt;-&lt;499.0,167.0&gt;&gt; = 3.3156965483788476

* uni08C6.fina: B&lt;&lt;612.0,65.0&gt;-&lt;594.0,69.0&gt;-&lt;573.0,85.0&gt;&gt;/B&lt;&lt;573.0,85.0&gt;-&lt;589.0,71.0&gt;-&lt;602.0,52.0&gt;&gt; = 3.881976887726235

* uni08C7 (U+08C7): L&lt;&lt;725.0,1614.0&gt;--&lt;662.0,1264.0&gt;&gt;/B&lt;&lt;662.0,1264.0&gt;-&lt;685.0,1365.0&gt;-&lt;748.0,1418.0&gt;&gt; = 2.624809149723495

* uni08C7.fina: L&lt;&lt;725.0,1614.0&gt;--&lt;662.0,1264.0&gt;&gt;/B&lt;&lt;662.0,1264.0&gt;-&lt;685.0,1365.0&gt;-&lt;748.0,1418.0&gt;&gt; = 2.624809149723495

* uni08C7.init: L&lt;&lt;741.0,1614.0&gt;--&lt;678.0,1264.0&gt;&gt;/B&lt;&lt;678.0,1264.0&gt;-&lt;701.0,1365.0&gt;-&lt;764.0,1418.0&gt;&gt; = 2.624809149723495

* uni08C7.medi: L&lt;&lt;859.0,1819.0&gt;--&lt;796.0,1469.0&gt;&gt;/B&lt;&lt;796.0,1469.0&gt;-&lt;819.0,1570.0&gt;-&lt;882.5,1623.0&gt;&gt; = 2.624809149723495

* uni08CC (U+08CC): B&lt;&lt;719.0,1483.5&gt;-&lt;726.0,1460.0&gt;-&lt;722.0,1450.0&gt;&gt;/B&lt;&lt;722.0,1450.0&gt;-&lt;776.0,1560.0&gt;-&lt;877.0,1636.0&gt;&gt; = 4.345431749229051

* uni08D6 (U+08D6): B&lt;&lt;429.0,969.0&gt;-&lt;453.0,1096.0&gt;-&lt;585.0,1201.0&gt;&gt;/B&lt;&lt;585.0,1201.0&gt;-&lt;552.0,1179.0&gt;-&lt;518.0,1223.5&gt;&gt; = 4.810586194365587

* uni08DC (U+08DC): B&lt;&lt;1056.0,1425.5&gt;-&lt;1077.0,1398.0&gt;-&lt;1078.0,1375.0&gt;&gt;/L&lt;&lt;1078.0,1375.0&gt;--&lt;1088.0,1431.0&gt;&gt; = 12.614224577396955

* uni08DC (U+08DC): B&lt;&lt;552.5,1289.0&gt;-&lt;571.0,1264.0&gt;-&lt;574.0,1232.0&gt;&gt;/L&lt;&lt;574.0,1232.0&gt;--&lt;575.0,1239.0&gt;&gt; = 13.485927397011148

* uni08DC (U+08DC): L&lt;&lt;1037.0,1143.0&gt;--&lt;1077.0,1369.0&gt;&gt;/B&lt;&lt;1077.0,1369.0&gt;-&lt;1067.0,1346.0&gt;-&lt;1040.0,1323.5&gt;&gt; = 13.461663221988582

* uni08DD (U+08DD): B&lt;&lt;1037.0,1036.0&gt;-&lt;1025.0,1030.0&gt;-&lt;1007.0,1027.0&gt;&gt;/L&lt;&lt;1007.0,1027.0&gt;--&lt;1007.0,1027.0&gt;&gt; = 9.462322208025613

* uni08DD (U+08DD): L&lt;&lt;633.0,1015.0&gt;--&lt;633.0,1015.0&gt;&gt;/B&lt;&lt;633.0,1015.0&gt;-&lt;615.0,1018.0&gt;-&lt;602.0,1025.0&gt;&gt; = 9.462322208025613

* uni08DF (U+08DF): B&lt;&lt;664.5,1173.5&gt;-&lt;669.0,1166.0&gt;-&lt;667.0,1160.0&gt;&gt;/B&lt;&lt;667.0,1160.0&gt;-&lt;672.0,1169.0&gt;-&lt;683.5,1180.5&gt;&gt; = 10.619655276155106

* uni08DF (U+08DF): L&lt;&lt;569.0,1254.0&gt;--&lt;566.0,1238.0&gt;&gt;/B&lt;&lt;566.0,1238.0&gt;-&lt;583.0,1277.0&gt;-&lt;618.5,1303.0&gt;&gt; = 12.932608396739491

* uni08E1 (U+08E1): B&lt;&lt;745.5,1153.0&gt;-&lt;681.0,1176.0&gt;-&lt;659.0,1216.0&gt;&gt;/B&lt;&lt;659.0,1216.0&gt;-&lt;669.0,1199.0&gt;-&lt;642.5,1180.5&gt;&gt; = 1.6547511764865084

* uni08EC (U+08EC): B&lt;&lt;920.5,1747.5&gt;-&lt;998.0,1699.0&gt;-&lt;1025.0,1635.0&gt;&gt;/B&lt;&lt;1025.0,1635.0&gt;-&lt;1013.0,1666.0&gt;-&lt;1015.5,1696.0&gt;&gt; = 1.712405373798543

* uni08EF (U+08EF): B&lt;&lt;524.5,-497.5&gt;-&lt;602.0,-546.0&gt;-&lt;629.0,-610.0&gt;&gt;/B&lt;&lt;629.0,-610.0&gt;-&lt;618.0,-579.0&gt;-&lt;620.0,-549.0&gt;&gt; = 3.3370102524982146

* uni08F6 (U+08F6): B&lt;&lt;378.0,-860.5&gt;-&lt;392.0,-840.0&gt;-&lt;411.0,-820.0&gt;&gt;/L&lt;&lt;411.0,-820.0&gt;--&lt;281.0,-920.0&gt;&gt; = 8.900208685558324

* uni08F6 (U+08F6): L&lt;&lt;748.0,-560.0&gt;--&lt;494.0,-756.0&gt;&gt;/B&lt;&lt;494.0,-756.0&gt;-&lt;504.0,-751.0&gt;-&lt;513.0,-750.0&gt;&gt; = 11.090649533419278

* uni08FB (U+08FB): B&lt;&lt;667.5,1229.0&gt;-&lt;678.0,1250.0&gt;-&lt;689.0,1263.0&gt;&gt;/L&lt;&lt;689.0,1263.0&gt;--&lt;476.0,1106.0&gt;&gt; = 13.370115210515044

* uni08FB (U+08FB): L&lt;&lt;851.0,1384.0&gt;--&lt;823.0,1363.0&gt;&gt;/L&lt;&lt;823.0,1363.0&gt;--&lt;981.0,1474.0&gt;&gt; = 1.780642445998502

* uni08FC (U+08FC): B&lt;&lt;733.5,1229.0&gt;-&lt;744.0,1250.0&gt;-&lt;755.0,1263.0&gt;&gt;/L&lt;&lt;755.0,1263.0&gt;--&lt;542.0,1106.0&gt;&gt; = 13.370115210515044

* uni08FC (U+08FC): L&lt;&lt;917.0,1384.0&gt;--&lt;889.0,1363.0&gt;&gt;/L&lt;&lt;889.0,1363.0&gt;--&lt;1047.0,1474.0&gt;&gt; = 1.780642445998502

* uni0E3F (U+0E3F): B&lt;&lt;990.0,704.0&gt;-&lt;933.0,667.0&gt;-&lt;872.0,663.0&gt;&gt;/B&lt;&lt;872.0,663.0&gt;-&lt;945.0,653.0&gt;-&lt;996.0,604.0&gt;&gt; = 11.551916954707687

* uni1E0D (U+1E0D): B&lt;&lt;915.0,928.5&gt;-&lt;988.0,878.0&gt;-&lt;992.0,793.0&gt;&gt;/L&lt;&lt;992.0,793.0&gt;--&lt;1074.0,1263.0&gt;&gt; = 12.59095625752517

* uni1E0F (U+1E0F): B&lt;&lt;915.0,928.5&gt;-&lt;988.0,878.0&gt;-&lt;992.0,793.0&gt;&gt;/L&lt;&lt;992.0,793.0&gt;--&lt;1074.0,1263.0&gt;&gt; = 12.59095625752517

* uni1E25 (U+1E25): L&lt;&lt;607.0,1251.0&gt;--&lt;513.0,722.0&gt;&gt;/B&lt;&lt;513.0,722.0&gt;-&lt;543.0,802.0&gt;-&lt;605.5,859.5&gt;&gt; = 10.480113582115342

* uni1E27 (U+1E27): L&lt;&lt;607.0,1251.0&gt;--&lt;513.0,722.0&gt;&gt;/B&lt;&lt;513.0,722.0&gt;-&lt;543.0,802.0&gt;-&lt;605.5,859.5&gt;&gt; = 10.480113582115342

* uni1E2B (U+1E2B): L&lt;&lt;607.0,1251.0&gt;--&lt;513.0,722.0&gt;&gt;/B&lt;&lt;513.0,722.0&gt;-&lt;543.0,802.0&gt;-&lt;605.5,859.5&gt;&gt; = 10.480113582115342

* uni1E43 (U+1E43): B&lt;&lt;801.5,890.5&gt;-&lt;821.0,850.0&gt;-&lt;807.0,799.0&gt;&gt;/B&lt;&lt;807.0,799.0&gt;-&lt;850.0,882.0&gt;-&lt;921.0,930.5&gt;&gt; = 12.037285664651744

* uni1E45 (U+1E45): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* uni1E47 (U+1E47): L&lt;&lt;529.0,863.0&gt;--&lt;477.0,738.0&gt;&gt;/B&lt;&lt;477.0,738.0&gt;-&lt;517.0,803.0&gt;-&lt;585.0,857.5&gt;&gt; = 9.020191714883133

* uni1E59 (U+1E59): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* uni1E5B (U+1E5B): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* uni1E5D (U+1E5D): L&lt;&lt;634.0,863.0&gt;--&lt;571.0,666.0&gt;&gt;/B&lt;&lt;571.0,666.0&gt;-&lt;627.0,759.0&gt;-&lt;708.0,829.5&gt;&gt; = 13.320153143693172

* uni1EA1 (U+1EA1): B&lt;&lt;460.0,-140.0&gt;-&lt;473.0,-73.0&gt;-&lt;547.0,-53.0&gt;&gt;/B&lt;&lt;547.0,-53.0&gt;-&lt;521.0,-56.0&gt;-&lt;495.0,-56.0&gt;&gt; = 8.542062653132573

* uni1EA1 (U+1EA1): B&lt;&lt;849.0,54.0&gt;-&lt;724.0,-25.0&gt;-&lt;595.0,-47.0&gt;&gt;/L&lt;&lt;595.0,-47.0&gt;--&lt;600.0,-47.0&gt;&gt; = 9.678260053133936

* uni1EA2 (U+1EA2): B&lt;&lt;682.0,1662.0&gt;-&lt;674.0,1661.0&gt;-&lt;670.0,1666.0&gt;&gt;/L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt; = 6.340191745909908

* uni1EA2 (U+1EA2): L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt;/B&lt;&lt;673.0,1663.0&gt;-&lt;665.0,1675.0&gt;-&lt;667.0,1681.0&gt;&gt; = 11.309932474020227

* uni1EA3 (U+1EA3): B&lt;&lt;598.0,1183.0&gt;-&lt;589.0,1182.0&gt;-&lt;586.0,1187.0&gt;&gt;/L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt; = 14.036243467926457

* uni1EA3 (U+1EA3): L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt;/B&lt;&lt;589.0,1184.0&gt;-&lt;580.0,1196.0&gt;-&lt;582.0,1202.0&gt;&gt; = 8.13010235415596

* uni1EA8 (U+1EA8): B&lt;&lt;918.0,1849.0&gt;-&lt;910.0,1848.0&gt;-&lt;906.0,1853.0&gt;&gt;/L&lt;&lt;906.0,1853.0&gt;--&lt;909.0,1850.0&gt;&gt; = 6.340191745909908

* uni1EA8 (U+1EA8): L&lt;&lt;906.0,1853.0&gt;--&lt;909.0,1850.0&gt;&gt;/B&lt;&lt;909.0,1850.0&gt;-&lt;901.0,1862.0&gt;-&lt;903.0,1868.0&gt;&gt; = 11.309932474020227

* uni1EAD (U+1EAD): B&lt;&lt;460.0,-140.0&gt;-&lt;473.0,-73.0&gt;-&lt;547.0,-53.0&gt;&gt;/B&lt;&lt;547.0,-53.0&gt;-&lt;521.0,-56.0&gt;-&lt;495.0,-56.0&gt;&gt; = 8.542062653132573

* uni1EAD (U+1EAD): B&lt;&lt;849.0,54.0&gt;-&lt;724.0,-25.0&gt;-&lt;595.0,-47.0&gt;&gt;/L&lt;&lt;595.0,-47.0&gt;--&lt;600.0,-47.0&gt;&gt; = 9.678260053133936

* uni1EB2 (U+1EB2): B&lt;&lt;725.0,1892.0&gt;-&lt;716.0,1891.0&gt;-&lt;713.0,1896.0&gt;&gt;/L&lt;&lt;713.0,1896.0&gt;--&lt;716.0,1893.0&gt;&gt; = 14.036243467926457

* uni1EB2 (U+1EB2): L&lt;&lt;713.0,1896.0&gt;--&lt;716.0,1893.0&gt;&gt;/B&lt;&lt;716.0,1893.0&gt;-&lt;707.0,1905.0&gt;-&lt;709.0,1911.0&gt;&gt; = 8.13010235415596

* uni1EB3 (U+1EB3): B&lt;&lt;662.0,1535.0&gt;-&lt;654.0,1534.0&gt;-&lt;650.0,1539.0&gt;&gt;/L&lt;&lt;650.0,1539.0&gt;--&lt;653.0,1536.0&gt;&gt; = 6.340191745909908

* uni1EB3 (U+1EB3): L&lt;&lt;650.0,1539.0&gt;--&lt;653.0,1536.0&gt;&gt;/B&lt;&lt;653.0,1536.0&gt;-&lt;644.0,1548.0&gt;-&lt;646.0,1554.0&gt;&gt; = 8.13010235415596

* uni1EB7 (U+1EB7): B&lt;&lt;460.0,-140.0&gt;-&lt;473.0,-73.0&gt;-&lt;547.0,-53.0&gt;&gt;/B&lt;&lt;547.0,-53.0&gt;-&lt;521.0,-56.0&gt;-&lt;495.0,-56.0&gt;&gt; = 8.542062653132573

* uni1EB7 (U+1EB7): B&lt;&lt;849.0,54.0&gt;-&lt;724.0,-25.0&gt;-&lt;595.0,-47.0&gt;&gt;/L&lt;&lt;595.0,-47.0&gt;--&lt;600.0,-47.0&gt;&gt; = 9.678260053133936

* uni1EBA (U+1EBA): B&lt;&lt;682.0,1662.0&gt;-&lt;674.0,1661.0&gt;-&lt;670.0,1666.0&gt;&gt;/L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt; = 6.340191745909908

* uni1EBA (U+1EBA): L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt;/B&lt;&lt;673.0,1663.0&gt;-&lt;665.0,1675.0&gt;-&lt;667.0,1681.0&gt;&gt; = 11.309932474020227

* uni1EBB (U+1EBB): B&lt;&lt;598.0,1183.0&gt;-&lt;589.0,1182.0&gt;-&lt;586.0,1187.0&gt;&gt;/L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt; = 14.036243467926457

* uni1EBB (U+1EBB): L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt;/B&lt;&lt;589.0,1184.0&gt;-&lt;580.0,1196.0&gt;-&lt;582.0,1202.0&gt;&gt; = 8.13010235415596

* uni1EC2 (U+1EC2): B&lt;&lt;918.0,1849.0&gt;-&lt;910.0,1848.0&gt;-&lt;906.0,1853.0&gt;&gt;/L&lt;&lt;906.0,1853.0&gt;--&lt;909.0,1850.0&gt;&gt; = 6.340191745909908

* uni1EC2 (U+1EC2): L&lt;&lt;906.0,1853.0&gt;--&lt;909.0,1850.0&gt;&gt;/B&lt;&lt;909.0,1850.0&gt;-&lt;901.0,1862.0&gt;-&lt;903.0,1868.0&gt;&gt; = 11.309932474020227

* uni1EC8 (U+1EC8): B&lt;&lt;682.0,1662.0&gt;-&lt;674.0,1661.0&gt;-&lt;670.0,1666.0&gt;&gt;/L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt; = 6.340191745909908

* uni1EC8 (U+1EC8): L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt;/B&lt;&lt;673.0,1663.0&gt;-&lt;665.0,1675.0&gt;-&lt;667.0,1681.0&gt;&gt; = 11.309932474020227

* uni1EC9 (U+1EC9): B&lt;&lt;598.0,1183.0&gt;-&lt;589.0,1182.0&gt;-&lt;586.0,1187.0&gt;&gt;/L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt; = 14.036243467926457

* uni1EC9 (U+1EC9): L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt;/B&lt;&lt;589.0,1184.0&gt;-&lt;580.0,1196.0&gt;-&lt;582.0,1202.0&gt;&gt; = 8.13010235415596

* uni1ECE (U+1ECE): B&lt;&lt;682.0,1662.0&gt;-&lt;674.0,1661.0&gt;-&lt;670.0,1666.0&gt;&gt;/L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt; = 6.340191745909908

* uni1ECE (U+1ECE): L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt;/B&lt;&lt;673.0,1663.0&gt;-&lt;665.0,1675.0&gt;-&lt;667.0,1681.0&gt;&gt; = 11.309932474020227

* uni1ECF (U+1ECF): B&lt;&lt;598.0,1183.0&gt;-&lt;589.0,1182.0&gt;-&lt;586.0,1187.0&gt;&gt;/L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt; = 14.036243467926457

* uni1ECF (U+1ECF): L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt;/B&lt;&lt;589.0,1184.0&gt;-&lt;580.0,1196.0&gt;-&lt;582.0,1202.0&gt;&gt; = 8.13010235415596

* uni1ED4 (U+1ED4): B&lt;&lt;918.0,1849.0&gt;-&lt;910.0,1848.0&gt;-&lt;906.0,1853.0&gt;&gt;/L&lt;&lt;906.0,1853.0&gt;--&lt;909.0,1850.0&gt;&gt; = 6.340191745909908

* uni1ED4 (U+1ED4): L&lt;&lt;906.0,1853.0&gt;--&lt;909.0,1850.0&gt;&gt;/B&lt;&lt;909.0,1850.0&gt;-&lt;901.0,1862.0&gt;-&lt;903.0,1868.0&gt;&gt; = 11.309932474020227

* uni1EDB (U+1EDB): B&lt;&lt;694.0,933.0&gt;-&lt;803.0,933.0&gt;-&lt;886.0,881.0&gt;&gt;/B&lt;&lt;886.0,881.0&gt;-&lt;883.0,884.0&gt;-&lt;892.0,887.0&gt;&gt; = 12.932608396739491

* uni1EDD (U+1EDD): B&lt;&lt;694.0,933.0&gt;-&lt;803.0,933.0&gt;-&lt;886.0,881.0&gt;&gt;/B&lt;&lt;886.0,881.0&gt;-&lt;883.0,884.0&gt;-&lt;892.0,887.0&gt;&gt; = 12.932608396739491

* uni1EDF (U+1EDF): B&lt;&lt;770.0,925.0&gt;-&lt;835.0,912.0&gt;-&lt;886.0,881.0&gt;&gt;/B&lt;&lt;886.0,881.0&gt;-&lt;883.0,884.0&gt;-&lt;892.0,887.0&gt;&gt; = 13.706961004079757

* uni1EE1 (U+1EE1): B&lt;&lt;694.0,933.0&gt;-&lt;803.0,933.0&gt;-&lt;886.0,881.0&gt;&gt;/B&lt;&lt;886.0,881.0&gt;-&lt;883.0,884.0&gt;-&lt;892.0,887.0&gt;&gt; = 12.932608396739491

* uni1EE3 (U+1EE3): B&lt;&lt;694.0,933.0&gt;-&lt;803.0,933.0&gt;-&lt;886.0,881.0&gt;&gt;/B&lt;&lt;886.0,881.0&gt;-&lt;883.0,884.0&gt;-&lt;892.0,887.0&gt;&gt; = 12.932608396739491

* uni1EE5 (U+1EE5): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EE6 (U+1EE6): B&lt;&lt;682.0,1662.0&gt;-&lt;674.0,1661.0&gt;-&lt;670.0,1666.0&gt;&gt;/L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt; = 6.340191745909908

* uni1EE6 (U+1EE6): L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt;/B&lt;&lt;673.0,1663.0&gt;-&lt;665.0,1675.0&gt;-&lt;667.0,1681.0&gt;&gt; = 11.309932474020227

* uni1EE7 (U+1EE7): B&lt;&lt;598.0,1183.0&gt;-&lt;589.0,1182.0&gt;-&lt;586.0,1187.0&gt;&gt;/L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt; = 14.036243467926457

* uni1EE7 (U+1EE7): L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt;/B&lt;&lt;589.0,1184.0&gt;-&lt;580.0,1196.0&gt;-&lt;582.0,1202.0&gt;&gt; = 8.13010235415596

* uni1EE7 (U+1EE7): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EE9 (U+1EE9): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EEB (U+1EEB): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EED (U+1EED): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EEF (U+1EEF): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EF1 (U+1EF1): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* uni1EF6 (U+1EF6): B&lt;&lt;682.0,1662.0&gt;-&lt;674.0,1661.0&gt;-&lt;670.0,1666.0&gt;&gt;/L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt; = 6.340191745909908

* uni1EF6 (U+1EF6): L&lt;&lt;670.0,1666.0&gt;--&lt;673.0,1663.0&gt;&gt;/B&lt;&lt;673.0,1663.0&gt;-&lt;665.0,1675.0&gt;-&lt;667.0,1681.0&gt;&gt; = 11.309932474020227

* uni1EF7 (U+1EF7): B&lt;&lt;598.0,1183.0&gt;-&lt;589.0,1182.0&gt;-&lt;586.0,1187.0&gt;&gt;/L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt; = 14.036243467926457

* uni1EF7 (U+1EF7): L&lt;&lt;586.0,1187.0&gt;--&lt;589.0,1184.0&gt;&gt;/B&lt;&lt;589.0,1184.0&gt;-&lt;580.0,1196.0&gt;-&lt;582.0,1202.0&gt;&gt; = 8.13010235415596

* uni1F08 (U+1F08): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F09 (U+1F09): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F0A (U+1F0A): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F0B (U+1F0B): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F0C (U+1F0C): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F0D (U+1F0D): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F0E (U+1F0E): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F0F (U+1F0F): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F28 (U+1F28): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F28 (U+1F28): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F29 (U+1F29): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F29 (U+1F29): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F2A (U+1F2A): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F2A (U+1F2A): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F2B (U+1F2B): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F2B (U+1F2B): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F2C (U+1F2C): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F2C (U+1F2C): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F2D (U+1F2D): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F2D (U+1F2D): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F2E (U+1F2E): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F2E (U+1F2E): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F2F (U+1F2F): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F2F (U+1F2F): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F88 (U+1F88): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F88 (U+1F88): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F88 (U+1F88): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F89 (U+1F89): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F89 (U+1F89): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F89 (U+1F89): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F8A (U+1F8A): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F8A (U+1F8A): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F8A (U+1F8A): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F8B (U+1F8B): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F8B (U+1F8B): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F8B (U+1F8B): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F8C (U+1F8C): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F8C (U+1F8C): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F8C (U+1F8C): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F8D (U+1F8D): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F8D (U+1F8D): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F8D (U+1F8D): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F8E (U+1F8E): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F8E (U+1F8E): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F8E (U+1F8E): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F8F (U+1F8F): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1F8F (U+1F8F): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1F8F (U+1F8F): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F98 (U+1F98): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F98 (U+1F98): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F98 (U+1F98): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F98 (U+1F98): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F99 (U+1F99): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F99 (U+1F99): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F99 (U+1F99): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F99 (U+1F99): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F9A (U+1F9A): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F9A (U+1F9A): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F9A (U+1F9A): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F9A (U+1F9A): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F9B (U+1F9B): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F9B (U+1F9B): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F9B (U+1F9B): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F9B (U+1F9B): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F9C (U+1F9C): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F9C (U+1F9C): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F9C (U+1F9C): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F9C (U+1F9C): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F9D (U+1F9D): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F9D (U+1F9D): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F9D (U+1F9D): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F9D (U+1F9D): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F9E (U+1F9E): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F9E (U+1F9E): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F9E (U+1F9E): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F9E (U+1F9E): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1F9F (U+1F9F): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1F9F (U+1F9F): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1F9F (U+1F9F): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1F9F (U+1F9F): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1FA8 (U+1FA8): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FA8 (U+1FA8): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FA9 (U+1FA9): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FA9 (U+1FA9): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FAA (U+1FAA): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FAA (U+1FAA): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FAB (U+1FAB): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FAB (U+1FAB): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FAC (U+1FAC): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FAC (U+1FAC): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FAD (U+1FAD): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FAD (U+1FAD): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FAE (U+1FAE): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FAE (U+1FAE): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FAF (U+1FAF): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FAF (U+1FAF): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FB8 (U+1FB8): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1FB9 (U+1FB9): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1FBA (U+1FBA): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1FBB (U+1FBB): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1FBC (U+1FBC): B&lt;&lt;145.0,156.5&gt;-&lt;174.0,154.0&gt;-&lt;171.0,138.0&gt;&gt;/L&lt;&lt;171.0,138.0&gt;--&lt;606.0,1211.0&gt;&gt; = 11.448244286255031

* uni1FBC (U+1FBC): B&lt;&lt;1495.5,405.0&gt;-&lt;1481.0,401.0&gt;-&lt;1482.0,415.0&gt;&gt;/L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt; = 5.755514979659465

* uni1FBC (U+1FBC): L&lt;&lt;1482.0,415.0&gt;--&lt;1431.0,121.0&gt;&gt;/B&lt;&lt;1431.0,121.0&gt;-&lt;1435.0,140.0&gt;-&lt;1449.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FBE (U+1FBE): B&lt;&lt;664.5,132.0&gt;-&lt;650.0,128.0&gt;-&lt;651.0,142.0&gt;&gt;/L&lt;&lt;651.0,142.0&gt;--&lt;600.0,-152.0&gt;&gt; = 5.755514979659465

* uni1FBE (U+1FBE): L&lt;&lt;651.0,142.0&gt;--&lt;600.0,-152.0&gt;&gt;/B&lt;&lt;600.0,-152.0&gt;-&lt;604.0,-133.0&gt;-&lt;618.5,-137.5&gt;&gt; = 2.0475262799936225

* uni1FCA (U+1FCA): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1FCA (U+1FCA): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1FCB (U+1FCB): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1FCB (U+1FCB): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1FCC (U+1FCC): B&lt;&lt;1503.5,405.0&gt;-&lt;1489.0,401.0&gt;-&lt;1490.0,415.0&gt;&gt;/L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt; = 5.755514979659465

* uni1FCC (U+1FCC): L&lt;&lt;1129.0,1119.0&gt;--&lt;953.0,121.0&gt;&gt;/L&lt;&lt;953.0,121.0&gt;--&lt;968.0,159.0&gt;&gt; = 11.539546451984878

* uni1FCC (U+1FCC): L&lt;&lt;1490.0,415.0&gt;--&lt;1439.0,121.0&gt;&gt;/B&lt;&lt;1439.0,121.0&gt;-&lt;1443.0,140.0&gt;-&lt;1457.5,135.5&gt;&gt; = 2.0475262799936225

* uni1FCC (U+1FCC): L&lt;&lt;858.0,739.0&gt;--&lt;919.0,1128.0&gt;&gt;/L&lt;&lt;919.0,1128.0&gt;--&lt;904.0,1092.0&gt;&gt; = 13.707756694068959

* uni1FE4 (U+1FE4): B&lt;&lt;365.5,-10.5&gt;-&lt;289.0,24.0&gt;-&lt;234.0,85.0&gt;&gt;/B&lt;&lt;234.0,85.0&gt;-&lt;245.0,67.0&gt;-&lt;243.0,7.0&gt;&gt; = 10.609498250997696

* uni1FE5 (U+1FE5): B&lt;&lt;365.5,-10.5&gt;-&lt;289.0,24.0&gt;-&lt;234.0,85.0&gt;&gt;/B&lt;&lt;234.0,85.0&gt;-&lt;245.0,67.0&gt;-&lt;243.0,7.0&gt;&gt; = 10.609498250997696

* uni1FEC (U+1FEC): L&lt;&lt;380.0,132.0&gt;--&lt;556.0,1130.0&gt;&gt;/L&lt;&lt;556.0,1130.0&gt;--&lt;541.0,1092.0&gt;&gt; = 11.53954645198491

* uni1FEC (U+1FEC): L&lt;&lt;622.0,482.0&gt;--&lt;562.0,123.0&gt;&gt;/L&lt;&lt;562.0,123.0&gt;--&lt;577.0,159.0&gt;&gt; = 13.131663889239368

* uni1FFC (U+1FFC): B&lt;&lt;1622.5,405.0&gt;-&lt;1608.0,401.0&gt;-&lt;1609.0,415.0&gt;&gt;/L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt; = 5.755514979659465

* uni1FFC (U+1FFC): L&lt;&lt;1609.0,415.0&gt;--&lt;1558.0,121.0&gt;&gt;/B&lt;&lt;1558.0,121.0&gt;-&lt;1562.0,140.0&gt;-&lt;1576.5,135.5&gt;&gt; = 2.0475262799936225

* uni200C (U+200C): B&lt;&lt;333.5,335.5&gt;-&lt;308.0,322.0&gt;-&lt;293.0,320.0&gt;&gt;/L&lt;&lt;293.0,320.0&gt;--&lt;370.0,320.0&gt;&gt; = 7.594643368591447

* uni200C (U+200C): B&lt;&lt;406.5,340.5&gt;-&lt;383.0,358.0&gt;-&lt;380.0,393.0&gt;&gt;/L&lt;&lt;380.0,393.0&gt;--&lt;380.0,388.0&gt;&gt; = 4.899092453787774

* uni200C (U+200C): B&lt;&lt;510.0,340.5&gt;-&lt;486.0,323.0&gt;-&lt;462.0,320.0&gt;&gt;/L&lt;&lt;462.0,320.0&gt;--&lt;575.0,320.0&gt;&gt; = 7.125016348901757

* uni200C (U+200C): L&lt;&lt;192.0,321.0&gt;--&lt;197.0,321.0&gt;&gt;/B&lt;&lt;197.0,321.0&gt;-&lt;188.0,322.0&gt;-&lt;173.5,329.5&gt;&gt; = 6.340191745909908

* uni200C (U+200C): L&lt;&lt;336.0,1381.0&gt;--&lt;336.0,1382.0&gt;&gt;/L&lt;&lt;336.0,1382.0&gt;--&lt;312.0,1248.0&gt;&gt; = 10.154266580200266

* uni200C (U+200C): L&lt;&lt;380.0,393.0&gt;--&lt;380.0,388.0&gt;&gt;/L&lt;&lt;380.0,388.0&gt;--&lt;372.0,446.0&gt;&gt; = 7.853313301978193

* uni200C (U+200C): L&lt;&lt;395.0,321.0&gt;--&lt;448.0,321.0&gt;&gt;/B&lt;&lt;448.0,321.0&gt;-&lt;430.0,323.0&gt;-&lt;406.5,340.5&gt;&gt; = 6.340191745909908

* uni200C (U+200C): L&lt;&lt;463.0,699.0&gt;--&lt;463.0,697.0&gt;&gt;/L&lt;&lt;463.0,697.0&gt;--&lt;484.0,815.0&gt;&gt; = 10.091057238888892

* uni200D (U+200D): B&lt;&lt;569.0,922.5&gt;-&lt;584.0,936.0&gt;-&lt;599.0,942.0&gt;&gt;/B&lt;&lt;599.0,942.0&gt;-&lt;594.0,941.0&gt;-&lt;588.0,941.0&gt;&gt; = 10.491477012331565

* uni200D (U+200D): B&lt;&lt;670.0,1010.0&gt;-&lt;661.0,966.0&gt;-&lt;620.0,948.0&gt;&gt;/B&lt;&lt;620.0,948.0&gt;-&lt;626.0,949.0&gt;-&lt;630.0,949.0&gt;&gt; = 14.240323742940625

* uni200E (U+200E): B&lt;&lt;326.5,450.5&gt;-&lt;354.0,460.0&gt;-&lt;354.0,440.0&gt;&gt;/L&lt;&lt;354.0,440.0&gt;--&lt;425.0,843.0&gt;&gt; = 9.991757893745355

* uni200E (U+200E): B&lt;&lt;739.0,1074.0&gt;-&lt;756.0,1076.0&gt;-&lt;753.0,1061.0&gt;&gt;/L&lt;&lt;753.0,1061.0&gt;--&lt;819.0,1437.0&gt;&gt; = 1.3541187700123827

* uni200E (U+200E): B&lt;&lt;966.5,829.0&gt;-&lt;939.0,820.0&gt;-&lt;941.0,840.0&gt;&gt;/L&lt;&lt;941.0,840.0&gt;--&lt;870.0,441.0&gt;&gt; = 4.379284520562349

* uni200E (U+200E): L&lt;&lt;354.0,440.0&gt;--&lt;425.0,843.0&gt;&gt;/B&lt;&lt;425.0,843.0&gt;-&lt;419.0,824.0&gt;-&lt;395.5,836.5&gt;&gt; = 7.533810479977468

* uni200E (U+200E): L&lt;&lt;532.0,1418.0&gt;--&lt;535.0,1444.0&gt;&gt;/L&lt;&lt;535.0,1444.0&gt;--&lt;465.0,1061.0&gt;&gt; = 3.775551263058629

* uni200E (U+200E): L&lt;&lt;549.0,782.0&gt;--&lt;493.0,430.0&gt;&gt;/B&lt;&lt;493.0,430.0&gt;-&lt;497.0,457.0&gt;-&lt;523.0,444.0&gt;&gt; = 0.6125137818734023

* uni200E (U+200E): L&lt;&lt;557.0,548.0&gt;--&lt;549.0,782.0&gt;&gt;/L&lt;&lt;549.0,782.0&gt;--&lt;493.0,430.0&gt;&gt; = 10.997550232589138

* uni200E (U+200E): L&lt;&lt;615.0,947.0&gt;--&lt;526.0,947.0&gt;&gt;/B&lt;&lt;526.0,947.0&gt;-&lt;566.0,946.0&gt;-&lt;589.0,928.5&gt;&gt; = 1.4320961841645452

* uni200E (U+200E): L&lt;&lt;723.0,441.0&gt;--&lt;758.0,639.0&gt;&gt;/B&lt;&lt;758.0,639.0&gt;-&lt;748.0,615.0&gt;-&lt;735.0,592.0&gt;&gt; = 12.5953781520938

* uni200E (U+200E): L&lt;&lt;961.0,1438.0&gt;--&lt;936.0,1296.0&gt;&gt;/L&lt;&lt;936.0,1296.0&gt;--&lt;949.0,1326.0&gt;&gt; = 13.443732604102049

* uni200F (U+200F): B&lt;&lt;306.0,1078.5&gt;-&lt;318.0,1078.0&gt;-&lt;315.0,1065.0&gt;&gt;/L&lt;&lt;315.0,1065.0&gt;--&lt;382.0,1442.0&gt;&gt; = 2.9172926618366253

* uni200F (U+200F): B&lt;&lt;327.0,452.5&gt;-&lt;354.0,462.0&gt;-&lt;355.0,442.0&gt;&gt;/L&lt;&lt;355.0,442.0&gt;--&lt;426.0,845.0&gt;&gt; = 12.8541631198571

* uni200F (U+200F): B&lt;&lt;968.5,831.5&gt;-&lt;942.0,822.0&gt;-&lt;941.0,842.0&gt;&gt;/L&lt;&lt;941.0,842.0&gt;--&lt;870.0,439.0&gt;&gt; = 12.8541631198571

* uni200F (U+200F): L&lt;&lt;1013.0,1422.0&gt;--&lt;1015.0,1448.0&gt;&gt;/L&lt;&lt;1015.0,1448.0&gt;--&lt;944.0,1065.0&gt;&gt; = 6.103485153754325

* uni200F (U+200F): L&lt;&lt;355.0,442.0&gt;--&lt;426.0,845.0&gt;&gt;/B&lt;&lt;426.0,845.0&gt;-&lt;419.0,826.0&gt;-&lt;396.0,838.5&gt;&gt; = 10.233101537422673

* uni200F (U+200F): L&lt;&lt;549.0,782.0&gt;--&lt;493.0,432.0&gt;&gt;/B&lt;&lt;493.0,432.0&gt;-&lt;499.0,459.0&gt;-&lt;524.5,445.5&gt;&gt; = 3.4385307883290963

* uni200F (U+200F): L&lt;&lt;558.0,550.0&gt;--&lt;549.0,782.0&gt;&gt;/L&lt;&lt;549.0,782.0&gt;--&lt;493.0,432.0&gt;&gt; = 11.311844053758348

* uni200F (U+200F): L&lt;&lt;724.0,443.0&gt;--&lt;793.0,790.0&gt;&gt;/L&lt;&lt;793.0,790.0&gt;--&lt;709.0,548.0&gt;&gt; = 7.895856511280928

* uni200F (U+200F): L&lt;&lt;941.0,842.0&gt;--&lt;870.0,439.0&gt;&gt;/B&lt;&lt;870.0,439.0&gt;-&lt;876.0,458.0&gt;-&lt;899.5,445.0&gt;&gt; = 7.533810479977468

* uni202A (U+202A): B&lt;&lt;649.5,561.5&gt;-&lt;639.0,587.0&gt;-&lt;660.0,584.0&gt;&gt;/L&lt;&lt;660.0,584.0&gt;--&lt;606.0,597.0&gt;&gt; = 5.405754014978266

* uni202A (U+202A): B&lt;&lt;743.5,1075.0&gt;-&lt;766.0,1080.0&gt;-&lt;761.0,1063.0&gt;&gt;/L&lt;&lt;761.0,1063.0&gt;--&lt;827.0,1439.0&gt;&gt; = 6.433726630026929

* uni202A (U+202A): L&lt;&lt;1177.0,1116.0&gt;--&lt;1177.0,1115.0&gt;&gt;/L&lt;&lt;1177.0,1115.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 10.145544433896337

* uni202A (U+202A): L&lt;&lt;535.0,1420.0&gt;--&lt;537.0,1446.0&gt;&gt;/L&lt;&lt;537.0,1446.0&gt;--&lt;467.0,1063.0&gt;&gt; = 5.958790563241179

* uni202A (U+202A): L&lt;&lt;760.0,815.0&gt;--&lt;793.0,815.0&gt;&gt;/L&lt;&lt;793.0,815.0&gt;--&lt;639.0,821.0&gt;&gt; = 2.231174608031095

* uni202A (U+202A): L&lt;&lt;969.0,1440.0&gt;--&lt;944.0,1298.0&gt;&gt;/L&lt;&lt;944.0,1298.0&gt;--&lt;957.0,1328.0&gt;&gt; = 13.443732604102049

* uni202B (U+202B): B&lt;&lt;304.0,1078.0&gt;-&lt;314.0,1076.0&gt;-&lt;311.0,1065.0&gt;&gt;/L&lt;&lt;311.0,1065.0&gt;--&lt;378.0,1442.0&gt;&gt; = 5.1777945729779

* uni202B (U+202B): B&lt;&lt;650.5,563.5&gt;-&lt;640.0,589.0&gt;-&lt;660.0,586.0&gt;&gt;/L&lt;&lt;660.0,586.0&gt;--&lt;606.0,599.0&gt;&gt; = 5.005090759186179

* uni202B (U+202B): L&lt;&lt;1009.0,1422.0&gt;--&lt;1011.0,1448.0&gt;&gt;/L&lt;&lt;1011.0,1448.0&gt;--&lt;940.0,1065.0&gt;&gt; = 6.103485153754325

* uni202B (U+202B): L&lt;&lt;760.0,815.0&gt;--&lt;793.0,817.0&gt;&gt;/L&lt;&lt;793.0,817.0&gt;--&lt;640.0,823.0&gt;&gt; = 5.713971824812196

* uni202D (U+202D): B&lt;&lt;743.5,1075.0&gt;-&lt;766.0,1080.0&gt;-&lt;761.0,1063.0&gt;&gt;/L&lt;&lt;761.0,1063.0&gt;--&lt;827.0,1439.0&gt;&gt; = 6.433726630026929

* uni202D (U+202D): B&lt;&lt;747.5,359.0&gt;-&lt;714.0,329.0&gt;-&lt;661.0,320.0&gt;&gt;/L&lt;&lt;661.0,320.0&gt;--&lt;780.0,320.0&gt;&gt; = 9.637538112930923

* uni202D (U+202D): L&lt;&lt;1177.0,1116.0&gt;--&lt;1177.0,1115.0&gt;&gt;/L&lt;&lt;1177.0,1115.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 10.145544433896337

* uni202D (U+202D): L&lt;&lt;395.0,321.0&gt;--&lt;538.0,320.0&gt;&gt;/B&lt;&lt;538.0,320.0&gt;-&lt;458.0,333.0&gt;-&lt;439.0,402.0&gt;&gt; = 8.829222987935541

* uni202D (U+202D): L&lt;&lt;535.0,1420.0&gt;--&lt;537.0,1446.0&gt;&gt;/L&lt;&lt;537.0,1446.0&gt;--&lt;467.0,1063.0&gt;&gt; = 5.958790563241179

* uni202D (U+202D): L&lt;&lt;969.0,1440.0&gt;--&lt;944.0,1298.0&gt;&gt;/L&lt;&lt;944.0,1298.0&gt;--&lt;957.0,1328.0&gt;&gt; = 13.443732604102049

* uni202E (U+202E): B&lt;&lt;304.0,1078.0&gt;-&lt;314.0,1076.0&gt;-&lt;311.0,1065.0&gt;&gt;/L&lt;&lt;311.0,1065.0&gt;--&lt;378.0,1442.0&gt;&gt; = 5.1777945729779

* uni202E (U+202E): B&lt;&lt;511.0,860.0&gt;-&lt;545.0,925.0&gt;-&lt;613.0,941.0&gt;&gt;/L&lt;&lt;613.0,941.0&gt;--&lt;610.0,941.0&gt;&gt; = 13.240519915187184

* uni202E (U+202E): B&lt;&lt;705.5,997.0&gt;-&lt;678.0,958.0&gt;-&lt;632.0,945.0&gt;&gt;/B&lt;&lt;632.0,945.0&gt;-&lt;659.0,949.0&gt;-&lt;696.0,949.0&gt;&gt; = 7.353784288034594

* uni202E (U+202E): B&lt;&lt;747.5,359.0&gt;-&lt;714.0,329.0&gt;-&lt;661.0,320.0&gt;&gt;/L&lt;&lt;661.0,320.0&gt;--&lt;780.0,320.0&gt;&gt; = 9.637538112930923

* uni202E (U+202E): L&lt;&lt;1009.0,1422.0&gt;--&lt;1011.0,1448.0&gt;&gt;/L&lt;&lt;1011.0,1448.0&gt;--&lt;940.0,1065.0&gt;&gt; = 6.103485153754325

* uni202E (U+202E): L&lt;&lt;395.0,321.0&gt;--&lt;538.0,320.0&gt;&gt;/B&lt;&lt;538.0,320.0&gt;-&lt;458.0,333.0&gt;-&lt;439.0,402.0&gt;&gt; = 8.829222987935541

* uni203D (U+203D): B&lt;&lt;556.5,1090.0&gt;-&lt;507.0,1074.0&gt;-&lt;479.0,1050.0&gt;&gt;/B&lt;&lt;479.0,1050.0&gt;-&lt;490.0,1060.0&gt;-&lt;493.0,1041.0&gt;&gt; = 1.6723943610892977

* uni2062 (U+2062): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uni2062 (U+2062): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uni2062 (U+2062): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uni2062 (U+2062): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uni2062 (U+2062): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uni2062 (U+2062): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uni2062 (U+2062): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uni2062 (U+2062): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uni2062 (U+2062): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uni2062 (U+2062): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uni2062 (U+2062): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uni2062 (U+2062): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uni2062 (U+2062): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uni2062 (U+2062): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uni2062 (U+2062): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uni2062 (U+2062): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uni2062 (U+2062): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uni2062 (U+2062): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uni2063 (U+2063): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uni2063 (U+2063): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uni2063 (U+2063): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uni2063 (U+2063): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uni2063 (U+2063): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uni2063 (U+2063): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uni2063 (U+2063): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uni2063 (U+2063): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uni2063 (U+2063): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uni2063 (U+2063): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uni2063 (U+2063): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uni2063 (U+2063): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uni2063 (U+2063): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uni2063 (U+2063): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uni2063 (U+2063): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uni2063 (U+2063): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uni2063 (U+2063): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uni2063 (U+2063): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uni2064 (U+2064): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uni2064 (U+2064): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uni2064 (U+2064): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uni2064 (U+2064): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uni2064 (U+2064): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uni2064 (U+2064): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uni2064 (U+2064): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uni2064 (U+2064): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uni2064 (U+2064): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uni2064 (U+2064): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uni2064 (U+2064): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uni2064 (U+2064): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uni2064 (U+2064): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uni2064 (U+2064): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uni2064 (U+2064): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uni2064 (U+2064): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uni2064 (U+2064): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uni2064 (U+2064): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uni2066 (U+2066): B&lt;&lt;739.0,1074.0&gt;-&lt;756.0,1076.0&gt;-&lt;753.0,1061.0&gt;&gt;/L&lt;&lt;753.0,1061.0&gt;--&lt;819.0,1437.0&gt;&gt; = 1.3541187700123827

* uni2066 (U+2066): L&lt;&lt;532.0,1418.0&gt;--&lt;535.0,1444.0&gt;&gt;/L&lt;&lt;535.0,1444.0&gt;--&lt;465.0,1061.0&gt;&gt; = 3.775551263058629

* uni2066 (U+2066): L&lt;&lt;961.0,1438.0&gt;--&lt;936.0,1296.0&gt;&gt;/L&lt;&lt;936.0,1296.0&gt;--&lt;949.0,1326.0&gt;&gt; = 13.443732604102049

* uni2067 (U+2067): B&lt;&lt;304.0,1078.0&gt;-&lt;314.0,1076.0&gt;-&lt;311.0,1065.0&gt;&gt;/L&lt;&lt;311.0,1065.0&gt;--&lt;378.0,1442.0&gt;&gt; = 5.1777945729779

* uni2067 (U+2067): L&lt;&lt;1009.0,1422.0&gt;--&lt;1011.0,1448.0&gt;&gt;/L&lt;&lt;1011.0,1448.0&gt;--&lt;940.0,1065.0&gt;&gt; = 6.103485153754325

* uni2068 (U+2068): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uni2068 (U+2068): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uni2068 (U+2068): L&lt;&lt;483.0,1472.0&gt;--&lt;488.0,1505.0&gt;&gt;/L&lt;&lt;488.0,1505.0&gt;--&lt;485.0,1472.0&gt;&gt; = 3.421219276429211

* uni20A6 (U+20A6): L&lt;&lt;1113.0,1114.0&gt;--&lt;1068.0,858.0&gt;&gt;/L&lt;&lt;1068.0,858.0&gt;--&lt;1083.0,892.0&gt;&gt; = 13.83627156478248

* uni20A6 (U+20A6): L&lt;&lt;180.0,137.0&gt;--&lt;225.0,393.0&gt;&gt;/L&lt;&lt;225.0,393.0&gt;--&lt;210.0,359.0&gt;&gt; = 13.836271564782507

* uni2103 (U+2103): B&lt;&lt;1031.5,1282.5&gt;-&lt;1071.0,1264.0&gt;-&lt;1090.0,1238.0&gt;&gt;/B&lt;&lt;1090.0,1238.0&gt;-&lt;1078.0,1252.0&gt;-&lt;1103.5,1279.5&gt;&gt; = 4.443109205196117

* uni2116 (U+2116): L&lt;&lt;129.0,143.0&gt;--&lt;289.0,1054.0&gt;&gt;/L&lt;&lt;289.0,1054.0&gt;--&lt;278.0,1016.0&gt;&gt; = 6.183008003022422

* uni2116 (U+2116): L&lt;&lt;951.0,1044.0&gt;--&lt;791.0,132.0&gt;&gt;/L&lt;&lt;791.0,132.0&gt;--&lt;802.0,170.0&gt;&gt; = 6.193712092331838

* uni2117 (U+2117): L&lt;&lt;405.0,302.0&gt;--&lt;405.0,276.0&gt;&gt;/L&lt;&lt;405.0,276.0&gt;--&lt;493.0,774.0&gt;&gt; = 10.021105982085244

* uni2127 (U+2127): B&lt;&lt;1067.0,1071.5&gt;-&lt;1070.0,1093.0&gt;-&lt;1085.0,1096.0&gt;&gt;/L&lt;&lt;1085.0,1096.0&gt;--&lt;984.0,1100.0&gt;&gt; = 13.577887009926041

* uni2222 (U+2222): L&lt;&lt;905.0,144.0&gt;--&lt;774.0,218.0&gt;&gt;/B&lt;&lt;774.0,218.0&gt;-&lt;790.0,210.0&gt;-&lt;781.0,196.5&gt;&gt; = 2.896423793889857

* uni2300 (U+2300): B&lt;&lt;377.5,557.0&gt;-&lt;375.0,528.0&gt;-&lt;356.0,509.0&gt;&gt;/L&lt;&lt;356.0,509.0&gt;--&lt;815.0,901.0&gt;&gt; = 4.5016626197639615

* uni2300 (U+2300): B&lt;&lt;916.5,696.0&gt;-&lt;919.0,725.0&gt;-&lt;938.0,744.0&gt;&gt;/L&lt;&lt;938.0,744.0&gt;--&lt;478.0,352.0&gt;&gt; = 4.563229754237693

* uni2300 (U+2300): L&lt;&lt;356.0,509.0&gt;--&lt;815.0,901.0&gt;&gt;/B&lt;&lt;815.0,901.0&gt;-&lt;792.0,883.0&gt;-&lt;763.5,885.5&gt;&gt; = 2.451294848409976

* uni2300 (U+2300): L&lt;&lt;938.0,744.0&gt;--&lt;478.0,352.0&gt;&gt;/B&lt;&lt;478.0,352.0&gt;-&lt;501.0,370.0&gt;-&lt;529.5,368.0&gt;&gt; = 2.3897277139359234

* uni2422 (U+2422): L&lt;&lt;180.0,90.0&gt;--&lt;306.0,801.0&gt;&gt;/L&lt;&lt;306.0,801.0&gt;--&lt;280.0,712.0&gt;&gt; = 6.2355738837585175

* uni2422 (U+2422): L&lt;&lt;528.0,897.0&gt;--&lt;505.0,818.0&gt;&gt;/B&lt;&lt;505.0,818.0&gt;-&lt;535.0,870.0&gt;-&lt;607.5,899.5&gt;&gt; = 13.749288707693122

* uni2E18 (U+2E18): B&lt;&lt;627.5,-294.0&gt;-&lt;677.0,-278.0&gt;-&lt;706.0,-253.0&gt;&gt;/B&lt;&lt;706.0,-253.0&gt;-&lt;694.0,-262.0&gt;-&lt;692.0,-243.0&gt;&gt; = 3.893707555097004

* uniFB51 (U+FB51): B&lt;&lt;743.0,1620.5&gt;-&lt;750.0,1597.0&gt;-&lt;746.0,1587.0&gt;&gt;/B&lt;&lt;746.0,1587.0&gt;-&lt;801.0,1697.0&gt;-&lt;901.5,1773.0&gt;&gt; = 4.763641690726066

* uniFB53 (U+FB53): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFB57 (U+FB57): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFB57 (U+FB57): B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uniFB57 (U+FB57): L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uniFB58 (U+FB58): B&lt;&lt;629.5,-208.0&gt;-&lt;587.0,-162.0&gt;-&lt;571.0,-116.0&gt;&gt;/B&lt;&lt;571.0,-116.0&gt;-&lt;573.0,-125.0&gt;-&lt;572.0,-133.0&gt;&gt; = 6.650200316659149

* uniFB58 (U+FB58): L&lt;&lt;565.0,-93.0&gt;--&lt;565.0,-94.0&gt;&gt;/B&lt;&lt;565.0,-94.0&gt;-&lt;564.0,-85.0&gt;-&lt;564.0,-76.0&gt;&gt; = 6.340191745909908

* uniFB59 (U+FB59): B&lt;&lt;611.5,-208.0&gt;-&lt;569.0,-162.0&gt;-&lt;553.0,-116.0&gt;&gt;/B&lt;&lt;553.0,-116.0&gt;-&lt;555.0,-125.0&gt;-&lt;554.0,-133.0&gt;&gt; = 6.650200316659149

* uniFB59 (U+FB59): L&lt;&lt;547.0,-93.0&gt;--&lt;547.0,-94.0&gt;&gt;/B&lt;&lt;547.0,-94.0&gt;-&lt;546.0,-85.0&gt;-&lt;546.0,-76.0&gt;&gt; = 6.340191745909908

* uniFB5B (U+FB5B): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFB5B (U+FB5B): B&lt;&lt;423.0,-420.5&gt;-&lt;456.0,-461.0&gt;-&lt;470.0,-499.0&gt;&gt;/B&lt;&lt;470.0,-499.0&gt;-&lt;469.0,-492.0&gt;-&lt;470.0,-486.0&gt;&gt; = 12.094757077012089

* uniFB5B (U+FB5B): B&lt;&lt;472.5,-61.0&gt;-&lt;514.0,-108.0&gt;-&lt;531.0,-153.0&gt;&gt;/B&lt;&lt;531.0,-153.0&gt;-&lt;530.0,-146.0&gt;-&lt;531.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB5C (U+FB5C): B&lt;&lt;423.0,-420.5&gt;-&lt;456.0,-461.0&gt;-&lt;470.0,-499.0&gt;&gt;/B&lt;&lt;470.0,-499.0&gt;-&lt;469.0,-492.0&gt;-&lt;470.0,-486.0&gt;&gt; = 12.094757077012089

* uniFB5C (U+FB5C): B&lt;&lt;472.5,-61.0&gt;-&lt;514.0,-108.0&gt;-&lt;531.0,-153.0&gt;&gt;/B&lt;&lt;531.0,-153.0&gt;-&lt;530.0,-146.0&gt;-&lt;531.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB5D (U+FB5D): B&lt;&lt;431.0,-420.5&gt;-&lt;464.0,-461.0&gt;-&lt;478.0,-499.0&gt;&gt;/B&lt;&lt;478.0,-499.0&gt;-&lt;477.0,-492.0&gt;-&lt;478.0,-486.0&gt;&gt; = 12.094757077012089

* uniFB5D (U+FB5D): B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB5F (U+FB5F): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFB63 (U+FB63): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFB63 (U+FB63): B&lt;&lt;744.5,1256.5&gt;-&lt;777.0,1216.0&gt;-&lt;792.0,1178.0&gt;&gt;/B&lt;&lt;792.0,1178.0&gt;-&lt;791.0,1185.0&gt;-&lt;791.0,1191.0&gt;&gt; = 13.410873564382426

* uniFB63 (U+FB63): B&lt;&lt;794.0,1616.0&gt;-&lt;836.0,1569.0&gt;-&lt;853.0,1524.0&gt;&gt;/B&lt;&lt;853.0,1524.0&gt;-&lt;852.0,1531.0&gt;-&lt;852.0,1537.0&gt;&gt; = 12.565348379907297

* uniFB63 (U+FB63): B&lt;&lt;858.5,1058.0&gt;-&lt;817.0,1103.0&gt;-&lt;799.0,1148.0&gt;&gt;/B&lt;&lt;799.0,1148.0&gt;-&lt;800.0,1142.0&gt;-&lt;800.0,1136.0&gt;&gt; = 12.33908727832621

* uniFB63 (U+FB63): B&lt;&lt;907.5,1417.0&gt;-&lt;875.0,1456.0&gt;-&lt;860.0,1494.0&gt;&gt;/B&lt;&lt;860.0,1494.0&gt;-&lt;861.0,1488.0&gt;-&lt;861.0,1482.0&gt;&gt; = 12.078653710512796

* uniFB64 (U+FB64): B&lt;&lt;744.5,1256.5&gt;-&lt;777.0,1216.0&gt;-&lt;792.0,1178.0&gt;&gt;/B&lt;&lt;792.0,1178.0&gt;-&lt;791.0,1185.0&gt;-&lt;791.0,1191.0&gt;&gt; = 13.410873564382426

* uniFB64 (U+FB64): B&lt;&lt;794.0,1616.0&gt;-&lt;836.0,1569.0&gt;-&lt;853.0,1524.0&gt;&gt;/B&lt;&lt;853.0,1524.0&gt;-&lt;852.0,1531.0&gt;-&lt;852.0,1537.0&gt;&gt; = 12.565348379907297

* uniFB64 (U+FB64): B&lt;&lt;858.5,1058.0&gt;-&lt;817.0,1103.0&gt;-&lt;799.0,1148.0&gt;&gt;/B&lt;&lt;799.0,1148.0&gt;-&lt;800.0,1142.0&gt;-&lt;800.0,1136.0&gt;&gt; = 12.33908727832621

* uniFB64 (U+FB64): B&lt;&lt;907.5,1417.0&gt;-&lt;875.0,1456.0&gt;-&lt;860.0,1494.0&gt;&gt;/B&lt;&lt;860.0,1494.0&gt;-&lt;861.0,1488.0&gt;-&lt;861.0,1482.0&gt;&gt; = 12.078653710512796

* uniFB65 (U+FB65): B&lt;&lt;722.5,1256.5&gt;-&lt;755.0,1216.0&gt;-&lt;770.0,1178.0&gt;&gt;/B&lt;&lt;770.0,1178.0&gt;-&lt;769.0,1185.0&gt;-&lt;769.0,1191.0&gt;&gt; = 13.410873564382426

* uniFB65 (U+FB65): B&lt;&lt;772.0,1616.0&gt;-&lt;814.0,1569.0&gt;-&lt;831.0,1524.0&gt;&gt;/B&lt;&lt;831.0,1524.0&gt;-&lt;830.0,1531.0&gt;-&lt;830.0,1537.0&gt;&gt; = 12.565348379907297

* uniFB65 (U+FB65): B&lt;&lt;836.5,1058.0&gt;-&lt;795.0,1103.0&gt;-&lt;777.0,1148.0&gt;&gt;/B&lt;&lt;777.0,1148.0&gt;-&lt;778.0,1142.0&gt;-&lt;778.0,1136.0&gt;&gt; = 12.33908727832621

* uniFB65 (U+FB65): B&lt;&lt;885.5,1417.0&gt;-&lt;853.0,1456.0&gt;-&lt;838.0,1494.0&gt;&gt;/B&lt;&lt;838.0,1494.0&gt;-&lt;839.0,1488.0&gt;-&lt;839.0,1482.0&gt;&gt; = 12.078653710512796

* uniFB67 (U+FB67): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFB67 (U+FB67): L&lt;&lt;867.0,1710.0&gt;--&lt;804.0,1360.0&gt;&gt;/B&lt;&lt;804.0,1360.0&gt;-&lt;827.0,1461.0&gt;-&lt;890.0,1514.0&gt;&gt; = 2.624809149723495

* uniFB68 (U+FB68): L&lt;&lt;1043.0,1710.0&gt;--&lt;980.0,1360.0&gt;&gt;/B&lt;&lt;980.0,1360.0&gt;-&lt;1003.0,1461.0&gt;-&lt;1066.0,1514.0&gt;&gt; = 2.624809149723495

* uniFB69 (U+FB69): L&lt;&lt;1043.0,1710.0&gt;--&lt;980.0,1360.0&gt;&gt;/B&lt;&lt;980.0,1360.0&gt;-&lt;1003.0,1461.0&gt;-&lt;1066.0,1514.0&gt;&gt; = 2.624809149723495

* uniFB6B (U+FB6B): B&lt;&lt;818.5,1453.0&gt;-&lt;860.0,1406.0&gt;-&lt;877.0,1361.0&gt;&gt;/B&lt;&lt;877.0,1361.0&gt;-&lt;876.0,1368.0&gt;-&lt;877.0,1374.0&gt;&gt; = 12.565348379907297

* uniFB6C (U+FB6C): B&lt;&lt;826.0,1508.0&gt;-&lt;868.0,1461.0&gt;-&lt;885.0,1416.0&gt;&gt;/B&lt;&lt;885.0,1416.0&gt;-&lt;884.0,1423.0&gt;-&lt;884.0,1429.0&gt;&gt; = 12.565348379907297

* uniFB6C (U+FB6C): B&lt;&lt;951.5,1296.0&gt;-&lt;910.0,1341.0&gt;-&lt;892.0,1386.0&gt;&gt;/B&lt;&lt;892.0,1386.0&gt;-&lt;893.0,1380.0&gt;-&lt;893.0,1374.0&gt;&gt; = 12.33908727832621

* uniFB6D (U+FB6D): B&lt;&lt;721.0,1492.0&gt;-&lt;763.0,1445.0&gt;-&lt;780.0,1400.0&gt;&gt;/B&lt;&lt;780.0,1400.0&gt;-&lt;779.0,1407.0&gt;-&lt;780.0,1413.0&gt;&gt; = 12.565348379907297

* uniFB6D (U+FB6D): B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uniFB6F (U+FB6F): B&lt;&lt;827.0,1422.5&gt;-&lt;860.0,1382.0&gt;-&lt;874.0,1344.0&gt;&gt;/B&lt;&lt;874.0,1344.0&gt;-&lt;873.0,1351.0&gt;-&lt;874.0,1357.0&gt;&gt; = 12.094757077012089

* uniFB6F (U+FB6F): B&lt;&lt;876.5,1782.0&gt;-&lt;918.0,1735.0&gt;-&lt;935.0,1690.0&gt;&gt;/B&lt;&lt;935.0,1690.0&gt;-&lt;934.0,1697.0&gt;-&lt;935.0,1703.0&gt;&gt; = 12.565348379907297

* uniFB70 (U+FB70): B&lt;&lt;1012.5,1581.0&gt;-&lt;980.0,1620.0&gt;-&lt;965.0,1658.0&gt;&gt;/B&lt;&lt;965.0,1658.0&gt;-&lt;966.0,1652.0&gt;-&lt;966.0,1646.0&gt;&gt; = 12.078653710512796

* uniFB70 (U+FB70): B&lt;&lt;849.5,1420.5&gt;-&lt;882.0,1380.0&gt;-&lt;897.0,1342.0&gt;&gt;/B&lt;&lt;897.0,1342.0&gt;-&lt;896.0,1349.0&gt;-&lt;896.0,1355.0&gt;&gt; = 13.410873564382426

* uniFB70 (U+FB70): B&lt;&lt;899.0,1780.0&gt;-&lt;941.0,1733.0&gt;-&lt;958.0,1688.0&gt;&gt;/B&lt;&lt;958.0,1688.0&gt;-&lt;957.0,1695.0&gt;-&lt;957.0,1701.0&gt;&gt; = 12.565348379907297

* uniFB70 (U+FB70): B&lt;&lt;963.0,1222.0&gt;-&lt;921.0,1267.0&gt;-&lt;904.0,1312.0&gt;&gt;/B&lt;&lt;904.0,1312.0&gt;-&lt;905.0,1306.0&gt;-&lt;905.0,1300.0&gt;&gt; = 11.233128526037627

* uniFB71 (U+FB71): B&lt;&lt;723.0,1422.5&gt;-&lt;756.0,1382.0&gt;-&lt;770.0,1344.0&gt;&gt;/B&lt;&lt;770.0,1344.0&gt;-&lt;769.0,1351.0&gt;-&lt;770.0,1357.0&gt;&gt; = 12.094757077012089

* uniFB71 (U+FB71): B&lt;&lt;772.5,1782.0&gt;-&lt;814.0,1735.0&gt;-&lt;831.0,1690.0&gt;&gt;/B&lt;&lt;831.0,1690.0&gt;-&lt;830.0,1697.0&gt;-&lt;831.0,1703.0&gt;&gt; = 12.565348379907297

* uniFB71 (U+FB71): B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uniFB77 (U+FB77): B&lt;&lt;533.5,117.0&gt;-&lt;575.0,70.0&gt;-&lt;593.0,25.0&gt;&gt;/B&lt;&lt;593.0,25.0&gt;-&lt;592.0,32.0&gt;-&lt;592.0,38.0&gt;&gt; = 13.67130713219584

* uniFB77 (U+FB77): B&lt;&lt;659.0,-95.0&gt;-&lt;617.0,-50.0&gt;-&lt;600.0,-5.0&gt;&gt;/B&lt;&lt;600.0,-5.0&gt;-&lt;601.0,-11.0&gt;-&lt;601.0,-17.0&gt;&gt; = 11.233128526037627

* uniFB78 (U+FB78): B&lt;&lt;447.5,-61.0&gt;-&lt;489.0,-108.0&gt;-&lt;506.0,-153.0&gt;&gt;/B&lt;&lt;506.0,-153.0&gt;-&lt;505.0,-146.0&gt;-&lt;506.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB79 (U+FB79): B&lt;&lt;447.5,-61.0&gt;-&lt;489.0,-108.0&gt;-&lt;506.0,-153.0&gt;&gt;/B&lt;&lt;506.0,-153.0&gt;-&lt;505.0,-146.0&gt;-&lt;506.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB7B (U+FB7B): B&lt;&lt;488.5,221.0&gt;-&lt;529.0,175.0&gt;-&lt;546.0,129.0&gt;&gt;/B&lt;&lt;546.0,129.0&gt;-&lt;544.0,138.0&gt;-&lt;544.0,147.0&gt;&gt; = 7.753751379765042

* uniFB7B (U+FB7B): B&lt;&lt;610.5,15.0&gt;-&lt;568.0,61.0&gt;-&lt;551.0,107.0&gt;&gt;/B&lt;&lt;551.0,107.0&gt;-&lt;553.0,98.0&gt;-&lt;552.0,90.0&gt;&gt; = 7.753751379765042

* uniFB7C (U+FB7C): B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uniFB7D (U+FB7D): B&lt;&lt;571.5,-272.0&gt;-&lt;529.0,-226.0&gt;-&lt;513.0,-180.0&gt;&gt;/B&lt;&lt;513.0,-180.0&gt;-&lt;514.0,-189.0&gt;-&lt;514.0,-197.0&gt;&gt; = 12.83881627990079

* uniFB7F (U+FB7F): B&lt;&lt;491.0,-55.5&gt;-&lt;524.0,-96.0&gt;-&lt;539.0,-134.0&gt;&gt;/B&lt;&lt;539.0,-134.0&gt;-&lt;538.0,-127.0&gt;-&lt;538.0,-121.0&gt;&gt; = 13.410873564382426

* uniFB7F (U+FB7F): B&lt;&lt;555.5,286.5&gt;-&lt;586.0,248.0&gt;-&lt;600.0,212.0&gt;&gt;/B&lt;&lt;600.0,212.0&gt;-&lt;599.0,219.0&gt;-&lt;599.0,225.0&gt;&gt; = 13.120403152977243

* uniFB7F (U+FB7F): B&lt;&lt;586.0,-232.5&gt;-&lt;559.0,-198.0&gt;-&lt;546.0,-164.0&gt;&gt;/B&lt;&lt;546.0,-164.0&gt;-&lt;547.0,-170.0&gt;-&lt;547.0,-176.0&gt;&gt; = 11.462179536895567

* uniFB7F (U+FB7F): B&lt;&lt;654.0,105.0&gt;-&lt;621.0,144.0&gt;-&lt;607.0,182.0&gt;&gt;/B&lt;&lt;607.0,182.0&gt;-&lt;608.0,176.0&gt;-&lt;608.0,170.0&gt;&gt; = 10.762537223142443

* uniFB80 (U+FB80): B&lt;&lt;398.0,-420.5&gt;-&lt;431.0,-461.0&gt;-&lt;445.0,-499.0&gt;&gt;/B&lt;&lt;445.0,-499.0&gt;-&lt;444.0,-492.0&gt;-&lt;445.0,-486.0&gt;&gt; = 12.094757077012089

* uniFB80 (U+FB80): B&lt;&lt;447.5,-61.0&gt;-&lt;489.0,-108.0&gt;-&lt;506.0,-153.0&gt;&gt;/B&lt;&lt;506.0,-153.0&gt;-&lt;505.0,-146.0&gt;-&lt;506.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB81 (U+FB81): B&lt;&lt;398.0,-420.5&gt;-&lt;431.0,-461.0&gt;-&lt;445.0,-499.0&gt;&gt;/B&lt;&lt;445.0,-499.0&gt;-&lt;444.0,-492.0&gt;-&lt;445.0,-486.0&gt;&gt; = 12.094757077012089

* uniFB81 (U+FB81): B&lt;&lt;447.5,-61.0&gt;-&lt;489.0,-108.0&gt;-&lt;506.0,-153.0&gt;&gt;/B&lt;&lt;506.0,-153.0&gt;-&lt;505.0,-146.0&gt;-&lt;506.0,-140.0&gt;&gt; = 12.565348379907297

* uniFB83 (U+FB83): B&lt;&lt;371.5,-106.0&gt;-&lt;413.0,-153.0&gt;-&lt;430.0,-198.0&gt;&gt;/B&lt;&lt;430.0,-198.0&gt;-&lt;429.0,-191.0&gt;-&lt;430.0,-185.0&gt;&gt; = 12.565348379907297

* uniFB83 (U+FB83): B&lt;&lt;497.0,-318.0&gt;-&lt;455.0,-273.0&gt;-&lt;438.0,-228.0&gt;&gt;/B&lt;&lt;438.0,-228.0&gt;-&lt;439.0,-234.0&gt;-&lt;438.0,-240.0&gt;&gt; = 11.233128526037627

* uniFB85 (U+FB85): B&lt;&lt;667.5,1573.0&gt;-&lt;709.0,1526.0&gt;-&lt;726.0,1481.0&gt;&gt;/B&lt;&lt;726.0,1481.0&gt;-&lt;725.0,1488.0&gt;-&lt;726.0,1494.0&gt;&gt; = 12.565348379907297

* uniFB85 (U+FB85): B&lt;&lt;793.0,1361.0&gt;-&lt;751.0,1406.0&gt;-&lt;734.0,1451.0&gt;&gt;/B&lt;&lt;734.0,1451.0&gt;-&lt;735.0,1445.0&gt;-&lt;734.0,1439.0&gt;&gt; = 11.233128526037627

* uniFB87 (U+FB87): B&lt;&lt;656.0,1508.0&gt;-&lt;698.0,1461.0&gt;-&lt;715.0,1416.0&gt;&gt;/B&lt;&lt;715.0,1416.0&gt;-&lt;714.0,1423.0&gt;-&lt;714.0,1429.0&gt;&gt; = 12.565348379907297

* uniFB87 (U+FB87): B&lt;&lt;781.5,1296.0&gt;-&lt;740.0,1341.0&gt;-&lt;722.0,1386.0&gt;&gt;/B&lt;&lt;722.0,1386.0&gt;-&lt;723.0,1380.0&gt;-&lt;723.0,1374.0&gt;&gt; = 12.33908727832621

* uniFB89 (U+FB89): L&lt;&lt;649.0,1778.0&gt;--&lt;586.0,1428.0&gt;&gt;/B&lt;&lt;586.0,1428.0&gt;-&lt;609.0,1529.0&gt;-&lt;672.0,1582.0&gt;&gt; = 2.624809149723495

* uniFB8B (U+FB8B): B&lt;&lt;685.5,1125.0&gt;-&lt;727.0,1078.0&gt;-&lt;744.0,1033.0&gt;&gt;/B&lt;&lt;744.0,1033.0&gt;-&lt;743.0,1040.0&gt;-&lt;744.0,1046.0&gt;&gt; = 12.565348379907297

* uniFB8B (U+FB8B): B&lt;&lt;811.0,913.0&gt;-&lt;769.0,958.0&gt;-&lt;752.0,1003.0&gt;&gt;/B&lt;&lt;752.0,1003.0&gt;-&lt;753.0,997.0&gt;-&lt;752.0,991.0&gt;&gt; = 11.233128526037627

* uniFB8D (U+FB8D): L&lt;&lt;799.0,1477.0&gt;--&lt;736.0,1127.0&gt;&gt;/B&lt;&lt;736.0,1127.0&gt;-&lt;759.0,1228.0&gt;-&lt;822.0,1281.0&gt;&gt; = 2.624809149723495

* uniFB9B (U+FB9B): B&lt;&lt;873.0,1100.0&gt;-&lt;915.0,1053.0&gt;-&lt;932.0,1008.0&gt;&gt;/B&lt;&lt;932.0,1008.0&gt;-&lt;931.0,1015.0&gt;-&lt;931.0,1021.0&gt;&gt; = 12.565348379907297

* uniFB9B (U+FB9B): B&lt;&lt;998.5,888.0&gt;-&lt;957.0,933.0&gt;-&lt;939.0,978.0&gt;&gt;/B&lt;&lt;939.0,978.0&gt;-&lt;940.0,972.0&gt;-&lt;940.0,966.0&gt;&gt; = 12.33908727832621

* uniFB9C (U+FB9C): B&lt;&lt;528.5,1782.0&gt;-&lt;570.0,1735.0&gt;-&lt;587.0,1690.0&gt;&gt;/B&lt;&lt;587.0,1690.0&gt;-&lt;586.0,1697.0&gt;-&lt;587.0,1703.0&gt;&gt; = 12.565348379907297

* uniFB9D (U+FB9D): B&lt;&lt;1030.0,960.0&gt;-&lt;988.0,1005.0&gt;-&lt;971.0,1050.0&gt;&gt;/B&lt;&lt;971.0,1050.0&gt;-&lt;972.0,1044.0&gt;-&lt;972.0,1038.0&gt;&gt; = 11.233128526037627

* uniFB9D (U+FB9D): B&lt;&lt;905.0,1172.0&gt;-&lt;947.0,1125.0&gt;-&lt;964.0,1080.0&gt;&gt;/B&lt;&lt;964.0,1080.0&gt;-&lt;963.0,1087.0&gt;-&lt;963.0,1093.0&gt;&gt; = 12.565348379907297

* uniFBA1 (U+FBA1): L&lt;&lt;766.0,1292.0&gt;--&lt;703.0,942.0&gt;&gt;/B&lt;&lt;703.0,942.0&gt;-&lt;726.0,1043.0&gt;-&lt;789.5,1096.0&gt;&gt; = 2.624809149723495

* uniFBA2 (U+FBA2): L&lt;&lt;637.0,1710.0&gt;--&lt;574.0,1360.0&gt;&gt;/B&lt;&lt;574.0,1360.0&gt;-&lt;597.0,1461.0&gt;-&lt;660.0,1514.0&gt;&gt; = 2.624809149723495

* uniFBA3 (U+FBA3): L&lt;&lt;637.0,1710.0&gt;--&lt;574.0,1360.0&gt;&gt;/B&lt;&lt;574.0,1360.0&gt;-&lt;597.0,1461.0&gt;-&lt;660.0,1514.0&gt;&gt; = 2.624809149723495

* uniFBA5 (U+FBA5): B&lt;&lt;429.0,1406.0&gt;-&lt;484.0,1433.0&gt;-&lt;541.0,1450.0&gt;&gt;/B&lt;&lt;541.0,1450.0&gt;-&lt;492.0,1442.0&gt;-&lt;459.5,1496.5&gt;&gt; = 7.334378801416706

* uniFBA9 (U+FBA9): B&lt;&lt;310.5,133.0&gt;-&lt;330.0,181.0&gt;-&lt;375.0,192.0&gt;&gt;/L&lt;&lt;375.0,192.0&gt;--&lt;26.0,194.0&gt;&gt; = 14.064607287393274

* uniFBAC (U+FBAC): B&lt;&lt;268.5,402.0&gt;-&lt;312.0,401.0&gt;-&lt;332.0,393.0&gt;&gt;/B&lt;&lt;332.0,393.0&gt;-&lt;314.0,403.0&gt;-&lt;307.0,439.5&gt;&gt; = 7.253194612725265

* uniFBAC (U+FBAC): B&lt;&lt;515.5,466.0&gt;-&lt;522.0,450.0&gt;-&lt;539.0,437.0&gt;&gt;/B&lt;&lt;539.0,437.0&gt;-&lt;537.0,439.0&gt;-&lt;554.0,447.0&gt;&gt; = 7.594643368591447

* uniFBAC (U+FBAC): B&lt;&lt;935.5,677.5&gt;-&lt;934.0,735.0&gt;-&lt;940.0,777.0&gt;&gt;/B&lt;&lt;940.0,777.0&gt;-&lt;917.0,648.0&gt;-&lt;883.0,550.0&gt;&gt; = 1.9791961383390095

* uniFBAD (U+FBAD): B&lt;&lt;268.5,402.0&gt;-&lt;312.0,401.0&gt;-&lt;332.0,393.0&gt;&gt;/B&lt;&lt;332.0,393.0&gt;-&lt;314.0,403.0&gt;-&lt;307.0,439.5&gt;&gt; = 7.253194612725265

* uniFBAD (U+FBAD): B&lt;&lt;515.5,466.0&gt;-&lt;522.0,450.0&gt;-&lt;539.0,437.0&gt;&gt;/B&lt;&lt;539.0,437.0&gt;-&lt;537.0,439.0&gt;-&lt;554.0,447.0&gt;&gt; = 7.594643368591447

* uniFBAD (U+FBAD): B&lt;&lt;935.5,677.5&gt;-&lt;934.0,735.0&gt;-&lt;940.0,777.0&gt;&gt;/B&lt;&lt;940.0,777.0&gt;-&lt;917.0,648.0&gt;-&lt;883.0,550.0&gt;&gt; = 1.9791961383390095

* uniFBB1 (U+FBB1): B&lt;&lt;248.0,866.0&gt;-&lt;303.0,893.0&gt;-&lt;360.0,910.0&gt;&gt;/B&lt;&lt;360.0,910.0&gt;-&lt;311.0,902.0&gt;-&lt;278.5,956.5&gt;&gt; = 7.334378801416706

* uniFBB4 (U+FBB4): B&lt;&lt;795.0,999.0&gt;-&lt;753.0,1044.0&gt;-&lt;736.0,1089.0&gt;&gt;/B&lt;&lt;736.0,1089.0&gt;-&lt;737.0,1083.0&gt;-&lt;736.0,1077.0&gt;&gt; = 11.233128526037627

* uniFBB5 (U+FBB5): B&lt;&lt;445.5,-59.0&gt;-&lt;487.0,-106.0&gt;-&lt;505.0,-151.0&gt;&gt;/B&lt;&lt;505.0,-151.0&gt;-&lt;504.0,-144.0&gt;-&lt;504.0,-138.0&gt;&gt; = 13.67130713219584

* uniFBB5 (U+FBB5): B&lt;&lt;571.0,-271.0&gt;-&lt;529.0,-226.0&gt;-&lt;512.0,-181.0&gt;&gt;/B&lt;&lt;512.0,-181.0&gt;-&lt;513.0,-187.0&gt;-&lt;513.0,-193.0&gt;&gt; = 11.233128526037627

* uniFBB6 (U+FBB6): B&lt;&lt;795.0,999.0&gt;-&lt;753.0,1044.0&gt;-&lt;736.0,1089.0&gt;&gt;/B&lt;&lt;736.0,1089.0&gt;-&lt;737.0,1083.0&gt;-&lt;736.0,1077.0&gt;&gt; = 11.233128526037627

* uniFBB7 (U+FBB7): B&lt;&lt;446.0,-58.0&gt;-&lt;488.0,-105.0&gt;-&lt;505.0,-150.0&gt;&gt;/B&lt;&lt;505.0,-150.0&gt;-&lt;504.0,-143.0&gt;-&lt;504.0,-137.0&gt;&gt; = 12.565348379907297

* uniFBB7 (U+FBB7): B&lt;&lt;571.0,-270.0&gt;-&lt;529.0,-225.0&gt;-&lt;512.0,-180.0&gt;&gt;/B&lt;&lt;512.0,-180.0&gt;-&lt;513.0,-186.0&gt;-&lt;513.0,-192.0&gt;&gt; = 11.233128526037627

* uniFBB8 (U+FBB8): B&lt;&lt;793.5,1000.0&gt;-&lt;751.0,1046.0&gt;-&lt;735.0,1092.0&gt;&gt;/B&lt;&lt;735.0,1092.0&gt;-&lt;737.0,1083.0&gt;-&lt;736.0,1075.0&gt;&gt; = 6.650200316659149

* uniFBB8 (U+FBB8): L&lt;&lt;729.0,1115.0&gt;--&lt;729.0,1114.0&gt;&gt;/B&lt;&lt;729.0,1114.0&gt;-&lt;728.0,1123.0&gt;-&lt;728.0,1132.0&gt;&gt; = 6.340191745909908

* uniFBB9 (U+FBB9): B&lt;&lt;619.5,9.0&gt;-&lt;577.0,55.0&gt;-&lt;560.0,101.0&gt;&gt;/B&lt;&lt;560.0,101.0&gt;-&lt;562.0,92.0&gt;-&lt;561.0,84.0&gt;&gt; = 7.753751379765042

* uniFBB9 (U+FBB9): L&lt;&lt;554.0,124.0&gt;--&lt;554.0,123.0&gt;&gt;/B&lt;&lt;554.0,123.0&gt;-&lt;553.0,132.0&gt;-&lt;553.0,141.0&gt;&gt; = 6.340191745909908

* uniFBBA (U+FBBA): B&lt;&lt;730.5,1557.0&gt;-&lt;772.0,1510.0&gt;-&lt;790.0,1465.0&gt;&gt;/B&lt;&lt;790.0,1465.0&gt;-&lt;789.0,1472.0&gt;-&lt;789.0,1478.0&gt;&gt; = 13.67130713219584

* uniFBBA (U+FBBA): B&lt;&lt;795.0,999.0&gt;-&lt;753.0,1044.0&gt;-&lt;736.0,1089.0&gt;&gt;/B&lt;&lt;736.0,1089.0&gt;-&lt;737.0,1083.0&gt;-&lt;736.0,1077.0&gt;&gt; = 11.233128526037627

* uniFBBA (U+FBBA): B&lt;&lt;844.0,1358.0&gt;-&lt;811.0,1397.0&gt;-&lt;797.0,1435.0&gt;&gt;/B&lt;&lt;797.0,1435.0&gt;-&lt;798.0,1429.0&gt;-&lt;797.0,1423.0&gt;&gt; = 10.762537223142443

* uniFBBB (U+FBBB): B&lt;&lt;457.0,-72.5&gt;-&lt;490.0,-113.0&gt;-&lt;505.0,-151.0&gt;&gt;/B&lt;&lt;505.0,-151.0&gt;-&lt;504.0,-144.0&gt;-&lt;504.0,-138.0&gt;&gt; = 13.410873564382426

* uniFBBB (U+FBBB): B&lt;&lt;506.5,287.0&gt;-&lt;548.0,240.0&gt;-&lt;566.0,195.0&gt;&gt;/B&lt;&lt;566.0,195.0&gt;-&lt;565.0,202.0&gt;-&lt;565.0,208.0&gt;&gt; = 13.67130713219584

* uniFBBB (U+FBBB): B&lt;&lt;571.0,-271.0&gt;-&lt;529.0,-226.0&gt;-&lt;512.0,-181.0&gt;&gt;/B&lt;&lt;512.0,-181.0&gt;-&lt;513.0,-187.0&gt;-&lt;513.0,-193.0&gt;&gt; = 11.233128526037627

* uniFBBB (U+FBBB): B&lt;&lt;620.5,88.0&gt;-&lt;588.0,127.0&gt;-&lt;573.0,165.0&gt;&gt;/B&lt;&lt;573.0,165.0&gt;-&lt;574.0,159.0&gt;-&lt;574.0,153.0&gt;&gt; = 12.078653710512796

* uniFBC0 (U+FBC0): L&lt;&lt;823.0,1614.0&gt;--&lt;760.0,1264.0&gt;&gt;/B&lt;&lt;760.0,1264.0&gt;-&lt;783.0,1365.0&gt;-&lt;846.0,1418.0&gt;&gt; = 2.624809149723495

* uniFBC1 (U+FBC1): L&lt;&lt;587.0,273.0&gt;--&lt;524.0,-77.0&gt;&gt;/B&lt;&lt;524.0,-77.0&gt;-&lt;547.0,24.0&gt;-&lt;610.0,77.0&gt;&gt; = 2.624809149723495

* uniFBD4 (U+FBD4): B&lt;&lt;706.0,1508.0&gt;-&lt;748.0,1461.0&gt;-&lt;765.0,1416.0&gt;&gt;/B&lt;&lt;765.0,1416.0&gt;-&lt;764.0,1423.0&gt;-&lt;764.0,1429.0&gt;&gt; = 12.565348379907297

* uniFBD4 (U+FBD4): B&lt;&lt;831.5,1296.0&gt;-&lt;790.0,1341.0&gt;-&lt;772.0,1386.0&gt;&gt;/B&lt;&lt;772.0,1386.0&gt;-&lt;773.0,1380.0&gt;-&lt;773.0,1374.0&gt;&gt; = 12.33908727832621

* uniFBD4 (U+FBD4): L&lt;&lt;1102.0,1429.0&gt;--&lt;1102.0,1426.0&gt;&gt;/L&lt;&lt;1102.0,1426.0&gt;--&lt;1118.0,1515.0&gt;&gt; = 10.191501850027691

* uniFBD4 (U+FBD4): L&lt;&lt;992.0,790.0&gt;--&lt;1099.0,1407.0&gt;&gt;/B&lt;&lt;1099.0,1407.0&gt;-&lt;1086.0,1376.0&gt;-&lt;1049.5,1339.5&gt;&gt; = 12.912604273903883

* uniFBD4 (U+FBD4): L&lt;&lt;992.0,793.0&gt;--&lt;992.0,790.0&gt;&gt;/L&lt;&lt;992.0,790.0&gt;--&lt;1099.0,1407.0&gt;&gt; = 9.838372068883682

* uniFBD5 (U+FBD5): B&lt;&lt;480.0,1508.0&gt;-&lt;522.0,1461.0&gt;-&lt;539.0,1416.0&gt;&gt;/B&lt;&lt;539.0,1416.0&gt;-&lt;538.0,1423.0&gt;-&lt;538.0,1429.0&gt;&gt; = 12.565348379907297

* uniFBD5 (U+FBD5): B&lt;&lt;605.5,1296.0&gt;-&lt;564.0,1341.0&gt;-&lt;546.0,1386.0&gt;&gt;/B&lt;&lt;546.0,1386.0&gt;-&lt;547.0,1380.0&gt;-&lt;547.0,1374.0&gt;&gt; = 12.33908727832621

* uniFBD6 (U+FBD6): B&lt;&lt;1002.0,801.0&gt;-&lt;960.0,846.0&gt;-&lt;943.0,891.0&gt;&gt;/B&lt;&lt;943.0,891.0&gt;-&lt;944.0,885.0&gt;-&lt;944.0,879.0&gt;&gt; = 11.233128526037627

* uniFBD6 (U+FBD6): B&lt;&lt;796.0,1208.0&gt;-&lt;801.0,1226.0&gt;-&lt;820.0,1252.0&gt;&gt;/L&lt;&lt;820.0,1252.0&gt;--&lt;588.0,1055.0&gt;&gt; = 13.505965319539056

* uniFBD6 (U+FBD6): B&lt;&lt;876.5,1013.0&gt;-&lt;918.0,966.0&gt;-&lt;936.0,921.0&gt;&gt;/B&lt;&lt;936.0,921.0&gt;-&lt;935.0,928.0&gt;-&lt;935.0,934.0&gt;&gt; = 13.67130713219584

* uniFBDF (U+FBDF): B&lt;&lt;795.0,1112.0&gt;-&lt;753.0,1157.0&gt;-&lt;736.0,1202.0&gt;&gt;/B&lt;&lt;736.0,1202.0&gt;-&lt;737.0,1196.0&gt;-&lt;736.0,1190.0&gt;&gt; = 11.233128526037627

* uniFBFE (U+FBFE): B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uniFBFF (U+FBFF): B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uniFCA1 (U+FCA1): B&lt;&lt;817.5,1926.0&gt;-&lt;859.0,1879.0&gt;-&lt;877.0,1834.0&gt;&gt;/B&lt;&lt;877.0,1834.0&gt;-&lt;876.0,1841.0&gt;-&lt;876.0,1847.0&gt;&gt; = 13.67130713219584

* uniFCA1 (U+FCA1): B&lt;&lt;943.0,1714.0&gt;-&lt;901.0,1759.0&gt;-&lt;884.0,1804.0&gt;&gt;/B&lt;&lt;884.0,1804.0&gt;-&lt;885.0,1798.0&gt;-&lt;885.0,1792.0&gt;&gt; = 11.233128526037627

* uniFCA2 (U+FCA2): B&lt;&lt;817.5,1926.0&gt;-&lt;859.0,1879.0&gt;-&lt;877.0,1834.0&gt;&gt;/B&lt;&lt;877.0,1834.0&gt;-&lt;876.0,1841.0&gt;-&lt;876.0,1847.0&gt;&gt; = 13.67130713219584

* uniFCA2 (U+FCA2): B&lt;&lt;943.0,1714.0&gt;-&lt;901.0,1759.0&gt;-&lt;884.0,1804.0&gt;&gt;/B&lt;&lt;884.0,1804.0&gt;-&lt;885.0,1798.0&gt;-&lt;885.0,1792.0&gt;&gt; = 11.233128526037627

* uniFDF2 (U+FDF2): B&lt;&lt;666.0,205.5&gt;-&lt;635.0,221.0&gt;-&lt;639.0,234.0&gt;&gt;/B&lt;&lt;639.0,234.0&gt;-&lt;631.0,219.0&gt;-&lt;596.5,204.5&gt;&gt; = 10.96975796680057

* uniFDF4 (U+FDF4): B&lt;&lt;441.5,211.5&gt;-&lt;418.0,228.0&gt;-&lt;424.0,245.0&gt;&gt;/B&lt;&lt;424.0,245.0&gt;-&lt;406.0,218.0&gt;-&lt;359.0,195.0&gt;&gt; = 14.25003269780357

* uniFDFA (U+FDFA): L&lt;&lt;58.0,259.0&gt;--&lt;58.0,244.0&gt;&gt;/B&lt;&lt;58.0,244.0&gt;-&lt;67.0,289.0&gt;-&lt;98.5,322.0&gt;&gt; = 11.309932474020195

* uniFDFA (U+FDFA): L&lt;&lt;596.0,485.0&gt;--&lt;603.0,522.0&gt;&gt;/B&lt;&lt;603.0,522.0&gt;-&lt;595.0,495.0&gt;-&lt;579.5,472.0&gt;&gt; = 5.791238358963932

* uniFDFA (U+FDFA): L&lt;&lt;937.0,461.0&gt;--&lt;939.0,459.0&gt;&gt;/B&lt;&lt;939.0,459.0&gt;-&lt;923.0,479.0&gt;-&lt;924.0,502.0&gt;&gt; = 6.340191745909908

* uniFDFB (U+FDFB): L&lt;&lt;178.0,371.0&gt;--&lt;194.0,394.0&gt;&gt;/B&lt;&lt;194.0,394.0&gt;-&lt;189.0,388.0&gt;-&lt;175.0,374.5&gt;&gt; = 4.981081935308452

* uniFDFB (U+FDFB): L&lt;&lt;674.0,429.0&gt;--&lt;673.0,424.0&gt;&gt;/L&lt;&lt;673.0,424.0&gt;--&lt;713.0,659.0&gt;&gt; = 1.6500393955779424

* uniFDFC (U+FDFC): L&lt;&lt;626.0,406.0&gt;--&lt;626.0,408.0&gt;&gt;/L&lt;&lt;626.0,408.0&gt;--&lt;592.0,215.0&gt;&gt; = 9.991043420169023

* uniFDFC (U+FDFC): L&lt;&lt;756.0,1143.0&gt;--&lt;746.0,1084.0&gt;&gt;/B&lt;&lt;746.0,1084.0&gt;-&lt;758.0,1126.0&gt;-&lt;786.5,1143.0&gt;&gt; = 6.325668101223985

* uniFDFD (U+FDFD): B&lt;&lt;559.0,583.0&gt;-&lt;563.0,587.0&gt;-&lt;561.0,588.0&gt;&gt;/B&lt;&lt;561.0,588.0&gt;-&lt;566.0,586.0&gt;-&lt;560.0,592.0&gt;&gt; = 4.763641690726066

* uniFE00 (U+FE00): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE00 (U+FE00): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE01 (U+FE01): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE01 (U+FE01): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE02 (U+FE02): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE02 (U+FE02): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE03 (U+FE03): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE03 (U+FE03): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE04 (U+FE04): B&lt;&lt;602.0,691.0&gt;-&lt;637.0,683.0&gt;-&lt;665.0,682.0&gt;&gt;/B&lt;&lt;665.0,682.0&gt;-&lt;628.0,674.0&gt;-&lt;594.0,654.0&gt;&gt; = 14.245877216268015

* uniFE04 (U+FE04): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE04 (U+FE04): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE04 (U+FE04): L&lt;&lt;641.0,854.0&gt;--&lt;666.0,877.0&gt;&gt;/L&lt;&lt;666.0,877.0&gt;--&lt;636.0,849.0&gt;&gt; = 0.411010019507171

* uniFE05 (U+FE05): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uniFE05 (U+FE05): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uniFE05 (U+FE05): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uniFE05 (U+FE05): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uniFE05 (U+FE05): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uniFE05 (U+FE05): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uniFE05 (U+FE05): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE05 (U+FE05): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uniFE05 (U+FE05): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uniFE05 (U+FE05): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uniFE05 (U+FE05): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE05 (U+FE05): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE05 (U+FE05): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uniFE05 (U+FE05): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE05 (U+FE05): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uniFE05 (U+FE05): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE05 (U+FE05): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uniFE05 (U+FE05): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE06 (U+FE06): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE06 (U+FE06): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE07 (U+FE07): B&lt;&lt;887.5,680.5&gt;-&lt;862.0,651.0&gt;-&lt;840.0,650.0&gt;&gt;/B&lt;&lt;840.0,650.0&gt;-&lt;865.0,645.0&gt;-&lt;884.5,606.5&gt;&gt; = 13.912494676519978

* uniFE07 (U+FE07): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uniFE07 (U+FE07): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uniFE07 (U+FE07): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uniFE07 (U+FE07): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uniFE07 (U+FE07): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uniFE07 (U+FE07): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uniFE07 (U+FE07): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE07 (U+FE07): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uniFE07 (U+FE07): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uniFE07 (U+FE07): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uniFE07 (U+FE07): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE07 (U+FE07): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE07 (U+FE07): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uniFE07 (U+FE07): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE07 (U+FE07): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uniFE07 (U+FE07): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE07 (U+FE07): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uniFE07 (U+FE07): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE08 (U+FE08): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uniFE08 (U+FE08): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uniFE08 (U+FE08): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uniFE08 (U+FE08): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uniFE08 (U+FE08): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uniFE08 (U+FE08): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uniFE08 (U+FE08): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE08 (U+FE08): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uniFE08 (U+FE08): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uniFE08 (U+FE08): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uniFE08 (U+FE08): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE08 (U+FE08): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE08 (U+FE08): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uniFE08 (U+FE08): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE08 (U+FE08): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uniFE08 (U+FE08): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE08 (U+FE08): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uniFE08 (U+FE08): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE09 (U+FE09): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uniFE09 (U+FE09): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uniFE09 (U+FE09): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uniFE09 (U+FE09): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uniFE09 (U+FE09): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uniFE09 (U+FE09): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uniFE09 (U+FE09): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE09 (U+FE09): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uniFE09 (U+FE09): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uniFE09 (U+FE09): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uniFE09 (U+FE09): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE09 (U+FE09): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE09 (U+FE09): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uniFE09 (U+FE09): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE09 (U+FE09): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uniFE09 (U+FE09): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE09 (U+FE09): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uniFE09 (U+FE09): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE0A (U+FE0A): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE0A (U+FE0A): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE0B (U+FE0B): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE0B (U+FE0B): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE0C (U+FE0C): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE0C (U+FE0C): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE0D (U+FE0D): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE0D (U+FE0D): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE0E (U+FE0E): B&lt;&lt;776.0,691.0&gt;-&lt;811.0,683.0&gt;-&lt;839.0,682.0&gt;&gt;/B&lt;&lt;839.0,682.0&gt;-&lt;802.0,674.0&gt;-&lt;768.0,654.0&gt;&gt; = 14.245877216268015

* uniFE0E (U+FE0E): L&lt;&lt;1154.0,981.0&gt;--&lt;1172.0,1086.0&gt;&gt;/B&lt;&lt;1172.0,1086.0&gt;-&lt;1145.0,1025.0&gt;-&lt;1084.5,982.5&gt;&gt; = 14.147702302525895

* uniFE0E (U+FE0E): L&lt;&lt;1187.0,1171.0&gt;--&lt;1187.0,1169.0&gt;&gt;/L&lt;&lt;1187.0,1169.0&gt;--&lt;1194.0,1210.0&gt;&gt; = 9.68878656036679

* uniFE0E (U+FE0E): L&lt;&lt;815.0,854.0&gt;--&lt;840.0,877.0&gt;&gt;/L&lt;&lt;840.0,877.0&gt;--&lt;810.0,849.0&gt;&gt; = 0.411010019507171

* uniFE0F (U+FE0F): L&lt;&lt;1074.0,1647.0&gt;--&lt;1200.0,1648.0&gt;&gt;/L&lt;&lt;1200.0,1648.0&gt;--&lt;1191.0,1648.0&gt;&gt; = 0.45471886169316617

* uniFE0F (U+FE0F): L&lt;&lt;1103.0,343.0&gt;--&lt;1107.0,359.0&gt;&gt;/L&lt;&lt;1107.0,359.0&gt;--&lt;1090.0,248.0&gt;&gt; = 5.328873196406038

* uniFE0F (U+FE0F): L&lt;&lt;1191.0,1648.0&gt;--&lt;1065.0,1647.0&gt;&gt;/L&lt;&lt;1065.0,1647.0&gt;--&lt;1074.0,1647.0&gt;&gt; = 0.45471886169316617

* uniFE0F (U+FE0F): L&lt;&lt;217.0,257.0&gt;--&lt;342.0,258.0&gt;&gt;/L&lt;&lt;342.0,258.0&gt;--&lt;332.0,257.0&gt;&gt; = 5.252236679499185

* uniFE0F (U+FE0F): L&lt;&lt;318.0,1636.0&gt;--&lt;304.0,1546.0&gt;&gt;/L&lt;&lt;304.0,1546.0&gt;--&lt;305.0,1561.0&gt;&gt; = 5.0277397259013075

* uniFE0F (U+FE0F): L&lt;&lt;332.0,257.0&gt;--&lt;208.0,256.0&gt;&gt;/L&lt;&lt;208.0,256.0&gt;--&lt;217.0,257.0&gt;&gt; = 5.878139024479216

* uniFE0F (U+FE0F): L&lt;&lt;419.0,257.0&gt;--&lt;547.0,258.0&gt;&gt;/L&lt;&lt;547.0,258.0&gt;--&lt;537.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE0F (U+FE0F): L&lt;&lt;462.0,1647.0&gt;--&lt;587.0,1648.0&gt;&gt;/L&lt;&lt;587.0,1648.0&gt;--&lt;578.0,1648.0&gt;&gt; = 0.4583564580000459

* uniFE0F (U+FE0F): L&lt;&lt;537.0,257.0&gt;--&lt;410.0,256.0&gt;&gt;/L&lt;&lt;410.0,256.0&gt;--&lt;419.0,257.0&gt;&gt; = 5.889053199122589

* uniFE0F (U+FE0F): L&lt;&lt;578.0,1648.0&gt;--&lt;453.0,1647.0&gt;&gt;/L&lt;&lt;453.0,1647.0&gt;--&lt;462.0,1647.0&gt;&gt; = 0.4583564580000459

* uniFE0F (U+FE0F): L&lt;&lt;624.0,257.0&gt;--&lt;752.0,258.0&gt;&gt;/L&lt;&lt;752.0,258.0&gt;--&lt;742.0,257.0&gt;&gt; = 5.2629789666391265

* uniFE0F (U+FE0F): L&lt;&lt;664.0,1647.0&gt;--&lt;792.0,1648.0&gt;&gt;/L&lt;&lt;792.0,1648.0&gt;--&lt;783.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE0F (U+FE0F): L&lt;&lt;742.0,257.0&gt;--&lt;615.0,256.0&gt;&gt;/L&lt;&lt;615.0,256.0&gt;--&lt;624.0,257.0&gt;&gt; = 5.889053199122589

* uniFE0F (U+FE0F): L&lt;&lt;783.0,1648.0&gt;--&lt;655.0,1647.0&gt;&gt;/L&lt;&lt;655.0,1647.0&gt;--&lt;664.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE0F (U+FE0F): L&lt;&lt;829.0,257.0&gt;--&lt;955.0,258.0&gt;&gt;/L&lt;&lt;955.0,258.0&gt;--&lt;945.0,257.0&gt;&gt; = 5.25587427580653

* uniFE0F (U+FE0F): L&lt;&lt;869.0,1647.0&gt;--&lt;997.0,1648.0&gt;&gt;/L&lt;&lt;997.0,1648.0&gt;--&lt;988.0,1648.0&gt;&gt; = 0.4476141708605809

* uniFE0F (U+FE0F): L&lt;&lt;945.0,257.0&gt;--&lt;820.0,256.0&gt;&gt;/L&lt;&lt;820.0,256.0&gt;--&lt;829.0,257.0&gt;&gt; = 5.881835287909446

* uniFE0F (U+FE0F): L&lt;&lt;988.0,1648.0&gt;--&lt;860.0,1647.0&gt;&gt;/L&lt;&lt;860.0,1647.0&gt;--&lt;869.0,1647.0&gt;&gt; = 0.4476141708605809

* uniFE84 (U+FE84): B&lt;&lt;567.5,1380.0&gt;-&lt;623.0,1407.0&gt;-&lt;680.0,1424.0&gt;&gt;/B&lt;&lt;680.0,1424.0&gt;-&lt;630.0,1416.0&gt;-&lt;598.0,1470.5&gt;&gt; = 7.5167036577946975

* uniFE86 (U+FE86): B&lt;&lt;399.0,956.0&gt;-&lt;454.0,983.0&gt;-&lt;511.0,1000.0&gt;&gt;/B&lt;&lt;511.0,1000.0&gt;-&lt;462.0,992.0&gt;-&lt;429.5,1046.5&gt;&gt; = 7.334378801416706

* uniFE88 (U+FE88): B&lt;&lt;275.5,-289.0&gt;-&lt;331.0,-262.0&gt;-&lt;387.0,-245.0&gt;&gt;/B&lt;&lt;387.0,-245.0&gt;-&lt;338.0,-253.0&gt;-&lt;306.0,-198.5&gt;&gt; = 7.614189346743762

* uniFE8A (U+FE8A): B&lt;&lt;384.0,884.0&gt;-&lt;439.0,911.0&gt;-&lt;496.0,928.0&gt;&gt;/B&lt;&lt;496.0,928.0&gt;-&lt;447.0,920.0&gt;-&lt;414.5,974.5&gt;&gt; = 7.334378801416706

* uniFE8B (U+FE8B): B&lt;&lt;435.0,1116.0&gt;-&lt;490.0,1143.0&gt;-&lt;547.0,1160.0&gt;&gt;/B&lt;&lt;547.0,1160.0&gt;-&lt;498.0,1152.0&gt;-&lt;465.5,1206.5&gt;&gt; = 7.334378801416706

* uniFE8C (U+FE8C): B&lt;&lt;438.0,1177.0&gt;-&lt;493.0,1204.0&gt;-&lt;550.0,1221.0&gt;&gt;/B&lt;&lt;550.0,1221.0&gt;-&lt;501.0,1213.0&gt;-&lt;468.5,1267.5&gt;&gt; = 7.334378801416706

* uniFE90 (U+FE90): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFE94 (U+FE94): B&lt;&lt;812.0,1407.0&gt;-&lt;770.0,1452.0&gt;-&lt;753.0,1497.0&gt;&gt;/B&lt;&lt;753.0,1497.0&gt;-&lt;754.0,1491.0&gt;-&lt;753.0,1485.0&gt;&gt; = 11.233128526037627

* uniFE96 (U+FE96): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFE96 (U+FE96): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uniFE97 (U+FE97): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uniFE98 (U+FE98): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uniFE9A (U+FE9A): B&lt;&lt;309.5,430.0&gt;-&lt;305.0,404.0&gt;-&lt;288.0,403.0&gt;&gt;/L&lt;&lt;288.0,403.0&gt;--&lt;933.0,398.0&gt;&gt; = 3.8106050965416993

* uniFE9A (U+FE9A): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uniFE9B (U+FE9B): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uniFE9C (U+FE9C): B&lt;&lt;726.5,1379.0&gt;-&lt;768.0,1332.0&gt;-&lt;785.0,1287.0&gt;&gt;/B&lt;&lt;785.0,1287.0&gt;-&lt;784.0,1294.0&gt;-&lt;785.0,1300.0&gt;&gt; = 12.565348379907297

* uniFEBA (U+FEBA): B&lt;&lt;999.5,504.5&gt;-&lt;929.0,415.0&gt;-&lt;817.0,395.0&gt;&gt;/L&lt;&lt;817.0,395.0&gt;--&lt;1295.0,402.0&gt;&gt; = 9.285672095801052

* uniFEBE (U+FEBE): B&lt;&lt;999.5,504.5&gt;-&lt;929.0,415.0&gt;-&lt;817.0,395.0&gt;&gt;/L&lt;&lt;817.0,395.0&gt;--&lt;1295.0,402.0&gt;&gt; = 9.285672095801052

* uniFEC2 (U+FEC2): L&lt;&lt;714.0,1503.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.163478407146162

* uniFEC3 (U+FEC3): L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uniFEC4 (U+FEC4): L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uniFEC6 (U+FEC6): L&lt;&lt;714.0,1503.0&gt;--&lt;555.0,602.0&gt;&gt;/B&lt;&lt;555.0,602.0&gt;-&lt;566.0,653.0&gt;-&lt;603.0,715.5&gt;&gt; = 2.163478407146162

* uniFEC7 (U+FEC7): L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uniFEC8 (U+FEC8): L&lt;&lt;706.0,1503.0&gt;--&lt;547.0,602.0&gt;&gt;/B&lt;&lt;547.0,602.0&gt;-&lt;558.0,653.0&gt;-&lt;595.0,715.5&gt;&gt; = 2.163478407146162

* uniFECB (U+FECB): L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uniFECF (U+FECF): L&lt;&lt;54.0,401.0&gt;--&lt;471.0,403.0&gt;&gt;/B&lt;&lt;471.0,403.0&gt;-&lt;434.0,408.0&gt;-&lt;427.5,453.5&gt;&gt; = 7.970849516696486

* uniFED4 (U+FED4): B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uniFED6 (U+FED6): B&lt;&lt;1025.0,1095.0&gt;-&lt;983.0,1140.0&gt;-&lt;966.0,1185.0&gt;&gt;/B&lt;&lt;966.0,1185.0&gt;-&lt;967.0,1179.0&gt;-&lt;966.0,1173.0&gt;&gt; = 11.233128526037627

* uniFED7 (U+FED7): B&lt;&lt;1066.0,1329.0&gt;-&lt;1024.0,1374.0&gt;-&lt;1007.0,1419.0&gt;&gt;/B&lt;&lt;1007.0,1419.0&gt;-&lt;1008.0,1413.0&gt;-&lt;1008.0,1407.0&gt;&gt; = 11.233128526037627

* uniFED7 (U+FED7): B&lt;&lt;941.0,1541.0&gt;-&lt;983.0,1494.0&gt;-&lt;1000.0,1449.0&gt;&gt;/B&lt;&lt;1000.0,1449.0&gt;-&lt;999.0,1456.0&gt;-&lt;999.0,1462.0&gt;&gt; = 12.565348379907297

* uniFED8 (U+FED8): B&lt;&lt;721.0,1492.0&gt;-&lt;763.0,1445.0&gt;-&lt;780.0,1400.0&gt;&gt;/B&lt;&lt;780.0,1400.0&gt;-&lt;779.0,1407.0&gt;-&lt;780.0,1413.0&gt;&gt; = 12.565348379907297

* uniFED8 (U+FED8): B&lt;&lt;891.0,517.5&gt;-&lt;829.0,440.0&gt;-&lt;767.0,393.0&gt;&gt;/B&lt;&lt;767.0,393.0&gt;-&lt;790.0,408.0&gt;-&lt;831.0,405.5&gt;&gt; = 4.053132933139351

* uniFEEB (U+FEEB): B&lt;&lt;413.0,401.0&gt;-&lt;457.0,399.0&gt;-&lt;493.0,390.0&gt;&gt;/B&lt;&lt;493.0,390.0&gt;-&lt;405.0,414.0&gt;-&lt;360.5,488.5&gt;&gt; = 1.2188752351313326

* uniFEEB (U+FEEB): B&lt;&lt;967.0,824.5&gt;-&lt;960.0,882.0&gt;-&lt;965.0,924.0&gt;&gt;/B&lt;&lt;965.0,924.0&gt;-&lt;947.0,810.0&gt;-&lt;903.0,703.5&gt;&gt; = 2.18365204045764

* uniFEEC (U+FEEC): B&lt;&lt;925.0,473.5&gt;-&lt;866.0,410.0&gt;-&lt;786.0,403.0&gt;&gt;/L&lt;&lt;786.0,403.0&gt;--&lt;1303.0,402.0&gt;&gt; = 5.111468017404124

* uniFEF2 (U+FEF2): B&lt;&lt;288.5,-753.0&gt;-&lt;330.0,-800.0&gt;-&lt;347.0,-845.0&gt;&gt;/B&lt;&lt;347.0,-845.0&gt;-&lt;346.0,-838.0&gt;-&lt;347.0,-832.0&gt;&gt; = 12.565348379907297

* uniFEF3 (U+FEF3): B&lt;&lt;476.5,-61.0&gt;-&lt;518.0,-108.0&gt;-&lt;535.0,-153.0&gt;&gt;/B&lt;&lt;535.0,-153.0&gt;-&lt;534.0,-146.0&gt;-&lt;535.0,-140.0&gt;&gt; = 12.565348379907297

* uniFEF4 (U+FEF4): B&lt;&lt;480.5,-61.0&gt;-&lt;522.0,-108.0&gt;-&lt;539.0,-153.0&gt;&gt;/B&lt;&lt;539.0,-153.0&gt;-&lt;538.0,-146.0&gt;-&lt;539.0,-140.0&gt;&gt; = 12.565348379907297

* uniFEF5 (U+FEF5): B&lt;&lt;822.0,435.0&gt;-&lt;780.0,400.0&gt;-&lt;732.0,400.0&gt;&gt;/L&lt;&lt;732.0,400.0&gt;--&lt;888.0,401.0&gt;&gt; = 0.3672756073381265

* uniFEF5 (U+FEF5): B&lt;&lt;879.0,455.0&gt;-&lt;878.0,487.0&gt;-&lt;891.0,514.0&gt;&gt;/B&lt;&lt;891.0,514.0&gt;-&lt;864.0,470.0&gt;-&lt;822.0,435.0&gt;&gt; = 5.824838124376952

* uniFEF7 (U+FEF7): B&lt;&lt;301.5,1380.0&gt;-&lt;357.0,1407.0&gt;-&lt;414.0,1424.0&gt;&gt;/B&lt;&lt;414.0,1424.0&gt;-&lt;364.0,1416.0&gt;-&lt;332.0,1470.5&gt;&gt; = 7.5167036577946975

* uniFEF7 (U+FEF7): B&lt;&lt;822.0,435.0&gt;-&lt;780.0,400.0&gt;-&lt;732.0,400.0&gt;&gt;/L&lt;&lt;732.0,400.0&gt;--&lt;888.0,401.0&gt;&gt; = 0.3672756073381265

* uniFEF7 (U+FEF7): B&lt;&lt;879.0,455.0&gt;-&lt;878.0,487.0&gt;-&lt;891.0,514.0&gt;&gt;/B&lt;&lt;891.0,514.0&gt;-&lt;864.0,470.0&gt;-&lt;822.0,435.0&gt;&gt; = 5.824838124376952

* uniFEF8 (U+FEF8): B&lt;&lt;239.5,1380.0&gt;-&lt;295.0,1407.0&gt;-&lt;352.0,1424.0&gt;&gt;/B&lt;&lt;352.0,1424.0&gt;-&lt;302.0,1416.0&gt;-&lt;270.0,1470.5&gt;&gt; = 7.5167036577946975

* uniFEF9 (U+FEF9): B&lt;&lt;275.5,-289.0&gt;-&lt;331.0,-262.0&gt;-&lt;387.0,-245.0&gt;&gt;/B&lt;&lt;387.0,-245.0&gt;-&lt;338.0,-253.0&gt;-&lt;306.0,-198.5&gt;&gt; = 7.614189346743762

* uniFEF9 (U+FEF9): B&lt;&lt;822.0,435.0&gt;-&lt;780.0,400.0&gt;-&lt;732.0,400.0&gt;&gt;/L&lt;&lt;732.0,400.0&gt;--&lt;888.0,401.0&gt;&gt; = 0.3672756073381265

* uniFEF9 (U+FEF9): B&lt;&lt;879.0,455.0&gt;-&lt;878.0,487.0&gt;-&lt;891.0,514.0&gt;&gt;/B&lt;&lt;891.0,514.0&gt;-&lt;864.0,470.0&gt;-&lt;822.0,435.0&gt;&gt; = 5.824838124376952

* uniFEFA (U+FEFA): B&lt;&lt;70.5,-289.0&gt;-&lt;126.0,-262.0&gt;-&lt;182.0,-245.0&gt;&gt;/B&lt;&lt;182.0,-245.0&gt;-&lt;133.0,-253.0&gt;-&lt;101.0,-198.5&gt;&gt; = 7.614189346743762

* uniFEFB (U+FEFB): B&lt;&lt;822.0,435.0&gt;-&lt;780.0,400.0&gt;-&lt;732.0,400.0&gt;&gt;/L&lt;&lt;732.0,400.0&gt;--&lt;888.0,401.0&gt;&gt; = 0.3672756073381265

* uniFEFB (U+FEFB): B&lt;&lt;879.0,455.0&gt;-&lt;878.0,487.0&gt;-&lt;891.0,514.0&gt;&gt;/B&lt;&lt;891.0,514.0&gt;-&lt;864.0,470.0&gt;-&lt;822.0,435.0&gt;&gt; = 5.824838124376952

* uogonek (U+0173): L&lt;&lt;863.0,50.0&gt;--&lt;906.0,189.0&gt;&gt;/B&lt;&lt;906.0,189.0&gt;-&lt;870.0,123.0&gt;-&lt;803.5,67.5&gt;&gt; = 11.420875109811552

* uring (U+016F): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* utilde (U+0169): L&lt;&lt;862.0,61.0&gt;--&lt;914.0,186.0&gt;&gt;/B&lt;&lt;914.0,186.0&gt;-&lt;874.0,121.0&gt;-&lt;806.0,66.5&gt;&gt; = 9.020191714883174

* wasla_ar: B&lt;&lt;719.0,1483.5&gt;-&lt;726.0,1460.0&gt;-&lt;722.0,1450.0&gt;&gt;/B&lt;&lt;722.0,1450.0&gt;-&lt;776.0,1560.0&gt;-&lt;877.0,1636.0&gt;&gt; = 4.345431749229051

* xi (U+03BE): B&lt;&lt;446.5,1024.0&gt;-&lt;468.0,1059.0&gt;-&lt;505.0,1064.0&gt;&gt;/B&lt;&lt;505.0,1064.0&gt;-&lt;450.0,1066.0&gt;-&lt;404.5,1093.5&gt;&gt; = 9.778617001747428

* zero.slash: L&lt;&lt;591.0,1071.0&gt;--&lt;871.0,362.0&gt;&gt;/B&lt;&lt;871.0,362.0&gt;-&lt;860.0,425.0&gt;-&lt;877.5,498.0&gt;&gt; = 11.645991822355471

* zero.slash: L&lt;&lt;702.0,187.0&gt;--&lt;420.0,900.0&gt;&gt;/B&lt;&lt;420.0,900.0&gt;-&lt;434.0,844.0&gt;-&lt;419.5,780.0&gt;&gt; = 7.543144249536517
</code></pre>
 [code: found-jaggy-segments]



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

<details><summary>[14] CourierBadi-Italic.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;Version 0.900; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: lira	Contours detected: 2	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2

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

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* sigma1 (U+03C2): B&lt;&lt;1129.0,854.0&gt;-&lt;1129.0,845.0&gt;-&lt;1127.0,852.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: L&lt;&lt;311.0,1165.0&gt;--&lt;311.0,1165.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.init: L&lt;&lt;272.0,842.0&gt;--&lt;272.0,842.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.medi: B&lt;&lt;255.0,1165.0&gt;-&lt;257.0,1165.0&gt;-&lt;254.0,1159.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.medi: B&lt;&lt;204.0,876.0&gt;-&lt;203.0,876.0&gt;-&lt;204.0,881.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.medi: B&lt;&lt;212.0,842.0&gt;-&lt;214.0,842.0&gt;-&lt;211.0,833.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.medi: B&lt;&lt;162.0,553.0&gt;-&lt;159.0,553.0&gt;-&lt;163.0,561.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D (U+077D): L&lt;&lt;903.0,1516.0&gt;--&lt;907.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.fina: L&lt;&lt;810.0,1516.0&gt;--&lt;814.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.init: L&lt;&lt;1061.0,1516.0&gt;--&lt;1065.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

* uni203B (U+203B): B&lt;&lt;607.0,839.0&gt;-&lt;615.0,820.0&gt;-&lt;632.0,808.0&gt;&gt; has the same coordinates as a previous segment.

* uni203B (U+203B): B&lt;&lt;821.0,579.0&gt;-&lt;829.0,562.0&gt;-&lt;844.0,551.0&gt;&gt; has the same coordinates as a previous segment.
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
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, canadian-aboriginal, hebrew, tai-le, todhri, old-permic, malayalam, math, syriac, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
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
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, math, cherokee</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, thai, sunuwar, cherokee, gothic, syriac, caucasian-albanian</li>
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
<li>U+060C ARABIC COMMA: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
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
<li>U+061B ARABIC SEMICOLON: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: arabic, syriac, thaana</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: arabic, yezidi, hanifi-rohingya, garay, adlam, syriac, nko, thaana</li>
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
<li>U+0640 ARABIC TATWEEL: try adding one of: arabic, old-uyghur, mandaic, psalter-pahlavi, hanifi-rohingya, adlam, manichaean, syriac, sogdian</li>
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
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: arabic, yezidi, hanifi-rohingya, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: arabic, syriac, nko, thaana</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: arabic, syriac, thaana</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: arabic, syriac, thaana</li>
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
<li>U+06D4 ARABIC FULL STOP: try adding one of: arabic, hanifi-rohingya, yezidi</li>
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
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, dogra, tagbanwa, duployan, batak, hatran, mandaic, cham, khojki, hanunoo, hebrew, javanese, masaram-gondi, mongolian, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, siddham, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, old-hungarian, dogra, tagbanwa, duployan, batak, mandaic, masaram-gondi, cham, khojki, hanunoo, hebrew, javanese, mongolian, siddham, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: arabic, hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+2010 HYPHEN: try adding one of: arabic, cham, yi, hebrew, sundanese, lisu, kharoshthi, armenian, sora-sompeng, syloti-nagri, kaithi, kayah-li, coptic</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
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
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: telugu, math, manichaean, sharada, tamil, duployan, batak, kharoshthi, sogdian, gurmukhi, symbols, saurashtra, balinese, soyombo, khudawadi, gujarati, bhaiksuki, myanmar, nko, grantha, lepcha, khojki, caucasian-albanian, gunjala-gondi, bengali, mende-kikakui, buginese, tai-viet, dogra, tagbanwa, siddham, cham, mongolian, hanunoo, zanabazar-square, bassa-vah, limbu, tirhuta, tibetan, warang-citi, marchen, new-tai-lue, hanifi-rohingya, syloti-nagri, canadian-aboriginal, pahawh-hmong, tai-tham, masaram-gondi, mandaic, yi, javanese, hebrew, adlam, rejang, tifinagh, sundanese, phags-pa, malayalam, devanagari, elbasan, syriac, kayah-li, psalter-pahlavi, music, oriya, tai-le, armenian, tagalog, sinhala, mahajani, meetei-mayek, old-permic, brahmi, osage, thai, takri, modi, kaithi, newa, wancho, chakma, khmer, coptic, miao, buhid, ahom, lao, kannada, thaana</li>
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
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: arabic, thaana</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: arabic, thaana</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, phags-pa, yi</li>
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
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* angleright (U+232A): L&lt;&lt;551.0,1348.0&gt;--&lt;677.0,1079.0&gt;&gt; -&gt; L&lt;&lt;677.0,1079.0&gt;--&lt;825.0,768.0&gt;&gt;

* angleright (U+232A): L&lt;&lt;840.0,563.0&gt;--&lt;370.0,-6.0&gt;&gt; -&gt; L&lt;&lt;370.0,-6.0&gt;--&lt;283.0,-111.0&gt;&gt;

* psi (U+03C8): L&lt;&lt;396.0,-424.0&gt;--&lt;429.0,-215.0&gt;&gt; -&gt; L&lt;&lt;429.0,-215.0&gt;--&lt;466.0,-6.0&gt;&gt;

* psi (U+03C8): L&lt;&lt;491.0,137.0&gt;--&lt;591.0,705.0&gt;&gt; -&gt; L&lt;&lt;591.0,705.0&gt;--&lt;649.0,1030.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;732.0,1108.0&gt;--&lt;648.0,887.0&gt;&gt; -&gt; L&lt;&lt;648.0,887.0&gt;--&lt;510.0,553.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;739.0,891.0&gt;--&lt;734.0,1014.0&gt;&gt; -&gt; L&lt;&lt;734.0,1014.0&gt;--&lt;732.0,1108.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;764.0,489.0&gt;--&lt;739.0,891.0&gt;&gt; -&gt; L&lt;&lt;739.0,891.0&gt;--&lt;734.0,1014.0&gt;&gt;

* uni046B (U+046B): L&lt;&lt;512.0,756.0&gt;--&lt;594.0,621.0&gt;&gt; -&gt; L&lt;&lt;594.0,621.0&gt;--&lt;627.0,563.0&gt;&gt;

* uni046C (U+046C): L&lt;&lt;372.0,127.0&gt;--&lt;510.0,479.0&gt;&gt; -&gt; L&lt;&lt;510.0,479.0&gt;--&lt;536.0,543.0&gt;&gt;

* uni046D (U+046D): L&lt;&lt;368.0,127.0&gt;--&lt;472.0,338.0&gt;&gt; -&gt; L&lt;&lt;472.0,338.0&gt;--&lt;493.0,379.0&gt;&gt;

* uni046D (U+046D): L&lt;&lt;472.0,338.0&gt;--&lt;493.0,379.0&gt;&gt; -&gt; L&lt;&lt;493.0,379.0&gt;--&lt;521.0,424.0&gt;&gt;

* uni0475 (U+0475): L&lt;&lt;463.0,756.0&gt;--&lt;527.0,225.0&gt;&gt; -&gt; L&lt;&lt;527.0,225.0&gt;--&lt;535.0,143.0&gt;&gt;

* uni0477 (U+0477): L&lt;&lt;465.0,756.0&gt;--&lt;532.0,225.0&gt;&gt; -&gt; L&lt;&lt;532.0,225.0&gt;--&lt;537.0,143.0&gt;&gt;

* uni0478 (U+0478): L&lt;&lt;542.0,1124.0&gt;--&lt;652.0,840.0&gt;&gt; -&gt; L&lt;&lt;652.0,840.0&gt;--&lt;674.0,768.0&gt;&gt;

* uni0478 (U+0478): L&lt;&lt;674.0,768.0&gt;--&lt;717.0,838.0&gt;&gt; -&gt; L&lt;&lt;717.0,838.0&gt;--&lt;929.0,1124.0&gt;&gt;

* uni0482 (U+0482): L&lt;&lt;472.0,227.0&gt;--&lt;562.0,250.0&gt;&gt; -&gt; L&lt;&lt;562.0,250.0&gt;--&lt;661.0,268.0&gt;&gt;

* uni0495 (U+0495): L&lt;&lt;524.0,547.0&gt;--&lt;641.0,547.0&gt;&gt; -&gt; L&lt;&lt;641.0,547.0&gt;--&lt;721.0,545.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;501.0,127.0&gt;--&lt;543.0,365.0&gt;&gt; -&gt; L&lt;&lt;543.0,365.0&gt;--&lt;547.0,399.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;669.0,401.0&gt;--&lt;660.0,365.0&gt;&gt; -&gt; L&lt;&lt;660.0,365.0&gt;--&lt;618.0,127.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;805.0,598.0&gt;--&lt;686.0,430.0&gt;&gt; -&gt; L&lt;&lt;686.0,430.0&gt;--&lt;669.0,401.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;499.0,127.0&gt;--&lt;524.0,266.0&gt;&gt; -&gt; L&lt;&lt;524.0,266.0&gt;--&lt;527.0,293.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;727.0,756.0&gt;--&lt;689.0,539.0&gt;&gt; -&gt; L&lt;&lt;689.0,539.0&gt;--&lt;683.0,492.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;758.0,418.0&gt;--&lt;666.0,315.0&gt;&gt; -&gt; L&lt;&lt;666.0,315.0&gt;--&lt;650.0,295.0&gt;&gt;

* uni0499 (U+0499): L&lt;&lt;465.0,117.0&gt;--&lt;504.0,117.0&gt;&gt; -&gt; L&lt;&lt;504.0,117.0&gt;--&lt;528.0,115.0&gt;&gt;

* uni049C (U+049C): L&lt;&lt;641.0,813.0&gt;--&lt;675.0,844.0&gt;&gt; -&gt; L&lt;&lt;675.0,844.0&gt;--&lt;946.0,1124.0&gt;&gt;

* uni049E (U+049E): L&lt;&lt;463.0,942.0&gt;--&lt;410.0,639.0&gt;&gt; -&gt; L&lt;&lt;410.0,639.0&gt;--&lt;402.0,584.0&gt;&gt;

* uni04A0 (U+04A0): L&lt;&lt;541.0,399.0&gt;--&lt;533.0,365.0&gt;&gt; -&gt; L&lt;&lt;533.0,365.0&gt;--&lt;491.0,127.0&gt;&gt;

* uni04A0 (U+04A0): L&lt;&lt;710.0,612.0&gt;--&lt;563.0,430.0&gt;&gt; -&gt; L&lt;&lt;563.0,430.0&gt;--&lt;541.0,399.0&gt;&gt;

* uni04C5 (U+04C5): L&lt;&lt;590.0,764.0&gt;--&lt;582.0,733.0&gt;&gt; -&gt; L&lt;&lt;582.0,733.0&gt;--&lt;576.0,696.0&gt;&gt;

* uni04C5 (U+04C5): L&lt;&lt;636.0,1028.0&gt;--&lt;590.0,764.0&gt;&gt; -&gt; L&lt;&lt;590.0,764.0&gt;--&lt;582.0,733.0&gt;&gt;

* uni04CD (U+04CD): L&lt;&lt;837.0,127.0&gt;--&lt;1001.0,1055.0&gt;&gt; -&gt; L&lt;&lt;1001.0,1055.0&gt;--&lt;1008.0,1108.0&gt;&gt;

* uni0512 (U+0512): L&lt;&lt;590.0,764.0&gt;--&lt;582.0,733.0&gt;&gt; -&gt; L&lt;&lt;582.0,733.0&gt;--&lt;576.0,696.0&gt;&gt;

* uni0512 (U+0512): L&lt;&lt;636.0,1028.0&gt;--&lt;590.0,764.0&gt;&gt; -&gt; L&lt;&lt;590.0,764.0&gt;--&lt;582.0,733.0&gt;&gt;

* uni06CD (U+06CD): L&lt;&lt;443.0,619.0&gt;--&lt;443.0,618.0&gt;&gt; -&gt; L&lt;&lt;443.0,618.0&gt;--&lt;443.0,616.0&gt;&gt;

* uni06CD.fina: L&lt;&lt;384.0,283.0&gt;--&lt;384.0,282.0&gt;&gt; -&gt; L&lt;&lt;384.0,282.0&gt;--&lt;384.0,281.0&gt;&gt;

* uni06E9 (U+06E9): L&lt;&lt;801.0,678.0&gt;--&lt;800.0,672.0&gt;&gt; -&gt; L&lt;&lt;800.0,672.0&gt;--&lt;787.0,598.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;482.0,1092.0&gt;--&lt;547.0,1092.0&gt;&gt; -&gt; L&lt;&lt;547.0,1092.0&gt;--&lt;547.0,1092.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;547.0,1092.0&gt;--&lt;547.0,1092.0&gt;&gt; -&gt; L&lt;&lt;547.0,1092.0&gt;--&lt;648.0,1092.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;983.0,1092.0&gt;--&lt;998.0,1092.0&gt;&gt; -&gt; L&lt;&lt;998.0,1092.0&gt;--&lt;998.0,1092.0&gt;&gt;

* uni08D4 (U+08D4): L&lt;&lt;998.0,1092.0&gt;--&lt;998.0,1092.0&gt;&gt; -&gt; L&lt;&lt;998.0,1092.0&gt;--&lt;1027.0,1092.0&gt;&gt;

* uni08DB (U+08DB): L&lt;&lt;1062.0,1063.0&gt;--&lt;1063.0,1063.0&gt;&gt; -&gt; L&lt;&lt;1063.0,1063.0&gt;--&lt;1063.0,1063.0&gt;&gt;

* uni08DB (U+08DB): L&lt;&lt;1063.0,1063.0&gt;--&lt;1063.0,1063.0&gt;&gt; -&gt; L&lt;&lt;1063.0,1063.0&gt;--&lt;1070.0,1063.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;530.0,1093.0&gt;--&lt;539.0,1093.0&gt;&gt; -&gt; L&lt;&lt;539.0,1093.0&gt;--&lt;539.0,1093.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;539.0,1093.0&gt;--&lt;539.0,1093.0&gt;&gt; -&gt; L&lt;&lt;539.0,1093.0&gt;--&lt;541.0,1093.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;539.0,1093.0&gt;--&lt;541.0,1093.0&gt;&gt; -&gt; L&lt;&lt;541.0,1093.0&gt;--&lt;559.0,1093.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;551.0,1046.0&gt;--&lt;532.0,1046.0&gt;&gt; -&gt; L&lt;&lt;532.0,1046.0&gt;--&lt;531.0,1046.0&gt;&gt;

* uni08DC (U+08DC): L&lt;&lt;843.0,1093.0&gt;--&lt;891.0,1093.0&gt;&gt; -&gt; L&lt;&lt;891.0,1093.0&gt;--&lt;891.0,1093.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;1027.0,1046.0&gt;--&lt;716.0,1046.0&gt;&gt; -&gt; L&lt;&lt;716.0,1046.0&gt;--&lt;715.0,1046.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;714.0,1093.0&gt;--&lt;723.0,1093.0&gt;&gt; -&gt; L&lt;&lt;723.0,1093.0&gt;--&lt;723.0,1093.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;723.0,1093.0&gt;--&lt;723.0,1093.0&gt;&gt; -&gt; L&lt;&lt;723.0,1093.0&gt;--&lt;725.0,1093.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;723.0,1093.0&gt;--&lt;725.0,1093.0&gt;&gt; -&gt; L&lt;&lt;725.0,1093.0&gt;--&lt;1013.0,1093.0&gt;&gt;

* uni203D (U+203D): L&lt;&lt;580.0,618.0&gt;--&lt;617.0,848.0&gt;&gt; -&gt; L&lt;&lt;617.0,848.0&gt;--&lt;659.0,1137.0&gt;&gt;

* uni203D (U+203D): L&lt;&lt;814.0,1135.0&gt;--&lt;788.0,999.0&gt;&gt; -&gt; L&lt;&lt;788.0,999.0&gt;--&lt;754.0,829.0&gt;&gt;

* uni2052 (U+2052): L&lt;&lt;185.0,162.0&gt;--&lt;281.0,297.0&gt;&gt; -&gt; L&lt;&lt;281.0,297.0&gt;--&lt;890.0,1145.0&gt;&gt;

* uni2052 (U+2052): L&lt;&lt;281.0,297.0&gt;--&lt;890.0,1145.0&gt;&gt; -&gt; L&lt;&lt;890.0,1145.0&gt;--&lt;1037.0,1348.0&gt;&gt;

* uni2E18 (U+2E18): L&lt;&lt;368.0,-338.0&gt;--&lt;396.0,-203.0&gt;&gt; -&gt; L&lt;&lt;396.0,-203.0&gt;--&lt;428.0,-33.0&gt;&gt;

* uni2E18 (U+2E18): L&lt;&lt;602.0,178.0&gt;--&lt;566.0,-51.0&gt;&gt; -&gt; L&lt;&lt;566.0,-51.0&gt;--&lt;524.0,-340.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* Mu (U+039C): L&lt;&lt;837.0,125.0&gt;--&lt;1009.0,1102.0&gt;&gt;/B&lt;&lt;1009.0,1102.0&gt;-&lt;999.0,1075.0&gt;-&lt;972.0,1018.5&gt;&gt; = 10.338577199564888

* uni0466 (U+0466): L&lt;&lt;760.0,553.0&gt;--&lt;764.0,489.0&gt;&gt;/L&lt;&lt;764.0,489.0&gt;--&lt;739.0,891.0&gt;&gt; = 0.01774687243908398

* uni0468 (U+0468): B&lt;&lt;872.5,960.0&gt;-&lt;880.0,1042.0&gt;-&lt;891.0,1108.0&gt;&gt;/B&lt;&lt;891.0,1108.0&gt;-&lt;859.0,960.0&gt;-&lt;818.0,824.0&gt;&gt; = 2.738146519354986

* uni0474 (U+0474): B&lt;&lt;510.0,288.5&gt;-&lt;510.0,196.0&gt;-&lt;506.0,143.0&gt;&gt;/B&lt;&lt;506.0,143.0&gt;-&lt;516.0,187.0&gt;-&lt;551.5,286.0&gt;&gt; = 8.48823854542108

* uni0476 (U+0476): B&lt;&lt;509.5,286.5&gt;-&lt;510.0,195.0&gt;-&lt;506.0,143.0&gt;&gt;/B&lt;&lt;506.0,143.0&gt;-&lt;515.0,180.0&gt;-&lt;544.0,263.5&gt;&gt; = 9.272601777200324

* uni048A (U+048A): L&lt;&lt;481.0,1124.0&gt;--&lt;331.0,270.0&gt;&gt;/B&lt;&lt;331.0,270.0&gt;-&lt;351.0,329.0&gt;-&lt;505.5,529.5&gt;&gt; = 8.763742651450915

* uni048A (U+048A): L&lt;&lt;810.0,127.0&gt;--&lt;961.0,981.0&gt;&gt;/B&lt;&lt;961.0,981.0&gt;-&lt;950.0,949.0&gt;-&lt;900.5,878.0&gt;&gt; = 8.943292419114242

* uni04CD (U+04CD): B&lt;&lt;460.5,1044.0&gt;-&lt;456.0,1086.0&gt;-&lt;455.0,1108.0&gt;&gt;/L&lt;&lt;455.0,1108.0&gt;--&lt;282.0,127.0&gt;&gt; = 12.603878154295307

* uni04CD (U+04CD): L&lt;&lt;1001.0,1055.0&gt;--&lt;1008.0,1108.0&gt;&gt;/B&lt;&lt;1008.0,1108.0&gt;-&lt;1001.0,1087.0&gt;-&lt;975.5,1032.0&gt;&gt; = 10.911128384283376

* uni0620 (U+0620): B&lt;&lt;591.0,21.0&gt;-&lt;604.0,21.0&gt;-&lt;617.0,20.0&gt;&gt;/B&lt;&lt;617.0,20.0&gt;-&lt;572.0,14.0&gt;-&lt;522.0,12.0&gt;&gt; = 11.993348723586953

* uni0620 (U+0620): B&lt;&lt;774.0,-81.0&gt;-&lt;727.0,9.0&gt;-&lt;617.0,20.0&gt;&gt;/B&lt;&lt;617.0,20.0&gt;-&lt;732.0,35.0&gt;-&lt;800.0,76.0&gt;&gt; = 13.142001108672124

* uni077D (U+077D): L&lt;&lt;903.0,1516.0&gt;--&lt;907.0,1515.0&gt;&gt;/B&lt;&lt;907.0,1515.0&gt;-&lt;902.0,1515.0&gt;-&lt;903.0,1516.0&gt;&gt; = 14.036243467926484

* uni077D.fina: L&lt;&lt;810.0,1516.0&gt;--&lt;814.0,1515.0&gt;&gt;/B&lt;&lt;814.0,1515.0&gt;-&lt;809.0,1515.0&gt;-&lt;810.0,1516.0&gt;&gt; = 14.036243467926484

* uni077D.init: L&lt;&lt;1061.0,1516.0&gt;--&lt;1065.0,1515.0&gt;&gt;/B&lt;&lt;1065.0,1515.0&gt;-&lt;1060.0,1515.0&gt;-&lt;1061.0,1516.0&gt;&gt; = 14.036243467926484

* uni08DB (U+08DB): L&lt;&lt;1053.0,1028.0&gt;--&lt;1053.0,1028.0&gt;&gt;/B&lt;&lt;1053.0,1028.0&gt;-&lt;1034.0,1029.0&gt;-&lt;1024.5,1038.5&gt;&gt; = 3.012787504183286

* uni08DC (U+08DC): L&lt;&lt;1009.0,1044.0&gt;--&lt;1009.0,1044.0&gt;&gt;/B&lt;&lt;1009.0,1044.0&gt;-&lt;977.0,1045.0&gt;-&lt;965.0,1059.0&gt;&gt; = 1.789910608246076

* uni08DD (U+08DD): L&lt;&lt;644.0,1047.0&gt;--&lt;644.0,1047.0&gt;&gt;/B&lt;&lt;644.0,1047.0&gt;-&lt;614.0,1049.0&gt;-&lt;602.0,1062.5&gt;&gt; = 3.8140748342903783
</code></pre>
 [code: found-jaggy-segments]



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

<details><summary>[14] CourierBadi-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;Version 0.900; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: hookabovecomb	Contours detected: 2	Expected: 1

- Glyph name: iotatonos	Contours detected: 1	Expected: 2

- Glyph name: sigma1	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 4	Expected: 2

- Glyph name: uni0428	Contours detected: 3	Expected: 1

- Glyph name: uni0429	Contours detected: 3	Expected: 1

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni0436	Contours detected: 3	Expected: 1

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni0466	Contours detected: 4	Expected: 2

- Glyph name: uni0467	Contours detected: 4	Expected: 2

- Glyph name: uni0468	Contours detected: 3	Expected: 2

- Glyph name: uni0469	Contours detected: 5	Expected: 2

- Glyph name: uni046C	Contours detected: 3	Expected: 2

- Glyph name: uni046D	Contours detected: 3	Expected: 2

- Glyph name: uni046E	Contours detected: 1	Expected: 2

- Glyph name: uni046F	Contours detected: 1	Expected: 2

- Glyph name: uni0476	Contours detected: 2	Expected: 3

- Glyph name: uni0477	Contours detected: 2	Expected: 3

- Glyph name: uni0478	Contours detected: 2	Expected: 3

- Glyph name: uni0479	Contours detected: 2	Expected: 3

- Glyph name: uni048C	Contours detected: 4	Expected: 2

- Glyph name: uni0497	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni049D	Contours detected: 2	Expected: 1

- Glyph name: uni049E	Contours detected: 3	Expected: 1

- Glyph name: uni04A1	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 3	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C2	Contours detected: 4	Expected: 2

- Glyph name: uni04DD	Contours detected: 5	Expected: 3

- Glyph name: uni04F2	Contours detected: 2	Expected: 3

- Glyph name: uni04F3	Contours detected: 2	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

- Glyph name: uni1EA4	Contours detected: 3	Expected: 4

- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

- Glyph name: uni1EAF	Contours detected: 3	Expected: 4

- Glyph name: uni1EB4	Contours detected: 3	Expected: 4

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni1EBE	Contours detected: 2	Expected: 3

- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

- Glyph name: uni1ECC	Contours detected: 2	Expected: 3

- Glyph name: uni1ECD	Contours detected: 2	Expected: 3

- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

- Glyph name: uni1ED0	Contours detected: 3	Expected: 4

- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

- Glyph name: uni1ED8	Contours detected: 3	Expected: 4

- Glyph name: uni1ED9	Contours detected: 3	Expected: 4

- Glyph name: uni1EDD	Contours detected: 2	Expected: 3

- Glyph name: uni1EDE	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EE4	Contours detected: 1	Expected: 2

- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

- Glyph name: uni1EED	Contours detected: 3	Expected: 2

- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

- Glyph name: uni1F02	Contours detected: 3	Expected: 4

- Glyph name: uni1F04	Contours detected: 3	Expected: 4

- Glyph name: uni1F05	Contours detected: 3	Expected: 4

- Glyph name: uni1F0A	Contours detected: 3	Expected: 4

- Glyph name: uni1F0C	Contours detected: 3	Expected: 4

- Glyph name: uni1F0D	Contours detected: 3	Expected: 4

- Glyph name: uni1F12	Contours detected: 2	Expected: 3

- Glyph name: uni1F14	Contours detected: 2	Expected: 3

- Glyph name: uni1F15	Contours detected: 2	Expected: 3

- Glyph name: uni1F1A	Contours detected: 2	Expected: 3

- Glyph name: uni1F1C	Contours detected: 2	Expected: 3

- Glyph name: uni1F1D	Contours detected: 2	Expected: 3

- Glyph name: uni1F22	Contours detected: 2	Expected: 3

- Glyph name: uni1F24	Contours detected: 2	Expected: 3

- Glyph name: uni1F25	Contours detected: 2	Expected: 3

- Glyph name: uni1F2A	Contours detected: 2	Expected: 3

- Glyph name: uni1F2C	Contours detected: 2	Expected: 3

- Glyph name: uni1F2D	Contours detected: 2	Expected: 3

- Glyph name: uni1F30	Contours detected: 1	Expected: 2

- Glyph name: uni1F31	Contours detected: 1	Expected: 2

- Glyph name: uni1F32	Contours detected: 2	Expected: 3

- Glyph name: uni1F34	Contours detected: 2	Expected: 3

- Glyph name: uni1F35	Contours detected: 2	Expected: 3

- Glyph name: uni1F36	Contours detected: 2	Expected: 3

- Glyph name: uni1F3A	Contours detected: 2	Expected: 3

- Glyph name: uni1F3C	Contours detected: 2	Expected: 3

- Glyph name: uni1F3D	Contours detected: 2	Expected: 3

- Glyph name: uni1F42	Contours detected: 3	Expected: 4

- Glyph name: uni1F44	Contours detected: 3	Expected: 4

- Glyph name: uni1F45	Contours detected: 3	Expected: 4

- Glyph name: uni1F4A	Contours detected: 3	Expected: 4

- Glyph name: uni1F4C	Contours detected: 3	Expected: 4

- Glyph name: uni1F4D	Contours detected: 3	Expected: 4

- Glyph name: uni1F52	Contours detected: 2	Expected: 3

- Glyph name: uni1F54	Contours detected: 2	Expected: 3

- Glyph name: uni1F55	Contours detected: 2	Expected: 3

- Glyph name: uni1F5D	Contours detected: 2	Expected: 3

- Glyph name: uni1F62	Contours detected: 2	Expected: 3

- Glyph name: uni1F64	Contours detected: 2	Expected: 3

- Glyph name: uni1F65	Contours detected: 2	Expected: 3

- Glyph name: uni1F6A	Contours detected: 2	Expected: 3

- Glyph name: uni1F6C	Contours detected: 2	Expected: 3

- Glyph name: uni1F6D	Contours detected: 2	Expected: 3

- Glyph name: uni1F70	Contours detected: 4	Expected: 3

- Glyph name: uni1F71	Contours detected: 4	Expected: 3

- Glyph name: uni1F76	Contours detected: 1	Expected: 2

- Glyph name: uni1F77	Contours detected: 1	Expected: 2

- Glyph name: uni1F82	Contours detected: 4	Expected: 5

- Glyph name: uni1F84	Contours detected: 4	Expected: 5

- Glyph name: uni1F85	Contours detected: 4	Expected: 5

- Glyph name: uni1F8A	Contours detected: 4	Expected: 5

- Glyph name: uni1F8C	Contours detected: 4	Expected: 5

- Glyph name: uni1F8D	Contours detected: 4	Expected: 5

- Glyph name: uni1F92	Contours detected: 3	Expected: 4

- Glyph name: uni1F94	Contours detected: 3	Expected: 4

- Glyph name: uni1F95	Contours detected: 3	Expected: 4

- Glyph name: uni1F9A	Contours detected: 3	Expected: 4

- Glyph name: uni1F9C	Contours detected: 3	Expected: 4

- Glyph name: uni1F9D	Contours detected: 3	Expected: 4

- Glyph name: uni1FA2	Contours detected: 3	Expected: 4

- Glyph name: uni1FA4	Contours detected: 3	Expected: 4

- Glyph name: uni1FA5	Contours detected: 3	Expected: 4

- Glyph name: uni1FAA	Contours detected: 3	Expected: 4

- Glyph name: uni1FAC	Contours detected: 3	Expected: 4

- Glyph name: uni1FAD	Contours detected: 3	Expected: 4

- Glyph name: uni1FB2	Contours detected: 5	Expected: 4

- Glyph name: uni1FB3	Contours detected: 4	Expected: 3

- Glyph name: uni1FB4	Contours detected: 5	Expected: 4

- Glyph name: uni1FC1	Contours detected: 2	Expected: 3

- Glyph name: uni1FCD	Contours detected: 1	Expected: 2

- Glyph name: uni1FCE	Contours detected: 1	Expected: 2

- Glyph name: uni1FD7	Contours detected: 3	Expected: 4

- Glyph name: uni1FD9	Contours detected: 4	Expected: 2

- Glyph name: uni1FDE	Contours detected: 1	Expected: 2

- Glyph name: uni1FE7	Contours detected: 1	Expected: 4

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: lira	Contours detected: 3	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: uni26AD	Contours detected: 6	Expected: 4

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: iotatonos	Contours detected: 1	Expected: 2

- Glyph name: lira	Contours detected: 3	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 4	Expected: 2

- Glyph name: uni0428	Contours detected: 3	Expected: 1

- Glyph name: uni0429	Contours detected: 3	Expected: 1

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni0436	Contours detected: 3	Expected: 1

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni0466	Contours detected: 4	Expected: 2

- Glyph name: uni0467	Contours detected: 4	Expected: 2

- Glyph name: uni0468	Contours detected: 3	Expected: 2

- Glyph name: uni0469	Contours detected: 5	Expected: 2

- Glyph name: uni046C	Contours detected: 3	Expected: 2

- Glyph name: uni046D	Contours detected: 3	Expected: 2

- Glyph name: uni046E	Contours detected: 1	Expected: 2

- Glyph name: uni046F	Contours detected: 1	Expected: 2

- Glyph name: uni0476	Contours detected: 2	Expected: 3

- Glyph name: uni0477	Contours detected: 2	Expected: 3

- Glyph name: uni0478	Contours detected: 2	Expected: 3

- Glyph name: uni0479	Contours detected: 2	Expected: 3

- Glyph name: uni048C	Contours detected: 4	Expected: 2

- Glyph name: uni0497	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni049D	Contours detected: 2	Expected: 1

- Glyph name: uni049E	Contours detected: 3	Expected: 1

- Glyph name: uni04A1	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 3	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C2	Contours detected: 4	Expected: 2

- Glyph name: uni04DD	Contours detected: 5	Expected: 3

- Glyph name: uni04F2	Contours detected: 2	Expected: 3

- Glyph name: uni04F3	Contours detected: 2	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

- Glyph name: uni1EA4	Contours detected: 3	Expected: 4

- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

- Glyph name: uni1EAA	Contours detected: 3	Expected: 4

- Glyph name: uni1EAF	Contours detected: 3	Expected: 4

- Glyph name: uni1EB4	Contours detected: 3	Expected: 4

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni1EBE	Contours detected: 2	Expected: 3

- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

- Glyph name: uni1EC4	Contours detected: 2	Expected: 3

- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

- Glyph name: uni1ECC	Contours detected: 2	Expected: 3

- Glyph name: uni1ECD	Contours detected: 2	Expected: 3

- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

- Glyph name: uni1ED0	Contours detected: 3	Expected: 4

- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

- Glyph name: uni1ED6	Contours detected: 3	Expected: 4

- Glyph name: uni1ED8	Contours detected: 3	Expected: 4

- Glyph name: uni1ED9	Contours detected: 3	Expected: 4

- Glyph name: uni1EDD	Contours detected: 2	Expected: 3

- Glyph name: uni1EDE	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EE4	Contours detected: 1	Expected: 2

- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

- Glyph name: uni1EED	Contours detected: 3	Expected: 2

- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

- Glyph name: uni1F02	Contours detected: 3	Expected: 4

- Glyph name: uni1F04	Contours detected: 3	Expected: 4

- Glyph name: uni1F05	Contours detected: 3	Expected: 4

- Glyph name: uni1F0A	Contours detected: 3	Expected: 4

- Glyph name: uni1F0C	Contours detected: 3	Expected: 4

- Glyph name: uni1F0D	Contours detected: 3	Expected: 4

- Glyph name: uni1F12	Contours detected: 2	Expected: 3

- Glyph name: uni1F14	Contours detected: 2	Expected: 3

- Glyph name: uni1F15	Contours detected: 2	Expected: 3

- Glyph name: uni1F1A	Contours detected: 2	Expected: 3

- Glyph name: uni1F1C	Contours detected: 2	Expected: 3

- Glyph name: uni1F1D	Contours detected: 2	Expected: 3

- Glyph name: uni1F22	Contours detected: 2	Expected: 3

- Glyph name: uni1F24	Contours detected: 2	Expected: 3

- Glyph name: uni1F25	Contours detected: 2	Expected: 3

- Glyph name: uni1F2A	Contours detected: 2	Expected: 3

- Glyph name: uni1F2C	Contours detected: 2	Expected: 3

- Glyph name: uni1F2D	Contours detected: 2	Expected: 3

- Glyph name: uni1F30	Contours detected: 1	Expected: 2

- Glyph name: uni1F31	Contours detected: 1	Expected: 2

- Glyph name: uni1F32	Contours detected: 2	Expected: 3

- Glyph name: uni1F34	Contours detected: 2	Expected: 3

- Glyph name: uni1F35	Contours detected: 2	Expected: 3

- Glyph name: uni1F36	Contours detected: 2	Expected: 3

- Glyph name: uni1F3A	Contours detected: 2	Expected: 3

- Glyph name: uni1F3C	Contours detected: 2	Expected: 3

- Glyph name: uni1F3D	Contours detected: 2	Expected: 3

- Glyph name: uni1F42	Contours detected: 3	Expected: 4

- Glyph name: uni1F44	Contours detected: 3	Expected: 4

- Glyph name: uni1F45	Contours detected: 3	Expected: 4

- Glyph name: uni1F4A	Contours detected: 3	Expected: 4

- Glyph name: uni1F4C	Contours detected: 3	Expected: 4

- Glyph name: uni1F4D	Contours detected: 3	Expected: 4

- Glyph name: uni1F52	Contours detected: 2	Expected: 3

- Glyph name: uni1F54	Contours detected: 2	Expected: 3

- Glyph name: uni1F55	Contours detected: 2	Expected: 3

- Glyph name: uni1F5D	Contours detected: 2	Expected: 3

- Glyph name: uni1F62	Contours detected: 2	Expected: 3

- Glyph name: uni1F64	Contours detected: 2	Expected: 3

- Glyph name: uni1F65	Contours detected: 2	Expected: 3

- Glyph name: uni1F6A	Contours detected: 2	Expected: 3

- Glyph name: uni1F6C	Contours detected: 2	Expected: 3

- Glyph name: uni1F6D	Contours detected: 2	Expected: 3

- Glyph name: uni1F70	Contours detected: 4	Expected: 3

- Glyph name: uni1F71	Contours detected: 4	Expected: 3

- Glyph name: uni1F76	Contours detected: 1	Expected: 2

- Glyph name: uni1F77	Contours detected: 1	Expected: 2

- Glyph name: uni1F82	Contours detected: 4	Expected: 5

- Glyph name: uni1F84	Contours detected: 4	Expected: 5

- Glyph name: uni1F85	Contours detected: 4	Expected: 5

- Glyph name: uni1F8A	Contours detected: 4	Expected: 5

- Glyph name: uni1F8C	Contours detected: 4	Expected: 5

- Glyph name: uni1F8D	Contours detected: 4	Expected: 5

- Glyph name: uni1F92	Contours detected: 3	Expected: 4

- Glyph name: uni1F94	Contours detected: 3	Expected: 4

- Glyph name: uni1F95	Contours detected: 3	Expected: 4

- Glyph name: uni1F9A	Contours detected: 3	Expected: 4

- Glyph name: uni1F9C	Contours detected: 3	Expected: 4

- Glyph name: uni1F9D	Contours detected: 3	Expected: 4

- Glyph name: uni1FA2	Contours detected: 3	Expected: 4

- Glyph name: uni1FA4	Contours detected: 3	Expected: 4

- Glyph name: uni1FA5	Contours detected: 3	Expected: 4

- Glyph name: uni1FAA	Contours detected: 3	Expected: 4

- Glyph name: uni1FAC	Contours detected: 3	Expected: 4

- Glyph name: uni1FAD	Contours detected: 3	Expected: 4

- Glyph name: uni1FB2	Contours detected: 5	Expected: 4

- Glyph name: uni1FB3	Contours detected: 4	Expected: 3

- Glyph name: uni1FB4	Contours detected: 5	Expected: 4

- Glyph name: uni1FC1	Contours detected: 2	Expected: 3

- Glyph name: uni1FCD	Contours detected: 1	Expected: 2

- Glyph name: uni1FCE	Contours detected: 1	Expected: 2

- Glyph name: uni1FD7	Contours detected: 3	Expected: 4

- Glyph name: uni1FD9	Contours detected: 4	Expected: 2

- Glyph name: uni1FDE	Contours detected: 1	Expected: 2

- Glyph name: uni1FE7	Contours detected: 1	Expected: 4

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: uni26AD	Contours detected: 6	Expected: 4

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* circumflexcomb_hookabove.cap: L&lt;&lt;794.0,1506.0&gt;--&lt;793.0,1503.0&gt;&gt; has the same coordinates as a previous segment.

* hookabovecomb (U+0309): L&lt;&lt;-484.0,1211.0&gt;--&lt;-485.0,1208.0&gt;&gt; has the same coordinates as a previous segment.

* sigma1 (U+03C2): B&lt;&lt;810.0,-43.0&gt;-&lt;812.0,-42.0&gt;-&lt;812.0,-41.0&gt;&gt; has the same coordinates as a previous segment.

* threeabove_ar: L&lt;&lt;567.0,1533.0&gt;--&lt;567.0,1531.0&gt;&gt; has the same coordinates as a previous segment.

* uni034F (U+034F): B&lt;&lt;280.0,1467.0&gt;-&lt;173.0,1430.0&gt;-&lt;148.0,1291.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C5 (U+04C5): B&lt;&lt;224.0,88.0&gt;-&lt;224.0,88.0&gt;-&lt;224.0,88.0&gt;&gt; has the same coordinates as a previous segment.

* uni0512 (U+0512): B&lt;&lt;224.0,88.0&gt;-&lt;224.0,88.0&gt;-&lt;224.0,88.0&gt;&gt; has the same coordinates as a previous segment.

* uni0605 (U+0605): B&lt;&lt;154.0,1469.0&gt;-&lt;154.0,1469.0&gt;-&lt;154.0,1469.0&gt;&gt; has the same coordinates as a previous segment.

* uni0663 (U+06F3): B&lt;&lt;607.0,1073.0&gt;-&lt;607.0,1073.0&gt;-&lt;607.0,1073.0&gt;&gt; has the same coordinates as a previous segment.

* uni06C2.fina: B&lt;&lt;675.0,1248.0&gt;-&lt;673.0,1252.0&gt;-&lt;676.0,1248.0&gt;&gt; has the same coordinates as a previous segment.

* uni06E4 (U+06E4): B&lt;&lt;269.0,1601.0&gt;-&lt;268.0,1601.0&gt;-&lt;268.0,1600.0&gt;&gt; has the same coordinates as a previous segment.

* uni0774 (U+0774): L&lt;&lt;309.0,1330.0&gt;--&lt;309.0,1328.0&gt;&gt; has the same coordinates as a previous segment.

* uni0774.fina: L&lt;&lt;252.0,1330.0&gt;--&lt;252.0,1328.0&gt;&gt; has the same coordinates as a previous segment.

* uni0774.fina.alt: L&lt;&lt;575.0,1330.0&gt;--&lt;575.0,1328.0&gt;&gt; has the same coordinates as a previous segment.

* uni0776 (U+0776): L&lt;&lt;448.0,1211.0&gt;--&lt;448.0,1209.0&gt;&gt; has the same coordinates as a previous segment.

* uni0776.fina: L&lt;&lt;448.0,894.0&gt;--&lt;448.0,892.0&gt;&gt; has the same coordinates as a previous segment.

* uni0776.init: L&lt;&lt;448.0,1211.0&gt;--&lt;448.0,1209.0&gt;&gt; has the same coordinates as a previous segment.

* uni0776.medi: L&lt;&lt;391.0,1211.0&gt;--&lt;391.0,1209.0&gt;&gt; has the same coordinates as a previous segment.

* uni0779 (U+0779): L&lt;&lt;356.0,896.0&gt;--&lt;356.0,894.0&gt;&gt; has the same coordinates as a previous segment.

* uni0779.fina: L&lt;&lt;372.0,904.0&gt;--&lt;372.0,902.0&gt;&gt; has the same coordinates as a previous segment.

* uni077B (U+077B): L&lt;&lt;305.0,1269.0&gt;--&lt;305.0,1267.0&gt;&gt; has the same coordinates as a previous segment.

* uni077B.fina: L&lt;&lt;305.0,1011.0&gt;--&lt;305.0,1009.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D (U+077D): L&lt;&lt;664.0,1505.0&gt;--&lt;665.0,1506.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.fina: L&lt;&lt;571.0,1505.0&gt;--&lt;572.0,1506.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.init: L&lt;&lt;822.0,1505.0&gt;--&lt;823.0,1506.0&gt;&gt; has the same coordinates as a previous segment.

* uni08D4 (U+08D4): B&lt;&lt;229.0,1231.0&gt;-&lt;231.0,1232.0&gt;-&lt;228.0,1232.0&gt;&gt; has the same coordinates as a previous segment.

* uni08DC (U+08DC): L&lt;&lt;253.0,1207.0&gt;--&lt;253.0,1209.0&gt;&gt; has the same coordinates as a previous segment.

* uni08DD (U+08DD): B&lt;&lt;593.0,1291.0&gt;-&lt;592.0,1290.0&gt;-&lt;593.0,1290.0&gt;&gt; has the same coordinates as a previous segment.

* uni08DE (U+08DE): L&lt;&lt;437.0,1207.0&gt;--&lt;437.0,1209.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EDE (U+1EDE): L&lt;&lt;884.0,1641.0&gt;--&lt;883.0,1638.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EDF (U+1EDF): L&lt;&lt;591.0,1211.0&gt;--&lt;590.0,1208.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEC (U+1EEC): L&lt;&lt;1354.0,1641.0&gt;--&lt;1353.0,1638.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EED (U+1EED): L&lt;&lt;688.0,1231.0&gt;--&lt;687.0,1228.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F06 (U+1F06): B&lt;&lt;467.0,1075.0&gt;-&lt;468.0,1076.0&gt;-&lt;462.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F0E (U+1F0E): B&lt;&lt;21.0,930.0&gt;-&lt;22.0,931.0&gt;-&lt;16.0,934.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F26 (U+1F26): B&lt;&lt;491.0,1075.0&gt;-&lt;492.0,1076.0&gt;-&lt;486.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F2E (U+1F2E): B&lt;&lt;-389.0,905.0&gt;-&lt;-388.0,906.0&gt;-&lt;-394.0,909.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F36 (U+1F36): B&lt;&lt;503.0,1075.0&gt;-&lt;504.0,1076.0&gt;-&lt;498.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F3E (U+1F3E): B&lt;&lt;-233.0,863.0&gt;-&lt;-232.0,864.0&gt;-&lt;-238.0,867.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F56 (U+1F56): B&lt;&lt;505.0,1075.0&gt;-&lt;506.0,1076.0&gt;-&lt;500.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F66 (U+1F66): B&lt;&lt;507.0,1075.0&gt;-&lt;508.0,1076.0&gt;-&lt;502.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F6E (U+1F6E): B&lt;&lt;-4.0,983.0&gt;-&lt;-3.0,984.0&gt;-&lt;-9.0,987.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F70 (U+1F70): B&lt;&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F71 (U+1F71): B&lt;&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F86 (U+1F86): B&lt;&lt;467.0,1075.0&gt;-&lt;468.0,1076.0&gt;-&lt;462.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F8E (U+1F8E): B&lt;&lt;21.0,930.0&gt;-&lt;22.0,931.0&gt;-&lt;16.0,934.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F96 (U+1F96): B&lt;&lt;491.0,1075.0&gt;-&lt;492.0,1076.0&gt;-&lt;486.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1F9E (U+1F9E): B&lt;&lt;-389.0,905.0&gt;-&lt;-388.0,906.0&gt;-&lt;-394.0,909.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FA6 (U+1FA6): B&lt;&lt;507.0,1075.0&gt;-&lt;508.0,1076.0&gt;-&lt;502.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FAE (U+1FAE): B&lt;&lt;-4.0,983.0&gt;-&lt;-3.0,984.0&gt;-&lt;-9.0,987.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB2 (U+1FB2): B&lt;&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB3 (U+1FB3): B&lt;&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FB4 (U+1FB4): B&lt;&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;-&lt;893.0,161.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FCF (U+1FCF): B&lt;&lt;503.0,1075.0&gt;-&lt;504.0,1076.0&gt;-&lt;498.0,1079.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FD9 (U+1FD9): B&lt;&lt;228.0,1386.0&gt;-&lt;228.0,1379.0&gt;-&lt;217.0,1386.0&gt;&gt; has the same coordinates as a previous segment.

* uni1FEC (U+1FEC): B&lt;&lt;173.0,1151.0&gt;-&lt;169.0,1149.0&gt;-&lt;168.0,1147.0&gt;&gt; has the same coordinates as a previous segment.

* uni203B (U+203B): L&lt;&lt;515.0,831.0&gt;--&lt;482.0,864.0&gt;&gt; has the same coordinates as a previous segment.

* uni26AD (U+26AD): B&lt;&lt;398.0,879.0&gt;-&lt;399.0,879.0&gt;-&lt;398.0,879.0&gt;&gt; has the same coordinates as a previous segment.

* uni26AD (U+26AD): B&lt;&lt;538.0,236.0&gt;-&lt;537.0,236.0&gt;-&lt;537.0,236.0&gt;&gt; has the same coordinates as a previous segment.

* uniFDFA (U+FDFA): B&lt;&lt;705.0,1185.0&gt;-&lt;701.0,1180.0&gt;-&lt;695.0,1175.0&gt;&gt; has the same coordinates as a previous segment.

* uniFDFA (U+FDFA): B&lt;&lt;991.0,867.0&gt;-&lt;998.0,873.0&gt;-&lt;1001.0,884.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE01 (U+FE01): B&lt;&lt;630.0,861.0&gt;-&lt;711.0,847.0&gt;-&lt;717.0,766.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE02 (U+FE02): B&lt;&lt;634.0,407.0&gt;-&lt;712.0,432.0&gt;-&lt;727.0,506.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE02 (U+FE02): B&lt;&lt;629.0,860.0&gt;-&lt;705.0,846.0&gt;-&lt;712.0,773.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE02 (U+FE02): B&lt;&lt;656.0,635.0&gt;-&lt;687.0,621.0&gt;-&lt;706.0,595.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE02 (U+FE02): B&lt;&lt;706.0,595.0&gt;-&lt;723.0,575.0&gt;-&lt;727.0,550.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE03 (U+FE03): B&lt;&lt;664.5,868.0&gt;-&lt;668.0,865.0&gt;-&lt;659.0,865.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE03 (U+FE03): L&lt;&lt;651.0,542.0&gt;--&lt;659.0,542.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE03 (U+FE03): B&lt;&lt;430.0,542.0&gt;-&lt;430.0,545.0&gt;-&lt;430.0,543.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE03 (U+FE03): L&lt;&lt;430.0,543.0&gt;--&lt;430.0,542.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE04 (U+FE04): B&lt;&lt;478.0,650.0&gt;-&lt;478.0,650.0&gt;-&lt;480.0,651.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE04 (U+FE04): B&lt;&lt;633.0,408.0&gt;-&lt;713.0,435.0&gt;-&lt;731.0,519.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE05 (U+FE05): B&lt;&lt;901.5,1366.5&gt;-&lt;901.0,1366.0&gt;-&lt;899.0,1368.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE05 (U+FE05): B&lt;&lt;603.5,1141.5&gt;-&lt;604.0,1142.0&gt;-&lt;607.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE07 (U+FE07): B&lt;&lt;901.5,1366.5&gt;-&lt;901.0,1366.0&gt;-&lt;899.0,1368.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE07 (U+FE07): B&lt;&lt;603.5,1141.5&gt;-&lt;604.0,1142.0&gt;-&lt;607.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE08 (U+FE08): B&lt;&lt;901.5,1366.5&gt;-&lt;901.0,1366.0&gt;-&lt;899.0,1368.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE08 (U+FE08): B&lt;&lt;603.5,1141.5&gt;-&lt;604.0,1142.0&gt;-&lt;607.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE09 (U+FE09): B&lt;&lt;901.5,1366.5&gt;-&lt;901.0,1366.0&gt;-&lt;899.0,1368.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE09 (U+FE09): B&lt;&lt;603.5,1141.5&gt;-&lt;604.0,1142.0&gt;-&lt;607.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0B (U+FE0B): B&lt;&lt;804.0,861.0&gt;-&lt;885.0,847.0&gt;-&lt;891.0,766.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0C (U+FE0C): B&lt;&lt;808.0,407.0&gt;-&lt;886.0,432.0&gt;-&lt;901.0,506.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0C (U+FE0C): B&lt;&lt;803.0,860.0&gt;-&lt;879.0,846.0&gt;-&lt;886.0,773.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0C (U+FE0C): B&lt;&lt;830.0,635.0&gt;-&lt;861.0,621.0&gt;-&lt;880.0,595.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0C (U+FE0C): B&lt;&lt;880.0,595.0&gt;-&lt;897.0,575.0&gt;-&lt;901.0,550.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0D (U+FE0D): B&lt;&lt;838.5,868.0&gt;-&lt;842.0,865.0&gt;-&lt;833.0,865.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0D (U+FE0D): L&lt;&lt;825.0,542.0&gt;--&lt;833.0,542.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0D (U+FE0D): B&lt;&lt;604.0,542.0&gt;-&lt;604.0,545.0&gt;-&lt;604.0,543.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0D (U+FE0D): L&lt;&lt;604.0,543.0&gt;--&lt;604.0,542.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0E (U+FE0E): B&lt;&lt;652.0,650.0&gt;-&lt;652.0,650.0&gt;-&lt;654.0,651.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0E (U+FE0E): B&lt;&lt;807.0,408.0&gt;-&lt;887.0,435.0&gt;-&lt;905.0,519.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0F (U+FE0F): B&lt;&lt;901.5,1366.5&gt;-&lt;901.0,1366.0&gt;-&lt;899.0,1368.0&gt;&gt; has the same coordinates as a previous segment.

* uniFE0F (U+FE0F): B&lt;&lt;603.5,1141.5&gt;-&lt;604.0,1142.0&gt;-&lt;607.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* uniFEF6 (U+FEF6): B&lt;&lt;779.0,1609.0&gt;-&lt;773.0,1606.0&gt;-&lt;768.0,1602.0&gt;&gt; has the same coordinates as a previous segment.
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
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, canadian-aboriginal, hebrew, tai-le, todhri, old-permic, malayalam, math, syriac, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
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
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, math, cherokee</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, thai, sunuwar, cherokee, gothic, syriac, caucasian-albanian</li>
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
<li>U+060C ARABIC COMMA: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
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
<li>U+061B ARABIC SEMICOLON: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: arabic, syriac, thaana</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: arabic, yezidi, hanifi-rohingya, garay, adlam, syriac, nko, thaana</li>
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
<li>U+0640 ARABIC TATWEEL: try adding one of: arabic, old-uyghur, mandaic, psalter-pahlavi, hanifi-rohingya, adlam, manichaean, syriac, sogdian</li>
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
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: arabic, yezidi, hanifi-rohingya, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: arabic, syriac, nko, thaana</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: arabic, syriac, thaana</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: arabic, syriac, thaana</li>
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
<li>U+06D4 ARABIC FULL STOP: try adding one of: arabic, hanifi-rohingya, yezidi</li>
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
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, dogra, tagbanwa, duployan, batak, hatran, mandaic, cham, khojki, hanunoo, hebrew, javanese, masaram-gondi, mongolian, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, siddham, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, old-hungarian, dogra, tagbanwa, duployan, batak, mandaic, masaram-gondi, cham, khojki, hanunoo, hebrew, javanese, mongolian, siddham, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: arabic, hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+2010 HYPHEN: try adding one of: arabic, cham, yi, hebrew, sundanese, lisu, kharoshthi, armenian, sora-sompeng, syloti-nagri, kaithi, kayah-li, coptic</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
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
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: telugu, math, manichaean, sharada, tamil, duployan, batak, kharoshthi, sogdian, gurmukhi, symbols, saurashtra, balinese, soyombo, khudawadi, gujarati, bhaiksuki, myanmar, nko, grantha, lepcha, khojki, caucasian-albanian, gunjala-gondi, bengali, mende-kikakui, buginese, tai-viet, dogra, tagbanwa, siddham, cham, mongolian, hanunoo, zanabazar-square, bassa-vah, limbu, tirhuta, tibetan, warang-citi, marchen, new-tai-lue, hanifi-rohingya, syloti-nagri, canadian-aboriginal, pahawh-hmong, tai-tham, masaram-gondi, mandaic, yi, javanese, hebrew, adlam, rejang, tifinagh, sundanese, phags-pa, malayalam, devanagari, elbasan, syriac, kayah-li, psalter-pahlavi, music, oriya, tai-le, armenian, tagalog, sinhala, mahajani, meetei-mayek, old-permic, brahmi, osage, thai, takri, modi, kaithi, newa, wancho, chakma, khmer, coptic, miao, buhid, ahom, lao, kannada, thaana</li>
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
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: arabic, thaana</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: arabic, thaana</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, phags-pa, yi</li>
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
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* Alpha (U+0391): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* Alphatonos (U+0386): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* Lambda (U+039B): L&lt;&lt;709.0,159.0&gt;--&lt;721.0,119.0&gt;&gt;/L&lt;&lt;721.0,119.0&gt;--&lt;537.0,1068.0&gt;&gt; = 5.726410245228462

* Mu (U+039C): B&lt;&lt;523.5,736.5&gt;-&lt;546.0,665.0&gt;-&lt;558.0,621.0&gt;&gt;/B&lt;&lt;558.0,621.0&gt;-&lt;557.0,657.0&gt;-&lt;569.5,718.5&gt;&gt; = 13.663978431863159

* Mu (U+039C): L&lt;&lt;781.0,127.0&gt;--&lt;781.0,973.0&gt;&gt;/B&lt;&lt;781.0,973.0&gt;-&lt;771.0,899.0&gt;-&lt;748.5,811.0&gt;&gt; = 7.696051722016556

* aogonek (U+0105): L&lt;&lt;846.0,51.0&gt;--&lt;873.0,89.0&gt;&gt;/B&lt;&lt;873.0,89.0&gt;-&lt;809.0,26.0&gt;-&lt;710.5,-14.5&gt;&gt; = 10.056342701800231

* asteriskmath (U+2217): B&lt;&lt;634.0,852.0&gt;-&lt;630.0,799.0&gt;-&lt;617.0,767.0&gt;&gt;/B&lt;&lt;617.0,767.0&gt;-&lt;638.0,796.0&gt;-&lt;680.5,823.0&gt;&gt; = 13.800274735425981

* asteriskmath (U+2217): B&lt;&lt;680.5,434.0&gt;-&lt;638.0,461.0&gt;-&lt;617.0,490.0&gt;&gt;/B&lt;&lt;617.0,490.0&gt;-&lt;630.0,458.0&gt;-&lt;634.0,405.5&gt;&gt; = 13.800274735425981

* at (U+0040): L&lt;&lt;766.0,727.0&gt;--&lt;766.0,725.0&gt;&gt;/L&lt;&lt;766.0,725.0&gt;--&lt;769.0,763.0&gt;&gt; = 4.513988458001203

* b (U+0062): B&lt;&lt;464.0,-7.5&gt;-&lt;375.0,40.0&gt;-&lt;326.0,114.0&gt;&gt;/L&lt;&lt;326.0,114.0&gt;--&lt;366.0,55.0&gt;&gt; = 0.624921280071304

* b (U+0062): L&lt;&lt;376.0,1257.0&gt;--&lt;375.0,788.0&gt;&gt;/B&lt;&lt;375.0,788.0&gt;-&lt;393.0,878.0&gt;-&lt;473.0,928.5&gt;&gt; = 11.187766817972967

* d (U+0064): B&lt;&lt;755.0,928.5&gt;-&lt;835.0,878.0&gt;-&lt;853.0,788.0&gt;&gt;/L&lt;&lt;853.0,788.0&gt;--&lt;852.0,1257.0&gt;&gt; = 11.187766817972967

* d (U+0064): L&lt;&lt;862.0,55.0&gt;--&lt;900.0,113.0&gt;&gt;/B&lt;&lt;900.0,113.0&gt;-&lt;851.0,39.0&gt;-&lt;762.5,-8.0&gt;&gt; = 0.27930772986015584

* dcaron (U+010F): B&lt;&lt;679.5,931.0&gt;-&lt;743.0,883.0&gt;-&lt;751.0,797.0&gt;&gt;/L&lt;&lt;751.0,797.0&gt;--&lt;750.0,1257.0&gt;&gt; = 5.189989823737527

* dong (U+20AB): B&lt;&lt;684.5,70.0&gt;-&lt;672.0,96.0&gt;-&lt;683.0,119.0&gt;&gt;/B&lt;&lt;683.0,119.0&gt;-&lt;668.0,96.0&gt;-&lt;635.0,72.5&gt;&gt; = 7.551376788548213

* eng (U+014B): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* fourbelow_ar: B&lt;&lt;542.0,1675.5&gt;-&lt;583.0,1640.0&gt;-&lt;585.0,1613.0&gt;&gt;/B&lt;&lt;585.0,1613.0&gt;-&lt;588.0,1640.0&gt;-&lt;605.0,1660.0&gt;&gt; = 10.576586544968738

* g (U+0067): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* g (U+0067): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* gamma (U+03B3): B&lt;&lt;408.5,816.5&gt;-&lt;494.0,709.0&gt;-&lt;579.0,466.0&gt;&gt;/B&lt;&lt;579.0,466.0&gt;-&lt;569.0,505.0&gt;-&lt;582.5,559.0&gt;&gt; = 4.898148277250887

* gbreve (U+011F): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* gbreve (U+011F): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* gcaron (U+01E7): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* gcaron (U+01E7): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* gcircumflex (U+011D): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* gcircumflex (U+011D): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* gdotaccent (U+0121): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* gdotaccent (U+0121): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* h (U+0068): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;/B&lt;&lt;385.0,728.0&gt;-&lt;403.0,804.0&gt;-&lt;456.5,860.5&gt;&gt; = 13.216221788799638

* hcircumflex (U+0125): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;/B&lt;&lt;385.0,728.0&gt;-&lt;403.0,804.0&gt;-&lt;456.5,860.5&gt;&gt; = 13.216221788799638

* kafDotless_ar.fina: L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* kafDotless_ar: L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* kappa (U+03BA): L&lt;&lt;294.0,692.0&gt;--&lt;289.0,582.0&gt;&gt;/B&lt;&lt;289.0,582.0&gt;-&lt;294.0,616.0&gt;-&lt;330.5,673.0&gt;&gt; = 5.763323921532758

* lira (U+20A4): B&lt;&lt;139.0,357.0&gt;-&lt;197.0,386.0&gt;-&lt;262.0,392.0&gt;&gt;/L&lt;&lt;262.0,392.0&gt;--&lt;170.0,392.0&gt;&gt; = 5.273895957351716

* lira (U+20A4): L&lt;&lt;360.0,392.0&gt;--&lt;324.0,392.0&gt;&gt;/B&lt;&lt;324.0,392.0&gt;-&lt;342.0,390.0&gt;-&lt;354.0,386.0&gt;&gt; = 6.340191745909908

* m (U+006D): B&lt;&lt;617.0,928.5&gt;-&lt;676.0,878.0&gt;-&lt;672.0,799.0&gt;&gt;/B&lt;&lt;672.0,799.0&gt;-&lt;697.0,880.0&gt;-&lt;761.0,929.5&gt;&gt; = 14.253844940930117

* musicalnote (U+266A): B&lt;&lt;768.5,508.5&gt;-&lt;744.0,564.0&gt;-&lt;740.0,624.0&gt;&gt;/L&lt;&lt;740.0,624.0&gt;--&lt;741.0,266.0&gt;&gt; = 3.6540311736844093

* n (U+006E): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* nacute (U+0144): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* ncaron (U+0148): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* nine (U+0039): B&lt;&lt;684.0,287.5&gt;-&lt;812.0,403.0&gt;-&lt;837.0,592.0&gt;&gt;/B&lt;&lt;837.0,592.0&gt;-&lt;825.0,508.0&gt;-&lt;748.0,465.5&gt;&gt; = 0.5950386308273755

* ntilde (U+00F1): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* ohorn (U+01A1): B&lt;&lt;535.0,933.0&gt;-&lt;644.0,933.0&gt;-&lt;735.0,882.0&gt;&gt;/B&lt;&lt;735.0,882.0&gt;-&lt;731.0,885.0&gt;-&lt;748.0,888.0&gt;&gt; = 7.6019024309512755

* p (U+0070): B&lt;&lt;473.0,-4.5&gt;-&lt;393.0,46.0&gt;-&lt;375.0,136.0&gt;&gt;/L&lt;&lt;375.0,136.0&gt;--&lt;376.0,-333.0&gt;&gt; = 11.187766817972967

* p (U+0070): L&lt;&lt;366.0,869.0&gt;--&lt;328.0,811.0&gt;&gt;/B&lt;&lt;328.0,811.0&gt;-&lt;377.0,885.0&gt;-&lt;465.5,932.0&gt;&gt; = 0.27930772986146074

* phi (U+03C6): B&lt;&lt;379.0,171.0&gt;-&lt;417.0,142.0&gt;-&lt;454.0,154.0&gt;&gt;/B&lt;&lt;454.0,154.0&gt;-&lt;438.0,152.0&gt;-&lt;436.5,201.5&gt;&gt; = 10.84412339125517

* prescription (U+211E): B&lt;&lt;855.0,462.0&gt;-&lt;855.0,440.0&gt;-&lt;830.0,416.0&gt;&gt;/L&lt;&lt;830.0,416.0&gt;--&lt;943.0,515.0&gt;&gt; = 2.60905837925404

* q (U+0071): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* q (U+0071): L&lt;&lt;852.0,-333.0&gt;--&lt;853.0,136.0&gt;&gt;/B&lt;&lt;853.0,136.0&gt;-&lt;835.0,46.0&gt;-&lt;755.0,-4.5&gt;&gt; = 11.187766817972967

* six (U+0036): B&lt;&lt;544.0,899.5&gt;-&lt;416.0,784.0&gt;-&lt;391.0,595.0&gt;&gt;/B&lt;&lt;391.0,595.0&gt;-&lt;403.0,679.0&gt;-&lt;480.0,721.5&gt;&gt; = 0.5950386308273755

* thorn (U+00FE): B&lt;&lt;473.0,-4.5&gt;-&lt;393.0,46.0&gt;-&lt;375.0,136.0&gt;&gt;/L&lt;&lt;375.0,136.0&gt;--&lt;376.0,-333.0&gt;&gt; = 11.187766817972967

* thorn (U+00FE): L&lt;&lt;376.0,1257.0&gt;--&lt;375.0,794.0&gt;&gt;/B&lt;&lt;375.0,794.0&gt;-&lt;395.0,883.0&gt;-&lt;476.0,931.0&gt;&gt; = 12.541314973635897

* threeabove_ar: B&lt;&lt;476.0,1628.5&gt;-&lt;482.0,1626.0&gt;-&lt;481.0,1627.0&gt;&gt;/B&lt;&lt;481.0,1627.0&gt;-&lt;495.0,1616.0&gt;-&lt;498.0,1633.5&gt;&gt; = 6.842773412630916

* threequarters (U+00BE): B&lt;&lt;524.0,1092.5&gt;-&lt;495.0,1050.0&gt;-&lt;459.0,1051.0&gt;&gt;/B&lt;&lt;459.0,1051.0&gt;-&lt;502.0,1049.0&gt;-&lt;538.5,1000.5&gt;&gt; = 1.0718604948722883

* u (U+0075): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uacute (U+00FA): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* ubreve (U+016D): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* ucircumflex (U+00FB): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* udieresis (U+00FC): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* ugrave (U+00F9): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uhorn (U+01B0): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uhungarumlaut (U+0171): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* umacron (U+016B): L&lt;&lt;855.0,55.0&gt;--&lt;879.0,185.0&gt;&gt;/B&lt;&lt;879.0,185.0&gt;-&lt;852.0,122.0&gt;-&lt;793.5,67.0&gt;&gt; = 12.738681420719066

* uni00B3 (U+00B3): B&lt;&lt;898.5,976.0&gt;-&lt;865.0,926.0&gt;-&lt;820.0,922.0&gt;&gt;/B&lt;&lt;820.0,922.0&gt;-&lt;873.0,916.0&gt;-&lt;916.0,859.5&gt;&gt; = 11.538424238733194

* uni0123 (U+0123): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* uni0123 (U+0123): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* uni0146 (U+0146): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* uni01D4 (U+01D4): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni01D8 (U+01D8): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni01DA (U+01DA): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni01DC (U+01DC): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni01EB (U+01EB): B&lt;&lt;360.0,-93.5&gt;-&lt;401.0,-36.0&gt;-&lt;454.0,-34.0&gt;&gt;/B&lt;&lt;454.0,-34.0&gt;-&lt;356.0,-18.0&gt;-&lt;272.0,48.0&gt;&gt; = 11.433681265426625

* uni01F5 (U+01F5): B&lt;&lt;764.0,931.5&gt;-&lt;853.0,884.0&gt;-&lt;902.0,810.0&gt;&gt;/L&lt;&lt;902.0,810.0&gt;--&lt;862.0,869.0&gt;&gt; = 0.624921280071304

* uni01F5 (U+01F5): L&lt;&lt;852.0,-17.0&gt;--&lt;859.0,163.0&gt;&gt;/B&lt;&lt;859.0,163.0&gt;-&lt;837.0,85.0&gt;-&lt;756.0,40.0&gt;&gt; = 13.524126696039461

* uni0215 (U+0215): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni034F (U+034F): L&lt;&lt;799.0,1214.0&gt;--&lt;920.0,1211.0&gt;&gt;/L&lt;&lt;920.0,1211.0&gt;--&lt;799.0,1208.0&gt;&gt; = 2.8405310927980456

* uni034F (U+034F): L&lt;&lt;941.0,1217.0&gt;--&lt;941.0,1235.0&gt;&gt;/L&lt;&lt;941.0,1235.0&gt;--&lt;944.0,1216.0&gt;&gt; = 8.972626614896399

* uni03BC (U+03BC): L&lt;&lt;846.0,55.0&gt;--&lt;872.0,165.0&gt;&gt;/B&lt;&lt;872.0,165.0&gt;-&lt;849.0,108.0&gt;-&lt;798.0,58.0&gt;&gt; = 8.675937660977642

* uni03E0 (U+03E0): L&lt;&lt;384.0,140.0&gt;--&lt;483.0,631.0&gt;&gt;/B&lt;&lt;483.0,631.0&gt;-&lt;481.0,626.0&gt;-&lt;463.5,659.5&gt;&gt; = 10.401742113872047

* uni0405 (U+0405): B&lt;&lt;380.0,16.0&gt;-&lt;351.0,36.0&gt;-&lt;337.0,60.0&gt;&gt;/L&lt;&lt;337.0,60.0&gt;--&lt;342.0,43.0&gt;&gt; = 13.866896829494456

* uni0425 (U+0425): L&lt;&lt;615.0,467.0&gt;--&lt;385.0,121.0&gt;&gt;/L&lt;&lt;385.0,121.0&gt;--&lt;437.0,170.0&gt;&gt; = 13.087783401735319

* uni0428 (U+0428): L&lt;&lt;1145.0,1017.0&gt;--&lt;1137.0,1049.0&gt;&gt;/L&lt;&lt;1137.0,1049.0&gt;--&lt;1137.0,138.0&gt;&gt; = 14.036243467926484

* uni0428 (U+0428): L&lt;&lt;317.0,1017.0&gt;--&lt;309.0,1049.0&gt;&gt;/L&lt;&lt;309.0,1049.0&gt;--&lt;308.0,145.0&gt;&gt; = 14.09962372914638

* uni0428 (U+0428): L&lt;&lt;506.0,145.0&gt;--&lt;505.0,1050.0&gt;&gt;/L&lt;&lt;505.0,1050.0&gt;--&lt;503.0,1017.0&gt;&gt; = 3.531539486756178

* uni0428 (U+0428): L&lt;&lt;725.0,1017.0&gt;--&lt;723.0,1050.0&gt;&gt;/L&lt;&lt;723.0,1050.0&gt;--&lt;722.0,145.0&gt;&gt; = 3.531539486756178

* uni0428 (U+0428): L&lt;&lt;920.0,145.0&gt;--&lt;919.0,1049.0&gt;&gt;/L&lt;&lt;919.0,1049.0&gt;--&lt;911.0,1017.0&gt;&gt; = 14.09962372914638

* uni0429 (U+0429): L&lt;&lt;1145.0,1017.0&gt;--&lt;1137.0,1049.0&gt;&gt;/L&lt;&lt;1137.0,1049.0&gt;--&lt;1137.0,138.0&gt;&gt; = 14.036243467926484

* uni0429 (U+0429): L&lt;&lt;317.0,1017.0&gt;--&lt;309.0,1049.0&gt;&gt;/L&lt;&lt;309.0,1049.0&gt;--&lt;308.0,145.0&gt;&gt; = 14.09962372914638

* uni0429 (U+0429): L&lt;&lt;506.0,145.0&gt;--&lt;505.0,1050.0&gt;&gt;/L&lt;&lt;505.0,1050.0&gt;--&lt;503.0,1017.0&gt;&gt; = 3.531539486756178

* uni0429 (U+0429): L&lt;&lt;725.0,1017.0&gt;--&lt;723.0,1050.0&gt;&gt;/L&lt;&lt;723.0,1050.0&gt;--&lt;722.0,145.0&gt;&gt; = 3.531539486756178

* uni0429 (U+0429): L&lt;&lt;920.0,145.0&gt;--&lt;919.0,1049.0&gt;&gt;/L&lt;&lt;919.0,1049.0&gt;--&lt;911.0,1017.0&gt;&gt; = 14.09962372914638

* uni0436 (U+0436): L&lt;&lt;505.0,141.0&gt;--&lt;505.0,404.0&gt;&gt;/L&lt;&lt;505.0,404.0&gt;--&lt;499.0,375.0&gt;&gt; = 11.689369175439202

* uni0436 (U+0436): L&lt;&lt;729.0,375.0&gt;--&lt;723.0,404.0&gt;&gt;/L&lt;&lt;723.0,404.0&gt;--&lt;723.0,141.0&gt;&gt; = 11.689369175439202

* uni0436 (U+0436): L&lt;&lt;827.0,831.0&gt;--&lt;826.0,828.0&gt;&gt;/B&lt;&lt;826.0,828.0&gt;-&lt;834.0,844.0&gt;-&lt;843.0,859.0&gt;&gt; = 8.130102354155916

* uni0445 (U+0445): L&lt;&lt;487.0,754.0&gt;--&lt;440.0,805.0&gt;&gt;/L&lt;&lt;440.0,805.0&gt;--&lt;623.0,592.0&gt;&gt; = 1.9950081240646063

* uni0445 (U+0445): L&lt;&lt;607.0,360.0&gt;--&lt;397.0,118.0&gt;&gt;/L&lt;&lt;397.0,118.0&gt;--&lt;447.0,170.0&gt;&gt; = 2.926278989196006

* uni0445 (U+0445): L&lt;&lt;751.0,170.0&gt;--&lt;817.0,119.0&gt;&gt;/L&lt;&lt;817.0,119.0&gt;--&lt;607.0,360.0&gt;&gt; = 11.237865529827765

* uni0447 (U+0447): L&lt;&lt;825.0,150.0&gt;--&lt;823.0,326.0&gt;&gt;/B&lt;&lt;823.0,326.0&gt;-&lt;820.0,295.0&gt;-&lt;790.0,277.0&gt;&gt; = 6.178600531885615

* uni0448 (U+0448): L&lt;&lt;1143.0,754.0&gt;--&lt;1143.0,138.0&gt;&gt;/L&lt;&lt;1143.0,138.0&gt;--&lt;1151.0,170.0&gt;&gt; = 14.036243467926484

* uni0448 (U+0448): L&lt;&lt;513.0,149.0&gt;--&lt;510.0,786.0&gt;&gt;/L&lt;&lt;510.0,786.0&gt;--&lt;502.0,754.0&gt;&gt; = 14.306080308946285

* uni0448 (U+0448): L&lt;&lt;77.0,170.0&gt;--&lt;85.0,138.0&gt;&gt;/L&lt;&lt;85.0,138.0&gt;--&lt;85.0,754.0&gt;&gt; = 14.036243467926484

* uni0449 (U+0449): L&lt;&lt;513.0,149.0&gt;--&lt;510.0,786.0&gt;&gt;/L&lt;&lt;510.0,786.0&gt;--&lt;502.0,754.0&gt;&gt; = 14.306080308946285

* uni0449 (U+0449): L&lt;&lt;77.0,170.0&gt;--&lt;85.0,138.0&gt;&gt;/L&lt;&lt;85.0,138.0&gt;--&lt;85.0,754.0&gt;&gt; = 14.036243467926484

* uni044B (U+044B): L&lt;&lt;108.0,139.0&gt;--&lt;108.0,786.0&gt;&gt;/L&lt;&lt;108.0,786.0&gt;--&lt;100.0,754.0&gt;&gt; = 14.036243467926484

* uni044B (U+044B): L&lt;&lt;1128.0,754.0&gt;--&lt;1120.0,786.0&gt;&gt;/L&lt;&lt;1120.0,786.0&gt;--&lt;1120.0,139.0&gt;&gt; = 14.036243467926484

* uni044B (U+044B): L&lt;&lt;902.0,139.0&gt;--&lt;902.0,786.0&gt;&gt;/L&lt;&lt;902.0,786.0&gt;--&lt;894.0,754.0&gt;&gt; = 14.036243467926484

* uni044D (U+044D): B&lt;&lt;889.5,331.5&gt;-&lt;900.0,348.0&gt;-&lt;920.0,350.0&gt;&gt;/L&lt;&lt;920.0,350.0&gt;--&lt;533.0,350.0&gt;&gt; = 5.710593137499633

* uni044D (U+044D): L&lt;&lt;533.0,554.0&gt;--&lt;936.0,554.0&gt;&gt;/B&lt;&lt;936.0,554.0&gt;-&lt;909.0,553.0&gt;-&lt;897.0,573.0&gt;&gt; = 2.1210963966614473

* uni044E (U+044E): L&lt;&lt;108.0,139.0&gt;--&lt;108.0,786.0&gt;&gt;/L&lt;&lt;108.0,786.0&gt;--&lt;100.0,754.0&gt;&gt; = 14.036243467926484

* uni0452 (U+0452): L&lt;&lt;410.0,940.0&gt;--&lt;414.0,739.0&gt;&gt;/B&lt;&lt;414.0,739.0&gt;-&lt;421.0,781.0&gt;-&lt;450.0,811.5&gt;&gt; = 10.602386241811988

* uni0454 (U+0454): B&lt;&lt;331.0,573.0&gt;-&lt;319.0,553.0&gt;-&lt;292.0,554.0&gt;&gt;/L&lt;&lt;292.0,554.0&gt;--&lt;695.0,554.0&gt;&gt; = 2.1210963966614473

* uni0454 (U+0454): L&lt;&lt;695.0,350.0&gt;--&lt;308.0,350.0&gt;&gt;/B&lt;&lt;308.0,350.0&gt;-&lt;328.0,348.0&gt;-&lt;338.5,331.5&gt;&gt; = 5.710593137499633

* uni045A (U+045A): L&lt;&lt;108.0,139.0&gt;--&lt;108.0,786.0&gt;&gt;/L&lt;&lt;108.0,786.0&gt;--&lt;100.0,754.0&gt;&gt; = 14.036243467926484

* uni045B (U+045B): L&lt;&lt;410.0,940.0&gt;--&lt;414.0,739.0&gt;&gt;/B&lt;&lt;414.0,739.0&gt;-&lt;421.0,781.0&gt;-&lt;450.0,811.5&gt;&gt; = 10.602386241811988

* uni0463 (U+0463): B&lt;&lt;126.5,915.5&gt;-&lt;130.0,914.0&gt;-&lt;127.0,915.0&gt;&gt;/L&lt;&lt;127.0,915.0&gt;--&lt;190.0,889.0&gt;&gt; = 3.9909130984297856

* uni0465 (U+0465): B&lt;&lt;811.5,920.0&gt;-&lt;848.0,907.0&gt;-&lt;865.0,893.0&gt;&gt;/B&lt;&lt;865.0,893.0&gt;-&lt;860.0,899.0&gt;-&lt;878.0,912.0&gt;&gt; = 10.721969059390938

* uni0466 (U+0466): L&lt;&lt;127.0,161.0&gt;--&lt;125.0,136.0&gt;&gt;/L&lt;&lt;125.0,136.0&gt;--&lt;393.0,1202.0&gt;&gt; = 9.538177123344873

* uni0466 (U+0466): L&lt;&lt;409.0,406.0&gt;--&lt;339.0,122.0&gt;&gt;/B&lt;&lt;339.0,122.0&gt;-&lt;344.0,135.0&gt;-&lt;355.5,131.5&gt;&gt; = 7.1913026135952665

* uni0467 (U+0467): B&lt;&lt;703.0,119.0&gt;-&lt;726.0,146.0&gt;-&lt;736.0,123.0&gt;&gt;/L&lt;&lt;736.0,123.0&gt;--&lt;699.0,240.0&gt;&gt; = 5.949563446884247

* uni0468 (U+0468): B&lt;&lt;715.0,649.5&gt;-&lt;705.0,701.0&gt;-&lt;699.0,768.0&gt;&gt;/B&lt;&lt;699.0,768.0&gt;-&lt;692.0,716.0&gt;-&lt;684.0,666.0&gt;&gt; = 12.784119111786808

* uni0468 (U+0468): L&lt;&lt;254.0,568.0&gt;--&lt;489.0,587.0&gt;&gt;/B&lt;&lt;489.0,587.0&gt;-&lt;471.0,585.0&gt;-&lt;470.5,598.5&gt;&gt; = 1.7178215042254559

* uni0469 (U+0469): B&lt;&lt;557.0,146.0&gt;-&lt;569.0,148.0&gt;-&lt;569.0,133.0&gt;&gt;/L&lt;&lt;569.0,133.0&gt;--&lt;570.0,206.0&gt;&gt; = 0.7848246029917126

* uni0469 (U+0469): L&lt;&lt;256.0,217.0&gt;--&lt;271.0,135.0&gt;&gt;/L&lt;&lt;271.0,135.0&gt;--&lt;269.0,161.0&gt;&gt; = 5.967617248454933

* uni0469 (U+0469): L&lt;&lt;371.0,161.0&gt;--&lt;366.0,142.0&gt;&gt;/L&lt;&lt;366.0,142.0&gt;--&lt;408.0,219.0&gt;&gt; = 13.866896829494456

* uni0469 (U+0469): L&lt;&lt;569.0,133.0&gt;--&lt;570.0,206.0&gt;&gt;/L&lt;&lt;570.0,206.0&gt;--&lt;557.0,146.0&gt;&gt; = 11.440298072743852

* uni0469 (U+0469): L&lt;&lt;59.0,161.0&gt;--&lt;60.0,129.0&gt;&gt;/L&lt;&lt;60.0,129.0&gt;--&lt;60.0,754.0&gt;&gt; = 1.789910608246076

* uni0469 (U+0469): L&lt;&lt;60.0,129.0&gt;--&lt;60.0,754.0&gt;&gt;/L&lt;&lt;60.0,754.0&gt;--&lt;59.0,722.0&gt;&gt; = 1.789910608246076

* uni0469 (U+0469): L&lt;&lt;768.0,213.0&gt;--&lt;770.0,133.0&gt;&gt;/B&lt;&lt;770.0,133.0&gt;-&lt;770.0,149.0&gt;-&lt;784.0,146.0&gt;&gt; = 1.4320961841645452

* uni0469 (U+0469): L&lt;&lt;784.0,146.0&gt;--&lt;768.0,213.0&gt;&gt;/L&lt;&lt;768.0,213.0&gt;--&lt;770.0,133.0&gt;&gt; = 11.998932686517028

* uni046B (U+046B): B&lt;&lt;604.5,685.0&gt;-&lt;641.0,717.0&gt;-&lt;686.0,723.0&gt;&gt;/L&lt;&lt;686.0,723.0&gt;--&lt;397.0,727.0&gt;&gt; = 8.387613904827283

* uni046C (U+046C): L&lt;&lt;407.0,553.0&gt;--&lt;452.0,555.0&gt;&gt;/L&lt;&lt;452.0,555.0&gt;--&lt;245.0,572.0&gt;&gt; = 7.239718659064084

* uni046D (U+046D): B&lt;&lt;761.0,376.5&gt;-&lt;762.0,386.0&gt;-&lt;758.0,403.0&gt;&gt;/L&lt;&lt;758.0,403.0&gt;--&lt;759.0,133.0&gt;&gt; = 13.028314294699063

* uni046D (U+046D): L&lt;&lt;319.0,158.0&gt;--&lt;314.0,140.0&gt;&gt;/L&lt;&lt;314.0,140.0&gt;--&lt;380.0,348.0&gt;&gt; = 2.080522339909582

* uni046D (U+046D): L&lt;&lt;394.0,392.0&gt;--&lt;439.0,391.0&gt;&gt;/L&lt;&lt;439.0,391.0&gt;--&lt;236.0,403.0&gt;&gt; = 2.1099757712738305

* uni046D (U+046D): L&lt;&lt;752.0,730.0&gt;--&lt;572.0,724.0&gt;&gt;/B&lt;&lt;572.0,724.0&gt;-&lt;596.0,719.0&gt;-&lt;622.5,693.0&gt;&gt; = 13.677441365017005

* uni046E (U+046E): B&lt;&lt;871.5,701.5&gt;-&lt;833.0,673.0&gt;-&lt;811.0,678.0&gt;&gt;/B&lt;&lt;811.0,678.0&gt;-&lt;900.0,635.0&gt;-&lt;946.5,570.5&gt;&gt; = 12.983062117527593

* uni046E (U+046E): L&lt;&lt;684.0,1292.0&gt;--&lt;683.0,1292.0&gt;&gt;/B&lt;&lt;683.0,1292.0&gt;-&lt;781.0,1269.0&gt;-&lt;839.5,1219.5&gt;&gt; = 13.207928462779101

* uni046F (U+046F): B&lt;&lt;322.5,898.5&gt;-&lt;378.0,891.0&gt;-&lt;406.0,871.0&gt;&gt;/L&lt;&lt;406.0,871.0&gt;--&lt;121.0,1088.0&gt;&gt; = 1.7480948137265115

* uni046F (U+046F): B&lt;&lt;852.5,527.0&gt;-&lt;827.0,511.0&gt;-&lt;808.0,519.0&gt;&gt;/B&lt;&lt;808.0,519.0&gt;-&lt;875.0,491.0&gt;-&lt;921.0,424.0&gt;&gt; = 0.15309457089095985

* uni0474 (U+0474): B&lt;&lt;451.5,501.5&gt;-&lt;473.0,401.0&gt;-&lt;488.0,316.0&gt;&gt;/B&lt;&lt;488.0,316.0&gt;-&lt;495.0,420.0&gt;-&lt;530.5,594.5&gt;&gt; = 13.858618625352113

* uni0474 (U+0474): L&lt;&lt;338.0,65.0&gt;--&lt;102.0,1116.0&gt;&gt;/L&lt;&lt;102.0,1116.0&gt;--&lt;106.0,1090.0&gt;&gt; = 3.9095717467995468

* uni0476 (U+0476): B&lt;&lt;467.5,418.5&gt;-&lt;489.0,313.0&gt;-&lt;501.0,236.0&gt;&gt;/B&lt;&lt;501.0,236.0&gt;-&lt;500.0,310.0&gt;-&lt;513.5,419.5&gt;&gt; = 8.08373859870028

* uni0476 (U+0476): L&lt;&lt;338.0,65.0&gt;--&lt;102.0,1116.0&gt;&gt;/L&lt;&lt;102.0,1116.0&gt;--&lt;106.0,1090.0&gt;&gt; = 3.9095717467995468

* uni0477 (U+0477): L&lt;&lt;389.0,722.0&gt;--&lt;365.0,762.0&gt;&gt;/L&lt;&lt;365.0,762.0&gt;--&lt;514.0,271.0&gt;&gt; = 14.08268945281852

* uni0478 (U+0478): L&lt;&lt;534.0,856.0&gt;--&lt;540.0,802.0&gt;&gt;/L&lt;&lt;540.0,802.0&gt;--&lt;539.0,854.0&gt;&gt; = 5.238485630703551

* uni048A (U+048A): L&lt;&lt;754.0,129.0&gt;--&lt;754.0,931.0&gt;&gt;/B&lt;&lt;754.0,931.0&gt;-&lt;744.0,874.0&gt;-&lt;705.0,787.0&gt;&gt; = 9.950626687951587

* uni048F (U+048F): B&lt;&lt;438.5,-9.5&gt;-&lt;382.0,24.0&gt;-&lt;373.0,86.0&gt;&gt;/L&lt;&lt;373.0,86.0&gt;--&lt;373.0,-321.0&gt;&gt; = 8.259437979878793

* uni0496 (U+0496): B&lt;&lt;404.0,483.5&gt;-&lt;385.0,530.0&gt;-&lt;403.0,582.0&gt;&gt;/L&lt;&lt;403.0,582.0&gt;--&lt;229.0,122.0&gt;&gt; = 1.626177085129323

* uni0496 (U+0496): B&lt;&lt;814.5,120.0&gt;-&lt;836.0,141.0&gt;-&lt;847.0,117.0&gt;&gt;/L&lt;&lt;847.0,117.0&gt;--&lt;675.0,575.0&gt;&gt; = 4.040105320101284

* uni0496 (U+0496): L&lt;&lt;403.0,582.0&gt;--&lt;229.0,122.0&gt;&gt;/B&lt;&lt;229.0,122.0&gt;-&lt;238.0,141.0&gt;-&lt;259.0,120.0&gt;&gt; = 4.62650685633177

* uni0496 (U+0496): L&lt;&lt;479.0,681.0&gt;--&lt;445.0,1122.0&gt;&gt;/B&lt;&lt;445.0,1122.0&gt;-&lt;446.0,1106.0&gt;-&lt;427.5,1106.5&gt;&gt; = 0.8323060899233623

* uni0496 (U+0496): L&lt;&lt;596.0,683.0&gt;--&lt;821.0,1138.0&gt;&gt;/B&lt;&lt;821.0,1138.0&gt;-&lt;803.0,1111.0&gt;-&lt;783.5,1135.0&gt;&gt; = 7.377419031190935

* uni0496 (U+0496): L&lt;&lt;630.0,365.0&gt;--&lt;630.0,132.0&gt;&gt;/B&lt;&lt;630.0,132.0&gt;-&lt;631.0,146.0&gt;-&lt;650.0,144.5&gt;&gt; = 4.085616779974798

* uni0497 (U+0497): B&lt;&lt;947.5,246.0&gt;-&lt;980.0,185.0&gt;-&lt;999.0,147.0&gt;&gt;/L&lt;&lt;999.0,147.0&gt;--&lt;995.0,161.0&gt;&gt; = 10.619655276155106

* uni0497 (U+0497): L&lt;&lt;409.0,388.0&gt;--&lt;411.0,391.0&gt;&gt;/L&lt;&lt;411.0,391.0&gt;--&lt;282.0,148.0&gt;&gt; = 5.7278353216053715

* uni0497 (U+0497): L&lt;&lt;628.0,593.0&gt;--&lt;762.0,775.0&gt;&gt;/B&lt;&lt;762.0,775.0&gt;-&lt;747.0,756.0&gt;-&lt;732.0,770.0&gt;&gt; = 1.9272946073138673

* uni0499 (U+0499): B&lt;&lt;234.0,916.5&gt;-&lt;257.0,903.0&gt;-&lt;250.0,900.0&gt;&gt;/B&lt;&lt;250.0,900.0&gt;-&lt;273.0,911.0&gt;-&lt;323.0,922.0&gt;&gt; = 2.3613746581755626

* uni049A (U+049A): L&lt;&lt;1012.0,-226.0&gt;--&lt;1012.0,-5.0&gt;&gt;/B&lt;&lt;1012.0,-5.0&gt;-&lt;1010.0,-26.0&gt;-&lt;987.0,-22.0&gt;&gt; = 5.4403320310054815

* uni049C (U+049C): B&lt;&lt;721.0,127.5&gt;-&lt;737.0,135.0&gt;-&lt;757.0,113.0&gt;&gt;/L&lt;&lt;757.0,113.0&gt;--&lt;459.0,650.0&gt;&gt; = 13.246269364654

* uni049C (U+049C): L&lt;&lt;117.0,161.0&gt;--&lt;124.0,128.0&gt;&gt;/L&lt;&lt;124.0,128.0&gt;--&lt;124.0,1123.0&gt;&gt; = 11.976132444203364

* uni049C (U+049C): L&lt;&lt;124.0,128.0&gt;--&lt;124.0,1123.0&gt;&gt;/L&lt;&lt;124.0,1123.0&gt;--&lt;117.0,1090.0&gt;&gt; = 11.976132444203333

* uni049C (U+049C): L&lt;&lt;306.0,675.0&gt;--&lt;306.0,130.0&gt;&gt;/L&lt;&lt;306.0,130.0&gt;--&lt;313.0,161.0&gt;&gt; = 12.724355685422363

* uni049C (U+049C): L&lt;&lt;313.0,1090.0&gt;--&lt;306.0,1120.0&gt;&gt;/L&lt;&lt;306.0,1120.0&gt;--&lt;305.0,816.0&gt;&gt; = 13.322494585526186

* uni049C (U+049C): L&lt;&lt;519.0,890.0&gt;--&lt;714.0,1136.0&gt;&gt;/B&lt;&lt;714.0,1136.0&gt;-&lt;689.0,1107.0&gt;-&lt;667.0,1131.5&gt;&gt; = 2.3603434988352596

* uni049C (U+049C): L&lt;&lt;757.0,113.0&gt;--&lt;459.0,650.0&gt;&gt;/L&lt;&lt;459.0,650.0&gt;--&lt;519.0,492.0&gt;&gt; = 8.233304685936025

* uni049E (U+049E): L&lt;&lt;152.0,1099.0&gt;--&lt;169.0,1099.0&gt;&gt;/L&lt;&lt;169.0,1099.0&gt;--&lt;157.0,1101.0&gt;&gt; = 9.462322208025613

* uni04A0 (U+04A0): L&lt;&lt;469.0,655.0&gt;--&lt;750.0,1140.0&gt;&gt;/B&lt;&lt;750.0,1140.0&gt;-&lt;734.0,1116.0&gt;-&lt;717.5,1121.0&gt;&gt; = 3.602861015674142

* uni04A9 (U+04A9): B&lt;&lt;331.5,239.5&gt;-&lt;372.0,169.0&gt;-&lt;473.0,154.0&gt;&gt;/B&lt;&lt;473.0,154.0&gt;-&lt;450.0,161.0&gt;-&lt;442.5,204.5&gt;&gt; = 8.479985816238528

* uni04AE (U+04AE): L&lt;&lt;614.0,676.0&gt;--&lt;835.0,1065.0&gt;&gt;/L&lt;&lt;835.0,1065.0&gt;--&lt;801.0,1017.0&gt;&gt; = 5.709293314160691

* uni04B0 (U+04B0): L&lt;&lt;614.0,676.0&gt;--&lt;835.0,1065.0&gt;&gt;/L&lt;&lt;835.0,1065.0&gt;--&lt;801.0,1017.0&gt;&gt; = 5.709293314160691

* uni04B4 (U+04B4): L&lt;&lt;421.0,976.0&gt;--&lt;421.0,977.0&gt;&gt;/L&lt;&lt;421.0,977.0&gt;--&lt;418.0,140.0&gt;&gt; = 0.205360337495141

* uni04B4 (U+04B4): L&lt;&lt;984.0,1091.0&gt;--&lt;984.0,128.0&gt;&gt;/L&lt;&lt;984.0,128.0&gt;--&lt;985.0,161.0&gt;&gt; = 1.735704588928346

* uni04BB (U+04BB): L&lt;&lt;416.0,1244.0&gt;--&lt;416.0,805.0&gt;&gt;/B&lt;&lt;416.0,805.0&gt;-&lt;424.0,845.0&gt;-&lt;452.5,874.0&gt;&gt; = 11.309932474020195

* uni04BC (U+04BC): B&lt;&lt;229.5,814.0&gt;-&lt;234.0,796.0&gt;-&lt;235.0,777.0&gt;&gt;/B&lt;&lt;235.0,777.0&gt;-&lt;254.0,913.0&gt;-&lt;312.5,1033.5&gt;&gt; = 10.965869475621751

* uni04BD (U+04BD): B&lt;&lt;253.0,569.0&gt;-&lt;259.0,558.0&gt;-&lt;259.0,534.0&gt;&gt;/B&lt;&lt;259.0,534.0&gt;-&lt;282.0,662.0&gt;-&lt;343.0,750.5&gt;&gt; = 10.186629759944772

* uni04BE (U+04BE): B&lt;&lt;229.5,814.0&gt;-&lt;234.0,796.0&gt;-&lt;235.0,777.0&gt;&gt;/B&lt;&lt;235.0,777.0&gt;-&lt;254.0,913.0&gt;-&lt;312.5,1033.5&gt;&gt; = 10.965869475621751

* uni04BF (U+04BF): B&lt;&lt;253.0,569.0&gt;-&lt;259.0,558.0&gt;-&lt;259.0,534.0&gt;&gt;/B&lt;&lt;259.0,534.0&gt;-&lt;282.0,662.0&gt;-&lt;343.0,750.5&gt;&gt; = 10.186629759944772

* uni04C2 (U+04C2): L&lt;&lt;505.0,141.0&gt;--&lt;505.0,404.0&gt;&gt;/L&lt;&lt;505.0,404.0&gt;--&lt;499.0,375.0&gt;&gt; = 11.689369175439202

* uni04C2 (U+04C2): L&lt;&lt;729.0,375.0&gt;--&lt;723.0,404.0&gt;&gt;/L&lt;&lt;723.0,404.0&gt;--&lt;723.0,141.0&gt;&gt; = 11.689369175439202

* uni04C2 (U+04C2): L&lt;&lt;827.0,831.0&gt;--&lt;826.0,828.0&gt;&gt;/B&lt;&lt;826.0,828.0&gt;-&lt;834.0,844.0&gt;-&lt;843.0,859.0&gt;&gt; = 8.130102354155916

* uni04CD (U+04CD): B&lt;&lt;522.0,731.0&gt;-&lt;542.0,663.0&gt;-&lt;552.0,618.0&gt;&gt;/B&lt;&lt;552.0,618.0&gt;-&lt;552.0,657.0&gt;-&lt;566.5,726.0&gt;&gt; = 12.528807709151522

* uni04CD (U+04CD): L&lt;&lt;109.0,128.0&gt;--&lt;109.0,1123.0&gt;&gt;/L&lt;&lt;109.0,1123.0&gt;--&lt;106.0,1090.0&gt;&gt; = 5.1944289077348

* uni04CD (U+04CD): L&lt;&lt;294.0,872.0&gt;--&lt;294.0,128.0&gt;&gt;/L&lt;&lt;294.0,128.0&gt;--&lt;295.0,161.0&gt;&gt; = 1.735704588928346

* uni04CD (U+04CD): L&lt;&lt;780.0,161.0&gt;--&lt;781.0,128.0&gt;&gt;/L&lt;&lt;781.0,128.0&gt;--&lt;781.0,876.0&gt;&gt; = 1.735704588928346

* uni04CD (U+04CD): L&lt;&lt;967.0,1090.0&gt;--&lt;966.0,1123.0&gt;&gt;/L&lt;&lt;966.0,1123.0&gt;--&lt;966.0,128.0&gt;&gt; = 1.735704588928346

* uni04CE (U+04CE): L&lt;&lt;759.0,131.0&gt;--&lt;759.0,646.0&gt;&gt;/B&lt;&lt;759.0,646.0&gt;-&lt;747.0,587.0&gt;-&lt;723.5,520.0&gt;&gt; = 11.496563017585768

* uni04D4 (U+04D4): L&lt;&lt;117.0,161.0&gt;--&lt;312.0,1129.0&gt;&gt;/B&lt;&lt;312.0,1129.0&gt;-&lt;300.0,1100.0&gt;-&lt;266.5,1117.5&gt;&gt; = 11.089845478556693

* uni04D5 (U+04D5): B&lt;&lt;430.0,540.5&gt;-&lt;449.0,540.0&gt;-&lt;448.0,527.0&gt;&gt;/L&lt;&lt;448.0,527.0&gt;--&lt;445.0,569.0&gt;&gt; = 8.484322134970375

* uni04D5 (U+04D5): B&lt;&lt;531.0,836.0&gt;-&lt;556.0,801.0&gt;-&lt;551.0,786.0&gt;&gt;/B&lt;&lt;551.0,786.0&gt;-&lt;557.0,807.0&gt;-&lt;586.5,841.5&gt;&gt; = 2.4895529219991284

* uni04D5 (U+04D5): B&lt;&lt;603.0,37.5&gt;-&lt;569.0,70.0&gt;-&lt;556.0,97.0&gt;&gt;/B&lt;&lt;556.0,97.0&gt;-&lt;561.0,83.0&gt;-&lt;533.0,49.5&gt;&gt; = 6.0561297227579045

* uni04DD (U+04DD): L&lt;&lt;505.0,141.0&gt;--&lt;505.0,404.0&gt;&gt;/L&lt;&lt;505.0,404.0&gt;--&lt;499.0,375.0&gt;&gt; = 11.689369175439202

* uni04DD (U+04DD): L&lt;&lt;729.0,375.0&gt;--&lt;723.0,404.0&gt;&gt;/L&lt;&lt;723.0,404.0&gt;--&lt;723.0,141.0&gt;&gt; = 11.689369175439202

* uni04DD (U+04DD): L&lt;&lt;827.0,831.0&gt;--&lt;826.0,828.0&gt;&gt;/B&lt;&lt;826.0,828.0&gt;-&lt;834.0,844.0&gt;-&lt;843.0,859.0&gt;&gt; = 8.130102354155916

* uni04E0 (U+04E0): B&lt;&lt;284.5,223.0&gt;-&lt;274.0,204.0&gt;-&lt;270.0,213.0&gt;&gt;/B&lt;&lt;270.0,213.0&gt;-&lt;277.0,201.0&gt;-&lt;296.0,182.5&gt;&gt; = 6.2939481889509645

* uni04E1 (U+04E1): B&lt;&lt;299.0,-184.5&gt;-&lt;289.0,-202.0&gt;-&lt;285.0,-192.0&gt;&gt;/B&lt;&lt;285.0,-192.0&gt;-&lt;300.0,-240.0&gt;-&lt;338.0,-264.5&gt;&gt; = 4.447384850090447

* uni04E9 (U+04E9): B&lt;&lt;327.5,583.0&gt;-&lt;316.0,565.0&gt;-&lt;292.0,564.0&gt;&gt;/L&lt;&lt;292.0,564.0&gt;--&lt;934.0,564.0&gt;&gt; = 2.3859440303887243

* uni04E9 (U+04E9): L&lt;&lt;292.0,564.0&gt;--&lt;934.0,564.0&gt;&gt;/B&lt;&lt;934.0,564.0&gt;-&lt;910.0,565.0&gt;-&lt;899.0,583.0&gt;&gt; = 2.3859440303887243

* uni04E9 (U+04E9): L&lt;&lt;934.0,360.0&gt;--&lt;292.0,360.0&gt;&gt;/B&lt;&lt;292.0,360.0&gt;-&lt;316.0,359.0&gt;-&lt;327.5,341.0&gt;&gt; = 2.3859440303887243

* uni04EB (U+04EB): B&lt;&lt;327.5,583.0&gt;-&lt;316.0,565.0&gt;-&lt;292.0,564.0&gt;&gt;/L&lt;&lt;292.0,564.0&gt;--&lt;934.0,564.0&gt;&gt; = 2.3859440303887243

* uni04EB (U+04EB): L&lt;&lt;292.0,564.0&gt;--&lt;934.0,564.0&gt;&gt;/B&lt;&lt;934.0,564.0&gt;-&lt;910.0,565.0&gt;-&lt;899.0,583.0&gt;&gt; = 2.3859440303887243

* uni04EB (U+04EB): L&lt;&lt;934.0,360.0&gt;--&lt;292.0,360.0&gt;&gt;/B&lt;&lt;292.0,360.0&gt;-&lt;316.0,359.0&gt;-&lt;327.5,341.0&gt;&gt; = 2.3859440303887243

* uni04F5 (U+04F5): L&lt;&lt;825.0,150.0&gt;--&lt;823.0,326.0&gt;&gt;/B&lt;&lt;823.0,326.0&gt;-&lt;820.0,295.0&gt;-&lt;790.0,277.0&gt;&gt; = 6.178600531885615

* uni04F9 (U+04F9): L&lt;&lt;108.0,139.0&gt;--&lt;108.0,786.0&gt;&gt;/L&lt;&lt;108.0,786.0&gt;--&lt;100.0,754.0&gt;&gt; = 14.036243467926484

* uni04F9 (U+04F9): L&lt;&lt;1128.0,754.0&gt;--&lt;1120.0,786.0&gt;&gt;/L&lt;&lt;1120.0,786.0&gt;--&lt;1120.0,139.0&gt;&gt; = 14.036243467926484

* uni04F9 (U+04F9): L&lt;&lt;902.0,139.0&gt;--&lt;902.0,786.0&gt;&gt;/L&lt;&lt;902.0,786.0&gt;--&lt;894.0,754.0&gt;&gt; = 14.036243467926484

* uni0600 (U+0600): L&lt;&lt;49.0,442.0&gt;--&lt;534.0,442.0&gt;&gt;/B&lt;&lt;534.0,442.0&gt;-&lt;514.0,447.0&gt;-&lt;507.5,473.0&gt;&gt; = 14.036243467926484

* uni0602 (U+0602): B&lt;&lt;508.0,272.5&gt;-&lt;495.0,221.0&gt;-&lt;468.0,181.0&gt;&gt;/B&lt;&lt;468.0,181.0&gt;-&lt;480.0,194.0&gt;-&lt;506.5,194.0&gt;&gt; = 8.690039967535016

* uni0604 (U+0604): B&lt;&lt;834.5,485.5&gt;-&lt;800.0,508.0&gt;-&lt;797.0,531.0&gt;&gt;/B&lt;&lt;797.0,531.0&gt;-&lt;795.0,508.0&gt;-&lt;761.5,485.5&gt;&gt; = 12.401148699282784

* uni0604 (U+0604): L&lt;&lt;43.0,407.0&gt;--&lt;209.0,406.0&gt;&gt;/B&lt;&lt;209.0,406.0&gt;-&lt;183.0,410.0&gt;-&lt;175.0,440.0&gt;&gt; = 8.401011139391024

* uni0608 (U+0608): L&lt;&lt;743.0,859.0&gt;--&lt;744.0,859.0&gt;&gt;/B&lt;&lt;744.0,859.0&gt;-&lt;678.0,860.0&gt;-&lt;650.0,830.5&gt;&gt; = 0.8680514497453689

* uni0608 (U+0608): L&lt;&lt;941.0,831.0&gt;--&lt;937.0,726.0&gt;&gt;/B&lt;&lt;937.0,726.0&gt;-&lt;938.0,741.0&gt;-&lt;939.5,759.0&gt;&gt; = 1.632433430738788

* uni060A (U+060A): B&lt;&lt;704.0,448.0&gt;-&lt;729.0,431.0&gt;-&lt;753.0,407.0&gt;&gt;/B&lt;&lt;753.0,407.0&gt;-&lt;720.0,458.0&gt;-&lt;718.0,492.0&gt;&gt; = 12.094757077012089

* uni060A (U+060A): B&lt;&lt;854.5,301.0&gt;-&lt;830.0,317.0&gt;-&lt;807.0,341.0&gt;&gt;/B&lt;&lt;807.0,341.0&gt;-&lt;839.0,293.0&gt;-&lt;841.0,262.0&gt;&gt; = 10.091057238888927

* uni060E (U+060E): B&lt;&lt;508.0,272.5&gt;-&lt;495.0,221.0&gt;-&lt;468.0,181.0&gt;&gt;/B&lt;&lt;468.0,181.0&gt;-&lt;480.0,194.0&gt;-&lt;506.5,194.0&gt;&gt; = 8.690039967535016

* uni0610 (U+0610): B&lt;&lt;372.0,1561.0&gt;-&lt;402.0,1518.0&gt;-&lt;391.0,1448.0&gt;&gt;/B&lt;&lt;391.0,1448.0&gt;-&lt;410.0,1493.0&gt;-&lt;456.5,1537.0&gt;&gt; = 13.959961555829308

* uni0610 (U+0610): B&lt;&lt;468.5,1132.0&gt;-&lt;424.0,1147.0&gt;-&lt;419.0,1188.0&gt;&gt;/B&lt;&lt;419.0,1188.0&gt;-&lt;419.0,1061.0&gt;-&lt;394.0,1002.0&gt;&gt; = 6.952957468173869

* uni0612 (U+0612): L&lt;&lt;312.0,1474.0&gt;--&lt;181.0,1436.0&gt;&gt;/B&lt;&lt;181.0,1436.0&gt;-&lt;197.0,1441.0&gt;-&lt;199.5,1438.5&gt;&gt; = 1.1778312746532906

* uni0613 (U+0613): B&lt;&lt;179.0,1561.0&gt;-&lt;209.0,1518.0&gt;-&lt;198.0,1448.0&gt;&gt;/B&lt;&lt;198.0,1448.0&gt;-&lt;217.0,1493.0&gt;-&lt;263.5,1537.0&gt;&gt; = 13.959961555829308

* uni0613 (U+0613): B&lt;&lt;275.0,1132.5&gt;-&lt;231.0,1148.0&gt;-&lt;226.0,1188.0&gt;&gt;/B&lt;&lt;226.0,1188.0&gt;-&lt;226.0,1061.0&gt;-&lt;201.0,1002.0&gt;&gt; = 7.125016348901757

* uni0615 (U+0615): L&lt;&lt;538.0,1620.0&gt;--&lt;537.0,1269.0&gt;&gt;/B&lt;&lt;537.0,1269.0&gt;-&lt;544.0,1365.0&gt;-&lt;599.5,1417.5&gt;&gt; = 4.007201127423053

* uni061C (U+061C): L&lt;&lt;613.0,1353.0&gt;--&lt;529.0,1314.0&gt;&gt;/B&lt;&lt;529.0,1314.0&gt;-&lt;545.0,1319.0&gt;-&lt;546.5,1311.0&gt;&gt; = 7.550744171833916

* uni0620.medi: B&lt;&lt;578.0,291.0&gt;-&lt;572.0,303.0&gt;-&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;570.0,301.0&gt;-&lt;560.0,285.0&gt;&gt; = 9.593134262730318

* uni0621 (U+FE80): B&lt;&lt;338.0,347.0&gt;-&lt;392.0,392.0&gt;-&lt;447.0,437.0&gt;&gt;/B&lt;&lt;447.0,437.0&gt;-&lt;423.0,421.0&gt;-&lt;380.5,446.5&gt;&gt; = 5.599339336520549

* uni0622.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0623 (U+FE83): B&lt;&lt;413.0,1377.5&gt;-&lt;464.0,1405.0&gt;-&lt;515.0,1418.0&gt;&gt;/B&lt;&lt;515.0,1418.0&gt;-&lt;465.0,1414.0&gt;-&lt;424.0,1466.5&gt;&gt; = 9.726356189284708

* uni0623.fina.alt: B&lt;&lt;651.0,1377.5&gt;-&lt;702.0,1405.0&gt;-&lt;753.0,1418.0&gt;&gt;/B&lt;&lt;753.0,1418.0&gt;-&lt;703.0,1414.0&gt;-&lt;662.0,1466.5&gt;&gt; = 9.726356189284708

* uni0623.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0624 (U+FE85): B&lt;&lt;274.0,1068.5&gt;-&lt;325.0,1096.0&gt;-&lt;376.0,1109.0&gt;&gt;/B&lt;&lt;376.0,1109.0&gt;-&lt;326.0,1105.0&gt;-&lt;285.0,1157.5&gt;&gt; = 9.726356189284708

* uni0625 (U+FE87): B&lt;&lt;415.0,-299.5&gt;-&lt;466.0,-272.0&gt;-&lt;517.0,-259.0&gt;&gt;/B&lt;&lt;517.0,-259.0&gt;-&lt;467.0,-263.0&gt;-&lt;426.0,-210.5&gt;&gt; = 9.726356189284708

* uni0625.fina.alt: B&lt;&lt;653.0,-291.5&gt;-&lt;704.0,-264.0&gt;-&lt;755.0,-251.0&gt;&gt;/B&lt;&lt;755.0,-251.0&gt;-&lt;705.0,-255.0&gt;-&lt;664.0,-202.5&gt;&gt; = 9.726356189284708

* uni0625.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0626 (U+FE89): B&lt;&lt;327.0,1309.5&gt;-&lt;378.0,1337.0&gt;-&lt;429.0,1350.0&gt;&gt;/B&lt;&lt;429.0,1350.0&gt;-&lt;379.0,1346.0&gt;-&lt;338.0,1398.5&gt;&gt; = 9.726356189284708

* uni0627.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0637 (U+FEC1): L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uni0638 (U+FEC5): L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uni063D.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni063E.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni063F.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0641 (U+FED1): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni0643 (U+FED9): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni0651 (U+0651): B&lt;&lt;580.5,1380.5&gt;-&lt;539.0,1413.0&gt;-&lt;537.0,1436.0&gt;&gt;/B&lt;&lt;537.0,1436.0&gt;-&lt;534.0,1413.0&gt;-&lt;492.5,1380.5&gt;&gt; = 12.401148699282784

* uni0654 (U+0654): B&lt;&lt;327.0,1383.5&gt;-&lt;378.0,1411.0&gt;-&lt;429.0,1424.0&gt;&gt;/B&lt;&lt;429.0,1424.0&gt;-&lt;379.0,1420.0&gt;-&lt;338.0,1472.5&gt;&gt; = 9.726356189284708

* uni0655 (U+0655): B&lt;&lt;315.0,-875.5&gt;-&lt;366.0,-848.0&gt;-&lt;417.0,-835.0&gt;&gt;/B&lt;&lt;417.0,-835.0&gt;-&lt;367.0,-839.0&gt;-&lt;326.0,-786.5&gt;&gt; = 9.726356189284708

* uni065F (U+065F): B&lt;&lt;460.5,-801.5&gt;-&lt;492.0,-822.0&gt;-&lt;510.0,-840.0&gt;&gt;/B&lt;&lt;510.0,-840.0&gt;-&lt;479.0,-792.0&gt;-&lt;478.0,-737.0&gt;&gt; = 12.144278049566983

* uni0663 (U+06F3): B&lt;&lt;622.0,1018.0&gt;-&lt;611.0,1056.0&gt;-&lt;609.0,1069.0&gt;&gt;/B&lt;&lt;609.0,1069.0&gt;-&lt;610.0,1056.0&gt;-&lt;602.5,1017.0&gt;&gt; = 4.347456907559587

* uni066E.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni066F.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni0671 (U+FB50): B&lt;&lt;546.5,1618.5&gt;-&lt;556.0,1594.0&gt;-&lt;553.0,1583.0&gt;&gt;/B&lt;&lt;553.0,1583.0&gt;-&lt;588.0,1693.0&gt;-&lt;677.5,1771.0&gt;&gt; = 2.3950055168722097

* uni0671.fina.alt: B&lt;&lt;784.5,1618.5&gt;-&lt;794.0,1594.0&gt;-&lt;791.0,1583.0&gt;&gt;/B&lt;&lt;791.0,1583.0&gt;-&lt;826.0,1693.0&gt;-&lt;915.5,1771.0&gt;&gt; = 2.3950055168722097

* uni0671.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0672 (U+0672): B&lt;&lt;464.5,1545.5&gt;-&lt;496.0,1525.0&gt;-&lt;514.0,1507.0&gt;&gt;/B&lt;&lt;514.0,1507.0&gt;-&lt;483.0,1555.0&gt;-&lt;482.0,1610.0&gt;&gt; = 12.144278049566983

* uni0672.fina.alt: B&lt;&lt;702.5,1545.5&gt;-&lt;734.0,1525.0&gt;-&lt;752.0,1507.0&gt;&gt;/B&lt;&lt;752.0,1507.0&gt;-&lt;721.0,1555.0&gt;-&lt;720.0,1610.0&gt;&gt; = 12.144278049566983

* uni0672.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0672.fina: B&lt;&lt;378.5,1545.5&gt;-&lt;410.0,1525.0&gt;-&lt;428.0,1507.0&gt;&gt;/B&lt;&lt;428.0,1507.0&gt;-&lt;397.0,1555.0&gt;-&lt;396.0,1610.0&gt;&gt; = 12.144278049566983

* uni0673 (U+0673): B&lt;&lt;464.5,-129.5&gt;-&lt;496.0,-150.0&gt;-&lt;514.0,-168.0&gt;&gt;/B&lt;&lt;514.0,-168.0&gt;-&lt;483.0,-120.0&gt;-&lt;482.0,-65.0&gt;&gt; = 12.144278049566983

* uni0673.fina.alt: B&lt;&lt;702.5,-115.5&gt;-&lt;734.0,-136.0&gt;-&lt;752.0,-154.0&gt;&gt;/B&lt;&lt;752.0,-154.0&gt;-&lt;721.0,-106.0&gt;-&lt;720.0,-51.0&gt;&gt; = 12.144278049566983

* uni0673.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0673.fina: B&lt;&lt;378.5,-115.5&gt;-&lt;410.0,-136.0&gt;-&lt;428.0,-154.0&gt;&gt;/B&lt;&lt;428.0,-154.0&gt;-&lt;397.0,-106.0&gt;-&lt;396.0,-51.0&gt;&gt; = 12.144278049566983

* uni0674 (U+0674): B&lt;&lt;338.0,859.0&gt;-&lt;392.0,904.0&gt;-&lt;447.0,949.0&gt;&gt;/B&lt;&lt;447.0,949.0&gt;-&lt;423.0,933.0&gt;-&lt;380.5,958.5&gt;&gt; = 5.599339336520549

* uni0675 (U+0675): B&lt;&lt;578.0,859.0&gt;-&lt;632.0,904.0&gt;-&lt;687.0,949.0&gt;&gt;/B&lt;&lt;687.0,949.0&gt;-&lt;663.0,933.0&gt;-&lt;620.5,958.5&gt;&gt; = 5.599339336520549

* uni0679 (U+FB66): L&lt;&lt;565.0,1716.0&gt;--&lt;564.0,1365.0&gt;&gt;/B&lt;&lt;564.0,1365.0&gt;-&lt;571.0,1461.0&gt;-&lt;626.5,1513.5&gt;&gt; = 4.007201127423053

* uni067D.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0681 (U+0681): B&lt;&lt;327.0,1141.5&gt;-&lt;378.0,1169.0&gt;-&lt;429.0,1182.0&gt;&gt;/B&lt;&lt;429.0,1182.0&gt;-&lt;379.0,1178.0&gt;-&lt;338.0,1230.5&gt;&gt; = 9.726356189284708

* uni0681.fina: B&lt;&lt;327.0,1141.5&gt;-&lt;378.0,1169.0&gt;-&lt;429.0,1182.0&gt;&gt;/B&lt;&lt;429.0,1182.0&gt;-&lt;379.0,1178.0&gt;-&lt;338.0,1230.5&gt;&gt; = 9.726356189284708

* uni0681.init: B&lt;&lt;327.0,1313.5&gt;-&lt;378.0,1341.0&gt;-&lt;429.0,1354.0&gt;&gt;/B&lt;&lt;429.0,1354.0&gt;-&lt;379.0,1350.0&gt;-&lt;338.0,1402.5&gt;&gt; = 9.726356189284708

* uni0681.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni0681.medi: B&lt;&lt;327.0,1313.5&gt;-&lt;378.0,1341.0&gt;-&lt;429.0,1354.0&gt;&gt;/B&lt;&lt;429.0,1354.0&gt;-&lt;379.0,1350.0&gt;-&lt;338.0,1402.5&gt;&gt; = 9.726356189284708

* uni0682.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni0685.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni0686 (U+FB7A): B&lt;&lt;469.0,381.0&gt;-&lt;388.0,314.0&gt;-&lt;327.0,235.0&gt;&gt;/B&lt;&lt;327.0,235.0&gt;-&lt;350.0,257.0&gt;-&lt;374.0,272.5&gt;&gt; = 8.599436680226221

* uni0688 (U+FB88): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;/B&lt;&lt;394.0,1433.0&gt;-&lt;401.0,1529.0&gt;-&lt;456.5,1581.5&gt;&gt; = 4.007201127423053

* uni068B (U+068B): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;/B&lt;&lt;394.0,1433.0&gt;-&lt;401.0,1529.0&gt;-&lt;456.5,1581.5&gt;&gt; = 4.007201127423053

* uni068B.fina: L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;/B&lt;&lt;334.0,1433.0&gt;-&lt;341.0,1529.0&gt;-&lt;396.5,1581.5&gt;&gt; = 4.007201127423053

* uni0691 (U+FB8C): L&lt;&lt;538.0,1602.0&gt;--&lt;537.0,1251.0&gt;&gt;/B&lt;&lt;537.0,1251.0&gt;-&lt;544.0,1347.0&gt;-&lt;599.5,1399.5&gt;&gt; = 4.007201127423053

* uni069D.fina: B&lt;&lt;910.0,508.0&gt;-&lt;855.0,416.0&gt;-&lt;753.0,395.0&gt;&gt;/L&lt;&lt;753.0,395.0&gt;--&lt;1229.0,402.0&gt;&gt; = 10.791109738200037

* uni069D.init: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni069D.medi: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni069E.fina: B&lt;&lt;910.0,508.0&gt;-&lt;855.0,416.0&gt;-&lt;753.0,395.0&gt;&gt;/L&lt;&lt;753.0,395.0&gt;--&lt;1229.0,402.0&gt;&gt; = 10.791109738200037

* uni069E.init: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni069E.medi: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni069F (U+069F): L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uni069F.fina: L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uni069F.init: L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uni069F.medi: L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uni06A0.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni06A0.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni06A1 (U+06A1): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni06A1.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni06A2 (U+06A2): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni06A2.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni06A3 (U+06A3): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni06A3.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni06A4 (U+FB6A): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni06A5 (U+06A5): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni06A5.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni06A6 (U+FB6E): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni06A7.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni06A8.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni06AC (U+06AC): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni06AC.fina: L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni06AD (U+FBD3): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni06AD (U+FBD3): L&lt;&lt;854.0,793.0&gt;--&lt;851.0,1418.0&gt;&gt;/B&lt;&lt;851.0,1418.0&gt;-&lt;846.0,1386.0&gt;-&lt;815.0,1347.0&gt;&gt; = 9.155676780060624

* uni06AE (U+06AE): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni06AE.fina: L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni06B1 (U+FB9A): L&lt;&lt;207.0,1241.0&gt;--&lt;510.0,1545.0&gt;&gt;/B&lt;&lt;510.0,1545.0&gt;-&lt;478.0,1523.0&gt;-&lt;457.0,1520.0&gt;&gt; = 10.585868655952787

* uni06B4.init: B&lt;&lt;457.0,760.0&gt;-&lt;475.0,758.0&gt;-&lt;501.0,740.0&gt;&gt;/L&lt;&lt;501.0,740.0&gt;--&lt;465.0,777.0&gt;&gt; = 11.089671071757897

* uni06B4.init: L&lt;&lt;833.0,403.0&gt;--&lt;599.0,641.0&gt;&gt;/B&lt;&lt;599.0,641.0&gt;-&lt;623.0,604.0&gt;-&lt;626.0,580.0&gt;&gt; = 11.545050266529739

* uni06B6.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;544.5,265.5&gt;&gt; = 5.710593137499633

* uni06B8 (U+06B8): B&lt;&lt;154.0,-267.0&gt;-&lt;157.0,-267.0&gt;-&lt;159.0,-268.0&gt;&gt;/B&lt;&lt;159.0,-268.0&gt;-&lt;83.0,-205.0&gt;-&lt;39.5,-107.5&gt;&gt; = 13.091893064346833

* uni06B8.fina: B&lt;&lt;154.0,-267.0&gt;-&lt;157.0,-267.0&gt;-&lt;159.0,-268.0&gt;&gt;/B&lt;&lt;159.0,-268.0&gt;-&lt;83.0,-205.0&gt;-&lt;39.5,-107.5&gt;&gt; = 13.091893064346833

* uni06B8.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;544.5,265.5&gt;&gt; = 5.710593137499633

* uni06B9.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni06BA.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni06BB (U+FBA0): L&lt;&lt;538.0,1569.0&gt;--&lt;537.0,1218.0&gt;&gt;/B&lt;&lt;537.0,1218.0&gt;-&lt;544.0,1314.0&gt;-&lt;599.5,1366.5&gt;&gt; = 4.007201127423053

* uni06BD.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni06BE (U+FBAA): B&lt;&lt;697.5,222.0&gt;-&lt;684.0,224.0&gt;-&lt;688.0,234.0&gt;&gt;/B&lt;&lt;688.0,234.0&gt;-&lt;602.0,111.0&gt;-&lt;493.0,46.0&gt;&gt; = 13.159335726495803

* uni06BE.init.comp: B&lt;&lt;434.5,470.0&gt;-&lt;445.0,452.0&gt;-&lt;467.0,437.0&gt;&gt;/B&lt;&lt;467.0,437.0&gt;-&lt;465.0,439.0&gt;-&lt;480.0,447.0&gt;&gt; = 10.713123022790997

* uni06BE.init.comp: B&lt;&lt;816.0,674.5&gt;-&lt;804.0,734.0&gt;-&lt;802.0,781.0&gt;&gt;/B&lt;&lt;802.0,781.0&gt;-&lt;802.0,651.0&gt;-&lt;784.5,551.5&gt;&gt; = 2.436648246810141

* uni06BF (U+06BF): B&lt;&lt;469.0,381.0&gt;-&lt;388.0,314.0&gt;-&lt;327.0,235.0&gt;&gt;/B&lt;&lt;327.0,235.0&gt;-&lt;350.0,257.0&gt;-&lt;374.0,272.5&gt;&gt; = 8.599436680226221

* uni06BF.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni06C0 (U+FBA4): B&lt;&lt;327.0,1322.5&gt;-&lt;378.0,1350.0&gt;-&lt;429.0,1363.0&gt;&gt;/B&lt;&lt;429.0,1363.0&gt;-&lt;379.0,1359.0&gt;-&lt;338.0,1411.5&gt;&gt; = 9.726356189284708

* uni06C2 (U+06C2): B&lt;&lt;454.0,1375.5&gt;-&lt;505.0,1403.0&gt;-&lt;556.0,1416.0&gt;&gt;/B&lt;&lt;556.0,1416.0&gt;-&lt;506.0,1412.0&gt;-&lt;465.0,1464.5&gt;&gt; = 9.726356189284708

* uni06CE.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni06D1.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni06D3 (U+FBB0): B&lt;&lt;98.0,1209.5&gt;-&lt;149.0,1237.0&gt;-&lt;200.0,1250.0&gt;&gt;/B&lt;&lt;200.0,1250.0&gt;-&lt;150.0,1246.0&gt;-&lt;109.0,1298.5&gt;&gt; = 9.726356189284708

* uni06DC (U+06DC): B&lt;&lt;790.0,1411.5&gt;-&lt;763.0,1429.0&gt;-&lt;766.0,1439.0&gt;&gt;/B&lt;&lt;766.0,1439.0&gt;-&lt;764.0,1428.0&gt;-&lt;737.5,1412.5&gt;&gt; = 6.3943977652276

* uni06DE (U+06DE): B&lt;&lt;414.0,562.0&gt;-&lt;442.0,586.0&gt;-&lt;472.0,603.0&gt;&gt;/L&lt;&lt;472.0,603.0&gt;--&lt;404.0,575.0&gt;&gt; = 7.158647207598488

* uni06DE (U+06DE): L&lt;&lt;136.0,451.0&gt;--&lt;146.0,407.0&gt;&gt;/L&lt;&lt;146.0,407.0&gt;--&lt;146.0,494.0&gt;&gt; = 12.80426606528674

* uni06DE (U+06DE): L&lt;&lt;146.0,407.0&gt;--&lt;146.0,494.0&gt;&gt;/L&lt;&lt;146.0,494.0&gt;--&lt;136.0,451.0&gt;&gt; = 13.091893064346833

* uni06DE (U+06DE): L&lt;&lt;229.0,698.0&gt;--&lt;290.0,758.0&gt;&gt;/L&lt;&lt;290.0,758.0&gt;--&lt;253.0,734.0&gt;&gt; = 11.55708803780295

* uni06DE (U+06DE): L&lt;&lt;253.0,167.0&gt;--&lt;290.0,143.0&gt;&gt;/L&lt;&lt;290.0,143.0&gt;--&lt;229.0,204.0&gt;&gt; = 12.030596096537908

* uni06DE (U+06DE): L&lt;&lt;253.0,734.0&gt;--&lt;229.0,698.0&gt;&gt;/L&lt;&lt;229.0,698.0&gt;--&lt;290.0,758.0&gt;&gt; = 11.783440532755144

* uni06DE (U+06DE): L&lt;&lt;290.0,143.0&gt;--&lt;229.0,204.0&gt;&gt;/L&lt;&lt;229.0,204.0&gt;--&lt;253.0,167.0&gt;&gt; = 12.030596096537877

* uni06DE (U+06DE): L&lt;&lt;493.0,841.0&gt;--&lt;580.0,841.0&gt;&gt;/L&lt;&lt;580.0,841.0&gt;--&lt;537.0,851.0&gt;&gt; = 13.091893064346861

* uni06DE (U+06DE): L&lt;&lt;537.0,50.0&gt;--&lt;580.0,60.0&gt;&gt;/L&lt;&lt;580.0,60.0&gt;--&lt;493.0,60.0&gt;&gt; = 13.091893064346833

* uni06DE (U+06DE): L&lt;&lt;537.0,851.0&gt;--&lt;493.0,841.0&gt;&gt;/L&lt;&lt;493.0,841.0&gt;--&lt;580.0,841.0&gt;&gt; = 12.80426606528674

* uni06DE (U+06DE): L&lt;&lt;580.0,60.0&gt;--&lt;493.0,60.0&gt;&gt;/L&lt;&lt;493.0,60.0&gt;--&lt;537.0,50.0&gt;&gt; = 12.80426606528674

* uni06DE (U+06DE): L&lt;&lt;784.0,758.0&gt;--&lt;844.0,698.0&gt;&gt;/L&lt;&lt;844.0,698.0&gt;--&lt;820.0,734.0&gt;&gt; = 11.309932474020227

* uni06DE (U+06DE): L&lt;&lt;820.0,167.0&gt;--&lt;844.0,204.0&gt;&gt;/L&lt;&lt;844.0,204.0&gt;--&lt;784.0,143.0&gt;&gt; = 11.55708803780295

* uni06DE (U+06DE): L&lt;&lt;820.0,734.0&gt;--&lt;784.0,758.0&gt;&gt;/L&lt;&lt;784.0,758.0&gt;--&lt;844.0,698.0&gt;&gt; = 11.309932474020227

* uni06DE (U+06DE): L&lt;&lt;844.0,204.0&gt;--&lt;784.0,143.0&gt;&gt;/L&lt;&lt;784.0,143.0&gt;--&lt;820.0,167.0&gt;&gt; = 11.783440532755144

* uni06DE (U+06DE): L&lt;&lt;927.0,494.0&gt;--&lt;927.0,407.0&gt;&gt;/L&lt;&lt;927.0,407.0&gt;--&lt;937.0,451.0&gt;&gt; = 12.80426606528674

* uni06DE (U+06DE): L&lt;&lt;937.0,451.0&gt;--&lt;927.0,494.0&gt;&gt;/L&lt;&lt;927.0,494.0&gt;--&lt;927.0,407.0&gt;&gt; = 13.091893064346833

* uni06E3 (U+06E3): B&lt;&lt;790.0,-695.5&gt;-&lt;763.0,-678.0&gt;-&lt;766.0,-668.0&gt;&gt;/B&lt;&lt;766.0,-668.0&gt;-&lt;764.0,-679.0&gt;-&lt;737.5,-694.5&gt;&gt; = 6.3943977652276

* uni06E6 (U+06E6): B&lt;&lt;381.0,-22.5&gt;-&lt;356.0,-63.0&gt;-&lt;340.0,-66.0&gt;&gt;/L&lt;&lt;340.0,-66.0&gt;--&lt;776.0,-66.0&gt;&gt; = 10.61965527615514

* uni06E7 (U+06E7): B&lt;&lt;381.0,1206.5&gt;-&lt;356.0,1166.0&gt;-&lt;340.0,1163.0&gt;&gt;/L&lt;&lt;340.0,1163.0&gt;--&lt;776.0,1163.0&gt;&gt; = 10.61965527615514

* uni06E9 (U+06E9): B&lt;&lt;334.5,558.0&gt;-&lt;342.0,583.0&gt;-&lt;358.0,603.0&gt;&gt;/L&lt;&lt;358.0,603.0&gt;--&lt;297.0,540.0&gt;&gt; = 5.4161463931371445

* uni06E9 (U+06E9): L&lt;&lt;537.0,789.0&gt;--&lt;378.0,624.0&gt;&gt;/B&lt;&lt;378.0,624.0&gt;-&lt;396.0,638.0&gt;-&lt;418.0,642.0&gt;&gt; = 8.185928039165995

* uni06F4 (U+06F4): B&lt;&lt;640.0,596.0&gt;-&lt;574.0,627.0&gt;-&lt;559.0,683.0&gt;&gt;/B&lt;&lt;559.0,683.0&gt;-&lt;593.0,558.0&gt;-&lt;611.5,403.0&gt;&gt; = 0.22124758284497256

* uni06FB.fina: B&lt;&lt;910.0,508.0&gt;-&lt;855.0,416.0&gt;-&lt;753.0,395.0&gt;&gt;/L&lt;&lt;753.0,395.0&gt;--&lt;1229.0,402.0&gt;&gt; = 10.791109738200037

* uni06FB.init: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni06FB.medi: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni06FC.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni06FC.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni06FD (U+06FD): B&lt;&lt;315.0,478.0&gt;-&lt;369.0,523.0&gt;-&lt;424.0,568.0&gt;&gt;/B&lt;&lt;424.0,568.0&gt;-&lt;400.0,552.0&gt;-&lt;357.5,577.5&gt;&gt; = 5.599339336520549

* uni06FF.init: B&lt;&lt;336.5,401.5&gt;-&lt;375.0,400.0&gt;-&lt;406.0,393.0&gt;&gt;/B&lt;&lt;406.0,393.0&gt;-&lt;320.0,421.0&gt;-&lt;268.5,491.5&gt;&gt; = 5.309929881707482

* uni06FF.init: B&lt;&lt;821.0,822.5&gt;-&lt;803.0,882.0&gt;-&lt;801.0,928.0&gt;&gt;/B&lt;&lt;801.0,928.0&gt;-&lt;804.0,812.0&gt;-&lt;778.0,704.0&gt;&gt; = 1.0080957511116757

* uni06FF.medi: B&lt;&lt;841.5,477.0&gt;-&lt;794.0,412.0&gt;-&lt;720.0,403.0&gt;&gt;/L&lt;&lt;720.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt; = 7.045172321115355

* uni0750.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0751.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0752.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0753.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0754.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0755.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0756.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0757 (U+0757): B&lt;&lt;325.0,-226.0&gt;-&lt;280.0,-187.0&gt;-&lt;253.0,-145.0&gt;&gt;/B&lt;&lt;253.0,-145.0&gt;-&lt;279.0,-217.0&gt;-&lt;345.5,-263.5&gt;&gt; = 12.88001190278654

* uni0757.fina: B&lt;&lt;325.0,-226.0&gt;-&lt;280.0,-187.0&gt;-&lt;253.0,-145.0&gt;&gt;/B&lt;&lt;253.0,-145.0&gt;-&lt;279.0,-217.0&gt;-&lt;345.5,-263.5&gt;&gt; = 12.88001190278654

* uni0757.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni0758.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni0759 (U+0759): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;/B&lt;&lt;394.0,1433.0&gt;-&lt;401.0,1529.0&gt;-&lt;456.5,1581.5&gt;&gt; = 4.007201127423053

* uni0759.fina: L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;/B&lt;&lt;334.0,1433.0&gt;-&lt;341.0,1529.0&gt;-&lt;396.5,1581.5&gt;&gt; = 4.007201127423053

* uni075A (U+075A): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;/B&lt;&lt;394.0,1433.0&gt;-&lt;401.0,1529.0&gt;-&lt;456.5,1581.5&gt;&gt; = 4.007201127423053

* uni075A.fina: L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;/B&lt;&lt;334.0,1433.0&gt;-&lt;341.0,1529.0&gt;-&lt;396.5,1581.5&gt;&gt; = 4.007201127423053

* uni075D.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni075D.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni075E.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni075E.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni075F.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni075F.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni0760 (U+0760): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni0760.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni0761 (U+0761): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni0761.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni0767.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0768 (U+0768): L&lt;&lt;573.0,1784.0&gt;--&lt;572.0,1433.0&gt;&gt;/B&lt;&lt;572.0,1433.0&gt;-&lt;579.0,1529.0&gt;-&lt;634.5,1581.5&gt;&gt; = 4.007201127423053

* uni0768.fina: L&lt;&lt;563.0,1620.0&gt;--&lt;562.0,1269.0&gt;&gt;/B&lt;&lt;562.0,1269.0&gt;-&lt;569.0,1365.0&gt;-&lt;624.5,1417.5&gt;&gt; = 4.007201127423053

* uni0768.init: L&lt;&lt;481.0,1784.0&gt;--&lt;480.0,1433.0&gt;&gt;/B&lt;&lt;480.0,1433.0&gt;-&lt;487.0,1529.0&gt;-&lt;542.5,1581.5&gt;&gt; = 4.007201127423053

* uni0768.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0768.medi: L&lt;&lt;573.0,1716.0&gt;--&lt;572.0,1365.0&gt;&gt;/B&lt;&lt;572.0,1365.0&gt;-&lt;579.0,1461.0&gt;-&lt;634.5,1513.5&gt;&gt; = 4.007201127423053

* uni0769.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni076A.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;544.5,265.5&gt;&gt; = 5.710593137499633

* uni076C (U+076C): B&lt;&lt;229.0,1045.5&gt;-&lt;280.0,1073.0&gt;-&lt;331.0,1086.0&gt;&gt;/B&lt;&lt;331.0,1086.0&gt;-&lt;281.0,1082.0&gt;-&lt;240.0,1134.5&gt;&gt; = 9.726356189284708

* uni076C.fina: B&lt;&lt;229.0,988.5&gt;-&lt;280.0,1016.0&gt;-&lt;331.0,1029.0&gt;&gt;/B&lt;&lt;331.0,1029.0&gt;-&lt;281.0,1025.0&gt;-&lt;240.0,1077.5&gt;&gt; = 9.726356189284708

* uni076E (U+076E): B&lt;&lt;448.0,-284.0&gt;-&lt;398.0,-284.0&gt;-&lt;346.0,-264.0&gt;&gt;/B&lt;&lt;346.0,-264.0&gt;-&lt;380.0,-285.0&gt;-&lt;428.0,-297.0&gt;&gt; = 10.663918644083887

* uni076E (U+076E): L&lt;&lt;583.0,358.0&gt;--&lt;582.0,7.0&gt;&gt;/B&lt;&lt;582.0,7.0&gt;-&lt;589.0,103.0&gt;-&lt;644.5,155.5&gt;&gt; = 4.007201127423053

* uni076E.fina: B&lt;&lt;448.0,-284.0&gt;-&lt;398.0,-284.0&gt;-&lt;346.0,-264.0&gt;&gt;/B&lt;&lt;346.0,-264.0&gt;-&lt;380.0,-285.0&gt;-&lt;428.0,-297.0&gt;&gt; = 10.663918644083887

* uni076E.fina: L&lt;&lt;583.0,358.0&gt;--&lt;582.0,7.0&gt;&gt;/B&lt;&lt;582.0,7.0&gt;-&lt;589.0,103.0&gt;-&lt;644.0,155.5&gt;&gt; = 4.007201127423053

* uni076E.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni076E.init: L&lt;&lt;501.0,-59.0&gt;--&lt;500.0,-410.0&gt;&gt;/B&lt;&lt;500.0,-410.0&gt;-&lt;507.0,-314.0&gt;-&lt;562.5,-261.5&gt;&gt; = 4.007201127423053

* uni076E.medi: L&lt;&lt;501.0,-59.0&gt;--&lt;500.0,-410.0&gt;&gt;/B&lt;&lt;500.0,-410.0&gt;-&lt;507.0,-314.0&gt;-&lt;562.5,-261.5&gt;&gt; = 4.007201127423053

* uni076F (U+076F): B&lt;&lt;452.0,-296.0&gt;-&lt;429.0,-296.0&gt;-&lt;403.0,-291.0&gt;&gt;/B&lt;&lt;403.0,-291.0&gt;-&lt;460.0,-309.0&gt;-&lt;537.0,-308.0&gt;&gt; = 6.640041319064085

* uni076F (U+076F): B&lt;&lt;673.0,-294.5&gt;-&lt;725.0,-280.0&gt;-&lt;758.0,-257.0&gt;&gt;/B&lt;&lt;758.0,-257.0&gt;-&lt;715.0,-275.0&gt;-&lt;663.5,-285.5&gt;&gt; = 12.160915991434917

* uni076F (U+076F): L&lt;&lt;587.0,346.0&gt;--&lt;586.0,-5.0&gt;&gt;/B&lt;&lt;586.0,-5.0&gt;-&lt;593.0,91.0&gt;-&lt;648.5,143.5&gt;&gt; = 4.007201127423053

* uni076F.fina: B&lt;&lt;452.0,-296.0&gt;-&lt;431.0,-296.0&gt;-&lt;408.0,-292.0&gt;&gt;/B&lt;&lt;408.0,-292.0&gt;-&lt;464.0,-309.0&gt;-&lt;539.0,-308.0&gt;&gt; = 7.020984180859628

* uni076F.fina: B&lt;&lt;677.5,-294.0&gt;-&lt;730.0,-279.0&gt;-&lt;763.0,-255.0&gt;&gt;/B&lt;&lt;763.0,-255.0&gt;-&lt;719.0,-274.0&gt;-&lt;666.5,-285.0&gt;&gt; = 12.671808525817573

* uni076F.fina: L&lt;&lt;587.0,346.0&gt;--&lt;586.0,-5.0&gt;&gt;/B&lt;&lt;586.0,-5.0&gt;-&lt;593.0,91.0&gt;-&lt;648.5,143.5&gt;&gt; = 4.007201127423053

* uni076F.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni076F.init: L&lt;&lt;501.0,-37.0&gt;--&lt;500.0,-388.0&gt;&gt;/B&lt;&lt;500.0,-388.0&gt;-&lt;507.0,-292.0&gt;-&lt;562.5,-239.5&gt;&gt; = 4.007201127423053

* uni076F.medi: L&lt;&lt;501.0,-37.0&gt;--&lt;500.0,-388.0&gt;&gt;/B&lt;&lt;500.0,-388.0&gt;-&lt;507.0,-292.0&gt;-&lt;562.5,-239.5&gt;&gt; = 4.007201127423053

* uni0771 (U+0771): L&lt;&lt;538.0,1604.0&gt;--&lt;537.0,1253.0&gt;&gt;/B&lt;&lt;537.0,1253.0&gt;-&lt;544.0,1349.0&gt;-&lt;599.5,1401.5&gt;&gt; = 4.007201127423053

* uni0771.fina: L&lt;&lt;538.0,1546.0&gt;--&lt;537.0,1195.0&gt;&gt;/B&lt;&lt;537.0,1195.0&gt;-&lt;544.0,1291.0&gt;-&lt;599.5,1343.5&gt;&gt; = 4.007201127423053

* uni0772 (U+0772): L&lt;&lt;526.0,1602.0&gt;--&lt;525.0,1251.0&gt;&gt;/B&lt;&lt;525.0,1251.0&gt;-&lt;532.0,1347.0&gt;-&lt;587.5,1399.5&gt;&gt; = 4.007201127423053

* uni0772.fina: L&lt;&lt;526.0,1602.0&gt;--&lt;525.0,1251.0&gt;&gt;/B&lt;&lt;525.0,1251.0&gt;-&lt;532.0,1347.0&gt;-&lt;587.5,1399.5&gt;&gt; = 4.007201127423053

* uni0772.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni0772.init: L&lt;&lt;444.0,1774.0&gt;--&lt;443.0,1423.0&gt;&gt;/B&lt;&lt;443.0,1423.0&gt;-&lt;450.0,1519.0&gt;-&lt;505.5,1571.5&gt;&gt; = 4.007201127423053

* uni0772.medi: L&lt;&lt;444.0,1774.0&gt;--&lt;443.0,1423.0&gt;&gt;/B&lt;&lt;443.0,1423.0&gt;-&lt;450.0,1519.0&gt;-&lt;505.5,1571.5&gt;&gt; = 4.007201127423053

* uni0773.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0774 (U+0774): B&lt;&lt;218.0,1425.5&gt;-&lt;224.0,1423.0&gt;-&lt;223.0,1424.0&gt;&gt;/B&lt;&lt;223.0,1424.0&gt;-&lt;237.0,1413.0&gt;-&lt;240.0,1430.5&gt;&gt; = 6.842773412630916

* uni0774.fina.alt: B&lt;&lt;484.0,1425.5&gt;-&lt;490.0,1423.0&gt;-&lt;489.0,1424.0&gt;&gt;/B&lt;&lt;489.0,1424.0&gt;-&lt;503.0,1413.0&gt;-&lt;506.0,1430.5&gt;&gt; = 6.842773412630916

* uni0774.fina.alt: B&lt;&lt;957.0,435.5&gt;-&lt;948.0,401.0&gt;-&lt;919.0,401.0&gt;&gt;/L&lt;&lt;919.0,401.0&gt;--&lt;1097.0,395.0&gt;&gt; = 1.9305874411669464

* uni0774.fina: B&lt;&lt;161.0,1425.5&gt;-&lt;167.0,1423.0&gt;-&lt;166.0,1424.0&gt;&gt;/B&lt;&lt;166.0,1424.0&gt;-&lt;180.0,1413.0&gt;-&lt;183.0,1430.5&gt;&gt; = 6.842773412630916

* uni0775.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0776 (U+0776): B&lt;&lt;357.0,1306.5&gt;-&lt;363.0,1304.0&gt;-&lt;362.0,1305.0&gt;&gt;/B&lt;&lt;362.0,1305.0&gt;-&lt;376.0,1294.0&gt;-&lt;379.0,1311.5&gt;&gt; = 6.842773412630916

* uni0776.fina: B&lt;&lt;357.0,989.5&gt;-&lt;363.0,987.0&gt;-&lt;362.0,988.0&gt;&gt;/B&lt;&lt;362.0,988.0&gt;-&lt;376.0,977.0&gt;-&lt;379.0,994.5&gt;&gt; = 6.842773412630916

* uni0776.init: B&lt;&lt;357.0,1306.5&gt;-&lt;363.0,1304.0&gt;-&lt;362.0,1305.0&gt;&gt;/B&lt;&lt;362.0,1305.0&gt;-&lt;376.0,1294.0&gt;-&lt;379.0,1311.5&gt;&gt; = 6.842773412630916

* uni0776.medi: B&lt;&lt;300.0,1306.5&gt;-&lt;306.0,1304.0&gt;-&lt;305.0,1305.0&gt;&gt;/B&lt;&lt;305.0,1305.0&gt;-&lt;319.0,1294.0&gt;-&lt;322.0,1311.5&gt;&gt; = 6.842773412630916

* uni0776.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0777 (U+0777): B&lt;&lt;542.0,-278.5&gt;-&lt;583.0,-314.0&gt;-&lt;585.0,-341.0&gt;&gt;/B&lt;&lt;585.0,-341.0&gt;-&lt;588.0,-314.0&gt;-&lt;605.0,-294.0&gt;&gt; = 10.576586544968738

* uni0777.fina: B&lt;&lt;560.0,-513.0&gt;-&lt;584.0,-538.0&gt;-&lt;585.0,-560.0&gt;&gt;/B&lt;&lt;585.0,-560.0&gt;-&lt;588.0,-534.0&gt;-&lt;608.0,-510.0&gt;&gt; = 9.18450685767776

* uni0777.init: B&lt;&lt;542.0,78.5&gt;-&lt;583.0,43.0&gt;-&lt;585.0,16.0&gt;&gt;/B&lt;&lt;585.0,16.0&gt;-&lt;588.0,43.0&gt;-&lt;605.0,63.0&gt;&gt; = 10.576586544968738

* uni0777.medi: B&lt;&lt;573.0,78.5&gt;-&lt;614.0,43.0&gt;-&lt;616.0,16.0&gt;&gt;/B&lt;&lt;616.0,16.0&gt;-&lt;619.0,43.0&gt;-&lt;636.0,63.0&gt;&gt; = 10.576586544968738

* uni0777.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni0779 (U+0779): B&lt;&lt;265.0,991.5&gt;-&lt;271.0,989.0&gt;-&lt;270.0,990.0&gt;&gt;/B&lt;&lt;270.0,990.0&gt;-&lt;284.0,979.0&gt;-&lt;287.0,996.5&gt;&gt; = 6.842773412630916

* uni0779.fina: B&lt;&lt;281.0,999.5&gt;-&lt;287.0,997.0&gt;-&lt;286.0,998.0&gt;&gt;/B&lt;&lt;286.0,998.0&gt;-&lt;300.0,987.0&gt;-&lt;303.0,1004.5&gt;&gt; = 6.842773412630916

* uni077B (U+077B): B&lt;&lt;214.0,1364.5&gt;-&lt;220.0,1362.0&gt;-&lt;219.0,1363.0&gt;&gt;/B&lt;&lt;219.0,1363.0&gt;-&lt;233.0,1352.0&gt;-&lt;236.0,1369.5&gt;&gt; = 6.842773412630916

* uni077B.fina: B&lt;&lt;214.0,1106.5&gt;-&lt;220.0,1104.0&gt;-&lt;219.0,1105.0&gt;&gt;/B&lt;&lt;219.0,1105.0&gt;-&lt;233.0,1094.0&gt;-&lt;236.0,1111.5&gt;&gt; = 6.842773412630916

* uni077C (U+077C): B&lt;&lt;575.0,258.5&gt;-&lt;616.0,223.0&gt;-&lt;618.0,196.0&gt;&gt;/B&lt;&lt;618.0,196.0&gt;-&lt;621.0,223.0&gt;-&lt;638.0,243.0&gt;&gt; = 10.576586544968738

* uni077C.fina: B&lt;&lt;300.0,156.0&gt;-&lt;301.0,192.0&gt;-&lt;318.0,224.0&gt;&gt;/B&lt;&lt;318.0,224.0&gt;-&lt;279.0,171.0&gt;-&lt;255.0,114.0&gt;&gt; = 8.367983820405101

* uni077C.fina: B&lt;&lt;484.0,393.0&gt;-&lt;411.0,334.0&gt;-&lt;352.0,265.0&gt;&gt;/B&lt;&lt;352.0,265.0&gt;-&lt;386.0,294.0&gt;-&lt;430.0,296.0&gt;&gt; = 9.004931569295922

* uni077C.fina: B&lt;&lt;546.0,258.5&gt;-&lt;587.0,223.0&gt;-&lt;589.0,196.0&gt;&gt;/B&lt;&lt;589.0,196.0&gt;-&lt;592.0,223.0&gt;-&lt;609.0,243.0&gt;&gt; = 10.576586544968738

* uni077C.init: B&lt;&lt;575.0,-3.5&gt;-&lt;616.0,-39.0&gt;-&lt;618.0,-66.0&gt;&gt;/B&lt;&lt;618.0,-66.0&gt;-&lt;621.0,-39.0&gt;-&lt;638.0,-19.0&gt;&gt; = 10.576586544968738

* uni077C.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni077C.medi: B&lt;&lt;575.0,-3.5&gt;-&lt;616.0,-39.0&gt;-&lt;618.0,-66.0&gt;&gt;/B&lt;&lt;618.0,-66.0&gt;-&lt;621.0,-39.0&gt;-&lt;638.0,-19.0&gt;&gt; = 10.576586544968738

* uni077D (U+077D): L&lt;&lt;613.0,1521.0&gt;--&lt;613.0,1522.0&gt;&gt;/B&lt;&lt;613.0,1522.0&gt;-&lt;612.0,1516.0&gt;-&lt;609.0,1507.0&gt;&gt; = 9.462322208025613

* uni077D.fina: L&lt;&lt;520.0,1521.0&gt;--&lt;520.0,1522.0&gt;&gt;/B&lt;&lt;520.0,1522.0&gt;-&lt;519.0,1516.0&gt;-&lt;516.0,1507.0&gt;&gt; = 9.462322208025613

* uni077D.init: L&lt;&lt;771.0,1521.0&gt;--&lt;771.0,1522.0&gt;&gt;/B&lt;&lt;771.0,1522.0&gt;-&lt;770.0,1516.0&gt;-&lt;767.0,1507.0&gt;&gt; = 9.462322208025613

* uni077D.medi: L&lt;&lt;659.0,1517.0&gt;--&lt;659.0,1521.0&gt;&gt;/B&lt;&lt;659.0,1521.0&gt;-&lt;658.0,1515.0&gt;-&lt;655.0,1507.0&gt;&gt; = 9.462322208025613

* uni077F (U+077F): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni077F.fina: L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni08A0.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08A1 (U+08A1): B&lt;&lt;413.0,1256.5&gt;-&lt;464.0,1284.0&gt;-&lt;515.0,1297.0&gt;&gt;/B&lt;&lt;515.0,1297.0&gt;-&lt;465.0,1293.0&gt;-&lt;424.0,1345.5&gt;&gt; = 9.726356189284708

* uni08A1.fina: B&lt;&lt;413.0,1256.5&gt;-&lt;464.0,1284.0&gt;-&lt;515.0,1297.0&gt;&gt;/B&lt;&lt;515.0,1297.0&gt;-&lt;465.0,1293.0&gt;-&lt;424.0,1345.5&gt;&gt; = 9.726356189284708

* uni08A1.init: B&lt;&lt;241.0,1256.5&gt;-&lt;292.0,1284.0&gt;-&lt;343.0,1297.0&gt;&gt;/B&lt;&lt;343.0,1297.0&gt;-&lt;293.0,1293.0&gt;-&lt;252.0,1345.5&gt;&gt; = 9.726356189284708

* uni08A1.medi: B&lt;&lt;233.0,1256.5&gt;-&lt;284.0,1284.0&gt;-&lt;335.0,1297.0&gt;&gt;/B&lt;&lt;335.0,1297.0&gt;-&lt;285.0,1293.0&gt;-&lt;244.0,1345.5&gt;&gt; = 9.726356189284708

* uni08A1.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08A2.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni08A3 (U+08A3): L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uni08A3.fina: L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uni08A3.init: L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uni08A3.medi: L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uni08A4 (U+08A4): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni08A4.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni08A5.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni08A6.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;544.5,265.5&gt;&gt; = 5.710593137499633

* uni08A8 (U+08A8): B&lt;&lt;624.0,1391.5&gt;-&lt;675.0,1419.0&gt;-&lt;726.0,1432.0&gt;&gt;/B&lt;&lt;726.0,1432.0&gt;-&lt;676.0,1428.0&gt;-&lt;635.0,1480.5&gt;&gt; = 9.726356189284708

* uni08A8.fina: B&lt;&lt;624.0,834.5&gt;-&lt;675.0,862.0&gt;-&lt;726.0,875.0&gt;&gt;/B&lt;&lt;726.0,875.0&gt;-&lt;676.0,871.0&gt;-&lt;635.0,923.5&gt;&gt; = 9.726356189284708

* uni08A8.init: B&lt;&lt;624.0,1256.5&gt;-&lt;675.0,1284.0&gt;-&lt;726.0,1297.0&gt;&gt;/B&lt;&lt;726.0,1297.0&gt;-&lt;676.0,1293.0&gt;-&lt;635.0,1345.5&gt;&gt; = 9.726356189284708

* uni08A8.medi: B&lt;&lt;624.0,1254.5&gt;-&lt;675.0,1282.0&gt;-&lt;726.0,1295.0&gt;&gt;/B&lt;&lt;726.0,1295.0&gt;-&lt;676.0,1291.0&gt;-&lt;635.0,1343.5&gt;&gt; = 9.726356189284708

* uni08A8.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08A9.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08AA (U+08AA): B&lt;&lt;922.0,0.0&gt;-&lt;842.0,-76.0&gt;-&lt;742.0,-116.0&gt;&gt;/B&lt;&lt;742.0,-116.0&gt;-&lt;759.0,-113.0&gt;-&lt;763.0,-132.5&gt;&gt; = 11.79342968491046

* uni08AA.fina: B&lt;&lt;915.0,4.0&gt;-&lt;833.0,-75.0&gt;-&lt;730.0,-116.0&gt;&gt;/B&lt;&lt;730.0,-116.0&gt;-&lt;747.0,-113.0&gt;-&lt;751.0,-132.5&gt;&gt; = 11.697456944664232

* uni08AC (U+08AC): B&lt;&lt;331.0,402.5&gt;-&lt;367.0,404.0&gt;-&lt;386.0,385.0&gt;&gt;/B&lt;&lt;386.0,385.0&gt;-&lt;331.0,434.0&gt;-&lt;294.5,507.0&gt;&gt; = 3.301865674434948

* uni08AC.comp: B&lt;&lt;331.0,402.5&gt;-&lt;367.0,404.0&gt;-&lt;386.0,385.0&gt;&gt;/B&lt;&lt;386.0,385.0&gt;-&lt;331.0,434.0&gt;-&lt;294.5,507.0&gt;&gt; = 3.301865674434948

* uni08AC.fina: B&lt;&lt;331.0,402.5&gt;-&lt;367.0,404.0&gt;-&lt;386.0,385.0&gt;&gt;/B&lt;&lt;386.0,385.0&gt;-&lt;331.0,434.0&gt;-&lt;294.5,507.0&gt;&gt; = 3.301865674434948

* uni08AF.fina: B&lt;&lt;910.0,508.0&gt;-&lt;855.0,416.0&gt;-&lt;753.0,395.0&gt;&gt;/L&lt;&lt;753.0,395.0&gt;--&lt;1229.0,402.0&gt;&gt; = 10.791109738200037

* uni08AF.init: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni08AF.medi: L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uni08B3.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni08B3.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni08B4 (U+08B4): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni08B4.fina: L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uni08B6.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08B7.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08B8.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08BA.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08BB (U+08BB): L&lt;&lt;876.0,402.0&gt;--&lt;852.0,547.0&gt;&gt;/B&lt;&lt;852.0,547.0&gt;-&lt;854.0,526.0&gt;-&lt;827.0,520.5&gt;&gt; = 3.9579009649205457

* uni08BB.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni08BC.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni08BD.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08BE.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08BF.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08C0 (U+08C0): L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;/B&lt;&lt;537.0,1146.0&gt;-&lt;544.0,1242.0&gt;-&lt;599.5,1294.5&gt;&gt; = 4.007201127423053

* uni08C0.fina: L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;/B&lt;&lt;537.0,1146.0&gt;-&lt;544.0,1242.0&gt;-&lt;599.5,1294.5&gt;&gt; = 4.007201127423053

* uni08C0.init: L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;/B&lt;&lt;537.0,1146.0&gt;-&lt;544.0,1242.0&gt;-&lt;599.5,1294.5&gt;&gt; = 4.007201127423053

* uni08C0.medi: L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;/B&lt;&lt;537.0,1146.0&gt;-&lt;544.0,1242.0&gt;-&lt;599.5,1294.5&gt;&gt; = 4.007201127423053

* uni08C0.medi: L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uni08C1 (U+08C1): B&lt;&lt;469.0,381.0&gt;-&lt;388.0,314.0&gt;-&lt;327.0,235.0&gt;&gt;/B&lt;&lt;327.0,235.0&gt;-&lt;350.0,257.0&gt;-&lt;374.0,272.5&gt;&gt; = 8.599436680226221

* uni08C1.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni08C2.medi: L&lt;&lt;252.0,1206.0&gt;--&lt;492.0,1446.0&gt;&gt;/L&lt;&lt;492.0,1446.0&gt;--&lt;372.0,1369.0&gt;&gt; = 12.313063458989452

* uni08C3.fina: B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uni08C3.fina: B&lt;&lt;575.0,1520.0&gt;-&lt;572.0,1520.0&gt;-&lt;570.0,1521.0&gt;&gt;/B&lt;&lt;570.0,1521.0&gt;-&lt;605.0,1491.0&gt;-&lt;634.5,1450.5&gt;&gt; = 14.036243467926457

* uni08C3.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uni08C4.init: L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uni08C5.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni08C6.fina: L&lt;&lt;525.0,105.0&gt;--&lt;526.0,104.0&gt;&gt;/B&lt;&lt;526.0,104.0&gt;-&lt;491.0,134.0&gt;-&lt;462.0,173.0&gt;&gt; = 4.398705354995591

* uni08C6.init: L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uni08C7 (U+08C7): L&lt;&lt;440.0,1620.0&gt;--&lt;439.0,1269.0&gt;&gt;/B&lt;&lt;439.0,1269.0&gt;-&lt;446.0,1365.0&gt;-&lt;501.5,1417.5&gt;&gt; = 4.007201127423053

* uni08C7.fina: L&lt;&lt;440.0,1620.0&gt;--&lt;439.0,1269.0&gt;&gt;/B&lt;&lt;439.0,1269.0&gt;-&lt;446.0,1365.0&gt;-&lt;501.5,1417.5&gt;&gt; = 4.007201127423053

* uni08C7.init: L&lt;&lt;456.0,1620.0&gt;--&lt;455.0,1269.0&gt;&gt;/B&lt;&lt;455.0,1269.0&gt;-&lt;462.0,1365.0&gt;-&lt;517.5,1417.5&gt;&gt; = 4.007201127423053

* uni08C7.medi: L&lt;&lt;538.0,1825.0&gt;--&lt;537.0,1474.0&gt;&gt;/B&lt;&lt;537.0,1474.0&gt;-&lt;544.0,1570.0&gt;-&lt;599.5,1622.5&gt;&gt; = 4.007201127423053

* uni08CC (U+08CC): B&lt;&lt;460.5,1481.5&gt;-&lt;470.0,1457.0&gt;-&lt;467.0,1446.0&gt;&gt;/B&lt;&lt;467.0,1446.0&gt;-&lt;502.0,1556.0&gt;-&lt;591.5,1634.0&gt;&gt; = 2.3950055168722097

* uni08D6 (U+08D6): B&lt;&lt;259.0,963.0&gt;-&lt;261.0,1093.0&gt;-&lt;374.0,1196.0&gt;&gt;/B&lt;&lt;374.0,1196.0&gt;-&lt;341.0,1177.0&gt;-&lt;301.0,1220.0&gt;&gt; = 12.417798476070361

* uni08DA (U+08DA): B&lt;&lt;195.5,1362.5&gt;-&lt;203.0,1381.0&gt;-&lt;221.0,1393.0&gt;&gt;/B&lt;&lt;221.0,1393.0&gt;-&lt;216.0,1391.0&gt;-&lt;212.0,1390.0&gt;&gt; = 11.888658039627936

* uni08DA (U+08DA): B&lt;&lt;270.0,1432.0&gt;-&lt;254.0,1412.0&gt;-&lt;236.0,1401.0&gt;&gt;/B&lt;&lt;236.0,1401.0&gt;-&lt;242.0,1403.0&gt;-&lt;248.0,1404.0&gt;&gt; = 12.994616791916455

* uni08DD (U+08DD): B&lt;&lt;253.0,1435.0&gt;-&lt;238.0,1416.0&gt;-&lt;220.0,1404.0&gt;&gt;/B&lt;&lt;220.0,1404.0&gt;-&lt;225.0,1406.0&gt;-&lt;230.0,1407.0&gt;&gt; = 11.888658039627936

* uni08DD (U+08DD): B&lt;&lt;472.0,1290.0&gt;-&lt;474.0,1316.0&gt;-&lt;492.0,1344.0&gt;&gt;/B&lt;&lt;492.0,1344.0&gt;-&lt;468.0,1319.0&gt;-&lt;445.0,1314.0&gt;&gt; = 11.095634399984965

* uni08DE (U+08DE): L&lt;&lt;813.0,1127.0&gt;--&lt;787.0,1150.0&gt;&gt;/B&lt;&lt;787.0,1150.0&gt;-&lt;798.0,1138.0&gt;-&lt;801.0,1131.0&gt;&gt; = 5.99308456678352

* uni08DF (U+08DF): B&lt;&lt;337.0,1433.5&gt;-&lt;321.0,1414.0&gt;-&lt;302.0,1402.0&gt;&gt;/B&lt;&lt;302.0,1402.0&gt;-&lt;308.0,1405.0&gt;-&lt;315.0,1406.0&gt;&gt; = 5.710593137499568

* uni08DF (U+08DF): B&lt;&lt;371.0,1122.0&gt;-&lt;354.0,1146.0&gt;-&lt;347.0,1178.0&gt;&gt;/L&lt;&lt;347.0,1178.0&gt;--&lt;347.0,1141.0&gt;&gt; = 12.33908727832618

* uni08DF (U+08DF): L&lt;&lt;287.0,1394.0&gt;--&lt;289.0,1396.0&gt;&gt;/B&lt;&lt;289.0,1396.0&gt;-&lt;284.0,1393.0&gt;-&lt;279.0,1392.0&gt;&gt; = 14.036243467926484

* uni08DF (U+08DF): L&lt;&lt;347.0,1260.0&gt;--&lt;347.0,1227.0&gt;&gt;/B&lt;&lt;347.0,1227.0&gt;-&lt;356.0,1269.0&gt;-&lt;389.5,1299.0&gt;&gt; = 12.094757077012089

* uni08DF (U+08DF): L&lt;&lt;755.0,1124.0&gt;--&lt;745.0,1137.0&gt;&gt;/B&lt;&lt;745.0,1137.0&gt;-&lt;749.0,1130.0&gt;-&lt;749.0,1124.0&gt;&gt; = 7.823710731885198

* uni08E1 (U+08E1): B&lt;&lt;540.0,1151.5&gt;-&lt;474.0,1173.0&gt;-&lt;443.0,1212.0&gt;&gt;/B&lt;&lt;443.0,1212.0&gt;-&lt;451.0,1197.0&gt;-&lt;428.0,1179.5&gt;&gt; = 10.40771131249005

* uni08EC (U+08EC): B&lt;&lt;607.5,1753.0&gt;-&lt;689.0,1710.0&gt;-&lt;733.0,1649.0&gt;&gt;/B&lt;&lt;733.0,1649.0&gt;-&lt;719.0,1672.0&gt;-&lt;716.5,1698.5&gt;&gt; = 4.474651240566884

* uni08EF (U+08EF): B&lt;&lt;607.5,-492.0&gt;-&lt;689.0,-535.0&gt;-&lt;733.0,-596.0&gt;&gt;/B&lt;&lt;733.0,-596.0&gt;-&lt;719.0,-573.0&gt;-&lt;716.5,-546.5&gt;&gt; = 4.474651240566884

* uni0E3F (U+0E3F): B&lt;&lt;864.5,707.5&gt;-&lt;814.0,670.0&gt;-&lt;754.0,668.0&gt;&gt;/B&lt;&lt;754.0,668.0&gt;-&lt;831.0,656.0&gt;-&lt;891.0,607.5&gt;&gt; = 10.767111196624704

* uni1E0D (U+1E0D): B&lt;&lt;755.0,928.5&gt;-&lt;835.0,878.0&gt;-&lt;853.0,788.0&gt;&gt;/L&lt;&lt;853.0,788.0&gt;--&lt;852.0,1257.0&gt;&gt; = 11.187766817972967

* uni1E0D (U+1E0D): L&lt;&lt;862.0,55.0&gt;--&lt;900.0,113.0&gt;&gt;/B&lt;&lt;900.0,113.0&gt;-&lt;851.0,39.0&gt;-&lt;762.5,-8.0&gt;&gt; = 0.27930772986015584

* uni1E0F (U+1E0F): B&lt;&lt;755.0,928.5&gt;-&lt;835.0,878.0&gt;-&lt;853.0,788.0&gt;&gt;/L&lt;&lt;853.0,788.0&gt;--&lt;852.0,1257.0&gt;&gt; = 11.187766817972967

* uni1E0F (U+1E0F): L&lt;&lt;862.0,55.0&gt;--&lt;900.0,113.0&gt;&gt;/B&lt;&lt;900.0,113.0&gt;-&lt;851.0,39.0&gt;-&lt;762.5,-8.0&gt;&gt; = 0.27930772986015584

* uni1E25 (U+1E25): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;/B&lt;&lt;385.0,728.0&gt;-&lt;403.0,804.0&gt;-&lt;456.5,860.5&gt;&gt; = 13.216221788799638

* uni1E27 (U+1E27): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;/B&lt;&lt;385.0,728.0&gt;-&lt;403.0,804.0&gt;-&lt;456.5,860.5&gt;&gt; = 13.216221788799638

* uni1E2B (U+1E2B): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;/B&lt;&lt;385.0,728.0&gt;-&lt;403.0,804.0&gt;-&lt;456.5,860.5&gt;&gt; = 13.216221788799638

* uni1E43 (U+1E43): B&lt;&lt;617.0,928.5&gt;-&lt;676.0,878.0&gt;-&lt;672.0,799.0&gt;&gt;/B&lt;&lt;672.0,799.0&gt;-&lt;697.0,880.0&gt;-&lt;761.0,929.5&gt;&gt; = 14.253844940930117

* uni1E45 (U+1E45): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* uni1E47 (U+1E47): L&lt;&lt;376.0,869.0&gt;--&lt;352.0,739.0&gt;&gt;/B&lt;&lt;352.0,739.0&gt;-&lt;379.0,802.0&gt;-&lt;437.5,857.0&gt;&gt; = 12.738681420719038

* uni1EA2 (U+1EA2): B&lt;&lt;420.0,1687.0&gt;-&lt;421.0,1679.0&gt;-&lt;411.0,1667.0&gt;&gt;/L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt; = 5.1944289077348

* uni1EA2 (U+1EA2): L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt;/B&lt;&lt;412.0,1668.0&gt;-&lt;407.0,1661.0&gt;-&lt;395.0,1662.0&gt;&gt; = 9.462322208025613

* uni1EA3 (U+1EA3): B&lt;&lt;420.0,1208.0&gt;-&lt;421.0,1200.0&gt;-&lt;411.0,1188.0&gt;&gt;/L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt; = 5.1944289077348

* uni1EA3 (U+1EA3): L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt;/B&lt;&lt;412.0,1189.0&gt;-&lt;407.0,1182.0&gt;-&lt;395.0,1183.0&gt;&gt; = 9.462322208025613

* uni1EA8 (U+1EA8): B&lt;&lt;623.0,1874.0&gt;-&lt;624.0,1866.0&gt;-&lt;614.0,1854.0&gt;&gt;/L&lt;&lt;614.0,1854.0&gt;--&lt;615.0,1855.0&gt;&gt; = 5.1944289077348

* uni1EA8 (U+1EA8): L&lt;&lt;614.0,1854.0&gt;--&lt;615.0,1855.0&gt;&gt;/B&lt;&lt;615.0,1855.0&gt;-&lt;610.0,1848.0&gt;-&lt;598.0,1849.0&gt;&gt; = 9.462322208025613

* uni1EA9 (U+1EA9): B&lt;&lt;623.0,1513.0&gt;-&lt;624.0,1505.0&gt;-&lt;614.0,1493.0&gt;&gt;/L&lt;&lt;614.0,1493.0&gt;--&lt;615.0,1494.0&gt;&gt; = 5.1944289077348

* uni1EA9 (U+1EA9): L&lt;&lt;614.0,1493.0&gt;--&lt;615.0,1494.0&gt;&gt;/B&lt;&lt;615.0,1494.0&gt;-&lt;610.0,1487.0&gt;-&lt;598.0,1488.0&gt;&gt; = 9.462322208025613

* uni1EB2 (U+1EB2): B&lt;&lt;422.0,1917.0&gt;-&lt;423.0,1909.0&gt;-&lt;413.0,1897.0&gt;&gt;/L&lt;&lt;413.0,1897.0&gt;--&lt;414.0,1898.0&gt;&gt; = 5.1944289077348

* uni1EB2 (U+1EB2): L&lt;&lt;413.0,1897.0&gt;--&lt;414.0,1898.0&gt;&gt;/B&lt;&lt;414.0,1898.0&gt;-&lt;409.0,1891.0&gt;-&lt;397.0,1892.0&gt;&gt; = 9.462322208025613

* uni1EB3 (U+1EB3): B&lt;&lt;422.0,1560.0&gt;-&lt;423.0,1552.0&gt;-&lt;413.0,1540.0&gt;&gt;/L&lt;&lt;413.0,1540.0&gt;--&lt;414.0,1541.0&gt;&gt; = 5.1944289077348

* uni1EB3 (U+1EB3): L&lt;&lt;413.0,1540.0&gt;--&lt;414.0,1541.0&gt;&gt;/B&lt;&lt;414.0,1541.0&gt;-&lt;409.0,1534.0&gt;-&lt;397.0,1535.0&gt;&gt; = 9.462322208025613

* uni1EBA (U+1EBA): B&lt;&lt;420.0,1687.0&gt;-&lt;421.0,1679.0&gt;-&lt;411.0,1667.0&gt;&gt;/L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt; = 5.1944289077348

* uni1EBA (U+1EBA): L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt;/B&lt;&lt;412.0,1668.0&gt;-&lt;407.0,1661.0&gt;-&lt;395.0,1662.0&gt;&gt; = 9.462322208025613

* uni1EBB (U+1EBB): B&lt;&lt;420.0,1208.0&gt;-&lt;421.0,1200.0&gt;-&lt;411.0,1188.0&gt;&gt;/L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt; = 5.1944289077348

* uni1EBB (U+1EBB): L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt;/B&lt;&lt;412.0,1189.0&gt;-&lt;407.0,1182.0&gt;-&lt;395.0,1183.0&gt;&gt; = 9.462322208025613

* uni1EC2 (U+1EC2): B&lt;&lt;623.0,1874.0&gt;-&lt;624.0,1866.0&gt;-&lt;614.0,1854.0&gt;&gt;/L&lt;&lt;614.0,1854.0&gt;--&lt;615.0,1855.0&gt;&gt; = 5.1944289077348

* uni1EC2 (U+1EC2): L&lt;&lt;614.0,1854.0&gt;--&lt;615.0,1855.0&gt;&gt;/B&lt;&lt;615.0,1855.0&gt;-&lt;610.0,1848.0&gt;-&lt;598.0,1849.0&gt;&gt; = 9.462322208025613

* uni1EC3 (U+1EC3): B&lt;&lt;623.0,1513.0&gt;-&lt;624.0,1505.0&gt;-&lt;614.0,1493.0&gt;&gt;/L&lt;&lt;614.0,1493.0&gt;--&lt;615.0,1494.0&gt;&gt; = 5.1944289077348

* uni1EC3 (U+1EC3): L&lt;&lt;614.0,1493.0&gt;--&lt;615.0,1494.0&gt;&gt;/B&lt;&lt;615.0,1494.0&gt;-&lt;610.0,1487.0&gt;-&lt;598.0,1488.0&gt;&gt; = 9.462322208025613

* uni1EC8 (U+1EC8): B&lt;&lt;420.0,1687.0&gt;-&lt;421.0,1679.0&gt;-&lt;411.0,1667.0&gt;&gt;/L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt; = 5.1944289077348

* uni1EC8 (U+1EC8): L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt;/B&lt;&lt;412.0,1668.0&gt;-&lt;407.0,1661.0&gt;-&lt;395.0,1662.0&gt;&gt; = 9.462322208025613

* uni1EC9 (U+1EC9): B&lt;&lt;420.0,1208.0&gt;-&lt;421.0,1200.0&gt;-&lt;411.0,1188.0&gt;&gt;/L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt; = 5.1944289077348

* uni1EC9 (U+1EC9): L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt;/B&lt;&lt;412.0,1189.0&gt;-&lt;407.0,1182.0&gt;-&lt;395.0,1183.0&gt;&gt; = 9.462322208025613

* uni1ECE (U+1ECE): B&lt;&lt;420.0,1687.0&gt;-&lt;421.0,1679.0&gt;-&lt;411.0,1667.0&gt;&gt;/L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt; = 5.1944289077348

* uni1ECE (U+1ECE): L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt;/B&lt;&lt;412.0,1668.0&gt;-&lt;407.0,1661.0&gt;-&lt;395.0,1662.0&gt;&gt; = 9.462322208025613

* uni1ECF (U+1ECF): B&lt;&lt;420.0,1208.0&gt;-&lt;421.0,1200.0&gt;-&lt;411.0,1188.0&gt;&gt;/L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt; = 5.1944289077348

* uni1ECF (U+1ECF): L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt;/B&lt;&lt;412.0,1189.0&gt;-&lt;407.0,1182.0&gt;-&lt;395.0,1183.0&gt;&gt; = 9.462322208025613

* uni1ED4 (U+1ED4): B&lt;&lt;623.0,1874.0&gt;-&lt;624.0,1866.0&gt;-&lt;614.0,1854.0&gt;&gt;/L&lt;&lt;614.0,1854.0&gt;--&lt;615.0,1855.0&gt;&gt; = 5.1944289077348

* uni1ED4 (U+1ED4): L&lt;&lt;614.0,1854.0&gt;--&lt;615.0,1855.0&gt;&gt;/B&lt;&lt;615.0,1855.0&gt;-&lt;610.0,1848.0&gt;-&lt;598.0,1849.0&gt;&gt; = 9.462322208025613

* uni1ED5 (U+1ED5): B&lt;&lt;623.0,1513.0&gt;-&lt;624.0,1505.0&gt;-&lt;614.0,1493.0&gt;&gt;/L&lt;&lt;614.0,1493.0&gt;--&lt;615.0,1494.0&gt;&gt; = 5.1944289077348

* uni1ED5 (U+1ED5): L&lt;&lt;614.0,1493.0&gt;--&lt;615.0,1494.0&gt;&gt;/B&lt;&lt;615.0,1494.0&gt;-&lt;610.0,1487.0&gt;-&lt;598.0,1488.0&gt;&gt; = 9.462322208025613

* uni1EDB (U+1EDB): B&lt;&lt;535.0,933.0&gt;-&lt;644.0,933.0&gt;-&lt;735.0,882.0&gt;&gt;/B&lt;&lt;735.0,882.0&gt;-&lt;731.0,885.0&gt;-&lt;748.0,888.0&gt;&gt; = 7.6019024309512755

* uni1EDD (U+1EDD): B&lt;&lt;535.0,933.0&gt;-&lt;644.0,933.0&gt;-&lt;735.0,882.0&gt;&gt;/B&lt;&lt;735.0,882.0&gt;-&lt;731.0,885.0&gt;-&lt;748.0,888.0&gt;&gt; = 7.6019024309512755

* uni1EDF (U+1EDF): B&lt;&lt;604.0,927.0&gt;-&lt;676.0,915.0&gt;-&lt;735.0,882.0&gt;&gt;/B&lt;&lt;735.0,882.0&gt;-&lt;731.0,885.0&gt;-&lt;748.0,888.0&gt;&gt; = 7.650650955359358

* uni1EE1 (U+1EE1): B&lt;&lt;535.0,933.0&gt;-&lt;644.0,933.0&gt;-&lt;735.0,882.0&gt;&gt;/B&lt;&lt;735.0,882.0&gt;-&lt;731.0,885.0&gt;-&lt;748.0,888.0&gt;&gt; = 7.6019024309512755

* uni1EE3 (U+1EE3): B&lt;&lt;535.0,933.0&gt;-&lt;644.0,933.0&gt;-&lt;735.0,882.0&gt;&gt;/B&lt;&lt;735.0,882.0&gt;-&lt;731.0,885.0&gt;-&lt;748.0,888.0&gt;&gt; = 7.6019024309512755

* uni1EE5 (U+1EE5): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EE6 (U+1EE6): B&lt;&lt;420.0,1687.0&gt;-&lt;421.0,1679.0&gt;-&lt;411.0,1667.0&gt;&gt;/L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt; = 5.1944289077348

* uni1EE6 (U+1EE6): L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt;/B&lt;&lt;412.0,1668.0&gt;-&lt;407.0,1661.0&gt;-&lt;395.0,1662.0&gt;&gt; = 9.462322208025613

* uni1EE7 (U+1EE7): B&lt;&lt;420.0,1208.0&gt;-&lt;421.0,1200.0&gt;-&lt;411.0,1188.0&gt;&gt;/L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt; = 5.1944289077348

* uni1EE7 (U+1EE7): L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt;/B&lt;&lt;412.0,1189.0&gt;-&lt;407.0,1182.0&gt;-&lt;395.0,1183.0&gt;&gt; = 9.462322208025613

* uni1EE7 (U+1EE7): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EE9 (U+1EE9): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EEB (U+1EEB): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EED (U+1EED): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EEF (U+1EEF): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EF1 (U+1EF1): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* uni1EF6 (U+1EF6): B&lt;&lt;420.0,1687.0&gt;-&lt;421.0,1679.0&gt;-&lt;411.0,1667.0&gt;&gt;/L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt; = 5.1944289077348

* uni1EF6 (U+1EF6): L&lt;&lt;411.0,1667.0&gt;--&lt;412.0,1668.0&gt;&gt;/B&lt;&lt;412.0,1668.0&gt;-&lt;407.0,1661.0&gt;-&lt;395.0,1662.0&gt;&gt; = 9.462322208025613

* uni1EF7 (U+1EF7): B&lt;&lt;420.0,1208.0&gt;-&lt;421.0,1200.0&gt;-&lt;411.0,1188.0&gt;&gt;/L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt; = 5.1944289077348

* uni1EF7 (U+1EF7): L&lt;&lt;411.0,1188.0&gt;--&lt;412.0,1189.0&gt;&gt;/B&lt;&lt;412.0,1189.0&gt;-&lt;407.0,1182.0&gt;-&lt;395.0,1183.0&gt;&gt; = 9.462322208025613

* uni1EF9 (U+1EF9): B&lt;&lt;1100.0,1088.0&gt;-&lt;1049.0,1006.0&gt;-&lt;972.0,956.0&gt;&gt;/B&lt;&lt;972.0,956.0&gt;-&lt;1014.0,976.0&gt;-&lt;1064.0,955.0&gt;&gt; = 7.534360039344612

* uni1EF9 (U+1EF9): B&lt;&lt;924.0,909.0&gt;-&lt;935.0,931.0&gt;-&lt;954.0,945.0&gt;&gt;/B&lt;&lt;954.0,945.0&gt;-&lt;884.0,906.0&gt;-&lt;810.0,905.0&gt;&gt; = 7.2602983210585

* uni1F06 (U+1F06): B&lt;&lt;467.0,1075.0&gt;-&lt;468.0,1076.0&gt;-&lt;462.0,1079.0&gt;&gt;/L&lt;&lt;462.0,1079.0&gt;--&lt;467.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F08 (U+1F08): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F09 (U+1F09): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F0A (U+1F0A): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F0B (U+1F0B): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F0C (U+1F0C): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F0D (U+1F0D): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F0E (U+1F0E): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F0E (U+1F0E): B&lt;&lt;21.0,930.0&gt;-&lt;22.0,931.0&gt;-&lt;16.0,934.0&gt;&gt;/L&lt;&lt;16.0,934.0&gt;--&lt;21.0,930.0&gt;&gt; = 12.094757077012058

* uni1F0F (U+1F0F): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F26 (U+1F26): B&lt;&lt;491.0,1075.0&gt;-&lt;492.0,1076.0&gt;-&lt;486.0,1079.0&gt;&gt;/L&lt;&lt;486.0,1079.0&gt;--&lt;491.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F2E (U+1F2E): B&lt;&lt;-389.0,905.0&gt;-&lt;-388.0,906.0&gt;-&lt;-394.0,909.0&gt;&gt;/L&lt;&lt;-394.0,909.0&gt;--&lt;-389.0,905.0&gt;&gt; = 12.094757077012058

* uni1F30 (U+1F30): B&lt;&lt;411.0,931.5&gt;-&lt;434.0,950.0&gt;-&lt;456.0,958.0&gt;&gt;/B&lt;&lt;456.0,958.0&gt;-&lt;448.0,957.0&gt;-&lt;442.0,957.0&gt;&gt; = 12.858090172998171

* uni1F36 (U+1F36): B&lt;&lt;503.0,1075.0&gt;-&lt;504.0,1076.0&gt;-&lt;498.0,1079.0&gt;&gt;/L&lt;&lt;498.0,1079.0&gt;--&lt;503.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F3E (U+1F3E): B&lt;&lt;-233.0,863.0&gt;-&lt;-232.0,864.0&gt;-&lt;-238.0,867.0&gt;&gt;/L&lt;&lt;-238.0,867.0&gt;--&lt;-233.0,863.0&gt;&gt; = 12.094757077012058

* uni1F56 (U+1F56): B&lt;&lt;505.0,1075.0&gt;-&lt;506.0,1076.0&gt;-&lt;500.0,1079.0&gt;&gt;/L&lt;&lt;500.0,1079.0&gt;--&lt;505.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F66 (U+1F66): B&lt;&lt;507.0,1075.0&gt;-&lt;508.0,1076.0&gt;-&lt;502.0,1079.0&gt;&gt;/L&lt;&lt;502.0,1079.0&gt;--&lt;507.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F6E (U+1F6E): B&lt;&lt;-4.0,983.0&gt;-&lt;-3.0,984.0&gt;-&lt;-9.0,987.0&gt;&gt;/L&lt;&lt;-9.0,987.0&gt;--&lt;-4.0,983.0&gt;&gt; = 12.094757077012058

* uni1F86 (U+1F86): B&lt;&lt;467.0,1075.0&gt;-&lt;468.0,1076.0&gt;-&lt;462.0,1079.0&gt;&gt;/L&lt;&lt;462.0,1079.0&gt;--&lt;467.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F88 (U+1F88): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F88 (U+1F88): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F88 (U+1F88): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F88 (U+1F88): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F89 (U+1F89): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F89 (U+1F89): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F89 (U+1F89): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F89 (U+1F89): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F8A (U+1F8A): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F8A (U+1F8A): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F8A (U+1F8A): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F8A (U+1F8A): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F8B (U+1F8B): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F8B (U+1F8B): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F8B (U+1F8B): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F8B (U+1F8B): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F8C (U+1F8C): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F8C (U+1F8C): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F8C (U+1F8C): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F8C (U+1F8C): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F8D (U+1F8D): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F8D (U+1F8D): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F8D (U+1F8D): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F8D (U+1F8D): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F8E (U+1F8E): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F8E (U+1F8E): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F8E (U+1F8E): B&lt;&lt;21.0,930.0&gt;-&lt;22.0,931.0&gt;-&lt;16.0,934.0&gt;&gt;/L&lt;&lt;16.0,934.0&gt;--&lt;21.0,930.0&gt;&gt; = 12.094757077012058

* uni1F8E (U+1F8E): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F8E (U+1F8E): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F8F (U+1F8F): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1F8F (U+1F8F): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1F8F (U+1F8F): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1F8F (U+1F8F): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1F96 (U+1F96): B&lt;&lt;491.0,1075.0&gt;-&lt;492.0,1076.0&gt;-&lt;486.0,1079.0&gt;&gt;/L&lt;&lt;486.0,1079.0&gt;--&lt;491.0,1075.0&gt;&gt; = 12.094757077012058

* uni1F98 (U+1F98): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F98 (U+1F98): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F98 (U+1F98): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F99 (U+1F99): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F99 (U+1F99): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F99 (U+1F99): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F9A (U+1F9A): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F9A (U+1F9A): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F9A (U+1F9A): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F9B (U+1F9B): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F9B (U+1F9B): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F9B (U+1F9B): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F9C (U+1F9C): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F9C (U+1F9C): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F9C (U+1F9C): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F9D (U+1F9D): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F9D (U+1F9D): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F9D (U+1F9D): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F9E (U+1F9E): B&lt;&lt;-389.0,905.0&gt;-&lt;-388.0,906.0&gt;-&lt;-394.0,909.0&gt;&gt;/L&lt;&lt;-394.0,909.0&gt;--&lt;-389.0,905.0&gt;&gt; = 12.094757077012058

* uni1F9E (U+1F9E): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F9E (U+1F9E): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F9E (U+1F9E): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1F9F (U+1F9F): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1F9F (U+1F9F): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1F9F (U+1F9F): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1FA6 (U+1FA6): B&lt;&lt;507.0,1075.0&gt;-&lt;508.0,1076.0&gt;-&lt;502.0,1079.0&gt;&gt;/L&lt;&lt;502.0,1079.0&gt;--&lt;507.0,1075.0&gt;&gt; = 12.094757077012058

* uni1FA8 (U+1FA8): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FA8 (U+1FA8): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FA8 (U+1FA8): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FA9 (U+1FA9): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FA9 (U+1FA9): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FA9 (U+1FA9): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FAA (U+1FAA): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FAA (U+1FAA): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FAA (U+1FAA): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FAB (U+1FAB): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FAB (U+1FAB): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FAB (U+1FAB): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FAC (U+1FAC): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FAC (U+1FAC): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FAC (U+1FAC): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FAD (U+1FAD): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FAD (U+1FAD): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FAD (U+1FAD): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FAE (U+1FAE): B&lt;&lt;-4.0,983.0&gt;-&lt;-3.0,984.0&gt;-&lt;-9.0,987.0&gt;&gt;/L&lt;&lt;-9.0,987.0&gt;--&lt;-4.0,983.0&gt;&gt; = 12.094757077012058

* uni1FAE (U+1FAE): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FAE (U+1FAE): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FAE (U+1FAE): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FAF (U+1FAF): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FAF (U+1FAF): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FAF (U+1FAF): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni1FB8 (U+1FB8): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1FB9 (U+1FB9): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1FBA (U+1FBA): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1FBB (U+1FBB): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1FBC (U+1FBC): B&lt;&lt;1198.5,129.5&gt;-&lt;1226.0,151.0&gt;-&lt;1232.0,127.0&gt;&gt;/L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt; = 14.036243467926457

* uni1FBC (U+1FBC): B&lt;&lt;122.5,156.0&gt;-&lt;151.0,153.0&gt;-&lt;147.0,133.0&gt;&gt;/L&lt;&lt;147.0,133.0&gt;--&lt;393.0,1206.0&gt;&gt; = 1.6027608107254878

* uni1FBC (U+1FBC): L&lt;&lt;1232.0,127.0&gt;--&lt;1232.0,416.0&gt;&gt;/B&lt;&lt;1232.0,416.0&gt;-&lt;1230.0,397.0&gt;-&lt;1203.0,418.0&gt;&gt; = 6.009005957494474

* uni1FBC (U+1FBC): L&lt;&lt;1409.0,416.0&gt;--&lt;1409.0,127.0&gt;&gt;/B&lt;&lt;1409.0,127.0&gt;-&lt;1415.0,151.0&gt;-&lt;1442.5,129.5&gt;&gt; = 14.036243467926457

* uni1FBE (U+1FBE): B&lt;&lt;415.5,-143.5&gt;-&lt;443.0,-122.0&gt;-&lt;449.0,-146.0&gt;&gt;/L&lt;&lt;449.0,-146.0&gt;--&lt;449.0,143.0&gt;&gt; = 14.036243467926457

* uni1FBE (U+1FBE): L&lt;&lt;449.0,-146.0&gt;--&lt;449.0,143.0&gt;&gt;/B&lt;&lt;449.0,143.0&gt;-&lt;447.0,124.0&gt;-&lt;420.0,145.0&gt;&gt; = 6.009005957494474

* uni1FBE (U+1FBE): L&lt;&lt;626.0,143.0&gt;--&lt;626.0,-146.0&gt;&gt;/B&lt;&lt;626.0,-146.0&gt;-&lt;632.0,-122.0&gt;-&lt;659.5,-143.5&gt;&gt; = 14.036243467926457

* uni1FCC (U+1FCC): B&lt;&lt;1206.5,129.5&gt;-&lt;1234.0,151.0&gt;-&lt;1240.0,127.0&gt;&gt;/L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt; = 14.036243467926457

* uni1FCC (U+1FCC): L&lt;&lt;1240.0,127.0&gt;--&lt;1240.0,416.0&gt;&gt;/B&lt;&lt;1240.0,416.0&gt;-&lt;1238.0,397.0&gt;-&lt;1211.0,418.0&gt;&gt; = 6.009005957494474

* uni1FCC (U+1FCC): L&lt;&lt;1417.0,416.0&gt;--&lt;1417.0,127.0&gt;&gt;/B&lt;&lt;1417.0,127.0&gt;-&lt;1423.0,151.0&gt;-&lt;1450.5,129.5&gt;&gt; = 14.036243467926457

* uni1FCF (U+1FCF): B&lt;&lt;503.0,1075.0&gt;-&lt;504.0,1076.0&gt;-&lt;498.0,1079.0&gt;&gt;/L&lt;&lt;498.0,1079.0&gt;--&lt;503.0,1075.0&gt;&gt; = 12.094757077012058

* uni1FEC (U+1FEC): L&lt;&lt;168.0,1147.0&gt;--&lt;173.0,1151.0&gt;&gt;/B&lt;&lt;173.0,1151.0&gt;-&lt;169.0,1149.0&gt;-&lt;168.0,1147.0&gt;&gt; = 12.094757077012058

* uni1FFC (U+1FFC): B&lt;&lt;1325.5,129.5&gt;-&lt;1353.0,151.0&gt;-&lt;1359.0,127.0&gt;&gt;/L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt; = 14.036243467926457

* uni1FFC (U+1FFC): L&lt;&lt;1359.0,127.0&gt;--&lt;1359.0,416.0&gt;&gt;/B&lt;&lt;1359.0,416.0&gt;-&lt;1357.0,397.0&gt;-&lt;1330.0,418.0&gt;&gt; = 6.009005957494474

* uni1FFC (U+1FFC): L&lt;&lt;1536.0,416.0&gt;--&lt;1536.0,127.0&gt;&gt;/B&lt;&lt;1536.0,127.0&gt;-&lt;1542.0,151.0&gt;-&lt;1569.5,129.5&gt;&gt; = 14.036243467926457

* uni200C (U+200C): B&lt;&lt;269.5,516.0&gt;-&lt;258.0,553.0&gt;-&lt;251.0,591.0&gt;&gt;/L&lt;&lt;251.0,591.0&gt;--&lt;251.0,454.0&gt;&gt; = 10.437475351118158

* uni200C (U+200C): B&lt;&lt;271.5,337.5&gt;-&lt;246.0,322.0&gt;-&lt;231.0,320.0&gt;&gt;/L&lt;&lt;231.0,320.0&gt;--&lt;318.0,320.0&gt;&gt; = 7.594643368591447

* uni200C (U+200C): B&lt;&lt;344.0,337.5&gt;-&lt;320.0,353.0&gt;-&lt;311.0,387.0&gt;&gt;/L&lt;&lt;311.0,387.0&gt;--&lt;312.0,383.0&gt;&gt; = 0.7902365024287767

* uni200C (U+200C): B&lt;&lt;446.5,342.5&gt;-&lt;422.0,323.0&gt;-&lt;398.0,320.0&gt;&gt;/L&lt;&lt;398.0,320.0&gt;--&lt;523.0,320.0&gt;&gt; = 7.125016348901757

* uni200C (U+200C): L&lt;&lt;311.0,387.0&gt;--&lt;312.0,383.0&gt;&gt;/L&lt;&lt;312.0,383.0&gt;--&lt;294.0,440.0&gt;&gt; = 3.489324905796376

* uni200C (U+200C): L&lt;&lt;343.0,320.0&gt;--&lt;386.0,320.0&gt;&gt;/B&lt;&lt;386.0,320.0&gt;-&lt;368.0,322.0&gt;-&lt;344.0,337.5&gt;&gt; = 6.340191745909908

* uni200E (U+200E): B&lt;&lt;250.5,447.5&gt;-&lt;278.0,458.0&gt;-&lt;277.0,435.0&gt;&gt;/L&lt;&lt;277.0,435.0&gt;--&lt;277.0,845.0&gt;&gt; = 2.4895529219991284

* uni200E (U+200E): B&lt;&lt;617.5,447.0&gt;-&lt;644.0,458.0&gt;-&lt;646.0,435.0&gt;&gt;/L&lt;&lt;646.0,435.0&gt;--&lt;646.0,648.0&gt;&gt; = 4.969740728110289

* uni200E (U+200E): B&lt;&lt;817.5,831.5&gt;-&lt;790.0,822.0&gt;-&lt;792.0,846.0&gt;&gt;/L&lt;&lt;792.0,846.0&gt;--&lt;792.0,439.0&gt;&gt; = 4.763641690726143

* uni200E (U+200E): L&lt;&lt;277.0,435.0&gt;--&lt;277.0,845.0&gt;&gt;/B&lt;&lt;277.0,845.0&gt;-&lt;276.0,822.0&gt;-&lt;249.5,831.5&gt;&gt; = 2.4895529219991284

* uni200E (U+200E): L&lt;&lt;409.0,785.0&gt;--&lt;417.0,436.0&gt;&gt;/B&lt;&lt;417.0,436.0&gt;-&lt;421.0,458.0&gt;-&lt;447.0,447.0&gt;&gt; = 11.617986809683527

* uni200E (U+200E): L&lt;&lt;442.0,947.0&gt;--&lt;365.0,947.0&gt;&gt;/B&lt;&lt;365.0,947.0&gt;-&lt;405.0,946.0&gt;-&lt;428.5,930.5&gt;&gt; = 1.4320961841645452

* uni200E (U+200E): L&lt;&lt;461.0,543.0&gt;--&lt;409.0,785.0&gt;&gt;/L&lt;&lt;409.0,785.0&gt;--&lt;417.0,436.0&gt;&gt; = 10.813950694012595

* uni200E (U+200E): L&lt;&lt;792.0,846.0&gt;--&lt;792.0,439.0&gt;&gt;/B&lt;&lt;792.0,439.0&gt;-&lt;794.0,458.0&gt;-&lt;819.5,447.0&gt;&gt; = 6.009005957494474

* uni200F (U+200F): B&lt;&lt;250.5,449.5&gt;-&lt;278.0,460.0&gt;-&lt;277.0,437.0&gt;&gt;/L&lt;&lt;277.0,437.0&gt;--&lt;277.0,847.0&gt;&gt; = 2.4895529219991284

* uni200F (U+200F): B&lt;&lt;618.5,448.5&gt;-&lt;644.0,460.0&gt;-&lt;646.0,437.0&gt;&gt;/L&lt;&lt;646.0,437.0&gt;--&lt;653.0,786.0&gt;&gt; = 6.118785675436484

* uni200F (U+200F): L&lt;&lt;277.0,437.0&gt;--&lt;277.0,847.0&gt;&gt;/B&lt;&lt;277.0,847.0&gt;-&lt;276.0,824.0&gt;-&lt;249.5,833.5&gt;&gt; = 2.4895529219991284

* uni200F (U+200F): L&lt;&lt;409.0,785.0&gt;--&lt;417.0,438.0&gt;&gt;/B&lt;&lt;417.0,438.0&gt;-&lt;422.0,460.0&gt;-&lt;447.5,448.5&gt;&gt; = 14.12497226544709

* uni200F (U+200F): L&lt;&lt;461.0,545.0&gt;--&lt;409.0,785.0&gt;&gt;/L&lt;&lt;409.0,785.0&gt;--&lt;417.0,438.0&gt;&gt; = 10.904416475575344

* uni200F (U+200F): L&lt;&lt;646.0,437.0&gt;--&lt;653.0,786.0&gt;&gt;/L&lt;&lt;653.0,786.0&gt;--&lt;611.0,552.0&gt;&gt; = 9.026465895717015

* uni200F (U+200F): L&lt;&lt;792.0,847.0&gt;--&lt;792.0,437.0&gt;&gt;/B&lt;&lt;792.0,437.0&gt;-&lt;793.0,460.0&gt;-&lt;820.0,450.0&gt;&gt; = 2.4895529219991284

* uni202A (U+202A): L&lt;&lt;523.0,1104.0&gt;--&lt;523.0,1029.0&gt;&gt;/B&lt;&lt;523.0,1029.0&gt;-&lt;530.0,1059.0&gt;-&lt;549.0,1069.0&gt;&gt; = 13.134022306396327

* uni202C (U+202C): L&lt;&lt;495.0,588.0&gt;--&lt;498.0,445.0&gt;&gt;/L&lt;&lt;498.0,445.0&gt;--&lt;498.0,472.0&gt;&gt; = 1.2018330644521886

* uni202C (U+202C): L&lt;&lt;605.0,805.0&gt;--&lt;632.0,809.0&gt;&gt;/L&lt;&lt;632.0,809.0&gt;--&lt;488.0,817.0&gt;&gt; = 11.60679914134491

* uni202D (U+202D): B&lt;&lt;704.5,400.0&gt;-&lt;675.0,333.0&gt;-&lt;597.0,320.0&gt;&gt;/L&lt;&lt;597.0,320.0&gt;--&lt;728.0,320.0&gt;&gt; = 9.462322208025613

* uni202D (U+202D): L&lt;&lt;343.0,320.0&gt;--&lt;473.0,320.0&gt;&gt;/B&lt;&lt;473.0,320.0&gt;-&lt;393.0,333.0&gt;-&lt;365.0,400.0&gt;&gt; = 9.2298862437277

* uni202D (U+202D): L&lt;&lt;523.0,1104.0&gt;--&lt;523.0,1029.0&gt;&gt;/B&lt;&lt;523.0,1029.0&gt;-&lt;530.0,1059.0&gt;-&lt;549.0,1069.0&gt;&gt; = 13.134022306396327

* uni202E (U+202E): B&lt;&lt;704.5,400.0&gt;-&lt;675.0,333.0&gt;-&lt;597.0,320.0&gt;&gt;/L&lt;&lt;597.0,320.0&gt;--&lt;728.0,320.0&gt;&gt; = 9.462322208025613

* uni202E (U+202E): L&lt;&lt;343.0,320.0&gt;--&lt;473.0,320.0&gt;&gt;/B&lt;&lt;473.0,320.0&gt;-&lt;393.0,333.0&gt;-&lt;365.0,400.0&gt;&gt; = 9.2298862437277

* uni203D (U+203D): B&lt;&lt;360.5,1090.0&gt;-&lt;314.0,1076.0&gt;-&lt;292.0,1054.0&gt;&gt;/B&lt;&lt;292.0,1054.0&gt;-&lt;303.0,1064.0&gt;-&lt;309.0,1046.0&gt;&gt; = 2.726310993906212

* uni2062 (U+2062): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uni2062 (U+2062): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uni2063 (U+2063): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uni2063 (U+2063): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uni2064 (U+2064): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uni2064 (U+2064): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uni2068 (U+2068): L&lt;&lt;221.0,1475.0&gt;--&lt;223.0,1499.0&gt;&gt;/L&lt;&lt;223.0,1499.0&gt;--&lt;223.0,1477.0&gt;&gt; = 4.763641690726143

* uni2068 (U+2068): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uni2068 (U+2068): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uni2103 (U+2103): B&lt;&lt;717.0,1310.0&gt;-&lt;820.0,1293.0&gt;-&lt;872.0,1243.0&gt;&gt;/B&lt;&lt;872.0,1243.0&gt;-&lt;863.0,1257.0&gt;-&lt;885.0,1282.0&gt;&gt; = 13.388076441967804

* uni2117 (U+2117): L&lt;&lt;497.0,452.0&gt;--&lt;503.0,273.0&gt;&gt;/L&lt;&lt;503.0,273.0&gt;--&lt;502.0,302.0&gt;&gt; = 0.05512388092142797

* uni2222 (U+2222): L&lt;&lt;744.0,1044.0&gt;--&lt;741.0,1042.0&gt;&gt;/L&lt;&lt;741.0,1042.0&gt;--&lt;876.0,1109.0&gt;&gt; = 7.295032999782071

* uni2222 (U+2222): L&lt;&lt;875.0,144.0&gt;--&lt;741.0,212.0&gt;&gt;/B&lt;&lt;741.0,212.0&gt;-&lt;749.0,205.0&gt;-&lt;742.5,194.0&gt;&gt; = 14.2798317097728

* uni2300 (U+2300): B&lt;&lt;279.5,556.5&gt;-&lt;283.0,524.0&gt;-&lt;263.0,501.0&gt;&gt;/L&lt;&lt;263.0,501.0&gt;--&lt;662.0,903.0&gt;&gt; = 3.7763231673003825

* uni2300 (U+2300): B&lt;&lt;793.5,697.0&gt;-&lt;790.0,729.0&gt;-&lt;810.0,752.0&gt;&gt;/L&lt;&lt;810.0,752.0&gt;--&lt;411.0,351.0&gt;&gt; = 3.84767394806145

* uni2300 (U+2300): L&lt;&lt;263.0,501.0&gt;--&lt;662.0,903.0&gt;&gt;/B&lt;&lt;662.0,903.0&gt;-&lt;638.0,882.0&gt;-&lt;606.5,885.0&gt;&gt; = 4.028664765419825

* uni2300 (U+2300): L&lt;&lt;810.0,752.0&gt;--&lt;411.0,351.0&gt;&gt;/B&lt;&lt;411.0,351.0&gt;-&lt;435.0,371.0&gt;-&lt;466.5,368.5&gt;&gt; = 5.337668058103043

* uni2422 (U+2422): L&lt;&lt;165.0,84.0&gt;--&lt;165.0,795.0&gt;&gt;/L&lt;&lt;165.0,795.0&gt;--&lt;151.0,713.0&gt;&gt; = 9.68878656036679

* uni2422 (U+2422): L&lt;&lt;374.0,1167.0&gt;--&lt;330.0,1119.0&gt;&gt;/L&lt;&lt;330.0,1119.0&gt;--&lt;467.0,1240.0&gt;&gt; = 6.038234895903548

* uni26AD (U+26AD): L&lt;&lt;537.0,662.0&gt;--&lt;537.0,664.0&gt;&gt;/B&lt;&lt;537.0,664.0&gt;-&lt;534.0,647.0&gt;-&lt;534.0,629.0&gt;&gt; = 10.007979801441312

* uni2E18 (U+2E18): B&lt;&lt;683.5,-293.5&gt;-&lt;730.0,-279.0&gt;-&lt;752.0,-257.0&gt;&gt;/B&lt;&lt;752.0,-257.0&gt;-&lt;741.0,-267.0&gt;-&lt;735.5,-248.5&gt;&gt; = 2.726310993906212

* uniA642 (U+A642): B&lt;&lt;380.0,16.0&gt;-&lt;351.0,36.0&gt;-&lt;337.0,60.0&gt;&gt;/L&lt;&lt;337.0,60.0&gt;--&lt;342.0,43.0&gt;&gt; = 13.866896829494456

* uniFB51 (U+FB51): B&lt;&lt;460.5,1618.5&gt;-&lt;470.0,1594.0&gt;-&lt;467.0,1583.0&gt;&gt;/B&lt;&lt;467.0,1583.0&gt;-&lt;502.0,1693.0&gt;-&lt;591.5,1771.0&gt;&gt; = 2.3950055168722097

* uniFB55 (U+FB55): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFB59 (U+FB59): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFB5D (U+FB5D): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFB61 (U+FB61): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFB65 (U+FB65): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFB67 (U+FB67): L&lt;&lt;565.0,1716.0&gt;--&lt;564.0,1365.0&gt;&gt;/B&lt;&lt;564.0,1365.0&gt;-&lt;571.0,1461.0&gt;-&lt;626.5,1513.5&gt;&gt; = 4.007201127423053

* uniFB68 (U+FB68): L&lt;&lt;741.0,1716.0&gt;--&lt;740.0,1365.0&gt;&gt;/B&lt;&lt;740.0,1365.0&gt;-&lt;747.0,1461.0&gt;-&lt;802.5,1513.5&gt;&gt; = 4.007201127423053

* uniFB69 (U+FB69): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFB69 (U+FB69): L&lt;&lt;741.0,1716.0&gt;--&lt;740.0,1365.0&gt;&gt;/B&lt;&lt;740.0,1365.0&gt;-&lt;747.0,1461.0&gt;-&lt;802.5,1513.5&gt;&gt; = 4.007201127423053

* uniFB6C (U+FB6C): L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uniFB70 (U+FB70): L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uniFB74 (U+FB74): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFB78 (U+FB78): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFB7C (U+FB7C): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFB80 (U+FB80): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFB89 (U+FB89): L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;/B&lt;&lt;334.0,1433.0&gt;-&lt;341.0,1529.0&gt;-&lt;396.5,1581.5&gt;&gt; = 4.007201127423053

* uniFB8D (U+FB8D): L&lt;&lt;538.0,1483.0&gt;--&lt;537.0,1132.0&gt;&gt;/B&lt;&lt;537.0,1132.0&gt;-&lt;544.0,1228.0&gt;-&lt;599.5,1280.5&gt;&gt; = 4.007201127423053

* uniFBA1 (U+FBA1): L&lt;&lt;538.0,1298.0&gt;--&lt;537.0,947.0&gt;&gt;/B&lt;&lt;537.0,947.0&gt;-&lt;544.0,1043.0&gt;-&lt;599.5,1095.5&gt;&gt; = 4.007201127423053

* uniFBA2 (U+FBA2): L&lt;&lt;335.0,1716.0&gt;--&lt;334.0,1365.0&gt;&gt;/B&lt;&lt;334.0,1365.0&gt;-&lt;341.0,1461.0&gt;-&lt;396.5,1513.5&gt;&gt; = 4.007201127423053

* uniFBA3 (U+FBA3): L&lt;&lt;335.0,1716.0&gt;--&lt;334.0,1365.0&gt;&gt;/B&lt;&lt;334.0,1365.0&gt;-&lt;341.0,1461.0&gt;-&lt;396.5,1513.5&gt;&gt; = 4.007201127423053

* uniFBA3 (U+FBA3): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFBA5 (U+FBA5): B&lt;&lt;184.0,1403.5&gt;-&lt;235.0,1431.0&gt;-&lt;286.0,1444.0&gt;&gt;/B&lt;&lt;286.0,1444.0&gt;-&lt;236.0,1440.0&gt;-&lt;195.0,1492.5&gt;&gt; = 9.726356189284708

* uniFBA8 (U+FBA8): L&lt;&lt;811.0,191.0&gt;--&lt;811.0,191.0&gt;&gt;/B&lt;&lt;811.0,191.0&gt;-&lt;780.0,185.0&gt;-&lt;743.5,163.0&gt;&gt; = 10.954062643398332

* uniFBAB (U+FBAB): B&lt;&lt;691.5,193.0&gt;-&lt;678.0,195.0&gt;-&lt;682.0,205.0&gt;&gt;/B&lt;&lt;682.0,205.0&gt;-&lt;596.0,82.0&gt;-&lt;487.0,17.0&gt;&gt; = 13.159335726495803

* uniFBAC (U+FBAC): B&lt;&lt;434.5,470.0&gt;-&lt;445.0,452.0&gt;-&lt;467.0,437.0&gt;&gt;/B&lt;&lt;467.0,437.0&gt;-&lt;465.0,439.0&gt;-&lt;480.0,447.0&gt;&gt; = 10.713123022790997

* uniFBAC (U+FBAC): B&lt;&lt;816.0,674.5&gt;-&lt;804.0,734.0&gt;-&lt;802.0,781.0&gt;&gt;/B&lt;&lt;802.0,781.0&gt;-&lt;802.0,651.0&gt;-&lt;784.5,551.5&gt;&gt; = 2.436648246810141

* uniFBAD (U+FBAD): B&lt;&lt;434.5,470.0&gt;-&lt;445.0,452.0&gt;-&lt;467.0,437.0&gt;&gt;/B&lt;&lt;467.0,437.0&gt;-&lt;465.0,439.0&gt;-&lt;480.0,447.0&gt;&gt; = 10.713123022790997

* uniFBAD (U+FBAD): B&lt;&lt;816.0,674.5&gt;-&lt;804.0,734.0&gt;-&lt;802.0,781.0&gt;&gt;/B&lt;&lt;802.0,781.0&gt;-&lt;802.0,651.0&gt;-&lt;784.5,551.5&gt;&gt; = 2.436648246810141

* uniFBB1 (U+FBB1): B&lt;&lt;98.0,863.5&gt;-&lt;149.0,891.0&gt;-&lt;200.0,904.0&gt;&gt;/B&lt;&lt;200.0,904.0&gt;-&lt;150.0,900.0&gt;-&lt;109.0,952.5&gt;&gt; = 9.726356189284708

* uniFBC0 (U+FBC0): L&lt;&lt;538.0,1620.0&gt;--&lt;537.0,1269.0&gt;&gt;/B&lt;&lt;537.0,1269.0&gt;-&lt;544.0,1365.0&gt;-&lt;599.5,1417.5&gt;&gt; = 4.007201127423053

* uniFBC1 (U+FBC1): L&lt;&lt;538.0,279.0&gt;--&lt;537.0,-72.0&gt;&gt;/B&lt;&lt;537.0,-72.0&gt;-&lt;544.0,24.0&gt;-&lt;599.5,76.5&gt;&gt; = 4.007201127423053

* uniFBD4 (U+FBD4): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uniFBD4 (U+FBD4): L&lt;&lt;854.0,793.0&gt;--&lt;851.0,1418.0&gt;&gt;/B&lt;&lt;851.0,1418.0&gt;-&lt;846.0,1386.0&gt;-&lt;815.0,1347.0&gt;&gt; = 9.155676780060624

* uniFBD6 (U+FBD6): B&lt;&lt;584.0,1202.0&gt;-&lt;587.0,1232.0&gt;-&lt;619.0,1276.0&gt;&gt;/L&lt;&lt;619.0,1276.0&gt;--&lt;399.0,1057.0&gt;&gt; = 9.103140693287445

* uniFBD6 (U+FBD6): B&lt;&lt;619.0,708.0&gt;-&lt;597.0,711.0&gt;-&lt;566.0,732.0&gt;&gt;/L&lt;&lt;566.0,732.0&gt;--&lt;763.0,532.0&gt;&gt; = 11.318484401941035

* uniFBD6 (U+FBD6): L&lt;&lt;376.0,925.0&gt;--&lt;476.0,823.0&gt;&gt;/B&lt;&lt;476.0,823.0&gt;-&lt;452.0,860.0&gt;-&lt;449.0,885.0&gt;&gt; = 11.4633296866799

* uniFBD6 (U+FBD6): L&lt;&lt;776.0,1432.0&gt;--&lt;700.0,1356.0&gt;&gt;/B&lt;&lt;700.0,1356.0&gt;-&lt;732.0,1379.0&gt;-&lt;754.0,1382.0&gt;&gt; = 9.293308599397053

* uniFBE7 (U+FBE7): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFBE9 (U+FBE9): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFBFF (U+FBFF): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFCA1 (U+FCA1): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFCA2 (U+FCA2): L&lt;&lt;-4.0,403.0&gt;--&lt;894.0,403.0&gt;&gt;/B&lt;&lt;894.0,403.0&gt;-&lt;883.0,405.0&gt;-&lt;853.5,443.0&gt;&gt; = 10.304846468766044

* uniFCC9 (U+FCC9): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFCCA (U+FCCA): L&lt;&lt;-4.0,403.0&gt;--&lt;894.0,403.0&gt;&gt;/B&lt;&lt;894.0,403.0&gt;-&lt;883.0,405.0&gt;-&lt;853.5,443.0&gt;&gt; = 10.304846468766044

* uniFCCB (U+FCCB): L&lt;&lt;-4.0,403.0&gt;--&lt;894.0,403.0&gt;&gt;/B&lt;&lt;894.0,403.0&gt;-&lt;883.0,405.0&gt;-&lt;853.5,443.0&gt;&gt; = 10.304846468766044

* uniFD88 (U+FD88): L&lt;&lt;-4.0,403.0&gt;--&lt;894.0,403.0&gt;&gt;/B&lt;&lt;894.0,403.0&gt;-&lt;883.0,405.0&gt;-&lt;853.5,443.0&gt;&gt; = 10.304846468766044

* uniFDF4 (U+FDF4): B&lt;&lt;397.0,212.0&gt;-&lt;370.0,230.0&gt;-&lt;377.0,249.0&gt;&gt;/B&lt;&lt;377.0,249.0&gt;-&lt;368.0,222.0&gt;-&lt;323.0,197.0&gt;&gt; = 1.7899106082458724

* uniFDF4 (U+FDF4): L&lt;&lt;453.0,409.0&gt;--&lt;453.0,408.0&gt;&gt;/B&lt;&lt;453.0,408.0&gt;-&lt;469.0,483.0&gt;-&lt;512.0,520.0&gt;&gt; = 12.042575142884978

* uniFDFA (U+FDFA): B&lt;&lt;1064.5,806.0&gt;-&lt;1024.0,759.0&gt;-&lt;964.0,754.0&gt;&gt;/L&lt;&lt;964.0,754.0&gt;--&lt;964.0,754.0&gt;&gt; = 4.763641690726143

* uniFDFB (U+FDFB): L&lt;&lt;599.0,425.0&gt;--&lt;599.0,420.0&gt;&gt;/L&lt;&lt;599.0,420.0&gt;--&lt;597.0,653.0&gt;&gt; = 0.4917971879457214

* uniFDFC (U+FDFC): L&lt;&lt;554.0,1149.0&gt;--&lt;554.0,1065.0&gt;&gt;/B&lt;&lt;554.0,1065.0&gt;-&lt;556.0,1115.0&gt;-&lt;585.0,1137.5&gt;&gt; = 2.2906100426384346

* uniFDFC (U+FDFC): L&lt;&lt;745.0,360.0&gt;--&lt;746.0,331.0&gt;&gt;/L&lt;&lt;746.0,331.0&gt;--&lt;746.0,555.0&gt;&gt; = 1.9749340108819595

* uniFDFD (U+FDFD): B&lt;&lt;453.5,575.0&gt;-&lt;462.0,583.0&gt;-&lt;458.0,582.0&gt;&gt;/B&lt;&lt;458.0,582.0&gt;-&lt;462.0,582.0&gt;-&lt;453.5,589.5&gt;&gt; = 14.036243467926484

* uniFDFD (U+FDFD): B&lt;&lt;731.0,1113.0&gt;-&lt;727.0,1118.0&gt;-&lt;724.0,1125.0&gt;&gt;/B&lt;&lt;724.0,1125.0&gt;-&lt;725.0,1119.0&gt;-&lt;726.0,1114.0&gt;&gt; = 13.736268305622554

* uniFDFD (U+FDFD): L&lt;&lt;95.0,1107.0&gt;--&lt;106.0,1122.0&gt;&gt;/B&lt;&lt;106.0,1122.0&gt;-&lt;104.0,1119.0&gt;-&lt;99.0,1114.0&gt;&gt; = 2.563770211464813

* uniFDFD (U+FDFD): L&lt;&lt;993.0,1148.0&gt;--&lt;996.0,1126.0&gt;&gt;/L&lt;&lt;996.0,1126.0&gt;--&lt;996.0,1146.0&gt;&gt; = 7.765166018425308

* uniFE00 (U+FE00): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE00 (U+FE00): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE01 (U+FE01): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE01 (U+FE01): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE02 (U+FE02): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE02 (U+FE02): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE03 (U+FE03): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE03 (U+FE03): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE04 (U+FE04): B&lt;&lt;517.0,681.5&gt;-&lt;533.0,680.0&gt;-&lt;545.0,680.0&gt;&gt;/B&lt;&lt;545.0,680.0&gt;-&lt;510.0,672.0&gt;-&lt;480.0,651.0&gt;&gt; = 12.875001559612462

* uniFE04 (U+FE04): B&lt;&lt;575.5,681.0&gt;-&lt;563.0,680.0&gt;-&lt;545.0,680.0&gt;&gt;/B&lt;&lt;545.0,680.0&gt;-&lt;569.0,686.0&gt;-&lt;595.0,687.0&gt;&gt; = 14.036243467926457

* uniFE04 (U+FE04): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE04 (U+FE04): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE05 (U+FE05): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uniFE05 (U+FE05): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uniFE06 (U+FE06): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE06 (U+FE06): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE07 (U+FE07): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uniFE07 (U+FE07): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uniFE08 (U+FE08): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uniFE08 (U+FE08): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uniFE09 (U+FE09): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uniFE09 (U+FE09): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uniFE0A (U+FE0A): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE0A (U+FE0A): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE0B (U+FE0B): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE0B (U+FE0B): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE0C (U+FE0C): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE0C (U+FE0C): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE0D (U+FE0D): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE0D (U+FE0D): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE0E (U+FE0E): B&lt;&lt;691.0,681.5&gt;-&lt;707.0,680.0&gt;-&lt;719.0,680.0&gt;&gt;/B&lt;&lt;719.0,680.0&gt;-&lt;684.0,672.0&gt;-&lt;654.0,651.0&gt;&gt; = 12.875001559612462

* uniFE0E (U+FE0E): B&lt;&lt;749.5,681.0&gt;-&lt;737.0,680.0&gt;-&lt;719.0,680.0&gt;&gt;/B&lt;&lt;719.0,680.0&gt;-&lt;743.0,686.0&gt;-&lt;769.0,687.0&gt;&gt; = 14.036243467926457

* uniFE0E (U+FE0E): L&lt;&lt;980.0,1176.0&gt;--&lt;981.0,1171.0&gt;&gt;/L&lt;&lt;981.0,1171.0&gt;--&lt;981.0,1205.0&gt;&gt; = 11.309932474020195

* uniFE0E (U+FE0E): L&lt;&lt;981.0,976.0&gt;--&lt;981.0,1097.0&gt;&gt;/B&lt;&lt;981.0,1097.0&gt;-&lt;966.0,1032.0&gt;-&lt;910.5,986.5&gt;&gt; = 12.994616791916512

* uniFE0F (U+FE0F): L&lt;&lt;28.0,245.0&gt;--&lt;31.0,354.0&gt;&gt;/L&lt;&lt;31.0,354.0&gt;--&lt;32.0,346.0&gt;&gt; = 8.701566404085526

* uniFE0F (U+FE0F): L&lt;&lt;32.0,1559.0&gt;--&lt;31.0,1551.0&gt;&gt;/L&lt;&lt;31.0,1551.0&gt;--&lt;28.0,1659.0&gt;&gt; = 8.716156620096388

* uniFE7D (U+FE7D): B&lt;&lt;580.5,1237.5&gt;-&lt;539.0,1270.0&gt;-&lt;537.0,1293.0&gt;&gt;/B&lt;&lt;537.0,1293.0&gt;-&lt;534.0,1270.0&gt;-&lt;492.5,1237.5&gt;&gt; = 12.401148699282784

* uniFE84 (U+FE84): B&lt;&lt;327.0,1377.5&gt;-&lt;378.0,1405.0&gt;-&lt;429.0,1418.0&gt;&gt;/B&lt;&lt;429.0,1418.0&gt;-&lt;379.0,1414.0&gt;-&lt;338.0,1466.5&gt;&gt; = 9.726356189284708

* uniFE86 (U+FE86): B&lt;&lt;233.0,953.5&gt;-&lt;284.0,981.0&gt;-&lt;335.0,994.0&gt;&gt;/B&lt;&lt;335.0,994.0&gt;-&lt;285.0,990.0&gt;-&lt;244.0,1042.5&gt;&gt; = 9.726356189284708

* uniFE88 (U+FE88): B&lt;&lt;329.0,-291.5&gt;-&lt;380.0,-264.0&gt;-&lt;431.0,-251.0&gt;&gt;/B&lt;&lt;431.0,-251.0&gt;-&lt;381.0,-255.0&gt;-&lt;340.0,-202.5&gt;&gt; = 9.726356189284708

* uniFE8A (U+FE8A): B&lt;&lt;231.0,881.5&gt;-&lt;282.0,909.0&gt;-&lt;333.0,922.0&gt;&gt;/B&lt;&lt;333.0,922.0&gt;-&lt;283.0,918.0&gt;-&lt;242.0,970.5&gt;&gt; = 9.726356189284708

* uniFE8B (U+FE8B): B&lt;&lt;241.0,1113.5&gt;-&lt;292.0,1141.0&gt;-&lt;343.0,1154.0&gt;&gt;/B&lt;&lt;343.0,1154.0&gt;-&lt;293.0,1150.0&gt;-&lt;252.0,1202.5&gt;&gt; = 9.726356189284708

* uniFE8C (U+FE8C): B&lt;&lt;233.0,1174.5&gt;-&lt;284.0,1202.0&gt;-&lt;335.0,1215.0&gt;&gt;/B&lt;&lt;335.0,1215.0&gt;-&lt;285.0,1211.0&gt;-&lt;244.0,1263.5&gt;&gt; = 9.726356189284708

* uniFE8C (U+FE8C): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFE92 (U+FE92): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFE98 (U+FE98): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFE9C (U+FE9C): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFE9F (U+FE9F): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFEA3 (U+FEA3): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFEA7 (U+FEA7): L&lt;&lt;-5.0,403.0&gt;--&lt;893.0,403.0&gt;&gt;/B&lt;&lt;893.0,403.0&gt;-&lt;882.0,405.0&gt;-&lt;852.5,443.0&gt;&gt; = 10.304846468766044

* uniFEBA (U+FEBA): B&lt;&lt;910.0,508.0&gt;-&lt;855.0,416.0&gt;-&lt;753.0,395.0&gt;&gt;/L&lt;&lt;753.0,395.0&gt;--&lt;1229.0,402.0&gt;&gt; = 10.791109738200037

* uniFEBB (U+FEBB): L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uniFEBC (U+FEBC): L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uniFEBE (U+FEBE): B&lt;&lt;910.0,508.0&gt;-&lt;855.0,416.0&gt;-&lt;753.0,395.0&gt;&gt;/L&lt;&lt;753.0,395.0&gt;--&lt;1229.0,402.0&gt;&gt; = 10.791109738200037

* uniFEBF (U+FEBF): L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uniFEC0 (U+FEC0): L&lt;&lt;251.0,237.0&gt;--&lt;253.0,237.0&gt;&gt;/B&lt;&lt;253.0,237.0&gt;-&lt;201.0,246.0&gt;-&lt;167.5,258.5&gt;&gt; = 9.819300638757893

* uniFEC2 (U+FEC2): L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uniFEC3 (U+FEC3): L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uniFEC4 (U+FEC4): L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uniFEC6 (U+FEC6): L&lt;&lt;448.0,1509.0&gt;--&lt;448.0,602.0&gt;&gt;/B&lt;&lt;448.0,602.0&gt;-&lt;450.0,649.0&gt;-&lt;476.0,711.5&gt;&gt; = 2.436648246810141

* uniFEC7 (U+FEC7): L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uniFEC8 (U+FEC8): L&lt;&lt;440.0,1509.0&gt;--&lt;440.0,602.0&gt;&gt;/B&lt;&lt;440.0,602.0&gt;-&lt;442.0,649.0&gt;-&lt;468.0,711.5&gt;&gt; = 2.436648246810141

* uniFECA (U+FECA): B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uniFECB (U+FECB): L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uniFECE (U+FECE): B&lt;&lt;368.5,660.0&gt;-&lt;396.0,614.0&gt;-&lt;428.0,576.0&gt;&gt;/L&lt;&lt;428.0,576.0&gt;--&lt;418.0,595.0&gt;&gt; = 12.342366945152207

* uniFECF (U+FECF): L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;/B&lt;&lt;406.0,403.0&gt;-&lt;364.0,405.0&gt;-&lt;348.5,449.0&gt;&gt; = 3.0011087885860364

* uniFED3 (U+FED3): L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uniFED7 (U+FED7): L&lt;&lt;878.0,402.0&gt;--&lt;852.0,549.0&gt;&gt;/B&lt;&lt;852.0,549.0&gt;-&lt;855.0,526.0&gt;-&lt;828.0,520.5&gt;&gt; = 2.598805348560221

* uniFEDA (U+FEDA): L&lt;&lt;239.0,403.0&gt;--&lt;238.0,403.0&gt;&gt;/L&lt;&lt;238.0,403.0&gt;--&lt;856.0,386.0&gt;&gt; = 1.5757001333657503

* uniFEE0 (U+FEE0): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;544.5,265.5&gt;&gt; = 5.710593137499633

* uniFEE8 (U+FEE8): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFEEB (U+FEEB): B&lt;&lt;336.5,401.5&gt;-&lt;375.0,400.0&gt;-&lt;406.0,393.0&gt;&gt;/B&lt;&lt;406.0,393.0&gt;-&lt;320.0,421.0&gt;-&lt;268.5,491.5&gt;&gt; = 5.309929881707482

* uniFEEB (U+FEEB): B&lt;&lt;821.0,822.5&gt;-&lt;803.0,882.0&gt;-&lt;801.0,928.0&gt;&gt;/B&lt;&lt;801.0,928.0&gt;-&lt;804.0,812.0&gt;-&lt;778.0,704.0&gt;&gt; = 1.0080957511116757

* uniFEEC (U+FEEC): B&lt;&lt;841.5,477.0&gt;-&lt;794.0,412.0&gt;-&lt;720.0,403.0&gt;&gt;/L&lt;&lt;720.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt; = 7.045172321115355

* uniFEF4 (U+FEF4): L&lt;&lt;571.0,313.0&gt;--&lt;571.0,314.0&gt;&gt;/B&lt;&lt;571.0,314.0&gt;-&lt;569.0,294.0&gt;-&lt;545.5,265.5&gt;&gt; = 5.710593137499633

* uniFEF5 (U+FEF5): B&lt;&lt;749.0,442.5&gt;-&lt;713.0,402.0&gt;-&lt;666.0,400.0&gt;&gt;/L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt; = 2.071711911079328

* uniFEF5 (U+FEF5): B&lt;&lt;798.0,458.5&gt;-&lt;790.0,496.0&gt;-&lt;800.0,527.0&gt;&gt;/B&lt;&lt;800.0,527.0&gt;-&lt;785.0,483.0&gt;-&lt;749.0,442.5&gt;&gt; = 0.9460134223984321

* uniFEF7 (U+FEF7): B&lt;&lt;61.0,1377.5&gt;-&lt;112.0,1405.0&gt;-&lt;163.0,1418.0&gt;&gt;/B&lt;&lt;163.0,1418.0&gt;-&lt;113.0,1414.0&gt;-&lt;72.0,1466.5&gt;&gt; = 9.726356189284708

* uniFEF7 (U+FEF7): B&lt;&lt;749.0,442.5&gt;-&lt;713.0,402.0&gt;-&lt;666.0,400.0&gt;&gt;/L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt; = 2.071711911079328

* uniFEF7 (U+FEF7): B&lt;&lt;798.0,458.5&gt;-&lt;790.0,496.0&gt;-&lt;800.0,527.0&gt;&gt;/B&lt;&lt;800.0,527.0&gt;-&lt;785.0,483.0&gt;-&lt;749.0,442.5&gt;&gt; = 0.9460134223984321

* uniFEF8 (U+FEF8): B&lt;&lt;-1.0,1377.5&gt;-&lt;50.0,1405.0&gt;-&lt;101.0,1418.0&gt;&gt;/B&lt;&lt;101.0,1418.0&gt;-&lt;51.0,1414.0&gt;-&lt;10.0,1466.5&gt;&gt; = 9.726356189284708

* uniFEF9 (U+FEF9): B&lt;&lt;329.0,-291.5&gt;-&lt;380.0,-264.0&gt;-&lt;431.0,-251.0&gt;&gt;/B&lt;&lt;431.0,-251.0&gt;-&lt;381.0,-255.0&gt;-&lt;340.0,-202.5&gt;&gt; = 9.726356189284708

* uniFEF9 (U+FEF9): B&lt;&lt;749.0,442.5&gt;-&lt;713.0,402.0&gt;-&lt;666.0,400.0&gt;&gt;/L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt; = 2.071711911079328

* uniFEF9 (U+FEF9): B&lt;&lt;798.0,458.5&gt;-&lt;790.0,496.0&gt;-&lt;800.0,527.0&gt;&gt;/B&lt;&lt;800.0,527.0&gt;-&lt;785.0,483.0&gt;-&lt;749.0,442.5&gt;&gt; = 0.9460134223984321

* uniFEFA (U+FEFA): B&lt;&lt;124.0,-291.5&gt;-&lt;175.0,-264.0&gt;-&lt;226.0,-251.0&gt;&gt;/B&lt;&lt;226.0,-251.0&gt;-&lt;176.0,-255.0&gt;-&lt;135.0,-202.5&gt;&gt; = 9.726356189284708

* uniFEFB (U+FEFB): B&lt;&lt;749.0,442.5&gt;-&lt;713.0,402.0&gt;-&lt;666.0,400.0&gt;&gt;/L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt; = 2.071711911079328

* uniFEFB (U+FEFB): B&lt;&lt;798.0,458.5&gt;-&lt;790.0,496.0&gt;-&lt;800.0,527.0&gt;&gt;/B&lt;&lt;800.0,527.0&gt;-&lt;785.0,483.0&gt;-&lt;749.0,442.5&gt;&gt; = 0.9460134223984321

* uogonek (U+0173): L&lt;&lt;855.0,46.0&gt;--&lt;869.0,188.0&gt;&gt;/B&lt;&lt;869.0,188.0&gt;-&lt;846.0,123.0&gt;-&lt;788.5,68.0&gt;&gt; = 13.855446814830467

* uring (U+016F): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* utilde (U+0169): L&lt;&lt;852.0,55.0&gt;--&lt;876.0,185.0&gt;&gt;/B&lt;&lt;876.0,185.0&gt;-&lt;849.0,122.0&gt;-&lt;790.5,67.0&gt;&gt; = 12.738681420719066

* wasla_ar: B&lt;&lt;460.5,1481.5&gt;-&lt;470.0,1457.0&gt;-&lt;467.0,1446.0&gt;&gt;/B&lt;&lt;467.0,1446.0&gt;-&lt;502.0,1556.0&gt;-&lt;591.5,1634.0&gt;&gt; = 2.3950055168722097

* xi (U+03BE): B&lt;&lt;266.5,1019.5&gt;-&lt;282.0,1056.0&gt;-&lt;314.0,1062.0&gt;&gt;/B&lt;&lt;314.0,1062.0&gt;-&lt;231.0,1067.0&gt;-&lt;163.5,1122.5&gt;&gt; = 14.06704212802033

* zero.slash: L&lt;&lt;402.0,1075.0&gt;--&lt;808.0,365.0&gt;&gt;/B&lt;&lt;808.0,365.0&gt;-&lt;786.0,422.0&gt;-&lt;790.5,493.5&gt;&gt; = 8.657420867231224

* zero.slash: L&lt;&lt;669.0,183.0&gt;--&lt;261.0,896.0&gt;&gt;/B&lt;&lt;261.0,896.0&gt;-&lt;285.0,847.0&gt;-&lt;281.5,784.5&gt;&gt; = 3.684061260071189
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* AE (U+00C6): L&lt;&lt;1042.0,506.0&gt;--&lt;759.0,508.0&gt;&gt;

* AE (U+00C6): L&lt;&lt;1087.0,1009.0&gt;--&lt;759.0,1011.0&gt;&gt;

* AE (U+00C6): L&lt;&lt;1107.0,-34.0&gt;--&lt;668.0,-32.0&gt;&gt;

* AE (U+00C6): L&lt;&lt;668.0,1219.0&gt;--&lt;1087.0,1221.0&gt;&gt;

* AE (U+00C6): L&lt;&lt;759.0,177.0&gt;--&lt;1107.0,178.0&gt;&gt;

* AE (U+00C6): L&lt;&lt;759.0,716.0&gt;--&lt;1042.0,718.0&gt;&gt;

* AEacute (U+01FC): L&lt;&lt;1042.0,506.0&gt;--&lt;759.0,508.0&gt;&gt;

* AEacute (U+01FC): L&lt;&lt;1087.0,1009.0&gt;--&lt;759.0,1011.0&gt;&gt;

* AEacute (U+01FC): L&lt;&lt;1107.0,-34.0&gt;--&lt;668.0,-32.0&gt;&gt;

* AEacute (U+01FC): L&lt;&lt;668.0,1219.0&gt;--&lt;1087.0,1221.0&gt;&gt;

* AEacute (U+01FC): L&lt;&lt;759.0,177.0&gt;--&lt;1107.0,178.0&gt;&gt;

* AEacute (U+01FC): L&lt;&lt;759.0,716.0&gt;--&lt;1042.0,718.0&gt;&gt;

* B (U+0042): L&lt;&lt;382.0,510.0&gt;--&lt;381.0,165.0&gt;&gt;

* Beta (U+0392): L&lt;&lt;402.0,510.0&gt;--&lt;401.0,165.0&gt;&gt;

* Ccedilla (U+00C7): L&lt;&lt;738.0,51.0&gt;--&lt;737.0,-89.0&gt;&gt;

* E (U+0045): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* E (U+0045): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* E (U+0045): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* E (U+0045): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* E (U+0045): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* E (U+0045): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Eacute (U+00C9): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Ebreve (U+0114): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Ebreve (U+0114): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Ebreve (U+0114): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Ebreve (U+0114): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Ebreve (U+0114): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Ebreve (U+0114): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Ecaron (U+011A): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Ecaron (U+011A): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Ecaron (U+011A): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Ecaron (U+011A): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Ecaron (U+011A): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Ecaron (U+011A): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Ecircumflex (U+00CA): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Ecircumflex (U+00CA): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Ecircumflex (U+00CA): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Ecircumflex (U+00CA): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Ecircumflex (U+00CA): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Ecircumflex (U+00CA): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Edieresis (U+00CB): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Edieresis (U+00CB): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Edieresis (U+00CB): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Edieresis (U+00CB): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Edieresis (U+00CB): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Edieresis (U+00CB): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Edotaccent (U+0116): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Edotaccent (U+0116): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Edotaccent (U+0116): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Edotaccent (U+0116): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Edotaccent (U+0116): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Edotaccent (U+0116): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Egrave (U+00C8): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Emacron (U+0112): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Emacron (U+0112): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Emacron (U+0112): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Emacron (U+0112): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Emacron (U+0112): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Emacron (U+0112): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* Eogonek (U+0118): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* Eogonek (U+0118): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Eogonek (U+0118): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* Eogonek (U+0118): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* Eogonek (U+0118): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* Eogonek (U+0118): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* F (U+0046): L&lt;&lt;336.0,1220.0&gt;--&lt;977.0,1221.0&gt;&gt;

* F (U+0046): L&lt;&lt;429.0,677.0&gt;--&lt;862.0,678.0&gt;&gt;

* F (U+0046): L&lt;&lt;862.0,466.0&gt;--&lt;429.0,467.0&gt;&gt;

* F (U+0046): L&lt;&lt;977.0,1009.0&gt;--&lt;429.0,1010.0&gt;&gt;

* G (U+0047): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* G (U+0047): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* G (U+0047): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* Gamma (U+0393): L&lt;&lt;399.0,1111.0&gt;--&lt;403.0,129.0&gt;&gt;

* Gbreve (U+011E): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* Gbreve (U+011E): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* Gbreve (U+011E): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* Gcaron (U+01E6): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* Gcaron (U+01E6): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* Gcaron (U+01E6): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* Gcircumflex (U+011C): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* Gcircumflex (U+011C): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* Gcircumflex (U+011C): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* Gdotaccent (U+0120): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* Gdotaccent (U+0120): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* Gdotaccent (U+0120): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* J (U+004A): L&lt;&lt;443.0,1221.0&gt;--&lt;872.0,1219.0&gt;&gt;

* J (U+004A): L&lt;&lt;770.0,1010.0&gt;--&lt;443.0,1009.0&gt;&gt;

* Jcircumflex (U+0134): L&lt;&lt;443.0,1221.0&gt;--&lt;872.0,1219.0&gt;&gt;

* Jcircumflex (U+0134): L&lt;&lt;770.0,1010.0&gt;--&lt;443.0,1009.0&gt;&gt;

* L (U+004C): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* L (U+004C): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* Lacute (U+0139): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Lacute (U+0139): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* Lcaron (U+013D): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Lcaron (U+013D): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* Ldot (U+013F): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Ldot (U+013F): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* Lslash (U+0141): L&lt;&lt;489.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* Lslash (U+0141): L&lt;&lt;977.0,-34.0&gt;--&lt;401.0,-33.0&gt;&gt;

* OE (U+0152): L&lt;&lt;1058.0,1009.0&gt;--&lt;770.0,1011.0&gt;&gt;

* OE (U+0152): L&lt;&lt;1078.0,-34.0&gt;--&lt;668.0,-32.0&gt;&gt;

* OE (U+0152): L&lt;&lt;668.0,1219.0&gt;--&lt;1058.0,1221.0&gt;&gt;

* OE (U+0152): L&lt;&lt;770.0,176.0&gt;--&lt;1078.0,178.0&gt;&gt;

* Phi (U+03A6): L&lt;&lt;436.0,455.0&gt;--&lt;435.0,796.0&gt;&gt;

* Pi (U+03A0): L&lt;&lt;350.0,1112.0&gt;--&lt;353.0,127.0&gt;&gt;

* Pi (U+03A0): L&lt;&lt;720.0,127.0&gt;--&lt;723.0,1112.0&gt;&gt;

* Psi (U+03A8): L&lt;&lt;434.0,456.0&gt;--&lt;433.0,1123.0&gt;&gt;

* Psi (U+03A8): L&lt;&lt;644.0,1123.0&gt;--&lt;643.0,457.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;698.0,51.0&gt;--&lt;697.0,-89.0&gt;&gt;

* Tau (U+03A4): L&lt;&lt;433.0,129.0&gt;--&lt;434.0,1117.0&gt;&gt;

* Tau (U+03A4): L&lt;&lt;643.0,1117.0&gt;--&lt;644.0,129.0&gt;&gt;

* Thorn (U+00DE): L&lt;&lt;419.0,430.0&gt;--&lt;659.0,432.0&gt;&gt;

* Thorn (U+00DE): L&lt;&lt;419.0,978.0&gt;--&lt;680.0,980.0&gt;&gt;

* Thorn (U+00DE): L&lt;&lt;659.0,768.0&gt;--&lt;419.0,770.0&gt;&gt;

* Thorn (U+00DE): L&lt;&lt;680.0,220.0&gt;--&lt;419.0,222.0&gt;&gt;

* Y (U+0059): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* Y (U+0059): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* Yacute (U+00DD): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* Yacute (U+00DD): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* Ycircumflex (U+0176): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* Ycircumflex (U+0176): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* Ydieresis (U+0178): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* Ydieresis (U+0178): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* Ygrave (U+1EF2): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* Ygrave (U+1EF2): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* Z (U+005A): L&lt;&lt;256.0,1221.0&gt;--&lt;899.0,1220.0&gt;&gt;

* Z (U+005A): L&lt;&lt;452.0,177.0&gt;--&lt;996.0,178.0&gt;&gt;

* Z (U+005A): L&lt;&lt;757.0,1010.0&gt;--&lt;256.0,1009.0&gt;&gt;

* Z (U+005A): L&lt;&lt;996.0,-34.0&gt;--&lt;303.0,-33.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;256.0,1221.0&gt;--&lt;899.0,1220.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;452.0,177.0&gt;--&lt;996.0,178.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;757.0,1010.0&gt;--&lt;256.0,1009.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;996.0,-34.0&gt;--&lt;303.0,-33.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;256.0,1221.0&gt;--&lt;899.0,1220.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;452.0,177.0&gt;--&lt;996.0,178.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;757.0,1010.0&gt;--&lt;256.0,1009.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;996.0,-34.0&gt;--&lt;303.0,-33.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;256.0,1221.0&gt;--&lt;899.0,1220.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;452.0,177.0&gt;--&lt;996.0,178.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;757.0,1010.0&gt;--&lt;256.0,1009.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;996.0,-34.0&gt;--&lt;303.0,-33.0&gt;&gt;

* Zeta (U+0396): L&lt;&lt;252.0,1221.0&gt;--&lt;895.0,1220.0&gt;&gt;

* Zeta (U+0396): L&lt;&lt;448.0,177.0&gt;--&lt;992.0,178.0&gt;&gt;

* Zeta (U+0396): L&lt;&lt;753.0,1010.0&gt;--&lt;252.0,1009.0&gt;&gt;

* Zeta (U+0396): L&lt;&lt;992.0,-34.0&gt;--&lt;299.0,-33.0&gt;&gt;

* ae (U+00E6): L&lt;&lt;711.0,610.0&gt;--&lt;980.0,611.0&gt;&gt;

* aeacute (U+01FD): L&lt;&lt;711.0,610.0&gt;--&lt;980.0,611.0&gt;&gt;

* b (U+0062): L&lt;&lt;376.0,1257.0&gt;--&lt;375.0,788.0&gt;&gt;

* beta (U+03B2): L&lt;&lt;262.0,75.0&gt;--&lt;263.0,-425.0&gt;&gt;

* bracketleft (U+005B): L&lt;&lt;442.0,1403.0&gt;--&lt;807.0,1406.0&gt;&gt;

* bracketleft (U+005B): L&lt;&lt;514.0,-157.0&gt;--&lt;807.0,-155.0&gt;&gt;

* bracketleft (U+005B): L&lt;&lt;807.0,-367.0&gt;--&lt;442.0,-364.0&gt;&gt;

* bracketleft (U+005B): L&lt;&lt;807.0,1194.0&gt;--&lt;514.0,1196.0&gt;&gt;

* bracketright (U+005D): L&lt;&lt;421.0,-155.0&gt;--&lt;714.0,-157.0&gt;&gt;

* bracketright (U+005D): L&lt;&lt;421.0,1406.0&gt;--&lt;786.0,1403.0&gt;&gt;

* bracketright (U+005D): L&lt;&lt;714.0,1196.0&gt;--&lt;421.0,1194.0&gt;&gt;

* bracketright (U+005D): L&lt;&lt;786.0,-364.0&gt;--&lt;421.0,-367.0&gt;&gt;

* ccedilla (U+00E7): L&lt;&lt;718.0,51.0&gt;--&lt;717.0,-89.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;688.0,51.0&gt;--&lt;687.0,-89.0&gt;&gt;

* cedilla.case: L&lt;&lt;688.0,51.0&gt;--&lt;687.0,-89.0&gt;&gt;

* d (U+0064): L&lt;&lt;853.0,788.0&gt;--&lt;852.0,1257.0&gt;&gt;

* dcaron (U+010F): L&lt;&lt;751.0,797.0&gt;--&lt;750.0,1257.0&gt;&gt;

* dotlessi (U+0131): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* dotlessi (U+0131): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* e (U+0065): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* eacute (U+00E9): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* ebreve (U+0115): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* ecaron (U+011B): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* ecircumflex (U+00EA): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* edieresis (U+00EB): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* edotaccent (U+0117): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* egrave (U+00E8): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* emacron (U+0113): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* eogonek (U+0119): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* five (U+0035): L&lt;&lt;375.0,1220.0&gt;--&lt;885.0,1221.0&gt;&gt;

* five (U+0035): L&lt;&lt;885.0,1009.0&gt;--&lt;451.0,1010.0&gt;&gt;

* franc (U+20A3): L&lt;&lt;336.0,1220.0&gt;--&lt;977.0,1221.0&gt;&gt;

* franc (U+20A3): L&lt;&lt;429.0,737.0&gt;--&lt;862.0,738.0&gt;&gt;

* franc (U+20A3): L&lt;&lt;862.0,526.0&gt;--&lt;429.0,527.0&gt;&gt;

* franc (U+20A3): L&lt;&lt;977.0,1009.0&gt;--&lt;429.0,1010.0&gt;&gt;

* h (U+0068): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;

* hcircumflex (U+0125): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;

* i (U+0069): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* i (U+0069): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* iacute (U+00ED): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* iacute (U+00ED): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* ibreve (U+012D): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* ibreve (U+012D): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* icircumflex (U+00EE): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* icircumflex (U+00EE): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* idieresis (U+00EF): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* idieresis (U+00EF): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* idotaccent: L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* idotaccent: L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* igrave (U+00EC): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* igrave (U+00EC): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* imacron (U+012B): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* imacron (U+012B): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* iogonek (U+012F): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* iogonek (U+012F): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* itilde (U+0129): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* itilde (U+0129): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* j (U+006A): L&lt;&lt;330.0,958.0&gt;--&lt;804.0,956.0&gt;&gt;

* j (U+006A): L&lt;&lt;719.0,747.0&gt;--&lt;330.0,746.0&gt;&gt;

* jcircumflex (U+0135): L&lt;&lt;330.0,958.0&gt;--&lt;804.0,956.0&gt;&gt;

* jcircumflex (U+0135): L&lt;&lt;719.0,747.0&gt;--&lt;330.0,746.0&gt;&gt;

* kafDotless_ar.fina: L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* kafDotless_ar: L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* l (U+006C): L&lt;&lt;280.0,1346.0&gt;--&lt;627.0,1343.0&gt;&gt;

* l (U+006C): L&lt;&lt;519.0,1136.0&gt;--&lt;280.0,1134.0&gt;&gt;

* lacute (U+013A): L&lt;&lt;280.0,1346.0&gt;--&lt;627.0,1343.0&gt;&gt;

* lacute (U+013A): L&lt;&lt;519.0,1136.0&gt;--&lt;280.0,1134.0&gt;&gt;

* lcaron (U+013E): L&lt;&lt;250.0,1346.0&gt;--&lt;597.0,1343.0&gt;&gt;

* lcaron (U+013E): L&lt;&lt;489.0,1136.0&gt;--&lt;250.0,1134.0&gt;&gt;

* ldot (U+0140): L&lt;&lt;250.0,1346.0&gt;--&lt;597.0,1343.0&gt;&gt;

* ldot (U+0140): L&lt;&lt;489.0,1136.0&gt;--&lt;250.0,1134.0&gt;&gt;

* lira (U+20A4): L&lt;&lt;446.0,602.0&gt;--&lt;582.0,603.0&gt;&gt;

* lira (U+20A4): L&lt;&lt;582.0,650.0&gt;--&lt;413.0,651.0&gt;&gt;

* logicalnot (U+00AC): L&lt;&lt;914.0,674.0&gt;--&lt;203.0,671.0&gt;&gt;

* longs (U+017F): L&lt;&lt;552.0,979.0&gt;--&lt;551.0,133.0&gt;&gt;

* lslash (U+0142): L&lt;&lt;280.0,1346.0&gt;--&lt;627.0,1343.0&gt;&gt;

* lslash (U+0142): L&lt;&lt;519.0,1136.0&gt;--&lt;280.0,1134.0&gt;&gt;

* mu (U+00B5): L&lt;&lt;699.0,324.0&gt;--&lt;700.0,749.0&gt;&gt;

* musicalnote (U+266A): L&lt;&lt;740.0,624.0&gt;--&lt;741.0,266.0&gt;&gt;

* oe (U+0153): L&lt;&lt;711.0,610.0&gt;--&lt;980.0,611.0&gt;&gt;

* one (U+0031): L&lt;&lt;536.0,178.0&gt;--&lt;537.0,983.0&gt;&gt;

* onehalf (U+00BD): L&lt;&lt;360.0,1359.0&gt;--&lt;359.0,797.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;360.0,1359.0&gt;--&lt;359.0,797.0&gt;&gt;

* p (U+0070): L&lt;&lt;375.0,136.0&gt;--&lt;376.0,-333.0&gt;&gt;

* paragraph (U+00B6): L&lt;&lt;492.0,-345.0&gt;--&lt;493.0,493.0&gt;&gt;

* phi (U+03C6): L&lt;&lt;437.0,-425.0&gt;--&lt;436.0,-13.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;427.0,763.0&gt;--&lt;432.0,55.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;796.0,55.0&gt;--&lt;801.0,763.0&gt;&gt;

* prescription (U+211E): L&lt;&lt;351.0,551.0&gt;--&lt;353.0,129.0&gt;&gt;

* product (U+220F): L&lt;&lt;375.0,1027.0&gt;--&lt;379.0,55.0&gt;&gt;

* product (U+220F): L&lt;&lt;849.0,55.0&gt;--&lt;853.0,1027.0&gt;&gt;

* q (U+0071): L&lt;&lt;852.0,-333.0&gt;--&lt;853.0,136.0&gt;&gt;

* scedilla (U+015F): L&lt;&lt;708.0,51.0&gt;--&lt;707.0,-89.0&gt;&gt;

* seven (U+0037): L&lt;&lt;262.0,1221.0&gt;--&lt;917.0,1220.0&gt;&gt;

* seven (U+0037): L&lt;&lt;799.0,1010.0&gt;--&lt;262.0,1009.0&gt;&gt;

* sterling (U+00A3): L&lt;&lt;464.0,177.0&gt;--&lt;915.0,178.0&gt;&gt;

* theta (U+03B8): L&lt;&lt;245.0,784.0&gt;--&lt;826.0,782.0&gt;&gt;

* theta (U+03B8): L&lt;&lt;824.0,591.0&gt;--&lt;237.0,587.0&gt;&gt;

* thorn (U+00FE): L&lt;&lt;375.0,136.0&gt;--&lt;376.0,-333.0&gt;&gt;

* thorn (U+00FE): L&lt;&lt;376.0,1257.0&gt;--&lt;375.0,794.0&gt;&gt;

* trademark (U+2122): L&lt;&lt;1117.0,811.0&gt;--&lt;1115.0,1043.0&gt;&gt;

* trademark (U+2122): L&lt;&lt;218.0,813.0&gt;--&lt;220.0,1182.0&gt;&gt;

* trademark (U+2122): L&lt;&lt;408.0,1182.0&gt;--&lt;410.0,813.0&gt;&gt;

* trademark (U+2122): L&lt;&lt;820.0,1043.0&gt;--&lt;819.0,811.0&gt;&gt;

* two (U+0032): L&lt;&lt;521.0,177.0&gt;--&lt;954.0,178.0&gt;&gt;

* two (U+0032): L&lt;&lt;954.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* uni00B9 (U+00B9): L&lt;&lt;738.0,1292.0&gt;--&lt;737.0,617.0&gt;&gt;

* uni0122 (U+0122): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* uni0122 (U+0122): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* uni0122 (U+0122): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* uni013B (U+013B): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni013B (U+013B): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* uni013C (U+013C): L&lt;&lt;280.0,1346.0&gt;--&lt;627.0,1343.0&gt;&gt;

* uni013C (U+013C): L&lt;&lt;519.0,1136.0&gt;--&lt;280.0,1134.0&gt;&gt;

* uni0162 (U+0162): L&lt;&lt;705.0,51.0&gt;--&lt;704.0,-89.0&gt;&gt;

* uni0163 (U+0163): L&lt;&lt;728.0,51.0&gt;--&lt;727.0,-89.0&gt;&gt;

* uni01D0 (U+01D0): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* uni01D0 (U+01D0): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* uni01DD (U+01DD): L&lt;&lt;195.0,532.0&gt;--&lt;795.0,531.0&gt;&gt;

* uni01DD (U+01DD): L&lt;&lt;794.0,342.0&gt;--&lt;271.0,343.0&gt;&gt;

* uni01F0 (U+01F0): L&lt;&lt;330.0,958.0&gt;--&lt;804.0,956.0&gt;&gt;

* uni01F0 (U+01F0): L&lt;&lt;719.0,747.0&gt;--&lt;330.0,746.0&gt;&gt;

* uni01F4 (U+01F4): L&lt;&lt;1117.0,526.0&gt;--&lt;1115.0,131.0&gt;&gt;

* uni01F4 (U+01F4): L&lt;&lt;900.0,418.0&gt;--&lt;666.0,416.0&gt;&gt;

* uni01F4 (U+01F4): L&lt;&lt;901.0,204.0&gt;--&lt;900.0,418.0&gt;&gt;

* uni0204 (U+0204): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni0204 (U+0204): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni0204 (U+0204): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni0204 (U+0204): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni0204 (U+0204): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni0204 (U+0204): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni0205 (U+0205): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni0209 (U+0209): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* uni0209 (U+0209): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* uni0237 (U+0237): L&lt;&lt;330.0,958.0&gt;--&lt;804.0,956.0&gt;&gt;

* uni0237 (U+0237): L&lt;&lt;719.0,747.0&gt;--&lt;330.0,746.0&gt;&gt;

* uni0258 (U+0258): L&lt;&lt;271.0,546.0&gt;--&lt;794.0,547.0&gt;&gt;

* uni0258 (U+0258): L&lt;&lt;795.0,358.0&gt;--&lt;195.0,357.0&gt;&gt;

* uni0327 (U+0327): L&lt;&lt;688.0,51.0&gt;--&lt;687.0,-89.0&gt;&gt;

* uni034F (U+034F): L&lt;&lt;941.0,1217.0&gt;--&lt;940.0,1078.0&gt;&gt;

* uni03D8 (U+03D8): L&lt;&lt;435.0,140.0&gt;--&lt;438.0,490.0&gt;&gt;

* uni03D8 (U+03D8): L&lt;&lt;639.0,490.0&gt;--&lt;642.0,140.0&gt;&gt;

* uni03DA (U+03DB): L&lt;&lt;437.0,2.0&gt;--&lt;435.0,338.0&gt;&gt;

* uni03DD (U+03DD): L&lt;&lt;263.0,482.0&gt;--&lt;653.0,483.0&gt;&gt;

* uni0400 (U+0400): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni0400 (U+0400): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni0400 (U+0400): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni0400 (U+0400): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni0400 (U+0400): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni0400 (U+0400): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni0401 (U+0401): L&lt;&lt;415.0,163.0&gt;--&lt;937.0,167.0&gt;&gt;

* uni0401 (U+0401): L&lt;&lt;919.0,1019.0&gt;--&lt;414.0,1023.0&gt;&gt;

* uni0402 (U+0402): L&lt;&lt;550.0,1037.0&gt;--&lt;553.0,634.0&gt;&gt;

* uni0402 (U+0402): L&lt;&lt;553.0,390.0&gt;--&lt;551.0,147.0&gt;&gt;

* uni0403 (U+0403): L&lt;&lt;505.0,1035.0&gt;--&lt;508.0,143.0&gt;&gt;

* uni0408 (U+0408): L&lt;&lt;299.0,465.0&gt;--&lt;298.0,207.0&gt;&gt;

* uni0408 (U+0408): L&lt;&lt;710.0,363.0&gt;--&lt;714.0,1036.0&gt;&gt;

* uni0408 (U+0408): L&lt;&lt;927.0,1042.0&gt;--&lt;928.0,333.0&gt;&gt;

* uni0409 (U+0409): L&lt;&lt;496.0,1044.0&gt;--&lt;497.0,301.0&gt;&gt;

* uni0409 (U+0409): L&lt;&lt;589.0,138.0&gt;--&lt;590.0,1045.0&gt;&gt;

* uni0409 (U+0409): L&lt;&lt;806.0,1042.0&gt;--&lt;807.0,719.0&gt;&gt;

* uni040A (U+040A): L&lt;&lt;774.0,1042.0&gt;--&lt;775.0,719.0&gt;&gt;

* uni040B (U+040B): L&lt;&lt;1120.0,363.0&gt;--&lt;1119.0,144.0&gt;&gt;

* uni040B (U+040B): L&lt;&lt;550.0,1037.0&gt;--&lt;553.0,634.0&gt;&gt;

* uni040C (U+040C): L&lt;&lt;436.0,541.0&gt;--&lt;438.0,145.0&gt;&gt;

* uni040F (U+040F): L&lt;&lt;399.0,1048.0&gt;--&lt;395.0,152.0&gt;&gt;

* uni040F (U+040F): L&lt;&lt;833.0,152.0&gt;--&lt;829.0,1048.0&gt;&gt;

* uni0411 (U+0411): L&lt;&lt;899.0,1019.0&gt;--&lt;434.0,1023.0&gt;&gt;

* uni0412 (U+0412): L&lt;&lt;443.0,526.0&gt;--&lt;444.0,154.0&gt;&gt;

* uni0413 (U+0413): L&lt;&lt;505.0,1035.0&gt;--&lt;508.0,143.0&gt;&gt;

* uni0414 (U+0414): L&lt;&lt;513.0,1034.0&gt;--&lt;517.0,403.0&gt;&gt;

* uni0414 (U+0414): L&lt;&lt;813.0,152.0&gt;--&lt;811.0,1039.0&gt;&gt;

* uni0415 (U+0415): L&lt;&lt;415.0,163.0&gt;--&lt;937.0,167.0&gt;&gt;

* uni0415 (U+0415): L&lt;&lt;919.0,1019.0&gt;--&lt;414.0,1023.0&gt;&gt;

* uni041A (U+041A): L&lt;&lt;436.0,541.0&gt;--&lt;438.0,145.0&gt;&gt;

* uni041B (U+041B): L&lt;&lt;534.0,1036.0&gt;--&lt;537.0,301.0&gt;&gt;

* uni041B (U+041B): L&lt;&lt;829.0,139.0&gt;--&lt;831.0,1039.0&gt;&gt;

* uni041F (U+041F): L&lt;&lt;395.0,1035.0&gt;--&lt;399.0,139.0&gt;&gt;

* uni041F (U+041F): L&lt;&lt;829.0,139.0&gt;--&lt;833.0,1035.0&gt;&gt;

* uni0420 (U+0420): L&lt;&lt;482.0,412.0&gt;--&lt;481.0,157.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;1035.0,-33.0&gt;--&lt;143.0,-34.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;399.0,1048.0&gt;--&lt;395.0,152.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;813.0,152.0&gt;--&lt;809.0,1048.0&gt;&gt;

* uni0427 (U+0427): L&lt;&lt;181.0,724.0&gt;--&lt;182.0,1044.0&gt;&gt;

* uni0427 (U+0427): L&lt;&lt;398.0,1041.0&gt;--&lt;399.0,739.0&gt;&gt;

* uni0427 (U+0427): L&lt;&lt;829.0,698.0&gt;--&lt;830.0,1042.0&gt;&gt;

* uni0427 (U+0427): L&lt;&lt;830.0,144.0&gt;--&lt;829.0,465.0&gt;&gt;

* uni0428 (U+0428): L&lt;&lt;309.0,1049.0&gt;--&lt;308.0,145.0&gt;&gt;

* uni0428 (U+0428): L&lt;&lt;506.0,145.0&gt;--&lt;505.0,1050.0&gt;&gt;

* uni0428 (U+0428): L&lt;&lt;723.0,1050.0&gt;--&lt;722.0,145.0&gt;&gt;

* uni0428 (U+0428): L&lt;&lt;920.0,145.0&gt;--&lt;919.0,1049.0&gt;&gt;

* uni0429 (U+0429): L&lt;&lt;1066.0,-33.0&gt;--&lt;73.0,-34.0&gt;&gt;

* uni0429 (U+0429): L&lt;&lt;309.0,1049.0&gt;--&lt;308.0,145.0&gt;&gt;

* uni0429 (U+0429): L&lt;&lt;506.0,145.0&gt;--&lt;505.0,1050.0&gt;&gt;

* uni0429 (U+0429): L&lt;&lt;723.0,1050.0&gt;--&lt;722.0,145.0&gt;&gt;

* uni0429 (U+0429): L&lt;&lt;920.0,145.0&gt;--&lt;919.0,1049.0&gt;&gt;

* uni042A (U+042A): L&lt;&lt;555.0,1036.0&gt;--&lt;553.0,733.0&gt;&gt;

* uni042B (U+042B): L&lt;&lt;352.0,1040.0&gt;--&lt;353.0,722.0&gt;&gt;

* uni042E (U+042E): L&lt;&lt;323.0,1045.0&gt;--&lt;322.0,691.0&gt;&gt;

* uni042F (U+042F): L&lt;&lt;781.0,147.0&gt;--&lt;779.0,510.0&gt;&gt;

* uni0433 (U+0433): L&lt;&lt;515.0,769.0&gt;--&lt;519.0,146.0&gt;&gt;

* uni0434 (U+0434): L&lt;&lt;270.0,346.0&gt;--&lt;271.0,782.0&gt;&gt;

* uni0434 (U+0434): L&lt;&lt;810.0,156.0&gt;--&lt;809.0,771.0&gt;&gt;

* uni0435 (U+0435): L&lt;&lt;1028.0,391.0&gt;--&lt;313.0,392.0&gt;&gt;

* uni0436 (U+0436): L&lt;&lt;505.0,591.0&gt;--&lt;506.0,782.0&gt;&gt;

* uni0436 (U+0436): L&lt;&lt;722.0,782.0&gt;--&lt;723.0,591.0&gt;&gt;

* uni043A (U+043A): L&lt;&lt;228.0,142.0&gt;--&lt;229.0,781.0&gt;&gt;

* uni043A (U+043A): L&lt;&lt;443.0,395.0&gt;--&lt;445.0,144.0&gt;&gt;

* uni043A (U+043A): L&lt;&lt;445.0,779.0&gt;--&lt;446.0,580.0&gt;&gt;

* uni043B (U+043B): L&lt;&lt;820.0,141.0&gt;--&lt;825.0,771.0&gt;&gt;

* uni0440 (U+0440): L&lt;&lt;385.0,128.0&gt;--&lt;382.0,-242.0&gt;&gt;

* uni0442 (U+0442): L&lt;&lt;506.0,144.0&gt;--&lt;508.0,775.0&gt;&gt;

* uni0442 (U+0442): L&lt;&lt;720.0,775.0&gt;--&lt;722.0,144.0&gt;&gt;

* uni0446 (U+0446): L&lt;&lt;978.0,-33.0&gt;--&lt;130.0,-34.0&gt;&gt;

* uni0447 (U+0447): L&lt;&lt;822.0,508.0&gt;--&lt;823.0,779.0&gt;&gt;

* uni0448 (U+0448): L&lt;&lt;303.0,754.0&gt;--&lt;300.0,149.0&gt;&gt;

* uni0448 (U+0448): L&lt;&lt;513.0,149.0&gt;--&lt;510.0,786.0&gt;&gt;

* uni0448 (U+0448): L&lt;&lt;728.0,754.0&gt;--&lt;725.0,149.0&gt;&gt;

* uni0448 (U+0448): L&lt;&lt;928.0,149.0&gt;--&lt;925.0,754.0&gt;&gt;

* uni0449 (U+0449): L&lt;&lt;303.0,754.0&gt;--&lt;300.0,149.0&gt;&gt;

* uni0449 (U+0449): L&lt;&lt;513.0,149.0&gt;--&lt;510.0,786.0&gt;&gt;

* uni0449 (U+0449): L&lt;&lt;728.0,754.0&gt;--&lt;725.0,149.0&gt;&gt;

* uni0449 (U+0449): L&lt;&lt;928.0,149.0&gt;--&lt;925.0,754.0&gt;&gt;

* uni044A (U+044A): L&lt;&lt;348.0,141.0&gt;--&lt;349.0,782.0&gt;&gt;

* uni044E (U+044E): L&lt;&lt;324.0,376.0&gt;--&lt;325.0,143.0&gt;&gt;

* uni044E (U+044E): L&lt;&lt;326.0,783.0&gt;--&lt;324.0,537.0&gt;&gt;

* uni0450 (U+0450): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni0451 (U+0451): L&lt;&lt;1028.0,391.0&gt;--&lt;313.0,392.0&gt;&gt;

* uni0453 (U+0453): L&lt;&lt;515.0,769.0&gt;--&lt;519.0,146.0&gt;&gt;

* uni0456 (U+0456): L&lt;&lt;532.0,151.0&gt;--&lt;531.0,776.0&gt;&gt;

* uni0456 (U+0456): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,150.0&gt;&gt;

* uni0457 (U+0457): L&lt;&lt;532.0,151.0&gt;--&lt;531.0,776.0&gt;&gt;

* uni0457 (U+0457): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,150.0&gt;&gt;

* uni0458 (U+0458): L&lt;&lt;719.0,-49.0&gt;--&lt;723.0,773.0&gt;&gt;

* uni0459 (U+0459): L&lt;&lt;477.0,777.0&gt;--&lt;479.0,271.0&gt;&gt;

* uni0459 (U+0459): L&lt;&lt;595.0,139.0&gt;--&lt;596.0,779.0&gt;&gt;

* uni0459 (U+0459): L&lt;&lt;812.0,781.0&gt;--&lt;810.0,539.0&gt;&gt;

* uni045A (U+045A): L&lt;&lt;792.0,781.0&gt;--&lt;790.0,539.0&gt;&gt;

* uni045B (U+045B): L&lt;&lt;1048.0,560.0&gt;--&lt;1047.0,142.0&gt;&gt;

* uni045B (U+045B): L&lt;&lt;831.0,143.0&gt;--&lt;830.0,545.0&gt;&gt;

* uni045C (U+045C): L&lt;&lt;228.0,142.0&gt;--&lt;229.0,781.0&gt;&gt;

* uni045C (U+045C): L&lt;&lt;443.0,395.0&gt;--&lt;445.0,144.0&gt;&gt;

* uni045C (U+045C): L&lt;&lt;445.0,779.0&gt;--&lt;446.0,580.0&gt;&gt;

* uni0461 (U+0461): L&lt;&lt;431.0,231.0&gt;--&lt;432.0,412.0&gt;&gt;

* uni0461 (U+0461): L&lt;&lt;641.0,413.0&gt;--&lt;642.0,231.0&gt;&gt;

* uni0462 (U+0462): L&lt;&lt;448.0,1241.0&gt;--&lt;793.0,1242.0&gt;&gt;

* uni0462 (U+0462): L&lt;&lt;467.0,1060.0&gt;--&lt;468.0,732.0&gt;&gt;

* uni0463 (U+0463): L&lt;&lt;189.0,132.0&gt;--&lt;190.0,750.0&gt;&gt;

* uni0463 (U+0463): L&lt;&lt;190.0,889.0&gt;--&lt;189.0,1292.0&gt;&gt;

* uni0464 (U+0464): L&lt;&lt;262.0,550.0&gt;--&lt;265.0,158.0&gt;&gt;

* uni0464 (U+0464): L&lt;&lt;262.0,701.0&gt;--&lt;383.0,702.0&gt;&gt;

* uni0464 (U+0464): L&lt;&lt;265.0,1092.0&gt;--&lt;262.0,701.0&gt;&gt;

* uni0464 (U+0464): L&lt;&lt;383.0,549.0&gt;--&lt;262.0,550.0&gt;&gt;

* uni0465 (U+0465): L&lt;&lt;319.0,412.0&gt;--&lt;320.0,134.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;437.0,156.0&gt;--&lt;438.0,418.0&gt;&gt;

* uni0466 (U+0466): L&lt;&lt;637.0,418.0&gt;--&lt;638.0,156.0&gt;&gt;

* uni0468 (U+0468): L&lt;&lt;257.0,1095.0&gt;--&lt;254.0,568.0&gt;&gt;

* uni046A (U+046A): L&lt;&lt;443.0,131.0&gt;--&lt;444.0,578.0&gt;&gt;

* uni046B (U+046B): L&lt;&lt;626.0,409.0&gt;--&lt;628.0,158.0&gt;&gt;

* uni046D (U+046D): L&lt;&lt;758.0,403.0&gt;--&lt;759.0,133.0&gt;&gt;

* uni0470 (U+0470): L&lt;&lt;432.0,460.0&gt;--&lt;431.0,1120.0&gt;&gt;

* uni0470 (U+0470): L&lt;&lt;434.0,140.0&gt;--&lt;433.0,306.0&gt;&gt;

* uni0470 (U+0470): L&lt;&lt;642.0,1120.0&gt;--&lt;640.0,463.0&gt;&gt;

* uni0471 (U+0471): L&lt;&lt;434.0,126.0&gt;--&lt;433.0,1119.0&gt;&gt;

* uni0471 (U+0471): L&lt;&lt;639.0,-26.0&gt;--&lt;640.0,-312.0&gt;&gt;

* uni0472 (U+0472): L&lt;&lt;263.0,747.0&gt;--&lt;800.0,743.0&gt;&gt;

* uni0472 (U+0472): L&lt;&lt;809.0,554.0&gt;--&lt;270.0,556.0&gt;&gt;

* uni0473 (U+0473): L&lt;&lt;821.0,393.0&gt;--&lt;249.0,391.0&gt;&gt;

* uni047D (U+047D): L&lt;&lt;431.0,231.0&gt;--&lt;432.0,412.0&gt;&gt;

* uni047D (U+047D): L&lt;&lt;641.0,413.0&gt;--&lt;642.0,231.0&gt;&gt;

* uni047E (U+047E): L&lt;&lt;464.0,1522.0&gt;--&lt;334.0,1521.0&gt;&gt;

* uni047F (U+047F): L&lt;&lt;431.0,231.0&gt;--&lt;432.0,412.0&gt;&gt;

* uni047F (U+047F): L&lt;&lt;641.0,413.0&gt;--&lt;642.0,231.0&gt;&gt;

* uni047F (U+047F): L&lt;&lt;740.0,1154.0&gt;--&lt;613.0,1155.0&gt;&gt;

* uni048B (U+048B): L&lt;&lt;359.0,749.0&gt;--&lt;360.0,339.0&gt;&gt;

* uni048B (U+048B): L&lt;&lt;712.0,134.0&gt;--&lt;711.0,547.0&gt;&gt;

* uni048C (U+048C): L&lt;&lt;263.0,129.0&gt;--&lt;264.0,931.0&gt;&gt;

* uni048D (U+048D): L&lt;&lt;189.0,133.0&gt;--&lt;190.0,750.0&gt;&gt;

* uni048D (U+048D): L&lt;&lt;191.0,891.0&gt;--&lt;192.0,1168.0&gt;&gt;

* uni0490 (U+0490): L&lt;&lt;143.0,1221.0&gt;--&lt;951.0,1220.0&gt;&gt;

* uni0490 (U+0490): L&lt;&lt;504.0,1033.0&gt;--&lt;508.0,143.0&gt;&gt;

* uni0491 (U+0491): L&lt;&lt;190.0,958.0&gt;--&lt;918.0,956.0&gt;&gt;

* uni0492 (U+0492): L&lt;&lt;293.0,661.0&gt;--&lt;294.0,1037.0&gt;&gt;

* uni0492 (U+0492): L&lt;&lt;294.0,151.0&gt;--&lt;293.0,502.0&gt;&gt;

* uni0492 (U+0492): L&lt;&lt;942.0,1022.0&gt;--&lt;497.0,1025.0&gt;&gt;

* uni0493 (U+0493): L&lt;&lt;337.0,536.0&gt;--&lt;338.0,771.0&gt;&gt;

* uni0493 (U+0493): L&lt;&lt;338.0,154.0&gt;--&lt;337.0,369.0&gt;&gt;

* uni0493 (U+0493): L&lt;&lt;544.0,365.0&gt;--&lt;543.0,158.0&gt;&gt;

* uni0493 (U+0493): L&lt;&lt;942.0,758.0&gt;--&lt;535.0,759.0&gt;&gt;

* uni0495 (U+0495): L&lt;&lt;461.0,416.0&gt;--&lt;460.0,139.0&gt;&gt;

* uni0496 (U+0496): L&lt;&lt;924.0,-268.0&gt;--&lt;925.0,-7.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;444.0,137.0&gt;--&lt;443.0,266.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;627.0,749.0&gt;--&lt;628.0,593.0&gt;&gt;

* uni0497 (U+0497): L&lt;&lt;628.0,267.0&gt;--&lt;627.0,136.0&gt;&gt;

* uni049A (U+049A): L&lt;&lt;436.0,541.0&gt;--&lt;438.0,145.0&gt;&gt;

* uni049B (U+049B): L&lt;&lt;228.0,142.0&gt;--&lt;229.0,781.0&gt;&gt;

* uni049B (U+049B): L&lt;&lt;443.0,395.0&gt;--&lt;445.0,144.0&gt;&gt;

* uni049B (U+049B): L&lt;&lt;445.0,779.0&gt;--&lt;446.0,580.0&gt;&gt;

* uni049C (U+049C): L&lt;&lt;306.0,1120.0&gt;--&lt;305.0,816.0&gt;&gt;

* uni049D (U+049D): L&lt;&lt;323.0,464.0&gt;--&lt;324.0,134.0&gt;&gt;

* uni049E (U+049E): L&lt;&lt;330.0,933.0&gt;--&lt;331.0,678.0&gt;&gt;

* uni049E (U+049E): L&lt;&lt;331.0,360.0&gt;--&lt;330.0,135.0&gt;&gt;

* uni049F (U+049F): L&lt;&lt;356.0,273.0&gt;--&lt;355.0,144.0&gt;&gt;

* uni04A1 (U+04A1): L&lt;&lt;310.0,130.0&gt;--&lt;311.0,748.0&gt;&gt;

* uni04A3 (U+04A3): L&lt;&lt;1058.0,783.0&gt;--&lt;1057.0,142.0&gt;&gt;

* uni04A5 (U+04A5): L&lt;&lt;762.0,748.0&gt;--&lt;763.0,131.0&gt;&gt;

* uni04A6 (U+04A6): L&lt;&lt;264.0,1115.0&gt;--&lt;265.0,160.0&gt;&gt;

* uni04A6 (U+04A6): L&lt;&lt;468.0,160.0&gt;--&lt;469.0,1115.0&gt;&gt;

* uni04A7 (U+04A7): L&lt;&lt;290.0,741.0&gt;--&lt;294.0,130.0&gt;&gt;

* uni04A7 (U+04A7): L&lt;&lt;541.0,130.0&gt;--&lt;545.0,741.0&gt;&gt;

* uni04A7 (U+04A7): L&lt;&lt;722.0,745.0&gt;--&lt;723.0,556.0&gt;&gt;

* uni04A7 (U+04A7): L&lt;&lt;724.0,390.0&gt;--&lt;723.0,134.0&gt;&gt;

* uni04AC (U+04AC): L&lt;&lt;431.0,131.0&gt;--&lt;432.0,1115.0&gt;&gt;

* uni04AC (U+04AC): L&lt;&lt;641.0,1115.0&gt;--&lt;642.0,131.0&gt;&gt;

* uni04AD (U+04AD): L&lt;&lt;433.0,137.0&gt;--&lt;434.0,743.0&gt;&gt;

* uni04AD (U+04AD): L&lt;&lt;639.0,743.0&gt;--&lt;640.0,138.0&gt;&gt;

* uni04AD (U+04AD): L&lt;&lt;753.0,-32.0&gt;--&lt;262.0,-34.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;421.0,977.0&gt;--&lt;418.0,140.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;776.0,140.0&gt;--&lt;773.0,1091.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;932.0,-32.0&gt;--&lt;223.0,-34.0&gt;&gt;

* uni04B5 (U+04B5): L&lt;&lt;943.0,-33.0&gt;--&lt;180.0,-34.0&gt;&gt;

* uni04B6 (U+04B6): L&lt;&lt;132.0,844.0&gt;--&lt;133.0,1118.0&gt;&gt;

* uni04B6 (U+04B6): L&lt;&lt;342.0,1117.0&gt;--&lt;343.0,834.0&gt;&gt;

* uni04B8 (U+04B8): L&lt;&lt;132.0,844.0&gt;--&lt;133.0,1118.0&gt;&gt;

* uni04B8 (U+04B8): L&lt;&lt;342.0,1117.0&gt;--&lt;343.0,846.0&gt;&gt;

* uni04B8 (U+04B8): L&lt;&lt;728.0,132.0&gt;--&lt;731.0,482.0&gt;&gt;

* uni04B8 (U+04B8): L&lt;&lt;730.0,631.0&gt;--&lt;728.0,1121.0&gt;&gt;

* uni04B9 (U+04B9): L&lt;&lt;715.0,482.0&gt;--&lt;713.0,745.0&gt;&gt;

* uni04BA (U+04BA): L&lt;&lt;1047.0,463.0&gt;--&lt;1046.0,143.0&gt;&gt;

* uni04BA (U+04BA): L&lt;&lt;398.0,1043.0&gt;--&lt;399.0,723.0&gt;&gt;

* uni04BA (U+04BA): L&lt;&lt;399.0,489.0&gt;--&lt;398.0,145.0&gt;&gt;

* uni04BA (U+04BA): L&lt;&lt;830.0,146.0&gt;--&lt;829.0,448.0&gt;&gt;

* uni04BB (U+04BB): L&lt;&lt;416.0,422.0&gt;--&lt;414.0,146.0&gt;&gt;

* uni04BB (U+04BB): L&lt;&lt;831.0,143.0&gt;--&lt;830.0,605.0&gt;&gt;

* uni04BC (U+04BC): L&lt;&lt;420.0,749.0&gt;--&lt;891.0,745.0&gt;&gt;

* uni04BC (U+04BC): L&lt;&lt;979.0,558.0&gt;--&lt;413.0,560.0&gt;&gt;

* uni04BD (U+04BD): L&lt;&lt;449.0,547.0&gt;--&lt;812.0,546.0&gt;&gt;

* uni04BD (U+04BD): L&lt;&lt;897.0,357.0&gt;--&lt;445.0,360.0&gt;&gt;

* uni04BE (U+04BE): L&lt;&lt;419.0,749.0&gt;--&lt;891.0,745.0&gt;&gt;

* uni04BE (U+04BE): L&lt;&lt;979.0,558.0&gt;--&lt;415.0,560.0&gt;&gt;

* uni04BF (U+04BF): L&lt;&lt;449.0,547.0&gt;--&lt;812.0,546.0&gt;&gt;

* uni04BF (U+04BF): L&lt;&lt;897.0,357.0&gt;--&lt;445.0,360.0&gt;&gt;

* uni04C2 (U+04C2): L&lt;&lt;505.0,591.0&gt;--&lt;506.0,782.0&gt;&gt;

* uni04C2 (U+04C2): L&lt;&lt;722.0,782.0&gt;--&lt;723.0,591.0&gt;&gt;

* uni04C3 (U+04C3): L&lt;&lt;329.0,576.0&gt;--&lt;331.0,131.0&gt;&gt;

* uni04C5 (U+04C5): L&lt;&lt;306.0,893.0&gt;--&lt;307.0,1116.0&gt;&gt;

* uni04C5 (U+04C5): L&lt;&lt;730.0,129.0&gt;--&lt;732.0,1114.0&gt;&gt;

* uni04C6 (U+04C6): L&lt;&lt;714.0,132.0&gt;--&lt;717.0,742.0&gt;&gt;

* uni04CB (U+04CB): L&lt;&lt;132.0,844.0&gt;--&lt;133.0,1118.0&gt;&gt;

* uni04CB (U+04CB): L&lt;&lt;342.0,1117.0&gt;--&lt;343.0,834.0&gt;&gt;

* uni04CE (U+04CE): L&lt;&lt;312.0,730.0&gt;--&lt;317.0,131.0&gt;&gt;

* uni04D4 (U+04D4): L&lt;&lt;507.0,510.0&gt;--&lt;505.0,1120.0&gt;&gt;

* uni04D5 (U+04D5): L&lt;&lt;617.0,546.0&gt;--&lt;897.0,545.0&gt;&gt;

* uni04D6 (U+04D6): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni04D6 (U+04D6): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni04D6 (U+04D6): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni04D6 (U+04D6): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni04D6 (U+04D6): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni04D6 (U+04D6): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni04D7 (U+04D7): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni04DA (U+04DA): L&lt;&lt;100.0,693.0&gt;--&lt;873.0,691.0&gt;&gt;

* uni04DA (U+04DA): L&lt;&lt;871.0,499.0&gt;--&lt;182.0,502.0&gt;&gt;

* uni04DD (U+04DD): L&lt;&lt;505.0,591.0&gt;--&lt;506.0,782.0&gt;&gt;

* uni04DD (U+04DD): L&lt;&lt;722.0,782.0&gt;--&lt;723.0,591.0&gt;&gt;

* uni04E0 (U+04E0): L&lt;&lt;773.0,1105.0&gt;--&lt;234.0,1103.0&gt;&gt;

* uni04EA (U+04EA): L&lt;&lt;263.0,747.0&gt;--&lt;800.0,743.0&gt;&gt;

* uni04EA (U+04EA): L&lt;&lt;809.0,554.0&gt;--&lt;270.0,556.0&gt;&gt;

* uni04ED (U+04ED): L&lt;&lt;766.0,393.0&gt;--&lt;406.0,390.0&gt;&gt;

* uni04F4 (U+04F4): L&lt;&lt;181.0,724.0&gt;--&lt;182.0,1044.0&gt;&gt;

* uni04F4 (U+04F4): L&lt;&lt;398.0,1041.0&gt;--&lt;399.0,739.0&gt;&gt;

* uni04F4 (U+04F4): L&lt;&lt;829.0,698.0&gt;--&lt;830.0,1042.0&gt;&gt;

* uni04F4 (U+04F4): L&lt;&lt;830.0,144.0&gt;--&lt;829.0,465.0&gt;&gt;

* uni04F5 (U+04F5): L&lt;&lt;822.0,508.0&gt;--&lt;823.0,779.0&gt;&gt;

* uni04F6 (U+04F6): L&lt;&lt;459.0,1111.0&gt;--&lt;461.0,133.0&gt;&gt;

* uni04F7 (U+04F7): L&lt;&lt;457.0,738.0&gt;--&lt;460.0,138.0&gt;&gt;

* uni04F7 (U+04F7): L&lt;&lt;571.0,-31.0&gt;--&lt;160.0,-34.0&gt;&gt;

* uni04F8 (U+04F8): L&lt;&lt;352.0,1040.0&gt;--&lt;353.0,722.0&gt;&gt;

* uni0512 (U+0512): L&lt;&lt;306.0,893.0&gt;--&lt;307.0,1115.0&gt;&gt;

* uni0512 (U+0512): L&lt;&lt;730.0,-76.0&gt;--&lt;731.0,1116.0&gt;&gt;

* uni0513 (U+0513): L&lt;&lt;714.0,-106.0&gt;--&lt;716.0,746.0&gt;&gt;

* uni0604 (U+0604): L&lt;&lt;43.0,407.0&gt;--&lt;209.0,406.0&gt;&gt;

* uni0611 (U+0611): L&lt;&lt;748.0,1070.0&gt;--&lt;420.0,1072.0&gt;&gt;

* uni0612 (U+0612): L&lt;&lt;655.0,1436.0&gt;--&lt;533.0,1437.0&gt;&gt;

* uni0615 (U+0615): L&lt;&lt;538.0,1620.0&gt;--&lt;537.0,1269.0&gt;&gt;

* uni0620.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni0620.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0620.init: L&lt;&lt;355.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0620.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0620.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;840.0,191.0&gt;&gt;

* uni0620.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0620.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0622.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0623.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0625.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0627.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0627.fina.short: L&lt;&lt;1088.0,193.0&gt;--&lt;719.0,191.0&gt;&gt;

* uni0627.fina.short: L&lt;&lt;719.0,403.0&gt;--&lt;1088.0,401.0&gt;&gt;

* uni0627.fina.shorter: L&lt;&lt;1088.0,193.0&gt;--&lt;719.0,191.0&gt;&gt;

* uni0627.fina.shorter: L&lt;&lt;719.0,403.0&gt;--&lt;1088.0,401.0&gt;&gt;

* uni0628 (U+FE8F): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni062A (U+FE95): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni062B (U+FE99): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni063B.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni063B.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni063C.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni063C.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni063D.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni063D.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni063D.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni063D.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni063D.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni063D.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni063D.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni063E.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni063E.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni063E.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni063E.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni063E.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni063E.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni063E.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni063F.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni063F.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni063F.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni063F.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni063F.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni063F.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni063F.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0641 (U+FED1): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni0643 (U+FED9): L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni0644.medi.short: L&lt;&lt;332.0,191.0&gt;--&lt;-14.0,194.0&gt;&gt;

* uni0645 (U+FEE1): L&lt;&lt;260.0,216.0&gt;--&lt;261.0,-469.0&gt;&gt;

* uni0669 (U+06F9): L&lt;&lt;616.0,785.0&gt;--&lt;615.0,1012.0&gt;&gt;

* uni066E (U+066E): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni066E.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni066E.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni066E.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni066E.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni066E.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni066E.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni066E.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni066F.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni066F.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni066F.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni0671.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0672.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0672.fina: L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uni0672.fina: L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uni0673.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0673.fina: L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uni0673.fina: L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uni0678.init: L&lt;&lt;442.0,191.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni0679 (U+FB66): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0679 (U+FB66): L&lt;&lt;565.0,1716.0&gt;--&lt;564.0,1365.0&gt;&gt;

* uni067A (U+FB5E): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067B (U+FB52): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067C (U+067C): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067C.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067C.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni067C.init: L&lt;&lt;384.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni067C.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni067C.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;797.0,191.0&gt;&gt;

* uni067C.medi: L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni067C.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni067D (U+067D): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067D.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067D.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni067D.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni067D.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni067D.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni067D.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni067D.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni067E (U+FB56): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni067F (U+FB62): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0680 (U+FB5A): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0681.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni0681.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni0682.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni0682.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni0685.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni0685.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni0688 (U+FB88): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;

* uni068B (U+068B): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;

* uni068B.fina: L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;

* uni0691 (U+FB8C): L&lt;&lt;538.0,1602.0&gt;--&lt;537.0,1251.0&gt;&gt;

* uni0692.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0692.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0693.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0693.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0694.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0694.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0695.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0695.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0696.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0696.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0697.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0697.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0699.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0699.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni069D.fina: L&lt;&lt;1229.0,191.0&gt;--&lt;193.0,192.0&gt;&gt;

* uni069D.medi: L&lt;&lt;1229.0,192.0&gt;--&lt;620.0,191.0&gt;&gt;

* uni069D.medi: L&lt;&lt;1230.0,397.0&gt;--&lt;1229.0,192.0&gt;&gt;

* uni069E.fina: L&lt;&lt;1229.0,191.0&gt;--&lt;193.0,192.0&gt;&gt;

* uni069E.medi: L&lt;&lt;1229.0,192.0&gt;--&lt;620.0,191.0&gt;&gt;

* uni069E.medi: L&lt;&lt;1230.0,397.0&gt;--&lt;1229.0,192.0&gt;&gt;

* uni069F.init: L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uni069F.init: L&lt;&lt;406.0,191.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni069F.medi: L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uni06A0.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni06A0.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni06A0.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni06A0.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni06A1 (U+06A1): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni06A1.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni06A1.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni06A1.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06A2 (U+06A2): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni06A2.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni06A2.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni06A2.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06A3 (U+06A3): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni06A3.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni06A3.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni06A3.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06A4 (U+FB6A): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni06A5 (U+06A5): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni06A5.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni06A5.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni06A5.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06A6 (U+FB6E): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni06A7.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni06A7.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni06A7.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06A8.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni06A8.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni06A8.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06AA.fina: L&lt;&lt;1238.0,193.0&gt;--&lt;796.0,192.0&gt;&gt;

* uni06AA.init: L&lt;&lt;-6.0,402.0&gt;--&lt;760.0,403.0&gt;&gt;

* uni06AA.init: L&lt;&lt;760.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06AA.medi: L&lt;&lt;-6.0,402.0&gt;--&lt;760.0,403.0&gt;&gt;

* uni06AA.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;796.0,192.0&gt;&gt;

* uni06AA.medi: L&lt;&lt;760.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06AB.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni06AB.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni06AC (U+06AC): L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni06AC.fina: L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni06AC.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni06AC.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni06AD (U+FBD3): L&lt;&lt;854.0,793.0&gt;--&lt;851.0,1418.0&gt;&gt;

* uni06AD (U+FBD3): L&lt;&lt;856.0,386.0&gt;--&lt;854.0,663.0&gt;&gt;

* uni06AE (U+06AE): L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni06AE.fina: L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni06AE.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni06AE.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni06B0.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni06B0.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni06B2.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni06B2.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni06B4.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni06B4.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni06B5.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni06B5.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06B5.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni06B5.medi: L&lt;&lt;332.0,191.0&gt;--&lt;-14.0,194.0&gt;&gt;

* uni06B5.medi: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni06B6.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni06B6.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06B6.medi: L&lt;&lt;-13.0,400.0&gt;--&lt;342.0,403.0&gt;&gt;

* uni06B6.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;799.0,191.0&gt;&gt;

* uni06B6.medi: L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,194.0&gt;&gt;

* uni06B6.medi: L&lt;&lt;799.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni06B7.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni06B7.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06B7.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni06B7.medi: L&lt;&lt;332.0,191.0&gt;--&lt;-14.0,194.0&gt;&gt;

* uni06B7.medi: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni06B8.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni06B8.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06B8.medi: L&lt;&lt;-13.0,400.0&gt;--&lt;342.0,403.0&gt;&gt;

* uni06B8.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;799.0,191.0&gt;&gt;

* uni06B8.medi: L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,194.0&gt;&gt;

* uni06B8.medi: L&lt;&lt;799.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni06B9.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni06B9.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06B9.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni06B9.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni06B9.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni06B9.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni06BA.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni06BA.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06BA.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni06BA.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni06BA.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni06BA.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni06BB (U+FBA0): L&lt;&lt;538.0,1569.0&gt;--&lt;537.0,1218.0&gt;&gt;

* uni06BC.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni06BC.init: L&lt;&lt;384.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06BC.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni06BC.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;797.0,191.0&gt;&gt;

* uni06BC.medi: L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni06BC.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni06BD.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni06BD.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06BD.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni06BD.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni06BD.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni06BD.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni06BF.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni06BF.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni06CD.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni06CE.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni06CE.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni06CE.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06CE.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni06CE.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni06CE.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni06CE.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni06D1.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni06D1.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni06D1.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni06D1.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni06D1.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni06D1.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni06D1.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni06E2 (U+06E2): L&lt;&lt;362.0,1521.0&gt;--&lt;364.0,1100.0&gt;&gt;

* uni06E9 (U+06E9): L&lt;&lt;322.0,-114.0&gt;--&lt;321.0,356.0&gt;&gt;

* uni06E9 (U+06E9): L&lt;&lt;449.0,370.0&gt;--&lt;448.0,-196.0&gt;&gt;

* uni06E9 (U+06E9): L&lt;&lt;625.0,-196.0&gt;--&lt;624.0,396.0&gt;&gt;

* uni06E9 (U+06E9): L&lt;&lt;752.0,356.0&gt;--&lt;751.0,-114.0&gt;&gt;

* uni06ED (U+06ED): L&lt;&lt;362.0,-550.0&gt;--&lt;364.0,-971.0&gt;&gt;

* uni06EF.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni06EF.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni06FB.fina: L&lt;&lt;1229.0,191.0&gt;--&lt;193.0,192.0&gt;&gt;

* uni06FB.medi: L&lt;&lt;1229.0,192.0&gt;--&lt;620.0,191.0&gt;&gt;

* uni06FB.medi: L&lt;&lt;1230.0,397.0&gt;--&lt;1229.0,192.0&gt;&gt;

* uni06FC.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni06FC.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni06FC.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni06FC.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni06FE (U+06FE): L&lt;&lt;260.0,441.0&gt;--&lt;261.0,-244.0&gt;&gt;

* uni06FE.init: L&lt;&lt;431.0,192.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni06FE.medi: L&lt;&lt;243.0,194.0&gt;--&lt;-17.0,195.0&gt;&gt;

* uni06FF.fina: L&lt;&lt;1241.0,194.0&gt;--&lt;887.0,191.0&gt;&gt;

* uni06FF.fina: L&lt;&lt;887.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni06FF.medi: L&lt;&lt;1237.0,402.0&gt;--&lt;1238.0,192.0&gt;&gt;

* uni06FF.medi: L&lt;&lt;1238.0,192.0&gt;--&lt;795.0,191.0&gt;&gt;

* uni06FF.medi: L&lt;&lt;720.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uni0750 (U+0750): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0750.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0750.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0750.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0750.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0750.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0750.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0750.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0751 (U+0751): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0751.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0751.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0751.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0751.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0751.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0751.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0751.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0752 (U+0752): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0752.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0752.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0752.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0752.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0752.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0752.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0752.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0753 (U+0753): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0753.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0753.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0753.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0753.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0753.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0753.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0753.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0754 (U+0754): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0754.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0754.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0754.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0754.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0754.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0754.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0754.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0755 (U+0755): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0755.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0755.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0755.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0755.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0755.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0755.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0755.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0756 (U+0756): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0756.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni0756.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0756.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0756.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0756.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0756.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0756.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0757.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni0757.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni0758.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni0758.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni0759 (U+0759): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;

* uni0759.fina: L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;

* uni075A (U+075A): L&lt;&lt;395.0,1784.0&gt;--&lt;394.0,1433.0&gt;&gt;

* uni075A.fina: L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;

* uni075B.fina: L&lt;&lt;1107.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni075D.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni075D.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni075D.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni075D.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni075E.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni075E.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni075E.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni075E.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni075F.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni075F.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni075F.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni075F.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni0760 (U+0760): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni0760.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni0760.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni0760.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni0761 (U+0761): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni0761.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni0761.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni0761.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni0762.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni0762.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni0763.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni0763.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni0764.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni0764.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni0765 (U+0765): L&lt;&lt;260.0,216.0&gt;--&lt;261.0,-469.0&gt;&gt;

* uni0765.init: L&lt;&lt;431.0,192.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni0765.medi: L&lt;&lt;243.0,194.0&gt;--&lt;-17.0,195.0&gt;&gt;

* uni0766 (U+0766): L&lt;&lt;260.0,216.0&gt;--&lt;261.0,-469.0&gt;&gt;

* uni0766.init: L&lt;&lt;431.0,192.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni0766.medi: L&lt;&lt;243.0,194.0&gt;--&lt;-17.0,195.0&gt;&gt;

* uni0767.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0767.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0767.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0767.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0767.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0767.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0768 (U+0768): L&lt;&lt;573.0,1784.0&gt;--&lt;572.0,1433.0&gt;&gt;

* uni0768.fina: L&lt;&lt;563.0,1620.0&gt;--&lt;562.0,1269.0&gt;&gt;

* uni0768.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0768.init: L&lt;&lt;481.0,1784.0&gt;--&lt;480.0,1433.0&gt;&gt;

* uni0768.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0768.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0768.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0768.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0768.medi: L&lt;&lt;573.0,1716.0&gt;--&lt;572.0,1365.0&gt;&gt;

* uni0768.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0769.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0769.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0769.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0769.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0769.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0769.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni076A.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni076A.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni076A.medi: L&lt;&lt;-13.0,400.0&gt;--&lt;342.0,403.0&gt;&gt;

* uni076A.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;799.0,191.0&gt;&gt;

* uni076A.medi: L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,194.0&gt;&gt;

* uni076A.medi: L&lt;&lt;799.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni076B.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni076B.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni076C.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni076C.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni076E (U+076E): L&lt;&lt;583.0,358.0&gt;--&lt;582.0,7.0&gt;&gt;

* uni076E.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;850.0,191.0&gt;&gt;

* uni076E.fina: L&lt;&lt;583.0,358.0&gt;--&lt;582.0,7.0&gt;&gt;

* uni076E.init: L&lt;&lt;501.0,-59.0&gt;--&lt;500.0,-410.0&gt;&gt;

* uni076E.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni076E.medi: L&lt;&lt;501.0,-59.0&gt;--&lt;500.0,-410.0&gt;&gt;

* uni076F (U+076F): L&lt;&lt;587.0,346.0&gt;--&lt;586.0,-5.0&gt;&gt;

* uni076F.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni076F.fina: L&lt;&lt;587.0,346.0&gt;--&lt;586.0,-5.0&gt;&gt;

* uni076F.init: L&lt;&lt;501.0,-37.0&gt;--&lt;500.0,-388.0&gt;&gt;

* uni076F.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni076F.medi: L&lt;&lt;501.0,-37.0&gt;--&lt;500.0,-388.0&gt;&gt;

* uni0770 (U+0770): L&lt;&lt;297.0,1291.0&gt;--&lt;296.0,1786.0&gt;&gt;

* uni0770.fina: L&lt;&lt;204.0,1291.0&gt;--&lt;203.0,1786.0&gt;&gt;

* uni0770.fina: L&lt;&lt;364.0,1786.0&gt;--&lt;362.0,1444.0&gt;&gt;

* uni0770.init: L&lt;&lt;455.0,1291.0&gt;--&lt;454.0,1786.0&gt;&gt;

* uni0770.medi: L&lt;&lt;410.0,1289.0&gt;--&lt;409.0,1784.0&gt;&gt;

* uni0770.medi: L&lt;&lt;570.0,1784.0&gt;--&lt;568.0,1442.0&gt;&gt;

* uni0771 (U+0771): L&lt;&lt;538.0,1604.0&gt;--&lt;537.0,1253.0&gt;&gt;

* uni0771.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni0771.fina: L&lt;&lt;538.0,1546.0&gt;--&lt;537.0,1195.0&gt;&gt;

* uni0771.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni0772 (U+0772): L&lt;&lt;526.0,1602.0&gt;--&lt;525.0,1251.0&gt;&gt;

* uni0772.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni0772.fina: L&lt;&lt;526.0,1602.0&gt;--&lt;525.0,1251.0&gt;&gt;

* uni0772.init: L&lt;&lt;444.0,1774.0&gt;--&lt;443.0,1423.0&gt;&gt;

* uni0772.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni0772.medi: L&lt;&lt;444.0,1774.0&gt;--&lt;443.0,1423.0&gt;&gt;

* uni0773.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0773.fina: L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uni0773.fina: L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uni0774.fina.alt: L&lt;&lt;1084.0,192.0&gt;--&lt;557.0,191.0&gt;&gt;

* uni0774.fina: L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uni0774.fina: L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uni0775.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni0775.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0775.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0775.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0775.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0775.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0775.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0776.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni0776.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0776.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0776.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0776.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0776.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0776.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni0777.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni0777.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni0777.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni0777.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni0777.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni0777.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni0777.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni077C.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni077C.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni077F (U+077F): L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni077F.fina: L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni077F.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni077F.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni08A0 (U+08A0): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08A0.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08A0.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08A0.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08A0.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08A0.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08A0.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08A0.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08A1 (U+08A1): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08A1.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08A1.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08A1.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08A1.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08A1.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08A1.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08A1.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08A2.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni08A2.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni08A3.init: L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uni08A3.init: L&lt;&lt;406.0,191.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni08A3.medi: L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uni08A4 (U+08A4): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni08A4.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni08A4.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni08A4.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni08A5.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni08A5.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni08A5.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni08A6.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni08A6.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08A6.medi: L&lt;&lt;-13.0,400.0&gt;--&lt;342.0,403.0&gt;&gt;

* uni08A6.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;799.0,191.0&gt;&gt;

* uni08A6.medi: L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,194.0&gt;&gt;

* uni08A6.medi: L&lt;&lt;799.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni08A7 (U+08A7): L&lt;&lt;260.0,216.0&gt;--&lt;261.0,-469.0&gt;&gt;

* uni08A7.init: L&lt;&lt;431.0,192.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uni08A7.medi: L&lt;&lt;243.0,194.0&gt;--&lt;-17.0,195.0&gt;&gt;

* uni08A8.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni08A8.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08A8.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08A8.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08A8.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08A8.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08A8.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08A9.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni08A9.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08A9.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08A9.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08A9.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08A9.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08A9.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08AC.fina: L&lt;&lt;1238.0,193.0&gt;--&lt;752.0,192.0&gt;&gt;

* uni08AC.fina: L&lt;&lt;744.0,401.0&gt;--&lt;1238.0,402.0&gt;&gt;

* uni08AF.fina: L&lt;&lt;1229.0,191.0&gt;--&lt;193.0,192.0&gt;&gt;

* uni08AF.medi: L&lt;&lt;1229.0,192.0&gt;--&lt;620.0,191.0&gt;&gt;

* uni08AF.medi: L&lt;&lt;1230.0,397.0&gt;--&lt;1229.0,192.0&gt;&gt;

* uni08B0.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni08B0.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni08B2.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni08B2.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni08B3.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni08B3.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni08B3.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni08B3.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni08B4 (U+08B4): L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni08B4.fina: L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uni08B4.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni08B4.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni08B6 (U+08B6): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08B6 (U+08B6): L&lt;&lt;505.0,1378.0&gt;--&lt;507.0,957.0&gt;&gt;

* uni08B6.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08B6.fina: L&lt;&lt;505.0,1378.0&gt;--&lt;507.0,957.0&gt;&gt;

* uni08B6.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08B6.init: L&lt;&lt;382.0,1378.0&gt;--&lt;384.0,957.0&gt;&gt;

* uni08B6.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08B6.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08B6.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08B6.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08B6.medi: L&lt;&lt;382.0,1378.0&gt;--&lt;384.0,957.0&gt;&gt;

* uni08B6.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08B7 (U+08B7): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08B7 (U+08B7): L&lt;&lt;505.0,1378.0&gt;--&lt;507.0,957.0&gt;&gt;

* uni08B7.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08B7.fina: L&lt;&lt;505.0,1378.0&gt;--&lt;507.0,957.0&gt;&gt;

* uni08B7.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08B7.init: L&lt;&lt;382.0,1378.0&gt;--&lt;384.0,957.0&gt;&gt;

* uni08B7.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08B7.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08B7.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08B7.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08B7.medi: L&lt;&lt;382.0,1378.0&gt;--&lt;384.0,957.0&gt;&gt;

* uni08B7.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08B8 (U+08B8): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08B8.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08B8.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08B8.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08B8.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08B8.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08B8.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08B8.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08B9.fina: L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uni08B9.fina: L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uni08BA.fina: L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uni08BA.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08BA.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08BA.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08BA.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08BA.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08BA.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08BB (U+08BB): L&lt;&lt;223.0,403.0&gt;--&lt;876.0,402.0&gt;&gt;

* uni08BB.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni08BB.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni08BB.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni08BC.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni08BC.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni08BC.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni08BD.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08BD.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08BD.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08BD.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08BD.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08BD.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08BE (U+08BE): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08BE.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08BE.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08BE.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08BE.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08BE.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08BE.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08BE.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08BF (U+08BF): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08BF.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08BF.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08BF.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08BF.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08BF.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08BF.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08BF.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08C0 (U+08C0): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08C0 (U+08C0): L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;

* uni08C0.fina: L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uni08C0.fina: L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;

* uni08C0.init: L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uni08C0.init: L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;

* uni08C0.init: L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08C0.medi: L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uni08C0.medi: L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uni08C0.medi: L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uni08C0.medi: L&lt;&lt;538.0,1497.0&gt;--&lt;537.0,1146.0&gt;&gt;

* uni08C0.medi: L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uni08C1.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni08C1.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni08C2.medi: L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uni08C2.medi: L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uni08C3.fina: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni08C3.fina: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni08C3.init: L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uni08C3.init: L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uni08C4.init: L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uni08C4.medi: L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uni08C4.medi: L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uni08C5.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni08C5.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni08C6.fina: L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uni08C6.medi: L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uni08C7 (U+08C7): L&lt;&lt;440.0,1620.0&gt;--&lt;439.0,1269.0&gt;&gt;

* uni08C7.fina: L&lt;&lt;440.0,1620.0&gt;--&lt;439.0,1269.0&gt;&gt;

* uni08C7.init: L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uni08C7.init: L&lt;&lt;456.0,1620.0&gt;--&lt;455.0,1269.0&gt;&gt;

* uni08C7.init: L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uni08C7.medi: L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uni08C7.medi: L&lt;&lt;332.0,191.0&gt;--&lt;-14.0,194.0&gt;&gt;

* uni08C7.medi: L&lt;&lt;538.0,1825.0&gt;--&lt;537.0,1474.0&gt;&gt;

* uni08C7.medi: L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uni08DB (U+08DB): L&lt;&lt;448.0,1094.0&gt;--&lt;574.0,1095.0&gt;&gt;

* uni08DD (U+08DD): L&lt;&lt;616.0,1013.0&gt;--&lt;496.0,1014.0&gt;&gt;

* uni08DE (U+08DE): L&lt;&lt;843.0,1012.0&gt;--&lt;527.0,1013.0&gt;&gt;

* uni0E3F (U+0E3F): L&lt;&lt;129.0,1285.0&gt;--&lt;445.0,1283.0&gt;&gt;

* uni0E3F (U+0E3F): L&lt;&lt;426.0,134.0&gt;--&lt;424.0,579.0&gt;&gt;

* uni0E3F (U+0E3F): L&lt;&lt;447.0,-32.0&gt;--&lt;129.0,-34.0&gt;&gt;

* uni0E3F (U+0E3F): L&lt;&lt;620.0,554.0&gt;--&lt;618.0,160.0&gt;&gt;

* uni1E0D (U+1E0D): L&lt;&lt;853.0,788.0&gt;--&lt;852.0,1257.0&gt;&gt;

* uni1E0F (U+1E0F): L&lt;&lt;853.0,788.0&gt;--&lt;852.0,1257.0&gt;&gt;

* uni1E25 (U+1E25): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;

* uni1E27 (U+1E27): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;

* uni1E2B (U+1E2B): L&lt;&lt;386.0,1257.0&gt;--&lt;385.0,728.0&gt;&gt;

* uni1E2F (U+1E2F): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* uni1E2F (U+1E2F): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* uni1E36 (U+1E36): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1E36 (U+1E36): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* uni1E37 (U+1E37): L&lt;&lt;280.0,1346.0&gt;--&lt;627.0,1343.0&gt;&gt;

* uni1E37 (U+1E37): L&lt;&lt;519.0,1136.0&gt;--&lt;280.0,1134.0&gt;&gt;

* uni1E38 (U+1E38): L&lt;&lt;429.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1E38 (U+1E38): L&lt;&lt;977.0,-34.0&gt;--&lt;341.0,-33.0&gt;&gt;

* uni1E39 (U+1E39): L&lt;&lt;280.0,1346.0&gt;--&lt;627.0,1343.0&gt;&gt;

* uni1E39 (U+1E39): L&lt;&lt;519.0,1136.0&gt;--&lt;280.0,1134.0&gt;&gt;

* uni1E92 (U+1E92): L&lt;&lt;256.0,1221.0&gt;--&lt;899.0,1220.0&gt;&gt;

* uni1E92 (U+1E92): L&lt;&lt;452.0,177.0&gt;--&lt;996.0,178.0&gt;&gt;

* uni1E92 (U+1E92): L&lt;&lt;757.0,1010.0&gt;--&lt;256.0,1009.0&gt;&gt;

* uni1E92 (U+1E92): L&lt;&lt;996.0,-34.0&gt;--&lt;303.0,-33.0&gt;&gt;

* uni1E93 (U+1E93): L&lt;&lt;261.0,958.0&gt;--&lt;897.0,957.0&gt;&gt;

* uni1E93 (U+1E93): L&lt;&lt;498.0,177.0&gt;--&lt;987.0,178.0&gt;&gt;

* uni1E93 (U+1E93): L&lt;&lt;720.0,747.0&gt;--&lt;261.0,746.0&gt;&gt;

* uni1E93 (U+1E93): L&lt;&lt;987.0,-34.0&gt;--&lt;324.0,-33.0&gt;&gt;

* uni1EB8 (U+1EB8): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EB8 (U+1EB8): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EB8 (U+1EB8): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EB8 (U+1EB8): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EB8 (U+1EB8): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EB8 (U+1EB8): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EB9 (U+1EB9): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EBA (U+1EBA): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EBA (U+1EBA): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EBA (U+1EBA): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EBA (U+1EBA): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EBA (U+1EBA): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EBA (U+1EBA): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EBB (U+1EBB): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EBC (U+1EBC): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EBC (U+1EBC): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EBC (U+1EBC): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EBC (U+1EBC): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EBC (U+1EBC): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EBC (U+1EBC): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EBD (U+1EBD): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EBE (U+1EBE): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EBE (U+1EBE): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EBE (U+1EBE): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EBE (U+1EBE): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EBE (U+1EBE): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EBE (U+1EBE): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EBF (U+1EBF): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EC0 (U+1EC0): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EC0 (U+1EC0): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EC0 (U+1EC0): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EC0 (U+1EC0): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EC0 (U+1EC0): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EC0 (U+1EC0): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EC1 (U+1EC1): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EC2 (U+1EC2): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EC3 (U+1EC3): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EC4 (U+1EC4): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EC4 (U+1EC4): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EC4 (U+1EC4): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EC4 (U+1EC4): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EC4 (U+1EC4): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EC4 (U+1EC4): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EC5 (U+1EC5): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EC6 (U+1EC6): L&lt;&lt;321.0,1220.0&gt;--&lt;957.0,1221.0&gt;&gt;

* uni1EC6 (U+1EC6): L&lt;&lt;409.0,177.0&gt;--&lt;977.0,178.0&gt;&gt;

* uni1EC6 (U+1EC6): L&lt;&lt;409.0,717.0&gt;--&lt;832.0,718.0&gt;&gt;

* uni1EC6 (U+1EC6): L&lt;&lt;832.0,506.0&gt;--&lt;409.0,507.0&gt;&gt;

* uni1EC6 (U+1EC6): L&lt;&lt;957.0,1009.0&gt;--&lt;409.0,1010.0&gt;&gt;

* uni1EC6 (U+1EC6): L&lt;&lt;977.0,-34.0&gt;--&lt;322.0,-33.0&gt;&gt;

* uni1EC7 (U+1EC7): L&lt;&lt;1026.0,391.0&gt;--&lt;311.0,392.0&gt;&gt;

* uni1EC9 (U+1EC9): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* uni1EC9 (U+1EC9): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* uni1ECB (U+1ECB): L&lt;&lt;532.0,159.0&gt;--&lt;531.0,767.0&gt;&gt;

* uni1ECB (U+1ECB): L&lt;&lt;747.0,856.0&gt;--&lt;744.0,158.0&gt;&gt;

* uni1EF4 (U+1EF4): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* uni1EF4 (U+1EF4): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* uni1EF6 (U+1EF6): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* uni1EF6 (U+1EF6): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* uni1EF8 (U+1EF8): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,476.0&gt;&gt;

* uni1EF8 (U+1EF8): L&lt;&lt;722.0,477.0&gt;--&lt;723.0,55.0&gt;&gt;

* uni1F21 (U+1F21): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F22 (U+1F22): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F23 (U+1F23): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F24 (U+1F24): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F25 (U+1F25): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F26 (U+1F26): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F74 (U+1F74): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F75 (U+1F75): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F90 (U+1F90): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F91 (U+1F91): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F92 (U+1F92): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F93 (U+1F93): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F94 (U+1F94): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F95 (U+1F95): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F96 (U+1F96): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1F97 (U+1F97): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1FC2 (U+1FC2): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1FC3 (U+1FC3): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1FC4 (U+1FC4): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1FC6 (U+1FC6): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni1FC7 (U+1FC7): L&lt;&lt;832.0,-425.0&gt;--&lt;830.0,515.0&gt;&gt;

* uni200E (U+200E): L&lt;&lt;280.0,1418.0&gt;--&lt;277.0,1066.0&gt;&gt;

* uni200E (U+200E): L&lt;&lt;707.0,1204.0&gt;--&lt;708.0,1082.0&gt;&gt;

* uni200F (U+200F): L&lt;&lt;269.0,1209.0&gt;--&lt;270.0,1086.0&gt;&gt;

* uni200F (U+200F): L&lt;&lt;759.0,1422.0&gt;--&lt;756.0,1070.0&gt;&gt;

* uni202A (U+202A): L&lt;&lt;282.0,1420.0&gt;--&lt;279.0,1068.0&gt;&gt;

* uni202A (U+202A): L&lt;&lt;715.0,1207.0&gt;--&lt;716.0,1084.0&gt;&gt;

* uni202B (U+202B): L&lt;&lt;755.0,1422.0&gt;--&lt;752.0,1070.0&gt;&gt;

* uni202D (U+202D): L&lt;&lt;282.0,1420.0&gt;--&lt;279.0,1068.0&gt;&gt;

* uni202D (U+202D): L&lt;&lt;715.0,1207.0&gt;--&lt;716.0,1084.0&gt;&gt;

* uni202E (U+202E): L&lt;&lt;755.0,1422.0&gt;--&lt;752.0,1070.0&gt;&gt;

* uni2066 (U+2066): L&lt;&lt;280.0,1418.0&gt;--&lt;277.0,1066.0&gt;&gt;

* uni2066 (U+2066): L&lt;&lt;707.0,1204.0&gt;--&lt;708.0,1082.0&gt;&gt;

* uni2067 (U+2067): L&lt;&lt;755.0,1422.0&gt;--&lt;752.0,1070.0&gt;&gt;

* uni2068 (U+2068): L&lt;&lt;243.0,1473.0&gt;--&lt;501.0,1474.0&gt;&gt;

* uni2068 (U+2068): L&lt;&lt;245.0,1240.0&gt;--&lt;452.0,1241.0&gt;&gt;

* uni2068 (U+2068): L&lt;&lt;452.0,1235.0&gt;--&lt;245.0,1236.0&gt;&gt;

* uni2068 (U+2068): L&lt;&lt;501.0,1468.0&gt;--&lt;243.0,1469.0&gt;&gt;

* uni2422 (U+2422): L&lt;&lt;169.0,983.0&gt;--&lt;170.0,1109.0&gt;&gt;

* uni2E18 (U+2E18): L&lt;&lt;399.0,-320.0&gt;--&lt;398.0,-202.0&gt;&gt;

* uniA64D (U+A64D): L&lt;&lt;431.0,231.0&gt;--&lt;432.0,412.0&gt;&gt;

* uniA64D (U+A64D): L&lt;&lt;641.0,413.0&gt;--&lt;642.0,231.0&gt;&gt;

* uniA656 (U+A656): L&lt;&lt;781.0,147.0&gt;--&lt;779.0,510.0&gt;&gt;

* uniFB01 (U+FB01): L&lt;&lt;1760.0,159.0&gt;--&lt;1759.0,767.0&gt;&gt;

* uniFB01 (U+FB01): L&lt;&lt;1975.0,856.0&gt;--&lt;1972.0,158.0&gt;&gt;

* uniFB02 (U+FB02): L&lt;&lt;1508.0,1346.0&gt;--&lt;1855.0,1343.0&gt;&gt;

* uniFB02 (U+FB02): L&lt;&lt;1747.0,1136.0&gt;--&lt;1508.0,1134.0&gt;&gt;

* uniFB51 (U+FB51): L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uniFB51 (U+FB51): L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uniFB53 (U+FB53): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFB54 (U+FB54): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFB54 (U+FB54): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFB55 (U+FB55): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFB55 (U+FB55): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFB55 (U+FB55): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFB55 (U+FB55): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFB57 (U+FB57): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFB58 (U+FB58): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFB58 (U+FB58): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFB59 (U+FB59): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFB59 (U+FB59): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFB59 (U+FB59): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFB59 (U+FB59): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFB5B (U+FB5B): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFB5C (U+FB5C): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFB5C (U+FB5C): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFB5D (U+FB5D): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFB5D (U+FB5D): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFB5D (U+FB5D): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFB5D (U+FB5D): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFB5F (U+FB5F): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFB60 (U+FB60): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFB60 (U+FB60): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFB61 (U+FB61): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFB61 (U+FB61): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFB61 (U+FB61): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFB61 (U+FB61): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFB63 (U+FB63): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFB64 (U+FB64): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFB64 (U+FB64): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFB65 (U+FB65): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFB65 (U+FB65): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFB65 (U+FB65): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFB65 (U+FB65): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFB67 (U+FB67): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFB67 (U+FB67): L&lt;&lt;565.0,1716.0&gt;--&lt;564.0,1365.0&gt;&gt;

* uniFB68 (U+FB68): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFB68 (U+FB68): L&lt;&lt;741.0,1716.0&gt;--&lt;740.0,1365.0&gt;&gt;

* uniFB68 (U+FB68): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFB69 (U+FB69): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFB69 (U+FB69): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFB69 (U+FB69): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFB69 (U+FB69): L&lt;&lt;741.0,1716.0&gt;--&lt;740.0,1365.0&gt;&gt;

* uniFB69 (U+FB69): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFB6C (U+FB6C): L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uniFB6D (U+FB6D): L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uniFB6D (U+FB6D): L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFB70 (U+FB70): L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uniFB71 (U+FB71): L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uniFB71 (U+FB71): L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFB73 (U+FB73): L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uniFB75 (U+FB75): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFB77 (U+FB77): L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uniFB79 (U+FB79): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFB7B (U+FB7B): L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uniFB7D (U+FB7D): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFB7F (U+FB7F): L&lt;&lt;1240.0,193.0&gt;--&lt;891.0,191.0&gt;&gt;

* uniFB81 (U+FB81): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFB89 (U+FB89): L&lt;&lt;335.0,1784.0&gt;--&lt;334.0,1433.0&gt;&gt;

* uniFB8B (U+FB8B): L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uniFB8B (U+FB8B): L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uniFB8D (U+FB8D): L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uniFB8D (U+FB8D): L&lt;&lt;538.0,1483.0&gt;--&lt;537.0,1132.0&gt;&gt;

* uniFB8D (U+FB8D): L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uniFB91 (U+FB91): L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uniFB91 (U+FB91): L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uniFB95 (U+FB95): L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uniFB95 (U+FB95): L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uniFB99 (U+FB99): L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uniFB99 (U+FB99): L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uniFB9D (U+FB9D): L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uniFB9D (U+FB9D): L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uniFBA1 (U+FBA1): L&lt;&lt;538.0,1298.0&gt;--&lt;537.0,947.0&gt;&gt;

* uniFBA2 (U+FBA2): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFBA2 (U+FBA2): L&lt;&lt;335.0,1716.0&gt;--&lt;334.0,1365.0&gt;&gt;

* uniFBA2 (U+FBA2): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFBA3 (U+FBA3): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFBA3 (U+FBA3): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFBA3 (U+FBA3): L&lt;&lt;335.0,1716.0&gt;--&lt;334.0,1365.0&gt;&gt;

* uniFBA3 (U+FBA3): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFBA3 (U+FBA3): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFBA5 (U+FBA5): L&lt;&lt;1241.0,194.0&gt;--&lt;887.0,191.0&gt;&gt;

* uniFBA5 (U+FBA5): L&lt;&lt;887.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFBA8 (U+FBA8): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFBA8 (U+FBA8): L&lt;&lt;519.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFBA9 (U+FBA9): L&lt;&lt;336.0,192.0&gt;--&lt;-13.0,194.0&gt;&gt;

* uniFBC0 (U+FBC0): L&lt;&lt;538.0,1620.0&gt;--&lt;537.0,1269.0&gt;&gt;

* uniFBC1 (U+FBC1): L&lt;&lt;538.0,279.0&gt;--&lt;537.0,-72.0&gt;&gt;

* uniFBD4 (U+FBD4): L&lt;&lt;854.0,793.0&gt;--&lt;851.0,1418.0&gt;&gt;

* uniFBD4 (U+FBD4): L&lt;&lt;856.0,386.0&gt;--&lt;854.0,663.0&gt;&gt;

* uniFBD6 (U+FBD6): L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uniFBD6 (U+FBD6): L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uniFBE5 (U+FBE5): L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uniFBE6 (U+FBE6): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFBE6 (U+FBE6): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFBE7 (U+FBE7): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFBE7 (U+FBE7): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFBE7 (U+FBE7): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFBE7 (U+FBE7): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFBE8 (U+FBE8): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFBE8 (U+FBE8): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFBE9 (U+FBE9): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFBE9 (U+FBE9): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFBE9 (U+FBE9): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFBE9 (U+FBE9): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFBFD (U+FBFD): L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uniFBFE (U+FBFE): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFBFE (U+FBFE): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFBFF (U+FBFF): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFBFF (U+FBFF): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFBFF (U+FBFF): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFBFF (U+FBFF): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFD88 (U+FD88): L&lt;&lt;586.0,1257.0&gt;--&lt;585.0,1694.0&gt;&gt;

* uniFDFB (U+FDFB): L&lt;&lt;599.0,420.0&gt;--&lt;597.0,653.0&gt;&gt;

* uniFE00 (U+FE00): L&lt;&lt;609.0,430.0&gt;--&lt;608.0,816.0&gt;&gt;

* uniFE00 (U+FE00): L&lt;&lt;610.0,816.0&gt;--&lt;611.0,431.0&gt;&gt;

* uniFE01 (U+FE01): L&lt;&lt;498.0,412.0&gt;--&lt;738.0,413.0&gt;&gt;

* uniFE01 (U+FE01): L&lt;&lt;738.0,407.0&gt;--&lt;498.0,408.0&gt;&gt;

* uniFE04 (U+FE04): L&lt;&lt;508.0,859.0&gt;--&lt;708.0,860.0&gt;&gt;

* uniFE04 (U+FE04): L&lt;&lt;708.0,854.0&gt;--&lt;508.0,855.0&gt;&gt;

* uniFE06 (U+FE06): L&lt;&lt;452.0,860.0&gt;--&lt;717.0,859.0&gt;&gt;

* uniFE06 (U+FE06): L&lt;&lt;717.0,855.0&gt;--&lt;452.0,854.0&gt;&gt;

* uniFE09 (U+FE09): L&lt;&lt;299.0,475.0&gt;--&lt;300.0,794.0&gt;&gt;

* uniFE0A (U+FE0A): L&lt;&lt;363.0,430.0&gt;--&lt;362.0,816.0&gt;&gt;

* uniFE0A (U+FE0A): L&lt;&lt;364.0,816.0&gt;--&lt;365.0,431.0&gt;&gt;

* uniFE0A (U+FE0A): L&lt;&lt;783.0,430.0&gt;--&lt;782.0,816.0&gt;&gt;

* uniFE0A (U+FE0A): L&lt;&lt;784.0,816.0&gt;--&lt;785.0,431.0&gt;&gt;

* uniFE0B (U+FE0B): L&lt;&lt;363.0,430.0&gt;--&lt;362.0,816.0&gt;&gt;

* uniFE0B (U+FE0B): L&lt;&lt;364.0,816.0&gt;--&lt;365.0,431.0&gt;&gt;

* uniFE0B (U+FE0B): L&lt;&lt;672.0,412.0&gt;--&lt;912.0,413.0&gt;&gt;

* uniFE0B (U+FE0B): L&lt;&lt;912.0,407.0&gt;--&lt;672.0,408.0&gt;&gt;

* uniFE0C (U+FE0C): L&lt;&lt;363.0,430.0&gt;--&lt;362.0,816.0&gt;&gt;

* uniFE0C (U+FE0C): L&lt;&lt;364.0,816.0&gt;--&lt;365.0,431.0&gt;&gt;

* uniFE0D (U+FE0D): L&lt;&lt;363.0,430.0&gt;--&lt;362.0,816.0&gt;&gt;

* uniFE0D (U+FE0D): L&lt;&lt;364.0,816.0&gt;--&lt;365.0,431.0&gt;&gt;

* uniFE0E (U+FE0E): L&lt;&lt;363.0,430.0&gt;--&lt;362.0,816.0&gt;&gt;

* uniFE0E (U+FE0E): L&lt;&lt;364.0,816.0&gt;--&lt;365.0,431.0&gt;&gt;

* uniFE0E (U+FE0E): L&lt;&lt;682.0,859.0&gt;--&lt;882.0,860.0&gt;&gt;

* uniFE0E (U+FE0E): L&lt;&lt;882.0,854.0&gt;--&lt;682.0,855.0&gt;&gt;

* uniFE0F (U+FE0F): L&lt;&lt;299.0,475.0&gt;--&lt;300.0,794.0&gt;&gt;

* uniFE82 (U+FE82): L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uniFE82 (U+FE82): L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uniFE84 (U+FE84): L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uniFE84 (U+FE84): L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uniFE88 (U+FE88): L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uniFE88 (U+FE88): L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uniFE8A (U+FE8A): L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uniFE8B (U+FE8B): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFE8B (U+FE8B): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFE8C (U+FE8C): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFE8C (U+FE8C): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFE8C (U+FE8C): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFE8C (U+FE8C): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFE8E (U+FE8E): L&lt;&lt;1237.0,192.0&gt;--&lt;719.0,191.0&gt;&gt;

* uniFE8E (U+FE8E): L&lt;&lt;719.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uniFE90 (U+FE90): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFE91 (U+FE91): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFE91 (U+FE91): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFE92 (U+FE92): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFE92 (U+FE92): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFE92 (U+FE92): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFE92 (U+FE92): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFE94 (U+FE94): L&lt;&lt;1241.0,194.0&gt;--&lt;887.0,191.0&gt;&gt;

* uniFE94 (U+FE94): L&lt;&lt;887.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFE96 (U+FE96): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFE97 (U+FE97): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFE97 (U+FE97): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFE98 (U+FE98): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFE98 (U+FE98): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFE98 (U+FE98): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFE98 (U+FE98): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFE9A (U+FE9A): L&lt;&lt;223.0,403.0&gt;--&lt;867.0,398.0&gt;&gt;

* uniFE9B (U+FE9B): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFE9B (U+FE9B): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFE9C (U+FE9C): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFE9C (U+FE9C): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFE9C (U+FE9C): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFE9C (U+FE9C): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFE9E (U+FE9E): L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uniFEA0 (U+FEA0): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFEA2 (U+FEA2): L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uniFEA4 (U+FEA4): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFEA6 (U+FEA6): L&lt;&lt;1240.0,193.0&gt;--&lt;848.0,191.0&gt;&gt;

* uniFEA8 (U+FEA8): L&lt;&lt;1043.0,398.0&gt;--&lt;1248.0,397.0&gt;&gt;

* uniFEAE (U+FEAE): L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uniFEAE (U+FEAE): L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uniFEB0 (U+FEB0): L&lt;&lt;1244.0,399.0&gt;--&lt;1243.0,195.0&gt;&gt;

* uniFEB0 (U+FEB0): L&lt;&lt;970.0,398.0&gt;--&lt;1244.0,399.0&gt;&gt;

* uniFEBA (U+FEBA): L&lt;&lt;1229.0,191.0&gt;--&lt;193.0,192.0&gt;&gt;

* uniFEBC (U+FEBC): L&lt;&lt;1229.0,192.0&gt;--&lt;620.0,191.0&gt;&gt;

* uniFEBC (U+FEBC): L&lt;&lt;1230.0,397.0&gt;--&lt;1229.0,192.0&gt;&gt;

* uniFEBE (U+FEBE): L&lt;&lt;1229.0,191.0&gt;--&lt;193.0,192.0&gt;&gt;

* uniFEC0 (U+FEC0): L&lt;&lt;1229.0,192.0&gt;--&lt;620.0,191.0&gt;&gt;

* uniFEC0 (U+FEC0): L&lt;&lt;1230.0,397.0&gt;--&lt;1229.0,192.0&gt;&gt;

* uniFEC3 (U+FEC3): L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uniFEC3 (U+FEC3): L&lt;&lt;406.0,191.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uniFEC4 (U+FEC4): L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uniFEC7 (U+FEC7): L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uniFEC7 (U+FEC7): L&lt;&lt;406.0,191.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uniFEC8 (U+FEC8): L&lt;&lt;231.0,377.0&gt;--&lt;230.0,1509.0&gt;&gt;

* uniFECA (U+FECA): L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uniFECA (U+FECA): L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uniFECB (U+FECB): L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uniFECB (U+FECB): L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uniFECE (U+FECE): L&lt;&lt;1239.0,193.0&gt;--&lt;813.0,191.0&gt;&gt;

* uniFECE (U+FECE): L&lt;&lt;813.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uniFECF (U+FECF): L&lt;&lt;-11.0,401.0&gt;--&lt;406.0,403.0&gt;&gt;

* uniFECF (U+FECF): L&lt;&lt;723.0,191.0&gt;--&lt;-7.0,192.0&gt;&gt;

* uniFED3 (U+FED3): L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uniFED4 (U+FED4): L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uniFED4 (U+FED4): L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFED7 (U+FED7): L&lt;&lt;-5.0,403.0&gt;--&lt;878.0,402.0&gt;&gt;

* uniFED8 (U+FED8): L&lt;&lt;1241.0,194.0&gt;--&lt;879.0,191.0&gt;&gt;

* uniFED8 (U+FED8): L&lt;&lt;879.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFEDA (U+FEDA): L&lt;&lt;856.0,386.0&gt;--&lt;851.0,1509.0&gt;&gt;

* uniFEDC (U+FEDC): L&lt;&lt;-10.0,402.0&gt;--&lt;481.0,403.0&gt;&gt;

* uniFEDC (U+FEDC): L&lt;&lt;481.0,191.0&gt;--&lt;-10.0,192.0&gt;&gt;

* uniFEDF (U+FEDF): L&lt;&lt;-6.0,402.0&gt;--&lt;774.0,403.0&gt;&gt;

* uniFEDF (U+FEDF): L&lt;&lt;774.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFEE0 (U+FEE0): L&lt;&lt;-13.0,400.0&gt;--&lt;342.0,403.0&gt;&gt;

* uniFEE0 (U+FEE0): L&lt;&lt;1239.0,193.0&gt;--&lt;799.0,191.0&gt;&gt;

* uniFEE0 (U+FEE0): L&lt;&lt;346.0,191.0&gt;--&lt;-13.0,194.0&gt;&gt;

* uniFEE0 (U+FEE0): L&lt;&lt;799.0,403.0&gt;--&lt;1239.0,401.0&gt;&gt;

* uniFEE3 (U+FEE3): L&lt;&lt;431.0,192.0&gt;--&lt;-11.0,193.0&gt;&gt;

* uniFEE4 (U+FEE4): L&lt;&lt;243.0,194.0&gt;--&lt;-17.0,195.0&gt;&gt;

* uniFEE7 (U+FEE7): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFEE7 (U+FEE7): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFEE8 (U+FEE8): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFEE8 (U+FEE8): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFEE8 (U+FEE8): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFEE8 (U+FEE8): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFEEA (U+FEEA): L&lt;&lt;1241.0,194.0&gt;--&lt;887.0,191.0&gt;&gt;

* uniFEEA (U+FEEA): L&lt;&lt;887.0,403.0&gt;--&lt;1241.0,400.0&gt;&gt;

* uniFEEC (U+FEEC): L&lt;&lt;1237.0,402.0&gt;--&lt;1238.0,192.0&gt;&gt;

* uniFEEC (U+FEEC): L&lt;&lt;1238.0,192.0&gt;--&lt;795.0,191.0&gt;&gt;

* uniFEEC (U+FEEC): L&lt;&lt;720.0,403.0&gt;--&lt;1237.0,402.0&gt;&gt;

* uniFEF0 (U+FEF0): L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uniFEF2 (U+FEF2): L&lt;&lt;1240.0,401.0&gt;--&lt;1239.0,193.0&gt;&gt;

* uniFEF3 (U+FEF3): L&lt;&lt;-6.0,402.0&gt;--&lt;724.0,398.0&gt;&gt;

* uniFEF3 (U+FEF3): L&lt;&lt;811.0,191.0&gt;--&lt;-6.0,192.0&gt;&gt;

* uniFEF4 (U+FEF4): L&lt;&lt;-13.0,401.0&gt;--&lt;356.0,403.0&gt;&gt;

* uniFEF4 (U+FEF4): L&lt;&lt;1238.0,193.0&gt;--&lt;784.0,191.0&gt;&gt;

* uniFEF4 (U+FEF4): L&lt;&lt;360.0,191.0&gt;--&lt;-13.0,193.0&gt;&gt;

* uniFEF4 (U+FEF4): L&lt;&lt;784.0,403.0&gt;--&lt;1238.0,401.0&gt;&gt;

* uniFEF5 (U+FEF5): L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt;

* uniFEF7 (U+FEF7): L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt;

* uniFEF9 (U+FEF9): L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt;

* uniFEFB (U+FEFB): L&lt;&lt;666.0,400.0&gt;--&lt;823.0,401.0&gt;&gt;

* yen (U+00A5): L&lt;&lt;505.0,55.0&gt;--&lt;506.0,256.0&gt;&gt;

* yen (U+00A5): L&lt;&lt;722.0,256.0&gt;--&lt;723.0,55.0&gt;&gt;

* z (U+007A): L&lt;&lt;261.0,958.0&gt;--&lt;897.0,957.0&gt;&gt;

* z (U+007A): L&lt;&lt;498.0,177.0&gt;--&lt;987.0,178.0&gt;&gt;

* z (U+007A): L&lt;&lt;720.0,747.0&gt;--&lt;261.0,746.0&gt;&gt;

* z (U+007A): L&lt;&lt;987.0,-34.0&gt;--&lt;324.0,-33.0&gt;&gt;

* zacute (U+017A): L&lt;&lt;261.0,958.0&gt;--&lt;897.0,957.0&gt;&gt;

* zacute (U+017A): L&lt;&lt;498.0,177.0&gt;--&lt;987.0,178.0&gt;&gt;

* zacute (U+017A): L&lt;&lt;720.0,747.0&gt;--&lt;261.0,746.0&gt;&gt;

* zacute (U+017A): L&lt;&lt;987.0,-34.0&gt;--&lt;324.0,-33.0&gt;&gt;

* zcaron (U+017E): L&lt;&lt;261.0,958.0&gt;--&lt;897.0,957.0&gt;&gt;

* zcaron (U+017E): L&lt;&lt;498.0,177.0&gt;--&lt;987.0,178.0&gt;&gt;

* zcaron (U+017E): L&lt;&lt;720.0,747.0&gt;--&lt;261.0,746.0&gt;&gt;

* zcaron (U+017E): L&lt;&lt;987.0,-34.0&gt;--&lt;324.0,-33.0&gt;&gt;

* zdotaccent (U+017C): L&lt;&lt;261.0,958.0&gt;--&lt;897.0,957.0&gt;&gt;

* zdotaccent (U+017C): L&lt;&lt;498.0,177.0&gt;--&lt;987.0,178.0&gt;&gt;

* zdotaccent (U+017C): L&lt;&lt;720.0,747.0&gt;--&lt;261.0,746.0&gt;&gt;

* zdotaccent (U+017C): L&lt;&lt;987.0,-34.0&gt;--&lt;324.0,-33.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[15] CourierBadi-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;Version 0.900; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: lira	Contours detected: 2	Expected: 1

- Glyph name: summation	Contours detected: 3	Expected: 1

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2

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

- Glyph name: uni203D	Contours detected: 3	Expected: 2

- Glyph name: uni26AE	Contours detected: 5	Expected: 3

- Glyph name: uni2E18	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* sigma1 (U+03C2): B&lt;&lt;978.5,854.0&gt;-&lt;980.0,845.0&gt;-&lt;977.0,852.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.medi: B&lt;&lt;50.0,1165.0&gt;-&lt;51.0,1165.0&gt;-&lt;49.0,1159.0&gt;&gt; has the same coordinates as a previous segment.

* uni0770.medi: B&lt;&lt;64.0,842.0&gt;-&lt;66.0,842.0&gt;-&lt;64.0,833.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D (U+077D): L&lt;&lt;636.0,1516.0&gt;--&lt;640.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.fina: L&lt;&lt;543.0,1516.0&gt;--&lt;547.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.init: L&lt;&lt;794.0,1516.0&gt;--&lt;798.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

* uni077D.medi: L&lt;&lt;681.0,1516.0&gt;--&lt;685.0,1515.0&gt;&gt; has the same coordinates as a previous segment.

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
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, canadian-aboriginal, hebrew, tai-le, todhri, old-permic, malayalam, math, syriac, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
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
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, math, cherokee</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, thai, sunuwar, cherokee, gothic, syriac, caucasian-albanian</li>
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
<li>U+060C ARABIC COMMA: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
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
<li>U+061B ARABIC SEMICOLON: try adding one of: arabic, yezidi, hanifi-rohingya, garay, syriac, nko, thaana</li>
<li>U+061C ARABIC LETTER MARK: try adding one of: arabic, syriac, thaana</li>
<li>U+061E ARABIC TRIPLE DOT PUNCTUATION MARK: try adding arabic</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: arabic, yezidi, hanifi-rohingya, garay, adlam, syriac, nko, thaana</li>
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
<li>U+0640 ARABIC TATWEEL: try adding one of: arabic, old-uyghur, mandaic, psalter-pahlavi, hanifi-rohingya, adlam, manichaean, syriac, sogdian</li>
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
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: arabic, yezidi, hanifi-rohingya, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: arabic, yezidi, indic-siyaq-numbers, syriac, thaana</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: arabic, syriac, nko, thaana</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: arabic, syriac, thaana</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: arabic, syriac, thaana</li>
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
<li>U+06D4 ARABIC FULL STOP: try adding one of: arabic, hanifi-rohingya, yezidi</li>
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
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, dogra, tagbanwa, duployan, batak, hatran, mandaic, cham, khojki, hanunoo, hebrew, javanese, masaram-gondi, mongolian, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, siddham, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: tagalog, gunjala-gondi, sinhala, bengali, mahajani, meetei-mayek, telugu, pahawh-hmong, zanabazar-square, brahmi, manichaean, tai-tham, buginese, sharada, tamil, tai-viet, old-hungarian, dogra, tagbanwa, duployan, batak, mandaic, masaram-gondi, cham, khojki, hanunoo, hebrew, javanese, mongolian, siddham, thai, kharoshthi, yi, takri, sogdian, modi, kaithi, limbu, gurmukhi, newa, rejang, saurashtra, tifinagh, tirhuta, sundanese, balinese, phags-pa, tibetan, khudawadi, malayalam, chakma, devanagari, khmer, gujarati, bhaiksuki, lepcha, myanmar, kayah-li, nko, syriac, arabic, warang-citi, grantha, psalter-pahlavi, new-tai-lue, buhid, oriya, tai-le, lao, hanifi-rohingya, kannada, syloti-nagri, avestan, thaana</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: arabic, hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: hebrew, phags-pa, syriac, nko, thaana</li>
<li>U+2010 HYPHEN: try adding one of: arabic, cham, yi, hebrew, sundanese, lisu, kharoshthi, armenian, sora-sompeng, syloti-nagri, kaithi, kayah-li, coptic</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
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
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: telugu, math, manichaean, sharada, tamil, duployan, batak, kharoshthi, sogdian, gurmukhi, symbols, saurashtra, balinese, soyombo, khudawadi, gujarati, bhaiksuki, myanmar, nko, grantha, lepcha, khojki, caucasian-albanian, gunjala-gondi, bengali, mende-kikakui, buginese, tai-viet, dogra, tagbanwa, siddham, cham, mongolian, hanunoo, zanabazar-square, bassa-vah, limbu, tirhuta, tibetan, warang-citi, marchen, new-tai-lue, hanifi-rohingya, syloti-nagri, canadian-aboriginal, pahawh-hmong, tai-tham, masaram-gondi, mandaic, yi, javanese, hebrew, adlam, rejang, tifinagh, sundanese, phags-pa, malayalam, devanagari, elbasan, syriac, kayah-li, psalter-pahlavi, music, oriya, tai-le, armenian, tagalog, sinhala, mahajani, meetei-mayek, old-permic, brahmi, osage, thai, takri, modi, kaithi, newa, wancho, chakma, khmer, coptic, miao, buhid, ahom, lao, kannada, thaana</li>
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
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: arabic, nko</li>
<li>U+FD88 ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM: try adding arabic</li>
<li>U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM: try adding one of: arabic, thaana</li>
<li>U+FDF4 ARABIC LIGATURE MOHAMMAD ISOLATED FORM: try adding arabic</li>
<li>U+FDFA ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM: try adding arabic</li>
<li>U+FDFB ARABIC LIGATURE JALLAJALALOUHOU: try adding arabic</li>
<li>U+FDFC RIAL SIGN: try adding arabic</li>
<li>U+FDFD ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM: try adding one of: arabic, thaana</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, phags-pa, yi</li>
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

* uni06CD.fina: L&lt;&lt;334.0,285.0&gt;--&lt;334.0,283.0&gt;&gt; -&gt; L&lt;&lt;334.0,283.0&gt;--&lt;334.0,282.0&gt;&gt;

* uni06E9 (U+06E9): L&lt;&lt;682.0,678.0&gt;--&lt;682.0,672.0&gt;&gt; -&gt; L&lt;&lt;682.0,672.0&gt;--&lt;682.0,598.0&gt;&gt;

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

* uniFCA2 (U+FCA2): L&lt;&lt;116.0,763.0&gt;--&lt;116.0,765.0&gt;&gt; -&gt; L&lt;&lt;116.0,765.0&gt;--&lt;116.0,768.0&gt;&gt;
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

* uni077D (U+077D): L&lt;&lt;636.0,1516.0&gt;--&lt;640.0,1515.0&gt;&gt;/B&lt;&lt;640.0,1515.0&gt;-&lt;635.0,1515.0&gt;-&lt;636.0,1516.0&gt;&gt; = 14.036243467926484

* uni077D.fina: L&lt;&lt;543.0,1516.0&gt;--&lt;547.0,1515.0&gt;&gt;/B&lt;&lt;547.0,1515.0&gt;-&lt;542.0,1515.0&gt;-&lt;543.0,1516.0&gt;&gt; = 14.036243467926484

* uni077D.init: L&lt;&lt;794.0,1516.0&gt;--&lt;798.0,1515.0&gt;&gt;/B&lt;&lt;798.0,1515.0&gt;-&lt;793.0,1515.0&gt;-&lt;794.0,1516.0&gt;&gt; = 14.036243467926484

* uni077D.medi: L&lt;&lt;681.0,1516.0&gt;--&lt;685.0,1515.0&gt;&gt;/B&lt;&lt;685.0,1515.0&gt;-&lt;680.0,1515.0&gt;-&lt;681.0,1516.0&gt;&gt; = 14.036243467926484

* uni08DB (U+08DB): L&lt;&lt;872.0,1028.0&gt;--&lt;872.0,1028.0&gt;&gt;/B&lt;&lt;872.0,1028.0&gt;-&lt;853.0,1029.0&gt;-&lt;841.5,1038.5&gt;&gt; = 3.012787504183286

* uni08DC (U+08DC): L&lt;&lt;825.0,1044.0&gt;--&lt;825.0,1044.0&gt;&gt;/B&lt;&lt;825.0,1044.0&gt;-&lt;792.0,1045.0&gt;-&lt;778.0,1059.0&gt;&gt; = 1.735704588928346

* uni08DD (U+08DD): L&lt;&lt;459.0,1047.0&gt;--&lt;459.0,1047.0&gt;&gt;/B&lt;&lt;459.0,1047.0&gt;-&lt;429.0,1049.0&gt;-&lt;415.0,1062.5&gt;&gt; = 3.8140748342903783

* uni200C (U+200C): B&lt;&lt;364.0,360.5&gt;-&lt;350.0,367.0&gt;-&lt;344.0,395.0&gt;&gt;/L&lt;&lt;344.0,395.0&gt;--&lt;344.0,393.0&gt;&gt; = 12.094757077012089
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

* uni03DE (U+03DE): L&lt;&lt;817.0,-121.0&gt;--&lt;821.0,438.0&gt;&gt;

* uni03DF (U+03DF): L&lt;&lt;817.0,-121.0&gt;--&lt;821.0,438.0&gt;&gt;

* uni0622.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0623.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0625.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0627.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0671.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0672.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0673.fina.alt: L&lt;&lt;910.0,368.0&gt;--&lt;1075.0,369.0&gt;&gt;

* uni0770 (U+0770): L&lt;&lt;329.0,1280.0&gt;--&lt;330.0,1786.0&gt;&gt;

* uni0770 (U+0770): L&lt;&lt;424.0,1786.0&gt;--&lt;426.0,1426.0&gt;&gt;

* uni0770.fina: L&lt;&lt;236.0,1280.0&gt;--&lt;237.0,1786.0&gt;&gt;

* uni0770.fina: L&lt;&lt;330.0,1786.0&gt;--&lt;333.0,1426.0&gt;&gt;

* uni0770.init: L&lt;&lt;487.0,1280.0&gt;--&lt;488.0,1786.0&gt;&gt;

* uni0770.init: L&lt;&lt;582.0,1786.0&gt;--&lt;584.0,1426.0&gt;&gt;

* uni0770.medi: L&lt;&lt;442.0,1278.0&gt;--&lt;443.0,1784.0&gt;&gt;

* uni0770.medi: L&lt;&lt;536.0,1784.0&gt;--&lt;539.0,1424.0&gt;&gt;

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
| 0 | 0 | 4 | 53 | 403 | 25 | 408 | 0 | 
| 0% | 0% | 0% | 6% | 45% | 3% | 46% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
