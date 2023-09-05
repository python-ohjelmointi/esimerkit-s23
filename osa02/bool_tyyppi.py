# pylint: disable=comparison-of-constants
# tähän asti olemme tutustuneet `str` ja `int`-tyyppeihin
nimi = 'Toma'
ika = 7

print(type(nimi))
print(type(ika))

# vertailuoperaatioiden tuloksena syntyy totuusarvoja:
print(1 < 3)
print(type(1 < 3))

# totuusarvot `bool` voidaan asettaa muuttujiin kuten muutkin tyypit:
tosi = 1 < 3
print(tosi)
print(type(tosi))

# esim. numerot voidaan muuttaa totuusarvoiksi:
t = bool(1)  # nollasta poikkeavat numerot ovat True
f = bool(0)  # nolla on epätosi

print(t, f)


# pieni vinkki debuggaukseen: f-merkkijonoilla
# voidaan printata muuttujan nimi ja arvo
print(f'{nimi=} {ika=} {tosi=} {t=} {f=}')
# Tulostaa: nimi='Toma' ika=7 tosi=True t=True f=False
