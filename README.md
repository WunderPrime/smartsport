# 🏆 SmartSport

> Application web de gestion de tournois de tennis — joueurs, arbitres, matchs, phases et classements, le tout par utilisateur.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)

---

## 📸 Aperçu

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Gestion des joueurs
![Joueurs](screenshots/players.png)

### Tournois & Phases
![Tournois](screenshots/tournament_detail.png)

### Arbitres
![Arbitres](screenshots/referees.png)

### Matchs
![Matchs](screenshots/matches.png)

### Classement
![Classement](screenshots/ranking.png)

---

## ✨ Fonctionnalités

- 🔐 **Authentification complète** — inscription, connexion, déconnexion
- 👤 **Page profil** — modifier son nom d'utilisateur, mot de passe, supprimer son compte
- 🏅 **Gestion des joueurs** — ajouter, supprimer, suivre les points
- 🧑‍⚖️ **Gestion des arbitres** — profil complet (niveau local/régional/national), assignation aux matchs
- 🚩 **Gestion des tournois** — formats variés (poules, élimination directe, mixte), dates, lieu
- 📋 **Phases de tournoi** — quart de finale, demi-finale, finale et plus, avec avancement automatique ou manuel
- ⚔️ **Gestion des matchs** — création, planification date/heure, suivi du statut
- 📊 **Classement automatique** — points calculés en temps réel (victoire = 3pts, nul = 1pt, défaite = 0pt)
- 🔒 **Données isolées par utilisateur** — chaque compte ne voit que ses propres données

---

## 🛠️ Stack technique

| Technologie | Usage |
|-------------|-------|
| Python 3.11+ | Langage principal |
| Django 4.2 | Framework web |
| SQLite | Base de données |
| Bootstrap 5.3 | Interface utilisateur |
| Bootstrap Icons | Icônes |

---

## 🚀 Installation

### Prérequis

- Python 3.11+
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/WunderPrime/smartsport.git
cd smartsport

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Créer la base de données
python3 manage.py makemigrations core
python3 manage.py migrate

# 4. (Optionnel) Créer un accès admin
python3 manage.py createsuperuser

# 5. Lancer le serveur
python3 manage.py runserver
```

L'application est accessible sur **http://127.0.0.1:8000**

---

## 🐳 Docker

```bash
# Build
docker build -t smartsport .

# Run (avec persistance des données)
docker run -p 8000:8000 -v $(pwd)/db.sqlite3:/app/db.sqlite3 smartsport
```

---

## 📁 Structure du projet

```
smartsport/
│
├── manage.py
├── requirements.txt
├── Dockerfile
│
├── smartsport/              # Configuration Django
│   ├── settings.py
│   └── urls.py
│
└── core/                    # Application principale
    ├── models.py            # Player, Referee, Tournament, TournamentPhase, Match
    ├── views.py             # Logique métier
    ├── forms.py             # Formulaires
    ├── urls.py              # Routes
    └── templates/core/      # Templates HTML
        ├── base.html
        ├── dashboard.html
        ├── players.html
        ├── referees.html
        ├── tournaments.html
        ├── tournament_detail.html
        ├── matches.html
        ├── ranking.html
        └── profile.html
```

---

## 🗺️ Routes

| URL | Description |
|-----|-------------|
| `/` | Page d'accueil |
| `/register/` | Inscription |
| `/login/` | Connexion |
| `/dashboard/` | Tableau de bord |
| `/players/` | Gestion des joueurs |
| `/referees/` | Gestion des arbitres |
| `/tournaments/` | Gestion des tournois |
| `/tournaments/<id>/` | Détail & phases d'un tournoi |
| `/matches/` | Gestion des matchs |
| `/ranking/` | Classement |
| `/profile/` | Profil utilisateur |
| `/admin/` | Interface admin Django |

---

## 📐 Modèles de données

```python
Player          → owner (User), name, points
Referee         → owner (User), first_name, last_name, level, phone, email
Tournament      → owner (User), name, format, start_date, end_date, location
TournamentPhase → tournament, name, phase_type, order
Match           → owner, tournament, phase, player1, player2, referee,
                  scheduled_at, score1, score2, played, status
```

---

## 🔮 Améliorations prévues

- [ ] Génération automatique des matchs (tirage aléatoire)
- [ ] Historique détaillé par tournoi
- [ ] Pagination des listes
- [ ] Déploiement en ligne (Railway / Render)
- [ ] Passage à PostgreSQL en production
- [ ] Export PDF des résultats

---

## 👥 Auteurs

| Nom | GitHub |
|-----|--------|
| **Badr Badaoui** | [@badr](https://github.com/WunderPrime) |
| **Nariman Chebihi** | [@nariman](https://github.com/NarimanPrime) |
| **Othman Belfkih** | Aucun compte sur GitHub |

---

## 📄 Licence

EMSI License — libre d'utilisation et de modification.
