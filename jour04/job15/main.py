
nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Función personalizada para redondear los números
def redondear(nombre):
    entier = int(nombre)
    decimal = nombre - entier
    if decimal >= 0.5:
        return entier + 1
    else:
        return entier

# Algoritmo de ordenamiento personalizado
def ordenar_lista(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Redondear los números de la lista
for i in range(len(nombres)):
    nombres[i] = redondear(nombres[i])

# Ordenar la lista
ordenar_lista(nombres)

print("Liste arrondi et ordonnée:", nombres)
