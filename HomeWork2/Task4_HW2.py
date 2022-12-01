# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку,
# а сам выбывает из круга. Процесс продолжается с места остановки аналогичным образом до последнего
# человека в круге. Составьте алгоритм, который проводит эту игру. Если хотите делать паузы,
# то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.
count = int(input('Введите количество игроков: '))
people = []
money = []
for i in range(count):
    people.append(i)
    money.append(0)
print(people)
print(money)
search_num = int(input('Введите количество игроков, посчитанных ведущим: '))
if search_num <= 0 or search_num >= count:
    print(
        f'Количество игроков, посчитаннх ведущим должно быть от 1 до {count}')


def searching_number(my_list, list2, num, count):
    people_after_game = []
    money_after_game = []

    for i in range(count):

        if i < num-1:
            list2[i] += 1
        elif i == num-1:  # or i == ((num-1) % i):
            list2[i+1] += list2[i] + 1
            print(f'Выбывает {my_list[i]}')
        else:
            list2[i] += 2

    people_after_game = my_list[num:] + my_list[:(num-1)]
    money_after_game = list2[num:] + list2[:(num-1)]
    return (people_after_game, money_after_game)


while len(people) >= 1:
    if search_num < len(people) and search_num > 2:
        people, money = searching_number(people, money, search_num, count)
        print(f'Остается игроков {people}')
        print(f'Монет у оставшихся {money}')
    else:
        search_num -= 1
        if search_num == 1:
            people, money = searching_number(people, money, search_num, count)
            print('******************')
            print(f'Выгрывает игрок {people} с количеством монет {money}')
            print('_____________________')
            break

        print('___________________')
        print(f'Теперь ведущий считает до {search_num}')
        people, money = searching_number(people, money, search_num, count)
        print(f'Остается игроков {people}')
        print(f'Монет у оставшихся {money}')

    count -= 1
