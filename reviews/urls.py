from django.urls import path
from django.views.generic import TemplateView

from movies.views import list_movies
from reviews.views import movie_details, list_my_reviews, delete_review, edit_review


urlpatterns = [
    path('edit-review/<int:reviewId>/', edit_review, name='edit_review'),
    path('my-reviews/', list_my_reviews, name='my_reviews'),
    path('new-review/<int:movieId>/', movie_details, name='new_review'),
    path('list-movies/', list_movies, name='list_movies'),
    path('movie-detail/<int:movieId>/', movie_details, name='movie_details'),
    path('delete_review/<int:reviewId>/', delete_review, name='delete_review'),

    ]