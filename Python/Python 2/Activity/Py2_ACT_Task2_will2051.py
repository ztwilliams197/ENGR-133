#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes input for temperature and pressure and outputs if there is a danger,
    warning, or if it is normal as well as outputting if the temperature or 
    pressure are high or low

Assignment Information
	Assignment:     Py2_ACT Task 2
	Author:         Zachary Williams, will2051@purdue.edu
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
#inputs values of temperature and pressure
temp = int(input("Temperature: "))
pres = int(input("Pressure: "))

#Determines output based on temperature and pressure
if((temp > 1000) or (pres > 20)):
    print("Danger")
    if(temp > 1000):
        print("High Temperature")
    else:
        print("High Pressure")
elif((750 < temp < 1000) and (10 < pres < 20)):
    print("Normal")
else:
    print("Warning")
    if(temp < 750):
        print("Low Temperature")
    else:
        print("Low Pressure")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''