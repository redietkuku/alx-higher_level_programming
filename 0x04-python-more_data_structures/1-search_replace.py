#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(map(lambda e: replace if e == search else e, my_list))
    return (new)
