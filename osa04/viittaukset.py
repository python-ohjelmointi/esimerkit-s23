# list generated by ChatGPT
nordic_capitals = ['Copenhagen', 'Oslo', 'Stockholm', 'Helsinki', 'Reykjavik']

kaupungit = nordic_capitals

# tehdään lisäys kaupungit-muuttujaan:
kaupungit.append('Tallinn')

# muutos vaikuttaa molempiin muuttujiin:
print(f'{kaupungit=}')
print(f'{nordic_capitals=}')

# molempien muuttujien kautta käsitellään täsmälleen samaa listaa:
print(id(kaupungit))
print(id(nordic_capitals))

print('\n' * 3)

# list generated by ChatGPT
top_songs = ["Bohemian Rhapsody by Queen",
             "Imagine by John Lennon", "Hey Jude by The Beatles"]

my_top_songs = list(top_songs)
my_top_songs.append('Cha cha cha')

print(f'{top_songs=}')
print(f'{my_top_songs=}')
