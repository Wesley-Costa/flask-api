import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from .users import user_by_username
import jwt
from werkzeug.security import check_password_hash


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"message": "Token não encontrado", "data": []}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            print('>>', data)
            current_user = user_by_username(username=data["username"])
        except:
            return jsonify({"message": "Token expirado ou inválido", "data": []}), 401
        return f(current_user, *args, **kwargs)

    return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return (
            jsonify(
                {
                    "message": "Não foi possível verificar",
                    "WWW-Authenticate": 'Basic auth="Login required"',
                }
            ),
            401,
        )
    user = user_by_username(auth.username)
    if not user:
        return jsonify({"message": "Usuário não encontrado", "data": []}), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {
                "username": user.username,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
            },
            app.config["SECRET_KEY"],
        )
        return jsonify(
            {
                "message": "Validado com sucesso",
                "token": token,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
            }
        )

    return (
        jsonify(
            {
                "message": "Não é possível verificar",
                "WWW-Authenticate": 'Basic auth="Login required"',
            }
        ),
        401,
    )
