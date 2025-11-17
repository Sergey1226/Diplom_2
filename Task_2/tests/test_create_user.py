import pytest
import requests
import allure
from helpers.urls import URLs
from helpers.data import TestData
from tests.conftest import get_user_data


@allure.feature("Создание пользователя")
class TestCreateUser:
    
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user_data = get_user_data()
        
        response = requests.post(URLs.REGISTER, json=user_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert "accessToken" in response_data
        assert response_data["user"]["email"] == user_data["email"]
    
    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        user_data = get_user_data()
        create_response = requests.post(URLs.REGISTER, json=user_data)
        assert create_response.status_code == 200
        
        duplicate_response = requests.post(URLs.REGISTER, json=user_data)
        
        assert duplicate_response.status_code == 403
        response_data = duplicate_response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["user_exists"]
    
    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        user_data = get_user_data()
        user_data.pop(missing_field)
        
        response = requests.post(URLs.REGISTER, json=user_data)
        
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["required_fields"]