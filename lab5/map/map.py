def square_all(l1):
    l2 = [i**2 for i in l1]
    return l2

def add_n_all(n, list1):
    list2 = [ ]
    for i in range(len(list1)):
        list2.append(list1[i]+n)
    return list2

def even_or_odd_all(l1):
    i = 0
    l2=[ ]
    while i < (len(l1)):
        if l1[i]%2 == 0: 
          l2.append(True)
          i+=1
        else:
          l2.append(False)
          i+=1
    return l2 
