from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [

    path('new-review/', TemplateView.as_view(template_name='review/review_1.html'), name='new_review'),

    ]