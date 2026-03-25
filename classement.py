from joueur import Joueur

def calculer_classement(matchs):
    scores = {}

    # Calcul des scores
    for match in matchs:
        j1, j2, s1, s2 = match  # on suppose que chaque match est un tuple (joueur1, joueur2, score1, score2)

        if j1.nom not in scores:
            scores[j1.nom] = 0
        if j2.nom not in scores:
            scores[j2.nom] = 0

        if s1 > s2:
            scores[j1.nom] += 3
        elif s2 > s1:
            scores[j2.nom] += 3
        else:
            scores[j1.nom] += 1
            scores[j2.nom] += 1

    # Tri du classement
    classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Classement ---")
    for i, (nom, pts) in enumerate(classement, 1):
        print(f"{i}. {nom} - {pts} pts")