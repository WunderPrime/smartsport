joueurs = []

def ajouter_joueur():
    nom = input("Nom du joueur : ")
    joueurs.append(nom)
    print("Joueur ajouté avec succès.")

def afficher_joueurs():
    if len(joueurs) == 0:
        print("Aucun joueur inscrit.")
    else:
        print("Liste des joueurs :")
        for j in joueurs:
            print("-", j)

def supprimer_joueur():
    nom = input("Nom du joueur à supprimer : ")

    if nom in joueurs:
        joueurs.remove(nom)
        print("Joueur supprimé.")
    else:
        print("Joueur introuvable.")