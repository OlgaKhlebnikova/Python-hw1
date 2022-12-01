# # #. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# #     *Пример:*5
# #     - Для N = 5: 1, -3, 9, -27, 81

# num = 1
# for _ int range(int(input('Введите число '))):
#     print(num, end=' ')
#     num *= -3

# # num = int(input ('Введите число '))
# #   for i in range(int(input())):
# #     print((-3)**i, end = ' ')

#2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# # натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#        *Пример:*
#         - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input('Введите число '))
# my_dict = {}
# for i in range(1, number+1):
#     my_dict[i] = 3*i + 1
# print(my_dict)

#Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой.
str1, str2 = input ('первая строка: ') , input ('вторая строка: ')
count = 0
str1 = str1.split()
for i in str1:
    if i == str2:
        count +=1
print (count)


float_num = float(input('Введите вещественное число: '))
float_num = abs(float_num)  # убирается минус
while float_num != int(float_num):
    float_num = round(float_num*10, 10)
sum_digits = 0
while float_num > 0:
    sum_digits += float_num % 10
    float_num //= 10
print(sum_digits)


def give_int(input_string: str,
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
