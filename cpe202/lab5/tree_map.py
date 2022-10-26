"""Contains starter code for lab 5

CPE202

Instructions:
    Complete this file by writing python3 code.

"""
import random
import bst
from classmate import classmate_factory 


class TreeMap:
    """Write the docstring
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        return bst.inorder_list(self.tree)

    def __eq__(self, other):
        return self.tree == other.tree

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.
        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False 
        """
        return self.contains(key)

    def get(self, key):
        """gets value associated with given key
        Args:
            key (any) : a key which is comparable by <,>,==
        Returns:
            any : the value associated with th key
        Raises:
            KeyError : if the key does not exist
        """
        return bst.get(self.tree, key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py and increments num_items by 1

        Args:
            key (any) : a key which is comparable by <,>,==
            val (any): the value associated with the key
        """
        self.tree = bst.insert(self.tree, key, val)
        self.num_items += 1

    def contains(self, key):
        """Checks to see if tree contains key
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False 
        """
        return bst.contains(self.tree, key)

    def delete(self, key):
        """deletes a key value pair from the map
        Calls delete function in bst.py and increments num_items by -1
        Args:
            key (any) : a key which is comparable by <,>,==
        Raises:
            KeyError : if the key does not exist
        """
        self.tree = bst.delete(self.tree, key)
        self.num_items -= 1

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self) -> (any, any):
        """Finds smallest key.
        Args:
            tree (BSTNode): the BST
        Returns:
            (int, any): returns key and val of min
        """
        return bst.find_min(self.tree)

    def find_max(self)->(any, any):
        """Finds largest key.
        Args:
            tree (BSTNode): the BST
        Returns:
            (int, any): returns key and val of max
        """
        return bst.find_max(self.tree)

    def inorder_list(self)->list:
        """Returns tree in inorder traversal.
        Args:
            tree (BSTNode): the BST
        Returns:
            (list): returns keys of tree nodes
        """
        return bst.inorder_list(self.tree)

    def preorder_list(self)->list:
        """Returns tree in preorder traversal.
        Args:
            tree (BSTNode): the BST
        Returns:
            (list): returns keys of tree nodes
        """
        return bst.preorder_list(self.tree)

    def tree_height(self)->int:
        """Finds height of tree.
        Args:
            tree (BSTNode): the BST
        Returns:
            (int): returns tree height
        """
        return bst.tree_height(self.tree)

    def range_search(self, low, high) -> list:
        """Searches for all keys in range.
        Args:
            tree (BSTNode): the BST
            low (int): lower bound
            high (int): upper bound
        Returns:
            (list): returns list of all keys in the given range
        """
        return bst.range_search(self.tree, low, high)


def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is done for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    tree_map = TreeMap()
    classmates = []
    lines = open(filename, 'r')
    for line in lines:
        tokens = line.split('\t')
        classmate = classmate_factory(tokens)
        classmates.append(classmate)

    random.seed(2)
    random.shuffle(classmates)

    for classmate in classmates:
        tree_map.put(classmate.sid, classmate)
    return tree_map


def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the sid as a key

    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : the id of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the id does not exist
    """
    if sid in tmap:
        return tmap[sid]
    raise KeyError()
