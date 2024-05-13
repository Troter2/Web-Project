import requests
import json


def get_movie_data(movieId):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = f'https://api.themoviedb.org/3/movie/{movieId}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    movie = response.json()
    return movie
