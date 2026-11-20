def partition_array(nums: list[int], pivot: int) -> list[int]:
    """
    Rearranges nums in-place so that all elements < pivot come first,
    then elements == pivot, then elements > pivot.
    The relative order within the less-than and greater-than groups is not preserved.
    Returns the same list after rearrangement.
    """
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
        else:  # nums[mid] > pivot
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums