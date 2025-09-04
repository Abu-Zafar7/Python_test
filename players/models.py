from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Player(models.Model):

    CHOICES = [
        ("Goalkeeper", "Goalkeeper"),
        ("Defender", "Defender"),
        ("Midfielder", "Midfielder"),
        ("Forward", "Forward"),
    ]
    name = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=CHOICES)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.club}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'player')

        