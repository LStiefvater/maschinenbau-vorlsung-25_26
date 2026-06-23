wort = "banane"
haeufigkeit = {}
for buchstabe in wort:
    if buchstabe in haeufigkeit:
        haeufigkeit[buchstabe] = haeufigkeit[buchstabe] + 1
    else:
        haeufigkeit[buchstabe] = 1
print(haeufigkeit)