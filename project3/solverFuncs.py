def check_valid(puzzle, cages): #done
    result_rows = check_rows_valid(puzzle)
    result_cols = check_columns_valid(puzzle)
    result_cages = check_cages_valid(puzzle, cages)
   # print("Rows, Cols, Cages :",result_rows, result_cols, result_cages)
    if check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle, cages):
        return True
    return False

def check_row_valid(rowList): #helper function for check_rows_valid(puzzle)
    for num in range(len(rowList)):
        if rowList.count(rowList[num]) > 1 and rowList[num] != 0:
              return False
    return True

def check_rows_valid(puzzle):   #done?       
    for i in range(len(puzzle)): #for each list in the puzzle = each row
       if check_row_valid(puzzle[i]) == False:
              return False
    return True

def check_cages_valid(puzzle, cages): #done
    for cage in cages: 
       if check_one_cage(cage, puzzle) == False:
             #  print('False')
               return False
    return True

def check_one_cage(cageList, puzzle): #helper cages function
     sum=0
     cageNums = [ ]

     for i in range(2, len(cageList)):#create list of numbers in cage
        r= cageList[i]//5
        c= cageList[i] % 5 
        cageNums.append(puzzle[r][c])

     for j in range(len(cageNums)): #sum of cage
        sum+=cageNums[j]

     if cageNums.count(0) >=1: #partial
        #if sum >= cageList[0]:
           # return False
        if sum < cageList[0]:
            return True
        else: 
            return False
     else:
        if sum != cageList[0]: #full
            return False
     return True 

def check_columns_valid(puzzle):
     for col in range(len(puzzle)):
        if check_col(puzzle, col)== False:
            return False
     return True

def check_col(puzzle, index):
     col = [ ] 
     for row in range(len(puzzle)): #number of rows in puzzle
            col.append( puzzle[row][index])
     if check_row_valid(col)== False:
         return False
     return True

     
def get_cages(): #returns the list of cages. each cage is  list
     #COMMENT UN. ALL THESE
     numCages = int(input("Number of cages: "))
     cage = [ ]
     cages=[ ]
     for i in range(numCages):
         cage = input("Cage number "+ str(i)+": ").split() 
         myCage = [int(i) for i in cage]
         cages.append(myCage)   
     return cages #PUT THIS BACK FROM THE BOTTOM ONE
    # return [[9,3,0,5,6],[7,2,1,2],[10,3,3,8,13],[14,4,4,9,14,19],[3,1,7],[8,3,10,11,16],[13,4,12,17,21,22],[5,2,15,20],[6,3,18,23,24]]



    
