
def nombre_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

# Afficher les nombres premiers jusqu'à 1000
for nombre in range(2, 1001):
    if nombre_premier(nombre):
        print(nombre)
