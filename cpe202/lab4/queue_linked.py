"""Class: QueueLinked.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

from node import *


class QueueLinked:
    """A queue that uses linked lists.
    Attributes:
        capacity (int): the capacity of the queue
        num_items (int): the number of items in the queue
        front (None or Node): the pointer to front of the queue
        rear (None or Node): the pointer to rear of the queue
    """
    def __init__(self, cap=2):
        self.capacity = cap
        self.num_items = 0
        self.front = None
        self.rear = None

    def __eq__(self, other):
        return self.capacity == other.capacity and self.front == other.front

    def __repr__(self):
        return str(self.front)

    def dequeue(self):
        """Dequeues item at front of the queue.
        Args:
            -
        Returns:
            returns item at front of queue
        """
        if self.num_items == 0:
            raise IndexError()
        temp = self.front.val
        self.front = self.front.next
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
        if self.rear is None:
            self.front = Node(item)
            self.rear = self.front
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next
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
