#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Calculates area using inputs

Assignment Information
	Assignment:     Py2_ACT Task 4 Area
	Author:         Zachary Williams, will2051@purdue.edu
	Team ID:        001-01 (e.g. 001-14 for section 1 team 14)
	
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
from math import pi

#Calculates the area of a circle using radius
def circArea(R):
    global area
    area = pi * R**2
    return area

#Calculates the area of a rectangle using side lengths
def rectArea(S1, S2):
    area = S1 * S2
    return area

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''