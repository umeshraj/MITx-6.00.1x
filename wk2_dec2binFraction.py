#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:31:05 2017

@author: umesh
"""

x = float(input('Enter a number between 0 and 1: '))

# multiply by powers of two to get an int
p = 0
while (2**p * x)%1 != 0:
    rem = 2**p * x - int(2**p * x)
    print('remainder: {0}'.format(rem))
    p += 1

num = int(x * (2**p))
print(num)

res = ''
if num == 0:
    res = '0'

while num > 0:
    res = str(num % 2) + res
    num = num//2

#print(res)

for i in range(p-len(res)):
    res = '0' + res

print(res)

