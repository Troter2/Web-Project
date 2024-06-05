
from django.shortcuts import render, redirect
from movies.models import movie
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json
from reviews.utils import get_movie_data, create_review, create_movie, get_my_reviews, get_rating
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
            try:
                reviews = Review.objects.filter(review_movie=movie_object)[:6]
            except :
                reviews = None
            return render(request, 'movies/movie_details_1.html', {'movie': movie_data, 'review_form': ReviewForm(), 'reviews': reviews})
        else:
            print(review_form.errors)
            return review_form.add_error(None, "Error en el formulari")

    try:
        reviews = Review.objects.filter(review_movie=movie_object)[:6]
        rating = get_rating(reviews)
    except :
        rating = None
        reviews = None
    return render(request, 'movies/movie_details_1.html', {'movie': movie_data, 'review_form': ReviewForm(), 'reviews': reviews, 'rating': rating, 'numReviews': len(reviews)})

@login_required
def list_my_reviews(request):
    reviews = get_my_reviews(request)
    return render(request, 'review/list_my_reviews.html', {'reviews': reviews, 'form': ReviewForm()})

@login_required
def delete_review(request, reviewId):
    review = Review.objects.get(id=reviewId)
    review.delete()
    return redirect('my_reviews')

def edit_review(request, reviewId):
    review = Review.objects.get(id=reviewId)
    review_form = ReviewForm(request.POST)
    review.content = review_form.data['content']
    review.rating = review_form.data['rating']
    review.save()
    return  redirect('my_reviews')
