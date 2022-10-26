"""Class: QueueArray.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

class QueueArray:
    """A queue that uses arrays.
    Attributes:
        capacity (int): the capacity of the queue
        num_items (int): the number of items in the queue
        read (int): the pointer to front of the queue
        write (int): the pointer to rear of the queue
    """
    def __init__(self, cap=2):
        self.capacity = cap
        self.arr = [None] * (self.capacity + 1)
        self.num_items = 0
        self.read = 0
        self.write = -1

    def __eq__(self, other):
        return self.arr == other.arr

    def __repr__(self):
        return str(self.arr)

    def dequeue(self):
        """Dequeues item at front of the queue.
        Args:
            -
        Returns:
            returns item at front of queue
        """
        if self.num_items == 0:
            raise IndexError()
        temp = self.arr[self.read % self.capacity]
        self.read += 1
        self.num_items -= 1
        return temp

    def enqueue(self, item):
        """Enqueues item at front of the queue.
        Args:
            item (int): item being enqueued
        Returns:
            nothing
        """
        if self.num_items == self.capacity:
            raise IndexError()
        self.arr[(self.write + 1) % self.capacity] = item
        self.write += 1
        self.num_items += 1

    def is_empty(self):
        """Returns whether or not queue is empty.
        Args:
            -
        Returns:
            returns True if queue is empty and False otherwise.
        """
        return self.num_items == 0

    def is_full(self):
        """Returns whether or not queue is full.
        Args:
            -
        Returns:
            returns True if queue is full and False otherwise.
        """
        return self.num_items == self.capacity

    def size(self):
        """Returns size of queue.
        Args:
            -
        Returns:
            returns number of items in queue.
        """
        return self.num_items
