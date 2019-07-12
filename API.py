# A RESTful API created using Python and Flask
# The API is used to store users' details

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
	{
		"name": "Nicholas",
		"age": 42,
		"occupation": "Network Engineer"
	},
	{
		"name": "Elvis",
		"age": 30,
		"occupation": "Teacher"
	},
	{
		"name": "John",
		"age": 32,
		"occupation": "Doctor"
	}
]

class User(Resource):
	def get(self, name):
		"""retrieves a particular user's details
		"""
		for user in users:
			if(name == user["name"]):
				return user, 200
		return "User not found", 404

	def post(self, name):
		"""creates a new user
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if (name == users["name"]):
				return "User with name {} already exists".format(name), 400
		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201

	def put(self, name):
		"""updates the details of a user or creates the user if it does not exist
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if (name == users["name"]):
				user["age"] = args["age"]
				user["occupation"] = args["occupation"]
				return user, 200

		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201

	def delete(self, name):
		"""deletes a given user
		"""
		global users
		users = [user for user in users if user[name]!= name]
		return "User {} was deleted".format(name), 200

# set up the API resource routing
api.add_resource(User, "/user/<string:name>")

if __name__ == '__main__':
	app.run(debug=True)
