#!/usr/bin/python3
"""
This file contains a class that defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height of 0."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width."""
        return (self.__width)

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
        return (self.__height)

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
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def bigger_or_equal(self, rect_1, rect_2):
        """Compare rectangles' size & confirm instance is of Rectangle class"""
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if area(rect_1) > area(rect_2):
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

    def __str__(self):
        """Print the rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            rect += (str(self.print_symbol) * self.__width) + "\n"
        """Remove the extra new line."""
        return (rect.rstrip())

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return ("Rectangle(%s, %s)" % (str(self.__width), str(self.__height)))

    def __del__(self):
        """Deletes rectangle instance and prints the message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
