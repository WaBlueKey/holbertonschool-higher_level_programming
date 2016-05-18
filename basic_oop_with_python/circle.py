'''
A script circle.py that describe a Circle Class
'''

import math

'''Class'''
class Circle(object):

   ''' Constructor '''
   def __init__(self, radius):
       self.__radius = radius

   def set_center(self, center):
       self.__center = center

   def set_color(self, color):
       self.__color = color

   def set_name(self, name):
       self.name = name

   def area(self):
       return (self.__radius ** 2) * math.pi

   def get_color(self):
       return self.color

   def get_center(self):
       return self.center
