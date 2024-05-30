import random
import allure
import pytest
import requests
from faker import Faker
from data.urls import TestAPIBaseLinks, TestAPICourierLinks
import data.courier_api

@allure.step('Формируем тело для создания курьера')
@pytest.fixture()
def default_courier():
    fake = Faker()
    payload = {
        'login': fake.user_name(),
        'password': random.randint(10000, 9999999999),
        'firstName': fake.first_name()

    }
    return payload

@allure.step('Удаление тестовых данных')
@pytest.fixture()
def create_and_delete_courier(default_courier):
    yield default_courier
    response = requests.post(f'{TestAPIBaseLinks.MAIN_URL}/{TestAPICourierLinks.LOGIN_URL}',
                             data={'login': default_courier['login'], 'password': default_courier['password']})
    response_json = response.json()["id"]
    requests.delete(f'{TestAPIBaseLinks.MAIN_URL}/{TestAPICourierLinks.COURIER_URL}/{response_json}')

@allure.step('Проверка идентификатора пользователя')
@pytest.fixture()
def test_signin_user_id():
    response, login_pass = data.courier_api.register_new_courier_and_return_login_password()
    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    courier_signin = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL, data=sign_in)
    courier_id = courier_signin.json()["id"]
    yield courier_id
    requests.delete(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL + str(courier_id))

@allure.step('Проверка пользователя')
@pytest.fixture
def test_user():
    response, login_pass = data.courier_api.register_new_courier_and_return_login_password()
    yield response, login_pass
    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    courier_signin = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL + str(courier_id))