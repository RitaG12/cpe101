from sys import *

def main():
	
	if len(argv) < 2:
		print("Usage: python blur.py <image> <OPTIONAL:reach>")
		exit(1)
	elif len(argv) < 3:
		reach = 4
	else:
		reach = int(argv[2])
		
	try:
		inFile = open(argv[1], 'r')
	except FileNotFoundError:
		print("Unable to open "+str(argv[1]))
	
	
	returned = makeRGBList(argv[1]) # [200,300, [234,345,223,233,...]]
	rgbList = returned[0] #all values
	pixelList = groups_of_3(rgbList)
	width = int(returned[1])
	height = int(returned[2])
	inFile = open(argv[1], 'r')

	twoDList = make2DList(width, height, pixelList)
	writeFile(argv[1], inFile, twoDList, reach, width, height) #remember to do exception thingy

def writeFile(name, inFile, twoDList, reach, width, height):
	inFile = open(name, 'r')
	listReqs = header(inFile)

	myFile = open('blurred.ppm', 'w')

	myFile.write(listReqs[0] + '\n')
	size = str(listReqs[1]+" "+listReqs[2])
	myFile.write(size+'\n')
	myFile.write(listReqs[3]+'\n')
	
	for r in range(height):
		for c in range(width):
			b = box(twoDList, r, c, reach, width, height)
			p = manipulatePixel(b)
			strP = ' '.join(p)
			myFile.write(strP+'\n')
	myFile.close()


def box(twoDList, x,y, reach, width, height): #makes a list of the pixels that are in the box
	box = [ ]
	for R in range((x-reach), (x+reach+1)):
		while R < 0:
			R+=1
		while R >=  height:
			R-=1
		#low r = ...while....make function?. high r. lowc, highc
		for C in range((y-reach), (y+reach+1)):
			while C < 0:
				C+=1
			while C >= width:
				C-=1
			box.append(twoDList[R][C])
	return box #list of pixels [ [3,3,3] , [23,45,44]..]

def manipulatePixel(box): #averages rgb and returns a pixel strin g
	sumR = 0
	sumG = 0
	sumB = 0
	for pixel in box:
		sumR += int(pixel[0])
		sumG += int(pixel[1])
		sumB += int(pixel[2])
	r = int(sumR/(len(box)))
	g = int(sumG/(len(box)))
	b = int(sumB/(len(box)))
	pix = [str(r),str(g),str(b)]
	return pix

def make2DList(w, h, pixelList):
	twoDList = [ ]
	count =0
	for r in range(int(h)):
		row = [ ]
		for c in range(int(w)):
			row.append(pixelList[count])
			count+=1
		twoDList.append(row)
	return twoDList


def makeRGBList(f):
	list = []
	inFile = open(f, 'r')
	for line in inFile:
		splitted = line.split()
		for s in splitted:
			list.append(s)
	width = list[1]
	height = list[2]
	list = list[4:] #get all rgb values
	return [list, width, height]

def header(inFile):
	l = [ ]
	counter = 0
	for line in inFile:
		splitted = line.split()
		for s in splitted:
			l.append(s)
			counter +=1
		if counter > 5:
			break
	l = l[0:4]
	return l



def groups_of_3(list):
	return [list[i:i+3] for i in range(0,len(list), 3)]

if __name__ == "__main__":
	main()
