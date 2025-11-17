import pytest
import requests
import allure
from helpers.urls import URLs
from helpers.data import TestData


@allure.feature("Получение заказов конкретного пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, create_authorized_user):
        user_info = create_authorized_user
        
        headers = {"Authorization": user_info["access_token"]}
        response = requests.get(URLs.ORDERS, headers=headers)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert "orders" in response_data
        assert isinstance(response_data["orders"], list)

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_without_auth(self):
        response = requests.get(URLs.ORDERS)

        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["unauthorized"]