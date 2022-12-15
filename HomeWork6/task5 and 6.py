# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]
# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]
import random
numbers = [random.randint(1, 100) for _ in range(20)]
tuple_numbers = list(filter(lambda x: x[0] != x[1], enumerate(numbers)))
print(f'Cписок без совпадений -> {tuple_numbers}')
print(f'Cписок удаленных -> {list(filter(lambda x: x[0] == x[1], enumerate(numbers)))}')
new_list = list(filter(lambda x: (x[0]+x[1])%5==0, tuple_numbers))
# delete_list = list(filter(lambda x: (x[0]+x[1])%5!=0, tuple_numbers))
print (f' Список  кортежей,  где сумма кортежа кратна 5 {new_list}')
# print (f'Список проверки {delete_list}')