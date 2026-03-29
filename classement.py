def classement_joueurs(liste_joueurs):
    return sorted(liste_joueurs, key=lambda j: j.score, reverse=True)

def afficher_classement(liste_joueurs):
    if not liste_joueurs:
        print("Pas de joueurs à classer.")
        return
    print("\n--- Classement des joueurs ---")
    classement = classement_joueurs(liste_joueurs)
    for idx, joueur in enumerate(classement, 1):
        print(f"{idx}. {joueur.nom} - {joueur.score} points")