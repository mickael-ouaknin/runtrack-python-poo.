class Rectangle:
    def __init__(self, longueur=0, largeur=0):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur=0, largeur=0, hauteur=0):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 3)
print(rectangle.perimetre())
print(rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(5, 3, 2)
print(parallelepipede.volume())
