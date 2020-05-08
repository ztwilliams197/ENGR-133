#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes input for level number, displays levels completed, and displays total
    number of candies crushed

Assignment Information
	Assignment:     Py3_CFU
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

level = abs(int(input("Please enter the level completed most recently: ")))
count = 0

print(f"The level is: {level}")
print("The levels that have been completed are:")

# Displays levels and adds candies
for num in range(1,level+1):
    print(level - num + 1)
    count += num

print(f"The total number of crushed candies is {count}")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''