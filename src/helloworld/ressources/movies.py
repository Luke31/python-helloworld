from flask_restful import Resource


class Movies(Resource):
    def get(self):
        return {'pulp': 'fiction'}
