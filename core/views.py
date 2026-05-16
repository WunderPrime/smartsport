from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Player, Tournament, TournamentPhase, Match, Referee
from .forms import (
    RegisterForm, LoginForm, PlayerForm, RefereeForm,
    TournamentForm, TournamentPhaseForm, MatchForm, ScoreForm
)


# ─────────────────── AUTH ───────────────────

def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "core/index.html")


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Compte créé avec succès !")
        return redirect("dashboard")
    return render(request, "core/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request, request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("dashboard")
    return render(request, "core/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


# ─────────────────── DASHBOARD ───────────────────

@login_required
def dashboard(request):
    context = {
        "player_count": Player.objects.filter(owner=request.user).count(),
        "tournament_count": Tournament.objects.filter(owner=request.user).count(),
        "match_count": Match.objects.filter(owner=request.user).count(),
        "referee_count": Referee.objects.filter(owner=request.user).count(),
        "top_players": Player.objects.filter(owner=request.user).order_by("-points")[:3],
        "upcoming_matches": Match.objects.filter(
            owner=request.user, played=False, scheduled_at__isnull=False
        ).order_by("scheduled_at")[:5],
    }
    return render(request, "core/dashboard.html", context)


# ─────────────────── PLAYERS ───────────────────

@login_required
def players_view(request):
    form = PlayerForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        player = form.save(commit=False)
        player.owner = request.user
        player.save()
        messages.success(request, f"Joueur '{player.name}' ajouté.")
        return redirect("players")
    players = Player.objects.filter(owner=request.user)
    return render(request, "core/players.html", {"form": form, "players": players})


@login_required
def delete_player(request, pk):
    player = get_object_or_404(Player, pk=pk, owner=request.user)
    player.delete()
    messages.success(request, "Joueur supprimé.")
    return redirect("players")


# ─────────────────── REFEREES ───────────────────

@login_required
def referees_view(request):
    form = RefereeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        referee = form.save(commit=False)
        referee.owner = request.user
        referee.save()
        messages.success(request, f"Arbitre '{referee.full_name}' ajouté.")
        return redirect("referees")
    referees = Referee.objects.filter(owner=request.user)
    return render(request, "core/referees.html", {"form": form, "referees": referees})


@login_required
def delete_referee(request, pk):
    referee = get_object_or_404(Referee, pk=pk, owner=request.user)
    referee.delete()
    messages.success(request, "Arbitre supprimé.")
    return redirect("referees")


# ─────────────────── TOURNAMENTS ───────────────────

@login_required
def tournaments_view(request):
    form = TournamentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        t = form.save(commit=False)
        t.owner = request.user
        t.save()
        messages.success(request, f"Tournoi '{t.name}' créé.")
        return redirect("tournaments")
    tournaments = Tournament.objects.filter(owner=request.user)
    return render(request, "core/tournaments.html", {"form": form, "tournaments": tournaments})


@login_required
def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk, owner=request.user)
    phases = tournament.phases.prefetch_related("matches__player1", "matches__player2")
    phase_form = TournamentPhaseForm(request.POST or None)

    if request.method == "POST" and phase_form.is_valid():
        phase = phase_form.save(commit=False)
        phase.tournament = tournament
        phase.save()
        messages.success(request, f"Phase '{phase.name}' ajoutée.")
        return redirect("tournament_detail", pk=pk)

    # Avancement automatique : préparer les vainqueurs de la phase précédente
    current_phase = tournament.get_current_phase()
    previous_winners = []
    if current_phase:
        phases_list = list(phases)
        idx = next((i for i, p in enumerate(phases_list) if p.pk == current_phase.pk), None)
        if idx and idx > 0:
            previous_winners = phases_list[idx - 1].winners()

    return render(request, "core/tournament_detail.html", {
        "tournament": tournament,
        "phases": phases,
        "phase_form": phase_form,
        "current_phase": current_phase,
        "previous_winners": previous_winners,
    })


@login_required
def delete_tournament(request, pk):
    t = get_object_or_404(Tournament, pk=pk, owner=request.user)
    t.delete()
    messages.success(request, "Tournoi supprimé.")
    return redirect("tournaments")


@login_required
def delete_phase(request, pk):
    phase = get_object_or_404(TournamentPhase, pk=pk, tournament__owner=request.user)
    tournament_pk = phase.tournament.pk
    phase.delete()
    messages.success(request, "Phase supprimée.")
    return redirect("tournament_detail", pk=tournament_pk)


# ─────────────────── MATCHES ───────────────────

@login_required
def matches_view(request):
    form = MatchForm(request.user, request.POST or None)
    if request.method == "POST" and form.is_valid():
        match = form.save(commit=False)
        if match.player1 == match.player2:
            messages.error(request, "Les deux joueurs doivent être différents.")
        else:
            match.owner = request.user
            match.save()
            messages.success(request, "Match créé.")
            return redirect("matches")
    matches = Match.objects.filter(owner=request.user).select_related(
        "player1", "player2", "tournament", "phase", "referee"
    )
    return render(request, "core/matches.html", {"form": form, "matches": matches})


@login_required
def enter_score(request, pk):
    match = get_object_or_404(Match, pk=pk, owner=request.user)
    if match.played:
        messages.warning(request, "Ce match a déjà été joué.")
        return redirect("matches")
    form = ScoreForm(request.POST or None, instance=match)
    if request.method == "POST" and form.is_valid():
        match = form.save(commit=False)
        match.played = True
        match.save()
        messages.success(request, "Scores enregistrés et points mis à jour !")
        return redirect("matches")
    return render(request, "core/enter_score.html", {"form": form, "match": match})


@login_required
def delete_match(request, pk):
    match = get_object_or_404(Match, pk=pk, owner=request.user)
    match.delete()
    messages.success(request, "Match supprimé.")
    return redirect("matches")


# ─────────────────── RANKING ───────────────────

@login_required
def ranking_view(request):
    players = Player.objects.filter(owner=request.user).order_by("-points")
    return render(request, "core/ranking.html", {"players": players})


# ─────────────────── PROFILE ───────────────────

@login_required
def profile_view(request):
    return render(request, "core/profile.html")


@login_required
def change_username(request):
    if request.method == "POST":
        new_username = request.POST.get("username", "").strip()
        if not new_username:
            messages.error(request, "Le nom d'utilisateur ne peut pas être vide.")
        elif new_username == request.user.username:
            messages.warning(request, "C'est déjà ton nom d'utilisateur.")
        else:
            from django.contrib.auth.models import User
            if User.objects.filter(username=new_username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            else:
                request.user.username = new_username
                request.user.save()
                messages.success(request, "Nom d'utilisateur modifié avec succès !")
    return redirect("profile")


@login_required
def change_password(request):
    if request.method == "POST":
        current = request.POST.get("current_password", "")
        new = request.POST.get("new_password", "")
        confirm = request.POST.get("confirm_password", "")
        if not request.user.check_password(current):
            messages.error(request, "Mot de passe actuel incorrect.")
        elif len(new) < 8:
            messages.error(request, "Le nouveau mot de passe doit contenir au moins 8 caractères.")
        elif new != confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        else:
            request.user.set_password(new)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Mot de passe modifié avec succès !")
    return redirect("profile")


@login_required
def delete_account(request):
    if request.method == "POST":
        password = request.POST.get("password", "")
        if request.user.check_password(password):
            request.user.delete()
            return redirect("index")
        else:
            messages.error(request, "Mot de passe incorrect.")
    return redirect("profile")
