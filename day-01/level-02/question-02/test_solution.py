import unittest
from typing import List

# The solution function is assumed to be available in the same namespace.
# If running standalone, define it here:
# def longest_unique_prefix_length(nums: List[int]) -> int: ...

class TestLongestUniquePrefixLength(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 2, 4]
        self.assertEqual(longest_unique_prefix_length(nums), 3)

    def test_example2(self):
        nums = [5, 5, 5, 5]
        self.assertEqual(longest_unique_prefix_length(nums), 1)

    def test_example3(self):
        nums = [10, 20, 30, 40, 50]
        self.assertEqual(longest_unique_prefix_length(nums), 5)

    def test_single_element(self):
        nums = [42]
        self.assertEqual(longest_unique_prefix_length(nums), 1)

    def test_all_unique(self):
        nums = list(range(1000))
        self.assertEqual(longest_unique_prefix_length(nums), 1000)

    def test_duplicate_at_start(self):
        nums = [1, 1, 2, 3]
        self.assertEqual(longest_unique_prefix_length(nums), 1)

    def test_empty_list(self):
        # Though constraint says length >=1, handle gracefully.
        nums = []
        self.assertEqual(longest_unique_prefix_length(nums), 0)

if __name__ == "__main__":
    unittest.main()