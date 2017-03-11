#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:34:51 2017
Problem 4: longest monotonic sequence
@author: umesh
"""


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # Your code here
    inc_beg, inc_end = get_longest_run_index(L, monotone_type='incr')
    dec_beg, dec_end = get_longest_run_index(L, monotone_type='decr')

    # increasing sequence
    inc_seq = L[inc_beg:inc_end+1]
    dec_seq = L[dec_beg:dec_end+1]

    inc_len = len(inc_seq)
    dec_len = len(dec_seq)

    if inc_len > dec_len:
        fin_seq = inc_seq
    elif inc_len < dec_len:
        fin_seq = dec_seq
    else:  # same length
        # pick the one that occured first
        if inc_beg < dec_beg:
            fin_seq = inc_seq
        else:
            fin_seq = dec_seq

    return sum(fin_seq)


def chk_criterion(num_b, num_a, monotone_type):
    """ check if comparison is greater/equal to or lesser/equal
    Args:
        num_b (float)

    """
    if monotone_type == 'incr':
        return num_b >= num_a
    elif monotone_type == 'decr':
        return num_b <= num_a


def get_longest_run_index(L, monotone_type):
    """ Find the index of the longest monotone seq of type monotone_type

    Args:
        L (:obj: `float`): List of numbers
        monotone_type (str): 'incr' or 'decr' monotone
    Returns:
        max_sum (float): Sum of maximum run
    """
    beg_idx = 0
    end_idx = 1
    cur_len = 1
    max_len = 1
    max_beg_idx = beg_idx
    max_end_idx = end_idx

    while end_idx < len(L):
        #if L[end_idx] >= L[end_idx-1]:  # next element is monotonic increase
        if chk_criterion(L[end_idx], L[end_idx-1], monotone_type):  # next element is monotonic increase
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                max_beg_idx = beg_idx
                max_end_idx = end_idx
        else:  # next element is not monotonic increase
            beg_idx = end_idx
            cur_len = 1

        end_idx += 1  # increment the right side

    # if end_idx is outside the range, cap it
    #max_end_idx = min(max_end_idx, len(L)-1)

    return (max_beg_idx, max_end_idx)


# tests to run using py.test

def test_get_longest_run_index():
    L1 = [1, 2, 3]
    assert get_longest_run_index(L1, 'incr') == (0, 2)
    L2 = [1, 1, 1]
    assert get_longest_run_index(L2, 'incr') == (0, 2)
    L3 = [3, 2, 1]
    assert get_longest_run_index(L3, 'incr') == (0, 1)
    L4 = [3, 2, 1, 9]
    assert get_longest_run_index(L4, 'incr') == (2, 3)
    L5 = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
    assert get_longest_run_index(L5, 'incr') == (4, 8)

    # test decreasing
    L1 = [1, 2, 3]
    assert get_longest_run_index(L1, 'decr') == (0, 1)
    L2 = [1, 1, 1]
    assert get_longest_run_index(L2, 'decr') == (0, 2)
    L3 = [3, 2, 1]
    assert get_longest_run_index(L3, 'decr') == (0, 2)
    L4 = [3, 2, 1, 9]
    assert get_longest_run_index(L4, 'decr') == (0, 2)
    L5 = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
    assert get_longest_run_index(L5, 'decr') == (0, 2)

def test_longest_run():
    L1 = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
    assert longest_run(L1) == 26
    L2 = [5, 4, 10]
    assert longest_run(L2) == 9