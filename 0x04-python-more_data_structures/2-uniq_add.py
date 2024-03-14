#!/usr/bin/python3
def uniq_add(my_list=[]):
    adder = 0
    for x in set(my_list):
        adder += x
    return adder
