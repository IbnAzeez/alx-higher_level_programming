#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c not in (ord('e'), ord('q')):
        print("{:c}".format(c), end='')
