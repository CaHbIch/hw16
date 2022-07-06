from flask import Flask

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


@app.route("/users/", methods=["GET"])
def get_users():
    all_users = service.get_all_users()
    return all_users


# @app.route("/")
# def get_users():
#     users = db.session.query(User.id, User.first_name, User.last_name).all()
#     for user in users:
#         return dict(user)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)
