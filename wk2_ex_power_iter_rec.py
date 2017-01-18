#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:30:06 2017

@author: umesh
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    res = 1
    for x in range(exp):
        res = res * base
    return res

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)