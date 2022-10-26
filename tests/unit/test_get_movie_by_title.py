# TODO: Feature 3
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import *

movie_repository = get_movie_repository()

def test_get_movie_by_title():
    test_app = app.test_client()
    movie_repository.create_movie('Bad Movie', 'John Doe', 1)
    response = test_app.get('/movies/search')
    response_data = response.data
    assert b'<td>Bad Movie</td>' in response_data
    movie_repository.get_movie_by_title(title='Bad Movie')
    
    
    
