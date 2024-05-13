from django.shortcuts import render
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json


# Create your views here.


@login_required
def new_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            """title = review_form.cleaned_data['title']
            rating = review_form.cleaned_data['rating']
            content = review_form.cleaned_data['content']
            product_type = review_form.cleaned_data['product_id']"""
            review = review_form.save(commit=False)
            review.user_id_id = request.user.id
            review.title = review_form.cleaned_data['title']
            review.save()
            return render(request, 'review/review_2.html')
        else:
            return form.add_error(None, "Error en el formulari")
    else:
        review_form = ReviewForm()
    return render(request, 'review/review_1.html', {'review_form': review_form})

def list_movies(request):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    data = response.json()
    movie = data['results']
    return render(request, 'movies/movie_1.html', {'data': movie})

def movie_details(request, movieId):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = f'https://api.themoviedb.org/3/movie/{movieId}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    movie = response.json()
    return render(request, 'movies/movie_details_1.html', {'movie': movie})