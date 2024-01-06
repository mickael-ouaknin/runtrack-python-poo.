class Joueur:
    def __init__(self, nom, num, pos, nb_but, nb_passe, nb_carton_jaune, nb_carton_rouge):
        self.nom = nom
        self.num = num
        self.pos = pos
        self.nb_but = nb_but
        self.nb_passe = nb_passe
        self.nb_carton_jaune = nb_carton_jaune
        self.nb_carton_rouge = nb_carton_rouge

    def merquerUnBut(self):
        self.nb_but += 1

    def effectuerUnePasseDecisive(self):
        self.nb_passe += 1

    def recevoirUsCartonJaune(self):
        self.nb_carton_jaune += 1

    def recevoirUsCartonRouge(self):
        self.nb_carton_rouge += 1

    def afficherStatistiques(self):
        print("Nom : ", self.nom)
        print("Numéro : ", self.num)
        print("Position : ", self.pos)
        print("Nombre de buts : ", self.nb_but)
        print("Nombre de passes décisives : ", self.nb_passe)
        print("Nombre de cartons jaunes : ", self.nb_carton_jaune)
        print("Nombre de cartons rouges : ", self.nb_carton_rouge)


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, **kwargs):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                for cle, valeur in kwargs.items():
                    if cle == "buts":
                        joueur.nb_but += valeur
                    elif cle == "passe_decisives":
                        joueur.nb_passe += valeur
                    elif cle == "carton_jaunes":
                        joueur.nb_carton_jaune += valeur
                    elif cle == "carton_rouges":
                        joueur.nb_carton_rouge += valeur

# Exemple d'utilisation
joueur1 = Joueur("Zidane", 1, "Miracle", 5, 3, 1, 0)
joueur2 = Joueur("Henry", 10, "Ailier", 20, 5, 0, 0)

equipe1 = Equipe("Real Madrid")
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)

# Simuler un match, marquer un but, avoir un carton rouge..
joueur1.merquerUnBut()
joueur1.recevoirUsCartonRouge()

# Afficher à nouveau les statistiques des joueurs
equipe1.afficherStatistiquesJoueurs()

# Mettre à jour les statistiques d'un joueur
equipe1.mettreAJourStatistiquesJoueur("Zidane", buts=1, passe_decisives=1, carton_jaunes=1)

# Afficher à nouveau les statistiques des joueurs
equipe1.afficherStatistiquesJoueurs()