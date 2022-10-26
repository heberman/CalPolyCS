def is_lower_101(a):
    val = ord(a)
    if val >= 65 and val <= 90:
        return False
    elif val >= 97 and val <= 122:
        return True
    else:
        return -1

def char_rot_13(a):
    if a.isalpha():
        char = chr(ord(a) + 13)
        if a.islower():
            if char.islower():
                return char
            else:
                return chr(ord(a) - 13)
        else:
            if char.isupper():
                return char
            else:
                return chr(ord(a) - 13)
    else:
        return a