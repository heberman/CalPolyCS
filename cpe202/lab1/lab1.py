"""Functions for Lab 1.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


def get_max(in_list):
    """Find the max value in a list of integers.
    Args:
        in_list(list): a list of integers
    Returns:
        max_val(int): the max value in the list, or None if in_list is empty
    """
    if len(in_list) == 0:
        return None
    max_val = in_list[0]
    for i in range(1, len(in_list)):
        if in_list[i] > max_val:
            max_val = in_list[i]
    return max_val


def reverse(str):
    """Reverses the input string.
    Args:
        str(string): any string
    Returns:
        string: returns the original string in reverse order
    """
    if len(str) == 0:
        return str
    return str[len(str) - 1] + reverse(str[:(len(str) - 1)])


def binary_search(in_list, target):
    """Searches sorted list for specified value.
    Time Complexity: O(log(n))
        Args:
            in_list(list): a sorted list of integers
            target(int): the value being searched for
        Returns:
            int: returns the index where the target is found in the list,
                        or None if the target is not found or the list is empty
    """
    if len(in_list) == 0:
        return None
    lo = 0
    hi = len(in_list) - 1
    return search_helper(in_list, target, lo, hi)


def search_helper(in_list, target, lo, hi):
    """Helper function for binary_search.
    Args:
        in_list(list): a sorted list of integers
        target(int): the value being searched for
        lo(int): the lower bound of the search
        hi(int): the upper bound of the search
    Returns:
        int: returns the index where the target is found in the list,
                    or None if the target is not found
    """
    mid = (lo + hi) // 2
    if in_list[mid] == target:
        return mid
    if lo == hi:
        return None
    if in_list[mid] > target:
        hi = mid - 1
    elif in_list[mid] < target:
        lo = mid + 1
    return search_helper(in_list, target, lo, hi)


def fib(n):
    """Finds and returns the Fibonacci number at the nth place.
    Time Complexity: O(2^n)
        Args:
            n(int): the index in the Fibonacci sequence
        Returns:
            int: returns the Fibonacci number at the nth place
    """
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def factorial_iter(n):
    """Calculates the factorial of the input integer iteratively.
        Args:
            n(int): the input integer
        Returns:
            int: returns the factorial of the input integer (n!)
    """
    ans = 1
    for i in range(n):
        ans = ans * (n - i)
    return ans


def factorial_rec(n):
    """Calculates the factorial of the input integer recursively.
        Args:
            n(int): the input integer
        Returns:
            int: returns the factorial of the input integer (n!)
    """
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


