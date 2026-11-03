import unittest
from typing import List

# The solution function is defined in the same context (solution_code)
# so we can use it directly without import.

class TestFindFirstLocalMaximum(unittest.TestCase):
    def test_example1(self):
        arr = [1, 3, 2, 4, 5]
        self.assertEqual(find_first_local_maximum(arr), 1)
    
    def test_example2(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_first_local_maximum(arr), 0)
    
    def test_example3(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_first_local_maximum(arr), 4)
    
    def test_example4(self):
        arr = [2, 2, 2]
        self.assertEqual(find_first_local_maximum(arr), -1)
    
    def test_single_element(self):
        arr = [10]
        self.assertEqual(find_first_local_maximum(arr), 0)
    
    def test_two_elements_increasing(self):
        arr = [1, 2]
        self.assertEqual(find_first_local_maximum(arr), 1)
    
    def test_two_elements_decreasing(self):
        arr = [2, 1]
        self.assertEqual(find_first_local_maximum(arr), 0)
    
    def test_two_elements_equal(self):
        arr = [2, 2]
        self.assertEqual(find_first_local_maximum(arr), -1)
    
    def test_multiple_peaks(self):
        arr = [1, 3, 2, 5, 4]
        self.assertEqual(find_first_local_maximum(arr), 1)
    
    def test_peak_at_end_after_plateau(self):
        arr = [1, 2, 2, 3]
        self.assertEqual(find_first_local_maximum(arr), 3)
    
    def test_no_peak_all_equal(self):
        arr = [5, 5, 5, 5]
        self.assertEqual(find_first_local_maximum(arr), -1)

if __name__ == '__main__':
    unittest.main()
