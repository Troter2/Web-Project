from django.db import models

# Create your models here.
class actor(models.Model):
    name = models.CharField(max_length=100,default="")
    biography = models.TextField(max_length=5000,default="")
    also_known_as = models.TextField(max_length=5000, default="")
    gender = models.CharField(max_length=100,default="")
