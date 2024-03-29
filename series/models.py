from django.db import models

from productions.models import production


# Create your models here.
class serie(models.Model):
    idProduction = models.ForeignKey(production,on_delete=models.CASCADE)

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