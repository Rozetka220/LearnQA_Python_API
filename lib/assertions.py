from http.client import responses

from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Это не json формат {response.text}'

        assert name in response_as_dict, f'В ответе нет нужного ключа {name}'
        assert response_as_dict[name] == expected_value, error_message