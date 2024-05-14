from django.db import models


from credits.models import productor
from genders.models import gender
from actors.models import actor


# Create your models here.
class movie(models.Model):
    
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)
    belongs_to_collection = models.CharField(max_length=255, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    genres = models.ManyToManyField(gender, blank=True)
    producer = models.ManyToManyField(productor, blank=True)
    actor = models.ManyToManyField(actor, blank=True)
    homepage = models.URLField(blank=True, null=True)
    original_language = models.CharField(max_length=20, null=True, unique=False)
    original_title = models.CharField(max_length=255, default="")
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, default="")
    release_date = models.DateField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, default="")
    video = models.BooleanField(default=False)
    vote_average = models.FloatField(blank=True, null=True)
