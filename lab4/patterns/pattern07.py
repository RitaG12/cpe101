import driver

def letter(row, col):
   if 4<= row <=5 and 7<= col <=9:
     return 'X'
   elif 2<= row <= 5 and 4<= col <= 9:
      return 'Z'
   elif 4<= row <= 6 and 7<= col <= 12:
      return 'B'
   else:
      return 'T'

if __name__ == '__main__':
   driver.comparePatterns(letter)

