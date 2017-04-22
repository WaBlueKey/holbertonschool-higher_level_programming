#!/usr/bin/python3
"""
This file contains a class that defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """check if width value is an integer and is positive."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """check if height is an integer and is positive."""
        if type(value) is not int:
                raise TypeError("height must be an integer")
        if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value
