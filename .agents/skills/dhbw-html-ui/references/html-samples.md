# DHBW HTML Samples

Implementation-ready CSS tokens, HTML templates, and components for DHBW lecture pages.

---

## Semantic Design Tokens

### Full CSS Custom Properties

```css
/* ===== DHBW Design Tokens ===== */
:root {
  /* Typografie */
  --dhbw-font-family: "Source Sans 3", "Arial", "Helvetica Neue", sans-serif;
  --dhbw-font-mono: "Fira Code", "Cascadia Code", "Consolas", "Courier New", monospace;
  --dhbw-font-weight-regular: 400;
  --dhbw-font-weight-semibold: 600;
  --dhbw-font-weight-bold: 700;

  /* Schriftgrößen */
  --dhbw-font-size-xs:  0.75rem;   /* 12px — Badges, Labels */
  --dhbw-font-size-sm:  0.875rem;  /* 14px — Metadaten, Sekundärtext */
  --dhbw-font-size-base: 1rem;     /* 16px — Fließtext */
  --dhbw-font-size-md:  1.125rem;  /* 18px — Einleitung, H3 */
  --dhbw-font-size-lg:  1.5rem;    /* 24px — H2 */
  --dhbw-font-size-xl:  2rem;      /* 32px — H1 */
  --dhbw-font-size-2xl: 2.5rem;    /* 40px — Hero-Titel */

  /* Zeilenhöhe */
  --dhbw-line-height-body: 1.65;
  --dhbw-line-height-heading: 1.25;
  --dhbw-line-height-code: 1.6;

  /* DHBW-Farben */
  --dhbw-color-red:           #E2001A;   /* DHBW Rot – Primärfarbe */
  --dhbw-color-red-dark:      #B50016;   /* Hover, aktive Zustände */
  --dhbw-color-red-tint:      #FAE5E8;   /* Callout-Hintergründe */
  --dhbw-color-red-mid:       #F0B3BB;   /* Akkzentlinie hell */

  /* Neutrale Farben */
  --dhbw-color-text:          #1A1A1A;   /* Haupttext */
  --dhbw-color-text-secondary: #6B7280;  /* Metadaten, Sekundärtext */
  --dhbw-color-border:        #D1D5DB;   /* Trennlinien, Rahmen */
  --dhbw-color-canvas:        #F5F5F5;   /* Seitenhintergrund */
  --dhbw-color-surface:       #FFFFFF;   /* Cards, content surfaces */

  /* Code */
  --dhbw-color-code-bg:       #1E2936;   /* Code-Block Hintergrund */
  --dhbw-color-code-bg-inline: #E8F0F7;  /* Inline-Code auf Weiß */
  --dhbw-color-code-text:     #E8EFF5;   /* Text im dunklen Code-Block */
  --dhbw-color-code-comment:  #7A9CB3;   /* Kommentare im Code */
  --dhbw-color-code-keyword:  #F97316;   /* Keywords */
  --dhbw-color-code-string:   #22C55E;   /* Strings */
  --dhbw-color-code-number:   #60A5FA;   /* Zahlen */

  /* Abstände */
  --dhbw-space-1:  4px;
  --dhbw-space-2:  8px;
  --dhbw-space-3:  12px;
  --dhbw-space-4:  16px;
  --dhbw-space-5:  24px;
  --dhbw-space-6:  32px;
  --dhbw-space-7:  48px;

  /* Border-Radius */
  --dhbw-radius-sm:     4px;   /* Badges, Tags */
  --dhbw-radius-base:   6px;   /* Buttons, Inputs, Code */
  --dhbw-radius-card:   8px;   /* Karten, Panels */

  /* Schatten */
  --dhbw-shadow-card:   0 2px 8px rgba(0,0,0,0.08);
  --dhbw-shadow-raised: 0 4px 16px rgba(0,0,0,0.12);

  /* Layout */
  --dhbw-max-width: 1200px;
  --dhbw-slide-width: 900px;
  --dhbw-gutter: clamp(16px, 4vw, 48px);
}
```

---

