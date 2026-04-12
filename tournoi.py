class Tournoi:
    def __init__(self, nom):
        self.nom = nom
        self.matchs = []


def creer_tournoi(liste_tournois):
    nom = input("Nom du tournoi : ")
    tournoi = Tournoi(nom)
    liste_tournois.append(tournoi)
    print(f"Tournoi '{nom}' créé avec succès.")
