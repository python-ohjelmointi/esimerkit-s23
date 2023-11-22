from pathlib import Path

print(f'{__file__=}')

polku = Path(__file__)
parent = polku.parent
esimerkki = parent / 'esimerkki.txt'

print(f'{polku=}')
print(f'{parent=}')
print(f'{esimerkki=}')

print(polku.exists())
