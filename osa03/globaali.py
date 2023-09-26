
def tervehdi(nimi):
    print(f'hello {etunimi}')


if __name__ == '__main__':
    etunimi = 'Teemu'

    tervehdi(etunimi)


# tulostaa "hello Teemu", koska etunimi on globaali muuttuja ja tervehdi-funktiossa on bugi
tervehdi('kasper')
