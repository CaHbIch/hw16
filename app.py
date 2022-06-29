from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from config import DATABASE

app = Flask(__name__)

# Конфигурация
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
