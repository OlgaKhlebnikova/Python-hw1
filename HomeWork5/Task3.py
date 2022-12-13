import random
import sys
import time
print('Будем играть в Крестики-Нолики')
player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
time.sleep(1)


def zero_win():
    if (area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0') or \
        (area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0') or \
        (area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0') or \
        (area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0') or \
        (area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0') or \
        (area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0') or \
        (area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0') or \
            (area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0'):
        str2 = 'Победил Второй игрок. Поздравляю'
    return str2


def cross_win():
    if (area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X') or \
        (area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X') or \
        (area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X') or \
        (area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X') or \
        (area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X') or \
        (area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X') or \
        (area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X') or \
            (area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X'):
        str1 = 'Победил Первый игрок. Поздравляю'
    return str1


def choose_player():
    '''
        Функция рандомно выбирает игрока для первого хода.

        Returns:
        motion: int - номер игрока
    '''

    motion = random.randrange(1, 3)
    return motion


first_player_in_game = choose_player()

if first_player_in_game == 1:
    print(f' {player_1}, тебе повезло - ты первый игрок.')
else:
    print(f'{player_2}, тебе повезло - ты первый игрок.')
print('\nНачинаем.\n')
time.sleep(1)


def game_cross_zero():
    area = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*']
    ]

    count = 0
    while True:
        # count += 1
        fir1, fir2 = map(int, input('Первый игрок. Напиши номер строки и столбца через пробел (1-3),'
                                    'где хочешь поставить "X"(Счёт идёт с левого верхнего угла):').split())
        fir1 = int(fir1 - 1)
        fir2 = int(fir2 - 1)

        # if count < 8:
        print(count)
        if fir1 in [0, 1, 2] and fir2 in [0, 1, 2] and area[fir1][fir2] != "X" and area[fir1][fir2] != "0":
            area[fir1][fir2] = "X"
            for item in area:
                print(f'{item}\n')

        else:
            print('Вы ввели неверные значения, попробуйте заново')
            continue
        if (area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X') or \
                (area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X') or \
                (area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X') or \
                (area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X') or \
                (area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X') or \
                (area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X') or \
                (area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X') or \
                (area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X'):
            str1 = 'Победил Первый игрок. Поздравляю'

            return str1
            break

        count += 1

        sec1, sec2 = map(int, input('Второй игрок. Напиши номер строки и столбца через пробел (1-3),'
                                        'где хочешь поставить "0"(Счёт идёт с левого верхнего угла):').split())
        sec1 = int(sec1 - 1)
        sec2 = int(sec2 - 1)
        print(count)
        if sec1 in [0, 1, 2] and sec2 in [0, 1, 2] and area[sec1][sec2] != "X" and area[sec1][sec2] != "0":
            area[sec1][sec2] = "0"
            for item in area:
                print(f'{item}\n')

        elif (area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0') or \
                (area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0') or \
                (area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0') or \
                (area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0') or \
                (area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0') or \
                (area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0') or \
                (area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0') or \
                (area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0'):
            str2 = 'Победил Второй игрок. Поздравляю'

            return str2
            break
        count += 1
        if count == 8:
            print(f'Ничья\n')
            # break


print(game_cross_zero())
