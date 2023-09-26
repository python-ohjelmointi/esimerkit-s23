import math
import random

print(math.__name__)    # "math"
print(random.__name__)  # "random"

# Kun tiedosto on "pääohjelma", tulostuu "__main__", muulloin
# tulostuu moduulin tiedostonimi eli "name_testi"
print(__name__)

if __name__ == "__main__":
    print("pääohjelma")
