class Personne:
    def __init__(self, age=14, initials=''):
        self.age = age
        self.initials = initials

    def afficherAge(self):
        print("Tage de la personne : ", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouveauAge):
        self.age = nouveauAge

class Eleve(Personne):
    def __init__(self, age=14, initials=''):
        super().__init__(age, initials)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer pour la matière :", self.__matiereEnseignée)

# Instanciation des classes
personne = Personne()
eleve = Eleve()

# Affichage Tage par défaut de rélève en console
personne.afficherAge()
eleve.afficherAge()