## Base Reset and Page Shell

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DHBW Lecture — Title</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    /* DHBW Tokens hier einfügen oder als separate dhbw.css einbinden */

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--dhbw-font-family);
      font-size: var(--dhbw-font-size-base);
      line-height: var(--dhbw-line-height-body);
      color: var(--dhbw-color-text);
      background: var(--dhbw-color-canvas);
    }
    h1, h2, h3, h4 { line-height: var(--dhbw-line-height-heading); }
    h1 { font-size: var(--dhbw-font-size-xl); font-weight: var(--dhbw-font-weight-bold); }
    h2 { font-size: var(--dhbw-font-size-lg); font-weight: var(--dhbw-font-weight-semibold); }
    h3 { font-size: var(--dhbw-font-size-md); font-weight: var(--dhbw-font-weight-semibold); }
    a { color: var(--dhbw-color-red); text-decoration: none; }
    a:hover { color: var(--dhbw-color-red-dark); text-decoration: underline; }
  </style>
</head>
<body>
  <!-- Header, Slides, Footer hier -->
</body>
</html>
```

---

## Page Header (Navigation)

```html
<header class="dhbw-header">
  <div class="dhbw-header__inner">
    <a href="/" class="dhbw-header__logo" aria-label="DHBW Stuttgart – Home">
      <!-- SVG-Logo oder img-Tag hier -->
      <span class="dhbw-header__logo-text">DHBW Stuttgart</span>
    </a>
    <nav class="dhbw-header__nav" aria-label="Hauptnavigation">
      <a href="#" class="dhbw-header__nav-link dhbw-header__nav-link--active">Lecture</a>
      <a href="#" class="dhbw-header__nav-link">Exercises</a>
      <a href="#" class="dhbw-header__nav-link">Solutions</a>
    </nav>
  </div>
</header>

<style>
.dhbw-header {
  background: var(--dhbw-color-surface);
  border-bottom: 3px solid var(--dhbw-color-red);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: var(--dhbw-shadow-card);
}
.dhbw-header__inner {
  max-width: var(--dhbw-max-width);
  margin: 0 auto;
  padding: var(--dhbw-space-3) var(--dhbw-gutter);
  display: flex;
  align-items: center;
  gap: var(--dhbw-space-6);
}
.dhbw-header__logo {
  display: flex;
  align-items: center;
  gap: var(--dhbw-space-2);
  text-decoration: none;
}
.dhbw-header__logo-text {
  font-size: var(--dhbw-font-size-md);
  font-weight: var(--dhbw-font-weight-bold);
  color: var(--dhbw-color-red);
  letter-spacing: -0.01em;
}
.dhbw-header__nav {
  display: flex;
  gap: var(--dhbw-space-5);
  margin-left: auto;
}
.dhbw-header__nav-link {
  font-size: var(--dhbw-font-size-base);
  font-weight: var(--dhbw-font-weight-semibold);
  color: var(--dhbw-color-text);
  text-decoration: none;
  padding-bottom: var(--dhbw-space-1);
  border-bottom: 2px solid transparent;
  transition: color 0.15s, border-color 0.15s;
}
.dhbw-header__nav-link:hover,
.dhbw-header__nav-link--active {
  color: var(--dhbw-color-red);
  border-bottom-color: var(--dhbw-color-red);
}
</style>
```

---

## Title Slide / Hero Section

Used for the first page of a lecture or a new topic block.

```html
<section class="dhbw-hero">
  <div class="dhbw-hero__inner">
    <p class="dhbw-hero__label">Lecture 01 · Computer Science for Mechanical Engineering</p>
    <h1 class="dhbw-hero__title">Binary Number System</h1>
    <p class="dhbw-hero__subtitle">Fundamentals of digital number representation</p>
    <div class="dhbw-hero__meta">
      <span>DHBW Stuttgart · WS 2025/26</span>
    </div>
  </div>
</section>

