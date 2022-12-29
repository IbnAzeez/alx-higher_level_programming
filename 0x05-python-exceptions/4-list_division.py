#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = list()

    for element in range(list_length):
        try:
            new_list.append(my_list_1[element] / my_list_2[element])
        except IndexError:
            new_list.append(0)
            print("out of range")
        except (ValueError, TypeError):
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except:
            pass
        finally:
            pass
    return new_list
