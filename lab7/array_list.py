#List contains:
#array represents an ArrayList, defined by Python
class List:
    def __init__(self, arr, size, capacity):
        self.arr = arr #ArrayList
        self.size = size #Integer
        self.capacity = capacity #Integer

    '''def __eq__(self, other):
        if type(other) == List and self.size == other.size:
            for i in range(self.size):
                if self.arr[i] != other.arr[i]:
                    #print("rRET FALSE NOT EQUAL ELMENTS")
                    return False

            #print("rRET TRUE INSIDE")
            return True
        return False'''
    def __eq__(self, other):
        if type(other) != List or self.size != other.size:
            return False
        else:
            for i in range(self.size):
                if self.arr[i] != other.arr[i]:
                    return False
            return True

    def __repr__(self):
        return "List = %r, size=%r, capacity=%r"%(self.arr,self.size, self.capacity)

#-->List
#returns an empty list
def empty_list():
    return List([None]*10, 0, 10)

#List Integer Any
#returns an AnyList with the given value placed at the given position and if the index is invalid, an InexEror exception is raised
def add(arr, index, value):
    if index < 0 or index > arr.size:
        raise IndexError
    else:
        l = arr.arr
        if arr.size == arr.capacity: #double size
            l1 = [None] * arr.capacity * 2
            for j in range(arr.size):
                l1[j] = l[j] #jusy transfers evrethign over
            return add(List(l1, 10,20), index, value)
        else:
            l1 = List([None]*(arr.capacity), arr.size+1, arr.capacity)
            for i in range(arr.size+1):
                if index < i:
                    l1.arr[i] = l[i-1]
                elif index==i:
                    l1.arr[i] = value
                else:
                    l1.arr[i] = l[i]
            return l1

#List --> Integer
#returns how many elements are in the list
def length(arr):
    return arr.size

#List Integer --> Any
#returns whatever is in the index position (the integer) and an IndexError if the index is out of bounds
def get(arr, index):
    if index < 0 or index > arr.size or arr.size ==0:
        raise IndexError
    else:
        for i in range(arr.size):
            if i == index:
                return arr.arr[i]

#List Integer Any --> List
#returns a list with the given value at the position (Integer) passed in
def set(arr, index, value):
    if index < 0 or index > arr.size or arr.size ==0:
        raise IndexError
    else:
        l1 = List([None] * (arr.capacity), arr.size, arr.capacity)
        for i in range(arr.size):
            if index == i:
                l1.arr[i] = value
            else:
                l1.arr[i] = arr.arr[i]
        return l1

#List Integer --> Tuple
#returns a 2-tuple of the element previoulsly at the specified index and the resulting list
def remove(arr, index):
    if index < 0 or index > arr.size or arr.size ==0:
        raise IndexError
    l = arr.arr
    l1 = List([None] * (arr.capacity), arr.size - 1, arr.capacity)
    removed = l[index]

    for i in range(arr.size):
        if index > i:
            l1.arr[i] = l[i]
        elif i > index:
            l1.arr[i-1] = l[i]
    return (removed, l1)









