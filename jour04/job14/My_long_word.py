
def my_long_word(nombre, chaîne):
    mots_filtrés = []
    mot_actuel = ""
    
    for caracter in chaîne:
        if caracter != " ":
            mot_actuel += caracter
        else:
            if len(mot_actuel) > nombre:
                mots_filtrés.append(mot_actuel)
            mot_actuel = ""
    
    if len(mot_actuel) > nombre:
        mots_filtrés.append(mot_actuel)
    
    return " ".join(mots_filtrés)

text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
résultat = my_long_word(3, text)
print(résultat)
