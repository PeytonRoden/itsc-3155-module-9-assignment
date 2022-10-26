from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()


def test_all_movies_page(test_app: FlaskClient):
    movie_repository.create_movie('Black Panther', 'Ryan Coogler', 4)
    response = test_app.get('/movies/search', query_string = {"movie-name": "Black Panther"})
    response_data = response.data

    assert b'<td>Black Panther</td>' in response_data
    assert b'<td>Ryan Coogler</td>' in response_data
    assert b'<td>4</td>' in response_data