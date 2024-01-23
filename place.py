import requests

class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_locaton(self):
        """Создание новой локации"""
        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'                      # параметр для всх запросов
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

        """Проверка создания новой локации"""

        get_resource = '/maps/api/place/get/json'    # Ресурс для метода GET
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код:", result_get.status_code)
        assert result_get.status_code == 200
        print('Проверка создания новой локации прошла успешно!')

        """Изменение новой локации"""

        put_resource = '/maps/api/place/update/json'    # Ресурс для метода PUT
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print("Статус код:", result_put.status_code)
        assert result_put.status_code == 200
        print('Изменение новой локации прошло успешно!')
        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print('Сообщение: ', check_put_info)
        assert check_put_info == "Address successfully updated"
        print('сообщение верно')

        """Проверка изменения локации"""

        get_resource = '/maps/api/place/get/json'    # Ресурс для метода GET
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код:", result_get.status_code)
        assert result_get.status_code == 200
        print('Проверка изменения локации прошла успешно!')
        check_adress = result_get.json()
        check_adress_info = check_adress.get('address')
        print('Новый дарес -', check_adress_info)
        assert check_adress_info == json_for_update_new_location.get("address")
        print('Новый адрес верен')

        """Изменение локации c несуществующим id"""

        put_resource = '/maps/api/place/update/json'    # Ресурс для метода PUT
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id + '1xy',
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print("Статус код:", result_put.status_code)
        assert result_put.status_code == 404
        print('Успех! Изменения локации не произошло!')
        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print('Сообщение: ', check_put_info)
        assert check_put_info == "Update address operation failed, looks like the data doesn't exists"
        print('сообщение верно')

        """Удаление новой локации"""

        delete_resource = '/maps/api/place/delete/json'    # Ресурс для метода PUT
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

        """Проверка удаления локации"""

        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код:", result_get.status_code)
        assert result_get.status_code == 404
        print('Проверка удаления локации прошла успешно!')
        check_msg = result_get.json()
        check_msg_info = check_msg.get('msg')
        print('Сообщение -', check_msg_info)
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print('Удаленная локация не находится')

        print('Тестирование Test_new_location завершено успешно')


new_place = Test_new_location()
new_place.test_create_new_locaton()