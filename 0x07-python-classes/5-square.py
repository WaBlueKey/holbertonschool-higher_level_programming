#!/usr/bin/python3
"""
This file contains one class that defines a square.
"""


class Square:
    """
    This is a class that defines a square.
    """

    def __init__(self, size=0):
        """Initialize square with size 0."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of a square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the squares with hash symbol #."""
        length = self.__size
        width = self.__size

        if self.__size == 0:
            print("")
        for j in range(width):
            print("#" * width)
