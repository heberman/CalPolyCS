"""Function: bears().
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


def bears(num):
    """Plays a game with bears trying to get exactly 42 bears.
    Args:
        n(int): the starting number of bears
    Returns:
        bool: returns whether or not n could result in 42 bears.
    """
    if num <= 42:
        return num == 42
    if num % 5 == 0 and num - 42 >= 42:
        return bears(num - 42)
    if num % 2 == 0 and num // 2 >= 42:
        return bears(num - (num // 2))
    if num % 3 == 0 or num % 4 == 0:
        new_num = num % 100
        return bears(num - ((new_num // 10) * (new_num % 10)))
    return False
