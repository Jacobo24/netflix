import requests

API_KEY = '9980df73b55139ebcf9a053dbdaf4031'
BASE_URL = 'https://api.themoviedb.org/3'
IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'


def fetch_data_from_api(endpoint):
    base_url = "https://api.themoviedb.org/3/"
    api_key = "9980df73b55139ebcf9a053dbdaf4031"  # Asegúrate de reemplazarlo con tu API Key válida
    url = f"{base_url}{endpoint}?api_key={api_key}&language=es-ES"
    
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos: {response.status_code}, {response.text}")
        return {}

IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'

def fetch_movies(endpoint='movie/popular'):
    """
    Obtiene películas desde la API de TMDB.
    Parámetro endpoint permite elegir el tipo de películas a obtener.
    """
    response = fetch_data_from_api(endpoint)
    results = response.get('results', [])
    # Formatear los resultados para garantizar que las claves existan
    formatted_results = [
        {
            "title": movie.get("title"),
            "poster_path": f"{IMAGE_BASE_URL}{movie['poster_path']}" if movie.get("poster_path") else None,
            "overview": movie.get("overview"),
            "release_date": movie.get("release_date"),
            "vote_average": movie.get("vote_average"),
        }
        for movie in results
    ]
    return formatted_results


def fetch_tv_shows(endpoint='tv/popular'):
    """
    Obtiene series desde la API de TMDB.
    Parámetro endpoint permite elegir el tipo de series a obtener.
    """
    response = fetch_data_from_api(endpoint)
    results = response.get('results', [])
    for show in results:
        if show.get('poster_path'):
            show['poster_path'] = f"{IMAGE_BASE_URL}{show['poster_path']}"
    return results
