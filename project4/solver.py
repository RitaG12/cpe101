from solverFuncs import *

def main():
   #makePuzzle("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")	
	#makePuzzle("EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR")
	#printPuzzle("EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR")


	stringCharacters = str(input())
	strWord = str(input())
	#print(stringCharacters)

	puzzle = makePuzzle(stringCharacters)
	solList = [ ] 

	listWords = strWord.split()
	#print(listWords)


	for word in listWords:
			Forward = forward(word, puzzle)
			Backward = backward(word, puzzle)
			Up  = up(word, puzzle)
			Down = down(word, puzzle)

			if Forward[0] == True:
				solList.append(word+": (FORWARD) row: "+str(Forward[1])+" column: "+str( Forward[2]))
				#print("Forward Branch")
				#print(solList)

			elif Backward[0] ==True:
				solList.append(word+": (BACKWARD) row: "+str(Backward[1])+" column: "+str( Backward[2]))
			elif Up[0] ==True:
			   solList.append(word+": (UP) row: "+str(Up[1])+ " column: "+str(Up[2]))
			elif Down[0] ==True:
				solList.append(word+": (DOWN) row: "+str(Down[1])+" column: "+str( Down[2]))
			else:
				#print("ELSEEEEE not found. word:"+word)
				solList.append(word+": word not found")

	print("Puzzle:" )
	print()
	printPuzzle(puzzle)
	#print()
	for i in solList:
		print(i)

		
if __name__ == "__main__":
	main()

