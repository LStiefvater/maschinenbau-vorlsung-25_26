# Bildgenerierungsprompt: OSI-Modell-Diagramm (V15)

## Zweck

Dieser Prompt dient zur Generierung eines OSI-Modell-Diagramms für die Vorlesungsfolie V15 – Netzwerktechnik Grundlagen & Protokolle. Das Bild soll die 7 Schichten des OSI-Modells als farbige, gestapelte Rechtecke von unten nach oben darstellen.

---

## Bildgenerierungsprompt

**Rolle:** Du bist ein technischer Illustrator und Infografik-Designer für Hochschullehrmaterialien.

**Kontext:** Das Bild wird in einer HTML-Vorlesungsseite für Maschinenbau-Erstsemester-Studenten der DHBW Stuttgart eingesetzt. Die Studierenden haben wenig Netzwerk-Vorwissen. Das Bild soll das OSI-Schichtenmodell auf einen Blick verständlich machen.

**Aufgabe:** Erstelle ein klares Infografik-Diagramm des OSI-Referenzmodells mit 7 horizontalen, farbigen Schichten, angeordnet von unten (Schicht 1) nach oben (Schicht 7). Jede Schicht besteht aus einem Rechteck mit drei Elementen: Schichtnummer links, deutschem Schichtnamen in der Mitte, und konkreten Protokoll-Beispielen rechts.

**Inhalt der Schichten (von unten nach oben):**

| Nr | Name (Deutsch) | Beispiele |
|----|----------------|-----------|
| 1 | Bitübertragungsschicht | Kabel, Funk (WLAN), Glasfaser |
| 2 | Sicherungsschicht | Ethernet, WLAN (802.11), MAC |
| 3 | Vermittlungsschicht (Netzwerk) | IP, ICMP, Routing |
| 4 | Transportschicht | TCP, UDP |
| 5 | Sitzungsschicht | NetBIOS, RPC |
| 6 | Darstellungsschicht | TLS/SSL, JPEG, ASCII |
| 7 | Anwendungsschicht | HTTP, FTP, SMTP, DNS |

**Format:** Hochformat, ca. 800 × 1000 px oder skalierbar. Jede Schicht hat gleiche Höhe. Klarer, großzügiger Weißraum zwischen den Elementen innerhalb einer Schicht.

**Farbgebung:** Jede Schicht hat eine eigene Farbe. Empfehlung: Regenbogen-Farbverlauf von unten nach oben (Schicht 1 tiefes Blau/Indigo, aufsteigend zu Schicht 7 in Warmrot oder Orange). Alle Farben haben gute Lesbarkeit für schwarzen Text. Kein grelles Neon. Akzentfarbe DHBW-Rot (#E2001A) optional für Schicht 7 (Anwendungsschicht) oder für Trennlinien.

**Beschriftung:** Schichtnummer (z.B. „7") als große, fette Zahl auf der linken Seite des Rechtecks. Schichtname in der Mitte, fett, gut lesbar. Rechts davon die Protokoll-Beispiele in kleinerer, normaler Schrift, durch Komma getrennt oder als kleines Tag/Badge. Deutsch als Primärsprache; englische Bezeichnung optional in Klammern (z.B. „Anwendungsschicht (Application)").

**Stil:** Flat Design, professionell-technisch, keine Verläufe innerhalb der Farbflächen. Klare Trennlinien zwischen Schichten. Keine Cartoon-Elemente.

**Zusätzlich:** Ein kleiner beschrifteter Pfeil oder Beschriftung auf der linken Seite „Hardware-nah" (unten) und „Software-nah" (oben). Optional: ein zweiter schmaler Bereich rechts neben dem Stapel mit einer Spalte „Zugehöriges TCP/IP-Modell" als Klammer, die die entsprechenden OSI-Schichten zusammenfasst.

**Hintergrund:** Weiß (#FFFFFF).

**Qualitätskriterien:**
- Alle Texte müssen bei 600 px Breite lesbar sein.
- Das Diagramm muss ohne zusätzliche Erklärung verständlich sein.
- Konsistente Typografie in allen Schichten.

---

## Hinweise zur Integration

Das generierte Bild wird im Ordner `lessons/V15-Netzwerktechnik-Grundlagen-Protokolle-Teil1/graphics/` gespeichert und in der HTML-Seite `V15-Netzwerktechnik-Grundlagen-Protokolle-Teil1_skript.html` eingebunden. Dateiname: `V15-osi-modell.png` oder `V15-osi-modell.svg`.
