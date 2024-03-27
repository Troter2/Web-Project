from django.db import models

from productions.models import production


# Create your models here.
class serie(models.Model):
    idProduction = models.ForeignKey(production,on_delete=models.CASCADE)