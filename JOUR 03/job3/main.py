class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

    def __str__(self):
        return f"{self.titre} - {self.description} - {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, index):
        del self.taches[index]

    def marquerCommeFinie(self, index):
        self.taches[index].statut = "terminer"

    def afficherListe(self):
        return "\n".join(str(tache) for tache in self.taches)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


# Création des tâches
tache1 = Tache("Faire le ménage", "Faire le ménage chaque semaine")
tache2 = Tache("Acheter du pain", "Acheter du pain chaque jour")
tache3 = Tache("Sortir avec les amis", "Sortir avec les amis chaque semaine")

# Ajout des tâches à la liste de tâches
listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)

# Suppression d'une tâche
listeDeTaches.supprimerTache(1)

# Modification du statut d'une tâche
listeDeTaches.marquerCommeFinie(0)

# Affichage de toutes les tâches
print(listeDeTaches.afficherListe())

# Affichage des tâches à faire
print("\nListe des tâches à faire :")
for tache in listeDeTaches.filterListe("à faire"):
    print(tache)