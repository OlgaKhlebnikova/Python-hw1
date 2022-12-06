# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from typing import List
number = int(input('Введите число, которое нужно разделить на простые множители: '))

def get_multipliers(num: int) -> List:
  '''
  Функция возвращает сформированный список простых множителей.
  Args:
  int - Целое число
  Reterns:
  List[int] - Cписок чисел
  '''

  multipliers = []
  divider = 2
  while (divider <= num):
    if (num % divider) == 0:
      multipliers.append(divider)
      num = num/divider
    else:
      divider += 1
      
  return list(set(multipliers))

mult_list = get_multipliers(number)
# или можно так
# for el in mult_list: 
#   if mult_list.count(el) > 1:
#     mult_list.remove(el)

print(f'Список простых множителей числа {number} -> {mult_list}')

