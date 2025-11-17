import pytest
import requests
import allure
from helpers.urls import URLs
from helpers.data import TestData


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, create_authorized_user, get_valid_ingredients):
        user_info = create_authorized_user
        
        order_data = {"ingredients": get_valid_ingredients}
        headers = {"Authorization": user_info["access_token"]}
        response = requests.post(URLs.ORDERS, json=order_data, headers=headers)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert "name" in response_data
        assert "order" in response_data
        assert "number" in response_data["order"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, get_valid_ingredients):
        order_data = {"ingredients": get_valid_ingredients}
        response = requests.post(URLs.ORDERS, json=order_data)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert "order" in response_data
        assert "number" in response_data["order"]

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, create_authorized_user, get_valid_ingredients):
        user_info = create_authorized_user
        
        order_data = {"ingredients": get_valid_ingredients}
        headers = {"Authorization": user_info["access_token"]}
        response = requests.post(URLs.ORDERS, json=order_data, headers=headers)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert "name" in response_data
        assert "order" in response_data
        assert "number" in response_data["order"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_authorized_user):
        user_info = create_authorized_user
        
        order_data = {"ingredients": []}
        headers = {"Authorization": user_info["access_token"]}
        response = requests.post(URLs.ORDERS, json=order_data, headers=headers)

        assert response.status_code == 400
        response_data = response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["ingredients_required"]

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_authorized_user):
        user_info = create_authorized_user
        
        order_data = {"ingredients": ["invalid_hash_1", "invalid_hash_2"]}
        headers = {"Authorization": user_info["access_token"]}
        response = requests.post(URLs.ORDERS, json=order_data, headers=headers)

        assert response.status_code == 500