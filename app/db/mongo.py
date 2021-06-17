import motor.motor_asyncio

class dbLayer(object):
	def __init__(self):
		self.__open_connection()

	def __open_connection(self):
		# Hardcoded database URL and PORT isn't a good practice but it's okay since we're changing it soon
		# mongodb://<username>:<password@<host>:<port>/<database>
		mongo_uri = 'mongodb://adam:BADPRACTICEHEREFOLKS@172.16.238.10:27017'
		mongo_connection_args = {
			'zlibCompressionLevel': 7,
			'compressors': 'zlib'
		}

		self.client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri, **mongo_connection_args)
		self.db = self.client.get_database('backend')
		print(self.db.get_collection('movies'))