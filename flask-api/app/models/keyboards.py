import datetime
from app import db, ma


class Keyboards(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(20), nullable=False, unique=True)
    color = db.Column(db.String(20), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price


class KeyboardSchema(ma.Schema):
    class Meta:
        field = {"id", "brand", "model", "color", "price", "created_on"}


keyboard_schema = KeyboardSchema()
keyboards_schema = KeyboardSchema(many=True)
