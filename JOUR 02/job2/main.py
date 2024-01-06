class Livre:
    def __init__(self, titre='', auteur='', nombre_de_pages=0):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

# Instanciation de la classe Livre
livre = Livre('Le Petit Prince', 'Antoine de Saint-Exupéry', 96)

# Appel des méthodes
print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_nombre_de_pages())
livre.set_nombre_de_pages(120)
print(livre.get_nombre_de_pages())
