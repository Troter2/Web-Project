from django.urls import path
from django.views.generic import TemplateView

from movies.views import list_movies
from reviews.views import movie_details


urlpatterns = [
    path('new-review/<int:movieId>/', movie_details, name='new_review'),
    path('list-movies/', list_movies, name='list_movies'),
    path('movie-detail/<int:movieId>/', movie_details, name='movie_details'),
    ]