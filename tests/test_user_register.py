from datetime import datetime

import json
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserRegister():
    def setup_method(self):
        base_part = 'user'
        random_part = datetime.now().strftime('%Y%m%d%H%M%S')
        self.email = f'{base_part}{random_part}@domain.com'

    def test_create_user_successfully(self):
        data = {
            'password': 'password',
            'username': 'юзернэйм',
            'firstName': 'перовоеимя',
            'lastName': 'второеимя',
            'email': self.email
        }
        #response = requests.post(url='https://playground.learnqa.ru/api/user/', data=data)
        response = MyRequests.post(url='/user/', data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    def test_create_user_with_existing_email(self):
        email = 'useremal12345@email.ru'
        data = {
            'password': 'password',
            'username': 'юзернэйм',
            'firstName': 'перовоеимя',
            'lastName': 'второеимя',
            'email': email
        }
        #response = requests.post(url='https://playground.learnqa.ru/api/user/', data=data)
        response = MyRequests.post(url='/user/', data=data)
        Assertions.assert_code_status(response, 400)
        assert response.text == f"Users with email '{email}' already exists", f'Ответ сервера {response.content}'



