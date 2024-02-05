from flask import request, jsonify
from models.keyboards import Keyboards, keyboard_schema, keyboards_schema
from application import db
from repository.keyboards_repository import save, delete, update


def post_keyboard():
    brand = request.json.get("brand", False)
    model = request.json.get("model", False)
    color = request.json.get("color", False)
    price = request.json.get("price", False)

    if not brand or not model or not color or not price:
        return jsonify({"error": "Fill in the data correctly."}), 404

    keyboard = Keyboards(brand, model, color, price)
    try:
        result = save(keyboard)
        if result:
            return jsonify({"message": "Successfully registered", "data": result}), 201
    except Exception as e:
        return (
            jsonify(
                {
                    "message": f"Unable to create. An error has occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def get_keyboards():
    keyboards = Keyboards.query.all()
    if keyboards:
        result = keyboards_schema.dump(keyboards)
        return jsonify({"message": "Sucessfully Fetched", "data": result}), 201

    return jsonify({"message": "No records found", "data": {}}), 404


def get_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if keyboard:
        result = keyboard_schema.dump(keyboard)
        return jsonify({"message": "Sucessfully Fetched", "data": result}), 201
    return jsonify({"message": "No records found", "data": {}}), 404


def delete_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if not keyboard:
        return jsonify({"error": "No records found", "data": {}}), 404

    try:
        result = delete(keyboard)
        if result:
            return jsonify({"message": "Sucessfully delete", "data": result}), 201
    except Exception as e:
        return (
            jsonify(
                {
                    "message": f"Unable to delete record. An error has occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def update_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if not keyboard:
        return (jsonify({"message": "User does not exist", "data": {}}), 404)

    try:
        keyboard.brand = request.json["brand"]
        keyboard.model = request.json["model"]
        keyboard.color = request.json["color"]
        keyboard.price = request.json["price"]

        result = update(keyboard)
        if result:
            return jsonify({"message": "Updated successfully", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "message": f"Unable to update. An error has occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )
