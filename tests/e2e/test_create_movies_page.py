# TODO: Feature 2


from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import app

movie_repository = get_movie_repository()


def test_get_all_movies():
    test_app = app.test_client()

    response = test_app.get('/movies/new')

    assert b'<input type="text" class="form-control" id="movie_name" name  = "movie_name" required autocomplete = "off">' in response.data
    assert b'<input type="text" class="form-control" id="movie_director" name = "movie_director" required autocomplete = "off">' in response.data
    assert b'<input type="range" class="form-range" min="1" max="5" step="1" id="customRange3" name = "movie_rating">' in response.data