import driver

def letter(row, col):
  if 2 <= row <= 4 and 3 <= col <= 6: 
    return 'M'
  else:
    return 'S'

if __name__ == '__main__':
   driver.comparePatterns(letter)

