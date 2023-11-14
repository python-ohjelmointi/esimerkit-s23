mjono = 'kahvi'

print(mjono[0])  # k
print(len(mjono))  # 5
print(mjono[0:2])  # ka

# iterointi eli läpikäynti:
for kirjain in mjono:
    print(kirjain)

# plus- ja kertolasku:
print('maito' + mjono)
print(mjono * 5)

print('a' in mjono)
print(mjono.count('x'))
print(sorted(mjono))

print('\n' * 3)

paivat = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']

print(paivat[0])  # ma
print(len(paivat))  # 7
print(paivat[0:2])  # ['ma', 'ti']

# iterointi:
for pv in paivat:
    print(pv)

print(paivat + ['mon', 'tue', 'wed'])
print(paivat * 5)
print('ma' in paivat)
print(paivat.count('ma'))
print(sorted(paivat))
