class Produit:
    def __init__(self, nom, prix_unitaire, quantite_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock

    def afficher_informations(self):
        print(f"Produit: {self.nom}")
        print(f"Prix unitaire: {self.prix_unitaire} euros")
        print(f"Quantité en stock: {self.quantite_stock} unités")

    def acheter_produits(self, quantite_achetee):
        if quantite_achetee <= self.quantite_stock:
            self.quantite_stock -= quantite_achetee
            print(f"{quantite_achetee} {self.nom}(s) acheté(s).")
        else:
            print(f"Stock insuffisant. Il ne reste que {self.quantite_stock} {self.nom}(s).")

    def ajuster_prix_inflation(self, pourcentage_augmentation):
        self.prix_unitaire *= (1 + pourcentage_augmentation / 100)
        print(f"Le prix unitaire a été ajusté en raison de l'inflation. Nouveau prix unitaire : {self.prix_unitaire} euros")


# Crecion del producto
produit1 = Produit(nom="Ordinateur portable", prix_unitaire=800, quantite_stock=50)

# mostrar el producto
produit1.afficher_informations()

# agregar productos en stock
quantite_achetee = int(input("Combien d'unités souhaitez-vous acheter ? "))
produit1.acheter_produits(quantite_achetee)

# Aumento del precio a causa de la inflacion
pourcentage_augmentation = 10
produit1.ajuster_prix_inflation(pourcentage_augmentation)

# Mostrar informacion de las actualizaciones del producto
produit1.afficher_informations()
