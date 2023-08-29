DISCLAIMER = '''
Voit kokeilla tämän laskurin avulla, minkä loppuarvosanan eri
osasuoritukset tuottavat. Viikkotehtävien pistemäärän voit
tarkastaa osoitteesta https://tmc.mooc.fi/org/haaga-helia/
tai VS Code:n TMC-laajennoksen "My Courses"-näkymästä.

* Viikkotehtävien painoarvo on 50 %
* Kokeen painoarvo on 50 %

Tässä laskurissa mahdollisesti esiintyvät bugit ja virheet eivät
muuta tai korvaa virallista arviointia ja siihen liittyvää kaavaa.
Laskuri antaa vain ei-sitovan arvion loppuarvosanasta.
'''


# Viikkotehtävien arviointi lasketaan siten, että 25 % tehtäväpisteistä oikeuttaa
# arvosanaan 1, kun taas 100 % tehtäväpisteistä oikeuttaa arvosanaan 5.
MAX_TEHTAVAPISTEET = 201
MIN_TEHTAVAPISTEET = 0.25 * MAX_TEHTAVAPISTEET


def laske_tehtavien_arvosana(tehtavapisteet: int) -> float:
    '''
    Laskee tehtävien arvosanan asteikolla 0-5 annetun pistemäärän perusteella.

    >>> laske_tehtavien_arvosana(201)
    5.0
    >>> laske_tehtavien_arvosana(10)
    0.0
    >>> 4.0 < laske_tehtavien_arvosana(165) < 4.05
    True
    '''
    assert 0 <= tehtavapisteet <= MAX_TEHTAVAPISTEET, 'Virheellinen tehtäväpistemäärä'

    if tehtavapisteet < MIN_TEHTAVAPISTEET:
        return 0.0

    return 1 + 4 * (tehtavapisteet - MIN_TEHTAVAPISTEET) / (MAX_TEHTAVAPISTEET - MIN_TEHTAVAPISTEET)


def pyorista(arvosana: float) -> int:
    '''
    Pyorista-funktio "korjaa" round-funktion ominaisuuden, jossa puolikkaat pyöristetään
    aina lähimpään parilliseen lukuun:

    >>> round(4.5)
    4

    Arvosanoja laskiessamme haluamme pyöristää puolikkaat kuten 4.5 aina ylöspäin, esim:

    >>> pyorista(4.5)
    5
    >>> pyorista(3.5)
    4
    >>> pyorista(3.3)
    3
    >>> pyorista(3.6)
    4
    '''

    # Lähde: https://stackoverflow.com/a/45424214
    return int(arvosana + 0.5)


def main():
    print(DISCLAIMER)

    teht_pisteet = int(
        input(f'Syötä tehtäväpisteiden määrä (0-{MAX_TEHTAVAPISTEET}): ')
    )
    teht_arvosana = laske_tehtavien_arvosana(teht_pisteet)

    print(f'{teht_pisteet} tehtäväpistettä vastaa arvosanaa {teht_arvosana:.2f}')
    print()

    koe_arvosana = float(input('Syötä kokeen arvosana (0.0-5.0): '))
    assert 0 <= koe_arvosana <= 5, 'Virheellinen koearvosana'

    print()

    if teht_arvosana >= 1 and koe_arvosana >= 1:
        arvosana = teht_arvosana * 0.5 + koe_arvosana * 0.5

        print(f'Loppuarvosana on {pyorista(arvosana)} ({arvosana:.2f})')

    else:
        print('Suoritusta tulee täydentää')


if __name__ == '__main__':
    main()
