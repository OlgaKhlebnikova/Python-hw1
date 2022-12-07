# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево
# или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" -
# сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает
# ключ, считывает текст и дешифровывает его.

def cipher_cesarius_input(shift_step = int(input("Введите ключ шифрования от 1 до 35: ")), str1 = (input("Введите текст для шифрования на русском языке: "))) -> str:
    """
    Функция зашифровывает текст с выбранным сдвигом

        Args:
        shift_step: int - количество элементов для сдвига

        Returns:
        cifr_text: str - зашифрованный текст
    """
        alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.:')
        str1 = str1.lower()
        cifr_text = ''
        for i in str1:
            position = alphabet.index(i)
            new_position = position + shift_step
            if i in alphabet:
                cifr_text += alphabet[new_position]
            else:
                print("Вы ввели недопустимое значение, попробуйте еще раз")
                break

        with open ('file_code.txt', 'w') as file:
            file.write(cifr_text)
        return cifr_text


print(f'Ваш зашифрованный текст: {cipher_cesarius_input()}')
tex = cipher_cesarius_input()

def transcrypt_cipher_cesarius(key = int(input("Введите ключ для дешифровки: "))) ->str:
    """
        Расшифровывает текст

        Args:
            key: int - ключ для разгадки шифра

        Returns:
            dechif_text: str - расшифрованный текст
    """
    with open('file_code.txt', 'r') as file:
        chif_text = file.read()

    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.:')
    dechif_text = ''
    for i in chif_text:
        position = alphabet.index(i)
        new_position = position + key
        if i in alphabet:
            dechif_text += alphabet[new_position]
    with open('file_encode.txt', 'a') as file:
        file.write(f'{dechif_text} \n')
    return dechif_text


 print(f'ваш зашифрованный текст: {transcrypt_cipher_cesarius()}')
