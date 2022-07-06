from flask import jsonify

from model import User
from schemas import userschema
from setup_db import db


class Service:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def get_all_users(self):
        all_users = db.session.query(User).all()
        result = userschema.dump(all_users)
        return jsonify(result)

