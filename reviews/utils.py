import requests
import json
from movies.models import movie


def get_movie_data(movieId):
    api_key = 'f4c3c931d2931acc4cade9ee84df005c'
    url = f'https://api.themoviedb.org/3/movie/{movieId}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    movie_1 = response.json()
    return movie_1


def create_movie(movieId):
    movie1 = get_movie_data(movieId)
    movie.objects.get_or_create(
        title=movie1['title'],
        overview=movie1['overview'],
        release_date=movie1['release_date'],
        poster_path=movie1['poster_path'],
        original_language=movie1['original_language'],
        vote_average=movie1['vote_average'],
        original_title=movie1['original_title'],
        backdrop_path=movie1['backdrop_path'],
        video=movie1['video'],
        adult=movie1['adult'],
        id=movieId
    )


def create_review(request, movieId, review_form):
    review = review_form.save(commit=False)
    movie1 = get_movie_data(movieId)
    review.user_id_id = request.user.id
    review.title = movie1['title']
    review.content = review_form.cleaned_data['content']
    review.rating = review_form.cleaned_data['rating']
    create_movie(movieId)
    review.review_movie_id = movieId
    review.save()
