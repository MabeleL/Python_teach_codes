# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 01:27:54 2016

@author: Mabele
"""
#prompt the user for input
purchaseAmount = eval(raw_input('Enter purchase amount:'))

#compute the sales tax
tax = purchaseAmount * 0.06

#Display tax amount with two digits after decimal amount
print 'Sales tax is', int ((tax * 100)/100.0)