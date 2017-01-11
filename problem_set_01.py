#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:54:22 2017

@author: umesh
"""

# %% Problem 1
""" count the number of vowels in a string s """
s = 'azcbobobegghakl'

num_vowels = 0
for char in s:
    if char in 'aeiou':
        num_vowels += 1
print('Number of vowels: {0}'.format(num_vowels))

# %% Problem 2
"""count the number of 'bobs' in a string s"""
s = 'bobobobobobobobobobob'
find_str = 'bob'

len_find_str = len('bob')
num_find = 0
for beg_idx in range(len(s)-len_find_str+1):
    if s[beg_idx:beg_idx+len_find_str] == 'bob':
        num_find += 1
print("Number of times bob occurs is: {0}".format(num_find))


# %% Problem 3:

""" Find the longest alphabetical substring"""
s = 'iugrqyqrzjjtulbo'

l = 0
r = l+1
cur_str = s[0]
max_str = s[0]

while r < len(s):
    if s[r] >= s[r-1]:
        cur_str = s[l:r+1]
        r += 1
    else:
        if len(cur_str) > len(max_str):
            max_str = cur_str
        l = r
        r = l+1

if len(cur_str) > len(max_str):
    max_str = cur_str
print('Longest substring in alphabetical order is: {0}'.format(max_str))
