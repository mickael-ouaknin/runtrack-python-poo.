class Livre:
    def __init__(self, titre='', auteur='', nombre_de_pages=0):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    # ... autres méthodes ...

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print("Erreur : Le livre n'est pas disponible.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
        else:
            print("Erreur : Le livre n'a pas été emprunté.")

# Instanciation de la classe Livre
livre = Livre('Le Petit Prince', 'Antoine de Saint-Exupéry', 96)

# Appel des méthodes
print(livre.verification())
livre.emprunter()
print(livre.verification())
livre.rendre()
print(livre.verification())
