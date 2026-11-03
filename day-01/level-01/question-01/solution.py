from typing import List

def find_first_min_index(nums: List[int]) -> int:
    """
    Returns the index of the first occurrence of the minimum element in nums.
    If nums is empty, returns -1 (though constraints guarantee at least one element).
    """
    if not nums:
        return -1
    min_val = nums[0]
    min_idx = 0
    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
            min_idx = i
    return min_idx
