from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('api/movies', views.MovieList.as_view(), name='api_movie_list'),
    path('api/movies/json', views.MovieList.as_view(), name='api_movie_list_json'),
    path('tv-shows', views.tvshow_list, name='tvshow_list'),
    path('api/tv-shows', views.TVShowList.as_view(), name='api_tvshow_list'),
    path('api/tv-shows/json', views.TVShowList.as_view(), name='api_tvshow_list_json'),
]