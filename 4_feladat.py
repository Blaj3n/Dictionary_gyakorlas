'''
4. Statisztika
Készíts egy dictionary-t, ami az osztály összes diákjának nevét és a matek dolgozatuk eredményét tartalmazza.

Feladat:

Számold ki az osztály átlagát.
Írd ki azokat a diákokat, akik a dolgozaton 70 pontnál többet kaptak.
'''

diakok = [
    {"nev": "Dávid", "osztalyzat": 3, "elert_pontszam": 65},
    {"nev": "Oszkár", "osztalyzat": 4, "elert_pontszam": 75},
    {"nev": "Bence", "osztalyzat": 5, "elert_pontszam": 91},
    {"nev": "Gergő", "osztalyzat": 3, "elert_pontszam": 60},
    {"nev": "Bálint", "osztalyzat": 4, "elert_pontszam": 78},
    {"nev": "Benjámin", "osztalyzat": 1, "elert_pontszam": 15},
    {"nev": "Kinga", "osztalyzat": 2, "elert_pontszam": 30},
    {"nev": "Polka", "osztalyzat": 3, "elert_pontszam": 55},
    {"nev": "Eszter", "osztalyzat": 1, "elert_pontszam": 5},
]
# Összesített osztályzat
osszes_osztalyzat = 0

# Összeadja az összes osztályzatot
for diak in diakok:
    osszes_osztalyzat += diak['osztalyzat']

# Számolja az átlagot
matek_atlag = osszes_osztalyzat / len(diakok)

print(f"A matek tantárgy átlaga: {matek_atlag:.2f}")

osszes_pont = 0

for diak in diakok:
    osszes_pont += diak['elert_pontszam']

pont_atlag = osszes_pont / len(diakok)


print(f"A matek pontszámok átlaga: {pont_atlag:.2f}")