# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 01:50:42 2016

@author: Mabele
"""

import turtle

#prompt user to enter two inputs
x1, y1 =eval(raw_input('Enter x1 and y1 for point 1:'))
x2, y2 =eval(raw_input('Enter x2 and y2 for point 1:'))

distance = ((x1-x2)** 2 +(y1-y2)** 2) ** 0.5

#display two points and the connecting line
turtle.penup()
turtle.goto(x1,y1) #move to (x1,y1)
turtle.pendown()
turtle.write('Point 1')
turtle.goto(x2,y2)  #move to (x2,y2)
turtle.write('Point 2')

turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.write(distance)
turtle.done()
