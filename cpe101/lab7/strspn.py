def main():
    str1 = input("Enter string1: ")
    str2 = input("Enter string2: ")
    print("Result:", my_strspn(str1, str2))

def my_strspn(str1, str2):
    result = 0
    for x in str1:
        if x in str2:
            result += 1
        else:
            break
    return result

if __name__ == '__main__':
    main()