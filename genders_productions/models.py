from django.db import models
from productions.models import production
from genders.models import gender
# Create your models here.
class gender_production(models.Model):
    idGender = models.ForeignKey(gender, on_delete=models.CASCADE)
    idProduction = models.ForeignKey(production, on_delete=models.CASCADE)