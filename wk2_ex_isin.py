#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:10:39 2017

@author: umesh
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    else:
        mid = len(aStr)//2
        if aStr[mid] == char:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[0:mid])
        elif char > aStr[mid]:
            return isIn(char, aStr[mid+1:])

print(isIn('a', 'apqrstvw'))