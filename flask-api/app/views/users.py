from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema


def post_user():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]

    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "message": f"Unable to create. An error occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def update_user(id):
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]

    user = Users.query.get(id)

    if not user:
        return jsonify({"message": "user don't exist", "data": {}})

    pass_hash = generate_password_hash(password)

    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email

        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "successfully update", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "message": f"Unable to update. An error occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )


def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({"message": "successesfully fetched", "data": result}), 201

    return jsonify({"message": "nothing found", "data": {}}), 401


def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "successesfully fetched", "data": result}), 201

    return jsonify({"message": "nothing found", "data": {}}), 404


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({"message": "nothing found", "data": {}}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)

        return jsonify({"message": "Successfully delete", "data": result}), 201
    except Exception as e:
        db.session.rollback()
        return (
            jsonify(
                {
                    "message": f"Unable to delete. An error occurred: {str(e)}",
                    "data": {},
                }
            ),
            500,
        )
