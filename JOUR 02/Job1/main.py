class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # mutateurs (setters)
    def set_longueur(self, valeur):
        if valeur > 0:
            self.__longueur = valeur
        else:
            print("La valeur doit être supérieure à 0.")

    def set_largeur(self, valeur):
        if valeur > 0:
            self.__largeur = valeur
        else:
            print("La valeur doit être supérieure à 0.")


# Création d'un rectangle
rectangle = Rectangle(10, 5)

# Affichage des attributs
print("Longueur:", rectangle.get_longueur())
print("Largeur:", rectangle.get_largeur())

# Modification des attributs
rectangle.set_longueur(20)
rectangle.set_largeur(10)

# Vérification des modifications
print("Longueur après modification:", rectangle.get_longueur())
print("Largeur après modification:", rectangle.get_largeur())