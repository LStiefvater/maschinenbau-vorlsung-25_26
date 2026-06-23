"""
Lösungen zu VL8 — Aufgabe 2
Implementiert: spiel_beendet(schiffe)

Die Funktion prüft, ob alle Schiffe versenkt sind (alle Positionslisten leer).
"""

def spiel_beendet(schiffe):
    """Gibt True zurück, wenn alle Schiffe versenkt sind (alle Listen leer).

    Args:
        schiffe (dict): Mapping SchiffName -> Liste von (zeile, spalte)-Tupeln

    Returns:
        bool: True wenn alle Listen leer sind, sonst False
    """
    for name, positionen in schiffe.items():
        if positionen:  # nicht-leere Liste → noch nicht versenkt
            return False
    return True


if __name__ == "__main__":
    # Tests aus der Aufgabenstellung
    tests = [
        ({"Kreuzer": [], "U-Boot": []}, True),
        ({"Kreuzer": [(0, 1)], "U-Boot": []}, False),
    ]

    for i, (input_schiffe, erwartet) in enumerate(tests, 1):
        erg = spiel_beendet(input_schiffe)
        print(f"Test {i}: erwartet={erwart}, erhalten={erg}")
