#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes target value as input and iterates through summation loop until target
    value is exceeded.

Assignment Information
	Assignment:     Py4_CFU
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
def sumLoop(target):
    sum = 0
    count = 1
    while(sum <= target):
        sum += 1/count
        count += 1
        print(f"{sum:.3f}")

target = float(input("Input the target value: "))

print(f"For a target value of {target}")
print("The summation of values at each iteration are:")
sumLoop(target)

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''