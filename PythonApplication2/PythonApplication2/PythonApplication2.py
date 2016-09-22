#Working with Named Constants

#Assign a radius

radius = 20    #radius is 20

#compute area
PI = 3.14159

area = radius * radius * PI

#Display results
print'The area of the circle of radius', radius, 'is', area


#Numeric operators

#prompt the user to enter input
seconds = eval(raw_input('Enter an integer for seconds: '))

#Get minutes and remaining seconds
minutes = seconds // 60    
remainingSeconds = seconds % 60  #seconds remaining
print seconds, 'seconds is', minutes, 'minutes and', remainingSeconds, 'seconds'