import json
import bson

class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, bson.ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)
