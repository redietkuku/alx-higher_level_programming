#!/usr/bin/python3
"""it defines the class Square"""


class Square:
    """it represents a square
    Attributes:
        __size (int): the size of a side of the square
    """
    def __init__(self, size=0):
        """it initializes the square
        Arguments:
            size (int): the size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """it calculates the square's area
        Returns:
            The area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """the getter of __size
        Returns:
            The size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """the setter of __size
        Arguments:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """it compares if square is less than another by area
        Arguments:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """it compares if square is less than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """it compares if square is equal to another by area
        Arguments:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """it compares if square is not equal to another by area
        Arguments:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """it compares if square is greater than or equal to another by area
        Arguments:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """it compares if square is greater than another by area
        Arguments:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
