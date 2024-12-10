from django.core.management.base import BaseCommand
from streaming.models import Movie
from streaming.utils import fetch_movies

class Command(BaseCommand):
    help = 'Import movies from The Movie Database'

    def handle(self, *args, **options):
        try:
            movies = fetch_movies()
            for movie in movies:
                Movie.objects.create(
                    title=movie.get('title'),
                    description=movie.get('overview'),
                    release_date=movie.get('release_date'),
                    genre=','.join([genre.get('name') for genre in movie.get('genres', [])]),
                    vote_average=movie.get('vote_average'),
                    poster_path=movie.get('poster_path'),
                    backdrop_path=movie.get('backdrop_path'),
                    tmdb_id=movie.get('id')
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported movies'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to import movies: {e}'))