import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_selection():
    selection = random.randint(0, len(Action) - 1)
    return Action(selection)


def determine_winner(one_action, other_action):
    if one_action == other_action:
        print(f"Силы равны. Никто не победил!")
    elif one_action == Action.Rock:
        if other_action == Action.Scissors:
            print("Победа! Планета захвачена!")
        else:
            print("Неудача! Ваша планета захвачена!")
    elif one_action == Action.Paper:
        if other_action == Action.Rock:
            print("Победа! Планета захвачена!")
        else:
            print("Неудача! Ваша планета захвачена!")
    elif one_action == Action.Scissors:
        if other_action == Action.Paper:
            print("Победа! Планета захвачена!")
        else:
            print("Неудача! Ваша планета захвачена!")

for i in range(10):
    user_action = get_selection()
    computer_action = get_selection()
    determine_winner(user_action, computer_action)



