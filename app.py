from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from sqldatabase import MySQL, AdminAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# Autenticação
@auth.verify_password
def auth_user(user, password):
    check_user = AdminAuth(user).password
    if not check_user:
        return False
    
    return check_user == password

class EcommerceUser(Resource):
    def get(self):
        # Retorna todos os produtos ao usuário
        pass


class Admin(Resource):
    @auth.login_required
    def post(self):
        # Cadastra novos produtos
        data = request.json()

    @auth.login_required
    def put(self):
        # Altera produts existentes
        pass

    @auth.login_required
    def delete(self):
        # Deleta produtos
        pass