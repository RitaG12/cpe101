import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_char(self):
      self.assertEqual(char_rot_13('z'), 'm')
   def test_char1(self):
      self.assertEqual(char_rot_13('A'), 'N') 
   def test_char2(self):
      self.assertEqual(char_rot_13('w'), 'j')
   def test_char3(self):
      self.assertEqual(char_rot_13('M'), 'Z') 
  
   def test_lower1(self):
      self.assertEqual(is_lower_101('M'), False)
   def test_lower2(self):
      self.assertEqual(is_lower_101('n'), True)

if __name__ == '__main__':
   unittest.main()

