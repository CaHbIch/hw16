import json
from models.config import DATAUSERS, DATAORDERS, DATAOFFER

users_json = json.dumps(DATAOFFER, ensure_ascii=False, indent=2)
print(users_json)


