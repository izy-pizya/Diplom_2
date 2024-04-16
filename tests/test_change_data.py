import allure
import requests as requests

from conftest import *
from data import EndpointsUrl
from data import ErrorMessage

@allure.feature('Проверяем изменения данных пользователя')
class TestApiUpdateUserData:
    @allure.title('Тест изменения данных авторизованного пользователя')
    def test_login_user_change_name(self, token):
        user_token = token
        new_name = 'Daniil'
        data = {"name": new_name}
        response = requests.patch(EndpointsUrl.DELETE_USER, headers={'Authorization': user_token}, json=data)
        assert response.status_code == 200 and response.json()['success']


    @allure.title('Тест изменения данных неавторизованного пользователя')
    def test_not_authorized_error(self, user):
        data = user
        response = requests.patch(EndpointsUrl.DELETE_USER, json=data)
        assert response.status_code == 401
        assert ErrorMessage.NOT_AUTHORIZED in response.text
