"""Function: perm_gen_lex().
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

def perm_gen_lex(in_str):
    """Generate all the permutations of the characters in a string.
    Args:
        in_str(string): input string that gets permutated
    Returns:
        perms(list): list of all permutations of in_str
    """
    perms = []
    if len(in_str) == 0:
        return []
    if len(in_str) == 1:
        return [in_str]
    if len(in_str) == 2:
        return [in_str, in_str[1] + in_str[0]]
    for i, val in enumerate(in_str):
        new_str = in_str[:i] + in_str[(i + 1):]
        temp_perms = perm_gen_lex(new_str)
        for perm in temp_perms:
            new_perm = val + perm
            perms.append(new_perm)
    return perms
