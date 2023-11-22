
def fruit_et_legume(type, saison):
    if type == "fruit" and saison == "hiver":
        print("“orange, mandarine et kiwi”")
    elif type == "fruit" and saison == "été":
        print("“Poire, fraise, cassis”")
    elif type == "legume" and saison == "hiver":
        print("“carotte, topinambour, endive”")
    elif type == "legume" and saison == "été":
        print("“artichaut, aubergine,navet”")
    else:
        print("Type ou saison non valides")

fruit_et_legume("fruit", "hiver")  # Salida: Naranja, mandarina y kiwi
fruit_et_legume("fruit", "été")  # Salida: Pera, fresa, grosella
fruit_et_legume("legume", "hiver")  # Salida: Zanahoria, topinambur, endibia
fruit_et_legume("legume", "été")  # Salida: Alcachofa, berenjena, nabo
fruit_et_legume("salade", "printemps")  # Salida: Tipo o temporada no válidos
