from flask import Flask
from flask_restful import Api
from src.helloworld.ressources.movies import Movies

srv = Flask(__name__)
api = Api(srv)
api.add_resource(Movies, '/')