<style>
.dhbw-hero {
  background: var(--dhbw-color-red);
  color: #FFFFFF;
  padding: var(--dhbw-space-7) var(--dhbw-gutter);
}
.dhbw-hero__inner {
  max-width: var(--dhbw-slide-width);
  margin: 0 auto;
}
.dhbw-hero__label {
  font-size: var(--dhbw-font-size-sm);
  font-weight: var(--dhbw-font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  opacity: 0.85;
  margin-bottom: var(--dhbw-space-3);
}
.dhbw-hero__title {
  font-size: var(--dhbw-font-size-2xl);
  font-weight: var(--dhbw-font-weight-bold);
  line-height: 1.15;
  margin-bottom: var(--dhbw-space-3);
  color: #FFFFFF;
}
.dhbw-hero__subtitle {
  font-size: var(--dhbw-font-size-lg);
  font-weight: var(--dhbw-font-weight-regular);
  opacity: 0.9;
  margin-bottom: var(--dhbw-space-5);
}
.dhbw-hero__meta {
  font-size: var(--dhbw-font-size-sm);
  opacity: 0.75;
}
</style>
```

---

## Content Slide

Standard layout for a lecture content page.

```html
<section class="dhbw-slide">
  <div class="dhbw-slide__inner">
    <header class="dhbw-slide__header">
      <span class="dhbw-slide__number">01</span>
      <h2 class="dhbw-slide__title">Was ist ein Binärsystem?</h2>
    </header>
    <div class="dhbw-slide__body">
  <p>In the binary system, numbers are represented using only two digits: <strong>0</strong> and <strong>1</strong>.</p>
      <p>Each position has the value of a power of two (2<sup>n</sup>).</p>
    </div>
  </div>
</section>

<style>
.dhbw-slide {
  background: var(--dhbw-color-surface);
  padding: var(--dhbw-space-7) var(--dhbw-gutter);
  min-height: 60vh;
}
.dhbw-slide__inner {
  max-width: var(--dhbw-slide-width);
  margin: 0 auto;
}
.dhbw-slide__header {
  display: flex;
  align-items: baseline;
  gap: var(--dhbw-space-4);
  border-left: 4px solid var(--dhbw-color-red);
  padding-left: var(--dhbw-space-4);
  margin-bottom: var(--dhbw-space-6);
}
.dhbw-slide__number {
  font-size: var(--dhbw-font-size-2xl);
  font-weight: var(--dhbw-font-weight-bold);
  color: var(--dhbw-color-red);
  line-height: 1;
  min-width: 2.5ch;
}
.dhbw-slide__title {
  font-size: var(--dhbw-font-size-xl);
  font-weight: var(--dhbw-font-weight-bold);
  color: var(--dhbw-color-text);
}
.dhbw-slide__body {
  font-size: var(--dhbw-font-size-base);
  line-height: var(--dhbw-line-height-body);
}
.dhbw-slide__body p + p { margin-top: var(--dhbw-space-4); }
.dhbw-slide__body strong { font-weight: var(--dhbw-font-weight-semibold); color: var(--dhbw-color-text); }
</style>
```

---

## Two-Column Layout (Theory + Example)

```html
<div class="dhbw-columns">
  <div class="dhbw-columns__item">
    <h3>Concept</h3>
    <p>Theory text …</p>
  </div>
  <div class="dhbw-columns__item">
    <h3>Example</h3>
    <p>Concrete example …</p>
  </div>
</div>

<style>
.dhbw-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--dhbw-space-6);
  margin-top: var(--dhbw-space-5);
}
@media (max-width: 640px) {
  .dhbw-columns { grid-template-columns: 1fr; }
}
.dhbw-columns__item {
  background: var(--dhbw-color-canvas);
  border-radius: var(--dhbw-radius-card);
  padding: var(--dhbw-space-5);
}
.dhbw-columns__item h3 {
  color: var(--dhbw-color-red);
  margin-bottom: var(--dhbw-space-3);
}
</style>
```

---

## Code Block

```html
<pre class="dhbw-code"><code class="dhbw-code__content"><span class="kw">def</span> <span class="fn">decimal_to_binary</span>(n: <span class="tp">int</span>) -> <span class="tp">str</span>:
    <span class="cm">"""Converts a decimal number to its binary string representation."""</span>
    <span class="kw">if</span> n == <span class="nm">0</span>:
        <span class="kw">return</span> <span class="st">"0"</span>
    bits = []
    <span class="kw">while</span> n > <span class="nm">0</span>:
        bits.append(<span class="tp">str</span>(n % <span class="nm">2</span>))
        n //= <span class="nm">2</span>
    <span class="kw">return</span> <span class="st">""</span>.join(<span class="bi">reversed</span>(bits))</code></pre>

<style>
.dhbw-code {
  background: var(--dhbw-color-code-bg);
  color: var(--dhbw-color-code-text);
  font-family: var(--dhbw-font-mono);
  font-size: var(--dhbw-font-size-sm);
  line-height: var(--dhbw-line-height-code);
  padding: var(--dhbw-space-5);
  border-radius: var(--dhbw-radius-base);
  overflow-x: auto;
  margin: var(--dhbw-space-5) 0;
  border-left: 4px solid var(--dhbw-color-red);
  tab-size: 4;
}
.dhbw-code__content { display: block; }

