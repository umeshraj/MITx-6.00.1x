#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:59:02 2017

@author: umesh
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def poly_sum(x):
        K = len(L)-1
        fin_sum = 0
        for k, n_k in enumerate(L):
            fin_sum += n_k * x**(K-k)
        return fin_sum
    return poly_sum

def test_general_poly():
    assert general_poly([1, 2, 3, 4])(10) == 1234