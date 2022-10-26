"""Class: StackLinked.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""
from node import *


class StackLinked:
    """A stack that uses linked lists.
    Attributes:
        top (Node or None): pointer to last item of list
        num_items (int): the number of items in the array
    """

    def __init__(self):
        self.top = None
        self.num_items = 0

    def __eq__(self, other):
        return self.top == other.top

    def __repr__(self):
        return str(self.top)

    def push(self, item):
        """Pushes (adds) item to top of stack.
        Args:
            item (int): the payload
        Returns:
            nothing
        """
        if self.num_items == 0:
            self.top = Node(item)
        else:
            temp = self.top
            self.top = Node(item, temp)
        self.num_items += 1

    def pop(self):
        """Pops (removes) item from top of stack and returns it.
        Args:
            none
        Returns:
            int: returns the item popped
        """
        if self.num_items == 0:
            raise IndexError()
        temp = self.top.val
        self.top = self.top.next
        self.num_items -= 1
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
        return self.top.val

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
