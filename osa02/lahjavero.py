'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

lahja = int(input("Lahjan suuruus? "))
rajavero = 0
raja = 0
prosentti = 0.0

if lahja >= 1_000_000:
    rajavero = 142_100
    raja = 1_000_000
    prosentti = 0.17

elif lahja >= 200_000:
    rajavero = 22_100
    raja = 200_000
    prosentti = 0.15

elif lahja >= 55_000:
    rajavero = 4_700
    raja = 55_000
    prosentti = 0.12

elif lahja >= 25_000:
    rajavero = 1_700
    raja = 25_000
    prosentti = 0.10

elif lahja >= 5_000:
    rajavero = 100
    raja = 5_000
    prosentti = 0.08


vero = rajavero + (lahja - raja) * prosentti

if vero == 0:
    print("Ei veroa!")
else:
    print(f"Vero: {vero} euroa")
