from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies', views.movie_list, name='movie_list'),
    path('api/movies', views.MovieList.as_view(), name='api_movie_list'),
    path('api/movies/json', views.MovieList.as_view(), name='api_movie_list_json'),
    path('api/tvshows', views.TVShowList.as_view(), name='api_tvshow_list'),
    path('api/tvshows/json', views.tv_show_list_json, name='api_tvshow_list_json'),
    path('tvshows', views.tvshow_list, name='tvshow_list'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<str:category_type>/<int:genre_id>/', views.category_detail, name='category_detail'),
]