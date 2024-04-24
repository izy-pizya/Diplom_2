import allure
from conftest import *
from data import EndpointsUrl
from data import Ingredients
from data import ErrorMessage


@allure.feature('Проверяем создание заказа')
class TestApiCreateOrder:
    @allure.title('Test of creating an order for an authorized user')
    def test_auth_user_create_order_successful(self, token):
        user_token = token
        data = Ingredients.INGREDIENTS
        response = requests.post(EndpointsUrl.ORDER, headers={'Authorization': user_token}, json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Test of creating an order with ingredients without authorization')
    def test_create_order_with_ingredients_user_no_auth_successful(self):
        data = Ingredients.INGREDIENTS
        response = requests.post(EndpointsUrl.ORDER, json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Test for creating an order without ingredients')
    def test_create_order_without_ingredients_error(self):
        data = Ingredients.WITHOUT_INGREDIENTS
        response = requests.post(EndpointsUrl.ORDER, json=data)
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.ERROR_INGREDIENT

    @allure.title('Test of creating an order with incorrect ingredients')
    def test_create_order_bad_ingredients_error(self):
        data = Ingredients.INCORRECT_INGREDIENTS
        response = requests.post(EndpointsUrl.ORDER, json=data)
        assert response.status_code == 500
        assert ErrorMessage.SERVER_ERROR in response.text


