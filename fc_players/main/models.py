from django.db import models
from django_countries.fields import CountryField
# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

POSITIONS = [
    ("striker", "Striker"),
    ("defender", "Defender"),
    ("midfielder", "Midfielder"),
    ("goalkeeper", "Goalkeeper")
]

class Player(models.Model):
    name = models.CharField(max_length=100)
    date_of_bith = models.DateField()
    country = CountryField()
    club = models.ForeignKey(Club, on_delete=models.PROTECT, related_name="players")
    position = models.CharField(max_length=100, choices=POSITIONS)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    
    def __str__(self):
        return self.name