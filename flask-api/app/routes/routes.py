import json
from app import app
from ..views import users, helper, keyboards
from flask import jsonify


@app.route("/", methods=["GET"])
@helper.token_required
def root(current_user):
    return jsonify({"message": "Test message"})


@app.route("/users", methods=["POST"])
def post_user():
    return users.post_user()


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    return users.update_user(id)


@app.route("/users", methods=["GET"])
def get_users():
    return users.get_users()


@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    return users.get_user(id)


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    return users.delete_user(id)


@app.route("/auth", methods=["POST"])
def auth():
    return helper.auth()


@app.route("/keyboards", methods=["GET"])
def get_keyboards():
    return keyboards.get_keyboards()


@app.route("/keyboards/<id>", methods=["GET"])
def get_keyboard(id):
    return keyboards.get_keyboard(id)


@app.route("/keyboards", methods=["POST"])
def post_keyboards():
    return keyboards.post_keyboard()


@app.route("/keyboards/<id>", methods=["PUT"])
def update_keyboards(id):
    return keyboards.update_keyboard(id)


@app.route("/keyboards/<id>", methods=["GET"])
def delete_keyboards(id):
    keyboards.delete_keyboard(id)
