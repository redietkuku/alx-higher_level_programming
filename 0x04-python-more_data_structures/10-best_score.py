#!/usr/bin/python3
def best_score(my_dict):
    if my_dict and len(my_dict):
        max = list(my_dict.keys())[0]
        for x in my_dict:
            if my_dict[x] > my_dict[max]:
                max = x
        return max
    return None
