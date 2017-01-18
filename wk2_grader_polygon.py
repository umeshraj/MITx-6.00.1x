#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:59:41 2017

@author: umesh
"""

import math

def area(n, s):
    """ Function to compute the area of a polygon"""
    num = 0.25 * n * s**2
    den = math.tan(math.pi/n)
    area = num/den
    return round(area, ndigits=4)

def perimeter(n, s):
    perim = n*s
    return round(perim, ndigits=4)
