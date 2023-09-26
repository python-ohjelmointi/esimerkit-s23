def kysy_luku(kysymys: str) -> int:
    while True:
        vastaus = input(kysymys)
        if vastaus.isdigit():
            return int(vastaus)


while True:
    luku = kysy_luku('Syötä luku väliltä 0-100: ')
    if 0 <= luku <= 100:
        print(f'Syötit luvun {luku}')
        break
