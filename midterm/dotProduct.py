#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:21:08 2017

@author: umesh
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    sum = 0
    for a, b in zip(listA, listB):
        sum += a*b
    return sum

listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA,listB))