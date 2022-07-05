import json
from pprint import pp

from model import *
from models.config import DATAUSERS, DATAORDERS, DATAOFFER
from app import app, db

# users_json = json.dumps(DATAUSERS, ensure_ascii=False, indent=2)

# #Создаем модельки
users = [User(**user_data) for user_data in DATAUSERS]
order = [Order(**order_data) for order_data in DATAORDERS]
offer = [Offer(**offer_data) for offer_data in DATAOFFER]

# Закидываем модели в сессию
db.session.add_all(users)
db.session.add_all(order)
db.session.add_all(offer)

# Пишем в базу изменения
db.session.commit()
