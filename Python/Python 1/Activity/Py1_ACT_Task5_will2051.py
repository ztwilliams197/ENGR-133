#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py1_ACT Task 1
	Author:         Zachary Williams, will2051@purdue.edu
	Team ID:        001-01
	
Contributor:    Mark Paral, mparal@purdue.edu
                Malcolm MacDonell, mmacdone@purdue.edu
                Calder Lowenthal, clowent@purdue.edu
	My contributor(s) helped me:	
	[X] understand the assignment expectations without
		telling me how they will approach it.
	[X] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import math

#Takes input for radius in cm
radius = int(input("Radius[cm]: "))

#Calculates area in cm^2 using pi and radius
area = math.pi * radius ** 2

#Displays the area of the circle
print(f"The area of the circle is {area} [cm^2]")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''