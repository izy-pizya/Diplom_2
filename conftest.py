import pytest
import requests
import string
import random
from data import EndpointsUrl


@pytest.fixture(scope="function")
def user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(6)}@yandex.ru'
    password = generate_random_string(6)
    name = generate_random_string(6)

    user_data = {
        "email": email,
        "password": password,
        "name": name
    }

    yield user_data

    data = {
        "email": user_data["email"],
        "password": user_data["password"],
    }
    response = requests.post(EndpointsUrl.LOGIN_USER, json=data)
    token = response.json().get("accessToken")

    if token:
        requests.delete(EndpointsUrl.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def token():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(6)}@yandex.ru'
    password = generate_random_string(6)
    name = generate_random_string(6)

    data = {"email": email, "password": password, "name": name}
    response = requests.post(EndpointsUrl.CREATE_USER, json=data)
    token = response.json().get("accessToken")

    yield token
    requests.delete(EndpointsUrl.DELETE_USER, headers={'Authorization': token})

