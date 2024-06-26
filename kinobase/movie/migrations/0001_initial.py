# Generated by Django 4.2.2 on 2024-06-09 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('slug', models.SlugField(max_length=150, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('slug', models.SlugField(max_length=150, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('slug', models.SlugField(max_length=150, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, upload_to='movie_posters/')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=250, verbose_name='*')),
                ('origin_title', models.CharField(blank=True, max_length=250, verbose_name='Origin title')),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True)),
                ('year', models.PositiveSmallIntegerField(default=0)),
                ('kp_rating', models.FloatField(blank=True)),
                ('imdb_rating', models.FloatField(blank=True)),
                ('quality', models.CharField(choices=[('bdrip', 'BDRip'), ('hdrip', 'HDRip'), ('ts', 'TS')], max_length=150)),
                ('drafts', models.BooleanField(default=False)),
                ('duration', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True)),
                ('sd_file_url', models.URLField(blank=True)),
                ('hd_file_url', models.URLField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movie.category')),
                ('genres', models.ManyToManyField(to='movie.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.BooleanField(default=False)),
                ('director', models.BooleanField(default=False)),
                ('producer', models.BooleanField(default=False)),
                ('author', models.ManyToManyField(to='movie.author')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Гость', max_length=150)),
                ('comment', models.TextField()),
                ('commented_time', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]
