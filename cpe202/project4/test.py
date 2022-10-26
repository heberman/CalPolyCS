def main():
    arr = [1, 2, 3, 4]
    print(arr[:len(arr) // 2])
    print(arr[:(len(arr) - 1) // 2:-1])
    print(arr[:len(arr) // 2] == arr)

if __name__ == '__main__':
    main()