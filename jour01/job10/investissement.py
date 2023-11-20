
montant_initial = 10000  # Monto inicial de la inversion en euros
taux_rendement_annuel = 5  # Tasa del rendimiento anual en porcentaje

# Affichage du gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel} euros")

# Aumento del capital y de la tasa de rendimiento
montant_initial += 5000
taux_rendement_annuel += 2

# xalcular y mostrar de buevo la ganancia anual
gain_annuel_nouveau = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel : {gain_annuel_nouveau} euros")

# Retiro de un 10% del monto inicial y disminucion del rendimiento
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calculo del monto final de la inversion
montant_final = montant_initial + gain_annuel_nouveau

# Mostrar el nuevo monto y las ganancias proporcionadas
print(f"Montant final de l'investissement : {montant_final} euros")
