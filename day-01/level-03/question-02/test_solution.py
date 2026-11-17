import unittest
from typing import List

# The solution function is assumed to be available in the global namespace
# (defined in solution_code).

class TestSortArrayByParityII(unittest.TestCase):
    def test_example1(self):
        nums = [4, 2, 5, 7]
        sortArrayByParityII(nums)
        for i, val in enumerate(nums):
            self.assertEqual(i % 2, val % 2)
        self.assertEqual(sorted(nums), sorted([4, 2, 5, 7]))

    def test_example2(self):
        nums = [2, 3]
        sortArrayByParityII(nums)
        for i, val in enumerate(nums):
            self.assertEqual(i % 2, val % 2)
        self.assertEqual(sorted(nums), sorted([2, 3]))

    def test_example3(self):
        nums = [1, 2, 3, 4, 5, 6]
        sortArrayByParityII(nums)
        for i, val in enumerate(nums):
            self.assertEqual(i % 2, val % 2)
        self.assertEqual(sorted(nums), sorted([1, 2, 3, 4, 5, 6]))

    def test_all_even_first(self):
        # Even numbers at even indices already, odd at odd indices already
        nums = [2, 1, 4, 3, 6, 5]
        original = nums.copy()
        sortArrayByParityII(nums)
        for i, val in enumerate(nums):
            self.assertEqual(i % 2, val % 2)
        self.assertEqual(sorted(nums), sorted(original))

    def test_all_odd_first(self):
        # Odd numbers at even indices, even at odd indices -> need full swap
        nums = [1, 2, 3, 4, 5, 6]
        original = nums.copy()
        sortArrayByParityII(nums)
        for i, val in enumerate(nums):
            self.assertEqual(i % 2, val % 2)
        self.assertEqual(sorted(nums), sorted(original))

    def test_large_random(self):
        import random
        n = 1000
        # generate half even, half odd
        evens = [random.randrange(0, 1000, 2) for _ in range(n // 2)]
        odds = [random.randrange(1, 1000, 2) for _ in range(n // 2)]
        nums = evens + odds
        random.shuffle(nums)
        original = nums.copy()
        sortArrayByParityII(nums)
        for i, val in enumerate(nums):
            self.assertEqual(i % 2, val % 2)
        self.assertEqual(sorted(nums), sorted(original))

if __name__ == '__main__':
    unittest.main()
