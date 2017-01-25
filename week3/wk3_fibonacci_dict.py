#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:00:22 2017

@author: umesh
"""

def fib(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def fib_dict(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_dict(n-1, d) + fib_dict(n-2, d)
        d[n] = ans
        return ans

n = 35
print('Using fib')
print(fib(n))


# Using dictionaries
d = {1: 1, 2:2}
print('Using fib_dict')
print(fib_dict(n, d))