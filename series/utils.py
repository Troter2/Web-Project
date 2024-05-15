import requests
from .models import serie


from reviews.utils import get_review
def get_serie_data(serie_id):
    api_key = '3462f0a957fcd5649fa50d0ffd4ba663'
    url = f'https://api.themoviedb.org/3/tv/{serie_id}?api_key={api_key}&language=es-ES'
    response = requests.get(url)
    serie_data = response.json()
    return serie_data


def create_serie(serie_id):
    serie1 = get_serie_data(serie_id)
    serie.objects.get_or_create(
        serieName=serie1['name'],
        overview=serie1['overview'],
        number_of_episodes=serie1['number_of_episodes'],
        number_of_seasons=serie1['number_of_seasons'],
        in_production=serie1['in_production'],
        original_language=serie1['spoken_languages'][0]['name'],
        poster_path=serie1['poster_path'],
        vote_average=serie1.get('vote_average'),
        original_title=serie1['original_name'],
        backdrop_path=serie1['backdrop_path'],
        id=serie_id
    )


def create_review(request, serie_id, review_form):
    review = review_form.save(commit=False)
    serie = get_serie_data(serie_id)
    review_exists = get_review(request.user.id, serie_id)
    if review_exists is None:
        review.user_id_id = request.user.id
        review.title = serie['name']
        review.content = review_form.cleaned_data['content']
        if not review_form.cleaned_data['rating'] or review_form.cleaned_data['rating'] == '':
            review.rating = str(0)
        else:
            review.rating = review_form.cleaned_data['rating']
        create_serie(serie_id)
        review.review_serie_id = serie_id
        review.save()
    else:
        review_exists.content = review_form.cleaned_data['content']
        review_exists.rating = review_form.cleaned_data['rating']
        review_exists.save()



