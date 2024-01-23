from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
from ..repository.users_repository import save, delete, update


def post_user():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]
    pass_hash = generate_password_hash(password)

    try:
        user = Users(username, pass_hash, name, email)
        result = save(user)
        return jsonify({"message": "Registrado com sucesso", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "error": f"Não foi possível criar. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify(
            {"message": "Usuário não existe", "data": {}}
        )

    try:
        user.username = request.json["username"]
        user.name = request.json["name"]
        user.email = request.json["email"]
        password = generate_password_hash(request.json["password"])
        user.password = password

        result = update(user)
        if result:
            return jsonify({"message": "Atualizado com sucesso", "data": result}), 201
    except Exception as e:
        return (
            jsonify(
                {
                    "message": f"Não foi possível atualizar. Um erro ocorreu: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({"message": "Dados obtidos com sucesso", "data": result}), 201

    return jsonify({"error": "Não foram encontrados registros", "data": {}}), 401


def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "Dados obtidos com sucesso", "data": result}), 201

    return jsonify({"error": "Não foram encontrados registros", "data": {}}), 404


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({"error": "Não foram encontrados registros", "data": {}}), 404

    try:
        result = delete(user)
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

