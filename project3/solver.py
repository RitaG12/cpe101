from solverFuncs import *

def main():
   #returns the list of cages 
   cages = get_cages() #cages now has the user inputted values 
   puzzle = [ ]
   checks = 0
   backtracks = 0
   r=0
   c=0
   for i in range(5):
      puzzle.append([0,0,0,0,0]) #initialize puzzle to all 0s
   
  
   while r < 5 and c < 5:
    # print("r: ",r)
    # print("c: ",c)
     puzzle[r][c] +=1 
    # print(puzzle)
     if check_valid(puzzle, cages) and not puzzle[r][c] >5:
      #  print("Valid")
        checks+=1
        c+=1
      
        if c >4:
           r+=1 
           c =0
        if r >4:
           break

     else: #not valid
     #   print("Not valid")
        checks+=1 #if the number is not valid, increment the number and check for validity again
          
        if puzzle[r][c] >= 5: #if the number is the maximum possible and still invalid, backtrack
            backtracks +=1
            puzzle[r][c] = 0
            if c==0: #if first column, left most side
               r-=1 #go to the previous row and right most column to go "backwards"
               c = 4
            else:
               c-=1 #when not frist column
   print()
   print("---Solution---")
   print()
     #print puzzle
   for r in puzzle:
       for i in range(len(r)):
           print(r[i],"", end='')
       print()
   print()
   print("checks:", checks, "backtracks:", backtracks)
   
  
if __name__ == "__main__":
   main()
