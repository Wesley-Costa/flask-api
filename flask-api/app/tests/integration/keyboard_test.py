import json


def test_with_no_keyboards(client):
    response = client.get("/keyboards")

    assert response.status_code == 404
    assert response.data == b'{\n  "data": {},\n  "message": "No records found"\n}\n'


def test_with_keyboards(client, create_keyboards_for_test):
    expected = {
        "data": [
            {
                "brand": "Nord",
                "color": "Dark Red",
                "id": 1,
                "model": "Stage 5 78",
                "price": "R$ 25.000",
            }
        ],
        "message": "Sucessfully Fetched",
    }

    response = client.get("/keyboards")
    response_data = json.loads(response.text)

    del response_data["data"][0]["created_on"]

    assert response.status_code == 201
    assert response_data == expected


def test_post_keyboard(client):
    data = {
        "brand": "Nord",
        "color": "Dark Blue",
        "id": 1,
        "model": "Stage 5",
        "price": "R$ 100.000",
    }

    expected = {"data": data, "message": "Successfully registered"}

    response = client.post("/keyboards", json=data)
    response_data = json.loads(response.text)
    del response_data["data"]["created_on"]

    assert response.status_code == 201
    assert response_data == expected


def test_get_keyboard(client, create_keyboards_for_test):
    expected = {
        "data": {
            "brand": "Nord",
            "color": "Dark Red",
            "id": 1,
            "model": "Stage 5 78",
            "price": "R$ 25.000",
        },
        "message": "Sucessfully Fetched",
    }
    response = client.get("/keyboards/1")
    response_data = json.loads(response.text)
    del response_data["data"]["created_on"]
    assert response.status_code == 201
    assert response_data == expected

def test_delete_keyboard(client, create_keyboards_for_test):
    expected = {
        "data": {
            "brand": "Nord",
            "color": "Dark Red",
            "id": 1,
            "model": "Stage 5 78",
            "price": "R$ 25.000",
        },
        "message": "Sucessfully delete",
    }
    response = client.delete("/keyboards/1")

    response_data = json.loads(response.text)

    del response_data["data"]["created_on"]

    assert response.status_code == 201
    assert response_data == expected


def test_update_keyboard(client, create_keyboards_for_test):
    data = {
        "brand": "Nord",
        "model": "Stage 5",
        "id": 1,
        "color": "Dark Red",
        "price": "R$ 25.000",
    }

    expected = {"data": data, "message": "Updated successfully"}

    response = client.put("/keyboards/1", json=data)
    response_data = json.loads(response.text)

    del response_data["data"]["created_on"]

    assert response.status_code == 201
    assert response_data == expected


def test_update_no_keyboard(client):
    data = {
        "brand": "Nord",
        "model": "Stage 5",
        "color": "Dark Red",
        "price": "R$ 25.000",
    }

    response = client.put("/keyboards/1", json=data)
    response_data = json.loads(response.text)

    assert response.status_code == 404
    assert "User does not exist" in response_data['message']