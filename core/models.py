from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return self.name


class Referee(models.Model):
    LEVEL_CHOICES = [
        ("local", "Local"),
        ("regional", "Régional"),
        ("national", "National"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referees")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="local")
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_level_display()})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Tournament(models.Model):
    FORMAT_CHOICES = [
        ("groups", "Phase de poules"),
        ("knockout", "Élimination directe"),
        ("mixed", "Poules + Élimination"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tournaments")
    name = models.CharField(max_length=100)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default="knockout")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_current_phase(self):
        phases = self.phases.order_by("order")
        for phase in phases:
            if not phase.is_complete():
                return phase
        return phases.last() if phases.exists() else None


class TournamentPhase(models.Model):
    PHASE_CHOICES = [
        ("groups", "Phase de poules"),
        ("round_of_16", "Huitième de finale"),
        ("quarter_final", "Quart de finale"),
        ("semi_final", "Demi-finale"),
        ("third_place", "Match pour la 3ème place"),
        ("final", "Finale"),
        ("custom", "Phase personnalisée"),
    ]
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="phases")
    name = models.CharField(max_length=100)
    phase_type = models.CharField(max_length=20, choices=PHASE_CHOICES, default="custom")
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.tournament.name} — {self.name}"

    def is_complete(self):
        matches = self.matches.all()
        if not matches.exists():
            return False
        return all(m.played for m in matches)

    def winners(self):
        winners = []
        for match in self.matches.filter(played=True):
            if match.score1 > match.score2:
                winners.append(match.player1)
            elif match.score2 > match.score1:
                winners.append(match.player2)
        return winners


class Match(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Planifié"),
        ("ongoing", "En cours"),
        ("finished", "Terminé"),
        ("cancelled", "Annulé"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches")
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name="matches", null=True, blank=True
    )
    phase = models.ForeignKey(
        TournamentPhase, on_delete=models.SET_NULL, related_name="matches", null=True, blank=True
    )
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="matches_as_p1")
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="matches_as_p2")
    referee = models.ForeignKey(
        Referee, on_delete=models.SET_NULL, related_name="matches", null=True, blank=True
    )
    scheduled_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    played = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["scheduled_at", "created_at"]

    def __str__(self):
        return f"{self.player1} vs {self.player2}"

    def save(self, *args, **kwargs):
        if self.played and self.pk:
            try:
                old = Match.objects.get(pk=self.pk)
                if not old.played:
                    if self.score1 > self.score2:
                        self.player1.points += 3
                        self.player1.save()
                    elif self.score2 > self.score1:
                        self.player2.points += 3
                        self.player2.save()
                    else:
                        self.player1.points += 1
                        self.player2.points += 1
                        self.player1.save()
                        self.player2.save()
                    self.status = "finished"
            except Match.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    @property
    def winner(self):
        if not self.played:
            return None
        if self.score1 > self.score2:
            return self.player1
        elif self.score2 > self.score1:
            return self.player2
        return None
