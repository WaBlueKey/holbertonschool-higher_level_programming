#!/usr/bin/python3
"""
This file contains one class, Square.
"""


class Square:
    """
    This class defines a square that allows for intantiation
    with a particular size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization function"""
        self.__size = size
        self.__position = position

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
        """To set the size of the square (setter)"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """To calculate the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """To print out the squares using '#' at the position provided."""
        length = self.__size

        if self.__size == 0:
            print("")

        """Print the spaces for the y-axis first"""
        for i in range(self.__position[1]):
            print("")
        for j in range(length):
            """Print the spaces to position lines in x-axis"""
            print((" " * self.__position[0]) + ("#" * length))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        if 
