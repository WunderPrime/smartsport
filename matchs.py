import random


def generer_matchs(liste_joueurs, tournoi):
    if len(liste_joueurs) < 2:
        print("Il faut au moins 2 joueurs pour générer des matchs.")
        return
    tournoi.matchs.clear()
    joueurs = liste_joueurs.copy()
    random.shuffle(joueurs)
    for i in range(0, len(joueurs) - 1, 2):
        tournoi.matchs.append((joueurs[i], joueurs[i + 1]))
    print(f"{len(tournoi.matchs)} matchs générés pour le tournoi '{tournoi.nom}'.")


def afficher_matchs(tournoi):
    if not tournoi.matchs:
        print("Aucun match pour ce tournoi.")
        return
    print(f"\nMatchs du tournoi {tournoi.nom} :")
    for idx, (j1, j2) in enumerate(tournoi.matchs, 1):
        print(f"{idx}. {j1.nom} vs {j2.nom}")


def entrer_scores(tournoi):
    if not tournoi.matchs:
        print("Aucun match pour entrer des scores.")
        return
    for idx, (j1, j2) in enumerate(tournoi.matchs, 1):
        while True:
            try:
                score1 = int(input(f"Score {j1.nom} : "))
                score2 = int(input(f"Score {j2.nom} : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        if score1 > score2:
            j1.ajouter_points(3)
        elif score2 > score1:
            j2.ajouter_points(3)
        else:
            j1.ajouter_points(1)
            j2.ajouter_points(1)
