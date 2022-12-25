import random

# number = int(input('Введите чило: '))
from typing import List, Optional

def fill_list(num_list = []):
    ''' Заполнение списка рандомными числами в заданном пользователем диапазоне значений'''
    for i in range(int(input('Введите чило: '))):
        num_list.append(random.randint(1,10))
    return num_list

# numbers = fill_list()
# print(numbers)

def give_num(input_string: str,
             min_num: Optional[int] = None,
             max_num: Optional[int] = None) -> int:
    """
    Выпытывает у пользователя число

    Args:
        input_string - предложение ввода
    Returns:
        int - число
    """    
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите больше, чем {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')