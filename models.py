from django.db import models

# Create your models here.
class cars(models.Model):
    name = models.CharField(max_length=64)
    founded_year = models.IntegerField()
    champ_wins = models.IntegerField()
    budget = models.IntegerField()
    race_wins = models.IntegerField()
    