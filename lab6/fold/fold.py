def sum(list):
   sum = 0
   for num in list:
       sum += num
   return sum

def index_of_smallest(list):
   if len(list) <=0:
      return -1
   else:
      smallest = list[0]
      for num in range(len(list)): 
          if list[num] < smallest:
             smallest = num
   return smallest
         
