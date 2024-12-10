from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('tv-shows', views.tvshow_list, name='tvshow_list'),
]