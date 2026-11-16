from typing import List

def longest_unique_prefix_length(nums: List[int]) -> int:
    """
    Returns the length of the longest prefix of `nums` that contains all unique elements.
    A prefix is a contiguous subarray starting at index 0.
    If the entire array has unique elements, returns len(nums).
    """
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return i
        seen.add(num)
    return len(nums)