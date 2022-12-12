#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    val = list(a_dictionary.keys())
    val.sort()
    for element in val:
        print("{}: {}".format(element, a_dictionary.get(element)))
