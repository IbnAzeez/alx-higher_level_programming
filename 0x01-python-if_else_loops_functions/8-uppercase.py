#!/usr/bin/python3
def uppercase(str):
    for c in str:
        C = ord(c)
        if C in range(ord('a'), ord('z') + 1):
            C = ord(c) - 32
        print("{:c}".format(C), end='')
    print()
