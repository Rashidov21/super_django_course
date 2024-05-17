import datetime
from django.db import models



from django_countries.fields import CountryField
# Create your models here.

class Tournament(models.Model):
    name = models.CharField(verbose_name="Tur nomini kirit",max_length=250)
    logo = models.ImageField(upload_to="logos/tournament/", blank=True)
    country = CountryField()
    last_winner = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=350)
    
    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(verbose_name="Klub nomini kirit",max_length=250)
    logo = models.ImageField(upload_to="logos/tournament/", blank=True)
    country = CountryField()
    coach = models.CharField(max_length=250, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

POS = (
    ("gk","GoalKeeper"),
    ("df","Deffender"),
    ("mdf","Middle deffender"),
    ("fw","Forward"),
    ("st","Striker")
)

class Player(models.Model):
    name = models.CharField(verbose_name="Player name",max_length=250)
    image = models.ImageField(upload_to="player/images/", blank=True)
    origin_name = models.CharField(verbose_name="Origin name",max_length=250)
    club = models.ForeignKey(Club,on_delete=models.PROTECT)
    position = models.CharField(max_length=250, choices=POS)
    country = CountryField()
    date_of_birth = models.DateField(blank=True)
    age = models.PositiveSmallIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    weight = models.PositiveSmallIntegerField(default=0)
    transfer_summa = models.FloatField(blank=True)
    
    def get_player_age(self):
        current_year = datetime.datetime.now().year # int 2024
        age = current_year - self.date_of_birth.year
        return age
    
    def __str__(self):
        return self.name
    

class Career(models.Model):
    player = models.OneToOneField(Player,on_delete=models.CASCADE)
    tournaments = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    clubs = models.ForeignKey(Club, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.player.name