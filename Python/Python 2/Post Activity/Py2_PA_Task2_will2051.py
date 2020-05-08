#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes inputs of Temp and Molar Volume and solves for current pressure
    and calculates minimum temperature change to be within the safe range

Assignment Information
	Assignment:     Py2_PA Task 2
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
from math import pow

# Calculates pressure
def calcPressure(R,T,a,b,V):
    return (R * T) / (V - b) - a / pow(V,2)
    
# Calculates temperature
def calcTemp(R,P,a,b,V):
    return (P + a / pow(V,2)) * (V - b) / R  
    
# Outputs initial values of problem
def printInitVals(V,t,a,b,p):
    print("Initial conditions:")
    print(f"Molar volume = {V:.1f} [L/mol]")
    print(f"Initial temperature = {t:.1f} [K]")
    print(f"Parameter a = {a} [L^2*atm/(mol^2)]")
    print(f"Parameter b = {b} [L/mol]")
    print(f"Resulting pressure = {p:.4f} [atm]")
    
# Outputs temperature changes
def printTempChange(temp, tempChange, press):
    print(f"Required temperature increment for in-range pressure = {tempChange:.2f} [K]")
    print(f"New temperature = {temp:.2f} [K]")
    print(f"New pressure = {press:.2f} [atm]")

def main():
    # Takes input for initial temp and molar volume
    tempI = float(input("Input Initial Temperature in Kelvin: "))
    volMol = float(input("Input molar volume in L/mol: "))
    a = 6.49
    b = .0562
    R = .0820573661
    
    # Tests if pressure calculation will work 
    if(volMol == b or volMol == 0):
        print("Error: Calculation resolves with 0 in denominator")
    else:
        pressInit = calcPressure(R,tempI,a,b,volMol)
        
        printInitVals(volMol, tempI, a, b, pressInit)
        
        # Tests if temperature needs to be changed and calculates change
        if(pressInit > 1.2):
            tempF = calcTemp(R, 1.2, a, b, volMol)
            tempDec = tempF - tempI
            printTempChange(tempF,tempDec,1.2)
        elif(pressInit < 1.1):
            tempF = calcTemp(R, 1.1, a, b, volMol)
            tempInc = tempF - tempI
            printTempChange(tempF,tempInc,1.1)
    
main()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''