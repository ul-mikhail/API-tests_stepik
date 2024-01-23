import requests
import json

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass
    def get_category_list(self):
        """Получаем и возвращаем список категорий"""
        url = 'https://api.chucknorris.io/jokes/categories'
        print(url)
        result = requests.get(url)
        print('статус код ', result.status_code)
        assert result.status_code == 200
        print('Успешно')
        result.encoding = 'utf-8'
        category_list = json.loads(result.text)
        print('Список категорий -', category_list)
        return category_list

    def test_create_category_joke(self, category):
        """Создание шутки по категории"""
        url = 'https://api.chucknorris.io/jokes/random?category=' + category
        print(url)
        result = requests.get(url)
        print('статус код ', result.status_code)
        assert result.status_code == 200
        print('Успешно! мы получили новую шутку!')

        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == [category]
        print('Категория верна')

        check_info_value = check.get('value')
        print('Шутка: ', check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print("Чак присутствует!")
        else:
            print("Чака нет!!!")


tema_shutki = input("Введите категорию шутки ")
new_joke = Test_new_joke()
spisok_kategorii = new_joke.get_category_list()
if tema_shutki in spisok_kategorii:
    new_joke.test_create_category_joke(tema_shutki)
else:
    print('Введенной Вами категории в списке нет!')

