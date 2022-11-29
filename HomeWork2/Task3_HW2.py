# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random
number = int(input('Введите число '))
my_list = []
for i in range(number):
    my_list.append(random.randint(-10, 10))
print(my_list)
for i in range(number+1):
    if my_list[i] < 0:
        my_list.insert(i+1, 0)
print(my_list)
