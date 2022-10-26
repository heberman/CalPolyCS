from funcs import *

def main():
    puzzle = input()
    words = input().split()
    display_puzzle(puzzle)
    for word in words:
        print(find_word(puzzle, word))

if __name__ == '__main__':
   main()