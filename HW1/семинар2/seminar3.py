# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3
# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# num = int(input('Введите искомое число'))
# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# def find_element(my_list,num):
#     count = 0
#     switch = True
#     for item in my_list:
#         if item.find('32')!=1:
#             print (f'32 содержится с индексом {count}')
#         switch = False
#     count+=1    
#     if switch:
#         print ('Элементов не найдено')

new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find = 'qwe'
def func(new_list, find):
    count = 0
    n = -1
    for i in range(0, len(new_list)):
        a = new_list[i] == find
        if a:
            count+=1
        if count == 2:
            return i
    return n
print(func(new_list, find))


def find_element(my_list, num):
    count = 0
    switch = True

    for i in my_list:
        if i.find(num)!= -1:
            print(f'{num}  содержится в элементе с индексом {count}')
            switch = False
        count+=1    
    if switch:
        print('элементов не найдено')


my_list = ['gfh5', 'gfh2', '67', 'jy32', '3put', '56u32']
num = input('введите искомый элемент: ')
find_element(my_list, num)
