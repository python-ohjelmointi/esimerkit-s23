from pathlib import Path

polku = Path(__file__).parent / 'tallennettu.txt'

rivit = []

for x in range(10):
    rivit.append(f'Rivi {x}')

polku.write_text('\n'.join(rivit), encoding='utf-8')
