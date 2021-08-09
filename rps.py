# rock paper scissors
from random import randint

while True:

    choices = ['r', 'p', 's']

    player_move = input('r, p or s?: ')
    if player_move not in choices:
        if player_move == 'q':
            break
        print('invalid choice!')   
        continue

    choices.remove(player_move)

    rand = randint(0,1)
    computer_move = choices[rand]

    if player_move == 'r':
        if computer_move =='s':
            print(f"computer move is {computer_move}, you win!")
        else:
            print(f"computer move is {computer_move}, you lose!")

    elif player_move == 'p':
        if computer_move == 'r':
            print(f"computer move is {computer_move}, you win!")
        else:
            print(f"computer move is {computer_move}, you lose!")

    else:
        if computer_move == 'p':
            print(f"computer move is {computer_move}, you win!")
        else:
            print(f"computer move is {computer_move}, you lose!")







