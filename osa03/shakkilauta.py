'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

from math import ceil


def venyta_merkkijonoa(mjono: str, pituus: int) -> str:
    venytetty = mjono * ceil(pituus / len(mjono))
    return venytetty[:pituus]


def shakkilauta(koko):
    # "101010"
    parillinen = venyta_merkkijonoa('10', koko)

    # "010101"
    pariton = venyta_merkkijonoa('01', koko)

    i = 0
    while i < koko:
        # https://stackoverflow.com/a/394814
        print(parillinen if i % 2 == 0 else pariton)
        i += 1


shakkilauta(10)
