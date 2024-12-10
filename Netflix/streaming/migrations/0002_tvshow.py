# Generated by Django 4.2.17 on 2024-12-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("streaming", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TVShow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("release_date", models.DateField(blank=True, null=True)),
                ("genre", models.TextField(blank=True, max_length=100, null=True)),
                ("vote_average", models.FloatField(blank=True, null=True)),
                ("poster_path", models.URLField(blank=True, null=True)),
                ("backdrop_path", models.URLField(blank=True, null=True)),
                ("tmdb_id", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
