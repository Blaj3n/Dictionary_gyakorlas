'''

Egy dictionary (szótár) a Pythonban egy olyan adattípus, amely kulcs-érték párokat tárol. Így tudsz vele dolgozni:

A kulcs egyedi, és segítségével lehet az értéket elérni.
Az értékek lehetnek bármilyen típusúak (szám, string, lista, stb.), míg a kulcsok általában
stringek vagy számok.

'''


'''
Ebben a példában a diak egy dictionary, ami három kulcsot tartalmaz: "nev", "kor", és "tantargyak".
A kulcsokhoz tartozó értékek: "Anna", 18, és egy lista a tantárgyakról.
'''
diak = {
    "nev": "Anna",
    "kor": 18,
    "tantargyak": ["matek", "fizika", "kémia"]
}
# Alapvető műveletek
# 1. Érték elérése kulccsal
# print(diak["nev"])  # Eredmény: Anna

# 2. Érték hozzáadása vagy módosítása
diak["kor"] = 19    # Módosítja a kor értékét
diak["osztaly"] = "12.A"    # Új kulcs-érték pár hozzáadása

# 3. Kulcs-érték pár törlése
del diak["tantargyak"]  # Törli a tantárgyakat


# Dictionary Műveletek
'''
1. Összes kulcs és érték kiírása
    A .keys() metódus segítségével ki tudod nyerni az összes kulcsot.
    A .values() metódus pedig az összes értéket adja vissza.
'''
print("1. Összes kulcs és érték kiírása")
print("Kulcsok:")
for kulcs in diak.keys():
    print(f"\t {kulcs}")
print("Értékek:")
for ertek in diak.values():
    print(f"\t {ertek}")

print("")

'''
2. Kulcs-érték pár bejárása
    A .items() metódussal egy ciklusban végig tudsz menni az összes kulcs-érték páron
'''

print("2. Kulcs-érték pár bejárása:")
for kulcs, ertek in diak.items():
    print(f"\tKulcs: {kulcs}, Érték: {ertek}")
print("")
for kulcs, ertek in diak.items():
    print(f"\t{kulcs}: {ertek}")
print("")
'''
3. Kulcsok ellenőrzése
    Ellenőrizheted, hogy egy kulcs létezik-e a dictionary-ban az in operátorral
'''
print("3. Kulcsok ellenőrzése:")
if "nev" in diak:
    print("\tA név kulcs létezik.")
if "osztalyzat" not in diak:
    print("\tAz osztályzat kulcs nem létezik.")

print("")

'''
4. Dictionary másolása
    A copy() metódussal másoaltot készíthetsz a dictionary-ról, ami hasznos lehet, ha módosítani szeretnéd
    anélkül, hogy az eredetit megváltoztatnád
'''
diak_masolat = diak.copy()

print("4. A diák dictionary másolata: ")
print(f"\t{diak_masolat}")

print("")
'''
5. Dictionary törlése
    A clear() metódus törli az összes kulcs-érték párt a dictionary-ból
'''
print(f"5. Dictionary törlése: \n \t diak.clear()")

print("")

'''
6. Kulcs-érték pár hozzáadása vagy módosítása
    Ha egy kulcs már létezik, a hozzárendelés felülírja az értéket.
    Ha nem létezik, akkor új párt hoz létre
'''

'''
6.1 Kulcs-érték pár hozzáadása
    Ha egy új kulcsot és értéket szeretnél hozzáadni egy szótárhoz, egyszerűen rendelj egy értéket a kulcshoz.
    Ha a kulcs még nem létezik, akkor a Python automatikusan létrehozza azt.
'''

print("6.1 Kulcs-érték pár hozzáadása: ")

diakok = {
    'nev': 'Tamás',
    'kor': 16
}
print("\t6.1.1 Diákok dictionary Új kulcs-érték pár hozzáadása előtt: ")
print(f"\t\t{diakok}")

diakok['osztaly'] = '10.A'

print("\t6.1.2 Diákok dictionary Új kulcs-érték pár hozzáadása után: ")
print(f"\t\t{diakok}")

'''
6.2 Kulcs-érték pár módosítása
    Ha egy létező kulcs értékét szeretnéd megváltoztatni, akkor csak rendelj egy új értéket a kulcshoz.
    Az érték frissülni fog, ha a kulcs már létezik a szótárban.
'''

diakok_2 = {
    'nev': 'Tamás',
    'kor': 16
}

print("6.2 Kulcs-érték pár módosítása: ")
print("\t6.2.1 Diákok dictionary Új kulcs-érték pár módosítása előtt: ")
print(f"\t\t{diakok_2}")

diakok_2['kor'] = 18

print("\t6.2.2 Diákok dictionary Új kulcs-érték pár módosítása után: ")
print(f"\t\t{diakok_2}")