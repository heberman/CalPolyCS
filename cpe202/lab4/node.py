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
        val (any) : the payload of any type
        next (Node) : a Linked List
    """
    def __init__(self, val, nxt=None):
        self.val = val  # the payload
        self.next = nxt  # a reference to the next node

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return "Node(%d, %s)" % (self.val, self.next)
