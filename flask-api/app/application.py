from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
app: Flask

def create_app(test: False) -> Flask:
    app = Flask('__name__')

    if(test):
        app.config.from_object('configtest')
    else:
        app.config.from_object('config')

    from routes.routes import user, keyboard
    app.register_blueprint(user)
    app.register_blueprint(keyboard)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    return app



