'''
GitHub repo:
Project directory:
Task #: 0 - 5
Dependent or test file(s): 0-main.py, 1-main.py, 2-main.py, 3-main.py, \
4-main.py, 5-main.py

Summary:

By: Zee Adams, 2016
'''

import json
import os.path

class Person():

    '''class attributes'''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        '''id exception'''
        if((id < 0) or (type(id) is not int)):
            raise Exception("id is not an integer")
        self.__id = id

        '''eye color exception'''
        if(eyes_color not in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

        '''gender exception'''
        if(genre not in Person.GENRES):
            raise Exception("genre is not valid")
        self.__genre = genre

        '''DOB exception'''
        if(len(date_of_birth) != 3):
            raise Exception("date_of_birth is not a valid date")
        if((date_of_birth[0] < 1) or (date_of_birth[0] > 12)):
            raise Exception("date_of_birth is not a valid date")
        if((date_of_birth[1] < 1) or (date_of_birth[1] > 31)):
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth

        '''first name exception'''
        if((type(first_name) is not str) or first_name == ""):
            raise Exception("first_name is not a string")
        self.__first_name = first_name

    '''getters'''
    def get_id(self):
        return self.__first_name
    def get_eyes_color(self):
        return self.__eyes_color
    def get_genre(self):
        return self.__genre
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_first_name(self):
        return self.__first_name

    '''public methods'''
    def __str__(self):
        return self.__first_name + " " + self.last_name

    def is_male(self):
        if(self.__genre == "Male"):
            return True
        else:
            return False

    def age(self):
        present_date = [05, 20, 2016]
        if(self.__date_of_birth[0] >= present_date[0] and self.__date_of_birth[1] > present_date[1]):
            return (present_date[2] - 1) - self.__date_of_birth[2]
        else:
            return present_date[2] - self.__date_of_birth[2]

    '''operator overloading'''
    def __gt__(self, other):
        return self.age() > other.age()

    def __ge__(self, other):
        return self.age() >= other.age()

    def __lt__(self, other):
        return self.age() < other.age()

    def __le__(self, other):
        return self.age() <= other.age()

    def __eq__(self, other):
        return self.age() == other.age()

    def __ne__(self, other):
        return self.age() != other.age()

    '''public attributes'''
    def is_married_to(int):
        self.is_married_to = is_married_to


    '''json method'''
    def json(self):
        json_def = {
            'id': self.__id,
            'eyes_color': self.__eyes_color,
            'genre': self.__genre,
            'date_of_birth': self.__date_of_birth,
            'first_name': self.__first_name,
            'last_name': self.last_name,
            'is_married_to': self.is_married_to
            }
        return json_def

    '''setting all Person attributes by value from Hash (json_def) '''
    def load_from_json(self, json):
        if(type(json_def) is not dict):
            raise Exception("json is not valid")

        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.__last_name = json['last_name']
        self.is_married_to = json['is_married_to']

'''Subclasses Baby, Teenager, Adult, Senior'''
class Baby(Person):
    '''public methods'''
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        if(self.is_married_to != 0):
            return True
        else:
            return False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if(self.can_be_married() == False or p.can_be_married() == False):
            raise Exception("Can't be married")
        if(self.is_married_to != 0 or p.is_married_to != 0):
            raise Exception("Already married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if(p.__genre == "Male" and self.__genre == "Female"):
            self.last_name = p.last_name
        elif(p.__genre == "Female" and self.__genre == "Male"):
            p.last_name = self.last_name

class Teenager(Person):
    '''public methods'''
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        if(self.is_married_to != 0):
            return True
        else:
            return False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if(self.can_be_married() == False or p.can_be_married() == False):
            raise Exception("Can't be married")
        if(self.is_married_to != 0 or p.is_married_to != 0):
            raise Exception("Already married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if(p.__genre == "Male" and self.__genre == "Female"):
            self.last_name = p.last_name
        elif(p.__genre == "Female" and self.__genre == "Male"):
            p.last_name = self.last_name

class Adult(Person):
    '''public methods'''
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        if(self.is_married_to != 0):
            return True
        else:
            return False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if(self.can_be_married() == False or p.can_be_married() == False):
            raise Exception("Can't be married")
        if(self.is_married_to != 0 or p.is_married_to != 0):
            raise Exception("Already married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if(p.__genre == "Male" and self.__genre == "Female"):
            self.last_name = p.last_name
        elif(p.__genre == "Female" and self.__genre == "Male"):
            p.last_name = self.last_name

class Senior(Person):
    '''public methods'''
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        if(self.is_married_to != 0):
            return True
        else:
            return False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if(self.can_be_married() == False or p.can_be_married() == False):
            raise Exception("Can't be married")
        if(self.is_married_to != 0 or p.is_married_to != 0):
            raise Exception("Already married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if(p.__genre == "Male" and self.__genre == "Female"):
            self.last_name = p.last_name
        elif(p.__genre == "Female" and self.__genre == "Male"):
            p.last_name = self.last_name
