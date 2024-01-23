import requests

base_url = 'https://rahulshettyacademy.com'  # базовая url
key = '?key=qaclick123'  # параметр для всх запросов
def test_create_new_locaton():
    """Создание новой локации"""

    post_resource = '/maps/api/place/add/json'   # Ресурс для метода POST
    post_url = base_url + post_resource + key
    print(post_url)

    json_for_create_new_location = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    result_post = requests.post(post_url, json=json_for_create_new_location)
    print(result_post.text)
    print("Статус код:", result_post.status_code)
    assert result_post.status_code == 200
    print('Создана новая локация!')

    check_post = result_post.json()
    check_info_post = check_post.get('status')
    print("Статус в ответе:", check_info_post)
    assert check_info_post == 'OK'
    print('Статус в ответе верен')

    place_id = check_post.get('place_id')
    print('place_id:', place_id)

    """Добавляем place_id в файл"""

    with open('file_with_place_id.txt', 'a') as files:
        files.write(place_id + '\n')

    """Проверка создания новой локации"""

def get_new_location_from_file(place_id):
    get_resource = '/maps/api/place/get/json'    # Ресурс для метода GET
    get_url = base_url + get_resource + key + '&place_id=' + place_id
    print(get_url)
    result_get = requests.get(get_url)
    print(result_get.text)
    print("Статус код:", result_get.status_code)
    assert result_get.status_code == 200
    print('Проверка создания новой локации прошла успешно!')


"""5 запросов POST"""

for i in range(5):
    test_create_new_locaton()

"""Открываем файл с place_id и создаём переменную со списком этих id"""

with open('file_with_place_id.txt', 'r') as files:
    list_place_id = [i.strip() for i in files.readlines()]
    print('Список айдишников -', list_place_id)

"""Далее запросы GET с айдишниками из файла"""

for i in list_place_id:
    get_new_location_from_file(i)



