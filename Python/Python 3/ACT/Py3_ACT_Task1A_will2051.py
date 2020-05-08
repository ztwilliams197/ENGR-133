#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     e.g. Py1_ACT Task 1
	Author:         Name, login@purdue.edu
	Team ID:        ###-## (e.g. 001-14 for section 1 team 14)
	
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

def nthFibonacci(n):
    if(n == 2):
        return 1
    elif(n == 1 or n == 0):
        return 0
    else:
        return nthFibonacci(n-1) + nthFibonacci(n-2)

numTerms = int(input("Enter number of terms: "))
sequence = []

for n in range(1,numTerms + 1):
    sequence.append(nthFibonacci(n))

print(sequence)

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''