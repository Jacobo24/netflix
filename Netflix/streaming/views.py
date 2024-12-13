from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .utils import fetch_movies, fetch_tv_shows
import requests
from django.contrib.auth.decorators import login_required
from .models import PersonalList
import json

TMDB_API_KEY = '9980df73b55139ebcf9a053dbdaf4031'

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'streaming/movie_list.html', {'movies': movies})

def tvshow_list(request):
    tv_shows = TVShow.objects.all()
    return render(request, 'streaming/tvshow_list.html', {'tv_shows': tv_shows})

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class TVShowList(APIView):
    def get(self, request):
        tv_shows = TVShow.objects.all()
        serializer = TVShowSerializer(tv_shows, many=True)
        return Response(serializer.data)

# Vista basada a través de JSON.
def movie_list_json(request):
    try:
        data = fetch_movies()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def tv_show_list_json(request):
    try:
        data = fetch_tv_shows()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def movie_list(request):
    movies = fetch_movies()  # Usar los datos procesados desde utils.py
    return render(request, 'streaming/movie_list.html', {'movies': movies})

def tvshow_list(request):
    tv_shows = fetch_tv_shows()  # Obtener datos de series
    return render(request, 'streaming/tvshow_list.html', {'tv_shows': tv_shows})


def home(request):
    # Películas
    popular_movies = fetch_movies(endpoint='movie/popular')
    top_rated_movies = fetch_movies(endpoint='movie/top_rated')
    recent_movies = fetch_movies(endpoint='movie/now_playing')

    # Series
    popular_tv_shows = fetch_tv_shows(endpoint='tv/popular')
    top_rated_tv_shows = fetch_tv_shows(endpoint='tv/top_rated')
    airing_today_tv_shows = fetch_tv_shows(endpoint='tv/airing_today')

    return render(request, 'streaming/home.html', {
        'popular_movies': popular_movies,
        'top_rated_movies': top_rated_movies,
        'recent_movies': recent_movies,
        'popular_tv_shows': popular_tv_shows,
        'top_rated_tv_shows': top_rated_tv_shows,
        'airing_today_tv_shows': airing_today_tv_shows,
    })


def category_list(request):
    # Llamar a la API de TMDB para obtener géneros de películas y series
    movie_genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=es-ES'
    tv_genres_url = f'https://api.themoviedb.org/3/genre/tv/list?api_key={TMDB_API_KEY}&language=es-ES'

    movie_genres = requests.get(movie_genres_url).json().get('genres', [])
    tv_genres = requests.get(tv_genres_url).json().get('genres', [])

    # Combinar géneros de películas y series
    categories = [
        {"id": genre['id'], "name": genre['name'], "type": "movie"} for genre in movie_genres
    ] + [
        {"id": genre['id'], "name": genre['name'], "type": "tv"} for genre in tv_genres
    ]

    return render(request, 'streaming/category_list.html', {'categories': categories})

def category_detail(request, category_type, genre_id):
    # Tipo de contenido: "movie" o "tv"
    content_url = f'https://api.themoviedb.org/3/discover/{category_type}?api_key={TMDB_API_KEY}&language=es-ES&with_genres={genre_id}'

    # Llamar a la API para obtener contenido del género seleccionado
    content = requests.get(content_url).json().get('results', [])

    # Convertir los datos a un formato amigable
    formatted_content = [
        {
            "title": item.get("title") or item.get("name"),
            "poster": f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}" if item.get("poster_path") else None,
            "type": category_type
        }
        for item in content
    ]

    return render(request, 'streaming/category_detail.html', {
        'category_name': request.GET.get("name", "Categoría"),
        'content': formatted_content
    })

@login_required
def toggle_list_item(request):
    """
    Agregar o quitar una película o serie de la lista personal.
    """
    if request.method == "POST":
        try:
            import json
            data = json.loads(request.body)

            item_id = data.get("item_id")
            item_type = data.get("item_type")

            if not item_id or not item_type:
                return JsonResponse({"error": "Faltan datos: item_id o item_type"}, status=400)

            if item_type == "movie":
                item, created = PersonalList.objects.get_or_create(
                    user=request.user, movie_id=item_id
                )
            elif item_type == "tvshow":
                item, created = PersonalList.objects.get_or_create(
                    user=request.user, tvshow_id=item_id
                )
            else:
                return JsonResponse({"error": "Tipo inválido"}, status=400)

            if not created:
                item.delete()
                return JsonResponse({"status": "removed"})
            return JsonResponse({"status": "added"})

        except json.JSONDecodeError as e:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)


@login_required
def my_list(request):
    movies = PersonalList.objects.filter(user=request.user, movie_id__isnull=False)
    tvshows = PersonalList.objects.filter(user=request.user, tvshow_id__isnull=False)

    return render(request, 'streaming/my_list.html', {'movies': movies, 'tv_shows': tvshows})