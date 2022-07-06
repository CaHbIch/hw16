from marshmallow import Schema, fields


class UserSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    age = fields.Str()
    email = fields.Str()
    role = fields.Str()
    phone = fields.Str()


class OrderSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    start_date = fields.Str()
    end_date = fields.Str()
    address = fields.Str()
    price = fields.Float()


class OfferSchema(Schema):
    order_id = fields.Int()
    executor_id = fields.Int()


userschema = UserSchema(many=True)
orderschema = OrderSchema(many=True)  # many- только для итерируемых коллекций или объектов.
offerschema = OfferSchema(many=True)
