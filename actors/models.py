from django.db import models

# Create your models here.
class actor(models.Model):
    idActor = models.CharField(max_length=200)