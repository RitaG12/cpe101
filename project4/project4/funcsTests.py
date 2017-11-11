import unittest

from funcs import *

class TestCases(unittest.TestCase):
    puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'Z', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'W', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
    sol = WAQHGTTWEE
          CBMIVQQELS
          AZXWKWIIIL
          LDWLFXPIPV
          PONDTMVAMN
          OEDSOYQGOB
          LGQCKGMMCT
          YCSLOACUZM
          XVDMGSXCYZ
          UUIUNIXFNU
    
    def forward1(self):
       
       self.assertEqual(forward("unix", puzzle), [True,9,3])
    
    def backward1(self):
        self.assertEqual(backward("VIM", puzzle), [True, 1,4])
    
    def up(self):
        self.assertEqual(up("compile"), 6, 8)
    
    def down(self):
        self.assertEqual(down("CALPOLY",puzzle), [True, 1, 0])
    
    
    def checkForward1(self):
       row = ['Y','C','S','L','O','A','C','U','Z','M']
       word = "SLO"
       self.assertEqual(checkForward(row, word),[True, 2])
    def checkForward2(self):
        row = ['U','U','I','U','N','I','X','F','N','U']
        word = "UNIX"
        self.assertEqual(checkForward(row, word), [True,3] )
    def checkForward3(self):
        row = ['Y','C','S','L','O','A','C','U','Z','M']
        word = "CALPOLY"
        self.assertEqual(checkForward(row, word), [True, 0])
            
    def makeReversed1(self):
        row = ['C','B','M','I','V','Q','Q','E','L','S']
        self.assertEqual(makeReversedRow(row),['S','L','E','Q','Q','V','I','M','B','C'])
    def checkUp(self):
        self.assertEqual(checkUp(puzzle, 8, "COMPILE"), [True, 8])
    
    def checkDown(self):
        self.assertEqual(checkDown(puzzle, 0, "CALPOLY"), [True, 1,0])
    
    def colToRow(self):
        self.assertEqual(colToRow(puzzle, 0), ['W','C','A','L','P','O','L','Y','X','U'])
    def makePuzzle(self):
        self.assertEqual(makePuzzle("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), puzzle)
    def printPuzzle(self):
        self.assertEqual(printPuzzle(puzzle), sol)
    def makeReversed2(self):
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
