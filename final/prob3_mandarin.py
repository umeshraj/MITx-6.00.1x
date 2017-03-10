#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:56:36 2017

problem 3: Numbers in Mandarin follow 3 simple rules.
@author: umesh
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE

    # handle 0-10 by seeing if numbers are in dictionary
    mand_num = trans.get(us_num, None)

    if mand_num is None:  # number is > 10
        first_num = us_num[0]
        if  first_num == '1':  # 11-19
            first_str = 'shi'
            last_str = trans[us_num[1]]
            mand_num = ' '.join([first_str, last_str])
        else:  # 20-99
            first_str = trans[first_num]
            last_num = us_num[-1]
            if  last_num == '0':  # check if last digit is 0
                last_str = trans['10']
                mand_num = ' '.join([first_str, last_str])
            else:
                last_str = trans[last_num]
                mand_num = ' '.join([first_str, trans['10'], last_str])

    return mand_num


# tests can be run using py.test
def test_mandarin_0to10():
    assert convert_to_mandarin('0') == 'ling'

def test_mandarin_11to19():
    ans_dict = {'11': 'shi yi', '19': 'shi jiu', '16': 'shi liu'}
    for k, v in ans_dict.items():
        assert convert_to_mandarin(k) == v

def test_mandarin_end_nonzero():
    ans_dict = {'25': 'er shi wu', '98': 'jiu shi ba', '36': 'san shi liu'}
    for k, v in ans_dict.items():
        assert convert_to_mandarin(k) == v

def test_mandarin_end_zero():
    ans_dict = {'20': 'er shi', '90': 'jiu shi'}
    for k, v in ans_dict.items():
        assert convert_to_mandarin(k) == v
