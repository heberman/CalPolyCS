# Project 3 - Calcudoku
#
# Name: Henry Berman
# Instructor: Hatalsky

from solverFuncs import *

def main():
    cages = get_cages()
    puzzle = []
    for i in range(5):
        puzzle.append([0,0,0,0,0])
    x = 0
    backtrack_val = 0
    checks = 0
    backtracks = 0
    while x < 25:
        row = x // 5
        column = x % 5
        for i in range(backtrack_val + 1, 6):
            checks += 1
            puzzle[row][column] = i
            if check_valid(puzzle, cages):
                x += 1
                backtrack_val = 0
                break
        else:
            while puzzle[row][column] == 5:
                puzzle[row][column] = 0
                x -= 1
                backtracks += 1
                if x < 0:
                    exit()
                row = x // 5
                column = x % 5
            backtrack_val = puzzle[row][column]
    print("\n---Solution---\n")
    for row in range(5):
        print(puzzle[row][0], puzzle[row][1], puzzle[row][2], puzzle[row][3], puzzle[row][4])
    print("\nchecks:", checks, "backtracks:", backtracks)

if __name__ == '__main__':
    main()