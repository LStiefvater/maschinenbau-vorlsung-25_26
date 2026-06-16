# Bildgenerierungs-Prompt: Messdaten-Liniendiagramm (matplotlib-Stil)

## Verwendung
Diesen Prompt in eine KI-Bildgenerierungs-Plattform eingeben (DALL-E 3, Midjourney, Adobe Firefly, Stable Diffusion).

---

## Prompt (Englisch)

```
A clean Python matplotlib line chart showing temperature sensor data over time, 
technical documentation style, light gray background (#F5F5F5), white plot area.

Chart content:
- Title: "Aufheizkurve Motor XY – Prüflauf 42" (bold, dark gray, top center)
- X-axis: "Zeit [Minuten]" label, values 0 to 50 with gridlines
- Y-axis: "Temperatur [°C]" label, values 20 to 100 with gridlines
- Two data lines:
  - Line 1: DHBW red (#E2001A), solid, 2px, labeled "Sensor 1 (Lager)"
  - Line 2: Steel blue (#60A5FA), dashed, labeled "Sensor 2 (Gehäuse)"
  - Both lines curve upward from ~20°C to ~90°C showing exponential heating
- Horizontal orange dotted line at y=80 labeled "Alarmgrenze 80°C"
- Legend box in upper left, clean white background
- Light gray grid lines
- Clean axis ticks, no top/right border (spine-off style)

Style: Technical, professional, academic publication quality
No decorative elements, no gradients, pixel-perfect crisp lines
Aspect ratio: 16:9 (landscape)
Font: resembles matplotlib default (DejaVu Sans or similar)
```

---

## Varianten

### Für Balkendiagramm
```
A clean Python matplotlib bar chart showing production comparison, 
4 stations labeled "Station A" through "Station D",
bars filled with DHBW red (#E2001A), 
Y-axis "Teile pro Schicht", X-axis "Fertigungsstation",
light background, professional technical style
```

### Für Streudiagramm
```
A clean Python matplotlib scatter plot showing correlation between 
RPM (X-axis: 800 to 2000) and temperature (Y-axis: 45 to 91°C),
6 red data points (#E2001A, circle markers, size 80),
labeled "Drehzahl vs. Lagertemperatur",
light background, grid visible, technical documentation style
```

---

## Kontextinfo

Diese Grafik wird in **V13-Betriebssysteme-Rechnerarchitektur-Teil1_praxis.html** verwendet.
Zielgruppe: Maschinenbau-Studenten, die matplotlib für Messdatenvisualisierung lernen.
Zielgröße im HTML: max-width 700px.
