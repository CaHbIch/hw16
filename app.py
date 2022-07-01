from flask import Flask
from config import DATABASE
from models.model import *

app = Flask(__name__)

# Конфигурация
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Связываем базу данных и приложение
db.init_app(app)

# Используйте для отправки контекста приложения при создании таблиц.
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
