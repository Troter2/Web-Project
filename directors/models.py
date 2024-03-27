from django.db import models

# Create your models here.
class director(models.Model):
    director = models.CharField(max_length=200)