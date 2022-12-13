


import random
from random import randint


import time
from typing import Optional
def give_num(input_string: str,
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




def choose_player_for_1_turn():
    '''
        Функция рандомно выбирает игрока для первого хода.
    
        Returns:
        motion: int - номер игрока
    '''

    motion = random.randrange(1,3)
    return motion



def game_with_player(candies:int, candy_for_turn:int):
    '''
    Принимает общее количество конфет и количество конфет в одни руки. Печатает имя победителя.
    Args:
    int(candies)
    int(candy_for_turt)
    '''
    print('Подождите. Выбирем первого играка.')
    time.sleep(2)
    first_player_in_game = choose_player_for_1_turn()
    print('\nНачинаем.\n')
    time.sleep(1)

    if first_player_in_game == 1:
        print (f' {player_1}, тебе повезло - ты первый игрок.  Помни, ты можешь взять не более {players_candy} конфет.')
    else:
        print (f'Игрок {player_2} играет первый. Помните, за 1 ход можно взять не более {players_candy} конфет.')
    # candy_for_turn
    while candies > 0:
       

        if candies <= candy_for_turn:
            candy_for_turn = candies

        if candies > candy_for_turn:
            print(f'Первый игрок, твой ход. Помни, можно брать не более {candy_for_turn} конфет.')
            time.sleep(1)
            first_player_in_game = give_num('Сколько конфет ты возьмешь в этом раунде?\n',1, candy_for_turn)
            candies -= first_player_in_game
            print(f'Осталось {candies} конфет. ')
            
            if candies > candy_for_turn:
                print(f'Второй игрок, твой ход. Помни. можно брать не более {candy_for_turn} конфет.')
                time.sleep(1)
                second_player_in_game = give_num('Сколько конфет ты возьмешь в этом раунде?\n',1, candy_for_turn)
                candies -= second_player_in_game
                print(f'Осталось {candies} конфет.')
                if candies < candy_for_turn:
                    if first_player_in_game == 1:
                        time.sleep(1)
                        print(f'Все конфеты забирает {player_1}. УРА!')
                        break
                    else:
                        time.sleep(1)
                        print(f'Все конфеты забирает {player_2}. УРА!')
                        break
        else:
            if first_player_in_game == 1:
                time.sleep(2)
                print(f'Все конфеты забирает {player_1}. УРА!')
                break
            else:
                time.sleep(2)
                print(f'Все конфеты забирает забирает {player_2}. УРА!')
                break

def bot_game_beginner(candies, candy_for_turn):
    if candies > candy_for_turn:
        bot = randint(1, candy_for_turn)
        print(f'Бот взял {bot} штук')
    else:
        bot = randint(1, candies)
        print(f'Бот взял {bot} штук')
    return bot

def bot_game_smart(first_player_in_game, candies, candy_for_turn):
    super_punch = candies - (int(candies / (candy_for_turn+1))*(candy_for_turn+1))
    print(super_punch)
    if candies > candy_for_turn:
        if first_player_in_game == 0:
            bot = super_punch
            print(f'Бот взял {bot} штук')
            return bot
        else:
            bot = candy_for_turn - first_player_in_game
            print(f'Бот взял {bot} штук')
        return bot

def game_with_bot(candies:int, candy_for_turn:int):
    '''
    Принимает общее количество конфет и количество конфет в одни руки. Печатает имя победителя.
    Args:
    int(candies)
    int(candy_for_turt)
    '''
    print('Подождите. Выбирем первого играка.')
    time.sleep(2)
    first_player_in_game = int(choose_player_for_1_turn())
    
    print('\nНачинаем.\n')
    time.sleep(1)
    if first_player_in_game == 1:
        print (f' {player_1}, тебе повезло - ты первый игрок.')
    else:
        print (f'Игрок {player_2} играет первый.')
    while candies > 0:
        if candies > candy_for_turn:
            if candies <= candy_for_turn:
                candy_for_turn = candies
            if first_player_in_game >= 0:
                if first_player_in_game == 1:
                    print(f'{player_1}, твой ход. Помни, можно брать не более {candy_for_turn} конфет.')
                    time.sleep(1)
                    player_in_game = give_num('Сколько конфет ты возьмешь в этом раунде?\n',1, candy_for_turn)
                    second_player_in_game = 0
                    
                else:
                    if  type_of_game == 2:
                        count = 0
                        if count == 0:
                            bot = super_punch
                            print(f'Бот взял {bot} штук')
                            count += 1
                        else:
                            bot = super_punch - player_in_game
                            print(f'Бот взял {bot} штук')
                        player_in_game = bot
                        second_player_in_game = 1
                    else:
                        bot = bot_game_beginner(candies,candy_for_turn) 
                        player_in_game = bot
                        second_player_in_game = 1
                
                candies -= player_in_game
                first_player_in_game = second_player_in_game
                print(f'Осталось {candies} конфет. ')
        
        else:
            if first_player_in_game == 1:
                time.sleep(2)
                print(f'Все конфеты не забирает {player_1}. УРА!')
                break
            else:
                time.sleep(2)
                print(f'Все конфеты теперь забирает забирает {player_2}. ')
                break      


player_1 = input('Введите имя первого игрока: ')
candies_in_game = give_num('Введите колличество конфет: ', 0, 2000)
players_candy = give_num('Введите колличество конфет, которые можно взять в одни руки за один ход: ',0, candies_in_game/2+1)
# if players_candy > candies_in_game/2:
#     print(f'Колличество конфет, которые можно взять в одни руки за один ход должно быть меньше чем {int(candies_in_game/2)} ')
    # players_candy = give_num('Введите колличество конфет, которые можно взять в одни руки за один ход: ')
super_punch = int(candies_in_game - (int(candies_in_game / (players_candy+1))*(players_candy+1)))
type_of_game = give_num('Выберите тип игры: 0 - с другом, 1 - с простым ботом, 2 - с умным ботом\n', 0, 2 )
if type_of_game == 0:
    player_2 = input('Введите имя второго игрока: ')
    game_with_player(candies_in_game,players_candy)
elif type_of_game == 1:
    player_2 = 'Бот-новичок'
    print(f'Итак {player_1} ты выбрал в соберники бота с именем {player_2}')
    game_with_bot(candies_in_game,players_candy)
else:
    player_2 = 'Умный Бот'
    print(f'Итак {player_1} ты выбрал в соберники бота с именем {player_2}')
    game_with_bot(candies_in_game,players_candy)
# time.sleep(1)


    



# game_with_player(candies_in_game,players_candy)


