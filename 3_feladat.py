'''
3. Tantárgyak Hozzáadása
Használj egy dictionary-t, ami diákok nevét tartalmazza kulcsként, és a tantárgyaikat listaként.

Feladat:

Adj hozzá egy új tantárgyat (pl. "biológia") az összes diák tantárgyaihoz.
Írd ki a diákok új tantárgyaikat.
'''

diakok = [
    {"nev": "Tamás",
     "tantargyak": ["matek", "angol", "magyar"]},
    {"nev": "Dávid",
     "tantargyak": ["matek", "testnevelés", "kémia"]},
    {"nev": "Petra",
     "tantargyak": ["matek", "ének", "testnevelés"]}
]
# Új tantárgy, amelyet hozzá akarsz adni
uj_tantargy = "biologia"

for diak in diakok:
    diak['tantargyak'].append(uj_tantargy)

# Kiírás az új tantárgyakkal
print("Diákok új tantárgyai: ")
for diak in diakok:
    print(f"{diak['nev']}: {', '.join(diak['tantargyak'])}")
