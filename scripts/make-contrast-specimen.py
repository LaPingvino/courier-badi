#!/usr/bin/env python3
"""Emit a self-contained HTML specimen for the bonus Contrast (XOPQ) variable
font, with the font embedded as a base64 data URI and a live axis slider.

Usage: python3 scripts/make-contrast-specimen.py \
    fonts-contrast/webfonts/'CourierBadi-Contrast[XOPQ,ital,wght].woff2' \
    documentation/contrast-specimen.html
"""
import base64
import sys

woff2, out = sys.argv[1], sys.argv[2]
b64 = base64.b64encode(open(woff2, "rb").read()).decode("ascii")

HTML = """<title>Courier Badi — Contrast axis</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@font-face {
  font-family: "Courier Badi Contrast";
  src: url("data:font/woff2;base64,__B64__") format("woff2");
  font-weight: 400 700;
  font-stretch: 100%;
  font-display: swap;
}
:root {
  --paper: #edeae1;
  --ink: #201d19;
  --ink-soft: #6a635726;
  --line: #c9c3b5;
  --ribbon: #b1332b;
  --muted: #7a7264;
  --card: #f5f2ea;
  --xopq: 88;
  --wght: 400;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #17140f;
    --ink: #e9e3d6;
    --ink-soft: #e9e3d612;
    --line: #3a352c;
    --ribbon: #dd5244;
    --muted: #948b7a;
    --card: #1f1b15;
  }
}
:root[data-theme="light"] {
  --paper: #edeae1; --ink: #201d19; --line: #c9c3b5; --ribbon: #b1332b;
  --muted: #7a7264; --card: #f5f2ea; --ink-soft: #6a635726;
}
:root[data-theme="dark"] {
  --paper: #17140f; --ink: #e9e3d6; --line: #3a352c; --ribbon: #dd5244;
  --muted: #948b7a; --card: #1f1b15; --ink-soft: #e9e3d612;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 66rem; margin: 0 auto; padding: clamp(1.5rem, 4vw, 4rem) clamp(1.1rem, 4vw, 3rem) 5rem; }
.eyebrow {
  font-size: .72rem; letter-spacing: .32em; text-transform: uppercase;
  color: var(--ribbon); margin: 0 0 1.1rem; font-weight: 600;
  display: flex; align-items: center; gap: .7rem;
}
.eyebrow::before { content: ""; width: 1.6rem; height: 2px; background: var(--ribbon); display: inline-block; }
h1 {
  font-family: "Courier Badi Contrast", monospace;
  font-variation-settings: "wght" 700, "XOPQ" 130;
  font-weight: 700;
  font-size: clamp(2.3rem, 8vw, 4.6rem);
  line-height: 1.02; margin: 0 0 1rem; letter-spacing: -.01em;
  text-wrap: balance;
}
.lede { max-width: 44rem; color: var(--muted); font-size: 1rem; margin: 0 0 .4rem; }
.lede b { color: var(--ink); font-weight: 600; }

/* control panel */
.panel {
  margin: 2.6rem 0 1rem; padding: 1.5rem clamp(1.1rem,3vw,2rem);
  border: 1px solid var(--line); border-radius: 3px; background: var(--card);
  position: sticky; top: 0; z-index: 5;
  box-shadow: 0 1px 0 var(--line);
}
.controls { display: grid; gap: 1.4rem; grid-template-columns: 1fr 1fr; }
@media (max-width: 34rem) { .controls { grid-template-columns: 1fr; } }
.ctl label {
  display: flex; justify-content: space-between; align-items: baseline;
  font-size: .72rem; letter-spacing: .18em; text-transform: uppercase;
  color: var(--muted); margin-bottom: .55rem;
}
.ctl .val {
  font-variant-numeric: tabular-nums; color: var(--ribbon);
  font-weight: 600; letter-spacing: .04em; font-size: .85rem;
}
.ctl .cap { color: var(--muted); font-weight: 400; }
input[type=range] {
  -webkit-appearance: none; appearance: none; width: 100%; height: 2px;
  background: var(--line); border-radius: 2px; outline-offset: 4px;
}
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none; width: 18px; height: 18px; border-radius: 50%;
  background: var(--ribbon); cursor: pointer; border: 3px solid var(--paper);
  box-shadow: 0 0 0 1px var(--ribbon);
}
input[type=range]::-moz-range-thumb {
  width: 18px; height: 18px; border-radius: 50%; background: var(--ribbon);
  cursor: pointer; border: 3px solid var(--paper); box-shadow: 0 0 0 1px var(--ribbon);
}

/* live sample */
.stage {
  font-family: "Courier Badi Contrast", monospace;
  font-variation-settings: "wght" var(--wght), "XOPQ" var(--xopq);
  font-weight: 400;
  border-bottom: 1px solid var(--line);
  padding: 2rem 0 2.4rem;
}
.stage .rtl { direction: rtl; font-size: clamp(2.6rem, 12vw, 6rem); line-height: 1.35; margin: 0 0 .3rem; }
.stage .ltr { font-size: clamp(1.5rem, 5.2vw, 2.9rem); line-height: 1.3; margin: .2rem 0 0; }
.stage [contenteditable] { outline: none; }
.stage [contenteditable]:focus-visible { box-shadow: inset 0 -2px 0 var(--ribbon); }
.hint { font-size: .7rem; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); margin: 1.4rem 0 0; }
.hint b { color: var(--ribbon); font-weight: 600; }

/* comparison ladder */
.section-h {
  font-size: .72rem; letter-spacing: .28em; text-transform: uppercase;
  color: var(--muted); margin: 3rem 0 0; padding-top: 1.6rem;
  border-top: 1px solid var(--line);
}
.ladder { display: grid; gap: 0; margin-top: 1.2rem; }
.rung {
  display: grid; grid-template-columns: 5.5rem 1fr; align-items: center;
  gap: 1.2rem; padding: 1.1rem 0; border-bottom: 1px solid var(--line);
}
.rung .tag {
  font-size: .7rem; letter-spacing: .1em; color: var(--muted);
  font-variant-numeric: tabular-nums;
}
.rung .tag b { display: block; color: var(--ink); font-size: 1.15rem; letter-spacing: 0; }
.rung .demo {
  font-family: "Courier Badi Contrast", monospace; font-weight: 400;
  font-size: clamp(1.8rem, 6vw, 3rem); line-height: 1; direction: rtl;
  overflow-x: auto;
}
.rung .demo.ltr { direction: ltr; font-size: clamp(1.3rem, 4.5vw, 2.1rem); }

footer {
  margin-top: 3.4rem; padding-top: 1.5rem; border-top: 1px solid var(--line);
  color: var(--muted); font-size: .8rem; line-height: 1.7;
}
footer b { color: var(--ink); font-weight: 600; }
footer .meta { display: flex; flex-wrap: wrap; gap: .4rem 1.6rem; margin-top: .8rem; font-variant-numeric: tabular-nums; }
footer .meta span::before { content: "· "; color: var(--ribbon); }
@media (prefers-reduced-motion: no-preference) {
  .stage, h1, .rung .demo { transition: font-variation-settings .12s linear; }
}
</style>

<div class="wrap">
  <p class="eyebrow">Courier Badi · bonus axis</p>
  <h1>Contrast</h1>
  <p class="lede"><b>XOPQ</b> tunes the vertical-stroke thickness. It grew out of
  the Bold: emboldening offsets each stroke outward, and when the horizontal
  offset outruns the vertical one the verticals fatten while the crossbars stay
  lean — modulation on a typewriter face. This axis exposes that imbalance as a
  continuous control, from an even monoline to full contrast.</p>
  <p class="lede">Drag the sliders. It reads loudest on the Arabic
  <b>seen / sheen / sad</b> teeth and on upright Latin stems.</p>

  <div class="panel">
    <div class="controls">
      <div class="ctl">
        <label for="xopq"><span>Contrast · XOPQ</span>
          <span class="val"><span id="xv">88</span> <span class="cap">/ even</span></span></label>
        <input id="xopq" type="range" min="88" max="130" value="88" step="1">
      </div>
      <div class="ctl">
        <label for="wght"><span>Weight · wght</span>
          <span class="val"><span id="wv">400</span> <span class="cap">/ regular</span></span></label>
        <input id="wght" type="range" min="400" max="700" value="400" step="1">
      </div>
    </div>
  </div>

  <div class="stage">
    <p class="rtl" contenteditable spellcheck="false" dir="rtl">شمس سلسبيل صحّة</p>
    <p class="ltr" contenteditable spellcheck="false">Handgloves &amp; typewriter 0123</p>
  </div>
  <p class="hint">The two lines above are <b>editable</b> — type your own text to test it.</p>

  <p class="section-h">The same word across the axis</p>
  <div class="ladder">
    <div class="rung">
      <div class="tag">XOPQ<b>88</b>even</div>
      <div class="demo" style="font-variation-settings:'wght' 400,'XOPQ' 88">شمس</div>
    </div>
    <div class="rung">
      <div class="tag">XOPQ<b>102</b>+</div>
      <div class="demo" style="font-variation-settings:'wght' 400,'XOPQ' 102">شمس</div>
    </div>
    <div class="rung">
      <div class="tag">XOPQ<b>116</b>++</div>
      <div class="demo" style="font-variation-settings:'wght' 400,'XOPQ' 116">شمس</div>
    </div>
    <div class="rung">
      <div class="tag">XOPQ<b>130</b>full</div>
      <div class="demo" style="font-variation-settings:'wght' 400,'XOPQ' 130">شمس</div>
    </div>
    <div class="rung">
      <div class="tag">Latin<b>88</b>even</div>
      <div class="demo ltr" style="font-variation-settings:'wght' 400,'XOPQ' 88">Millinur</div>
    </div>
    <div class="rung">
      <div class="tag">Latin<b>130</b>full</div>
      <div class="demo ltr" style="font-variation-settings:'wght' 400,'XOPQ' 130">Millinur</div>
    </div>
  </div>

  <footer>
    <b>Bonus / experimental.</b> This contrast axis ships as a release-only extra,
    separate from the Google-Fonts submission (a clean <b>wght + ital</b> family).
    It reuses the directional emboldening from <code>make-bold&nbsp;--contrast</code>,
    mapped onto the registered parametric <b>XOPQ</b> (vertical stroke thickness) axis.
    <div class="meta">
      <span>Family: Courier Badi</span>
      <span>Axes: wght 400–700 · XOPQ 88–130</span>
      <span>Monospace · UPM 2048</span>
    </div>
  </footer>
</div>

<script>
(function () {
  var root = document.documentElement;
  function bind(id, out, cssvar) {
    var el = document.getElementById(id), o = document.getElementById(out);
    function upd() { root.style.setProperty(cssvar, el.value); o.textContent = el.value; }
    el.addEventListener("input", upd); upd();
  }
  bind("xopq", "xv", "--xopq");
  bind("wght", "wv", "--wght");
})();
</script>
"""

open(out, "w").write(HTML.replace("__B64__", b64))
print("wrote", out, "(%d KB)" % (len(HTML) // 1024 + len(b64) // 1024))
