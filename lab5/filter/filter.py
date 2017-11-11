def are_positive(l1):
   l2 = [ num for num in l1 if num>-1]
   return l2

def are_greater_than_n(l1, n):
   l2 = [ ]
   l = len(l1)
   for i in range (l):
       if l1[i] > n:
           l2.append(l1[i])
   return l2

def are_divisible_by_n(l1, n):
    curr = 0
    l2 = [ ]
    while curr < len(l1):
        if l1[curr]%n ==0:
            l2.append(l1[curr])
        curr+=1
    return l2
