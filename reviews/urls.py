from django.urls import path
from django.views.generic import TemplateView
from reviews.views import new_review, list_movies


urlpatterns = [

    path('new-review/', new_review, name='new_review'),
    path('list-movies/', list_movies, name='list_movies'),

    ]