def check_for_wins(board):
    winning_conditions = [
        any(line == ['X'] * 3 or line == ['0'] * 3 for line in board),
        any(board[0][i] == board[1][i] == board[2][i] for i in range(0,3)),
        board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]
    ]
    if any(winning_conditions):
        return True

def position_taken(val):
    if val in ['X', '0']:
        print('Position already taken! Try another.')
        return True

def change_board(i, symbol):
    if i in range(1, 4):
        if position_taken(board[0][i-1]): return
        board[0][i-1] = symbol
    elif i in range(4, 7):
        if position_taken(board[1][i-4]): return
        board[1][i-4] = symbol
    elif i in range (7, 10):
        if position_taken(board[2][i-7]): return
        board[2][i-7] = symbol
    return board

def all_X0(board):
    positions_taken = []
    for i in board:
        for j in i:
            if j == '0' or j == 'X':
                positions_taken.append(True)
    if len(positions_taken) == 9:
        return True

def print_board(board):
    for i in board:
        print('\n', end='')
        for j in i:
            print(j, end='')
    print('\n')
            
board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

turn = 'X'

while True:
    move = input(f'{turn} player move: ')
    if not move.isdigit() or int(move) not in range (1, 10):
        print('Error: Input a number between 1 and 9!')
        continue
    if not change_board(int(move), turn):
        continue
    print_board(board)
    if check_for_wins(board):
        print(f'{turn} player wins!')
        break
    elif all_X0(board):
        print('Tie!')
        break
    else:
        turn = '0' if turn == 'X' else 'X'
        






