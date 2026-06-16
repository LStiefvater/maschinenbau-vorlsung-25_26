---
name: dhbw-html-ui
description: >
  Design and generate HTML pages in the DHBW Stuttgart corporate style.
  Use whenever the user mentions DHBW, Duale Hochschule, lecture slide, Lehrfolie, Vorlesungsseite,
  Skript, Übungsblatt, Aufgabenblatt, Lernunterlage, HTML in DHBW style,
  DHBW design, DHBW layout, DHBW colors, Maschinenbau lecture, Informatik lecture,
  red accent color for university page, or when an HTML page in the style of dhbw-stuttgart.de
  should be created or reviewed.
applyTo:
  - "**/*.html"
  - "lessons/**"
  - "schiffeversenken/**"
---

# DHBW HTML UI

This skill encapsulates the DHBW Stuttgart corporate design for HTML lecture pages and learning materials.
It applies to the `maschinenbau-vorlsung-25_26` lecture project and to any request to create or review
HTML in the DHBW style.

Response language: match the user's language. Default to German when the user writes in German.

---

## Read These References

- Read [references/brand-core.md](references/brand-core.md) for typography, color palette, layout tokens, and logo rules.
- Read [references/html-samples.md](references/html-samples.md) when the user needs HTML, CSS, full page templates,
  code blocks, tables, callouts, cards, buttons, or navigation components.

---

## Core Position

Anchor every answer in these official DHBW design foundations:

- **DHBW Red `#E2001A`** is the identity color — primary buttons, accent lines, hero backgrounds, table headers.
- **Source Sans 3** (Google Fonts) is the preferred web typeface; Arial as fallback.
- White and light gray (`#F5F5F5`) for content pages — no colorful backgrounds.
- Academic, structured tone: no glassmorphism effects, no heavy gradients, no neon accents.
- Lecture slides may have **full-red title pages (hero)** — content slides stay light with red accents.

---

## Workflow

1. Identify the task type: new HTML template, single component, review, or full page.
2. State the relevant DHBW design rules from `brand-core.md` first when they materially affect the answer.
3. Use the CSS Custom Properties from `html-samples.md` as the base for all implementations.
4. Load only the components the task actually needs (e.g. only code-block CSS, not the full template).
5. Deliver a complete `<!DOCTYPE html>` page only when the user explicitly requests a full template.
6. Inline styles are acceptable for small snippets; prefer CSS Custom Properties and classes for longer pages.

---

## Trigger and Routing Hints

- Load this skill for German prompts as readily as for English prompts.
- Words like `Lehrfolie`, `Skript`, `Übungsblatt`, `Aufgabe`, `Lösung`, `Vorlesung`, `V01`–`V20`
  combined with a DHBW context are strong signals for this skill.
- If the user asks to "improve", "review", or "make DHBW-compliant" an existing HTML page,
  load this skill even without an explicit design mention.
- For Python code in lectures: use the code-block style from `html-samples.md` (dark background `#1E2936`).
- The skill applies to all directories in this project: `lessons/`, `schiffeversenken/`, `src/`.

---

## Output Expectations

### For design or review tasks

Start with:
- Which DHBW rules are relevant for the task
- Concrete improvement recommendations (color, spacing, typography, component choice)

### For implementation tasks

Default deliverables:
- CSS Custom Properties block (`:root {}`) from the tokens
- Finished HTML component or full page
- Class naming: `dhbw-[component]__[element]--[modifier]` (BEM-like)

### Typical deliverables

- Complete lecture HTML pages for V01–V20
- Hero/title area (red) + content slide (white + red accent line)
- Code blocks with syntax-highlighting classes (Python, general)
- Callout/info boxes (Note, Important, Example)
- Tables with red header
- Button variants (Primary red, Outline, Ghost)
- Card grid for topic overviews / table of contents
- Learning objectives list with red bullet markers
- Slide navigation (Previous / Next)
- Sticky header with DHBW logo and navigation
- Footer (red)

---

## Hard Constraints

Do not use:

- Glassmorphism, backdrop-filter, heavy drop shadows
- Heavy gradients as an identity surface
- Accent colors other than DHBW Red `#E2001A` and its derived shades
- Playful, neon, or startup branding patterns
- Redrawing or recoloring the DHBW logo
- Long body text on a red background (only title pages/hero sections)
- Gray values not from the defined palette (`#6B7280`, `#D1D5DB`, `#F5F5F5`)

---

## Quality Checklist

Verify before every output:

- [ ] Primary red is `#E2001A` (not `#cc0000`, `#ff0000`, or other approximations)
- [ ] Font family includes Source Sans 3 + Arial fallback
- [ ] White text on red (`#E2001A`) — WCAG AA satisfied ✓
- [ ] Dark code-block background: `#1E2936`
- [ ] No `!important` spam or overriding browser defaults without reason
- [ ] No `font-size: 14px` as the base font size (minimum 16px / 1rem)
