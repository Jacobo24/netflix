from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    genre = models.TextField(max_length=100, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    poster_path = models.URLField(blank=True, null=True)
    backdrop_path = models.URLField(blank=True, null=True)
    tmdb_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title