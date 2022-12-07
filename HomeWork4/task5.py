# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся
# в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

user_str = str(
    'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')


def write_to_file(my_str: str):
    with open('task_5.txt', 'w') as file:
        file.write(my_str)
    return my_str


# write_to_file(user_str)
print(f'Текст до сжатия {write_to_file(user_str)}')

def modify_to_RLE() -> str:
    """
        Функция кодирeт длины серий (RLE)
        Args:
            str - строка пользователя
        Returns:
            str - сжатый текст
    """

    with open('task_5.txt', 'r') as file:
        source_text = file.read()
    index = 0
    count = 1
    compr_text = ''
    source_text += ' '
    while index < len(source_text)-1:

        if source_text[index] == source_text[index + 1]:
            count += 1
        elif source_text[index] != source_text[index + 1]:
            if count == 1:
                compr_text += source_text[index]
            else:
                compr_text += str(count) + source_text[index]
            count = 1
        index += 1

    with open('task_5_compr.txt', 'w') as file:
        file.write(compr_text)
    return compr_text

print(f'Текст после сжатия {modify_to_RLE()}')

def recompression_RLE() -> str:
    """
        Функция осуществляет распаковку сжатого текста
        Returns:
            text : str - распакованный текст
    """
    with open('task_5_compr.txt', 'r') as file:
        text_from_file = file.read()
    index = 0
    count = ''
    compr_text = ''
    while index < len(text_from_file):
        if text_from_file[index].isdigit():
            count += text_from_file[index]
        elif count == '':
            compr_text += text_from_file[index]
        else:
            compr_text += text_from_file[index] * int(count)
            count = ''
        index += 1
    return compr_text


print(f'Текст после распаковки {recompression_RLE()}')
