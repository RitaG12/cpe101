import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_translate1(self):
      self.assertEqual(str_translate_101("banana", "a", "z"), "bznznz")
   def test_translate2(self):
      self.assertEqual(str_translate_101("hi", "h", "z"), "zi")
   def test_translate3(self):
      self.assertEqual(str_translate_101("", "a", "z"), "")
   def test_translate4(self):
      self.assertEqual(str_translate_101("banana", "a", "z"), "bznznz")
   def test_translate5(self):
      self.assertEqual(str_translate_101("hif riends", "i", "z"), "hzf rzends")
   
   def test_rot1(self):
      self.assertEqual(str_rot_13("ABCD"), "NOPQ")
   def test_rot12(self):
      self.assertEqual(str_rot_13("hello"), "uryyb")
   def test_rot3(self):
      self.assertEqual(str_rot_13("AbCd"), "NoPq")
if __name__ == '__main__':
   unittest.main()

