import unittest

class TestPartitionByParity(unittest.TestCase):
    def test_example1(self):
        nums = [3,1,2,4]
        result = partition_by_parity(nums)
        # Check all evens before odds
        self.assertTrue(all(x % 2 == 0 for x in result[:2]))
        self.assertTrue(all(x % 2 == 1 for x in result[2:]))
        # Check it's a permutation
        self.assertEqual(sorted(result), sorted([3,1,2,4]))

    def test_example2(self):
        nums = [0,1,2,3,4]
        result = partition_by_parity(nums)
        # Count evens
        evens = sum(1 for x in nums if x % 2 == 0)
        self.assertTrue(all(x % 2 == 0 for x in result[:evens]))
        self.assertTrue(all(x % 2 == 1 for x in result[evens:]))
        self.assertEqual(sorted(result), sorted([0,1,2,3,4]))

    def test_example3(self):
        nums = [1,3,5]
        result = partition_by_parity(nums)
        self.assertEqual(result, [1,3,5])  # unchanged

    def test_single_element_even(self):
        nums = [2]
        result = partition_by_parity(nums)
        self.assertEqual(result, [2])

    def test_single_element_odd(self):
        nums = [3]
        result = partition_by_parity(nums)
        self.assertEqual(result, [3])

    def test_all_even(self):
        nums = [2,4,6,8]
        result = partition_by_parity(nums)
        self.assertEqual(sorted(result), sorted(nums))
        self.assertTrue(all(x % 2 == 0 for x in result))

    def test_all_odd(self):
        nums = [1,3,5,7]
        result = partition_by_parity(nums)
        self.assertEqual(sorted(result), sorted(nums))
        self.assertTrue(all(x % 2 == 1 for x in result))

    def test_negative_numbers(self):
        nums = [-2, -3, -4, -1, 0]
        result = partition_by_parity(nums)
        evens = sum(1 for x in nums if x % 2 == 0)
        self.assertTrue(all(x % 2 == 0 for x in result[:evens]))
        self.assertTrue(all(x % 2 == 1 for x in result[evens:]))
        self.assertEqual(sorted(result), sorted(nums))

if __name__ == '__main__':
    unittest.main()