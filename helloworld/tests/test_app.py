"""Tests for app.py."""

from unittest import TestCase

from helloworld.app import APP


class TestApp(TestCase):
    """Integration Test for app.py."""

    def test_app_movies(self):
        """Test /movies endpoint."""
        APP.testing = True
        with APP.test_client() as client:
            resp = client.get('/movies')
            self.assertEqual(resp.status, "200 OK")
            self.assertIsNotNone(resp.data)

    def test_app_wordcount(self):
        """Test /wordcount endpoint."""
        APP.testing = True
        with APP.test_client() as client:
            resp = client.get('/wordcount/hello%20world')
            self.assertEqual(resp.status, "200 OK")
            self.assertEqual(resp.get_json()['wordcount'], 2)

    def test_app_noroute(self):
        """Test non exiting endpoint."""
        APP.testing = True
        with APP.test_client() as client:
            resp = client.get('/notvalidroute')
            self.assertEqual(resp.status, "404 NOT FOUND")
            self.assertIsNotNone(resp.data)
