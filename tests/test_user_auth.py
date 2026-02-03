import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):
    #Параметры для тестов, принято выносить на самый вверх
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    #Функция для подготовки данных для всех тестов типа TestUserAuth. Запускается автоматически для этого класса
    def setup_method(self):
        data = {
            'email': 'useremal12345@email.ru',
            'password': '12345'
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        #assert 'user_id' in response1.json(), 'Нет user_id в ответе'

        # self.auth_sid = response1.cookies['auth_sid']
        # self.token = response1.headers.get('x-csrf-token')
        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_auth = self.get_json_value(response1, 'user_id')

        #self.user_id_auth = response1.json()['user_id']

    def test_auth_user(self):
        response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token': self.token}, cookies={'auth_sid': self.auth_sid})

        Assertions.assert_json_value_by_name(response2, 'user_id', self.user_id_auth, 'User_ID отличаются')

        #assert 'user_id' in response2.json(), "В GET не вернулся user_id"
        #user_id_check = response2.json()['user_id']
        #assert user_id_check == self.user_id_auth, 'Юзер айди отличаются'

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token': self.token})
        else:
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth', cookies={'auth_sid': self.auth_sid})

        Assertions.assert_json_value_by_name(response2, 'user_id', 0, '"Произошла авторизация без {condition}')
        #assert 'user_id' in response2.json(), "Первый запрос не вернул user_id"
        #user_id_check = response2.json()['user_id']
        #assert user_id_check == 0, f"Произошла авторизация без {condition}"


