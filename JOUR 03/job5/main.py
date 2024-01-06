class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 10
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige 10 points de dégâts!")

    def vérifierSanté(self):
        if self.vie <= 0:
            print(f"{self.nom} est KO!")
            return True
        else:
            print(f"{self.nom} a encore {self.vie} points de vie.")
            return False

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1-3): "))
        return self.niveau

    def lancerJeu(self):
        vie_joueur = 50 * self.niveau
        vie_ennemi = 40 * self.niveau

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while not joueur.vérifierSanté() and not ennemi.vérifierSanté():
            joueur.attaquer(ennemi)
            if joueur.vérifierSanté():
                break
            ennemi.attaquer(joueur)
            if ennemi.vérifierSanté():
                break

        if joueur.vérifierSanté():
            print(f"{joueur.nom} a gagné!")
        else:
            print(f"{ennemi.nom} a gagné!")

def main():
    jeu = Jeu()
    jeu.choisirNiveau()
    jeu.lancerJeu()

if __name__ == "__main__":
    main()