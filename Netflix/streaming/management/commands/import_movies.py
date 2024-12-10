from django.core.management.base import BaseCommand
from streaming.models import Movie
from streaming.utils import fetch_movies

class Command(BaseCommand):
    help = 'Import movies from The Movie Database'

    def handle(self, *args, **options):
        movies = fetch_movies()
        for movie in movies:
            Movie.objects.update_or_create(
                tmdb_id=movie['id'],
                defaults={
                    'title': movie['title'],
                    'description': movie['overview'],
                    'release_date': movie['release_date'],
                    'genre': ', '.join([genre['name'] for genre in movie['genres']]),
                    'vote_average': movie['vote_average'],
                    'poster_path': f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}',
                    'backdrop_path': f'https://image.tmdb.org/t/p/w1280{movie["backdrop_path"]}',
                }
            )
        self.stdout.write(self.style.SUCCESS('Movies imported successfully!'))