import random
from enum import IntEnum
from time import sleep


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_selection():
    selection = random.randint(0, len(Action) - 1)
    return Action(selection)


def determine_winner(one_action, other_action, num):
    if one_action == other_action:
        num += 1
        print(f"Силы равны. Никто не победил! Планет: {num}")
        return num, 0

    elif one_action == Action.Rock:
        if other_action == Action.Scissors:
            num += 1
            print(f"Победа! Планета захвачена! Планет: {num}")
            return num, 1
        else:
            num -= 1
            print(f"Неудача! Ваша планета захвачена! Планет: {num}")
            return num, -1
    elif one_action == Action.Paper:
        if other_action == Action.Rock:
            num += 1
            print(f"Победа! Планета захвачена! Планет: {num}")
            return num, 1
        else:
            num -= 1
            print(f"Неудача! Ваша планета захвачена! Планет: {num}")
            return num, -1
    elif one_action == Action.Scissors:
        if other_action == Action.Paper:
            num += 1
            print(f"Победа! Планета захвачена! Планет: {num}")
            return num, 1
        else:
            num -= 1
            print(f"Неудача! Ваша планета захвачена! Планет: {num}")
            return num, -1

i = 0
num = 0
planets = 0

while True:
    i += 1
    user_action = get_selection()
    computer_action = get_selection()
    num, win_loose = determine_winner(user_action, computer_action, num)

    if num > 99 and win_loose == -1:
        num += 1

    if num == 100 or num == 200 or num == 300 or num == 400 or num == 500 \
            or num == 600 or num == 700 or num == 800 or num == 900:
        print(f"{i} бой: Новая Галактика захвачена! {num} новых планет наши!")
        sleep(5)
        planets = num
    elif num == 1000:
        print(f"{i} бой: Захвачено 10 галактик! 1000 новых планет наши!")
        break
    elif num == -100:
        print(f"{i} бой: Нас победили! 100 наших планет захвачены!")
        break
    sleep(0.1)

