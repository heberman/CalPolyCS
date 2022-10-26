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

def str_rot_13(str):
    new_str = ""
    return new_str.join([char_rot_13(x) for x in str])

def str_translate_101(str, old, new):
    new_str = ""
    for char in str:
        if char == old:
            new_str += new
        else:
            new_str += char
    return new_str