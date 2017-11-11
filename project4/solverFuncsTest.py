import unittest

from solverFuncs import *

class TestCases(unittest.TestCase):
    
    def checkForward1(self):
        row = ['Y','C','S','L','O','A','C','U','Z','M']
        word = "SLO"
        self.assertTrue(checkForward(row, word))
    def checkForward2(self):
        row = ['U','U','I','U','N','I','X','F','N','U']
        word = "UNIX"
        self.assertTrue(checkForward(row, word))
    def checkForward3(self):
        row = ['Y','C','S','L','O','A','C','U','Z','M']
        word = "CALPOLY"
        self.assertFalse(checkForward(row, word))
            
    def checkReversed1(self):
        row = ['C','B','M','I','V','Q','Q','E','L','S']
        self.assertEqual(makeReversedRow(row),['S','L','E','Q','Q','V','I','M','B','C'])
    
    def checkReversed2(self):
        row = ['W','A','Q','H','G','T','T','W','E','E']
        self.assertEqual(makeReversedRow(row),['E','E','W','T','T','G','H','Q','A','W'])
    def checkBackwards1(self):
        row = ['C','B','M','I','V','Q','Q','E','L','S']
        self.assertTrue(checkBackward(row, "VIM"))

    def checkBackwards2(self):
        row = ['C','B','M','I','V','Q','Q','E','L','S']
        self.assertTrue(checkBackward(row, "VIM"))   
    def checkBackwards3(self):
        row = ['Z','E','B','R','A','E','B','R','B','H']
        self.assertTrue(checkBackward(row, "BEAR"))
    def checkBackwards4(self):
        row = ['Z','E','B','R','A','E','B','R','B','H']
        self.assertFalse(checkBackward(row, "VIM"))
   
	 def checkUp(self):
	     
			pass


    if __name__ == '__main__':
        unittest.main()
