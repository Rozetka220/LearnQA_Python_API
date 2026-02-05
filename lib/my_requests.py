import requests


class MyRequests():
    @staticmethod
    def post(url: str, data: dict = None,headers: dict = None, cookies: dict = None):
        return MyRequests._send(url=url, data=data, headers=headers, cookies=cookies, method='POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url=url, data=data, headers=headers, cookies=cookies, method='GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url=url, data=data, headers=headers, cookies=cookies, method='PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url=url, data=data, headers=headers, cookies=cookies, method='DELETE')

    #В Python нет private функций, поэтому для обозначения внутренней функции такие функции называют начиная с "_"
    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str) -> requests.Response:
        url = f'https://playground.learnqa.ru/api{url}'

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f'Method {method} not supported')

        return response
