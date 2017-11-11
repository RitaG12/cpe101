def sumHundred(ints):
	#for i in range(9):
	for i in range(len(ints)):
		for j in range(i+1,len(ints)):
			sum= ints[i] + ints[j]
			#print("i ",i,"sum: ",sum)
			if sum == 100:
				return True
	return False
