from django.urls import path
from django.views.generic import TemplateView

from movies.views import list_movies
from reviews.views import movie_details


urlpatterns = [
    path('list-movies/', list_movies, name='list_movies'),
    path('movie-detail/<int:movieId>/', movie_details, name='movie_details'),
    ]