'''

5. Évfolyamok
Hozz létre egy dictionary-t, ami a diákok neveit és évfolyamaikat tárolja.

Feladat:

Írd ki a különböző évfolyamok számát (pl. hány diák van az 11. évfolyamon).

'''

# Hogyan működik a kód:
# Szótár használata: Az evfolyam_szamlalo egy szótár, amely minden évfolyamhoz tárolja a diákok számát.
# Feltételes ellenőrzés: Ha egy adott évfolyam már szerepel a szótárban, akkor növeli a hozzá tartozó számlálót,
# különben létrehozza az új évfolyamot a szótárban.
# Eredmény kiíratása: A végén egy for ciklus segítségével kiírjuk, hogy hány diák van az egyes évfolyamokon.
diakok = [
    {"nev": "Anna", "evfolyam": 9},
    {"nev": "Bence", "evfolyam": 10},
    {"nev": "Csilla", "evfolyam": 9},
    {"nev": "Dávid", "evfolyam": 11},
    {"nev": "Eszter", "evfolyam": 11},
    {"nev": "Fanni", "evfolyam": 10},
    {"nev": "Gergő", "evfolyam": 12},
    {"nev": "Hanna", "evfolyam": 11}
]

# Üres szótár az évfolyamok diákjainak számlálásához
evfolyam_szamlalo = {}

# Diákok évfolyamonkénti számlálása
for diak in diakok:
    evfolyam = diak['evfolyam']
    if evfolyam in evfolyam_szamlalo:
        evfolyam_szamlalo[evfolyam] += 1
    else:
        evfolyam_szamlalo[evfolyam] = 1

# Eredmény kiiratása
for evfolyam, darab in evfolyam_szamlalo.items():
    print(f"A(z) {evfolyam}. évfolyamon {darab} diák van.")