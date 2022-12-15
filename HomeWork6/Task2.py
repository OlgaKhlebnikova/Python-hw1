# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
import math
import random
from functions import fill_list,List,Optional
numbers = fill_list()
print (numbers)
# numbers = list(map(int,input('Введите список чисел через пробел ').split()))
mult_el_in_list = [numbers[i]*numbers[-(i+1)] for i in range(math.ceil(len(numbers)/2))]
print(mult_el_in_list)