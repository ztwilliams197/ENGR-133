#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Calculates the surface area of the solar panel required to produce enough
    power to drive the rover

Assignment Information
	Assignment:     Py2_ACT Task 1
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

# Calculates solar panel area
def solarPanelArea(power, irradiance, efficiency):
    return (power) / (irradiance * efficiency)

# Calculates distance rover travels
def distanceRover(speed, time):
    return speed * time * 3600

def main():
    speed = 1   #speed of rover
    time = 2    #time that rover travels for
    power = 100 #power that rover drains
    irradiance = 590    #solar irradiance
    efficiency = .25    #efficiency of solar panel
    
    print(f"Area: {solarPanelArea(power,irradiance,efficiency)} m^2")
    print(f"Distance: {distanceRover(speed,time)} cm")
    
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