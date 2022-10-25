# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()


def test_all_movies_page(test_app: FlaskClient):
    movie_repository.create_movie('Black Panter', 'Ryan Coogler', 4)
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<td>Black Panter</td>' in response_data
    assert b'<td>Ryan Coogler</td>' in response_data
    assert b'<td>4</td>' in response_data


def test_all_movies_page_unorder(test_app: FlaskClient):
    movie_repository.create_movie(4, 'Ryan Coogler', 'Black Panter')
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<td>Black Panter</td>' in response_data
    assert b'<td>Ryan Coogler</td>' in response_data
    assert b'<td>4</td>' in response_data
