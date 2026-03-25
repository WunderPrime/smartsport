from joueur import *
from tournois import *
from matchs import *
from classement import *

while True:

    print("\n SmartSport ")
    print("1. Ajouter joueur")
    print("2. Voir joueurs")
    print("3. Créer tournoi")
    print("4. Générer matchs")
    print("5. Voir matchs")
    print("6. Entrer scores")
    print("7. Classement")
    print("8. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        ajouter_joueur()

    elif choix == "2":
        afficher_joueurs()

    elif choix == "3":
        creer_tournoi()

    elif choix == "4":
        generer_matchs(get_joueurs())

    elif choix == "5":
        afficher_matchs()

    elif choix == "6":
        enregistrer_score()

    elif choix == "7":
        calculer_classement(get_matchs())

    elif choix == "8":
        print("Fin du programme")
        break

    else:
        print("Choix invalide")