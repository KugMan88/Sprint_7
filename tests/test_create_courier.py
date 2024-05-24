import allure
import pytest
from data.courier_api import *
from data.test_data import TestCourier, CourierErrors
from data.urls import TestAPIBaseLinks, TestAPICourierLinks

class TestAPICourierCreate:
    @allure.description('Проверка успешного создания курьера | POST /api/v1/courier')
    @allure.title('Курьер создается')
    def test_create_new_courier_successful(self, unregistered_user):
        courier_signin = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL, data=unregistered_user)
        courier_id = courier_signin.json()["id"]
        requests.delete(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL + str(courier_id))

        assert courier_signin.status_code == 200

    @allure.description('Проверка на создание дубликата курьера | POST /api/v1/courier')
    @allure.title('Получение ошибки при создании дубликата курьера')
    def test_create_double_courier_is_failed(self, test_user):
        exist_login_courier = \
            {
                "login": test_user[1][0],
                "password": test_user[1][1],
                "firstName": test_user[1][2]
            }

        r = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.COURIER_URL, data=exist_login_courier)

        assert r.status_code == 409 and r.json()['message'] == CourierErrors.create_already_exist

    @allure.description('Проверка создания курьера без обязательных полей | POST /api/v1/courier')
    @allure.title('Получение ошибки при создание курьера без обязательных полей')
    @pytest.mark.parametrize('user_data', (TestCourier.create_no_login_courier, TestCourier.create_no_password_courier,
                                           TestCourier.create_empty_login, TestCourier.create_empty_password))
    def test_create_courier_without_data_failed(self, user_data):
        r = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.COURIER_URL, data=user_data)

        assert r.status_code == 400 and r.json()['message'] == CourierErrors.create_no_data