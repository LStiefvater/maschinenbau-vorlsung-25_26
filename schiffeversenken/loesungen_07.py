"""
Lösungen zu VL7 — Aufgabe 2 und 3
- lade_sicher(dateiname): ruft spielstand_laden(dateiname) auf und fängt FileNotFoundError ab
- zeige_menue(): gibt das Menü auf der Konsole aus

Hinweis: In dieser Umgebung ist `spielstand_laden` möglicherweise nicht definiert (Notebook VL6).
Deshalb fängt `lade_sicher` auch den Fall ab, dass die Funktion fehlt.
"""


def lade_sicher(dateiname):
    try:
        # Versuch, die Funktion spielstand_laden aufzurufen (sollte in VL6 definiert sein)
        return spielstand_laden(dateiname)
    except NameError:
        print("Funktion spielstand_laden ist nicht definiert.")
        return None
    except FileNotFoundError:
        print(f"Datei '{dateiname}' nicht gefunden!")
        return None


def zeige_menue():
    print("=== Schiffe versenken ===")
    print("1) Neues Spiel")
    print("2) Spielstand laden")
    print("3) Regeln")
    print("4) Beenden")


if __name__ == "__main__":
    zeige_menue()
    print('\nTeste lade_sicher (falls spielstand_laden verfügbar):')
    ergebnis = lade_sicher("spielstand.csv")
    print("Ergebnis:", ergebnis)
