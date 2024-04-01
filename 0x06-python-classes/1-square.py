#!/usr/bin/python3
"""Definition of the class Square"""


class Square:
    """it represents a square
    the attributes are:
        __size (int): the size of one of the sides
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): the size of the sides
        Returns: None
        """
        self.__size = size
