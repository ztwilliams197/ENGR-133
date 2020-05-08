#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Contains various functions in order to calculate newton's method

Assignment Information
	Assignment:     Py3_PA Functions
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

import math as m

def trim_leading_zeros(coefficients):
    for num in range(len(coefficients)):
        if(coefficients[0] != "0"):
            return coefficients
        del coefficients[0]
    
    return coefficients

def calc_derivative(function):
    derivative = []
    
    for index in range(len(function) - 1):
        derivative.append((len(function) - index - 1) * function[index])
    
    return derivative

def calc_funct(function,guess):
    num = 0
    
    for index in range(len(function)):
        num += m.pow(guess, len(function) - index - 1) * function[index]
     
    return num

def calc_new_guess(guess,function,derivative):
    return guess - (calc_funct(function,guess) / calc_funct(derivative,guess))


def newtons_method(guess,function,derivative,maxIter,tolerance,goal):
    count = maxIter + 1
    
    for i in range(maxIter + 1):
        if(calc_funct(derivative,guess) == 0):
            print("Error 2: Function of derivative resolved to value of 0")
            return
        print(f"   {i}: x = {guess:.4E} : f(x) = {calc_funct(function,guess):.4E} : f'(x) = {calc_funct(derivative,guess):.4E}")
        if(calc_funct(function,guess) < tolerance):
            count = i
            break
        guess = calc_new_guess(guess,function,derivative)
            
    if(count <= maxIter):
        print(f"A solution was estimated to be {guess}")
        print(f"Total number of iterations: {count}")
    else:
        print("Error 1: The max number of iterations was reached")
    return

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''