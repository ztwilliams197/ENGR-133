#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes input for a, b, and c, and determines

Assignment Information
	Assignment:     Py2_ACT Task 5 Main
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

from Py2_ACT_Task5_Discriminant_will2051 import discriminant

print("The inputs are:")
a,b,c = input("a, b, c: ").split()

a = int(a)
b = int(b)
c = int(c)
disc = discriminant(a,b,c)

print(f"No real roots: {disc < 0}")
print(f"One real root: {disc == 0}")
print(f"Two real roots: {disc > 0}")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''