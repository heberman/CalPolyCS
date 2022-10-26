import time
import random

def tic_tac_toe():
    first = ''
    a = input("Welcome to Tic-Tac-Toe!")
    a = input("Let's see who goes first...")
    print("Flipping coin...", end='')
    x = random.randint(0, 1)
    time.sleep(1)
    if x == 0:
        first = 'X'
    else:
        first = 'O'
    print(first, "goes first!")
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def display_board(board):
    for row in board:
        print('\n')
