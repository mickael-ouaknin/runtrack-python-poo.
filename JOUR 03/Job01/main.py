class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    def get_nom(self):
        return self.nom

    def get_population(self):
        return self.population

    def ajouter_population(self, nombre):
        self.population += nombre

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouter_population(self):
        self.ville.ajouter_population(1)


def main():
    paris = Ville("Paris", 1000000)
    marseille = Ville("Marseille", 861635)

    print("Population de Paris: ", paris.get_population())
    print("Population de Marseille: ", marseille.get_population())

    john = Personne("John", 45, paris)
    myrtille = Personne("Myrtille", 4, paris)
    chloe = Personne("Chloé", 18, marseille)

    john.ajouter_population()
    myrtille.ajouter_population()
    chloe.ajouter_population()

    print("Population de Paris après l'arrivée de John, Myrtille et Chloé: ", paris.get_population())
    print("Population de Marseille après l'arrivée de John, Myrtille et Chloé: ", marseille.get_population())

if __name__ == "__main__":
    main()