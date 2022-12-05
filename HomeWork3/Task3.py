# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114
import random
from functions import fill_list, List


def fill_list(num_list=[]):
    ''' 
    Заполнение списка рандомными вещественными числами числами в заданном пользователем диапазоне значений.
    Колличество знаков после запятой выбирается рандомно в заданном пользователем диапазоне
    '''
    for i in range(int(input('Введите чило: '))):
        num_list.append(round(random.uniform(1, 9), random.randint(1, 5)))
    return num_list


numbers = fill_list()
print(numbers)


def find_numbers_after_point(float_nums_list: List[float]) -> List:
    '''
    Возвращает список, состоящий из чисел после запятой  из элементов исходного списка

    Args:
      List[float] - Список вещественных числел
    Reterns:
      List[int] - Cписок целых числел
    '''
    fractional_part = []
    for item in float_nums_list:
        fractional_part.append(round(float(item)-int(item), 5))
    return fractional_part


fractional_part_list = find_numbers_after_point(numbers)
difference = round(max(fractional_part_list)-min(fractional_part_list), 5)
print( f"Разницу между максимальным и минимальным значением дробной части элементов равна {difference} или {str(difference).split('.')[1]}")
