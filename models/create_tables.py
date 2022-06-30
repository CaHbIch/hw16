import json
from pprint import pp
from models.config import DATAUSERS, DATAORDERS, DATAOFFER
from setup_db import db

users_json = json.dumps(DATAUSERS, ensure_ascii=False, indent=2)


# Закидываем модели в сессию
db.session.add(DATAUSERS)

# Пишем в базу изменения
db.session.commit()
