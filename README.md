# 🏆 SmartSport – Tournament Management System

## 📌 Description

**SmartSport** est une application développée en Python permettant de gérer des tournois sportifs et e-sportifs.
Le système permet d’ajouter des joueurs, créer des tournois, générer des matchs, enregistrer les scores et afficher un classement.

---

## 🚀 Fonctionnalités

### 👤 Gestion des utilisateurs

* Créer un compte
* Se connecter
* Modifier son profil
* Supprimer son compte

### 🧑‍🤝‍🧑 Gestion des joueurs

* Ajouter un joueur
* Afficher la liste des joueurs

### 🏆 Gestion des tournois

* Créer un tournoi
* Générer automatiquement des matchs

### 🎮 Gestion des matchs

* Afficher les matchs
* Entrer les scores

### 📊 Classement

* Calcul automatique des points
* Affichage du classement des joueurs

---

## 🛠️ Technologies utilisées

* Python 3
* JSON (pour la sauvegarde des utilisateurs)
* Flask

---

## 📂 Structure du projet

```
SmartSport/
│
├── main.py               # Interface menu pour choisir une option après l'authentification
├── app.py                # Application Flask (backend web)
├── joueur.py             # Gestion des joueurs (logique Python)
├── tournoi.py            # Gestion des tournois
├── matchs.py             # Génération et gestion des matchs
├── classement.py        # Classement des joueurs
├── auth.py              # Système d’authentification (si séparé)
│
├── users.json           # Base de données des utilisateurs (auto-générée)
│
├── templates/           # Interface web (frontend HTML)
│   ├── index.html       # Page d’accueil
│   ├── login.html       # Page de connexion
│   ├── register.html    # Page d’inscription
│   ├── dashboard.html   # Tableau de bord utilisateur
│
├── static/              # (optionnel mais recommandé)
│   ├── style.css        # Design du site
│   ├── script.js        # JavaScript (si besoin)
│
└── README.md            # Documentation du projet
```

---

## ▶️ Installation et exécution

### 1. Cloner le projet

```
git clone https://github.com/ton-username/smartsport.git
cd smartsport
```

### 2. Lancer le programme

```
python3 main.py
```

OU

## ▶️ Lancer l'application
```
python3 app.py
```
Puis ouvrir dans le navigateur :

http://127.0.0.1:5000

## ⚙️ Installation des dépendances
```
python3 -m pip install flask
```

---


## 💡 Exemple d’utilisation

1. Créer un compte
2. Se connecter
3. Ajouter des joueurs
4. Créer un tournoi
5. Générer des matchs
6. Entrer les scores
7. Voir le classement

---

## 📈 Améliorations possibles

* 💾 Sauvegarde des tournois
* 📱 Application mobile

---

## 👨‍💻 Auteur

Projet réalisé par Badr BADAOUI, Narimane CHEBIHI, Othmane BELFKIH

---

## 📄 Licence

Ce projet est libre d’utilisation à des fins éducatives.
