
def les_notes(notes):
    résultats_arrondis = []
    for note in notes:
        if note >= 40 and note % 5 >= 3:
            arrondi = note + (5 - (note % 5))
        else:
            arrondi = note
        résultats_arrondis.append(arrondi)
    return résultats_arrondis

notes = [83, 82, 75, 68, 91]
résultats_arrondis = les_notes(notes)
print(résultats_arrondis)
