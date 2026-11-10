import unittest
from typing import List

# The function under test (normally imported from solution)
def find_first_duplicate(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

class TestFindFirstDuplicate(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(find_first_duplicate([2, 5, 1, 2, 3, 5]), 2)
    def test_example2(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4]), -1)
    def test_example3(self):
        self.assertEqual(find_first_duplicate([1, 1, 2, 2, 3, 3]), 1)
    def test_single_element(self):
        self.assertEqual(find_first_duplicate([5]), -1)
    def test_all_same(self):
        self.assertEqual(find_first_duplicate([7, 7, 7]), 7)
    def test_negative_numbers(self):
        self.assertEqual(find_first_duplicate([-1, 2, -1, 3]), -1)
    def test_large_numbers(self):
        self.assertEqual(find_first_duplicate([10**9, -10**9, 10**9]), 10**9)
    def test_duplicate_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 1]), 1)

if __name__ == '__main__':
    unittest.main()