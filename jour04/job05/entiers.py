
L = [1, 2, 3, 4, 5]
# Afficher la deuxième valeur de la liste
print(L[1])

# Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4], puis afficher à nouveau le tableau.
def actualizar_lista(lista):
    lista[3] = lista[2] + lista[4]

actualizar_lista(L)
print(L)

# Puis afficher la dernière valeur de la liste.
print(L[-1])
