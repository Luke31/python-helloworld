"""Wordcount Resource."""

from flask_restful import Resource


class Wordcount(Resource):
    """Wordcount REST endpoint."""

    # pylint: disable=R0201
    def tokenize(self, text):
        """Split a string into tokens."""
        if text:
            return text.split()
        return []

    # pylint: disable=R0201
    def get(self, text):
        """GET method which tokenizes the path extension into tokens."""
        tokens = self.tokenize(text)
        return {'wordcount': len(tokens)}
