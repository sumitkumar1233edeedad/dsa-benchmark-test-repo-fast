from typing import List

def find_first_local_maximum(arr: List[int]) -> int:
    """
    Returns the index of the first local maximum in arr.
    A local maximum is strictly greater than its adjacent elements.
    For boundaries, only one neighbor is considered.
    Returns -1 if none exists.
    """
    n = len(arr)
    if n == 1:
        # Single element is trivially a local maximum
        return 0
    # Check first element
    if arr[0] > arr[1]:
        return 0
    # Check middle elements
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i
    # Check last element
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    return -1
