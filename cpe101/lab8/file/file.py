def main():
    f = open("in.txt", "r")
    i = 0
    for line in f:
        print("Line", i, "(" + str(len(line)), "chars): " + line, end='')
        i += 1

if __name__ == '__main__':
    main()