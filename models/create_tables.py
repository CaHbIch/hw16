import json
from pprint import pp

from model import Users
from models.config import DATAUSERS, DATAORDERS, DATAOFFER
from app import app, db

# users_json = json.dumps(DATAUSERS, ensure_ascii=False, indent=2)

# Создаем модельки
users = [Users(**user_data) for user_data in DATAUSERS]


# Закидываем модели в сессию
db.session.add(users)

# Пишем в базу изменения
db.session.commit()
