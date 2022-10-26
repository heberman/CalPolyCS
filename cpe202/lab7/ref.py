class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): the capacity of the queue. The default capacity is 2,
        but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, arr=None):
        if arr is None:
            self.capacity = 2
            self.arr = [None] * self.capacity
            self.num_items = 0
        else:
            self.heapify(arr)
            self.capacity = len(self.arr)
            self.num_items = len(self.arr)

    def __eq__(self, other):
        if self.arr == other.arr and self.num_items == other.num_items:
            return True
        return False

    def __repr__(self):
        pass

    def heapify(self, arr):
        """initialize the queue with a given array and convert the array into a min heap
        Args:
            arr (list): an array
        Returns:
            None : it returns nothing
        """
        heap = MinPQ()
        for i in arr:
            heap.insert(i)
        self.arr = heap.arr

    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.
        Args:
            item (any): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
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
                    self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
                    index = parent_index
                    parent_index = (index - 1) // 2
                    if parent_index < 0:
                        break

    def del_min(self):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array
        Returns:
            any : it returns the minimum item, which has just been deleted
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
        if self.capacity > 2 and self.num_items > 0 and self.num_items <= self.capacity // 4:
            self.shrink()
        return temp

    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
            any : it returns the minimum item
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.num_items > 0:
            return self.arr[0]
        raise IndexError

    def is_empty(self):
        """checks if the queue is empty
        Returns:
            bool : True if empty, False otherwise.
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """returns the number of items in the queue
        Returns:
            int : it returns the number of items in the queue
        """
        return self.num_items

    def enlarge(self):
        """double the original capacity of the array
        """
        self.capacity += 1
        self.arr += [None]


    def shrink(self):
        """shrinks the array.
        """
        self.capacity /= 2