# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# import random
from functions import give_num,List
my_list = list(map(lambda i: ((-3)**i), [i for i in range(give_num('Введите число: '))]))
print(f'Список элементов последовательности {my_list}')