# Bildgenerierungsprompt: KI-Übersichtsdiagramm (V11)

## Zweck

Dieser Prompt dient zur Generierung eines KI-Übersichtsdiagramms für die Vorlesungsfolie V11 – GPTs, LLMs & Künstliche Intelligenz. Das Bild soll die Beziehung der vier Begriffe KI, Machine Learning, Deep Learning und LLMs als ineinander verschachtelte Kreise darstellen.

---

## Bildgenerierungsprompt

**Rolle:** Du bist ein technischer Illustrator, der Lehrmaterialien für Hochschulen gestaltet.

**Kontext:** Das Bild wird in einer HTML-Vorlesungsseite für Maschinenbau-Erstsemester-Studenten der DHBW Stuttgart eingesetzt. Die Zielgruppe hat wenig Informatik-Erfahrung. Das Bild soll auf weißem oder sehr hellgrauem Hintergrund gut lesbar sein.

**Aufgabe:** Erstelle ein klares, professionelles Diagramm mit vier ineinander verschachtelten (konzentrischen) Kreisen, die von außen nach innen kleiner werden. Beschrifte jeden Kreis mit dem Fachbegriff und einer kurzen Erklärung.

**Inhalt der Kreise (von außen nach innen):**

- Äußerster Kreis: **Künstliche Intelligenz (KI)** – Oberbegriff: Systeme mit intelligenzähnlichem Verhalten
- Zweiter Kreis: **Machine Learning (ML)** – Lernen aus Daten, ohne explizite Regeln
- Dritter Kreis: **Deep Learning** – Mehrschichtige neuronale Netze
- Innerster Kreis: **Large Language Models (LLMs)** – GPT, ChatGPT, Gemini

**Format:** Quadratisches Bild, mindestens 1200 × 1200 px. Vektorstil bevorzugt oder hochauflösendes Raster-PNG. Saubere Schrift, gut lesbar auch bei 50% Zoom.

**Stil:** Technisch-sachlich, minimalistisch, kein Cartoon-Look. Flaches Design (Flat Design), keine Schlagschatten außer subtilen Trennlinien. Farbgebung: Helles, harmonisches Farbschema. Der äußerste Kreis hat die hellste Farbe; je weiter innen, desto gesättigter oder dunkler. Akzentfarbe Rot (#E2001A) für die Beschriftung des innersten Kreises (LLMs) und für Pfeile oder Highlights.

**Hintergrund:** Weiß (#FFFFFF) oder sehr helles Grau (#F5F5F5).

**Schrift:** Serifenlose Schrift (z.B. Inter, Source Sans Pro oder ähnlich). Fachbegriff fett, Kurzbeschreibung in kleinerer, normaler Schriftstärke darunter.

**Zusätzliche Gestaltungselemente:** Kleine Icons oder Symbole in jedem Kreis sind optional, aber erwünscht – z.B. Gehirn-Symbol für Deep Learning, Sprechblase für LLMs. Ein kurzer Pfeil oder Label „Enthält" an der Grenze zwischen den Kreisen wäre hilfreich.

**Qualitätskriterien:**
- Alle vier Begriffe müssen lesbar sein, auch wenn das Bild auf 400 px Breite skaliert wird.
- Kein Clipart-Look.
- Kein übermäßiger Text – nur Bezeichnung und Kurzbeschreibung pro Ebene.

---

## Hinweise zur Integration

Das generierte Bild wird im Ordner `lessons/V11-GPTs-LLMs-KI/graphics/` gespeichert und in der HTML-Seite `V11-GPTs-LLMs-KI_skript.html` eingebunden. Dateiname: `V11-ki-ueberblick.png` oder `V11-ki-ueberblick.svg`.
