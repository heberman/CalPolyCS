"""Class for Node and function invert_list().
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


def invert_list(int_list):
    """Inverts given linked list.
    Args:
        int_list (list): singly linked list of integers
    Returns:
        list: returns int_list in reverse order
    """
    return invert_list_helper(int_list)


def invert_list_helper(int_list, rev_list=None):
    """Helper function for invert_list().
    Args:
        int_list (list): singly linked list of integers
        rev_list (list): the new reverse list being built
    Returns:
        list: returns int_list in reverse order
    """
    if int_list is None:
        return rev_list
    return invert_list_helper(int_list.next, Node(int_list.val, rev_list))
