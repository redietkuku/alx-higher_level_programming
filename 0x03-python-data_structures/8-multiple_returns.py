#!/usr/bin/python3
def multiple_returns(sentence):
    the_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        the_tuple = len(sentence), sentence[0]
    return the_tuple
