# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension
# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
from typing import List
def find_second_occurence(string_list: List[str], search_word: str) -> int:
    try:
        list_indexes = [index for index, string in enumerate(
            string_list) if string == search_word]
        return list_indexes[1]
    except IndexError:
        return -1

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
need_find = 'qwe'
print (f'Список {my_list}  ищем 2 вхождение "{need_find}"  ответ  - {find_second_occurence(my_list, need_find)}')