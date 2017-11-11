from sys import *

def main():

	if len(argv) < 2:
		print("Usage: python decode.py <image>")
		exit(1)
	if len(argv) ==2:
		name = argv[1]

	try:
		inFile = open(argv[1], 'r')
	except FileNotFoundError:
		print("Unable to open "+name)
		exit(1)
	except PermissionError:					   
		print("Unable to open "+name)
		exit(1)
	
	RGBList = makeRGBList(inFile)
	pixelList = makePixelList(RGBList) #list of lists[ [24, 3, 2], [3,3,2],... ]
	
	inFile = open(name, 'r')	

	writeNewPixels(name, inFile, pixelList) #wrote first 3 values in helper function, then pixels in writeNew function. Check the output!


def writeNewPixels(name, inFile, pixelList):
	
	inFile = open(name, 'r')
	listReqs = preset(inFile)

	myFile = open('decoded.ppm', 'w')

	myFile.write(listReqs[0]+'\n')
	size  = str(listReqs[1]+" "+listReqs[2])

	myFile.write(size+'\n')
	myFile.write(listReqs[3]+'\n')

	for p in pixelList:
		newP = decodePixel(p) #['200','200','200']
		for value in newP:
#changed
			#myFile.write(int(value+'\n'))
			myFile.write(value+'\n')
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

def decodePixel(p):
	r = int(p[0])
	newR  = r*10
	if newR > 255:
		newR = 255
	p[0] = str(newR)
	p[1] = str(newR)
	p[2] = str(newR)
	return p
			

if __name__ == "__main__":
	main()


