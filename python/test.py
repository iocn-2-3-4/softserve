#!/usr/bin/python

import random

#initializing board
board = []

order = int(raw_input("Enter order: "))

for x in range(order):
    board.append(["O"] * order)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return random.randint(1, len(board))

def random_col(board):
    return random.randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)


#your shoot
for turn in range(4):
    fire_row = int(raw_input("Fire row:"))
    fire_col = int(raw_input("Fire col:"))

    # if right, game ends
    if fire_row == ship_row and fire_col == ship_col:
        print "Congratulations! "
        break
    else:
        #warning if the guess is out of the board
        if (fire_row < 0 or fire_row > 4) or (fire_col < 0 or fire_col > 4):
            print "Out of the board!"
        
        #warning if the guess was already made
        elif(board[fire_row][fire_col] == "X"):
            print "You guessed that one already."
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print "You missed my battleship!"
            board[fire_row][fire_col] = "X"
        
        # Print turn and board again here
        print "Turn " + str(turn+1) + " out of 4." 
        print_board(board)

#if the user have made 4 tries, it's game over
if turn >= 3:
    print "Game Over"
