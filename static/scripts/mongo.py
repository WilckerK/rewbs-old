from flask_pymongo import PyMongo

class Mongo:
	def __init__(self, app):
		self.db = PyMongo(app).db

	def database(self):
		return self.db