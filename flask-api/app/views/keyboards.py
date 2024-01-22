from app import db
from flask import request, jsonify
from ..models.keyboards import Keyboards, keyboard_schema, keyboards_schema


def post_keyboard():
    brand = request.json["brand"]
    model = request.json["model"]
    color = request.json["color"]
    price = request.json["price"]

    keyboard = Keyboards(brand, model, color, price)

    try:
        db.session.add(keyboard)
        db.session.commit()

        result = keyboard_schema.dump(keyboard)

        return jsonify({"message": "Registrado com sucesso", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "message": f"Não foi possível criar. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def get_keyboards():
    keyboards = Keyboards.query.all()
    if keyboards:
        result = keyboards_schema.dump(keyboards)
        return jsonify({"message": "Dados obtidos com sucesso", "data": result}), 201

    return jsonify({"message": "Não foram encontrados registros", "data": {}}), 404


def get_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if keyboard:
        result = keyboard_schema.dump(keyboard)
        return jsonify({"message": "Dados obtidos com sucesso", "data": result}), 201
    return jsonify({"message": "Não foram encontrados registros", "data": {}}), 404


def delete_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if not keyboard:
        return jsonify({"message": "Não foram encontrados registros", "data": {}}), 404

    try:
        db.session.delete(keyboard)
        db.session.commit()
        result = keyboard_schema.dump(keyboard)

        return jsonify({"message": "Excluido com sucesso", "data": result}), 201

    except Exception as e:
        db.session.rollback()

        return (
            jsonify(
                {
                    "message": f"Não foi possível excluir o registro. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def update_keyboard(id):
    brand = request.json["brand"]
    model = request.json["model"]
    color = request.json["color"]
    price = request.json["price"]

    keyboard = Keyboards.query.get(id)

    if not keyboard:
        return jsonify({"message": "Registro não existe", "data": {}})

    try:
        keyboard.brand = brand
        keyboard.model = model
        keyboard.color = color
        keyboard.price = price

        db.session.commit()

        result = keyboard_schema.dump(keyboard)

        return jsonify({"message": "Atualizado com sucesso", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "message": f"Não foi possível atualizar. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )
