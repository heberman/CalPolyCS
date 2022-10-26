from sys import *

def main():
    s = False
    ints = 0
    floats = 0
    other = 0
    sum = 0
    f = ""

    if len(argv) == 3:
        for i in range(len(argv)):
            if argv[i] == '-s':
                s = True
                f = argv[3 - i]
                break
        else:
            print("Usage: [-s] file_name")
            exit()
    elif len(argv) == 2:
        f = argv[1]
    else:
        print("Usage: [-s] file_name")
        exit()

    try:
        t = open(f, "r")
    except:
        print("Unable to open", f)
        exit()
        
    for line in t:
        x = line.split()
        for val in x:
            try:
                a = int(val)
                ints += 1
                sum += a
            except:
                try:
                    b = float(val)
                    floats += 1
                    sum += b
                except:
                    other += 1

    print("Ints:", ints)
    print("Floats:", floats)
    print("Other:", other)
    if s:
        print("Sum: %.2f" % sum)

if __name__ == '__main__':
    main()



