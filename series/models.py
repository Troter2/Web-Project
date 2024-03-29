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


class seasonDetail(models.Model):
    _id = models.CharField(max_length=30,unique=True)
    air_date = models.DateField()
    # episodes = models.IntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField(blank= True, null=True)
    id = models.IntegerField(primary_key=True)
    poster_path = models.CharField(max_length=255, default="")
    season_number = models.IntegerField()
    vote_average = models.FloatField(blank=True, null=True)

class episodeDetail(models.Model):
    air_date = models.DateField()
    crew = models.CharField(max_length=255)
    episode_number = models.IntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField(blank= True, null=True)
    id = models.IntegerField(primary_key=True)
    runtime = models.IntegerField()
    still_path = models.CharField(max_length=255, default="")
    vote_average = models.FloatField(blank=True, null=True)

