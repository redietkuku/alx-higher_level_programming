#!/usr/bin/python3
"""
Peak-finder algorithm

"""

def find_peak(list_of_integers):
"""
Finds a peak in a list of unsorted integers

"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    x = int(length // 2)
    num = list_of_integers

    if x - 1 < 0 and x + 1 >= length:
        return num[x]
    elif x - 1 < 0:
         return num[x] if num[x] > num[x + 1] else num[x + 1]
    elif x + 1 >= length:
        return num[x] if num[x] > num[x-1] else num[x-1]

    if num[x - 1] < num[x] > num[x + 1]:
        return num[x]

    if num[x + 1] > num[x - 1]
        return find_peak(num[x:])
    return find_peak(num[x:])
