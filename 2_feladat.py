'''
2. Diákok Gyűjteménye
Hozz létre egy diakok dictionary-t, ami három diák nevét és adatait tartalmazza
(használj dictionary-t a diák információinak tárolására).
Feladat:

Kiírd minden diák nevét, korát, és a tantárgyaikat.
Ellenőrizd, hogy az egyik diák (pl. "Béla") szerepel-e a listában.
'''

# Dictionary Lista: A diakok lista három diák adatát tartalmazza, mindegyik a nevét, korát és tantárgyait
# egy dictionary formájában tárolja.
diakok = [
    {"nev": "Tamás",
     "kor": 16,
     "tantargyak": ["matek", "angol", "magyar"]},
    {"nev": "Dávid",
     "kor": 17,
     "tantargyak": ["matek", "testnevelés", "kémia"]},
    {"nev": "Petra",
     "kor": 18,
     "tantargyak": ["matek", "ének", "testnevelés"]}
]

print("Diákok nevei: ")
for diak in diakok:
    print(diak['nev'])

print()

print("Diákok korai: ")
for diak in diakok:
    print(diak['kor'])

print()

print("Diákok tantárgyai: ")
for diak in diakok:
    print(f"{diak['nev']}: {', '.join(diak['tantargyak'])}")  # print(diak['tantargyak'])
