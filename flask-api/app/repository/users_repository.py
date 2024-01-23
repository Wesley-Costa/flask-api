from werkzeug.security import generate_password_hash
from app import db
from ..models.users import Users, user_schema, users_schema
from flask import request


def save(user: Users):
    try:
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except Exception as e:
        db.session.rollback()
        raise e


def delete(user: Users):
    try:
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user)
    except Exception as e:
        db.session.rollback()
        raise e


def update(user: Users, request):
    try:
        user.username = request["username"]
        user.password = generate_password_hash(request["password"])
        user.name = request["name"]
        user.email = request["email"]

        db.session.commit()
        return user_schema.dump(user)
    except Exception as e:
        db.session.rollback()
        raise e


def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except Exception as e:
        return None
