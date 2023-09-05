"""
"Vuosi on karkausvuosi, jos se on jaollinen 4:llä. Kuitenkin jos vuosi on jaollinen
100:lla, se on karkausvuosi vain silloin, kun se on jaollinen myös 400:lla."
https://ohjelmointi-23.mooc.fi/osa-2/3-ehtojen-yhdist%C3%A4minen#programming-exercise-karkausvuosi
"""

vuosi = 2024

# jaollisuus tarkastetaan jakojäännöksellä:
jaollinen_4 = vuosi % 4 == 0  # True, jos jaollinen neljällä
jaollinen_100 = vuosi % 100 == 0  # True, jos jaollinen 100:lla
jaollinen_400 = vuosi % 400 == 0  # True, jos jaollinen 400:lla

# https://github.com/python/cpython/blob/main/Lib/calendar.py#L141:
# year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

karkausvuosi = jaollinen_4 and (not jaollinen_100 or jaollinen_400)

if karkausvuosi:
    print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')

# muutama apuprintti debuggausta varten:
print(f'{vuosi=} {karkausvuosi=}')
print(f'{jaollinen_4=} {jaollinen_100=} {jaollinen_400=}')
