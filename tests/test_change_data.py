import allure
import requests as requests

from conftest import *
from data import EndpointsUrl
from data import ErrorMessage

@allure.feature('Проверяем изменения данных пользователя')
class TestApiUpdateUserData:
    @allure.title('Test of changing authorized user data')
    def test_login_user_change_name(self, token):
        user_token = token
        new_name = 'izy'
        data = {"name": new_name}
        response = requests.patch(EndpointsUrl.DELETE_USER, headers={'Authorization': user_token}, json=data)
        assert response.status_code == 200 and response.json()['success']


    @allure.title('Unauthorized user data modification test')
    def test_not_authorized_error(self, user):
        data = user
        response = requests.patch(EndpointsUrl.DELETE_USER, json=data)
        assert response.status_code == 401
        assert ErrorMessage.NOT_AUTHORIZED in response.text
