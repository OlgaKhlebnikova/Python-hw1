# В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5 -> АНГЕЛА МЕРКЕЛЬ 5
# Энакин Скайуокер 5 -> ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3 -> Фредди Меркури 3
# Александр Пушкин 4 -> Александр Пушкин 4
  #     print(line)

my_str = str('Ангела Меркель 5, Энакин Скайуокер 5, Фредди Меркури 3, Александр Пушкин 4')
#my_str = input('Введите ФИ студента средний бал и через запятую всю группу: ')
stduents_list = list(my_str.split(", "))
print(stduents_list)

def write_to_file(stduents_list: list[str]):
    with open('file1.txt','w', encoding = 'utf-8') as file:
        for item in stduents_list:
            file.write(item +'\n')


def rewrite_students_list():
    
    with open('file1.txt', 'r', encoding = 'utf-8') as file1, open('file2.txt', 'w', encoding = 'utf-8') as text2:
        lines = file1.readlines()
        char = '5'
        for line in lines:
            if char in line:
                new_write = line.replace(line, line.upper())
                text2.write(new_write)
            else:
                text2.write(line)
write_to_file(stduents_list)
rewrite_students_list()