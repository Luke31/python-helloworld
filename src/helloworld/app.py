from flask import Flask
from flask_restful import Api
from src.helloworld.ressources.movies import Movies
from src.helloworld.ressources.wordcount import Wordcount

app = Flask(__name__)
api = Api(app)
api.add_resource(Movies, '/movies')
api.add_resource(Wordcount, '/wordcount/<text>')
