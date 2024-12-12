import requests

API_KEY = '9980df73b55139ebcf9a053dbdaf4031'
BASE_URL = 'https://api.themoviedb.org/3'
IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'


def fetch_data_from_api(endpoint, params=None, langauge='es-ES'):
    if params is None:
        params = {}

    url = f'{BASE_URL}/{endpoint}'
    params['api_key'] = API_KEY
    params['language'] = langauge
    response = requests.get(url, params=params)


    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch data from {url}: {response.text}')

IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'

def fetch_movies():
    endpoint = 'movie/popular'
    response = fetch_data_from_api(endpoint)
    results = response.get('results', [])
    for movie in results:
        if movie.get('poster_path'):
            movie['poster_path'] = f"{IMAGE_BASE_URL}{movie['poster_path']}"
    return results

def fetch_tv_shows():
    endpoint = 'tv/popular'
    response = fetch_data_from_api(endpoint)
    results = response.get('results', [])
    for show in results:
        if show.get('poster_path'):
            show['poster_path'] = f"{IMAGE_BASE_URL}{show['poster_path']}"
    return results
