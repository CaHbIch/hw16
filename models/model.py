from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(50), unique=True)
    role = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), unique=True)

    def __repr__(self):
        return f"<id{self.id}>"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=True)
    description = db.Column(db.String, nullable=True)
    start_date = db.Column(db.String(12), nullable=True)
    end_date = db.Column(db.String(12), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('offer.id'))


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
