from flask_restful import Resource


class Wordcount(Resource):
    def tokenize(self, text):
        return text.split()

    def get(self, text):
        tokens = self.tokenize(text)
        return {'wordcount': len(tokens)}
