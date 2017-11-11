def forward(word, puzzle): #check all rows if word is forward
	for r in range(10):
		result =checkForward(puzzle[r], word)
		if result[0]==True:
			return [True,r, result[1]]
	return [False, False, False]


def backward(word, puzzle):
	for r in range(10):
		result = checkBackward(puzzle[r], word)
		if result[0] == True:
			return [True, r, 9-result[1]]
	return [False, -1,-1]


def up(word, puzzle):
	for c in range(10):
		result = checkUp(puzzle, c, word)
		if result[0] ==True:
			return [True, 9-result[1], c]  
	return [False, -1,-1]

def down(word, puzzle):
	for c in range(10):
		result = checkDown(puzzle, c, word)
		if result[0] ==True:
			return[True, result[1], c]
	return [False, -1,-1]

def checkForward(row, word): #works
		joinedRow = "".join(row)
		if word in joinedRow:
			#description = word+": (FORWARD) row: "+r+"column: "+
			#solution(description)
			
			return [True, joinedRow.index(word)]# column
		else:
			return [False, False]

def checkBackward(row, word): #works, right to left
    myRow = makeReversedRow(row) #reverse the row using a helper method

    return checkForward(myRow, word) #use the forward method to check

def makeReversedRow(row):#works
    reversed = [ ]
    for i in range(9,-1,-1):
        reversed.append(row[i])
    return reversed

def checkUp(puzzle, index, word): #down to up
    col = [ ] #making a list of the column
    for row in range(len(puzzle)): #number of rows in puzzle,
        col.append( puzzle[row][index])

    return checkBackward(col, word) #col is the up to down column in row form, so we check backward



def checkDown(puzzle,index,word): #up to down
    col = [ ] #making a list of the column
    for row in range(10): #number of rows in puzzle,
        col.append( puzzle[row][index])
    return checkForward(col,word) #now col is a row, so chekc forward

def colToRow(puzzle, colNumber):
    row = [ ]
    for row in range(len(puzzle)):
       row.append( puzzle[row] [colNumber] )
    return row
   
def makePuzzle(string): #works
	allCharacterString = string[:100] #string of 100 characters
	puzzle = [ ] #list of lists 10 by 10

	i =0 
	while i < 100 :
		row = [ ]
		for r in range(0,10):
				 row.append(allCharacterString[i])
				 i+=1
		puzzle.append(row)
	#print(puzzle)
	#printPuzzle(puzzle)
	return puzzle 
	#printPuzzle(puzzle)

def printPuzzle(puzzle): #works
	for r in puzzle:
		for i in range(len(r)):
			print(r[i], end='')
		print()
	print()

