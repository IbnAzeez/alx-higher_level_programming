#!/usr/bin/python3
def max_integer(my_list=[]):
    if 0 == len(my_list):
        return None
    number = min(my_list)
    for num in my_list:
        if num > number:
            number = num
    return number

