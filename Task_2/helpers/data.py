class TestData:
    DEFAULT_PASSWORD = "password123"
    
    UNAUTHORIZED_USER = {
        "email": "unauthorized@example.com",
        "password": "password123",
        "name": "Unauthorized User"
    }
    
    UPDATED_USER_DATA = {
        "name": "Updated User Name",
        "email": "updated_email@example.com"
    }
    
    ERROR_MESSAGES = {
        "user_exists": "User already exists",
        "required_fields": "Email, password and name are required fields",
        "invalid_credentials": "email or password are incorrect",
        "unauthorized": "You should be authorised",
        "ingredients_required": "Ingredient ids must be provided"
    }