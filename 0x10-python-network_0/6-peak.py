#!/usr/bin/python3
"""
Peak-finder algorithm

"""

def find_peak(list_of_integers):
"""
Finds a peak in a list of unsorted integers

"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of _integers) - 1

    while low <= high:
        mid =(low + high) // 2

        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
            (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
                return lsit_of_integers[mid]

        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else
            low = mid + 1
    return None
