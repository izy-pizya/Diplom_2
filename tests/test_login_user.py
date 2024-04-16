import allure
from conftest import *
from data import EndpointsUrl
from data import ErrorMessage


@allure.feature('Проверяем авторизацию пользователя')
class TestLoginUser:
    @allure.title('Тест авторизации существующего пользователя')
    def test_login_existing_user(self, user):
        data = user
        response = requests.post(EndpointsUrl.CREATE_USER, json=data)
        assert response.status_code == 200 and response.json()['success']
        response_2 = requests.post(EndpointsUrl.LOGIN_USER, json=data)
        assert response_2.status_code == 200 and response.json()['success']

    @allure.title('Тест авторизации с неверным логином')
    def test_login_user_incorrect_email_error(self, user):
        data = user.copy()
        data["email"] = 'new_incorrect_email@example.com'
        response = requests.post(EndpointsUrl.LOGIN_USER, json=data)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.INCORRECT_DATA

    @allure.title('Тест авторизации с неверным паролем')
    def test_login_user_incorrect_password_error(self, user):
        data = user.copy()
        data["password"] = 'new_incorrect_password'
        response = requests.post(EndpointsUrl.LOGIN_USER, json=data)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.INCORRECT_DATA
