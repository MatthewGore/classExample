# test_sum_nums.py
import unittest
from sum_nums import sum_nums

class TestSumNums(unittest.TestCase):

  def test_sum_nums(self):
    self.assertEqual(sum_nums(2, 3), 5)

if __name__ == "__main__":
  unittest.main()
