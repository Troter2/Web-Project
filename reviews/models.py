from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from series.models import Serie




# Create your models here.
class review(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, default="")
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
