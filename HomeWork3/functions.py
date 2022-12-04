import random
# number = int(input('Введите чило: '))
from typing import List

def fill_list(num_list = []):
    ''' Заполнение списка рандомными числами в заданном пользователем диапазоне значений'''
    for i in range(int(input('Введите чило: '))):
        num_list.append(random.randint(1,10))
    return num_list

# numbers = fill_list()
# print(numbers)

