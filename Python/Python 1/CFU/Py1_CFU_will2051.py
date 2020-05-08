#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py1_CFU
	Author:         Zachary Williams, will2051@purdue.edu
	Team ID:        001-01
	
Contributor:    Name, login@purdue [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
from math import pi, pow, sqrt

#Radius, height, and calculated surface area of cone
r = 3
h = 4
surfArea = (pi * pow(r,2)) + (pi * r * sqrt(pow(r,2) + pow(h,2)))

#Outputs radius, height, and surface area
print(f"Given a radius of {r}[cm] and a height of {h}[cm], the surface area of a cone is {surfArea}[cm^2]")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''