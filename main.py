from joueur import Joueur, afficher_joueurs
from tournoi import Tournoi, creer_tournoi
from matchs import generer_matchs, afficher_matchs, entrer_scores
from classement import afficher_classement

liste_joueurs = []
liste_tournois = []

while True:
    print("\n=== SmartSport ===")
    print("1. Ajouter joueur")
    print("2. Voir joueurs")
    print("3. Créer tournoi")
    print("4. Générer matchs")
    print("5. Voir matchs")
    print("6. Entrer scores")
    print("7. Classement")
    print("8. Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        nom = input("Nom du joueur : ")
        liste_joueurs.append(Joueur(nom))
        print(f"Joueur '{nom}' ajouté.")
    elif choix == "2":
        afficher_joueurs(liste_joueurs)
    elif choix == "3":
        creer_tournoi(liste_tournois)
    elif choix == "4":
        if not liste_tournois:
            print("Aucun tournoi créé.")
            continue
        print("Sélectionner le tournoi :")
        for idx, t in enumerate(liste_tournois, 1):
            print(f"{idx}. {t.nom}")
        sel = int(input("Numéro : ")) - 1
        generer_matchs(liste_joueurs, liste_tournois[sel])
    elif choix == "5":
        if not liste_tournois:
            print("Aucun tournoi créé.")
            continue
        for t in liste_tournois:
            afficher_matchs(t)
    elif choix == "6":
        if not liste_tournois:
            print("Aucun tournoi créé.")
            continue
        for t in liste_tournois:
            entrer_scores(t)
    elif choix == "7":
        afficher_classement(liste_joueurs)
    elif choix == "8":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, réessayez.")