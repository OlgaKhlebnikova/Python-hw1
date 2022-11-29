# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

print ('Вариант 1')
number = input('Введите число ')
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print (f'Сумма чисел {number} равна {sum}')

print()

print ('Вариант 2')
user_input = input('Введите число : ')
try:
    sum = 0
    for element in user_input:
        if element != '.' and element != '-':
            sum += int(element)
    print(f'Сумма чисел {user_input} равна {sum}')
except ValueError:
    print('Введенное значение не является числом')
