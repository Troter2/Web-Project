from django.shortcuts import render
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json
from reviews.utils import get_movie_data


# Create your views here.


@login_required
def new_review(request, movieId):

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review.user_id_id = request.user.id
            """title = review_form.cleaned_data['title']
            rating = review_form.cleaned_data['rating']
            content = review_form.cleaned_data['content']
            product_type = review_form.cleaned_data['product_id']
            review = review_form.save(commit=False)
            review.user_id_id = request.user.id
            review.title = review_form.cleaned_data['title']
            review.save()"""
            return render(request, 'review/review_2.html')
        else:
            return form.add_error(None, "Error en el formulari")
    else:

        review_form = ReviewForm()

    return render(request, 'review/review_1.html', {'review_form': review_form, 'movie_title': request.session['movie_title']})


def list_movies(request):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    LAST_MOVIES = response.json()
    movies = LAST_MOVIES['results']
    return render(request, 'movies/movie_1.html', {'data': movies})

def movie_details(request, movieId):
    movie = get_movie_data(movieId)
    request.session['movie_title'] = movie['title']
    return render(request, 'movies/movie_details_1.html', {'movie': movie})

