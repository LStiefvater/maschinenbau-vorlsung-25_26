# Bildgenerierungs-Prompt: Schiffe-Versenken Spielfeld

## Verwendung
Diesen Prompt in eine KI-Bildgenerierungs-Plattform eingeben (DALL-E 3, Midjourney, Adobe Firefly).

---

## Prompt (Englisch)

```
A clean Python-terminal-style battleship game grid, flat UI design, dark background (#1E2936).

Layout: 5x5 grid with column headers A B C D E and row numbers 1-5.

Grid specifications:
- Overall size: compact grid, well-spaced cells
- Column headers: A B C D E in steel blue (#60A5FA), bold monospace font
- Row numbers: 1-5 in dark gray (#7A9CB3), left side
- Each cell is a rounded square (6px radius)

Cell states visible in the example:
- Row 1, Col A: "X" cell – DHBW red (#E2001A) background, white bold X = HIT
- Row 1, Col B: "~" cell – dark blue cell (#1E2936), blue ~ = water/unknown
- Row 1, Col C: "~" cell – same water
- Row 2, Col A: "O" cell – dark purple (#2D1F4E), light purple O = MISS  
- Row 2, Col B: "X" cell – DHBW red background, white X = HIT
- All other cells: dark water "~" in steel blue

Below grid:
- Legend row: red square "X = Treffer" | purple square "O = Wasser" | dark square "~ = Unbekannt"
- Input prompt line: "> Gib einen Schuss an: _" in green (#22C55E) monospace

Title at top: "🚢 Schiffe Versenken" in white bold, DHBW red accent line below

Style: Terminal/console aesthetic, monospace fonts throughout (Fira Code), 
clean grid lines, professional game UI
No gradients, no shadows, flat design
Aspect ratio: 1:1 (square)
```

---

## Varianten

### Für Midjourney
`--style raw --ar 1:1 --v 6`

### Mit Spielstand-Overlay
```
Same grid as above, but add a score panel on the right side:
- "Schüsse: 7" in white
- "Treffer: 2" in DHBW red  
- "Versenkt: 0/3" in orange
Clean dark UI panel (#0F1E2B) with steel blue border
```

---

## Kontextinfo

Diese Grafik wird in **schiffeversenken_praxis.html** verwendet.
Zeigt das typische Spielfeld für Maschinenbau-Studenten.
Zielgröße: ca. 400×400px, zentriert auf der HTML-Seite.
