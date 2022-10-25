# TODO: Feature 2
from pathlib import Path
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app

#get movie repository
movie_repository = get_movie_repository()


def test_edit_user():

    test_app = app.test_client()

    response = test_app.post("/movies", data={
        "movie_name": "star wars",
        "movie_director": "george lucas",
        "movie_rating": 4,
    })


    assert movie_repository.get_movie_by_title("star wars") != None

    assert response.status_code == 302 or response.status_code == 200