#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decs = [roman_dict[y] for y in roman_string]
    result = 0
    for z in range(len(decs)):
        result += decs[z]
        if decs[z - 1] < decs[z] and z != 0:
            result -= (decs[z - 1] + decs[z - 1])
    return result
