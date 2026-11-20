import unittest
from typing import List

def partition_array(nums: List[int], pivot: int) -> List[int]:
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == pivot:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

class TestPartitionArray(unittest.TestCase):
    def assertPartitioned(self, original: List[int], pivot: int, result: List[int]):
        # Check that result is a permutation of original
        self.assertEqual(sorted(original), sorted(result))
        # Check ordering: all < pivot, then == pivot, then > pivot
        seen_equal = False
        seen_greater = False
        for x in result:
            if x < pivot:
                self.assertFalse(seen_equal, f"Element {x} < pivot appears after equal or greater")
                self.assertFalse(seen_greater, f"Element {x} < pivot appears after greater")
            elif x == pivot:
                seen_equal = True
                self.assertFalse(seen_greater, f"Element {x} == pivot appears after greater")
            else:
                seen_greater = True

    def test_example1(self):
        nums = [9,12,5,10,14,3,10]
        pivot = 10
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_example2(self):
        nums = [-3,4,3,2]
        pivot = 2
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_example3(self):
        nums = [5,5,5]
        pivot = 5
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_single_element_less(self):
        nums = [1]
        pivot = 5
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_single_element_equal(self):
        nums = [5]
        pivot = 5
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_single_element_greater(self):
        nums = [10]
        pivot = 5
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_all_less(self):
        nums = [1,2,3,4]
        pivot = 10
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_all_greater(self):
        nums = [10,20,30]
        pivot = 5
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

    def test_negative_numbers(self):
        nums = [-5, -10, 0, 5, -3]
        pivot = -2
        result = partition_array(nums.copy(), pivot)
        self.assertPartitioned(nums, pivot, result)

if __name__ == '__main__':
    unittest.main()