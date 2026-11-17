from typing import List

def sortArrayByParityII(nums: List[int]) -> None:
    """
    Sorts the array in-place such that even indices contain even numbers and odd indices contain odd numbers.
    Uses two pointers: one for even indices (i) and one for odd indices (j).
    Time Complexity: O(n), Space Complexity: O(1).
    """
    n = len(nums)
    i, j = 0, 1  # i for even indices, j for odd indices
    while i < n and j < n:
        if nums[i] % 2 == 0:
            i += 2
        elif nums[j] % 2 == 1:
            j += 2
        else:
            # nums[i] is odd and nums[j] is even -> swap
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