/* Syntax-Highlighting-Klassen */
.dhbw-code .kw { color: #F97316; font-weight: var(--dhbw-font-weight-semibold); } /* Keywords */
.dhbw-code .fn { color: #60A5FA; }   /* Funktionsnamen */
.dhbw-code .tp { color: #34D399; }   /* Typen */
.dhbw-code .st { color: #22C55E; }   /* Strings */
.dhbw-code .nm { color: #A78BFA; }   /* Zahlen */
.dhbw-code .cm { color: #7A9CB3; font-style: italic; } /* Kommentare */
.dhbw-code .bi { color: #F9A8D4; }   /* Builtins */
</style>
```

### Inline Code

```html
<p>Die Variable <code class="dhbw-inline-code">n</code> enthält den Eingabewert.</p>

<style>
.dhbw-inline-code {
  background: var(--dhbw-color-code-bg-inline);
  color: var(--dhbw-color-red-dark);
  font-family: var(--dhbw-font-mono);
  font-size: 0.875em;
  padding: 0.1em 0.4em;
  border-radius: var(--dhbw-radius-sm);
}
</style>
```

---

## Callout / Info Box

```html
<!-- Note (default) -->
<div class="dhbw-callout">
  <strong class="dhbw-callout__label">Note</strong>
  <p>The binary system is the foundation of all digital systems.</p>
</div>

<!-- Important (highlighted) -->
<div class="dhbw-callout dhbw-callout--important">
  <strong class="dhbw-callout__label">Important</strong>
  <p>Every decimal number can be uniquely converted to a binary number.</p>
</div>

<!-- Example -->
<div class="dhbw-callout dhbw-callout--example">
  <strong class="dhbw-callout__label">Example</strong>
  <p>13<sub>10</sub> = 1101<sub>2</sub></p>
</div>

<style>
.dhbw-callout {
  background: var(--dhbw-color-red-tint);
  border-left: 4px solid var(--dhbw-color-red);
  border-radius: 0 var(--dhbw-radius-base) var(--dhbw-radius-base) 0;
  padding: var(--dhbw-space-4) var(--dhbw-space-5);
  margin: var(--dhbw-space-5) 0;
}
.dhbw-callout__label {
  display: block;
  font-size: var(--dhbw-font-size-sm);
  font-weight: var(--dhbw-font-weight-bold);
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--dhbw-color-red);
  margin-bottom: var(--dhbw-space-2);
}
.dhbw-callout p { margin: 0; font-size: var(--dhbw-font-size-base); }

.dhbw-callout--important {
  background: var(--dhbw-color-red-tint);
  border-left-color: var(--dhbw-color-red-dark);
}
.dhbw-callout--example {
  background: #EFF6FF;
  border-left-color: #3B82F6;
}
.dhbw-callout--example .dhbw-callout__label { color: #1D4ED8; }
</style>
```

---

## Table

```html
<div class="dhbw-table-wrap">
  <table class="dhbw-table">
    <thead>
      <tr>
        <th>Decimal</th>
        <th>Binary</th>
        <th>Hexadecimal</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>0000</td><td>0</td></tr>
      <tr><td>8</td><td>1000</td><td>8</td></tr>
      <tr><td>15</td><td>1111</td><td>F</td></tr>
      <tr><td>255</td><td>1111 1111</td><td>FF</td></tr>
    </tbody>
  </table>
</div>

<style>
.dhbw-table-wrap { overflow-x: auto; margin: var(--dhbw-space-5) 0; }
.dhbw-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--dhbw-font-size-base);
}
.dhbw-table thead tr {
  background: var(--dhbw-color-red);
  color: #FFFFFF;
}
.dhbw-table th {
  padding: var(--dhbw-space-3) var(--dhbw-space-4);
  text-align: left;
  font-weight: var(--dhbw-font-weight-semibold);
  font-size: var(--dhbw-font-size-sm);
  letter-spacing: 0.03em;
}
.dhbw-table td {
  padding: var(--dhbw-space-3) var(--dhbw-space-4);
  border-bottom: 1px solid var(--dhbw-color-border);
  font-family: var(--dhbw-font-mono);
  font-size: var(--dhbw-font-size-sm);
}
.dhbw-table tbody tr:nth-child(even) { background: var(--dhbw-color-canvas); }
.dhbw-table tbody tr:hover { background: var(--dhbw-color-red-tint); }
</style>
```

---

## Buttons

```html
<!-- Primary (red, filled) -->
<a href="#" class="dhbw-btn dhbw-btn--primary">Next →</a>

<!-- Secondary (outline) -->
<a href="#" class="dhbw-btn dhbw-btn--outline">Show solutions</a>

<!-- Ghost (subtle, for slide navigation) -->
<a href="#" class="dhbw-btn dhbw-btn--ghost">← Back</a>

<style>
.dhbw-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--dhbw-space-2);
  padding: var(--dhbw-space-3) var(--dhbw-space-5);
  border-radius: var(--dhbw-radius-base);
  font-family: var(--dhbw-font-family);
  font-size: var(--dhbw-font-size-base);
  font-weight: var(--dhbw-font-weight-semibold);
  text-decoration: none;
  cursor: pointer;
  border: 2px solid transparent;
  transition: background 0.15s, color 0.15s, border-color 0.15s;
}
.dhbw-btn--primary {
  background: var(--dhbw-color-red);
  color: #FFFFFF;
  border-color: var(--dhbw-color-red);
}
.dhbw-btn--primary:hover {
  background: var(--dhbw-color-red-dark);
  border-color: var(--dhbw-color-red-dark);
  color: #FFFFFF;
  text-decoration: none;
}
.dhbw-btn--outline {
  background: transparent;
  color: var(--dhbw-color-red);
  border-color: var(--dhbw-color-red);
}
.dhbw-btn--outline:hover {
  background: var(--dhbw-color-red-tint);
  text-decoration: none;
}
.dhbw-btn--ghost {
  background: transparent;
  color: var(--dhbw-color-text-secondary);
  border-color: var(--dhbw-color-border);
}
.dhbw-btn--ghost:hover {
  background: var(--dhbw-color-canvas);
  color: var(--dhbw-color-text);
  text-decoration: none;
}
</style>
```

---

## Slide Navigation

```html
<nav class="dhbw-slide-nav" aria-label="Slide Navigation">
  <a href="previous-slide.html" class="dhbw-btn dhbw-btn--ghost">← Previous</a>
  <span class="dhbw-slide-nav__indicator">Slide 3 / 12</span>
  <a href="next-slide.html" class="dhbw-btn dhbw-btn--primary">Next →</a>
</nav>

<style>
.dhbw-slide-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--dhbw-space-5) var(--dhbw-gutter);
  max-width: var(--dhbw-slide-width);
  margin: 0 auto;
  border-top: 1px solid var(--dhbw-color-border);
}
.dhbw-slide-nav__indicator {
  font-size: var(--dhbw-font-size-sm);
  color: var(--dhbw-color-text-secondary);
  font-weight: var(--dhbw-font-weight-semibold);
}
</style>
```

---

## Card Grid (e.g. Topic Overview / Table of Contents)

```html
<div class="dhbw-card-grid">
  <article class="dhbw-card">
    <div class="dhbw-card__num">V01</div>
    <h3 class="dhbw-card__title">Binary Number System</h3>
    <p class="dhbw-card__desc">Fundamentals of digital number representation, conversion</p>
    <a href="v01.html" class="dhbw-btn dhbw-btn--outline" style="margin-top: auto;">View Lecture</a>
  </article>
  <!-- weitere Karten … -->
</div>

<style>
.dhbw-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: var(--dhbw-space-5);
  margin: var(--dhbw-space-6) 0;
}
.dhbw-card {
  background: var(--dhbw-color-surface);
  border-radius: var(--dhbw-radius-card);
  padding: var(--dhbw-space-5);
  display: flex;
  flex-direction: column;
  gap: var(--dhbw-space-3);
  box-shadow: var(--dhbw-shadow-card);
  border-top: 3px solid var(--dhbw-color-red);
  transition: box-shadow 0.15s, transform 0.15s;
}
.dhbw-card:hover {
  box-shadow: var(--dhbw-shadow-raised);
  transform: translateY(-2px);
}
.dhbw-card__num {
  font-size: var(--dhbw-font-size-xs);
  font-weight: var(--dhbw-font-weight-bold);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--dhbw-color-red);
}
.dhbw-card__title {
  font-size: var(--dhbw-font-size-md);
  font-weight: var(--dhbw-font-weight-semibold);
  color: var(--dhbw-color-text);
}
.dhbw-card__desc {
  font-size: var(--dhbw-font-size-sm);
  color: var(--dhbw-color-text-secondary);
  flex: 1;
}
</style>
```

---

## Learning Objectives List (bullet list with red marker)

```html
<ul class="dhbw-list">
  <li>Convert decimal numbers to binary</li>
  <li>Perform binary addition</li>
  <li>Explain the difference between signed and unsigned numbers</li>
