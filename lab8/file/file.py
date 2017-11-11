def main():
    openFunc("in.txt")
	# myFile = "in.txt"
	#open(myFile)
def openFunc(f):
    
    inFile = open(f, "r")
   
    lineNum =0

    for line in inFile:  
        line = line.strip()
        print("Line",lineNum, "("+str(len(line))+" chars): "+line)
        lineNum +=1
    
    inFile.close()

if __name__ == "__main__":
    main()
