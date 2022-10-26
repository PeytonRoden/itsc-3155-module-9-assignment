
from flask import Flask, redirect, render_template, request
from src.models.movie import Movie
from src.repositories import movie_repository
from src.repositories.movie_repository import *
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()
app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    list_movie = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=get_movie_repository, list_movie=list_movie)

@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    movie_name = request.form.get('movie_name')
    movie_director = request.form.get('movie_director')
    movie_rating = request.form.get('movie_rating')


    if(movie_name == None or movie_director == None):
        return render_template('please_fill_all_fields.html')

    movie_repository.create_movie(movie_name, movie_director, int(movie_rating))

    return redirect('/movies') 


@app.get('/movies/search')
def search_movies():
    all_movies = movie_repository.get_all_movies()
    ratings_list = []
    movietitle = request.args.get('movie-name')
    movie_repository.get_movie_by_title(movietitle)
    for movietitle in all_movies:
        if movietitle == movietitle:
            ratings_list.append


    return render_template('search_movies.html', search_active=True, movietitle=movietitle, all_movies=all_movies, ratings_list=ratings_list)
