
# El algoritmo de Burbuja
# On utilise le "bubble sort"

def trier(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

liste_desordonée = [5, 2, 8, 1, 9]
liste_ordonée =trier(liste_desordonée)
print(liste_ordonée)
