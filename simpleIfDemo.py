# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 02:40:06 2016

@author: Mabele
"""

number = eval(raw_input('Enter an integer: '))

if number %5 == 0:
    print 'HiFive'
    
if number %2 == 0:
    print 'HiEven'
    
else: print 'Try a divisibility of 2 or 5'