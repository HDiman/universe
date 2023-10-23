import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_selection():
    selection = random.randint(0, len(Action) - 1)
    return Action(selection)


def determine_winner(one_action, other_action, num):
    if one_action == other_action:
        num += 0
        print(f"Силы равны. Никто не победил! Планет: {num}")
        return num

    elif one_action == Action.Rock:
        if other_action == Action.Scissors:
            num += 1
            print(f"Победа! Планета захвачена! Планет: {num}")
            return num
        else:
            num -= 1
            print(f"Неудача! Ваша планета захвачена! Планет: {num}")
            return num
    elif one_action == Action.Paper:
        if other_action == Action.Rock:
            num += 1
            print(f"Победа! Планета захвачена! Планет: {num}")
            return num
        else:
            num -= 1
            print(f"Неудача! Ваша планета захвачена! Планет: {num}")
            return num
    elif one_action == Action.Scissors:
        if other_action == Action.Paper:
            num += 1
            print(f"Победа! Планета захвачена! Планет: {num}")
            return num
        else:
            num -= 1
            print(f"Неудача! Ваша планета захвачена! Планет: {num}")
            return num

num = 0
for i in range(100000):
    user_action = get_selection()
    computer_action = get_selection()
    num = determine_winner(user_action, computer_action, num)
    if num == 100:
        print(f"{i} бой: Новая Галактика захвачена! 100 новых планет наши!")
        break
    elif num == -100:
        print(f"{i} бой: Наша Галактика захвачена! 100 наших планет захвачены!")
        break


