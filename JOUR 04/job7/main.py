class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def valeur_carte(self):
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        elif self.valeur == 'A':
            return 11
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        self.cartes = [Carte(valeur, couleur) for valeur in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for couleur in ['Coeur', 'Carreau', 'Trefle', 'Pique']]

# Instanciation de la classe Jeu
jeu = Jeu()

# Affichage de la valeur de la première carte du jeu
print(jeu.cartes[0].valeur_carte())
