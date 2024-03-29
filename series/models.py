from django.db import models

from productions.models import production


# Create your models here.
class serie(models.Model):
    idProduction = models.ForeignKey(production,on_delete=models.CASCADE)
    serieName = models.CharField(max_length=100,default="noSerie")
    overview = models.TextField(default="No overview")
    number_of_episodes = models.IntegerField(default=0)
    number_of_seasons = models.IntegerField(default=0)
    season_number = models.IntegerField(default=0)
    in_production = models.BooleanField(default=False)
    original_language = models.CharField(max_length=100,default="")