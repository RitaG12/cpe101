import driver

def letter(row, col):
  if col <= 19 and row <= 9:
     return 'R'
  else:
     return 'Q'

if __name__ == '__main__':
   driver.comparePatterns(letter)

