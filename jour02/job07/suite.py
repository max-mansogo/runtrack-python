
la_base = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de caractères à afficher par ligne
caracteres_por_linea = 1

# Afficher la suite pyramidale
for i in range(len(la_base)):
    print(la_base[:caracteres_por_linea].center(30))
    caracteres_por_linea += 2
