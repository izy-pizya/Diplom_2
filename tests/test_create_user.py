import allure
from conftest import *
from data import EndpointsUrl
from data import ErrorMessage


@allure.feature('Checking user creation')
class TestApiCreateUser:
    @allure.title('New user creation test')
    def test_create_new_user_successful(self, user):
        data = user
        response = requests.post(EndpointsUrl.CREATE_USER, json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('user duplicate test')
    def test_create_duplicate_user_error(self, user):
        data = user
        response = requests.post(EndpointsUrl.CREATE_USER, json=data)
        assert response.status_code == 200
        response_2 = requests.post(EndpointsUrl.CREATE_USER, json=data)
        assert response_2.status_code == 403 and response_2.json()['message'] == ErrorMessage.EXIST_USER

    @allure.title('Test error when creating a user without a required parameter')
    def test_create_user_without_one_field(self, user):
        data = user
        wrong_data = {"email": data["email"], "password": data["password"]}
        response = requests.post(EndpointsUrl.CREATE_USER, json=wrong_data)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorMessage.REQUIRED_FIELD
