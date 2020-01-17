import pandas as pd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

# Creation Of Main Endpoint Classes
class Test(Resource):
    def post(self):

        # Get POST data as json & read it as a DataFrame
        new_x = request.get_json()

        print(new_x)
        return {'message': 'POST data read successfully'}

# Addition of the Endpoint Classes As Endpoints For The RESTFul API
api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(debug=True)