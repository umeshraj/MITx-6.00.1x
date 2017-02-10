#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:11:57 2017

@author: umesh
"""

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    outList = []
    for item in aList:
        if isinstance(item, list):
            outList += flatten(item)
        else:
             outList += [item]
    return outList


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#aList = [1, 2, 3, [4, 5]]
print(flatten(aList))