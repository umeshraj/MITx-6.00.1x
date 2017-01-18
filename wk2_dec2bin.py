#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:31:05 2017

@author: umesh
"""

num = 0
res = ''
if num == 0:
    res = '0'

while num > 0:
    res = str(num % 2) + res
    num = num//2
print(res)