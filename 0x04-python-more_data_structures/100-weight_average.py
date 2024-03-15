#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        demo = 0
        for y in my_list:
            number += (y[0] * y[1])
            demo += y[1]
        return (number / demo)
    return 0
