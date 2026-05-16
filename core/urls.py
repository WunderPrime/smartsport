from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # Players
    path("players/", views.players_view, name="players"),
    path("players/delete/<int:pk>/", views.delete_player, name="delete_player"),
    # Referees
    path("referees/", views.referees_view, name="referees"),
    path("referees/delete/<int:pk>/", views.delete_referee, name="delete_referee"),
    # Tournaments
    path("tournaments/", views.tournaments_view, name="tournaments"),
    path("tournaments/<int:pk>/", views.tournament_detail, name="tournament_detail"),
    path("tournaments/delete/<int:pk>/", views.delete_tournament, name="delete_tournament"),
    path("phases/delete/<int:pk>/", views.delete_phase, name="delete_phase"),
    # Matches
    path("matches/", views.matches_view, name="matches"),
    path("matches/score/<int:pk>/", views.enter_score, name="enter_score"),
    path("matches/delete/<int:pk>/", views.delete_match, name="delete_match"),
    # Ranking
    path("ranking/", views.ranking_view, name="ranking"),
    # Profile
    path("profile/", views.profile_view, name="profile"),
    path("profile/username/", views.change_username, name="change_username"),
    path("profile/password/", views.change_password, name="change_password"),
    path("profile/delete/", views.delete_account, name="delete_account"),
]
