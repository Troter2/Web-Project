from django.db import models

from productions.models import production


# Create your models here.
class movie(models.Model):
    idProduction = models.ForeignKey(production, on_delete=models.CASCADE)
    nom = models."tipo de camp"