"""Class: MinPQ.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): The capacity of the queue.
                        The default capacity is 2, but will be increased automatically.
        num_items (int): The number of items in the queue.
                         Also points to the position where a new item will be added.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, arr=None):
        if arr is None:
            self.arr = [None] * 2
            self.capacity = 2
            self.num_items = 0
        else:
            self.arr = arr
            self.capacity = len(arr)
            self.num_items = len(arr)
            self.heapify(self.arr)

    def __eq__(self, other):
        return self.arr == other.arr

    def __repr__(self):
        return str(self.arr)

    def heapify(self, arr):
        """converts array to heap
        Args:
            arr (list): an array
        Returns:
            -
        """
        heap = MinPQ()
        for i in arr:
            heap.insert(i)
        self.arr = heap.arr

    def insert(self, item):
        """inserts an item to the queue
        Args:
            item (any): an item to be inserted to the queue
        Returns:
            -
        """
        if self.capacity == self.num_items:
            self.enlarge()
        index = self.num_items
        self.arr[index] = item
        self.num_items += 1
        if (index - 1) // 2 >= 0:
            parent_index = (index - 1) // 2
            if self.arr[index] is not None:
                while self.arr[index] < self.arr[parent_index]:
                    temp = self.arr[index]
                    self.arr[index] = self.arr[parent_index]
                    self.arr[parent_index] = temp
                    index = parent_index
                    parent_index = (index - 1) // 2
                    if parent_index < 0:
                        break

    def del_min(self):
        """deletes the minimum item in the queue
        Returns:
            any: returns the minimum item
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        last_index = self.num_items - 1
        temp = self.arr[0]
        self.arr[0] = self.arr[last_index]
        self.arr[last_index] = None
        self.heapify(self.arr)
        self.num_items -= 1
        if self.capacity > 2 and 0 < self.num_items <= self.capacity // 4:
            self.shrink()
        return temp

    def min(self):
        """returns the minimum item in the queue
        Returns:
            any: returns the minimum item
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.num_items > 0:
            return self.arr[0]
        raise IndexError

    def is_empty(self):
        """checks if the queue is empty
        Returns:
            bool: True if empty, False otherwise
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """returns the number of items in the queue
        Returns:
            int: returns the number of items in the queue
        """
        return self.num_items

    def enlarge(self):
        """double the original capacity of the array
        Returns:
            -
        """
        self.capacity += 1
        self.arr += [None]

    def shrink(self):
        """shrinks the array.
        Returns:
            -
        """
        self.capacity /= 2
