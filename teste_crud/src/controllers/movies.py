# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restx import Api, Resource
from src.server.instance import server
from werkzeug.utils import cached_property

app = server.app
api = server.api




movies_db = [
	{'id':1, 'title':'Titanic'},
	{'id':2, 'title':'The Clone Wars'}
] 


@api.route('/filmes/')
class MovieList(Resource):
	
	# Traz todos os filmes
	def get(self):
		return movies_db

	
	def post(self):
		response = api.payload
		movies_db.append(response)
		return response, 200




@api.route('/filmes/<int:movie_id>')
class MovieSimple(Resource):

	def get(self, movie_id):
		for movie in movies_db:
			if movie_id and movie_id == movie['id']:
				return movie

	def delete(self, movie_id):
		for movie in movies_db:
			if movie_id and movie_id == movie['id']:
				movies_db.remove(movie)
				return 204



@api.route('/filmes/<string:movie_name>')
class MovieSimple2(Resource):

	def get(self, movie_name):
		for movie in movies_db:
			if movie_name and movie_name == movie['title']:
				return movie

	def delete(self, movie_name):
		for movie in movies_db:
			if movie_name and movie_name == movie['title']:
				movies_db.remove(movie)
				return 204

