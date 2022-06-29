import requests
import pytest


def test_user_details():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    body = response.json()
    assert body['name'] == "Leanne Graham"
    assert body['company']['name'] == "Romaguera-Crona"

def test_users_details():

    another_response = requests.get("https://jsonplaceholder.typicode.com/users/")
    another_body = another_response.json()
    assert another_body[1]['name'] == "Ervin Howell"
    assert another_body[7]['company']['name'] == "Abernathy Group"