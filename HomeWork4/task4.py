# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево
# или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" -
# сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает
# ключ, считывает текст и дешифровывает его.
#decript: bool = Folse
def cipher_cesarius(alphabet: str, text: str, key: int, decript:bool = False) -> str:
    """
    Функция зашифровывает текст с выбранным сдвигом.

        Args:
        alphabet - алфавит для шифрования
        text - строка для шифрования
        key - сдвиг элемента для шифрования

        Returns:
        cifr_text: str - зашифрованный текст
    """
    
    key = - key if decript else key
    cifr_text = ''
    alphabet_lenght = len(alphabet)
    for simbol in text:
        i = 0
        index = alphabet.find(simbol)
        for el in alphabet:
            # index = alphabet.find(simbol)
            if simbol == el:
                index = i + key
            i += 1
        if index > alphabet_lenght:
            index = (index+key) % alphabet_lenght
        
        cifr_text += alphabet[index]
    return cifr_text


# print(f'Ваш зашифрованный текст: {cipher_cesarius_input()}')
# tex=cipher_cesarius_input()

# def transcrypt_cipher_cesarius(key=int(input("Введите ключ для дешифровки: "))) -> str:
#     """
#         Расшифровывает текст

#         Args:
#             key: int - ключ для разгадки шифра

#         Returns:
#             dechif_text: str - расшифрованный текст
#     """
#     with open('file_code.txt', 'r') as file:
#         chif_text=file.read()

#     alphabet=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.:')
#     dechif_text=''
#     for i in chif_text:
#         position=alphabet.index(i)
#         new_position=position + key
#         if i in alphabet:
#             dechif_text += alphabet[new_position]
#     with open('file_encode.txt', 'a') as file:
#         file.write(f'{dechif_text} \n')
#     return dechif_text


#  print(f'ваш зашифрованный текст: {transcrypt_cipher_cesarius()}')
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.:;!*-/?&#№"`~'
int_text = 'Я решаяю эту задачу.'
key = 3

cifr_text1 = cipher_cesarius(alphabet, int_text, key)

file_task5 = open('ciper_ces.txt', 'w', encoding='utf-8')
file_task5.write(cifr_text1)
file_task5.close()


print(cifr_text1)
descript_file = cipher_cesarius(alphabet, cifr_text1, key, decript = True)
file_task5 = open('descript_ciper_ces.txt', 'w', encoding='utf-8')
file_task5.write(descript_file)
file_task5.close()
print(cipher_cesarius(alphabet, cifr_text1, key, decript = True))