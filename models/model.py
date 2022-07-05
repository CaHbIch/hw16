from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(50), unique=True)
    role = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), unique=True)

    order = db.relationship("Order")

    # def __int__(self, first_name, last_name, age, email, role, phone):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.age = age
    #     self.email = email
    #     self.role = role
    #     self.phone = phone

    def __repr__(self):
        return f"<id{self.id}>"


class Order(db.Model):
    __tablename__ = 'order'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=True)
    description = db.Column(db.String, nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float)

    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('offer.id'))

    users = db.relationship("User")

class Offer(db.Model):
    __tablename__ = 'offer'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
