import requests

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_random_joke(self):
        """Создание случайной шутки"""
        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print('статус код ', result.status_code)
        assert result.status_code == 200
        print('Успешно! мы получили новую шутку!')

        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print('Категория верна')

        check_info_value = check.get('value')
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print("Чак присутствует!")
        else:
            print("Чака нет!!!")

    def test_create_category_joke(self):
        """Создание шутки по категории"""
        category = 'sport'
        url = 'https://api.chucknorris.io/jokes/random?category=' + category
        print(url)
        result = requests.get(url)
        print('статус код ', result.status_code)
        assert result.status_code == 200
        print('Успешно! мы получили новую шутку!')

        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ['sport']
        print('Категория верна')

        check_info_value = check.get('value')
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print("Чак присутствует!")
        else:
            print("Чака нет!!!")

# random_joke = Test_new_joke()
# random_joke.test_create_random_joke()

sport_joke =Test_new_joke()
sport_joke.test_create_category_joke()