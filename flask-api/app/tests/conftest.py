import pytest
from application import create_app, db
from models.users import Users
from models.keyboards import Keyboards


@pytest.fixture()
def app():
    app = create_app(test=True)

    # other setup can go here

    yield app

    # clean up / reset resources here
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def create_users_for_test(app):
    with app.app_context():
        db.session.add(
            Users(
                email="UsuárioTeste@Teste.com",
                name="Usuário Teste",
                password="12354567",
                username="UsuárioTeste",
            )
        )

        db.session.commit()


@pytest.fixture()
def create_keyboards_for_test(app):
    with app.app_context():
        db.session.add(
            Keyboards(
                brand="Nord", 
                color="Dark Red", 
                model="Stage 5 78", 
                price="R$ 25.000"
            )
        )

        db.session.commit()
