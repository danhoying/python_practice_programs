# BINGO
# Displays a bingo board to the player and allows him to input numbers onto the board
# *(Not finished yet)*

import random


def displayBoard():
    board = ['_'] * 100
    print(' '.join(board[1:11]))
    print(' '.join(board[11:21]))
    print(' '.join(board[21:31]))
    print(' '.join(board[31:41]))
    print(' '.join(board[41:51]))
    print(' '.join(board[51:61]))
    print(' '.join(board[61:71]))
    print(' '.join(board[71:81]))
    print(' '.join(board[81:91]))
    print(' '.join(board[91:101]))
    return board
    
def starterTen():
    numbers = list(range(1,101))
    random.shuffle(numbers)
    return(numbers[:10])
    
def addStarters(board, starters):
    for i in starters:
        board[i] = i + 1
    return board

def addNumber(starter_board):
    try:
        number = int(input('Pick a number: '))
    except ValueError:
        print('Try again.')
    else:
        if 0 < number < 101:
            starter_board[number - 1] = number
            print(starter_board)
        else:
            print('Try again.')
    
    return starter_board
    
board = displayBoard()
starters = starterTen()
starter_board = addStarters(board, starters)
while True:
    addNumber(starter_board)






    


