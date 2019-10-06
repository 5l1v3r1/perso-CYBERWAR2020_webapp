from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    idPlayer = models.IntegerField(None)
    name = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
