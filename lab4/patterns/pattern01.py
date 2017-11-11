import driver

def letter(row, col):
  
 if col == 9 and row == 9:
    return 'Z'
 else:
    return 'G'

if __name__ == '__main__':
  driver.comparePatterns(letter)
