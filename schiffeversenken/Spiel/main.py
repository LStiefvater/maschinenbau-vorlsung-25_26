def erstelle_spielfeld():
    spielfeld = []

    for _ in range(5):
        zeile = ["~"] * 5
        spielfeld.append(zeile)

    return spielfeld

spielfeld = erstelle_spielfeld()
print(spielfeld[0])

def spielfeld_ausgeben(spielfeld):
    print("   A B C D E")
    for zeile_idx, zeile_inhalt in enumerate(spielfeld):
        print(f"{zeile_idx + 1}  " + " ".join(zeile_inhalt))

spielfeld = erstelle_spielfeld()
spielfeld_ausgeben(spielfeld)

def eingabe_lesen():
    eingabe = input("Koordinate (z.B. B3): ").strip().upper()

    if len(eingabe) != 2:
        return None

    buchstabe = eingabe[0]
    zahl_teil = eingabe[1]

    if buchstabe not in "ABCDE" or not zahl_teil.isdigit():
        return None

    zeile = int(zahl_teil) - 1
    spalte = "ABCDE".index(buchstabe)

    if 0 <= zeile <= 4:
        return (zeile, spalte)

    return None

def schuss_auswerten(spielfeld, schiffe, koordinate):
    zeile, spalte = koordinate

    for name, positionen in schiffe.items():
        if koordinate in positionen:
            positionen.remove(koordinate)
            spielfeld[zeile][spalte] = "X"

            if len(positionen) == 0:
                return "versenkt"

            return "treffer"

    spielfeld[zeile][spalte] = "O"
    return "wasser"

spielfeld = erstelle_spielfeld()
schiffe = {"Kreuzer": [(0, 1), (0, 2)], "U-Boot": [(3, 0)]}

print(schuss_auswerten(spielfeld, schiffe, (0, 1)))
print(schuss_auswerten(spielfeld, schiffe, (0, 2)))
print(schuss_auswerten(spielfeld, schiffe, (4, 4)))

import random

def platziere_schiffe():
    schiffe = {}
    schiffstypen = [("kreuzer", 3), ("u_boot", 2)]

    for name, laenge in schiffstypen:
        platziert = False
        while not platziert:
            zeile = random.randint(0, 4)
            spalte = random.randint(0, 4)
            richtung = random.randint(0, 1)  # 0 = horizontal, 1 = vertikal

            if richtung == 0 and spalte + laenge - 1 <= 4:
                # Horizontal: Spalte erhöht sich
                koordinaten = [(zeile, spalte + i) for i in range(laenge)]
                platziert = True
            elif richtung == 1 and zeile + laenge - 1 <= 4:
                # Vertikal: Zeile erhöht sich
                koordinaten = [(zeile + i, spalte) for i in range(laenge)]
                platziert = True

        schiffe[name] = {"koordinaten": koordinaten, "versenkt": False}

    return schiffe

# Test
schiffe = platziere_schiffe()
print("Schiffe platziert:")
for name, daten in schiffe.items():
    print(f"  {name}: {daten['koordinaten']}")


    import csv
from spiellogik import erstelle_spielfeld

def spielstand_speichern(dateiname, spielfeld, statistik):
    with open(dateiname, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([statistik["treffer"], statistik["wasser"], statistik["versenkt"]])
        for zeile in spielfeld:
            writer.writerow(zeile)

# Test
spielfeld = erstelle_spielfeld()
spielfeld[0][2] = "X"  # Treffer simulieren
spielfeld[1][3] = "O"  # Wasser simulieren
statistik = {"treffer": 1, "wasser": 1, "versenkt": 0}

spielstand_speichern("spielstand.csv", spielfeld, statistik)
print("Spielstand gespeichert!")

import csv
from spiellogik import spielfeld_ausgeben

def spielstand_laden(dateiname):
    spielfeld = []
    with open(dateiname, "r") as f:
        reader = csv.reader(f)
        # Erste Zeile: Statistik
        erste_zeile = next(reader)
        statistik = {
            "treffer": int(erste_zeile[0]),
            "wasser": int(erste_zeile[1]),
            "versenkt": int(erste_zeile[2])
        }
        # Restliche Zeilen: Spielfeld
        for zeile in reader:
            spielfeld.append(zeile)
    return spielfeld, statistik

# Test: Laden und ausgeben
geladenes_spielfeld, geladene_statistik = spielstand_laden("spielstand.csv")
print("Geladenes Spielfeld:")
spielfeld_ausgeben(geladenes_spielfeld)
print(f"Statistik: {geladene_statistik}")

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
