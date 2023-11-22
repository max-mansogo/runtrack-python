def String(langage):
    if langage == "Javascript":
        print('tu es un développeur web')
    elif langage == "Python":
        print('tu es un développeur IA')
    elif langage == "Java":
        print('tu es un développeur logiciel')
    elif langage == "reactjs":
        print('tu es un developpeur mobile')
    else:
        return "un jour, je serai le meilleur développeur... "

langage_utilisateur = input("Entrez votre langage de programmation : ")
String(langage_utilisateur)
