import requests
import pytest

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'useremal12345@email.ru',
            'password': '12345'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert "auth_sid" in response1.cookies, "Проблема с куки"
        assert 'x-csrf-token' in response1.headers, 'Проблема с заголовком'
        assert 'user_id' in response1.json(), 'Нет user_id в ответе'

        auth_sid = response1.cookies['auth_sid']
        token = response1.headers.get('x-csrf-token')
        user_id_auth = response1.json()['user_id']

        response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        assert 'user_id' in response2.json(), "В GET не вернулся user_id"
        user_id_check = response2.json()['user_id']

        assert user_id_check == user_id_auth, 'Юзер айди отличаются'

    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'useremal12345@email.ru',
            'password': '12345'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert "auth_sid" in response1.cookies, "Проблема с куки"
        assert 'x-csrf-token' in response1.headers, 'Проблема с заголовком'
        assert 'user_id' in response1.json(), 'Нет user_id в ответе'

        auth_sid = response1.cookies['auth_sid']
        token = response1.headers.get('x-csrf-token')

        if condition == "no_cookie":
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token': token})
        else:
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth', cookies={'auth_sid': auth_sid})

        assert 'user_id' in response1.json(), "Первый запрос не вернул user_id"

        user_id_check = response2.json()['user_id']

        assert user_id_check == 0, f"Произошла авторизация без {condition}"


