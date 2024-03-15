#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete_list = []
    for i in my_dict:
        if my_dict[i] == value:
            delete_list.append(i)
    for i in delete_list:
        del my_dict[i]
    return my_dict
