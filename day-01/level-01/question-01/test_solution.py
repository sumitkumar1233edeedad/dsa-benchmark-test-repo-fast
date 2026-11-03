import unittest
from typing import List

# Import the function from the solution (assuming it's in the same module)
# In practice, the test would import from the solution file.
# For this self-contained test, we define the function here again or import.
# We'll just use the function defined above.

def find_first_min_index(nums: List[int]) -> int:
    if not nums:
        return -1
    min_val = nums[0]
    min_idx = 0
    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
            min_idx = i
    return min_idx

class TestFindFirstMinIndex(unittest.TestCase):
    def test_example1(self):
        nums = [3, 1, 4, 1, 5]
        self.assertEqual(find_first_min_index(nums), 1)
    
    def test_example2(self):
        nums = [10, 20, 30]
        self.assertEqual(find_first_min_index(nums), 0)
    
    def test_example3(self):
        nums = [5, 5, 5, 5]
        self.assertEqual(find_first_min_index(nums), 0)
    
    def test_single_element(self):
        nums = [42]
        self.assertEqual(find_first_min_index(nums), 0)
    
    def test_negative_numbers(self):
        nums = [-5, -10, -3, -10]
        self.assertEqual(find_first_min_index(nums), 1)
    
    def test_decreasing_order(self):
        nums = [10, 9, 8, 7, 6]
        self.assertEqual(find_first_min_index(nums), 4)
    
    def test_increasing_order(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(find_first_min_index(nums), 0)
    
    def test_empty_list(self):
        # Though constraints say at least one element, we test empty for robustness
        nums = []
        self.assertEqual(find_first_min_index(nums), -1)

if __name__ == '__main__':
    unittest.main()
