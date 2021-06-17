import pymongo

class dbLayer(object):
	def __init__(self):
		self.__open_connection()

	def __open_connection(self):
		# Hardcoded database URL and PORT isn't a good practice but it's okay since we're using just two containers
		# mongodb://<username>:<password@<host>:<port>/<database>
		mongo_uri = 'mongodb://adam:BADPRACTICEHEREFOLKS@172.16.238.10:27017'

		self.client = pymongo.MongoClient(mongo_uri)
		self.db = self.client['backend']