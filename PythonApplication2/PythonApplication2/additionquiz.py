# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 02:28:07 2016

@author: Mabele
"""

import random

#generate random numbers

number1 = random.randint(0,9)
number2 = random.randint(0,9)

#prompt user to enter the answer
answer = eval(raw_input('What is '+str(number1)+ '+' +str(number2)+'?'))

#display result
print number1, '+', number2, '=', answer, 'is', number1+number2 == answer