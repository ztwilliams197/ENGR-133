from PIL import Image
import os.path
import Functions as funct

def checkInFile(fileName):
    if(fileName[-3:] != 'jpg' or os.path.exists(fileName) == False):
        #if last three characters of input filename don't end with jpg, raise error
        print("Error: Entered invalid file name")
        return False
    else:
        return True

def checkOutFile(fileName):
    #if last three characters of output filename don't end with jpg, raise error
    if(fileName[-3:] != 'jpg'):
        print("Error: Entered invalid file name")
        return False
    else:
        return True

def main():
    isValid = False
    while(isValid == False):
        fName = input("Enter file name: ")
        isValid = checkInFile(fName)
        #checks if input filename is valid
    
    isValid = False
    while(isValid == False):
        oName = input("Enter output file name: ")
        isValid = checkOutFile(oName)
        #checks if output filename is valid
    
    selection = ""
    while(selection != "end"):
        print('Possible selections: ')
        print('grayscale')
        print('mirror')
        print('rotate90')
        print('rotate180')
        print('rotate270')
        print('smooth')
        print('end')
        #prints options for functions
        
        inF = Image.open(fName)
        outF = Image.new('RGB',inF.size)
        
        selection = input("Enter processing method: ")
        inputValid = True
        #asks for selection from user
        if(selection == 'grayscale'):
            outF = funct.grayscale(inF)
        elif(selection == 'mirror'):
            outF = funct.mirror(inF)
        elif(selection == 'rotate180'):
            outF = funct.rotate180(inF)
        elif(selection == 'rotate270'):
            outF = funct.rotate270(inF)
        elif(selection == 'rotate90'):
            outF = funct.rotate90(inF)
        elif(selection == 'smooth'):
            outF = funct.smooth(inF)
        elif(selection == 'end'):
            break
        else:
            print("Error: Entered invalid input")
            inputValid = False
        #if selection is invalid, raise error
        if(inputValid):
            outF.save(oName)
            outF.show()
        #shows new image
main()