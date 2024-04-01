#!/usr/bin/python3
"""Definiton of the class MagicClass"""
import math


class MagicClass:
    """This class represents a circle"""
    def __init__(self, radius=0):
        """it initializes the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """it calculates the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """it calculates the circumference"""
        return 2 * math.pi * self.__radius
