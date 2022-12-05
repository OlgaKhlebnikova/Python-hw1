# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
from typing import List

def convert_in_binary(num: int)-> List:
    '''
    Функция возвращает сформированный рекурсивным образом список.
    Args:
      int - Целое число
    Reterns:
      List[int] - Cписок разрядов двоичного числа (0,1)
    '''
    if (num == 0):
      binary_list.reverse()
      return binary_list
    # bin_num = num % 2
    binary_list.append(num % 2)
    convert_in_binary(num // 2)

number = int(input('Введите число, которое нужно преобразовать: '))
binary_list = [] 
convert_in_binary(number)
binary_list.reverse()   
# print (binary_list) 
print(f'Число {number} в двоичной системе -> ' + "".join(map(str, binary_list)))
