from typing import List

def longest_subarray_sum_at_most_k(nums: List[int], k: int) -> int:
    """
    Returns the length of the longest contiguous subarray with sum <= k.
    Since all numbers are positive, we can use a sliding window (two pointers).
    Time Complexity: O(n), Space Complexity: O(1).
    """
    left = 0
    current_sum = 0
    max_len = 0
    for right, val in enumerate(nums):
        current_sum += val
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1
        # now current_sum <= k
        max_len = max(max_len, right - left + 1)
    return max_len
