# 1. Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
#
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок
#
def search_substr(input_text: str, substr: str)->str:
    """
       Функция фильтрует слова в строке по наличию в них указанного элемента
       Args:
           input_text: str
           substr: str
       Returns:
           new_text - обновленная строка
    """
    input_text = list(input_text.split())
    new_text = []
    for item in input_text:
        if substr in item:
            pass
        else:
            new_text.append(item)
    return new_text
user_str = 'В двери Новый год стучится, Дед Мороз к нам в гости мчится.'
serch_str = 'го'
new_str = search_substr(user_str, serch_str)

print (' '.join(new_str))