from flask import jsonify

from model import User, Order, Offer
from schemas import userschema, orderschema, offerschema
from setup_db import db


class Service:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def get_users(self):
        """ получения всех пользователей """
        all_users = db.session.query(User).all()
        result = userschema.dump(all_users)
        return jsonify(result)

    def get_one_user(self, pk):
        """ одного пользователя по идентификатору """
        user = db.session.query(User).filter(User.id == pk).all()
        result = userschema.dump(user)
        return jsonify(result)

    def get_orders(self):
        """ запросы получения всех заказов """
        all_orders = db.session.query(Order).all()
        result = orderschema.dump(all_orders)
        return jsonify(result)

    def get_one_order(self, pk):
        """ заказы по идентификатору """
        order = db.session.query(Order).filter(Order.id == pk).all()
        result = orderschema.dump(order)
        return jsonify(result)

    def get_offers(self):
        """ получения всех предложений """
        all_offers = db.session.query(Offer).all()
        result = offerschema.dump(all_offers)
        return jsonify(result)

    def get_one_offer(self, pk):
        """ предложения по идентификатору """
        offer = db.session.query(Offer).filter(Offer.id == pk).all()
        result = offerschema.dump(offer)
        return jsonify(result)
