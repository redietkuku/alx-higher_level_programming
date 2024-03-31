#!/usr/bin/python3
"""does the same thing as python bytecode"""


def magic_calculation(a, b):
    result = 0

    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')

            result += a ** b / x
        except:
            result = b + a
            break

    return result
