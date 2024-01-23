import requests

base_url = 'https://rahulshettyacademy.com'  # базовая url
key = '?key=qaclick123'  # параметр для всх запросов

"""Удаление новой локации"""

def delete_lokation(place_id):
    delete_resource = '/maps/api/place/delete/json'  # Ресурс для метода PUT
    delete_url = base_url + delete_resource + key
    print(delete_url)
    json_for_delete_location = {
        "place_id": place_id
    }
    result_delete = requests.delete(delete_url, json=json_for_delete_location)
    print(result_delete.text)
    print("Статус код:", result_delete.status_code)
    assert result_delete.status_code == 200
    print('Удаление локации прошло успешно!')
    check_status = result_delete.json()
    check_status_info = check_status.get('status')
    print('Сообщение: ', check_status_info)
    assert check_status_info == "OK"
    print('Статус верный')

"""Проверка наличия локации по id из файла и создание нового файла по результатам проверки"""
def get_new_location_from_file(place_id):
    get_resource = '/maps/api/place/get/json'    # Ресурс для метода GET
    get_url = base_url + get_resource + key + '&place_id=' + place_id
    print(get_url)
    result_get = requests.get(get_url)
    print(result_get.text)
    print("Статус код:", result_get.status_code)
    if result_get.status_code == 200:
        print('Проверка создания новой локации прошла успешно!')
        with open('new_file_with_place_id.txt', 'a') as files:
            files.write(place_id + '\n')
    else:
        print('Локации с таким place_id не существует!')


"""Открываем файл с place_id и создаём переменную со списком этих id"""

with open('file_with_place_id.txt', 'r') as files:
    list_place_id = [i.strip() for i in files.readlines()]
    print('Список айдишников -', list_place_id)

"""Далее запросы DELETE с айдишниками из файла"""

for i in range(len(list_place_id)):
    if i == 1 or i == 3:
        delete_lokation(list_place_id[i])

"""Затем GET запросы + создание нового файла с существующими place_id"""
for i in list_place_id:
    get_new_location_from_file(i)
