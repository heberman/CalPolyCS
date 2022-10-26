"""Class: Node.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


class Node:
    """A Linked List is one of
        - None, or
        - Node(val, next) : A Linked Lists
    Attributes:
        key (str) : key of type string for lab 8
        val (any) : the payload of any type
        next (Node) : a Linked List
    """
    def __init__(self, key, val, nxt=None):
        self.key = key  # the key
        self.val = val  # the payload
        self.next = nxt  # a reference to the next node

    def __eq__(self, other):
        return self.key == other.key and self.val == other.val and self.next == other.next

    def __repr__(self):
        return "Node(%s, %d, %s)" % (self.key, self.val, self.next)
