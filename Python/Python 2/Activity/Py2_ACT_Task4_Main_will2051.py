#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Calculates area of a circle and outputs radius and area

Assignment Information
	Assignment:     Py2_ACT Task 4
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

import Areas

# Calculates and outputs area of circle with radius radius
radius = 5
A = Areas.circArea(radius)
print(A)
print(radius)

# Calculates and outputs Area of rectangle with side lengths side1 and side2
side1 = 3
side2 = 6
A2 = Areas.rectArea(side1,side2)
print(A2)

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
