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
        new_user = User(**json.loads(request.data))
        db.session.add(new_user)
        db.session.commit()
        return f'Пользователь {new_user.first_name} добавлен'


@app.route("/users/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def get_user(pk):
    if request.method == "GET":
        user = service.get_one_user(pk)
        return user
    elif request.method == "PUT":
        user_data = json.loads(request.data)
        new_user = db.session.query(User).filter(User.id == pk)
        new_user.update(user_data)
        db.session.commit()
        return f"Пользователь  обновлен"
    elif request.method == "DELETE":
        user_data = User.query.get(pk)
        db.session.delete(user_data)
        db.session.commit()
        return "Пользователь удален"


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == "GET":
        all_orders = service.get_orders()
        return all_orders
    elif request.method == "POST":
        new_order = Order(**json.loads(request.data))
        db.session.add(new_order)
        db.session.commit()
        return f'Заказ {new_order.name} добавлен'


@app.route("/orders/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def get_order(pk):
    if request.method == "GET":
        one_order = service.get_one_order(pk)
        return one_order
    elif request.method == "PUT":
        user_order = json.loads(request.data)
        new_order = db.session.query(Order).filter(Order.id == pk)
        new_order.update(user_order)
        db.session.commit()
        return "Заказ обновлен"
    elif request.method == "DELETE":
        user_order = Order.query.get(pk)
        db.session.delete(user_order)
        db.session.commit()
        return "заказ удален"


@app.route("/offer/", methods=['GET', 'POST'])
def get_offers():
    if request.method == "GET":
        all_orders = service.get_offers()
        return all_orders
    elif request.method == "POST":
        new_offer = Offer(**json.loads(request.data))
        db.session.add(new_offer)
        db.session.commit()
        return f'номер предложения {new_offer.id} добавлен'


@app.route("/offer/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def get_offer(pk):
    if request.method == "GET":
        one_offer = service.get_one_offer(pk)
        return one_offer
    elif request.method == "PUT":
        user_offer = json.loads(request.data)
        new_offer = db.session.query(Offer).filter(Offer.id == pk)
        new_offer.update(user_offer)
        db.session.commit()
        return "номер предложения обновлен"
    elif request.method == "DELETE":
        user_offer = Offer.query.get(pk)
        db.session.delete(user_offer)
        db.session.commit()
        return "Номер предложения удален"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
