from sys import *
import math


def main():

	if len(argv) !=5:
		print("Usage: python fade.py <image> <row> <column> <radius>")
		exit(1)
	else:
		name = argv[1]
	
	try:
		inFile = open(name, 'r')
	except FileNotFoundError:
		print("Unable to open "+name)
	except PermissionError:					   
		print("Unable to open "+name)
	
	row = (argv[2])
	col = (argv[3])
	radius = (argv[4])
	
	RGBList = makeRGBList(inFile)
	pixelList = makePixelList(RGBList) #list of lists[ [24, 3, 2], [3,3,2],... ]

	inFile = open(name, 'r')	
	#print(decodePixel([10,20,30], 10,4, row, col, radius))
	writeNewPixels(name, inFile, pixelList, row, col, radius) #wrote first 3 values in helper function, then pixels in writeNew function. Check the output!
	

def writeNewPixels(name, inFile, pixelList, row, col, radius):
	
	inFile = open(name, 'r')
	listReqs = preset(inFile)

	myFile = open('faded.ppm', 'w')

	myFile.write(listReqs[0]+'\n')
	size  = str(listReqs[1]+" "+listReqs[2])

	myFile.write(size+'\n')
	myFile.write(listReqs[3]+'\n')

	pos = 0
	for R in range(int(listReqs[2])): #height
		for C in range(int(listReqs[1])): #width
# pix is ['23','23', 23']
			pix = decodePixel(pixelList[pos], R, C, row, col, radius)
			sPix = ' '.join(pix)
			myFile.write(sPix + '\n') #"23 23 23" writes as one line into file
			pos+=1
	myFile.close()

def preset(inFile):
	l = [ ]
	for line in inFile:
		splitted = line.split()
		for s in splitted:
			l.append(s)
	l = l[0:4] #4 values
	return l


def makeRGBList(inFile):
	bigList = [ ]
	for line in inFile:
		splitted = line.split()
		for s in splitted:
			bigList.append(line)
	bigList = bigList[4:] #4 pixels
	return bigList

def makePixelList(RGBList):
	return groups_of_3(RGBList)

def groups_of_3(list):
   return [list[i:i+3] for i in range(0, len(list), 3)]

def decodePixel(p,r, c, row, col, radius):
	distance = math.sqrt((r-int(row))**2+(c-int(col))**2)
	scale = (int(radius)- distance)/int(radius)
	if scale < .2:
		scale = .2

	for i in range(3):
		x  = int((int(p[i]))*scale)
		if	x > 225:
			p[i] = 225
		else:
			p[i] = x
		p[i] = str(p[i])	
	return p
			

if __name__ == "__main__":
	main()



