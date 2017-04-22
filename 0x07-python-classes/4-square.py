#!/usr/bin/python3
"""
This file contains one class Square
"""


class Square:
    """
    This class defines a square that allows for intantiation
    with a particular size.
    """

    def __init__(self, size=0):
        """ Initialization function"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """To get the size (a getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """To calculate the area of the square"""
        return (self.__size ** 2)
