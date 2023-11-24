
def échanges(liste):
    if len(liste) == 0:
        print("La liste est vide.")
    else:
        premier_élément = liste[0]
        dernier_élément = liste[-1]
        liste[0] = dernier_élément
        liste[-1] = premier_élément
        print("Liste après l'échange:", liste)

ma_liste = [1, 2, 3, 4, 5]
échanges(ma_liste)
