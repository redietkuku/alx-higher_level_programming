#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for x in range(0, len(my_list)):
        if my_list[x] % 2 == 0:
            new_list[x] = 1
        else:
            new_list[x] = 0
    return new_list
