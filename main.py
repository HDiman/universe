import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    return Action(selection)


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action.name}. Ничья!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")

for i in range(10):
    user_action = get_computer_selection()
    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)



