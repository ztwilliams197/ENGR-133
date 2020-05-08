# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:01:11 2019

@author: ztwil
"""

#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Calculates points earned based on distance from target

Assignment Information
	Assignment:     Py2_CFU
	Author:         Zach Williams, will2051@purdue.edu
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
from math import sqrt,pow

# Uses x and y values to calculate distance from center of target
def distance_target():
    x = float(input("Input x distance in ft: "))
    y = float(input("Input y distance in ft: "))
    return sqrt(pow(x,2) + pow(y,2))

# Calculates distance from center of target
radius = distance_target()

# Determines color and score
if 12 >= radius > 8:
    print("Ball landed in the blue zone for 6 points.")
elif 8 >= radius > 4:
    print("Ball landed in the red zone for 8 points.")
elif 4 >= radius > 0:
    print("Ball landed in the yellow zone for 10 points.")
else:
    print("Ball landed outside the zone for 0 points.")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''