'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''
from math import ceil


def nelio(merkit: str, koko: int):
    pinta_ala = koko ** 2
    kerroin = ceil(pinta_ala / len(merkit))

    boksi = merkit * kerroin

    i = 0
    while i < koko:
        # indeksi, josta tämä rivi `i` alkaa:
        indeksi = koko * i

        print(boksi[indeksi:indeksi + koko])
        i += 1
