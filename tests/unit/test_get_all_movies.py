# TODO: Feature 1
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import app

movie_repository = get_movie_repository()


def test_get_all_movies():
    test_app = app.test_client()

    movie_repository.create_movie('Black Panter', 'Ryan Coogler', 4)
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<td>Black Panter</td>' in response_data
    assert b'<td>Ryan Coogler</td>' in response_data
    assert b'<td>4</td>' in response_data


def test_get_all_movies_unordered():
    test_app = app.test_client()

    movie_repository.create_movie(3, 'Spider Man', 'Jon Watts')
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<td>Spider Man</td>' in response_data
    assert b'<td>Jon Watts</td>' in response_data
    assert b'<td>3</td>' in response_data
