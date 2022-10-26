"""Module for BST
CPE202

Contains the data definition of BST,
and functions (not class member methods) on BST.

Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.


Author:
    Henry Berman
"""
class BSTNode:
    """ Binary Search Tree is one of
    - None
    - BSTNode

    Attributes:
        key (any): key
        val (any): value associated with the key
        left (BSTNode): left subtree of Binary Search Tree
        right (BSTNode): right subtree of Binary Search Tree
    """
    #---- to do ----
    # implement __init__, __eq__ and __repr__
    #---------------
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return "(" + str(self.key) + ", " + str(self.val) + ")"


def get(tree, key) -> any:
    """Returns value at key or None if not found.
    Args:
        tree (BSTNode): the BST
        key (int): the key being searched for
    Returns:
        (any): returns val or None
    """
    if tree is None:
        raise KeyError()
    if key == tree.key:
        return tree.val
    if key < tree.key:
        return get(tree.left, key)
    return get(tree.right, key)


def contains(tree, key) -> bool:
    """Returns True if key is in map.
    Args:
        tree (BSTNode): the BST
        key (int): the key being searched for
    Returns:
        (bool): Returns True if key is in map and False otherwise.
    """
    if tree is None:
        return False
    if key == tree.key:
        return True
    if key < tree.key:
        return contains(tree.left, key)
    return contains(tree.right, key)


def insert(tree, key, val) -> BSTNode:
    """Inserts node into tree with given key and val.
    Args:
        tree (BSTNode): the BST
        key (any): the key being added
        val (any): the val being added
    Returns:
        (BSTNode): returns new tree
    """
    if tree is None:
        tree = BSTNode(key, val)
    else:
        if key < tree.key:
            tree.left = insert(tree.left, key, val)
        else:
            tree.right = insert(tree.right, key, val)
    return tree


def delete(tree, key) -> BSTNode:
    """Deletes node from tree.
    Args:
        tree (BSTNode): the BST
        key (any): the key being deleted
    Returns:
        (BSTNode): returns new tree
    """
    if tree is None:
        raise KeyError()
    if tree.key == key:
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        new_tree = tree.right
        while new_tree.left is not None:
            new_tree = tree.left
        tree = delete(tree, new_tree.key)
        tree.key = new_tree.key
        tree.val = new_tree.val
        return tree
    if tree.key > key:
        tree.left = delete(tree.left, key)
    if tree.key < key:
        tree.right = delete(tree.right, key)
    return tree


def find_min(tree) -> (any, any):
    """Finds smallest key.
    Args:
        tree (BSTNode): the BST
    Returns:
        (int, any): returns key and val of min
    """
    if tree is None:
        raise ValueError()
    if tree.left is None:
        return tree.key, tree.val
    return find_min(tree.left)


def find_max(tree) -> (any, any):
    """Finds largest key.
    Args:
        tree (BSTNode): the BST
    Returns:
        (int, any): returns key and val of max
    """
    if tree is None:
        raise ValueError()
    if tree.right is None:
        return tree.key, tree.val
    return find_max(tree.right)


def inorder_list(tree):
    """Returns tree in inorder traversal.
    Args:
        tree (BSTNode): the BST
    Returns:
        (list): returns keys of tree nodes
    """
    if tree is None:
        return []
    left = inorder_list(tree.left)
    right = inorder_list(tree.right)
    return left + [tree.key] + right


def preorder_list(tree):
    """Returns tree in preorder traversal.
    Args:
        tree (BSTNode): the BST
    Returns:
        (list): returns keys of tree nodes
    """
    if tree is None:
        return []
    left = preorder_list(tree.left)
    right = preorder_list(tree.right)
    return [tree.key] + left + right


def tree_height(tree) -> int:
    """Finds height of tree.
    Args:
        tree (BSTNode): the BST
    Returns:
        (int): returns tree height
    """
    if tree is None:
        return -1
    if tree.left is None:
        return tree_height(tree.right) + 1
    if tree.right is None:
        return tree_height(tree.left) + 1
    return max(tree_height(tree.left), tree_height(tree.right)) + 1


def range_search(tree, low, high, accum=[]):
    """Searches for all keys in range.
    Args:
        tree (BSTNode): the BST
        low (int): lower bound
        high (int): upper bound
        accum (list): list of found keys
    Returns:
        (list): returns list of all keys in the given range
    """
    if tree is None:
        return []
    if tree.key > low:
        range_search(tree.left, low, high)
    if low <= tree.key < high:
        accum.append((tree.key, tree.val))
    if tree.key < high:
        range_search(tree.right, low, high)
    return accum
