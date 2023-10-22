import random

# randon choice
def choice():
    loc = ['stone', 'scissors', 'paper']
    num = random.randint(0, 2)
    return loc[num]


print(choice())
