#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete = []
    for key, val in my_dict.items():
        if val is value:
            delete.append(key)
    for element in delete:
        del my_dict[element]
    return(my_dict)
