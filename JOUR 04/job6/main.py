class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque : ", self.marque)
        print("Model : ", self.modele)
        print("Année : ", self.annee)
        print("Prix : ", self.prix)

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de porte = ", self.portes)

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues = ", self.roues)

voiture = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
voiture.informationsVehicule()

moto = Moto("Harley-Davidson", "Street 750", 2020, 14999, 2)
moto.informationsVehicule()