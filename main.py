import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


# randon choice
def choice():
    possible_actions = ['rock', 'scissors', 'paper']
    computer_action = random.choice(possible_actions)
    return computer_action

def who_wins(a, b):
    if a == b:
        return 'draw'
    elif


for i in range(100):
    print(i+1)


