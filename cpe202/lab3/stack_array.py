"""Class: StackArray.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


class StackArray:
    """A stack that uses arrays
    Attributes:
        arr (array): the array
        capacity (int): the size of the array
        num_items (int): the number of items in the array
    """
    def __init__(self):
        self.arr = [None] * 2
        self.capacity = 2
        self.num_items = 0

    def __repr__(self):
        return str(self.arr)

    def __eq__(self, other):
        return self.arr == other.arr

    def enlarge(self):
        """Enlarges the list capacity by a factor of 2.
        Args:
            none
        Returns:
            nothing
        """
        new_arr = [None] * (self.capacity * 2)
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity * 2

    def shrink(self):
        """Shrinks the list capacity by a factor of 1/2.
        Args:
            none
        Returns:
            nothing
        """
        new_arr = [None] * (self.capacity // 2)
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity // 2

    def push(self, item):
        """Pushes (adds) item to top of stack.
        Args:
            item (int): the payload
        Returns:
            nothing
        """
        self.arr[self.num_items] = item
        self.num_items += 1
        if self.num_items == self.capacity:
            self.enlarge()

    def pop(self):
        """Pops (removes) item from top of stack and returns it.
        Args:
            none
        Returns:
            int: returns the item popped
        """
        if self.num_items == 0:
            raise IndexError()
        temp = self.arr[self.num_items - 1]
        self.arr[self.num_items - 1] = None
        self.num_items -= 1
        if self.num_items != 0:
            if self.capacity / self.num_items >= 4:
                self.shrink()
        return temp

    def peek(self):
        """Peeks at (returns) the top item in the list.
        Args:
            none
        Returns:
            int: returns the top item
        """
        if self.num_items == 0:
            raise IndexError()
        return self.arr[self.num_items - 1]

    def is_empty(self):
        """Returns whether or not stack is empty.
        Args:
            none
        Returns:
            bool: returns True if stack is empty and False otherwise
        """
        return self.num_items == 0

    def size(self):
        """Returns size of stack.
        Args:
            none
        Returns:
            int: returns number of items in stack
        """
        return self.num_items
