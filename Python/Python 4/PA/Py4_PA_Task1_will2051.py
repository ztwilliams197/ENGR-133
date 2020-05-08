# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes input for file names and copies input file into output file with step
    numbers

Assignment Information
	Assignment:     Py4_PA Task 1
	Author:         Zach Williams, will2051@purdue.edu
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

inFile = input("Enter the filename of the input file: ")
outFile = input("Enter the filename of the output file: ")

fIn = open(inFile,'r')
fOut = open(outFile,'w')

lines = fIn.readlines()

for i in range(1,len(lines) + 1):
    fOut.write(f"Step {i}: {lines[i-1]}")
    
fIn.close()
fOut.close()
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''