from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # Используется для полей только для чтения
    first_name = fields.Str()
    last_name = fields.Str()
    age = fields.Str()
    email = fields.Str()
    role = fields.Str()
    phone = fields.Str()


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    start_date = fields.Str()
    end_date = fields.Str()
    address = fields.Str()
    price = fields.Float()


userschema = UserSchema(many=True)
orderschema = OrderSchema(many=True)  # many- только для итерируемых коллекций или объектов.
