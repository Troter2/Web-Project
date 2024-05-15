from django.shortcuts import render
import requests

from .models import movie
from series.models import serie



# Create your views here.
def homepage(request):
    movies = movie.objects.all()[:5]
    series = serie.objects.all()[:5]

    context = {
        'movies': movies,
        'series': series,
    }

    return render(request, 'home.html', context)



def list_movies(request):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    data = response.json()
    movie = data['results']

    return render(request, 'movies/movies_list.html', {'data': movie})

