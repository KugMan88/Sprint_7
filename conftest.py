import pytest

from data.courier_api import *
from data.urls import TestAPIBaseLinks, TestAPICourierLinks


@pytest.fixture()
def test_user():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL + str(courier_id))


@pytest.fixture
def courier_login(test_user):
    return test_user[1][0]


@pytest.fixture
def courier_password(test_user):
    return test_user[1][1]

@pytest.fixture()
def unregistered_user():
    response, login_pass = register_new_courier_and_return_login_password()
    credentials = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    return credentials

@pytest.fixture()
def test_signin_user_id():
    response, login_pass = register_new_courier_and_return_login_password()

    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL, data=sign_in)
    courier_id = courier_signin.json()["id"]
    yield courier_id
    requests.delete(TestAPIBaseLinks.MAIN_URL + TestAPICourierLinks.LOGIN_URL + str(courier_id))