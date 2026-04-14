# Programme créé uniquement pour l'interface WEB

from flask import Flask, render_template, request, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = "secret123"

FICHIER = "users.json"


# Gestion utilisateurs

def charger_utilisateurs():
    if not os.path.exists(FICHIER):
        return {}
    with open(FICHIER, "r") as f:
        return json.load(f)


def sauvegarder_utilisateurs(users):
    with open(FICHIER, "w") as f:
        json.dump(users, f, indent=4)


# Routes


# Accueil
@app.route("/")
def index():
    return render_template("index.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = charger_utilisateurs()
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Identifiants incorrects"

    return render_template("login.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = charger_utilisateurs()
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "Utilisateur déjà existant"

        users[username] = {"password": password}
        sauvegarder_utilisateurs(users)

        return redirect("/login")

    return render_template("register.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html", user=session["user"])


# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# Lancement
if __name__ == "__main__":
    app.run(debug=True)
