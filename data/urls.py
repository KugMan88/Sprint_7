class TestAPIBaseLinks:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'


class TestAPICourierLinks:
    LOGIN_URL = '/api/v1/courier/login'
    COURIER_URL = '/api/v1/courier/'
    COURIER_ORDER_URL = '/ordersCount'


class TestAPIOrdersLinks:
    MAIN_ORDERS_URL = '/api/v1/orders'
    ACCEPT_ORDER_URL = '/api/v1/orders/accept/'
    FINISH_ORDER_URL = '/api/v1/orders/finish/'
    CANCEL_ORDER_URL = '/api/v1/orders/cancel'
    TRACK_ORDER_URL = '/api/v1/orders/track?t='