"""Function: convert().
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


def convert(num, base):
    """Converts integer to given base.
    Args:
        in_int(int): input integer in base 10
        base(int): base that in_int will be converted to
    Returns:
        result(int): returns result after base conversion
    """
    quotient = num // base
    remainder = num % base
    if remainder > 9:
        remainder = chr(55 + remainder)
    if quotient == 0:
        return str(remainder)
    return str(convert(quotient, base)) + str(remainder)
