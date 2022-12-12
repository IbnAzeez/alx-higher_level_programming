#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_n = a_dictionary.copy()
    for key, value in list(dict_n.items()):
        dict_n[key] = value * 2
    return dict_n
