import pytest
import requests
import allure
from helpers.urls import URLs
from helpers.data import TestData
from tests.conftest import get_user_data


@allure.feature("Логин пользователя")
class TestLoginUser:
    
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self):
        user_data = get_user_data()
        create_response = requests.post(URLs.REGISTER, json=user_data)
        assert create_response.status_code == 200
        
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        
        response = requests.post(URLs.LOGIN, json=login_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] == True
        assert "accessToken" in response_data
        assert response_data["user"]["email"] == user_data["email"]
    
    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_credentials(self):
        login_data = {
            "email": TestData.UNAUTHORIZED_USER["email"],
            "password": "wrong_" + TestData.UNAUTHORIZED_USER["password"]  
        }
    
        response = requests.post(URLs.LOGIN, json=login_data)
    
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] == False
        assert response_data["message"] == TestData.ERROR_MESSAGES["invalid_credentials"]