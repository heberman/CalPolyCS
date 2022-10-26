def rotate_chars(chars, n_pos):
    word = ""
    for i in chars:
        num = ord(i)
        if (num < 65 or num > 90) and (num < 97 or num > 122):
            word = word + i
        elif (num >= 65 and num <= 90 and num + n_pos > 90):
            extra = (num + n_pos) - 90
            x = 64 + extra
            word = word + chr(x)
        elif (num >= 97 and num <= 122 and num + n_pos > 122):
            extra = (num + n_pos) - 122
            x = 96 + extra
            word = word + chr(x)
        else:
            word = word + chr(num + n_pos)
    return word
