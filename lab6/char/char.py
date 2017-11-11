def is_lower_101(char):
    if ord(char) > 96 and ord(char) < 123:
       return True
    return False

def char_rot_13(char):
    if is_lower_101(char):
       if ord(char) < 111: #if it's less than 'o' 
          newC = chr(ord(char)+13)
       else: 
          newC = chr(ord(char)-13)
    else: #uppercase
       if ord(char) < 79:
          newC = chr(ord(char)+13)
       else:
          newC = chr(ord(char)-13)
    return newC
         
   
