#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:22:54 2017

@author: umesh
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for l in L:
        l.reverse()


#L = [[1, 2], [3, 4], [5, 6, 7]]
#deep_reverse(L)
#print(L)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)