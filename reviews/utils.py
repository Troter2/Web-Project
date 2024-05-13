import requests
import json


def get_movie_data(movieId):
    api_key = 'f4c3c931d2931acc4cade9ee84df005c'
    url = f'https://api.themoviedb.org/3/movie/{movieId}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    movie = response.json()
    return movie

def create_movie(movieId):
    movie = get_movie_data(movieId)
    Movie.objects.create(
        movie_id=movie['id'],
        title=movie['title'],
        overview=movie['overview'],
        release_date=movie['release_date'],
        poster_path=movie['poster_path']
    )
    return

def create_review(request, movieId, review_form):
    review = review_form.save(commit=False)
    movie = get_movie_data(movieId)
    review.user_id_id = request.user.id
    review.title = movie['title']
    review.content = review_form.cleaned_data['content']
    review.rating = review_form.cleaned_data['rating']
    review.review_movie_id = movieId
    review.save()
    return