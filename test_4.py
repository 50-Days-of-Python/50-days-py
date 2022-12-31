import unittest
import main

# DO NOT TOUCH THE BELOW CODE

class Test_4(unittest.TestCase):
  def test_01(self):
    self.assertEqual(main.digits_of(12), 2)
    
if __name__ == '__main__':
  unittest.main(verbosity=2)
