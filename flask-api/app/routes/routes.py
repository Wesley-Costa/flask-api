from flask import jsonify
from views import users, helper, keyboards
from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/')
keyboard = Blueprint('keyboard', __name__, url_prefix='/')


@user.route("/", methods=["GET"])
@helper.token_required
def root(current_user):
    return jsonify({"message": "Test message"})


@user.route("/users", methods=["POST"])
def post_user():
    return users.post_user()


@user.route("/users/<id>", methods=["PUT"])
def update_user(id):
    return users.update_user(id)


@user.route("/users", methods=["GET"])
def get_users():
    return users.get_users()


@user.route("/users/<id>", methods=["GET"])
def get_user(id):
    return users.get_user(id)


@user.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    return users.delete_user(id)


@user.route("/auth", methods=["POST"])
def auth():
    return helper.auth()


@keyboard.route("/keyboards", methods=["GET"])
def get_keyboards():
    return keyboards.get_keyboards()


@keyboard.route("/keyboards/<id>", methods=["GET"])
def get_keyboard(id):
    return keyboards.get_keyboard(id)


@keyboard.route("/keyboards", methods=["POST"])
def post_keyboards():
    return keyboards.post_keyboard()


@keyboard.route("/keyboards/<id>", methods=["PUT"])
def update_keyboards(id):
    return keyboards.update_keyboard(id)


@keyboard.route("/keyboards/<id>", methods=["DELETE"])
def delete_keyboard(id):
    return keyboards.delete_keyboard(id)
