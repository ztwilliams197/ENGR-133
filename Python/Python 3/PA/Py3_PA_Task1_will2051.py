#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes user input and uses newton's method in order to calculate the solution

Assignment Information
	Assignment:     Py3_PA Main
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
import Py3_PA_Task1_Functions_will2051 as func

function = input("Enter Coefficients: ").split(" ")
goal = float(input("Enter Goal Value: "))
initial = float(input("Enter Initial Guess: "))
tolerance = float(input("Enter Tolerance: "))
maxIter = int(input("Enter Maximum Allowed Iterations: "))

function = [float(i) for i in func.trim_leading_zeros(function)]
function[-1] -= goal
derivative = func.calc_derivative(function)

print(f"The polynomial entered is of order: {len(function) - 1}")
func.newtons_method(initial,function,derivative,maxIter,tolerance,goal)

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''