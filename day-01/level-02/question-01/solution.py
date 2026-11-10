from typing import List

def find_first_duplicate(nums: List[int]) -> int:
    """
    Returns the first duplicate element in the list `nums`.
    The first duplicate is defined as the element whose second occurrence has the smallest index.
    If no duplicates exist, returns -1.

    Args:
        nums: List of integers.

    Returns:
        The first duplicate element, or -1 if none.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1