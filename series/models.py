from django.db import models
from django.core.exceptions import ValidationError

from credits.models import productor
from actors.models import actor


# Create your models here.
class serie(models.Model):
    serieName = models.CharField(max_length=100, default="noSerie")
    overview = models.TextField(default="No overview")
    number_of_episodes = models.IntegerField(default=0)
    number_of_seasons = models.IntegerField(default=0)
    in_production = models.BooleanField(default=False)
    original_language = models.CharField(max_length=100, default="")
    producer = models.ManyToManyField(productor, blank=True)

    original_title = models.CharField(max_length=255, default="")
    vote_average = models.FloatField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, default="")
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)


class seasonDetail(models.Model):
    air_date = models.DateField()
    episodes = models.IntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)
    poster_path = models.CharField(max_length=255, default="")
    season_number = models.IntegerField()
    vote_average = models.DecimalField(max_digits=4, decimal_places=2)

    def clean(self):
        if self.season_number >= self.serie.number_of_seasons:
            raise ValidationError(
                "El número de temporada debe ser menor que el número total de temporadas de la serie.")


class episodeDetail(models.Model):
    air_date = models.DateField()
    crew = models.CharField(max_length=255)
    episode_number = models.IntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    runtime = models.IntegerField()
    season = models.ForeignKey(seasonDetail, on_delete=models.CASCADE)
    still_path = models.CharField(max_length=255, default="")
    vote_average = models.FloatField(blank=True, null=True)

    def clean(self):
        if self.episode_number >= self.season.episodes:
            raise ValidationError(
                "El número de espisodio debe ser menor que el número total de espisodios de la temporada.")

    def clean(self):
        if self.air_date <= self.season.air_date:
            raise ValidationError(
                "Un espodi tiene que estar creado antes o igual que su temporada correspondiente.")
