from django.core.management.base import BaseCommand
from streaming.models import TVShow
from streaming.utils import fetch_tv_shows

class Command(BaseCommand):
    help = 'Import TV shows from The Movie Database'

    def handle(self, *args, **options):
        try:
            tv_shows = fetch_tv_shows()
            for tv_show in tv_shows:
                TVShow.objects.create(
                    title=tv_show.get('name'),
                    description=tv_show.get('overview'),
                    release_date=tv_show.get('first_air_date'),
                    genre=','.join([genre.get('name') for genre in tv_show.get('genres', [])]),
                    vote_average=tv_show.get('vote_average'),
                    poster_path=tv_show.get('poster_path'),
                    backdrop_path=tv_show.get('backdrop_path'),
                    tmdb_id=tv_show.get('id')
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported TV shows'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to import TV shows: {e}'))