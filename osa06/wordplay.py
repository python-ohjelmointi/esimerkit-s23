from pathlib import Path

fin = Path(__file__).parent / 'kaikkisanat.txt'
swe = Path(__file__).parent / 'swe_wordlist.txt'

finnish = fin.read_text(encoding='utf-8').splitlines()
swedish = swe.read_text(encoding='utf-8').splitlines()

print(len(finnish))  # 93086
print(len(swedish))  # 410786

print(len(finnish) * len(swedish))  # 38 238 425 596 -> 93 086

# "dict comprehension"
swe_dict = {s: False for s in swedish}

for word in finnish:  # 93086
    if word in swe_dict:  # 1
        print(word)
