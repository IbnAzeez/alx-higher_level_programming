#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    i = 0

    for element in range(list_length):
        try:
            new_list.append(my_list_1[element] / my_list_2[element])
        except IndexError:        
            print("out of range")
            i = 0
        except (ValueError, TypeError):
            print("wrong type")
            i = 0
        except ZeroDivisionError:
            print("division by 0")
            i = 0
        finally:
            new_list.append(i)
    return new_list
