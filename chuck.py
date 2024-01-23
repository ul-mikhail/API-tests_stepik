import requests
import json

url = 'https://api.chucknorris.io/jokes/categories'
print(url)
result = requests.get(url)
print('статус код ', result.status_code)
assert result.status_code == 200
print('Успешно')


result.encoding = 'utf-8'
category_list = json.loads(result.text)
print(category_list)
