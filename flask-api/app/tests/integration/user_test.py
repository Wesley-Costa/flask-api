import json


def test_with_no_users(client):
    response = client.get("/users")

    assert response.status_code == 401

    assert response.data == b'{\n  "data": {},\n  "message": "No records found"\n}\n'


def test_with_users(client, create_users_for_test):
    expected = {
        "data": [
            {
                "email": "UsuárioTeste@Teste.com",
                "id": 1,
                "name": "Usuário Teste",
                "password": "12354567",
                "username": "UsuárioTeste",
            }
        ],
        "message": "Sucessfully Fetched",
    }
    response = client.get("/users")

    response_data = json.loads(response.text)

    del response_data["data"][0]["created_on"]  # remove timestamp because is useless

    assert response.status_code == 201
    assert response_data == expected


def test_get_user(client, create_users_for_test):
    expected = {
        "data": {
            "email": "UsuárioTeste@Teste.com",
            "id": 1,
            "name": "Usuário Teste",
            "password": "12354567",
            "username": "UsuárioTeste",
        },
        "message": "Sucessfully Fetched",
    }
    response = client.get("/users/1")

    response_data = json.loads(response.text)

    del response_data["data"]["created_on"]  # remove timestamp because is useless

    assert response.status_code == 201
    assert response_data == expected


def test_delete_one_user(client, create_users_for_test):
    expected = {
        "data": {
            "email": "UsuárioTeste@Teste.com",
            "id": 1,
            "name": "Usuário Teste",
            "password": "12354567",
            "username": "UsuárioTeste",
        },
        "message": "Sucessfully delete",
    }
    response = client.delete("/users/1")

    response_data = json.loads(response.text)

    del response_data["data"]["created_on"]  # remove timestamp because is useless

    assert response.status_code == 201
    assert response_data == expected


def test_update_user(client, create_users_for_test):
    data = {
        "email": "UsuárioTeste@Teste.com",
        "name": "Usuário Teste",
        "id": 1,
        "password": "12354567",
        "username": "UsuárioTeste2",
    }

    expected = {"data": data, "message": "Updated successfully"}

    response = client.put("/users/1", json=data)
    response_data = json.loads(response.text)

    print(response_data)

    del response_data["data"]["created_on"] 
    del response_data["data"]["password"]
    del expected["data"]["password"]

    assert response.status_code == 201
    assert response_data == expected

