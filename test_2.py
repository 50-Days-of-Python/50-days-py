import unittest
import main

# DO NOT TOUCH THE BELOW CODE

class Test_2(unittest.TestCase):
  def test_02(self):
    self.assertEqual(main.digits_of(186), 3)
    
if __name__ == '__main__':
  unittest.main(verbosity=2)
    
