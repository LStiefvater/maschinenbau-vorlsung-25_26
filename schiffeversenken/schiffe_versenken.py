spielfeld = []
schiff = [(0, 1), (0, 2), (0, 3)]
for i in range(5):
    spielfeld.append(["~"] * 5)

 # Spielfeld ausgeben
print("   ", end="")
for buchstabe in "ABCDE":
    print(f"{buchstabe} ", end="")
print()
for zeile_idx, zeile_inhalt in enumerate(spielfeld):
    print(f"{zeile_idx + 1}  ", end="")
    for feld in zeile_inhalt:
        print(f"{feld} ", end="")
    print()
eingabe = input("gib einen schuss an:")
while eingabe != "ende":
    spalte = "ABCDE".index(eingabe[0])
    zeile  = int(eingabe[1]) - 1
    koordinate = (zeile, spalte)

    if koordinate in schiff:
        spielfeld[zeile][spalte] = "X"
        print("Treffer!")
    else:
        spielfeld[zeile][spalte] = "O"
        print("Wasser!")

    # Spielfeld ausgeben
    print("   ", end="")
    for buchstabe in "ABCDE":
        print(f"{buchstabe} ", end="")
    print()
    for zeile_idx, zeile_inhalt in enumerate(spielfeld):
        print(f"{zeile_idx + 1}  ", end="")
        for feld in zeile_inhalt:
            print(f"{feld} ", end="")
        print()
    eingabe =  input("gib einen schuss an:")
