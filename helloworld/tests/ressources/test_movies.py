"""tests for movies.py."""

from unittest import TestCase

from helloworld.ressources.movies import Movies


class TestMovies(TestCase):
    """Test for Movies endpoint."""

    def test_get(self):
        """Test GET Method."""
        self.assertEqual(Movies().get(), {'pulp': 'fiction'})
