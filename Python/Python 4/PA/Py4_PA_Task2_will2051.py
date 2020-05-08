#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Takes input of word and searches file to determine how often the word
    occurs in the file

Assignment Information
	Assignment:     Py4_PA Task 2
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

# Removes punctuation
def remPunct(word):
    for char in word:
        if(not char.isalnum()):
            word = word.replace(char,"")
    return word

# Changes list of lines into list of words
def changeToWords(lines):
    for line in range(len(lines)):
        for word in lines[0].split(' '):
            lines.append(remPunct(word))
        del lines[0]
    
    return lines

def main():
    fIn = open("Text_File.txt",'r')
    
    wordTest = input("Enter the search word: ")
    fText = fIn.readlines()
    
    fText = changeToWords(fText)
    
    count = 0
    for word in fText:
        if(word.lower() == wordTest.lower()):
            count += 1
            
    print(f"The search word occurred {100 * count / len(fText):.2f}% of the time")
    
    fIn.close()
    
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