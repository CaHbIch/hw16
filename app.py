import json

from flask import Flask, request

from classes.data_service import Service
from config import DATABASE
from models.model import *

app = Flask(__name__)

# Конфигурация
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False

service = Service(DATABASE)

# Связываем базу данных и приложение
db.init_app(app)

# Используется для отправки контекста приложения при создании таблиц.
app.app_context().push()


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == "GET":
        all_users = service.get_users()
        return all_users
    elif request.method == "POST":
        user = json.loads(request.data)
        new_user = User(
            id=user["id"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            age=user["age"],
            email=user["email"],
            role=user["role"],
            phone=user["phone"],
        )
        db.session.add(new_user)
        db.session.commit()
        return f'Пользователь добавлен {new_user}'

@app.route("/users/<int:pk>")
def get_user(pk):
    if request.method == "GET":
        user = service.get_one_user(pk)
        return user

@app.route("/orders/")
def get_orders():
    if request.method == "GET":
        all_orders = service.get_orders()
        return all_orders

@app.route("/orders/<int:pk>")
def get_order(pk):
    if request.method == "GET":
        one_order = service.get_one_order(pk)
        return one_order

@app.route("/offer/")
def get_offers():
    if request.method == "GET":
        all_orders = service.get_offers()
        return all_orders

@app.route("/offer/<int:pk>")
def get_offer(pk):
    if request.method == "GET":
        one_offer = service.get_one_offer(pk)
        return one_offer

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
