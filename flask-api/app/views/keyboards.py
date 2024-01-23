from app import db
from flask import request, jsonify
from ..models.keyboards import Keyboards, keyboard_schema, keyboards_schema
from ..repository.keyboards_repository import save, delete, update


def post_keyboard():
    req_json = request.json
    brand = request.json.get("brand", False)
    model = request.json.get("model", False)
    color = request.json.get("color", False)
    price = request.json.get("price", False)

    if not brand or not model or not color or not price:
        return jsonify({"error": "Preencha os dados corretamente."}), 400

    keyboard = Keyboards(brand, model, color, price)
    try:
        result = save(keyboard, req_json)
        if result:
            return jsonify({"message": "Registrado com sucesso", "data": result}), 201
    except Exception as e:
        return (
            jsonify(
                {
                    "message": f"Não foi possível criar. Erro: {str(e)}",
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

    return jsonify({"error": "Não foram encontrados registros", "data": {}}), 404


def get_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if keyboard:
        result = keyboard_schema.dump(keyboard)
        return jsonify({"message": "Dados obtidos com sucesso", "data": result}), 201
    return jsonify({"error": "Não foram encontrados registros", "data": {}}), 404


def delete_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if not keyboard:
        return jsonify({"error": "Preencha os dados corretamente."}), 400

    try:
        result = delete(keyboard)

        if result:
            return jsonify({"message": "Excluido com sucesso", "data": result}), 201
    except Exception as e:
        return (
            jsonify(
                {
                    "error": f"Não foi possível excluir o registro. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def update_keyboard(id):
    keyboard = Keyboards.query.get(id)

    if not keyboard:
        return jsonify({"error": "Registro não existe", "data": {}})

    try:
        keyboard.brand = request.json["brand"]
        keyboard.model = request.json["model"]
        keyboard.color = request.json["color"]
        keyboard.price = request.json["price"]

        result = update(keyboard)
        if result:
            return jsonify({"message": "Atualizado com sucesso", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "error": f"Não foi possível atualizar. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )
