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
    password_original = AuthAdmin(email).password[0]

    if not password_original:
        return False
    
    return password_original == password


class EcommerceUser(Resource):
    def get(self):
        # Retorna todos os produtos ao usuário
        return 'hello'


class Products(Resource):
    @auth.login_required
    def post(self):
        # Cadastra novos produtos
        data = request.json
        
        if not data:
            response = {'status': 'erro', 'mensagem': 'Dados do produto estão vazios'}

        try:
            MySQL().set_product(
                data['name'], data['price'], data['description'],
                data['inventory'], data['barcode']
            )
            response = data
        except KeyError:
            response = {'status': 'erro', 'mensagem': 'Alguns dados não foram preenchidos'}

        return response

    def get(self):
        id = request.args.get('id')

        if not id:
            # Retornando todos os produtos
            return MySQL().return_all()
        
        if not id.isnumeric():
            return {'status': 'erro', 'mensagem': 'ID deve ser um número'}
        
        product = MySQL().return_product(int(id))
        if not product:
            return {'status': 'erro', 'mensagem': 'Produto não encontrado'}

        return product

    @auth.login_required
    def put(self):
        # Altera produts existentes
        pass

    @auth.login_required
    def delete(self):
        # Deleta produtos
        pass


api.add_resource(EcommerceUser, '/')
api.add_resource(Products, '/admin/products')

if __name__ == '__main__':
    app.run(debug=True)