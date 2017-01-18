#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:56:17 2017

@author: umesh
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    min_val = min(a, b)
    for gcd in range(min_val, 0, -1):
        if a%gcd == 0 and b%gcd == 0:
            break
    return gcd

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

#print(gcdIter(2, 12))
#print(gcdIter(6, 12))
#print(gcdIter(9, 12))
#print(gcdIter(17, 12))

print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))
