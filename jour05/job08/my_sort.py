
def my_sort(liste):
    swaps = 0
    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                swaps += 1
                sorted = False

    print("Nombre total d'héchanges:", swaps)
    return liste

non_ordonné = [5, 2, 8, 1, 9]
ordonné = my_sort(non_ordonné)
print("Lista ordenada:", ordonné)
