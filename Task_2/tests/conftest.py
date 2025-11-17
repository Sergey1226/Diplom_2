import pytest
import requests
import random
import string
from helpers.urls import URLs
from helpers.data import TestData


def generate_unique_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test_{random_string}@example.com"


def get_user_data():
    return {
        "email": generate_unique_email(),
        "password": TestData.DEFAULT_PASSWORD,
        "name": "Test User"
    }


@pytest.fixture
def create_authorized_user():
    user_data = get_user_data()
    response = requests.post(URLs.REGISTER, json=user_data)
    
    if response.status_code == 200:
        response_data = response.json()
        return {
            "user_data": user_data,
            "access_token": response_data["accessToken"],
            "refresh_token": response_data["refreshToken"]
        }
    return None


@pytest.fixture
def get_valid_ingredients():
    try:
        response = requests.get(URLs.INGREDIENTS, timeout=10)
        if response.status_code == 200:
            ingredients = response.json()["data"]
            if len(ingredients) >= 2:
                return [ingredients[0]["_id"], ingredients[1]["_id"]]
    except requests.exceptions.RequestException:
        pass
    
    pytest.fail("Не удалось получить валидные ингредиенты с сервера")