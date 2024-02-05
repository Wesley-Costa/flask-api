from werkzeug.security import generate_password_hash
from flask import request, jsonify
from models.users import Users, user_schema, users_schema
from application import db
from repository.users_repository import save, delete, update


def post_user():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]
    pass_hash = generate_password_hash(password)

    try:
        user = Users(username, pass_hash, name, email)
        result = save(user)
        return jsonify({"message": "Successfully registered", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "error": f"Unable to create. An error has occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify(
            {"message": "User does not exist", "data": {}}, 404
        )

    try:
        user.username = request.json["username"]
        user.name = request.json["name"]
        user.email = request.json["email"]
        password = generate_password_hash(request.json["password"])
        user.password = password

        result = update(user)
        if result:
            return jsonify({"message": "Updated successfully", "data": result}), 201
    except Exception as e:
        return (
            jsonify(
                {
                    "message": f"Unable to update. An error has occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({"message": "Sucessfully Fetched", "data": result}), 201

    return jsonify({"message": "No records found", "data": {}}), 401


def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "Sucessfully Fetched", "data": result}), 201

    return jsonify({"error": "No records found", "data": {}}), 404


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({"error": "No records found", "data": {}}), 404

    try:
        result = delete(user)
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

