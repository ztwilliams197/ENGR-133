#!/usr/bin/env python3
'''
===============================================================================
ENGR 133 Program Description 
	Generates two random numbers from a given seed and adding the two values
    as decimals and fractions

Assignment Information
	Assignment:     Py1_PA Task 1
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
import random
from fractions import Fraction

#User input to determine random seed
random.seed(int(input("Enter the seed:")))

num1 = random.uniform(0,10) #First generated value
num2 = random.uniform(0,10) #Second generated value
roundNum1 = round(num1,1) #num1 rounded to the nearest 10th place
roundNum2 = round(num2,1) #num2 rounded to the nearest 10th place

#Prints out num1 and num2 as well as the sum of both the decimals and fractions
print(f"First Random Number : {num1:.4}")
print(f"Second Random Number: {num2:.4}")
print(f"Sum from decimals   : {roundNum1} + {roundNum2} = {round(num1 + num2,1)}")
print(f"Sum from fractions  : {Fraction(roundNum1).limit_denominator(10)} + {Fraction(roundNum2).limit_denominator(10)} = {Fraction(roundNum1).limit_denominator(10) + Fraction(roundNum2).limit_denominator(10)}")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''