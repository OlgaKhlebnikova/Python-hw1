# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
from functions import fill_list, List
# num = int(input('Введите чило: '))
numbers = fill_list()

def summing_odd_list_items (nums_list: List[int]) -> List:

  '''
  Возвращает список, состоящий из сумм нечетных элементов исходного списка
  
  Args:
    List[int] - Список числел
  Reterns:
    List[int] - Cписок сумм числел
  '''

  sum = 0

  for i in range(1, len(numbers), 2):
      sum += numbers[i]
  return sum

result = summing_odd_list_items(numbers)

print(f'Список элементов {numbers}')
print(f'Сумма нечетных элементов списка равна {result}')
