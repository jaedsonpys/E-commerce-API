from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)

class EcommerceUser(Resource):
    def get(self):
        # Retorna todos os produtos ao usuário
        pass