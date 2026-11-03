# Find the First Local Maximum Index

- **Day:** `Day 01`
- **Level:** `Level 01`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `arr`, find the index of the **first local maximum**.

A **local maximum** is defined as an element that is **strictly greater** than its immediate neighbor(s).
- For an element at index `i` (where `0 < i < n-1`), it must satisfy `arr[i] > arr[i-1]` and `arr[i] > arr[i+1]`.
- For the first element (index `0`), it only needs to be greater than the second element: `arr[0] > arr[1]`.
- For the last element (index `n-1`), it only needs to be greater than the second-to-last element: `arr[n-1] > arr[n-2]`.

If no such element exists, return `-1`.

**Constraints:**
- `1 <= len(arr) <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

**Examples:**

**Example 1:**
```
Input: arr = [1, 3, 2, 4, 5]
Output: 1
Explanation: arr[1] = 3 is greater than both neighbors (1 and 2). It is the first local maximum.
```

**Example 2:**
```
Input: arr = [5, 4, 3, 2, 1]
Output: 0
Explanation: The first element 5 is greater than its only neighbor 4.
```

**Example 3:**
```
Input: arr = [1, 2, 3, 4, 5]
Output: 4
Explanation: The last element 5 is greater than its only neighbor 4.
```

**Example 4:**
```
Input: arr = [2, 2, 2]
Output: -1
Explanation: No element is strictly greater than its neighbor(s).
```

---

## 💻 Starter Function

```python
from typing import List

def find_first_local_maximum(arr: List[int]) -> int:
    """
    Returns the index of the first local maximum in arr.
    A local maximum is strictly greater than its adjacent elements.
    For boundaries, only one neighbor is considered.
    Returns -1 if none exists.
    """
    # Your code here
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Day 01 Level 01 Q01) asked for the index of the first global minimum element, which is a straightforward linear scan tracking the minimum value and its first occurrence. This problem provides a complementary twist on linear traversal: instead of a global property, we search for a local property (first local maximum) that requires checking immediate neighbors. This introduces edge boundary optimization (handling first and last elements differently) and reinforces the pattern of a single pass with conditional checks on adjacent elements. It avoids duplication by focusing on a local extremum rather than a global one, and it does not reuse any mechanics from the avoided list (e.g., no in-place modification, no hashing, no two-pointer pairing). The problem remains Easy, fits the Arrays & Hashing topic, and naturally extends the linear traversal skill set.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
