import pymysql
import os


ROOT = os.getenv('USER_MYSQL')
PASSWORD = os.getenv('PASSWORD_MYSQL')

conn = pymysql.connect(
    user=ROOT,
    password=PASSWORD
)

sql = conn.cursor()

sql.execute('create database if not exists APIMercado')
sql.execute('use APIMercado')
sql.execute('create table if not exists admins(email varchar(70), password varchar(255))')
sql.execute('insert into admins values("admin", "admin")')
sql.execute('create table if not exists produtos(id int auto_increment primary key, name varchar(70), price float, description text, inventory int, barcode bigint)')


class MySQL:
    def set_product(self, name: str, price: float, 
                    description: str, inventory: int, barcode: int):

        sql.execute('insert into produtos(name, price, description, inventory, barcode) values(%s, %s, %s, %s, %s)', (name, float(price), description, int(inventory), int(barcode), ))
        conn.commit()


    def modify_product(self, id, new: dict):
        sql.execute('update produtos set name = %s, price = %s, description = %s, inventory = %s, barcode = %s where id = %s',
                    (new['name'], new['price'], new['description'], new['inventory'], new['barcode'], int(id)))
        conn.commit()

    
    def return_product(self, id):
        sql.execute('select * from produtos where id = %s', (int(id)))
        product = sql.fetchone()

        if not product:
            return None

        product_dict = {
            'id': product[0],
            'name': product[1],
            'description': product[3],
            'price': product[2],
            'inventory': product[4],
            'barcode': product[5]
        }
        
        return product_dict


    def return_all(self):
        sql.execute('select * from produtos')
        products = sql.fetchall()

        if not products:
            return None

        all_products = []

        for p in products:
            all_products.append({
                'id': p[0],
                'name': p[1],
                'description': p[3],
                'price': p[2],
                'inventory': p[4],
                'barcode': p[5]
            })

        return all_products


    def delete_product(self, id):
        sql.execute('delete from produtos where id = %s', (int(id)))
        conn.commit()


class AdminAuth:
    def __init__(self, user):
        sql.execute('select password from admins where user = %s', (user, ))
        password = sql.fetchone()

        self.password = password
