#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    else:
        i = sum(set(my_list))
        return i
