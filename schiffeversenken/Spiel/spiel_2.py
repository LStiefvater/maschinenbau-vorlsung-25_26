"""Schiffeversenken Spiel aus VL 01–08."""

import csv
import random
from typing import Dict, List, Optional, Set, Tuple

COLOMAP = "ABCDE"
BOARD_SIZE = 5
SAVE_FILE = "spielstand.csv"


def erstelle_spielfeld() -> List[List[str]]:
    return [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def spielfeld_ausgeben(spielfeld: List[List[str]]) -> None:
    print("  " + " ".join(COLOMAP))
    for i, zeile in enumerate(spielfeld, 1):
        print(f"{i} " + " ".join(zeile))


def eingabe_lesen(prompt: str = "Koordinate (z.B. B3): ") -> Optional[Tuple[int, int]]:
    eingabe = input(prompt).strip().upper()
    if len(eingabe) != 2:
        print("Ungültige Eingabe: bitte Buchstabe+Zahl, z.B. B3")
        return None
    buchstabe, zahl = eingabe[0], eingabe[1]
    if buchstabe not in COLOMAP or not zahl.isdigit():
        print("Ungültige Eingabe.")
        return None
    zeile = int(zahl) - 1
    spalte = COLOMAP.index(buchstabe)
    if not (0 <= zeile < BOARD_SIZE):
        print("Ungültige Zeile.")
        return None
    return zeile, spalte


def schuss_auswerten(spielfeld: List[List[str]], schiffe: Dict[str, List[Tuple[int, int]]], koordinate: Tuple[int, int]) -> str:
    zeile, spalte = koordinate
    for name, positionen in schiffe.items():
        if koordinate in positionen:
            positionen.remove(koordinate)
            spielfeld[zeile][spalte] = "X"
            if not positionen:
                print(f"{name} versenkt!")
                return "versenkt"
            return "treffer"
    spielfeld[zeile][spalte] = "O"
    return "wasser"


def platziere_schiffe() -> Dict[str, List[Tuple[int, int]]]:
    schiffe: Dict[str, List[Tuple[int, int]]] = {}
    schiffstypen = [("Kreuzer", 3), ("U-Boot", 2)]
    besetzt: Set[Tuple[int, int]] = set()
    for name, laenge in schiffstypen:
        platziert = False
        while not platziert:
            richtung = random.choice(["horizontal", "vertikal"])
            if richtung == "horizontal":
                zeile = random.randint(0, BOARD_SIZE - 1)
                spalte = random.randint(0, BOARD_SIZE - laenge)
                koordinaten = [(zeile, spalte + i) for i in range(laenge)]
            else:
                zeile = random.randint(0, BOARD_SIZE - laenge)
                spalte = random.randint(0, BOARD_SIZE - 1)
                koordinaten = [(zeile + i, spalte) for i in range(laenge)]
            if any(k in besetzt for k in koordinaten):
                continue
            schiffe[name] = koordinaten
            besetzt.update(koordinaten)
            platziert = True
    return schiffe


def spiel_beendet(schiffe: Dict[str, List[Tuple[int, int]]]) -> bool:
    return all(len(positionen) == 0 for positionen in schiffe.values())


def spielstand_speichern(dateiname: str, spielfeld: List[List[str]], statistik: Dict[str, int], schiffe: Dict[str, List[Tuple[int, int]]]) -> None:
    with open(dateiname, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([statistik["treffer"], statistik["wasser"], statistik["versenkt"]])
        for zeile in spielfeld:
            writer.writerow(zeile)
        writer.writerow(["SCHIFFE"])
        for name, koordinaten in schiffe.items():
            flache_koords = [f"{r},{c}" for r, c in koordinaten]
            writer.writerow([name] + flache_koords)


def spielstand_laden(dateiname: str) -> Tuple[List[List[str]], Dict[str, int], Dict[str, List[Tuple[int, int]]]]:
    spielfeld: List[List[str]] = []
    schiffe: Dict[str, List[Tuple[int, int]]] = {}
    with open(dateiname, "r", newline="") as f:
        reader = csv.reader(f)
        erste = next(reader)
        statistik = {"treffer": int(erste[0]), "wasser": int(erste[1]), "versenkt": int(erste[2])}
        for zeile in reader:
            if zeile and zeile[0] == "SCHIFFE":
                break
            spielfeld.append(list(zeile))
        for schiff in reader:
            if not schiff:
                continue
            name = schiff[0]
            koordinaten = []
            for coord in schiff[1:]:
                if coord:
                    r, c = coord.split(",")
                    koordinaten.append((int(r), int(c)))
            schiffe[name] = koordinaten
    return spielfeld, statistik, schiffe


def lade_sicher(dateiname: str) -> Optional[Tuple[List[List[str]], Dict[str, int], Dict[str, List[Tuple[int, int]]]]]:
    try:
        return spielstand_laden(dateiname)
    except FileNotFoundError:
        print(f"Datei '{dateiname}' nicht gefunden!")
        return None


def zeige_menue() -> None:
    print("=== Schiffe versenken ===")
    print("1) Neues Spiel")
    print("2) Spielstand laden")
    print("3) Regeln")
    print("4) Beenden")


def spiele_spiel() -> None:
    spielfeld = erstelle_spielfeld()
    schiffe = platziere_schiffe()
    statistik = {"treffer": 0, "wasser": 0, "versenkt": 0}
    geschossen: Set[Tuple[int, int]] = set()

    while not spiel_beendet(schiffe):
        spielfeld_ausgeben(spielfeld)
        koordinate = eingabe_lesen()
        if koordinate is None:
            continue
        if koordinate in geschossen:
            print("Bereits geschossen!")
            continue
        geschossen.add(koordinate)
        ergebnis = schuss_auswerten(spielfeld, schiffe, koordinate)
        statistik[ergebnis] = statistik.get(ergebnis, 0) + 1
        print(f"Ergebnis: {ergebnis}")

    print("Alle Schiffe versenkt!")
    spielfeld_ausgeben(spielfeld)
    print("Statistik:")
    for k, v in statistik.items():
        print(f"  {k}: {v}")
    speichern = input("Spielstand speichern? (j/n): ").strip().lower()
    if speichern == "j":
        spielstand_speichern(SAVE_FILE, spielfeld, statistik, schiffe)
        print("Spielstand gespeichert.")


def hauptprogramm() -> None:
    while True:
        zeige_menue()
        wahl = input("Deine Wahl: ").strip()
        match wahl:
            case "1":
                spiele_spiel()
            case "2":
                ergebnis = lade_sicher(SAVE_FILE)
                if ergebnis is not None:
                    spielfeld, statistik, schiffe = ergebnis
                    print("Geladener Spielstand:")
                    spielfeld_ausgeben(spielfeld)
                    print("Statistik:")
                    for k, v in statistik.items():
                        print(f"  {k}: {v}")
                    weiterspielen = input("Weiterspielen? (j/n): ").strip().lower()
                    if weiterspielen == "j":
                        geschossen = {
                            (r, c)
                            for r, row in enumerate(spielfeld)
                            for c, z in enumerate(row)
                            if z in {"X", "O"}
                        }
                        while not spiel_beendet(schiffe):
                            spielfeld_ausgeben(spielfeld)
                            koordinate = eingabe_lesen()
                            if koordinate is None:
                                continue
                            if koordinate in geschossen:
                                print("Bereits geschossen!")
                                continue
                            geschossen.add(koordinate)
                            ergebnis = schuss_auswerten(spielfeld, schiffe, koordinate)
                            statistik[ergebnis] = statistik.get(ergebnis, 0) + 1
                            print(f"Ergebnis: {ergebnis}")
                        print("Alle Schiffe versenkt!")
                        spielfeld_ausgeben(spielfeld)
                        print("Statistik:")
                        for k, v in statistik.items():
                            print(f"  {k}: {v}")
            case "3":
                print("Regeln: Versenke alle Schiffe auf dem 5x5-Board. Gib Koordinaten wie B3 ein.")
            case "4":
                print("Auf Wiedersehen!")
                break
            case _:
                print("Ungültige Eingabe!")


if __name__ == "__main__":
    hauptprogramm()
