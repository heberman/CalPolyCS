"""Lab 6 Functions.
Course: CPE202
Quarter: Spring 2020
Authors: Henry Berman, Yale Hone, Panya Ou
"""

import random
import time


def insertion_sort(alist):
    """insertion sort by Henry Berman
        Args:
            alist (list): list of integers
        Returns:
            (int): returns number of comparisons made
        """
    comparisons = 0
    for i in range(1, len(alist)):
        j = i
        while j > 0 and alist[j - 1] > alist[j]:
            comparisons += 1
            alist[j - 1], alist[j] = alist[j], alist[j - 1]
            j -= 1
        comparisons += 1
    return comparisons


def merge_sort(alist):
    """merge sort by Henry Berman
    Args:
        alist (list): list of integers
    Returns:
        (int): returns number of comparisons made
    """
    return merge_sorter(alist)[1]


def merge_sorter(alist, comps=0):
    """merge sort helper by Henry Berman
    Args:
        alist (list): list of integers
        comps (int): number of comparisons
    Returns:
        (list, int): returns list and number of comparisons made
    """
    if len(alist) <= 1:
        return alist, comps
    mid = len(alist) // 2
    left, comps = merge_sorter(alist[:mid], comps)
    right, comps = merge_sorter(alist[mid:], comps)
    return merge(left, right, comps)


def merge(left, right, comps):
    """merge sort helper by Henry Berman
    Args:
        left (list): left side of list
        right (list): right side of list
        comps (int): number of comparisons
    Returns:
        (list, int): returns list and number of comparisons made
    """
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        comps += 1
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    comps += 1
    merged += left[left_idx:]
    merged += right[right_idx:]
    return merged, comps


QuickSort_comparisons = 0
alist = []


def BubbleSort(alist):
    """
    Author: Yale Hone
    """
    comparisons = 0
    size = len(alist)
    length = len(alist)
    for item in range(size - 1):
        for index in range (0, length - 1):
            comparisons += 1
            if alist[index] > alist[index + 1]:
                temp = alist[index + 1]
                alist[index + 1] = alist[index]
                alist[index] = temp
        length -= 1
    return comparisons


def QuickSort(hold):
    """
    Author: Yale Hone
    """
    global QuickSort_comparisons
    QuickSort_comparisons = 0
    global alist
    alist = QuickSort_Helper(alist)
    return QuickSort_comparisons


def QuickSort_Helper(list):
    """
    Author: Yale Hone
    """
    global QuickSort_comparisons
    Less = []
    Equal = []
    Greater = []
    if len(list) <= 1:
        return list
    pivot = list[len(list)//2]
    for index in range(len(list)):
        QuickSort_comparisons += 1
        item = list[index]
        if item == pivot:
            Equal.append(item)
        if item < pivot:
            Less.append(item)
        if item > pivot:
            Greater.append(item)
    return QuickSort_Helper(Less) + Equal + QuickSort_Helper(Greater)

class count:
    """
    Author: Panya Ou
    """
    def __init__(self):
        self.num = 0

    def increment(self):
        self.num += 1

    def getc(self):
        return self.num


count = count()


def selection_sort(alist):
    """A sorting algorithm which checks for the smallest value and places the value
    in the beginning of the list. this repeats N^2 times.
    Author: Panya Ou
    args:
        alist(list): a list of integers
    returns:
        int: the amount of comparisons it has made
        """
    size = len(alist)
    for index in reversed(range(1, size)):
        max_idx = 0
        for index_2 in range(1, index + 1):
            count.increment()
            if alist[index_2] > alist[max_idx]:
                max_idx = index_2
        alist[max_idx], alist[index] = alist[index], alist[max_idx]
    return count.getc()


# MAX HEAP
def index_parent(index):
    """compute the index of the parent.
    Author: Panya Ou
    args:
        index (int): index
    returns:
        int: the index of the parent
    """
    return (index - 1) // 2


def shift_down(alist, index, end):
    """shift down an item in the list to keep the max heap order
    Author: Panya Ou
    args:
        alist(list):a list of int
        index(int): the index of the item of interest
        end(int): the end index of the heap
    """
    if index >= end:
        return
    index_max = index_maxchild(alist, index, end)
    if index_max < 0 or alist[index_max] <= alist[index]:
        return
    alist[index], alist[index_max] = alist[index_max], alist[index]
    count.increment()
    return shift_down(alist, index_max, end)


def index_maxchild(alist, index, end):
    """returns the index of the max child.
    Author: Panya Ou
    args:
        alist(list): the list
        index(int): the index of the integer
        end(int): the end of the heap.
    returns:
        int: the index of the max child of an item."""
    left = index * 2 + 1
    right = index * 2 + 2
    if left > end:
        return -1
    if right > end:
        return left
    if alist[right] > alist[left]:
        return right
    return left


def heapify(alist):
    """convert a list into a max heap.
    Author: Panya Ou
    args:
        alist(list): a list of int
    """
    length = len(alist)
    index = index_parent(length)
    while index >= 0:
        shift_down(alist, index, length-1)
        count.increment()
        index = index - 1
    return


def del_max(alist, end):
    """pop the maximum value item from the max heap.
    Author: Panya Ou
    args:
        alist(list): a list of int
        end(int): the index of the end of the heap.
    return:
        int: the largest integer value in the max heap.
    """
    max_item = alist[0]
    alist[0] = alist[end]
    shift_down(alist, 0, end - 1)
    count.increment()
    return max_item


def heap_sort(alist):
    """Sorting the list with the use of Max Heap.
    Author: Panya Ou
    args:
        alist(lsit): a list of integers
    returns:
        int: the amount of comparisons it has made
        """
    heapify(alist)
    counter = 1
    while counter != len(alist):
        max = del_max(alist, len(alist) - counter)
        alist[len(alist)-counter] = max
        counter += 1
    return count.getc()

# alist = random.sample(range(1000000), 500000)
# # alist.sort()
# start_time = time.time()
# print(insertion_sort(alist))
# end_time = time.time()
# print(end_time - start_time)
