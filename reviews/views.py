from django.shortcuts import render

from movies.models import movie
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json
from reviews.utils import get_movie_data, create_review, create_movie
from .models import Review


# Create your views here.
def list_movies(request):
    api_key = 'f4c3c931d2931acc4cade9ee84df005c'
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    LAST_MOVIES = response.json()
    movies = LAST_MOVIES['results']
    return render(request, 'movies/movie_list.html', {'data': movies})


def movie_details(request, movieId):
    try:
        movie_data = get_movie_data(movieId)
        movie_object = movie.objects.get(id=movieId)
    except :
        reviews = None


    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            create_review(request, movieId, review_form)
            reviews = Review.objects.filter(review_movie=movie_object)[:6]
            return render(request, 'movies/movie_details_1.html', {'movie': movie_data, 'review_form': ReviewForm(), 'reviews': reviews})
        else:
            return review_form.add_error(None, "Error en el formulari")

    reviews = Review.objects.filter(review_movie=movie_object)[:6]
    return render(request, 'movies/movie_details_1.html', {'movie': movie_data, 'review_form': ReviewForm(), 'reviews': reviews})
