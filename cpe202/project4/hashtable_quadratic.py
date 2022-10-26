"""Class: HashTableQuadratic
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


def hash_string(string, size):
    """computes hash value for a string
    Args:
        string (str): input string
        size (int): size of the hash table
    Returns:
        (int): hash value for string
    """
    hash_val = 0
    for val in string:
        hash_val = (hash_val * 31 + ord(val)) % size
    return hash_val


class HashTableQuadratic:
    """hash table object that uses quadratic probing for collision resolution
    Attributes:
        hash (list): hash table
        table_size (int): size of the table
        num_items (int): number of items in the list
        num_collisions (int): number of collisions that have occurred
    """
    def __init__(self, table_size=16):
        self.hash = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.num_collisions = 0

    def __eq__(self, other):
        return self.hash == other.hash

    def __repr__(self):
        return str(self.hash)

    def resize(self):
        """increases size of hash table
        Args:
            -
        Returns:
            -
        """
        old_arr = self.hash
        self.hash = [None] * (2 * self.table_size)
        self.table_size = len(self.hash)
        for item in old_arr:
            if item is not None:
                self.put(item[0], item[1])
                self.num_items -= 1

    def put(self, key, data):
        """puts key-data pair into hash table
        Args:
            key (str): key of key-data pair
            data (any): data of key-data pair
        Returns:
            -
        """
        if (self.num_items + 1) / self.table_size > 0.75:
            self.resize()
        hash_val = hash_string(key, self.table_size)
        index = hash_val % self.table_size
        root = 1
        if self.hash[index] is not None:
            self.num_collisions += 1
        while self.hash[index] is not None and self.hash[index] != 'del' \
                and self.hash[index][0] != key:
            index = (index + root ** 2) % self.table_size
            root += 1
        if self.hash[index] is None:
            self.hash[index] = [key, data]
            self.num_items += 1
        else:
            self.hash[index][1] = data

    def get(self, key):
        """gets value from key-value pair in hash table
        Args:
            key (str): key being searched for
        Returns:
            (any): returns value associated with given key
        Raises:
            KeyError: if key not found
        """
        hash_val = hash_string(key, self.table_size)
        index = hash_val % self.table_size
        root = 1
        while self.hash[index] is not None and self.hash[index][0] != key:
            index = (index + root ** 2) % self.table_size
            root += 1
        if self.hash[index] is not None and self.hash[index][0] == key:
            return self.hash[index][1]
        raise KeyError

    def contains(self, key):
        """checks if hash table contains given key
        Args:
            key (str): key being searched for
        Returns:
            (bool): True if found, False otherwise
        """
        try:
            val = self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """removes given key-value pair from table
        Args:
            key (str): key being removed
        Returns:
            (str, any): returns key-value pair
        """
        if key not in self:
            raise KeyError
        hash_val = hash_string(key, self.table_size)
        index = hash_val % self.table_size
        root = 1
        while self.hash[index] is not None and self.hash[index][0] != key:
            index = (index + root ** 2) % self.table_size
            root += 1
        temp = self.hash[index]
        self.hash[index] = 'del'
        self.num_items -= 1
        return temp

    def size(self):
        """returns number of key-val pairs in hash table
        Args:
            -
        Returns:
            (int): returns num_items
        """
        return self.num_items

    def load_factor(self):
        """finds and returns current load factor of the hash table
        Args:
            -
        Returns:
            (float): returns num_items / table_size
        """
        return float('{:.2f}'.format(self.num_items / self.table_size))

    def collisions(self):
        """returns number of collisions that have occurred with this hash table
        Args:
            -
        Returns:
            (int): returns number of collisions
        """
        return self.num_collisions

    def keys(self):
        """returns list of keys present in table
        Args:
            -
        Returns:
            (list): list of keys
        """
        keys = []
        for item in self.hash:
            if item:
                keys.append(item[0])
        return keys

    def __getitem__(self, key):
        """This is for getting a value with []"""
        return self.get(key)

    def __setitem__(self, key, data):
        """This is for enabling value assignment with []"""
        self.put(key, data)

    def __contains__(self, key):
        """This is for enabling 'in' operator on our Hash Tables"""
        return self.contains(key)


def import_stopwords(filename, hashtable):
    """imports stopwords from file and organizes them into a hash table.
    Args:
        filename (str): name of file
        hashtable (HashTableSepchain or HashTableLinear or HashTableQuadratic): empty hash table
    Returns:
        (HashTable): returns new hash table containing the stop words
    """
    file = open(filename, 'r')
    words = file.readline().split()
    for word in words:
        hashtable[word] = 0
    file.close()
    return hashtable
