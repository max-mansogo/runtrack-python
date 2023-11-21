
def type_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or b == c or a == c:
        return "isocèle"
    else:
        return "quelconque"

def est_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

# Demander à l'utilisateur de saisir les longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérifier si les longueurs forment un triangle
if est_triangle(a, b, c):
    print("Les longueurs peuvent former un triangle de type", type_triangle(a, b, c))
    # Vérifier si le triangle est rectangle
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("Le triangle est également rectangle.")
else:
    print("Les longueurs ne peuvent pas former un triangle.")
