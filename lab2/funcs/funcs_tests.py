import unittest
from funcs import * 

class TestCases(unittest.TestCase):
   def test_f_1(self):
      self.assertEqual(f(1),9)
      
   def test_f_2(self):
      self.assertEqual(f(-1),5)

   def test_g_1(self):
      self.assertAlmostEqual(g(1,2),1.66666666)
   
   def test_g_2(self):
      self.assertAlmostEqual(g(2,0),.66666666)  
  
   def test_hyp_1(self):
      self.assertEqual(hypotenuse(3,4),5)
  
   def test_hyp_2(self):
      self.assertAlmostEqual(hypotenuse(4,6),7.211102550927)
   
   def test_ispos_1(self):
      self.assertTrue(is_positive(4))

   def test_ispos_2(self):
      self.assertFalse(is_positive(-1)) 
  
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

