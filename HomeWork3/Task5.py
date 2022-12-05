# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
from typing import List
number = int(input('Введите число: '))


def get_fibonacci_list(num: int) -> List:
    '''
    Функция возвращает сформированный список чисел Фибоначчи.
    Args:
      int - Целое число
    Reterns:
      List[int] - Cписок чисел
    '''
    if num == 0:
        fibonacci_list = [0]
        return fibonacci_list
    fibonacci_list = [0, 1]
    for i in range(0,num -1 ):
        fib1 = fibonacci_list[i]
        fib2 = fibonacci_list[i+1]
        fib = fib1+fib2
        fibonacci_list.append(fib)
    return fibonacci_list


def get_negafibonacci_list(fibonacci_list) -> List:
       
    negafibonacci_list = []
    n = 0
    for i in fibonacci_list:
        negafib = ((-1)**(n+1))*i
        negafibonacci_list.append(negafib)
        n+=1
    negafibonacci_list.reverse()
    return negafibonacci_list

fibonacci = get_fibonacci_list(number)
nega_fib = get_negafibonacci_list(fibonacci)

print (nega_fib[:-1] + fibonacci)
