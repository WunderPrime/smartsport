from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Player, Tournament, TournamentPhase, Match, Referee


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom du joueur"})}


class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        fields = ["first_name", "last_name", "level", "phone", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Prénom"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom"}),
            "level": forms.Select(attrs={"class": "form-select"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Téléphone (optionnel)"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email (optionnel)"}),
        }


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ["name", "format", "start_date", "end_date", "location"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom du tournoi"}),
            "format": forms.Select(attrs={"class": "form-select"}),
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Lieu (optionnel)"}),
        }


class TournamentPhaseForm(forms.ModelForm):
    class Meta:
        model = TournamentPhase
        fields = ["name", "phase_type", "order"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom de la phase"}),
            "phase_type": forms.Select(attrs={"class": "form-select"}),
            "order": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["tournament", "phase", "player1", "player2", "referee", "scheduled_at", "location", "notes"]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tournament"].queryset = Tournament.objects.filter(owner=user)
        self.fields["phase"].queryset = TournamentPhase.objects.filter(tournament__owner=user)
        self.fields["player1"].queryset = Player.objects.filter(owner=user)
        self.fields["player2"].queryset = Player.objects.filter(owner=user)
        self.fields["referee"].queryset = Referee.objects.filter(owner=user)
        for name, field in self.fields.items():
            if hasattr(field.widget, "attrs"):
                if isinstance(field.widget, forms.Select):
                    field.widget.attrs.update({"class": "form-select"})
                elif isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.update({"class": "form-control", "rows": 2})
                else:
                    field.widget.attrs.update({"class": "form-control"})
        self.fields["tournament"].required = False
        self.fields["phase"].required = False
        self.fields["referee"].required = False
        self.fields["scheduled_at"].required = False
        self.fields["scheduled_at"].widget = forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        )
        self.fields["location"].required = False
        self.fields["notes"].required = False


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["score1", "score2"]
        widgets = {
            "score1": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "score2": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }
