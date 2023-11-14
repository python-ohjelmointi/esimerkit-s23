from collections import namedtuple

Movie = namedtuple("Movie", ["title", "year", "score"])

# source: ChatGPT (GPT-3.5)
leffat = [
    Movie("The Godfather", 1972, 9.2),
    Movie("Citizen Kane", 1941, 8.3),
    Movie("Schindler's List", 1993, 8.9),
    Movie("The Shawshank Redemption", 1994, 9.3),
    Movie("Pulp Fiction", 1994, 8.9),
    Movie("Casablanca", 1942, 8.5),
    Movie("Gone with the Wind", 1939, 8.1),
    Movie("The Godfather Part II", 1974, 9.0),
    Movie("The Dark Knight", 2008, 9.0),
    Movie("2001: A Space Odyssey", 1968, 8.3)
]

for leffa in leffat:
    print(leffa)

    # voimme käyttää indeksien sijasta nimiä:
    print(leffa.title, leffa.year, leffa.score)

    # myös indeksit toimivat:
    print(leffa[0], leffa[1], leffa[2])

    print()
