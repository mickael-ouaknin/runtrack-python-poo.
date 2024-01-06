from math import pi

class Forme:
    def aire(self):
        raise NotImplementedError

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return pi * self.radius * self.radius

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote * self.cote

# Test
rectangle = Rectangle(4, 2)
cercle = Cercle(3)
carre = Carre(4)

print(f"Aire du rectangle : {rectangle.aire()}")
print(f"Aire du cercle : {cercle.aire()}")
print(f"Aire du carre : {carre.aire()}")