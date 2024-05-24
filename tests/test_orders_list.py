import allure
from data.courier_api import *
from data.urls import TestAPIOrdersLinks

class TestGetOrdersList:

    @allure.description("Получение списка заказов | GET /api/v1/orders")
    @allure.title('Успешное получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(TestAPIBaseLinks.MAIN_URL + TestAPIOrdersLinks.MAIN_ORDERS_URL)
        orders_list = response.json()["orders"]
        assert response.status_code == 200 and isinstance(orders_list, list) == True