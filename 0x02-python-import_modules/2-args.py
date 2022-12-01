#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if (num - 1 == 1):
        print("{:d} argument".format(num - 1), end='')
    else:
        print("{:d} arguments".format(num - 1), end='')
        if (num - 1 == 0):
            print('.')
        else:
            print(':')
            for i in range(1, num):
                print("{}: {}".format(i, sys.argv[i]))
