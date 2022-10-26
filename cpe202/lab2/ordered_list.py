"""Classes for Node and OrderedList.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


class Node:
    """ A node of a list
    Attributes:
        val (int): the payload
        next (Node): the next item in the list
        prev (Node): the previous item in the list
    """
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev


    def __repr__(self):
        return "Node(%d, %s, %s)" % (self.val, self.next, self.prev)


    def __eq__(self, other):
        return isinstance(other, Node)\
          and self.val == other.val\
          and self.next == other.next\
          and self.prev == other.prev

class OrderedList:
    """an ordered list
    Attributes:
        head (Node): a pointer to the head of the list
        tail (Node): a pointer to the tail of the list
        num_items (int): the number of items stored in the list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __repr__(self):
        return "OrderedList(%s, %s, %d)" % (self.head, self.tail, self.num_items)

    def __eq__(self, other):
        return self.head == other.head

    def add(self, item):
        """Adds the given item into the list. O(n)
        Args:
            item (int): item to be added
        Returns:
            nothing
        """
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.head, self.tail = add_helper(self.head, self.tail, item)
        self.num_items += 1

    def remove(self, item):
        """Removes the given item from the list. O(n)
        Raises ValueError if item not found.
        Args:
            item (int): item to be removed
        Returns:
            pos(int): position of removed item
        """
        self.head, self.tail, pos = remove_helper(self.head, self.tail, item)
        self.num_items -= 1
        return pos

    def search_forward(self, item):
        """Searchs for the given item in the list starting at the head. O(n)
        Args:
            item (int): item to be searched for
        Returns:
            bool: returns True if item is found and False otherwise
        """
        return search_forward_helper(self.head, item)

    def search_backward(self, item):
        """Searchs for the given item in the list starting at the tail. O(n)
        Args:
            item (int): item to be searched for
        Returns:
            bool: returns True if item is found and False otherwise
        """
        return search_backward_helper(self.tail, item)

    def is_empty(self):
        """Returns whether or not the list is empty. O(1)
        Args:
            no args
        Returns:
            bool: returns True if list is empty and False otherwise
        """
        return self.num_items == 0

    def size(self):
        """Returns size of the list. O(1)
        Args:
            no args
        Returns:
            int: returns size of the list
        """
        return self.num_items

    def index(self, item):
        """Returns the position of item in the list. O(n)
        Raises ValueError if item not found.
        Args:
            item (int): item at the position that will be returned
        Returns:
            int: returns the index of the item in the list
        """
        return index_helper(self.head, item)

    def pop(self, pos=None):
        """Removes and returns the item at the given position from the list. O(n)
        Raises IndexError if index out of range.
        Args:
            pos (int): position of item to be popped
        Returns:
            Node: returns item at position
        """
        if pos is None:
            pos = self.num_items - 1
        if pos < 0 or pos >= self.num_items:
            raise IndexError()
        self.num_items -= 1
        if pos <= self.num_items / 2:
            self.head, val = pop_forward(self.head, pos)
        else:
            self.tail, val = pop_backward(self.tail, pos, self.num_items)
        return val


def add_helper(head, tail, item):
    """Recursive helper function for add().
    Args:
        head (Node): pointer to head node of ordered list
        tail (Node): pointer to tail node of ordered list
        item (int): item to be added
    Returns:
        (Node, Node): returns new head and tail for list
    """
    if item < head.val:
        new_node = Node(item, head, head.prev)
        if head.prev is not None:
            head.prev.next = new_node
        head.prev = new_node
        new_head = head
        while new_head.prev is not None:
            new_head = new_head.prev
        return new_head, tail
    if head.next is None:
        node = Node(item, None, head)
        head.next = node
        tail = node
        new_head = head
        while new_head.prev is not None:
            new_head = new_head.prev
        return new_head, tail
    return add_helper(head.next, tail, item)


def remove_helper(head, tail, item, pos=0):
    """Recursive helper function for remove().
    Args:
        head (Node): pointer to head node of ordered list
        tail (Node): pointer to tail node of ordered list
        item (int): item to be added
        pos (int): current position in list
    Returns:
        (Node, Node, int): returns new head and tail for list and position where item was removed
    """
    if item == head.val:
        if head.next is None and head.prev is None:
            return None, None, 0
        if head.prev is None:
            new_head = head.next
            new_head.prev = None
            new_head.next.prev = new_head
            return new_head, tail, pos
        if head.next is None:
            new_tail = head.prev
            new_tail.next = None
            new_tail.prev.next = new_tail
            new_head = head
            while new_head.prev is not None:
                new_head = new_head.prev
            return new_head, new_tail, pos
        head.prev.next = head.next
        head.next.prev = head.prev
        new_head = head
        while new_head.prev is not None:
            new_head = new_head.prev
        return new_head, tail, pos
    if head.next is None:
        raise ValueError()
    return remove_helper(head.next, tail, item, pos + 1)

def search_forward_helper(head, item):
    """Recursive helper function for search_forward().
    Args:
        head (Node): pointer to head node of ordered list
        item (int): item being searched for
    Returns:
        bool: returns True if item is found and False otherwise
    """
    if head is None:
        return False
    if head.val == item:
        return True
    return search_forward_helper(head.next, item)


def search_backward_helper(tail, item):
    """Recursive helper function for search_backward().
    Args:
        tail (Node): pointer to tail node of ordered list
        item (int): item being searched for
    Returns:
        bool: returns True if item is found and False otherwise
    """
    if tail is None:
        return False
    if tail.val == item:
        return True
    return search_backward_helper(tail.prev, item)


def index_helper(head, item, pos=0):
    """Recursive helper function for index().
    Args:
        head (Node): pointer to head node of ordered list
        item (int): item being searched for
        pos (int): current position in list
    Returns:
        int: returns index of item in list
    """
    if head.val == item:
        return pos
    if head.next is None or item < head.val:
        raise ValueError
    return index_helper(head.next, item, pos + 1)


def pop_forward(head, pos, current_pos=0):
    """Recursive helper function for pop().
    Args:
        head (Node): pointer to head node of ordered list
        pos (int): position of item
        current_pos (int): current position in list
    Returns:
        Node, int: returns pointer to head node and the value being popped
    """
    if current_pos < pos:
        return pop_forward(head.next, pos, current_pos + 1)
    if head.next is None and head.prev is None:
        return None, head.val
    if head.prev is None:
        new_head = head.next
        new_head.prev = None
        if new_head.next is not None:
            new_head.next.prev = new_head
        return new_head, head.val
    head.prev.next = head.next
    head.next.prev = head.prev
    new_head = head
    while new_head.prev is not None:
        new_head = new_head.prev
    return new_head, head.val


def pop_backward(tail, pos, current_pos):
    """Recursive helper function for pop().
        Args:
            tail (Node): pointer to tail node of ordered list
            pos (int): position of item
            current_pos (int): current position in list
        Returns:
            Node, int: returns pointer to tail node and the value being popped
        """
    if current_pos > pos:
        return pop_backward(tail.prev, pos, current_pos - 1)
    if tail.next is None and tail.prev is None:
        return None, tail.val
    if tail.next is None:
        new_tail = tail.prev
        new_tail.next = None
        if new_tail.prev is not None:
            new_tail.prev.next = new_tail
        return new_tail, tail.val
    tail.next.prev = tail.prev
    tail.prev.next = tail.next
    new_tail = tail
    while new_tail.next is not None:
        new_tail = new_tail.next
    return new_tail, tail.val
