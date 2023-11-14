# ...yhdistää jokin tieto toiseen...

postinumerot = {}

postinumerot['00100'] = 'helsinki'
postinumerot['00200'] = 'helsinki'
postinumerot['00730'] = 'helsinki'
postinumerot['99999'] = 'korvatunturi'

print(postinumerot)
print(postinumerot['00730'])

# ...ryhmitellä tietoa...
toimipaikat = {
    'helsinki': ['00100', '00200', '00730']
}


hki = toimipaikat['helsinki']
hki.append('00750')

print(toimipaikat)
