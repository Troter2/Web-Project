from django.db import models
from actors.models import actor
from productions.models import production


# Create your models here.
class credit(models.Model):
    idActor = models.ForeignKey(actor, on_delete=models.CASCADE)
    idProduction = models.ForeignKey(production, on_delete=models.CASCADE)