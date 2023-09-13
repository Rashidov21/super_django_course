from django.db import models

# Create your models here.


class Players(models.Model):
    number = models.IntegerField(default=0, blank=True)
    player = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    dr = models.DateField(blank=True)
    height = models.PositiveIntegerField(default=0, blank=True)
    weight = models.PositiveIntegerField(default=0, blank=True)
    price = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.player)
