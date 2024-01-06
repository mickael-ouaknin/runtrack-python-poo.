class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

personne1 = Personne("Kevin", "Mistigri")
personne2 = Personne("Harry", "Jean")

print(personne1.SePresenter())
print(personne2.SePresenter())