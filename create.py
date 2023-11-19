#Харабиберова Анастасия 10 когорта - Финальный проект, инженер по тестированию плюс
import requests
from data import order_data
import configuration

def test_create_order_and_get_status():
    # Шаг 1: Запрос на создание заказа
    create_order_url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    create_order_response = requests.post(create_order_url, json=order_data)
    # Проверка успешного создания заказа
    assert create_order_response.status_code == 201
    assert "track" in create_order_response.json()
    track_number = create_order_response.json()["track"]

    # Шаг 2: Запрос на получение заказа
    get_order_url = configuration.URL_SERVICE + configuration.GET_ORDER + f"?t={track_number}"
    get_order_response = requests.get(get_order_url)

    # Шаг 3: Проверка, что код ответа равен 200
    assert get_order_response.status_code == 200

test_create_order_and_get_status()
