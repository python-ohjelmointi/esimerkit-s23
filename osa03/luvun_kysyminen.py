prosentit = -1

while prosentit < 0 or prosentit > 100:
    prosentit = int(input("Syötä akun varaus prosentteina: "))  # 0-100

print(f"Akun varaus on {prosentit} %")
