from django.db import models

from productions.models import production


# Create your models here.
class movie(models.Model):
    idProduction = models.ForeignKey(production, on_delete=models.CASCADE)
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)
    belongs_to_collection = models.CharField(max_length=255, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    # genres = models.ManyToManyField(Genres, blank=True)
    homepage = models.URLField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=20, default="")
    original_language = models.CharField(max_length=20,unique=True,null=True)
    original_title = models.CharField(max_length=255, default="")
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, default="")
    # production_companies = models.OneToManyField(CompaniesProduction)
    # production_countries = models.CharField(max_length=)
    release_date = models.DateField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    # spoken_languages = models.ManyToManyField(Language)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, default="")
    video = models.BooleanField(default=False)
    vote_average = models.FloatField(blank=True, null=True)
