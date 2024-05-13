from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    country = models.CharField(max_length=9)
    phone = models.CharField(max_length=11)
