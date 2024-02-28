#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    last_digit_of_num = abs(number) % 10
    print(f"{last_digit_of_num}", end='')
    return last_digit_of_num
