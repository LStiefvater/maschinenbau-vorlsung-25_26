# DHBW Brand Core

Authoritative source for the DHBW HTML UI skill — typography, colors, layout foundations, and brand rules.

---

## Typography

The preferred web typeface is **Source Sans 3** (Google Fonts).
It matches the clean, modern tone of the DHBW website and is freely available for lecture pages.

Fallback stack: `"Source Sans 3", "Arial", "Helvetica Neue", sans-serif`

Embed via Google Fonts:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
```

### Gewichte

| Gewicht | CSS-Wert | Verwendung |
|---------|----------|------------|
| Regular | 400 | Fließtext, Beschriftungen, Metadaten |
| SemiBold | 600 | Abschnittstitel, Kartentitel, Navigationspunkte |
| Bold | 700 | Seitentitel, Hauptüberschriften (H1) |

Kursiv nur bei semantischer Notwendigkeit (z. B. Fremdwörter, Begriffsdefinitionen).

### Schriftgrößen-Skala (für HTML-Lehrseiten)

| Rolle | Größe | Gewicht |
|-------|-------|---------|
| Seitentitel (H1) | 2rem – 2.5rem | Bold 700 |
| Abschnittstitel (H2) | 1.5rem – 1.75rem | SemiBold 600 |
| Untertitel / H3 | 1.125rem – 1.25rem | SemiBold 600 |
| Fließtext | 1rem (16px Basis) | Regular 400 |
| Sekundärtext, Metadaten | 0.875rem | Regular 400 |
| Code | 0.9rem | Monospace-Stack |

### Zeilenhöhe

- Fließtext: `1.65`
- Überschriften: `1.25`
- Code: `1.6`

---

## Color

### Official Core Palette

| Role | Value | Note |
|------|-------|------|
| DHBW Red (Primary) | `#E2001A` | Official DHBW corporate red |
| DHBW Red Dark (Hover/Active) | `#B50016` | Interactive states |
| DHBW Red Tint | `#FAE5E8` | Callouts, highlighted areas |
| Text Black | `#1A1A1A` | Main text |
| Secondary Gray | `#6B7280` | Metadata, supporting text |
| Border Gray | `#D1D5DB` | Dividers, borders |
| Canvas Light | `#F5F5F5` | Page background, panel BG |
| White | `#FFFFFF` | Card surfaces, main content BG |
| Code Dark | `#1E2936` | Code block background |
| Code Light | `#E8F0F7` | Inline code on white background |

### Color Rules

- DHBW Red is an identity color, not a full-page background for long text.
- Title pages / hero sections of a lecture slide may be entirely red (white text on top).
- Accent lines (border-left, underline, badge) always use `#E2001A`.
- Callout boxes: light red background `#FAE5E8` with a red left border.
- Code blocks: dark `#1E2936` background with light text.
- Use only grays from the defined palette; do not introduce custom gray values.

### Contrast Requirements (WCAG AA)

- White text on `#E2001A` ✓ (contrast > 4.5:1)
- `#1A1A1A` text on `#FFFFFF` ✓
- `#1A1A1A` text on `#F5F5F5` ✓
- Use `#6B7280` only for decorative secondary text and metadata, never for long body text.

---

## Layout Foundations

### Widths and Spacing

| Token | Value | Use case |
|-------|-------|----------|
| Max content width | `1200px` | Maximum content width |
| Slide width | `900px` | Recommended lecture slide width |
| Gutter (sides) | `24px–48px` | Side padding, mobile → desktop |
| Space XS | `4px` | Tight spacing, badges |
| Space S | `8px` | Small internal gaps |
| Space M | `16px` | Default spacing |
| Space L | `24px` | Sections within a component |
| Space XL | `32px` | Between sections |
| Space XXL | `48px` | Large page sections, hero padding |

### Border Radius

| Context | Value |
|---------|-------|
| Buttons, inputs | `6px` |
| Cards, panels | `8px` |
| Badges, tags | `4px` |
| Code blocks | `6px` |

### Shadows

- Card (default): `0 2px 8px rgba(0, 0, 0, 0.08)`
- Card (hover): `0 4px 16px rgba(0, 0, 0, 0.12)`
- No glassmorphism; no heavy drop shadows.

---

## Logo Rules

- Use the DHBW logo only in official file formats (SVG/PNG from the corporate design portal).
- Do not redraw or redesign the logo.
- Do not recolor the logo.
- Clear space: at least `20px` on all sides.
- On red backgrounds: use the white version of the logo (if available), otherwise place the logo against a calm, light area.
- Recommended placement: top-left corner in the page header or slide header.

---

## Brand Mood for Lecture Pages

HTML lecture pages and learning materials in the DHBW style should feel:

- **factual and clear** — academic, not promotional tone
- **structured** — clear hierarchy, unambiguous section boundaries
- **readable** — sufficient whitespace, clear contrast
- **modern but timeless** — no trends (glassmorphism, heavy gradients, neon)
- **red as an orientation color** — not as decoration

Lecture slides may have fully red title pages.
Content slides stay white with red accents (line, heading, button).
