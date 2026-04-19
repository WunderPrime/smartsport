from flask import Flask, render_template, request, redirect, session
from utils import load_data, save_data

app = Flask(__name__)
app.secret_key = "smartsport_secret"


# ---------------- HOME ----------------
@app.route("/")
def index():
    if "user" in session:
        return redirect("/dashboard")
    return render_template("index.html")


# ---------------- AUTH ----------------
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = load_data("users.json")

        users.append({
            "username": request.form["username"],
            "password": request.form["password"]
        })

        save_data("users.json", users)
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        users = load_data("users.json")

        for u in users:
            if u["username"] == request.form["username"] and u["password"] == request.form["password"]:
                session["user"] = u["username"]
                return redirect("/dashboard")

        return "Login incorrect"

    return render_template("login.html")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")

    return render_template("profile.html", user=session["user"])


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html", user=session["user"])


# ===================== PLAYERS =====================

@app.route("/players")
def players():
    players = load_data("players.json")
    return render_template("players.html", players=players)


@app.route("/add_player", methods=["POST"])
def add_player():
    players = load_data("players.json")

    players.append({
        "id": len(players) + 1,
        "name": request.form["name"],
        "points": 0
    })

    save_data("players.json", players)

    return redirect("/players")


# ===================== TOURNAMENTS =====================

@app.route("/tournaments")
def tournaments():
    tournaments = load_data("tournaments.json")
    return render_template("tournaments.html", tournaments=tournaments)


@app.route("/add_tournament", methods=["POST"])
def add_tournament():
    tournaments = load_data("tournaments.json")

    tournaments.append({
        "id": len(tournaments) + 1,
        "name": request.form["name"]
    })

    save_data("tournaments.json", tournaments)

    return redirect("/tournaments")


# ===================== MATCHES =====================

@app.route("/matches")
def matches():
    matches = load_data("matches.json")
    return render_template("matches.html", matches=matches)


@app.route("/add_match", methods=["POST"])
def add_match():
    matches = load_data("matches.json")

    matches.append({
        "id": len(matches) + 1,
        "team1": request.form["team1"],
        "team2": request.form["team2"],
        "score1": 0,
        "score2": 0
    })

    save_data("matches.json", matches)

    return redirect("/matches")


# ===================== RANKING =====================

@app.route("/ranking")
def ranking():
    players = load_data("players.json")
    players = sorted(players, key=lambda x: x["points"], reverse=True)

    return render_template("ranking.html", players=players)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)