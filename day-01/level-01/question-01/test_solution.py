import unittest

class TestFindFirstOccurrence(unittest.TestCase):
    def test_example1(self):
        nums = [4, 2, 7, 2, 9]
        target = 2
        self.assertEqual(find_first_occurrence(nums, target), 1)
    
    def test_example2(self):
        nums = [1, 3, 5, 7]
        target = 8
        self.assertEqual(find_first_occurrence(nums, target), -1)
    
    def test_example3(self):
        nums = [10]
        target = 10
        self.assertEqual(find_first_occurrence(nums, target), 0)
    
    def test_target_not_present(self):
        nums = [5, 5, 5]
        target = 3
        self.assertEqual(find_first_occurrence(nums, target), -1)
    
    def test_multiple_occurrences(self):
        nums = [1, 2, 3, 2, 1]
        target = 2
        self.assertEqual(find_first_occurrence(nums, target), 1)
    
    def test_negative_numbers(self):
        nums = [-5, -2, 0, 3, -2]
        target = -2
        self.assertEqual(find_first_occurrence(nums, target), 1)
    
    def test_single_element_not_target(self):
        nums = [7]
        target = 8
        self.assertEqual(find_first_occurrence(nums, target), -1)

if __name__ == '__main__':
    unittest.main()
