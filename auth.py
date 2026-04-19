import json
import os
import re

FICHIER = "users.json"


# Charger les utilisateurs
def charger_utilisateurs():
    if not os.path.exists(FICHIER):
        return {}
    with open(FICHIER, "r") as f:
        return json.load(f)


# Sauvegarder
def sauvegarder_utilisateurs(users):
    with open(FICHIER, "w") as f:
        json.dump(users, f, indent=4)


# Créer compte
def creer_compte():
    users = charger_utilisateurs()

    username = input("Nom d'utilisateur : ")
    if username in users:
        print("Utilisateur déjà existant.")
        return

    password = input("Mot de passe : ")
    print(hash(password))

    valide, message = mot_de_passe_valide(password)
    if not valide:
        print("Erreur :", message)
        return

    users[username] = {
        "password": password
    }

    sauvegarder_utilisateurs(users)
    print("Compte créé avec succès.")


# Forcer mot de passe fort
def mot_de_passe_valide(password):
    if len(password) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères"

    if not re.search(r"[A-Z]", password):
        return False, "Ajouter une majuscule"

    if not re.search(r"[a-z]", password):
        return False, "Ajouter une minuscule"

    if not re.search(r"[0-9]", password):
        return False, "Ajouter un chiffre"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Ajouter un symbole"

    return True, "Mot de passe valide"



# Se connecter
def se_connecter():
    users = charger_utilisateurs()

    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    print(hash(password))

    if username in users and users[username]["password"] == password:
        print("Connexion réussie.")
        return username
    else:
        print("Identifiants incorrects.")
        return None


# Modifier profil
def modifier_profil(username):
    users = charger_utilisateurs()

    if username not in users:
        print("Utilisateur introuvable.")
        return

    new_password = input("Nouveau mot de passe : ")
    users[username]["password"] = new_password
    print(hash(new_password))

    sauvegarder_utilisateurs(users)
    print("Mot de passe modifié.")


# Supprimer compte
def supprimer_compte(username):
    users = charger_utilisateurs()

    if username in users:
        del users[username]
        sauvegarder_utilisateurs(users)
        print("Compte supprimé.")
    else:
        print("Utilisateur introuvable.")
