
def parité(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            return "Le nombre {} est pair.".format(nombre)
        else:
            return "Le nombre {} est impair.".format(nombre)
    else:
        return "Le nombre doit être un entier positif"

print(parité(4)) 
print(parité(7)) 
print(parité(2.5))  
