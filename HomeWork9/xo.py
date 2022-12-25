from tic_tac_toe_miked import ttt
from colorama import Fore, Back, Style
game = input(Fore.MAGENTA + Style.BRIGHT + "Привет!\nСыгрем в крестики-нолики\nНажми 'Д' or 'Y' если согласен, иначе просто нажми <Enter>: "+ Style.RESET_ALL)

if game.lower() == 'д' or game.lower() == 'y':
    ttt.play()
# print('Игра окончена. Хорошего дня.')
print(Fore.GREEN + Style.BRIGHT + '\n''Игра окончена. Хорошего дня.' + Style.RESET_ALL)