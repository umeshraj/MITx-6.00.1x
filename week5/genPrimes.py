#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:00:42 2017

@author: umesh
"""

def isPrime(num):
    is_prime = True
    for div in range(2, num//2+1):
        if num%div == 0:
            return False
    return is_prime

def genPrimes():
    """ Generator to make primes"""
    n = 1
    while True:
        n += 1
        if isPrime(n):
            yield(n)


def genPrimes2():
    """ Generator to make primes"""
    primes = []
    last = 1
    while True:
        last += 1
        for p in primes:
            if last%p == 0:
                break
        else:
            primes.append(last)
            yield(last)