#!/usr/bin/python3

def multiple_returns(sentence):
    len_sent = len(sentence)
    if len_sent == 0:
        result = (0, None)
        return result
    else:
        res = (len_sent, sentence[0:1])
        return res
