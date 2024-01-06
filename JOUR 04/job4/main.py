class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, longueur=0, largeur=0):
        self.__longueur = longueur
        self.__largeur = largeur

    def aire(self):
        return self.__longueur * self.__largeur

# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 3)

# Appel de la méthode aire
print(rectangle.aire())
