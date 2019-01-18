import pytest
from src.helloworld.ressources.movies import Movies


class TestMovies(object):
    def test_get(self):
        assert Movies().get() == {'pulp': 'fiction'}
