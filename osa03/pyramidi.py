n = 10  # pyramidin kerrosten määrä

max_leveys = n * 2 + 1

leveys = 1
while leveys <= max_leveys:
    tahdet = '*' * leveys
    print(tahdet.center(max_leveys))
    leveys += 2
