class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        return f"Bonjour, {self.nom} !"


class Eleve(Personne):
    def __init__(self, nom, age=15):
        super().__init__(nom, age)

    def allerEnCours(self):
        return "Je vais en cours."


class Professeur(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)
        self.matiere = matiere

    def enseigner(self):
        return f"Je vais enseigner {self.matiere}."


eleve = Eleve("Alice")
print(eleve.bonjour())
print(eleve.allerEnCours())

professeur = Professeur("Bob", 40, "Mathématiques")
print(professeur.bonjour())
print(professeur.enseigner())