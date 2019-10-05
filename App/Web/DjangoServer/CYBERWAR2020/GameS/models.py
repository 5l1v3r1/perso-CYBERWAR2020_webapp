from django.db import models
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    iDGame = models.IntegerField(None)
    vRègles = models.IntegerField(default = 0)

    def __str__(self):
        return self.partie_text

class Turn(models.Model):
    idGame = models.ForeignKey(Game, on_delete=models.CASCADE)
    tour = models.IntegerField(default = 0)

    def __str__(self):
        return self.tour_text

class Player(models.Model):
    idPlayer = models.IntegerField(None)
    name = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
