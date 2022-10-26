def get_cages():
    num = int(input("Number of cages: "))
    cage_list = []
    for i in range(num):
        cage = input("Cage number " + str(i) + ": ").split()
        for j in range(len(cage)):
            cage[j] = int(cage[j])
        #cage = list(map(int, input("Cage number " + str(i) + ": ").split()))
        print(cage)
        if int(cage[1]) == (len(cage) - 2):
            cage_list.append(cage)
        else:
            break
    return cage_list

def check_rows_valid(puzzle):
    for row in puzzle:
        for x in range(len(row)):
            for i in range(1, 5 - x):
                if row[x] == row[x + i] and row[x] != 0:
                    return False

    return True

def check_columns_valid(puzzle):
    for a in range(5):
        column = []
        for row in puzzle:
            column.append(row[a])
        for x in range(5):
            for i in range(1, 5 - x):
                if column[x] == column[x + i] and column[x] != 0:
                    return False
    return True


def check_cages_valid(puzzle, cages):
    for cage in cages:
        incomplete = False
        sum = 0
        end_sum = cage[0]
        num_cells = cage[1]
        for i in range(2, num_cells + 2):
            row = puzzle[cage[i] // 5]
            val = row[cage[i] % 5]
            if val == 0:
                incomplete = True
            sum += val
        if (not incomplete and sum != end_sum) or (incomplete and sum >= end_sum):
            return False
    return True

def check_valid(puzzle, cages):
    return check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle, cages)