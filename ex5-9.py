import json

import requests

#ex4
response = requests.get('https://playground.learnqa.ru/api/get_text')

print(response.text)

#ex5
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

json_obj = json.loads(json_text)
result = json_obj['messages'][1]['message']
print(result)

#ex6
redirect_response = requests.get('https://playground.learnqa.ru/api/long_redirect')

result = redirect_response.history
print(len(result))

#ex7

no_params_request = requests.get('https://playground.learnqa.ru/api/compare_query_type')
print("Отправка GET запроса без указания параметра methods: ", no_params_request.text)

no_list_request = requests.head('https://playground.learnqa.ru/api/compare_query_type')
print("Отправка запроса не из списка, метод HEAD: ", no_list_request.text)

good_request = requests.get('https://playground.learnqa.ru/api/compare_query_type', params='method=GET')
print("Отправка GET запроса с параметром method=GET: ", good_request.text)

good_request = requests.post('https://playground.learnqa.ru/api/compare_query_type', data='method=POST')
print("Отправка POST запроса с параметром method=POST: ", good_request.text)

good_request = requests.put('https://playground.learnqa.ru/api/compare_query_type', data='method=PUT')
print("Отправка PUT запроса с параметром method=PUT: ", good_request.text)

good_request = requests.delete('https://playground.learnqa.ru/api/compare_query_type', data='method=DELETE')
print("Отправка DELETE запроса с параметром method=DELETE: ", good_request.text)

methods_list = ['GET', 'POST', 'PUT', 'DELETE']
for method in methods_list:
    print("проверяем метод GET с ", method)
    request = requests.get('https://playground.learnqa.ru/api/compare_query_type', params=f'method={method}')
    print(request.text)
print()

for method in methods_list:
    print("проверяем метод POST с ", method)
    request = requests.post('https://playground.learnqa.ru/api/compare_query_type', data=f'method={method}')
    print(request.text)
print()

for method in methods_list:
    print("проверяем метод PUT с ", method)
    request = requests.put('https://playground.learnqa.ru/api/compare_query_type', data=f'method={method}')
    print(request.text)
print()

for method in methods_list:
    print("проверяем метод DELETE с ", method)
    request = requests.delete('https://playground.learnqa.ru/api/compare_query_type', data=f'method={method}')
    print(request.text)

#ex8

