#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:36:21 2017

@author: umesh
"""

# Exercise: guess my number

print('Please think of a number between 0 and 100!')

low = 0
high = 100
guess = int((low+high)/2)

ans = ''
while ans != 'c':
    print('Is your secret number {0}?'.format(guess))
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if ans == 'l':
        low = guess
        guess = int((low+high)/2)
    elif ans == 'h':
        high = guess
        guess = int((low+high)/2)
    elif ans == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: {0}".format(guess))
