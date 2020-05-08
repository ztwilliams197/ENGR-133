#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes resistance input and calculates and displays equivalent resistances
    for the resistances in series and parallel

Assignment Information
	Assignment:     Py1_PA Task 2
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
import math

formatSpaces = 11

#Takes input for ohms
r1 = round(float(input("Input the first resistance value [ohm]:")),1)
r2 = round(math.sqrt(5.6) * math.pi,1)

#Calculates equivalent resistances
parEqRes = round(1/(1/r1 + 1/r2),1)
serEqRes = round(r1 + r2,1)

#Calculates and outputs equivalent resistances
print(f"{'Type':formatSpaces}{'First':formatSpaces}{'Second':formatSpaces}Equivalent Resistance")
print(f"{'Parallel':formatSpaces}{str(r1) + ' ohms':formatSpaces}{str(r2) + ' ohms':formatSpaces}{str(parEqRes) + ' ohms'}")
print(f"{'Series':formatSpaces}{str(r1) + ' ohms':formatSpaces}{str(r2) + ' ohms':formatSpaces}{str(serEqRes) + ' ohms'}")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''