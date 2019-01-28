"""
Hello World REST Application.

Assembles all the REST endpoints.
"""


from flask import Flask

from flask_restful import Api

from helloworld.ressources.movies import Movies
from helloworld.ressources.wordcount import Wordcount

APP = Flask(__name__)
API = Api(APP)
API.add_resource(Movies, '/movies')
API.add_resource(Wordcount, '/wordcount/<text>')
