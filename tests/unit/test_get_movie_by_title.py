# TODO: Feature 3
from turtle import onclick
from src.models.movie import *
from src.repositories.movie_repository import *
from app import *

movie_repository = get_movie_repository()

def test_get_movie_by_title():
    test_app = app.test_client()
    movie_repository.create_movie('Bad Movie', 'John Doe', 1)
    response = test_app.get('/movies/search')

    assert movie_repository.get_movie_by_title("Bad Movie")
    
    
    
    
