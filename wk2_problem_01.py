#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:25:23 2017

@author: umesh
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month_int_rate = annualInterestRate/12

# %% Problem 01
for month in range(1, 13):
    min_payment = balance * monthlyPaymentRate
    month_unpaid_bal = balance - min_payment
    balance = month_unpaid_bal + month_int_rate*month_unpaid_bal
    #print('Month {0} Remaining balance: {1:0.2f}'.format(month, balance))

print('Remaining balance: {0:0.2f}'.format(balance))

# %% Problem 02

def annual_balance(balance, min_payment, annualInterestRate):
    month_int_rate = annualInterestRate/12
    for month in range(1, 13):
        month_unpaid_bal = balance - min_payment
        balance = month_unpaid_bal + month_int_rate*month_unpaid_bal
    return balance

balance = 3926
annualInterestRate = 0.2

min_payment = 0
test_balance = annual_balance(balance, min_payment, annualInterestRate)
while test_balance > 0:
    min_payment += 10
    test_balance = annual_balance(balance, min_payment, annualInterestRate)
print('Lowest  Payment {0}'.format(min_payment))

# %% Problem 03 - payment with bisection

balance = 999999
annualInterestRate = 0.18

month_int_rate = annualInterestRate/12
low_bound = balance / 12
up_bound = (balance * (1 + month_int_rate)**12) / 12.0

min_payment = 0.5*(low_bound + up_bound)
test_balance = annual_balance(balance, min_payment, annualInterestRate)
#while test_balance > 0:
while abs(test_balance) > 0.01:
     if test_balance > 0:
         low_bound = min_payment
     else:
         up_bound = min_payment
     min_payment = 0.5*(low_bound + up_bound)
     test_balance = annual_balance(balance, min_payment, annualInterestRate)
print('Lowest  Payment {0:.2f}'.format(min_payment))
