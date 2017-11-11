from sys import *

def main():

	if len(argv) < 2 or len(argv) > 3:
		print("Usage: [-s] file_name") #no arguemnts 
		exit(1)
	
	if len(argv) == 3:
		if "-s" not in argv: #if the second or third  argument is not -s
			print("Usage: [-s] file_name")
			exit(1)
		if "-s" == argv[1]:
			fileName = argv[2]
		else:
			fileName = argv[1]
	
	if len(argv) ==2:
		fileName = argv[1]
    
    
	try: 
		inFile = open(fileName, 'r')
	except FileNotFoundError:
		print("Unable to open"+fileName) # + file name
		exit(1)
	except PermissionError:
		print("Unable to open"+fileName)
		exit(1)
	

	ints =0
	floats = 0
	other = 0
	sum = 0

	for line in inFile:
		splitted = line.split()
		for s in splitted:				
				if s.isdigit():
					ints+=1
					sum+= int(s)
				elif isFloat(s):
					floats+=1
					sum+= float(s)
				else:
					other+=1

	print("Ints:",ints)
	print("Floats:",floats)
	print("Other:", other)
	if "-s" in argv:
		print("Sum:", sum)

def isFloat(string):
	#work on this
	#if float(string):
		#return True
	#else:
		#pass
	try:
		float(string)
		return True
	except:
		return False


if __name__ == "__main__":
	main()









