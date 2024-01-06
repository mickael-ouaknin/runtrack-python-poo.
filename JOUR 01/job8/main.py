import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changer_rayon(self, rayon):
        self.rayon = rayon

    def afficher(self):
        print(f"Le rayon du cercle est: {self.rayon}")
        print(f"L'aire du cercle est: {self.calculer_aire()}")
        print(f"Le périmètre du cercle est: {self.calculer_perimetre()}")

    def calculer_aire(self):
        return math.pi * self.rayon ** 2

    def calculer_perimetre(self):
        return 2 * math.pi * self.rayon


cercle = Cercle(5)
cercle.afficher()

cercle.changer_rayon(10)
cercle.afficher()