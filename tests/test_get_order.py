import allure
from conftest import *
from data import EndpointsUrl
from data import ErrorMessage


@allure.feature('Проверяем получение заказа пользователя')
class TestApiGetUserOrders:
    @allure.title('Получение заказа авторизованного пользователя')
    def test_auth_user_get_order_successful(self, token):
        user_token = token
        response = requests.get(EndpointsUrl.ORDER, headers={'Authorization': user_token})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Получение заказа пользователя без авторизации')
    def test_no_auth_user_get_user_order_error(self):
        user_token = None
        response = requests.get(EndpointsUrl.ORDER, headers={'Authorization': user_token})
        assert response.status_code == 401
        assert ErrorMessage.NOT_AUTHORIZED in response.text