</ul>

<style>
.dhbw-list {
  list-style: none;
  padding: 0;
  margin: var(--dhbw-space-4) 0;
  display: flex;
  flex-direction: column;
  gap: var(--dhbw-space-3);
}
.dhbw-list li {
  display: flex;
  align-items: flex-start;
  gap: var(--dhbw-space-3);
  font-size: var(--dhbw-font-size-base);
  line-height: var(--dhbw-line-height-body);
}
.dhbw-list li::before {
  content: "";
  display: block;
  min-width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--dhbw-color-red);
  margin-top: 0.5em;
  flex-shrink: 0;
}
</style>
```

---

## Footer

```html
<footer class="dhbw-footer">
  <div class="dhbw-footer__inner">
    <span class="dhbw-footer__org">DHBW Stuttgart · Mechanical Engineering</span>
    <span class="dhbw-footer__copy">© 2025/26 · Lecture materials</span>
  </div>
</footer>

<style>
.dhbw-footer {
  background: var(--dhbw-color-red);
  color: rgba(255,255,255,0.85);
  padding: var(--dhbw-space-5) var(--dhbw-gutter);
  margin-top: var(--dhbw-space-7);
}
.dhbw-footer__inner {
  max-width: var(--dhbw-max-width);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--dhbw-space-3);
  font-size: var(--dhbw-font-size-sm);
}
.dhbw-footer__org { font-weight: var(--dhbw-font-weight-semibold); color: #FFFFFF; }
</style>
```

---

## Complete Page Template (all tokens + example slide)

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>V01 – Binary Number System | DHBW Stuttgart</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --dhbw-font-family: "Source Sans 3", Arial, "Helvetica Neue", sans-serif;
      --dhbw-font-mono: "Fira Code", Consolas, "Courier New", monospace;
      --dhbw-font-weight-regular: 400;
      --dhbw-font-weight-semibold: 600;
      --dhbw-font-weight-bold: 700;
      --dhbw-font-size-xs: 0.75rem;
      --dhbw-font-size-sm: 0.875rem;
      --dhbw-font-size-base: 1rem;
      --dhbw-font-size-md: 1.125rem;
      --dhbw-font-size-lg: 1.5rem;
      --dhbw-font-size-xl: 2rem;
      --dhbw-font-size-2xl: 2.5rem;
      --dhbw-line-height-body: 1.65;
      --dhbw-line-height-heading: 1.25;
      --dhbw-line-height-code: 1.6;
      --dhbw-color-red: #E2001A;
      --dhbw-color-red-dark: #B50016;
      --dhbw-color-red-tint: #FAE5E8;
      --dhbw-color-text: #1A1A1A;
      --dhbw-color-text-secondary: #6B7280;
      --dhbw-color-border: #D1D5DB;
      --dhbw-color-canvas: #F5F5F5;
      --dhbw-color-surface: #FFFFFF;
      --dhbw-color-code-bg: #1E2936;
      --dhbw-color-code-bg-inline: #E8F0F7;
      --dhbw-color-code-text: #E8EFF5;
      --dhbw-space-1: 4px; --dhbw-space-2: 8px; --dhbw-space-3: 12px;
      --dhbw-space-4: 16px; --dhbw-space-5: 24px; --dhbw-space-6: 32px;
      --dhbw-space-7: 48px;
      --dhbw-radius-sm: 4px; --dhbw-radius-base: 6px; --dhbw-radius-card: 8px;
      --dhbw-shadow-card: 0 2px 8px rgba(0,0,0,0.08);
      --dhbw-shadow-raised: 0 4px 16px rgba(0,0,0,0.12);
      --dhbw-max-width: 1200px;
      --dhbw-slide-width: 900px;
      --dhbw-gutter: clamp(16px, 4vw, 48px);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: var(--dhbw-font-family); font-size: var(--dhbw-font-size-base);
      line-height: var(--dhbw-line-height-body); color: var(--dhbw-color-text);
      background: var(--dhbw-color-canvas); }
    h1,h2,h3 { line-height: var(--dhbw-line-height-heading); }
    a { color: var(--dhbw-color-red); }
    a:hover { color: var(--dhbw-color-red-dark); }
  </style>
</head>
<body>

  <!-- Header -->
  <header style="background:#fff; border-bottom:3px solid var(--dhbw-color-red);
    padding: var(--dhbw-space-3) var(--dhbw-gutter); display:flex; align-items:center;
    gap: var(--dhbw-space-6); position:sticky; top:0; z-index:100;
    box-shadow: var(--dhbw-shadow-card);">
    <span style="font-size:var(--dhbw-font-size-md); font-weight:700;
      color:var(--dhbw-color-red);">DHBW Stuttgart</span>
    <nav style="margin-left:auto; display:flex; gap:var(--dhbw-space-5);">
      <a href="#" style="font-weight:600; color:var(--dhbw-color-red);
        text-decoration:none; border-bottom:2px solid var(--dhbw-color-red);
        padding-bottom:2px;">Lecture</a>
      <a href="#" style="font-weight:600; color:var(--dhbw-color-text);
        text-decoration:none;">Exercises</a>
    </nav>
  </header>

  <!-- Hero -->
  <section style="background:var(--dhbw-color-red); color:#fff;
    padding:var(--dhbw-space-7) var(--dhbw-gutter);">
    <div style="max-width:var(--dhbw-slide-width); margin:0 auto;">
      <p style="font-size:var(--dhbw-font-size-sm); font-weight:700; text-transform:uppercase;
        letter-spacing:0.08em; opacity:0.8; margin-bottom:var(--dhbw-space-3);">
        Lecture 01 · WS 2025/26
      </p>
      <h1 style="font-size:var(--dhbw-font-size-2xl); font-weight:700; color:#fff;
        margin-bottom:var(--dhbw-space-3);">Binary Number System</h1>
      <p style="font-size:var(--dhbw-font-size-lg); opacity:0.9;">
        Fundamentals of digital number representation
      </p>
    </div>
  </section>

  <!-- Content -->
  <main style="max-width:var(--dhbw-slide-width); margin:0 auto;
    padding:var(--dhbw-space-7) var(--dhbw-gutter);">

    <div style="border-left:4px solid var(--dhbw-color-red);
      padding-left:var(--dhbw-space-4); margin-bottom:var(--dhbw-space-6);">
      <h2 style="font-size:var(--dhbw-font-size-xl); font-weight:700;">
        What is a Binary System?
      </h2>
    </div>

    <p>In the binary system, numbers are represented using only two digits: <strong>0</strong> and <strong>1</strong>.</p>

    <div style="background:var(--dhbw-color-red-tint); border-left:4px solid var(--dhbw-color-red);
      border-radius:0 var(--dhbw-radius-base) var(--dhbw-radius-base) 0;
      padding:var(--dhbw-space-4) var(--dhbw-space-5); margin:var(--dhbw-space-5) 0;">
      <strong style="display:block; font-size:var(--dhbw-font-size-sm); font-weight:700;
        text-transform:uppercase; letter-spacing:0.07em; color:var(--dhbw-color-red);
        margin-bottom:var(--dhbw-space-2);">Example</strong>
      <p>13<sub>10</sub> = 1101<sub>2</sub></p>
    </div>

    <pre style="background:var(--dhbw-color-code-bg); color:var(--dhbw-color-code-text);
      font-family:var(--dhbw-font-mono); font-size:var(--dhbw-font-size-sm);
      line-height:var(--dhbw-line-height-code); padding:var(--dhbw-space-5);
      border-radius:var(--dhbw-radius-base); overflow-x:auto;
      margin:var(--dhbw-space-5) 0; border-left:4px solid var(--dhbw-color-red);">
<code>13 / 2 = 6  remainder 1
 6 / 2 = 3  remainder 0
 3 / 2 = 1  remainder 1
 1 / 2 = 0  remainder 1
→ 1101₂</code></pre>

  </main>

  <!-- Footer -->
  <footer style="background:var(--dhbw-color-red); color:rgba(255,255,255,0.85);
    padding:var(--dhbw-space-5) var(--dhbw-gutter); margin-top:var(--dhbw-space-7);">
    <div style="max-width:var(--dhbw-max-width); margin:0 auto;
      display:flex; justify-content:space-between; font-size:var(--dhbw-font-size-sm);">
      <span style="font-weight:700; color:#fff;">DHBW Stuttgart · Mechanical Engineering</span>
      <span>© 2025/26</span>
    </div>
  </footer>

</body>
</html>
```
