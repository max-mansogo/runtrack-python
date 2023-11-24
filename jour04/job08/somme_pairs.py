
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme_pairs = 0

for num in L:
    if num % 2 == 0:
        somme_pairs += num

print("La somme des valeurs pairs dans la liste est:", somme_pairs)
