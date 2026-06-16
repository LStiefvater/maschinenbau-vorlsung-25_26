# Bildgenerierungsprompt: Asymmetrische Verschlüsselung (V17)

## Zweck

Dieser Prompt dient zur Generierung eines Diagramms zur asymmetrischen Verschlüsselung für die Vorlesungsfolie V17 – Kryptografie Teil 1. Das Bild soll die Briefkasten-Analogie mit Alice und Bob sowie Public Key / Private Key visuell veranschaulichen.

---

## Bildgenerierungsprompt

**Rolle:** Du bist ein professioneller Infografik-Designer, der komplexe technische Konzepte für Einsteiger verständlich illustriert.

**Kontext:** Das Bild wird in einer HTML-Vorlesungsseite für Maschinenbau-Erstsemester-Studenten der DHBW Stuttgart eingesetzt. Es soll das Prinzip der asymmetrischen Verschlüsselung intuitiv und ohne mathematische Details erklären. Die Zielgruppe ist technisch wenig vorgebildet.

**Aufgabe:** Erstelle eine klare Infografik, die das Konzept der asymmetrischen Verschlüsselung anhand der Briefkasten-Analogie darstellt. Die Grafik soll aus zwei klar getrennten Bereichen bestehen: links Alice (Sender), rechts Bob (Empfänger).

**Inhalt und Ablauf (von links nach rechts):**

1. **Alice (links):** Eine einfache Figur (Person) mit einem Brief/Umschlag in der Hand. Beschriftung: „Alice sendet eine verschlüsselte Nachricht".

2. **Pfeil nach rechts:** Zeigt den Kommunikationsweg an. Über dem Pfeil steht: „Verschlüsselt mit Bobs Public Key 🔓". Eve (eine dritte Figur, zwischen Alice und Bob, leicht kleiner dargestellt) schaut auf den Pfeil, kann aber nichts lesen – symbolisiert durch ein Fragezeichen oder ein rotes ❌ neben Eve.

3. **Briefkasten (Mitte-rechts):** Ein symbolischer offener Briefkasten mit dem Label „Public Key 🔓 – Jeder kann einwerfen". Der Brief fällt hinein.

4. **Bob (rechts):** Bob hält einen physischen Schlüssel in der Hand und öffnet den Briefkasten. Beschriftung: „Nur Bob kann öffnen – Private Key 🔑 bleibt geheim".

5. **Kurze Legende unten:** Zwei Zeilen: „Public Key (öffentlich): Jeder darf ihn kennen – zum Verschlüsseln" und „Private Key (privat): Nur der Besitzer kennt ihn – zum Entschlüsseln".

**Format:** Querformat, ca. 1200 × 600 px. Leserichtung links nach rechts. Viel Weißraum, kein überladenes Design.

**Stil:** Flat Design, freundlich aber technisch-sachlich. Einfache Figuren (keine fotorealistischen Personen, kein Cartoon-Übertrieb). Konsistente Icon-Sprache. Akzentfarbe DHBW-Rot (#E2001A) für die Schlüssel-Symbole und wichtige Beschriftungen. Neutrale Farben (Grau, Hellblau) für die Figuren und Hintergrundelemente.

**Hintergrund:** Weiß (#FFFFFF) oder sehr helles Grau (#F5F5F5).

**Schrift:** Serifenlos (z.B. Inter oder Source Sans Pro). Klare Hierarchie: Beschriftungen der Hauptelemente fett und größer, Erklärtexte kleiner und in Grau.

**Qualitätskriterien:**
- Das Bild muss ohne den begleitenden Text verständlich sein.
- Alle Beschriftungen müssen bei 600 px Breite lesbar sein.
- Die Briefkasten-Analogie muss auf einen Blick erkennbar sein.
- Eve als Angreiferin muss klar als „blockiert" oder „ausgeschlossen" dargestellt werden.

---

## Hinweise zur Integration

Das generierte Bild wird im Ordner `lessons/V17-Kryptografie-Teil1/graphics/` gespeichert und in der HTML-Seite `V17-Kryptografie-Teil1_skript.html` eingebunden. Dateiname: `V17-asymmetrisch.png` oder `V17-asymmetrisch.svg`.
