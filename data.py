class EndpointsUrl:
    CREATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    LOGIN_USER = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    DELETE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'


class Ingredients:
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    WITHOUT_INGREDIENTS = {"ingredients": []}
    INCORRECT_INGREDIENTS = payload = {"ingredients": ["qwertyasdfghjkl123456789", "987654321qwertyasdfghjkl"]}


class ErrorMessage:
    SERVER_ERROR = "Internal Server Error"
    NOT_AUTHORIZED = "You should be authorised"
    EXIST_USER = 'User already exists'
    INCORRECT_DATA = "email or password are incorrect"
    REQUIRED_FIELD = "Email, password and name are required fields"
    ERROR_INGREDIENT = "Ingredient ids must be provided"

