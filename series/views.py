from django.shortcuts import render

import requests

from reviews.forms import ReviewForm
from reviews.models import Review
from series.models import serie
from series.utils import create_review


def get_popular_series(request):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = f'https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=es-ES'
    response = requests.get(url)
    data = response.json()

    series_list = []

    if data:
        for serie_data in data['results']:
            serie = {
                'id': serie_data['id'],
                'poster_path': serie_data['poster_path'],
                'title': serie_data['name'],
                'description': serie_data['overview'],
                'release_date': serie_data.get('first_air_date'),
                'rating': serie_data.get('vote_average'),
            }
            series_list.append(serie)

    return render(request, 'series/serie_list.html', {'data': series_list})


def serie_details(request, serie_id):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = f'https://api.themoviedb.org/3/tv/{serie_id}?api_key={api_key}&language=es-ES'
    response = requests.get(url)
    serie_data = response.json()

    if serie_data:
        cur_serie = {
            'poster_path': serie_data['poster_path'],
            'title': serie_data['name'],
            'description': serie_data['overview'],
            'release_date': serie_data.get('first_air_date'),
            'rating': serie_data.get('vote_average'),
            'original_language': serie_data.get('original_language'),
            'homepage': serie_data.get('homepage'),
            'number_of_episodes': serie_data.get('number_of_episodes'),
            'number_of_seasons': serie_data.get('number_of_seasons'),
            'popularity': serie_data.get('popularity'),
        }

    try:
        serie_object = serie.objects.get(id=serie_id)
        reviews = Review.objects.filter(review_serie=serie_object)[:6]
    except:
        reviews = None

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():

            create_review(request, serie_id, review_form)
            return render(request, 'series/serie_detail.html',
                          {'series': cur_serie, 'review_form': review_form, 'reviews': reviews})
        else:
            print(review_form.errors)
            return review_form.add_error(None, "Error en el formulario")
    return render(request, 'series/serie_detail.html',
                  {'series': cur_serie, 'review_form': ReviewForm(), 'reviews': reviews})
