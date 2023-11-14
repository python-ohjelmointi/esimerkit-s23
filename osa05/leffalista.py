teksti = '''
The Godfather (1972)
Citizen Kane (1941)
Schindler's List (1993)
The Shawshank Redemption (1994)
Pulp Fiction (1994)
Casablanca (1942)
Gone with the Wind (1939)
The Godfather Part II (1974)
The Dark Knight (2008)
2001: A Space Odyssey (1968)
'''.strip()


def find_line_with_str(lines: list, search: str):
    for i, line in enumerate(lines):
        if search in line:
            return i, line

    raise ValueError('not found')


rivit = teksti.splitlines()

indeksi, rivi = find_line_with_str(rivit, 'Knight')

print((indeksi, rivi))
print(find_line_with_str(rivit, 'Casa'))
