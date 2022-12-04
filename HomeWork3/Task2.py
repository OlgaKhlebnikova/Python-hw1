# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
from functions import fill_list, List
import math


def mult_pairs_list_items(nums_list: List[int]) -> List:
    '''
    Возвращает список, состоящий из произведений пар элементов исходного списка
    Пара элементов это первый и последний элемент, второй и предпоследний и т.д.

    Args:
      List[int] - Список числел
    Reterns:
      List[int] - Cписок произведений числел
    '''
    mult_list = []
    for i in range(math.ceil(len(numbers)/2)):
        mult_list.append(nums_list[i] * nums_list[-(i+1)])
    return mult_list

numbers = fill_list()
result = mult_pairs_list_items(numbers)
print(f'Список элементов {numbers}')
print(f'Произведение пар элементов списка равна {result}')
