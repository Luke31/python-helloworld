"""Movies Resource."""

from flask_restful import Resource


class Movies(Resource):
    """
    Movies REST Endpoint.

    >>> Movies().get()
    {'pulp': 'fiction'}
    """

    # pylint: disable=R0201
    def get(self):
        """Get Method."""
        return {'pulp': 'fiction'}

    # pylint: disable=R0201
    def untested_method(self):
        """Untested method to test coverage checks."""
