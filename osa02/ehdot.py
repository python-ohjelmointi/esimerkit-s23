kuukausi = 11

if 9 <= kuukausi <= 10:
    print('on syksy')

if 5 <= kuukausi <= 8:
    print('ok kesä')

if 3 <= kuukausi <= 4:
    print('on kevät')

if kuukausi <= 2 or kuukausi >= 11:
    print('on talvi')

# "For Boolean operations, all and operations are performed first,
# from left to right, then the or operations are performed."
# - https://realpython.com/lessons/operator-precedence/
# a and b or c and d
# (a and b) or (c and d)
# a and (b or c) and d

# 1 2   | 3 4   | 5 6 7 8 | 9 10  | 11 12
# talvi | kevät | kesä    | syksy | talvi
