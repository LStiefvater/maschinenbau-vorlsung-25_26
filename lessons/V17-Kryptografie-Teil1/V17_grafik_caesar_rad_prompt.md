# Bildgenerierungs-Prompt: Caesar-Chiffre Rad

## Verwendung
Diesen Prompt in eine KI-Bildgenerierungs-Plattform eingeben (DALL-E 3, Midjourney, Adobe Firefly).

---

## Prompt (Englisch)

```
A clean technical diagram of the Caesar cipher as two concentric alphabet rings, 
flat design, dark background (#1E2936).

Design:
- Outer ring: 26 segments, each containing one capital letter A-Z, 
  filled with dark red (#E2001A), white bold text (Fira Code font), 
  labeled "Klartext" (Plaintext) on the outside
- Inner ring: same 26 segments but rotated clockwise by 3 positions,
  filled with dark blue (#1E2936) with steel blue border (#60A5FA), 
  light blue bold text, labeled "Chiffrat (Schlüssel=3)" (Ciphertext)
- Arrow indicating rotation direction: orange arrow showing "+3 shift"
- Center circle: dark, contains text "k=3" in orange
- Example annotation: "A → D" with dotted line connecting outer A to inner D

Color scheme: background #1E2936, outer ring #E2001A, inner ring borders #60A5FA, 
annotation arrows #F97316, label text #E8EFF5
Style: Clean technical documentation, flat design, no shadows, no gradients
Aspect ratio: 1:1 (square)
```

---

## Varianten

### Für Midjourney
Füge am Ende hinzu: `--style raw --ar 1:1 --v 6`

### Vereinfachte Lineardarstellung (Alternative)
```
A clean diagram showing Caesar cipher as two horizontal rows of alphabet letters,
top row: A B C D ... Z (DHBW red #E2001A background, white text)
bottom row shifted by 3: D E F G ... C (steel blue border #60A5FA, dark background)
Arrow between rows labeled "Schlüssel: 3"
Clean dark background #1E2936, monospace font
Aspect ratio: 3:1 (wide)
```

---

## Kontextinfo

Diese Grafik wird in **V17-Kryptografie-Teil1_praxis.html** verwendet.
Illustriert die Caesar-Verschiebung für Maschinenbau-Studenten.
