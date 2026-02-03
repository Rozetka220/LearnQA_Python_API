import requests
import pytest
import json

def test_phrase_check_len():
    phrase = input('Enter a phrase: ')
    assert len(phrase) < 15, "Фраза содержит больше 15 символов"

def test_cookie_method():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
    assert response.cookies['HomeWork'] == 'hw_value'

def test_header_method():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')
    assert response.headers['x-secret-homework-header'] == 'Some secret value', 'Неправильный заголовок'

def test_useragent_method():
    response = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check')
    assert json.loads(response.text)['user_agent'] == 'python-requests/2.32.5'
