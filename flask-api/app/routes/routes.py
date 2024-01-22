import json
from app import app
from ..views import users, helper, keyboards
from flask import jsonify, request


@app.route("/", methods=["GET"])
@helper.token_required
def root():
    return jsonify({"message": "GET Success"})


@app.route("/users/<id>", methods=["GET", "DELETE", "PUT"])
def routes_by_user_specific(id):
    if request.method == "GET":
        return users.get_user(id)
    elif request.method == "DELETE":
        return users.delete_user(id)
    elif request.method == "PUT":
        return users.update_user(id)
    else:
        return jsonify({"message": "Página não encontrada", "data": {}}), 404


@app.route("/users", methods=["POST", "GET"])
def routes_by_all_user():
    if request.method == "POST":
        return users.post_user()
    elif request.method == "GET":
        return users.get_users()
    else:
        return jsonify({"message": "Página não encontrada", "data": {}}), 404


@app.route("/auth", methods=["POST"])
def auth():
    return helper.auth()


@app.route("/keyboards", methods=["POST", "GET"])
def routes_by_keyboards():
    if request.method == "POST":
        return keyboards.post_keyboard()
    elif request.method == "GET":
        return keyboards.get_keyboards()
    else:
        return jsonify({"message": "Página não encontrada", "data": {}}), 404


@app.route("/keyboards/<id>", methods=["DELETE", "PUT", 'GET'])
def routes_by_keyboard_specific(id):
    if request.method == "DELETE":
        return keyboards.delete_keyboard(id)
    elif request.method == "PUT":
        return keyboards.update_keyboard(id)
    elif request.method == "GET":
        return keyboards.get_keyboard(id)
    else:
        return jsonify({"message": "Página não encontrada", "data": {}}), 404
