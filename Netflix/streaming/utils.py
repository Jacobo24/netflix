import requests

API_KEY = '9980df73b55139ebcf9a053dbdaf4031'
BASE_URL = 'https://api.themoviedb.org/3/'

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

def fetch_movies():
    endpoint = 'movie/popular'
    response = fetch_data_from_api(endpoint)
    return response.get('results', [])

def fetch_tv_shows():
    endpoint = 'tv/popular'
    response = fetch_data_from_api(endpoint)
    return response.get('results', [])