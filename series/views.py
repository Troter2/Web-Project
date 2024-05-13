from django.shortcuts import render

import requests

def get_popular_series():
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = f'https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=es-ES'
    response = requests.get(url)
    data = response.json()

    series_list = []

    if data:
        for serie_data in data['results']:
            serie = {
                'title': serie_data['name'],
                'description': serie_data['overview'],
                'release_date': serie_data.get('first_air_date'),
                'rating': serie_data.get('vote_average'),
            }
            series_list.append(serie)


    return render(request, 'series/serie_1.html', {'data': movie})