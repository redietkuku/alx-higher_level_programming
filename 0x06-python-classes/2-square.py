#!/usr/bin/python3
""" definition of a square """


class Square:
    """ square and it's private instance attribute size """

    def __init__(self, size=0):
        """
        Argumentss:
            size: the size of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
