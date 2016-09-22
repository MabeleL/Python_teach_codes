# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 01:38:54 2016

@author: Mabele
"""
#Enter annual interest rate as a percentage 
annualInterestRate =eval(raw_input('Enter annual interest rate e.g. 7.25:'))
monthlyInterestRate = annualInterestRate/1200

#Enter number of years
numberOfYears = eval(raw_input('Enter number of years as an integer, e.g. 5: '))

#Enter Loan Amount 
loanAmount = eval(raw_input('Enter loan amount, e.g. 120000.95: '))

#Calculate Payment
monthlyPayment = loanAmount * monthlyInterestRate /(1-1 /(1+monthlyInterestRate)** (numberOfYears * 12))

totalPayment = monthlyPayment * numberOfYears * 12

#Display results
print 'The monthly payment is', int((monthlyPayment * 100)/100)
print 'The total payment is', int((totalPayment * 100) /100)
