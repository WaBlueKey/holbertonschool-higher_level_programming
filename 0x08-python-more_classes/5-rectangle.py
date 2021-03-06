#!/usr/bin/python3
"""
This file contains a class that defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height of 0."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """check if width value is an integer and is positive."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """check if height is an integer and is positive."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print the rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += ("#" * self.__width) + "\n"
        """Remove the extra new line."""
        return rect.rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return ("Rectangle(%s, %s)" % (str(self.__width), str(self.__height)))

    def __del__(self):
        """Deletes rectangle and prints the message."""
        print("Bye rectangle...")
