# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
from typing import List
int_list = list(map(int, input('Введите числа через пробел: ').split()))
# int_list = [1,1,1,1,2,2,2,3,3,3,4,4,4]
print (int_list)
# Способ 1
int_list2 = list(dict.fromkeys(int_list))
print (f'Способ №1 через ключи словаря {int_list2}')
# Способ 2
def delete_repeats(my_list: List[int])-> List[int]:
  '''
  Функция возвращает сформированный список без повторов.
  Args:
  list [int] - Список целых чисел
  Reterns:
  List[int] - Cписок целых чисел без повторов
  '''
  list_1 = []   
  for el in my_list: 
    if el not in list_1:
      list_1.append(el)
  return list_1
new_list = delete_repeats(int_list)
print(f'Способ №2 через новый список1 {new_list}')