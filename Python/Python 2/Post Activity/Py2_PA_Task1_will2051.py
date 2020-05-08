#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes inputs for theta1 and n1 and outputs calculated values for theta2
    d3 and critTheta    

Assignment Information
	Assignment:     Py2_PA Task 1
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
import math as ma


theta1 = float(input("Input incoming angle [degrees]: "))
n1 = float(input("Input refractive index medium 1 [unitless]: "))
n2 = 1.3
d1 = 5.3
d2 = 7.6

# Calculates leaving angle using indices of refraction and incoming angle
def calcTheta2(n1, n2, theta1):
    return ma.degrees(ma.asin(n1 * ma.sin(ma.radians(theta1)) / n2))

# Calculates ending distance of light ray using d1, d2, and angles
def calcD3(d1, theta1, d2, theta2):
    return d1 * ma.tan(ma.radians(theta1)) + d2 * ma.tan(ma.radians(theta2))

# Calculates critical angle using indices of refraction
def calcCritTheta(n1, n2):
    if(n1 > n2):
        return ma.degrees(ma.asin(n2 / n1))
    else:
        return ma.degrees(ma.asin(n1 / n2))
    
# Calls functions to calculate theta2, d3, and critTheta
theta2 = calcTheta2(n1,n2,theta1)
d3 = calcD3(d1,theta1,d2,theta2)
critTheta = calcCritTheta(n1,n2)

# Outputs theta2, d3, and critTheta
print(f"There is a refraction with a leaving angle of {theta2:.1f} degrees.")
print(f"The ending distance for the light ray is {d3:.1f}cm.")
print(f"For these two media, the critical angle is {critTheta:.1f} degrees.")
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''