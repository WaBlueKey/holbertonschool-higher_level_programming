#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    else:
        return max(my_dict, key=my_dict.get)
