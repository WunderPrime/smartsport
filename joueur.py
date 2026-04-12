class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def ajouter_points(self, points):
        self.score += points


def afficher_joueurs(liste_joueurs):
    if not liste_joueurs:
        print("Aucun joueur enregistré.")
        return
    print("Liste des joueurs :")
    for idx, joueur in enumerate(liste_joueurs, 1):
        print(f"{idx}. {joueur.nom} - Score: {joueur.score}")
