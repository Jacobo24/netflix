import requests

API_KEY = '9980df73b55139ebcf9a053dbdaf4031'
BASE_URL = 'https://api.themoviedb.org/3/'

def fetch_movies():
    url = f'{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []