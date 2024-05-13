from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from movies.models import movie
from series.models import serie

# Create your models here.
class Review(models.Model):

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_movie = models.ForeignKey(movie, on_delete=models.CASCADE, blank=True, null=True)
    review_serie = models.ForeignKey(serie, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, default="")
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
