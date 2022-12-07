# В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5 -> АНГЕЛА МЕРКЕЛЬ 5
# Энакин Скайуокер 5 -> ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3 -> Фредди Меркури 3
# Александр Пушкин 4 -> Александр Пушкин 4
#     print(line)

my_str = str(
    'Ангела Меркель 5, Энакин Скайуокер 5, Фредди Меркури 3, Александр Пушкин 4')
#my_str = input('Введите ФИ студента средний бал и через запятую всю группу: ')
my_stduents_list = list(my_str.split(", "))
print(my_stduents_list)


def write_to_file(stduents_list: list[str]):
    with open('report.txt', 'w', encoding='utf-8') as file_task3:
        for item in stduents_list:
            data = file_task3.write(item + '\n')
    return data

# Если создать новый файл
# def rewrite_students_list():

#     with open('report.txt', 'r', encoding = 'utf-8') as file_task3, open('file2.txt', 'w', encoding = 'utf-8') as text2:
#         lines = file_task3.readlines()
#         char = '5'
#         for line in lines:
#             if char in line:
#                 new_write = line.replace(line, line.upper())
#                 text2.write(new_write)
#             else:
#                 text2.write(line)
# write_to_file(stduents_list)
# rewrite_students_list()

# или если преезаписать файл
  

def find_el(my_list:list[str]):
  write_to_file(my_list)
  # rewrite_students_list()
  # find_el(my_stduents_list):
  for el in range(len(my_list)):
    if '5' in my_stduents_list[el]:
      my_list[el] = my_list[el].replace(my_list[el],my_list[el].upper())
  # print(my_list)
  return my_list
new_st_list = find_el(my_stduents_list)
print(new_st_list)
write_to_file(new_st_list)