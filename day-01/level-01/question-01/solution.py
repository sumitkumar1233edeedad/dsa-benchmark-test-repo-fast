def find_first_occurrence(nums: list[int], target: int) -> int:
    """
    Returns the index of the first occurrence of target in nums.
    If target is not found, returns -1.
    """
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1
