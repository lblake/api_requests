import requests


def test_get_customer_details():
    response = requests.get("http://automation-engineer-test.herokuapp.com/customer")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "Our first customer"
    assert response_body[0]["email"] == "first-customer@bonhams.com"


def test_get_customer_id():
    response = requests.get("http://automation-engineer-test.herokuapp.com/customer/1")
    response_body = response.json()
    assert response_body["id"] == 1


def test_post_customer_id():
    response = requests.post(
        "http://automation-engineer-test.herokuapp.com/customer",
        {"name": "Lloyd", "email": "test@test.com"},
    )
    assert response.status_code == 201


def test_put_customer_id():
    response = requests.put(
        "http://automation-engineer-test.herokuapp.com/customer/3",
        {"name": "Lloyd2", "email": "test@test.com"},
    )
    assert response.status_code == 200
    response = requests.get("http://automation-engineer-test.herokuapp.com/customer/3")
    response_body = response.json()
    assert response_body["name"] == "Lloyd2"


def test_wrong_url():
    response = requests.get("http://automation-engineer-test.herokuapp.com/custome")
    assert response.status_code == 404


def test_name_value_incorrect():
    response = requests.put(
        "http://automation-engineer-test.herokuapp.com/customer/3",
        {"name": "626262", "email": "test@test.com"},
    )
    assert response.status_code == 200
