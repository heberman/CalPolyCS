def sum(a):
    sum = 0
    for val in a:
        sum += val
    return sum

def index_of_smallest(a):
    if len(a) <= 0:
        return -1
    min = a[0]
    min_index = 0
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
            min_index = i
    return min_index
