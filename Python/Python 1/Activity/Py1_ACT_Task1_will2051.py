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

sideA = 12  #Length for side A
sideB = 4   #Length for side B
angle = 30  #Angle A

#Calculates area using side lengths and angle
area = 1/2 * sideA * sideB * math.sin(math.radians(30))

#Outputs area, side lengths, and angle
print(f"The area of a triangle is {area}[cm^2] for a given length of {sideA}[cm] and {sideB}[cm] with the angle of 30 [degrees] in between.")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''