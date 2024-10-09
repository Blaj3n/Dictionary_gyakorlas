'''

1. Diák Információk
Hozz létre egy diak dictionary-t, ami tartalmazza a következő kulcsokat és értékeket:

nev: a diák neve (pl. "Mária")
kor: a diák kora (pl. 16)
tantargyak: egy lista a tantárgyak neveivel (pl. ["matek", "irodalom", "fizika"])
Feladat:

Kiírd a diák nevét, korát, és az összes tantárgyát.

'''

diak = {
    "nev": "Mária",
    "kor": 16,
    "tantargyak": ["matek", "irodalom", "fizika"]
}

print(f"Diák neve: {diak['nev']}")
print(f"Diák kora: {diak['kor']}")
print("Tantárgyak:", ", ".join(diak["tantargyak"]))  # print(diak["tantargyak"]
# Tantárgyak kiírása: A join() metódus segítségével a tantárgyakat egy sorba fűzöd, elválasztva őket vesszővel,
# ami rendezettebb megjelenítést eredményez.