#!/usr/bin/python3
"""
This file contains one class that defines a square.
"""


class Square:
    """
    This is a class that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size 0 and position (x=0, y=0)."""

        """Check for errors in given size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """Check for errors in given position."""
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        self.__size = value

    def area(self):
        """Calculate the area of a square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the squares with hash symbol #."""
        length = self.__size

        if self.__size == 0:
            print("")

        """Print using position of y-axis."""
        for i in range(self.__position[1]):
            print("")
        for j in range(length):
            """Print spaces and # in x-axis."""
            print((" " * self.__position[0]) + ("#" * length))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
