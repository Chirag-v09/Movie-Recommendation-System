from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import movie_rec
import random
from .models import Latest

# Create your views here.


def index(request):
    movies = []
    movies_obj = Latest.objects.all()
    for movie in movies_obj:
        movies.append(movie.latest)
    movies = movies[::-1]
    context = {"movies": movies}
    return render(request, 'movie/index.html', context)


def index1(request):
    movies = []
    movies_obj = Latest.objects.all()
    for movie in movies_obj:
        df_movie = movie_rec.movies(movie.latest)
        for i in range(3):
            movies.append(df_movie.index[i])

    movies_s = random.sample(movies, 6)
    context = {"movies": movies_s}
    return render(request, 'movie/index.html', context)


def details(request, movie_name):

    if Latest.objects.filter(latest=movie_name):
        l_m_d = Latest.objects.filter(latest=movie_name)
        l_m_d.delete()
    l_m = Latest()
    l_m.latest = movie_name
    l_m.save()
    # Latest.save()

    movies = Latest.objects.all()
    while len(movies) > 6:
        l_m_d = Latest.objects.filter(latest=movies[0].latest)
        l_m_d.delete()
        movies = Latest.objects.all()

    df_movie = movie_rec.movies(movie_name)
    movies = []
    for i in range(1, len(df_movie)):
        movies.append(df_movie.index[i])
    context = {"main_movie": movie_name, "movies": movies}

    return render(request, 'movie/details.html', context)
