class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__liste_plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, plat, prix):
        self.__liste_plats[plat] = {"prix": prix, "statut": "en cours"}

    def annuler_commande(self):
        self.__statut = "annulée"
        for plat in self.__liste_plats:
            self.__liste_plats[plat]["statut"] = "annulée"

    def calculer_total(self):
        total = 0
        for plat in self.__liste_plats:
            if self.__liste_plats[plat]["statut"] != "annulée":
                total += self.__liste_plats[plat]["prix"]
        return total

    def afficher_commande(self):
        print(f"Commande n°{self.__numero} :")
        total = self.calculer_total()
        print(f"Total à payer : {total}€")
        for plat in self.__liste_plats:
            print(f"- {plat} : {self.__liste_plats[plat]['prix']}€ ({self.__liste_plats[plat]['statut']})")

    def calculer_TVA(self, taux):
        total = self.calculer_total()
        return total * taux / 100

# Utilisation de la classe
commande1 = Commande(1)
commande1.ajouter_plat("Spaghetti", 8)
commande1.ajouter_plat("Risotto", 12)
commande1.afficher_commande()

TVA = commande1.calculer_TVA(5.5)
print(f"TVA à payer : {TVA}€")

commande1.annuler_commande()
commande1.afficher_commande()