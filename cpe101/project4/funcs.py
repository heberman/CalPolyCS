def display_puzzle(puzzle):
    print("Puzzle:\n")
    new_puzzle = ""
    for i in range(len(puzzle)):
        new_puzzle += puzzle[i]
        if (i + 1) % 10 == 0:
            new_puzzle += "\n"
    print(new_puzzle)

def check_forward(puzzle, word):
    for i in range(10):
        row = ""
        for j in range(10):
            row += puzzle[(i * 10) + j]
        found = row.find(word)
        if found != -1:
            return (i, found)
    return None

def check_backward(puzzle, word):
    for i in range(10):
        row = ""
        for j in range(10):
            row += puzzle[(i * 10) + j]
        backwards_row = ""
        for k in range(9, -1, -1):
            backwards_row += row[k]
        found = backwards_row.find(word)
        if found != -1:
            return (i, 9 - found)
    return None

def check_down(puzzle, word):
    new_puzzle = ""
    for i in range(10):
        for j in range(10):
            new_puzzle += puzzle[(j * 10) + i]
    result =  check_forward(new_puzzle, word)
    if result == None:
        return None
    else:
        return (result[1] , result[0])

def check_up(puzzle, word):
    new_puzzle = ""
    for i in range(10):
        for j in range(9, -1, -1):
            new_puzzle += puzzle[(j * 10) + i]
    result = check_forward(new_puzzle, word)
    if result == None:
        return None
    else:
        return (9 - result[1], result[0])

def check_diagonal(puzzle, word):
    diagonals = []
    for i in range(10):
        new_diagonal = ""
        for j in range(10):
            if j + i > 9:
                new_diagonal += puzzle[j * 10 + (j + i - 10)]
            else:
                new_diagonal += puzzle[j * 11 + i]
        diagonals.append(new_diagonal)

    for diagonal in diagonals:
        result = diagonal.find(word)
        if result != -1:
            if diagonals.index(diagonal) + result < 10:
                return (result, diagonals.index(diagonal) + result)
            else:
                if (10 - (diagonals.index(diagonal) + result) >= 0):
                    return (result, 10 - (diagonals.index(diagonal) + result))
                else:
                    return (result, -10 + (diagonals.index(diagonal) + result))
    return None

def find_word(puzzle, word):
    forward_result = check_forward(puzzle, word)
    backward_result = check_backward(puzzle, word)
    down_result = check_down(puzzle, word)
    up_result = check_up(puzzle, word)
    diagonal_result = check_diagonal(puzzle, word)
    if forward_result != None:
        return word + ": (FORWARD) row: " + str(forward_result[0]) + " column: " + str(forward_result[1])
    elif backward_result != None:
        return word + ": (BACKWARD) row: " + str(backward_result[0]) + " column: " + str(backward_result[1])
    elif down_result != None:
        return word + ": (DOWN) row: " + str(down_result[0]) + " column: " +  str(down_result[1])
    elif up_result != None:
        return word + ": (UP) row: " + str(up_result[0]) + " column: " + str(up_result[1])
    elif diagonal_result != None:
        return word + ": (DIAGONAL) row: " + str(diagonal_result[0]) + " column: " + str(diagonal_result[1])
    else:
        return word + ": word not found"