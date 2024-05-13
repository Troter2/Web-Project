from django.shortcuts import render
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json
from reviews.utils import get_movie_data, create_review, create_movie


# Create your views here.
def list_movies(request):
    api_key = 'f4c3c931d2931acc4cade9ee84df005c'
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    LAST_MOVIES = response.json()
    movies = LAST_MOVIES['results']
    return render(request, 'movies/movie_1.html', {'data': movies})

def movie_details(request, movieId):
    movie = get_movie_data(movieId)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            create_review(request, movieId, review_form)
            return render(request, 'movies/movie_details_1.html', {'movie': movie, 'review_form': ReviewForm()})
        else:
            print("PRINNTTTTTT: ", review_form.errors)
            return review_form.add_error(None, "Error en el formulari")


    return render(request, 'movies/movie_details_1.html', {'movie': movie, 'review_form': ReviewForm()})

