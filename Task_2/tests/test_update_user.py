import pytest
import requests
import allure
from helpers.urls import URLs
from helpers.data import TestData
from tests.conftest import generate_unique_email


@allure.feature("Изменение данных пользователя")
class TestUpdateUser:

    @allure.title("Изменение имени пользователя с авторизацией")
    def test_update_user_name_with_auth(self, create_authorized_user):
        user_info = create_authorized_user
        
        update_data = {"name": TestData.UPDATED_USER_DATA["name"]}
        headers = {"Authorization": user_info["access_token"]}
        response = requests.patch(URLs.USER, json=update_data, headers=headers)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert response_data["user"]["name"] == TestData.UPDATED_USER_DATA["name"]

    @allure.title("Изменение email пользователя с авторизацией")
    def test_update_user_email_with_auth(self, create_authorized_user):
        user_info = create_authorized_user
        
        unique_email = generate_unique_email().replace("test_", "updated_")
        
        update_data = {"email": unique_email}
        headers = {"Authorization": user_info["access_token"]}
        response = requests.patch(URLs.USER, json=update_data, headers=headers)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert response_data["user"]["email"] == unique_email

    @allure.title("Изменение имени пользователя без авторизации")
    def test_update_user_name_without_auth(self):
        update_data = {"name": TestData.UPDATED_USER_DATA["name"]}
        response = requests.patch(URLs.USER, json=update_data)

        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["unauthorized"]

    @allure.title("Изменение email пользователя без авторизации")
    def test_update_user_email_without_auth(self):
        update_data = {"email": TestData.UPDATED_USER_DATA["email"]}
        response = requests.patch(URLs.USER, json=update_data)

        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["unauthorized"]