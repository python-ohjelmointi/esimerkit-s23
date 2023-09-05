# ns. "vakiot"
PRONSSI = 50
HOPEA = 150
KULTA = 400
PLATINA = 2_000

# "muuttuvat" muuttujat:
ostot = 10

# logiikka, seuraavista ehdoista voi olla tosi *korkeintaan yksi*
if ostot >= PLATINA:
    alennusprosentti = 8
elif ostot >= KULTA:
    alennusprosentti = 6
elif ostot >= HOPEA:
    alennusprosentti = 4
elif ostot >= PRONSSI:
    alennusprosentti = 2
else:
    alennusprosentti = 0

summa = ostot * (100 - alennusprosentti) / 100

print(f'Ostostesi loppusumma on {summa}')
print(f'{ostot=} {alennusprosentti=}')
