from PIL import Image

def grayscale(inF):
    #grays image
    width, height = inF.size
    outF = Image.new('RGB',inF.size)
    #replaces pixel values
    for pixX in range(width):
        for pixY in range(height):
            r,g,b = inF.getpixel((pixX,pixY))
            gray = int(round(r * .3 + g * .59 + b * .11,0))
            outF.putpixel((pixX,pixY),(gray,gray,gray))
    return outF        

def smooth(inF):
    #smooth edges and spots in a jpg and save it 
    outF = Image.new('RGB',inF.size)
    width, height = inF.size
    for pixX in range(0, width):
        for pixY in range(0, height):
            rNew,bNew,gNew = 0,0,0
            rangeStartX = -1
            rangeStartY = -1
            if(pixX == 0):
                rangeStartX = 0
            if(pixY == 0):
                rangeStartY = 0
            for x in range(rangeStartX,2):
                for y in range(rangeStartY,2):
                    try:
                        r,b,g = inF.getpixel((pixX + x,pixY + y))
                    except IndexError:
                        r,b,g = 0,0,0
                    else:
                        rNew += round(r/9)
                        bNew += round(b/9)
                        gNew += round(g/9)
            outF.putpixel((pixX,pixY),(rNew,bNew,gNew))
    return outF

def mirror(inF):
    #Flips a jpg image over the yaxis and saves as a new jpg 
    width, height = inF.size
    outF = Image.new('RGB',inF.size)
    for row in range(height):
        for column in range(round(int(width/2)) + 1):
            temp = inF.getpixel((column,row))
            outF.putpixel((column,row),inF.getpixel((-column,row)))
            outF.putpixel((-column,row),temp)
    return outF

def rotate90(inF):
    #Rotate a jpg image 90 degrees to the left and save it as a new jpg
    width,height = inF.size
    outF = Image.new('RGB', (height,width), color ='red')
    a=0
    #Take a vertical vector from the pixel matrix and save as l. After, insert 
    #vector into new image rotated 90 degrees to the left
    l = [[0 for x in range(0,3)] for y in range(0, width)]
    for i in range(0,height):
        b=width-1
        for x in range(0,width):
            l[x] = tuple(inF.getpixel((x,i)))
        for x in range(0,len(l)):
            outF.putpixel((a,(b)), l[x])
            b-=1
        a+=1
    return outF

def rotate180(inF):
    #Flips a jpg image 180 degrees and saves as a new jpg 
    width,height = inF.size
    outF = inF
    a=0
    #Take a vertical vector from the pixel matrix and save as l. After, insert 
    #vector into new image upside down
    for i in range(0,width):
        b=height-1
        l = [[0 for x in range(0,4)] for y in range(height)]
        for x in range(0,height):
            l[x] = tuple(inF.getpixel((i,x)))
        for x in range(0,len(l)):
            outF.putpixel((a,b), l[x])
            b-=1
        a+=1
    return outF
     
def rotate270(inF):
    #Rotates a jpg image 270 degrees to the left and saves as a new jpg 
    #Calls rotate90 3 times
    outF = Image.new('RGB',inF.size)
    outF = rotate90(inF)
    outF = rotate90(outF)
    outF = rotate90(outF)
    return outF