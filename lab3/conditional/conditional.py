def max_101(x,y):
   if x > y:
     return x
   else:
     return y

def max_of_three(x,y,z):
    if x > y and y > z:
         if x > y:
              return x
         else:
              return z
    elif y > z:
         return y
    else:
         return z    

def rental_late_fee(days):
   if days <= 0:
     return 0
   elif days <= 9:
     return 5
   elif days <=15:
     return 7
   elif days <=24:
     return 19
   else:
      return 100
