
hauteur = int(input("Inserez la hauteur du triangle: "))

for i in range(1, hauteur + 1):
    espaces = hauteur - i
    ligne = "_" * espaces + "\\" * i + "/" * i
    print(ligne)
    