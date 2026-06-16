# Bildgenerierungs-Prompt: while-Schleife Ablaufdiagramm

## Verwendung
Diesen Prompt in eine KI-Bildgenerierungs-Plattform (DALL-E 3, Midjourney, Stable Diffusion, Firefly) eingeben.

---

## Prompt (Englisch – für bessere Ergebnisse)

```
Clean technical diagram of a while loop flow chart, flat design, dark background (#1E2936), 
no gradients, no shadows, no 3D effects.

Layout: vertical top-to-bottom flow with left branch for loop body.

Elements (top to bottom):
1. Rounded rectangle labeled "Program Start" – filled dark red (#E2001A), white text, Fira Code monospace font
2. Vertical arrow down
3. Diamond shape labeled "while condition?" – dark fill (#1E2936), border (#E2001A 2px), red text "while", gray subtext "condition True?"
4. LEFT branch from diamond (label "True" in green): 
   - Horizontal arrow left
   - Rectangle labeled "Loop Body" (blue border #60A5FA, dark fill, white text "execute code")
   - Curved arrow back up to diamond
5. RIGHT branch from diamond (label "False" in orange):
   - Horizontal arrow right  
   - Rectangle labeled "Continue Program" (gray border #6B7280, dark fill, gray text)
6. Small red warning badge below loop body: "⚠ Variable must change!"

Colors: background #1E2936, arrows #D1D5DB, True-path #22C55E, False-path #F97316
Font: Fira Code monospace for code labels, Source Sans Pro for descriptions
Style: Technical documentation diagram, clean lines, no decorative elements
Aspect ratio: 3:4 (portrait)
```

---

## Varianten

### Deutsche Beschriftung
Ersetze im Prompt:
- "while condition?" → "while Bedingung?"
- "Loop Body" → "Schleifenkörper"
- "Continue Program" → "Programm weiter"
- "Variable must change!" → "Variable muss sich ändern!"

### Alternative Stilangabe für Midjourney
Füge am Ende hinzu: `--style raw --ar 3:4 --v 6`

### Alternative Stilangabe für Stable Diffusion
Füge am Ende hinzu: `technical diagram, vector style, clean, minimalist, dark theme`

---

## Kontextinfo für die Verwendung im Skript

Diese Grafik wird in **V06-Programm-Ablauf-Plaene-Teil2_praxis.html** referenziert.
Sie illustriert den Ablauf einer while-Schleife für Maschinenbau-Studenten.
Zielgröße: ca. 400×500 px, eingebettet in die HTML-Seite neben dem Code-Beispiel.
