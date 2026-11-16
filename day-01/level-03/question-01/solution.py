def partition_by_parity(nums: list[int]) -> list[int]:
    '''
    Rearranges the array in-place so that all even integers come before all odd integers.
    The relative order of even and odd integers is not preserved.

    Args:
        nums: List of integers.

    Returns:
        The same list after partitioning.
    '''
    left, right = 0, len(nums) - 1
    while left < right:
        # Move left pointer to the right until an odd number is found
        if nums[left] % 2 == 0:
            left += 1
        # Move right pointer to the left until an even number is found
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            # nums[left] is odd and nums[right] is even -> swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums