class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Nom du compte: {self.__nom}")
        print(f"Prénom du compte: {self.__prenom}")
        print(f"Numéro de compte: {self.__num_compte}")
        print(f"Solde: {self.__solde}")

    def afficherSolde(self):
        print(f"Solde: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Nouveau solde: {self.__solde}")
        else:
            print("Erreur: Montant insuffisant")

    def agios(self):
        if self.__solde < 0:
            self.__solde += self.__solde * 0.05

    def virement(self, reference, montant):
        if reference.__solde >= montant:
            reference.__solde -= montant
            self.__solde += montant
            print("Virement effectué avec succès")
        else:
            print("Erreur: Montant insuffisant")

compte1 = CompteBancaire("001", "Dupont", "Pierre", 500, False)
compte2 = CompteBancaire("002", "Martin", "Lucas", -500, True)

compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.afficherSolde()
compte1.retrait(1000)
compte1.agios()
compte1.afficherSolde()
compte1.virement(compte2, 200)
compte2.afficherSolde()