#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:38:55 2017

@author: umesh
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    inter_dict = {}
    diff_dict = {}
    for k1 in d1.keys():
        if k1 in d2:  # key1 is in dict2
            inter_dict[k1] = f(d1[k1], d2[k1])
        else: # key1 is not in dict2
            diff_dict[k1] = d1[k1]

    # add all keys from d2 that are not in d1
    for k2 in d2:
        if k2 not in d1:
            diff_dict[k2] = d2[k2]

    return(inter_dict, diff_dict)

# example 1
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
f = lambda a, b : a + b

# example 2
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
f = lambda a, b: a > b


print(dict_interdiff(d1, d2))