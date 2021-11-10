from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from sqldatabase import MySQL, AuthAdmin

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# Autenticação
@auth.verify_password
def auth_user(email, password):
    check_user = AuthAdmin(email).password[0]
    print(check_user)
    if not check_user:
        return False
    
    return check_user == password


class EcommerceUser(Resource):
    def get(self):
        # Retorna todos os produtos ao usuário
        return 'hello'


class Admin(Resource):
    @auth.login_required
    def post(self):
        # Cadastra novos produtos
        data = request.json
        print(data)

    @auth.login_required
    def put(self):
        # Altera produts existentes
        pass

    @auth.login_required
    def delete(self):
        # Deleta produtos
        pass


api.add_resource(EcommerceUser, '/')
api.add_resource(Admin, '/admin')

if __name__ == '__main__':
    app.run(debug=True)