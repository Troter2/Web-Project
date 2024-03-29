from django.db import models
from actors.models import actor
from productions.models import production


# Create your models here.
class credit(models.Model):
    idActor = models.ForeignKey(actor, on_delete=models.CASCADE)
    idProduction = models.ForeignKey(production, on_delete=models.CASCADE)

class productor(models.Model):
    description = models.TextField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    logo_path = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    original_country = models.CharField(max_length=20,unique=True,null=True)