# liste pour stocker les matchs
matchs = []

# fonction pour créer un match
def creer_match(equipe1, equipe2):

    match = {
        "equipe1": equipe1,
        "equipe2": equipe2,
        "score1": None,
        "score2": None,
        "valide": False
    }

    matchs.append(match)

    print("Match créé :", equipe1, "vs", equipe2)


# fonction pour afficher les matchs
def afficher_matchs():

    if len(matchs) == 0:
        print("Aucun match programmé.")
        return

    for i, match in enumerate(matchs):

        print("\nMatch", i+1)
        print(match["equipe1"], "vs", match["equipe2"])

        if match["score1"] is None:
            print("Score : non enregistré")
        else:
            print("Score :", match["score1"], "-", match["score2"])


# fonction pour enregistrer le score
def enregistrer_score():

    afficher_matchs()

    if len(matchs) == 0:
        return

    choix = int(input("\nChoisir le numéro du match : ")) - 1

    if choix < 0 or choix >= len(matchs):
        print("Match invalide")
        return

    score1 = int(input("Score équipe 1 : "))
    score2 = int(input("Score équipe 2 : "))

    matchs[choix]["score1"] = score1
    matchs[choix]["score2"] = score2

    print("Score enregistré.")


# validation des scores par l'arbitre
def valider_score():

    afficher_matchs()

    choix = int(input("\nNuméro du match à valider : ")) - 1

    if choix < 0 or choix >= len(matchs):
        print("Match invalide")
        return

    matchs[choix]["valide"] = True

    print("Score validé par l'arbitre.")


# afficher les résultats
def afficher_resultats():

    print("\n===== RESULTATS =====")

    for match in matchs:

        if match["score1"] is not None:

            print(
                match["equipe1"],
                match["score1"],
                "-",
                match["score2"],
                match["equipe2"]
            )