#import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserGet(BaseCase):
    def setup_method(self):
        data = {
            'email': 'useremal12345@email.ru',
            'password': '12345'
        }
        #response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)
        response1 = MyRequests.post(url='/user/login', data=data)

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_auth = self.get_json_value(response1, 'user_id')

    def test_get_user_details_not_auth(self):
        id = 2
        #response = requests.get(url=f'https://playground.learnqa.ru/api/user/{id}')
        response = MyRequests.get(url=f'/user/{id}')
        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_key(response, 'firstName')
        Assertions.assert_json_has_not_key(response, 'lastName')
        Assertions.assert_json_has_not_key(response, 'email')

    def test_get_user_details_auth(self):
        #response = requests.get(url=f'https://playground.learnqa.ru/api/user/{self.user_id_auth}', cookies={'auth_sid':self.auth_sid}, headers={'x-csrf-token': self.token})
        response = MyRequests.get(url=f'/user/{self.user_id_auth}', cookies={'auth_sid': self.auth_sid}, headers={'x-csrf-token': self.token})
        print("Answer ", response.text)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_key(response, 'firstName')
        Assertions.assert_json_has_key(response, 'lastName')
        Assertions.assert_json_has_key(response, 'email')