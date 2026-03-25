import joueur
from matchs import jouer_match

joueurs = []
matchs = []
tournois = []

def ajouter_joueur():
    nom = input("Nom du joueur : ")
    joueurs.append(joueur.Joueur(nom))
    print(f"Joueur {nom} ajouté !")

def get_joueurs():
    return joueurs

def afficher_joueurs():
    if not joueurs:
        print("Aucun joueur enregistré.")
        return
    print("\n--- Joueurs ---")
    for i, j in enumerate(joueurs, 1):
        print(f"{i}. {j.nom}")

def creer_tournoi():
    nom = input("Nom du tournoi : ")
    tournois.append({"nom": nom, "joueurs": joueurs.copy()})
    print(f"Tournoi {nom} créé avec {len(joueurs)} joueurs !")

def generer_matchs(joueurs_tournoi):
    matchs.clear()  # réinitialise les matchs pour le tournoi
    for i in range(len(joueurs_tournoi)):
        for j in range(i+1, len(joueurs_tournoi)):
            matchs.append((joueurs_tournoi[i], joueurs_tournoi[j], 0, 0))  # scores initiaux à 0
    print(f"{len(matchs)} matchs générés.")

def get_matchs():
    return matchs

def afficher_matchs():
    if not matchs:
        print("Aucun match généré.")
        return
    print("\n--- Matchs ---")
    for i, (j1, j2, s1, s2) in enumerate(matchs, 1):
        print(f"{i}. {j1.nom} ({s1}) vs {j2.nom} ({s2})")

def enregistrer_score():
    if not matchs:
        print("Aucun match à scorer.")
        return
    afficher_matchs()
    num = int(input("Numéro du match à scorer : ")) - 1
    if num < 0 or num >= len(matchs):
        print("Match invalide.")
        return
    s1 = int(input(f"Score {matchs[num][0].nom} : "))
    s2 = int(input(f"Score {matchs[num][1].nom} : "))
    j1, j2, _, _ = matchs[num]
    matchs[num] = (j1, j2, s1, s2)
    print("Score enregistré !")