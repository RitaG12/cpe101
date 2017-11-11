from char import *

def str_rot_13(string):
    rot13 = [char_rot_13(s) for s in string ]
    delimiter=''
    s= delimiter.join(rot13)
    return s

def str_translate_101(string, old, new):
    length = len(string)
    for s in range(length):
       if string[s] == old:
           newString = string[:s]+new+string[s+1:]
           string = newString
    return string
