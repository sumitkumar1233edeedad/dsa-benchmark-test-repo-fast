import unittest
from typing import List

# Import the solution function (assuming it's in the same module)
# For the purpose of this test, we define it here again.
def longest_subarray_sum_at_most_k(nums: List[int], k: int) -> int:
    left = 0
    current_sum = 0
    max_len = 0
    for right, val in enumerate(nums):
        current_sum += val
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

class TestLongestSubarraySumAtMostK(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4, 5]
        k = 10
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 4)
    
    def test_example2(self):
        nums = [5, 1, 3, 2, 4]
        k = 7
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 3)
    
    def test_example3(self):
        nums = [10, 20, 30]
        k = 5
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 0)
    
    def test_single_element_within_k(self):
        nums = [5]
        k = 10
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 1)
    
    def test_single_element_exceeds_k(self):
        nums = [15]
        k = 10
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 0)
    
    def test_whole_array_within_k(self):
        nums = [1, 2, 3]
        k = 10
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 3)
    
    def test_all_elements_equal_k(self):
        nums = [2, 2, 2]
        k = 6
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 3)
    
    def test_large_k(self):
        nums = [100, 200, 300]
        k = 1000
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 3)
    
    def test_multiple_valid_subarrays(self):
        nums = [1, 1, 1, 10, 1, 1]
        k = 3
        # longest is first three 1's or last two 1's? first three sum=3 length=3
        self.assertEqual(longest_subarray_sum_at_most_k(nums, k), 3)

if __name__ == '__main__':
    unittest.main()
