# -*- coding: utf-8 -*-

from flask import Flask
from flask_restx import Api
from werkzeug.utils import cached_property


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='CRUD - Movies',
            description='Movies simple Api',
            doc='/docs'
        )


    def run(self):
        self.app.run(
            debug=True
        )

server = Server()