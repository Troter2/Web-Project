from django.urls import path
from django.views.generic import TemplateView
from reviews.views import new_review


urlpatterns = [

    path('new-review/', new_review, name='new_review'),

    ]