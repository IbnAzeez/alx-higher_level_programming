#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for element in my_list[:x]:
        try:
            print("{:d}".format(element), end='')
            i += 1
        except ValueError:
            pass
    print()
    return i
