def erstelle_spielfeld():
    spielfeld = []
    for i in range(5):
        spielfeld.append(["~"] * 5)
    return spielfeld


def spielfeld_ausgeben(spielfeld):
    for zeile in spielfeld:
        print(" ".join(zeile))