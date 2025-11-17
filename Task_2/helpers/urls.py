class URLs:
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    
    # Auth endpoints
    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    USER = f"{BASE_URL}/auth/user"
    
    # Order endpoints
    ORDERS = f"{BASE_URL}/orders"
    INGREDIENTS = f"{BASE_URL}/ingredients"