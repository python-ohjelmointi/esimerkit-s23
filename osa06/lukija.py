from pathlib import Path

polku = Path(__file__).parent / 'esimerkki.txt'

if polku.exists():
    sisalto = polku.read_text(encoding='utf-8')
    for x in sisalto.splitlines():
        print(x)
else:
    print('tiedostoa ei löytynyt')
