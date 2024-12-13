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
    """
    response = fetch_data_from_api(endpoint)
    results = response.get('results', [])
    
    # Formatear los resultados y asegurarse de incluir 'id'
    formatted_results = [
        {
            "id": movie.get("id"),  # Asegurarte de incluir 'id'
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
    """
    response = fetch_data_from_api(endpoint)
    results = response.get('results', [])
    
    # Formatear los resultados y asegurarse de incluir 'id'
    formatted_results = [
        {
            "id": tv_show.get("id"),  # Asegurarte de incluir 'id'
            "title": tv_show.get("name"),
            "poster_path": f"{IMAGE_BASE_URL}{tv_show['poster_path']}" if tv_show.get("poster_path") else None,
            "overview": tv_show.get("overview"),
            "release_date": tv_show.get("first_air_date"),
            "vote_average": tv_show.get("vote_average"),
        }
        for tv_show in results
    ]
    return formatted_results
