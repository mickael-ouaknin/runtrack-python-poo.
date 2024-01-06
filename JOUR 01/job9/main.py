class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        print(f"Nom du produit: {self.nom}")
        print(f"Prix HT: {self.prixHT}")
        print(f"TVA: {self.TVA}")
        print(f"Prix TTC: {self.CalculerPrixTTC()}")

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenir_nom(self):
        return self.nom

    def obtenir_prix(self):
        return self.prixHT


produit1 = Produit("Smartphone", 500, 20)
produit2 = Produit("Ordinateur", 1200, 10)
produit3 = Produit("Laptop", 900, 20)

produit1.afficher()
produit2.afficher()
produit3.afficher()

produit1.modifier_nom("Smartphone Modifié")
produit1.modifier_prix(550)
produit2.modifier_nom("Ordinateur Modifié")
produit2.modifier_prix(1250)
produit3.modifier_nom("Laptop Modifié")
produit3.modifier_prix(950)

print("Nouveaux prix des produits:")
print(produit1.obtenir_prix())
print(produit2.obtenir_prix())
print(produit3.obtenir_prix())