# Find the Index of the First Minimum Element

- **Day:** `Day 01`
- **Level:** `Level 01`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, return the **index** of the first occurrence of the minimum value in the array.

If the array is empty, return `-1` (though constraints guarantee at least one element).

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Example 1:**
```
Input: nums = [3, 1, 4, 1, 5]
Output: 1
Explanation: The minimum value is 1, which first appears at index 1.
```

**Example 2:**
```
Input: nums = [10, 20, 30]
Output: 0
Explanation: The minimum value is 10 at index 0.
```

**Example 3:**
```
Input: nums = [5, 5, 5, 5]
Output: 0
Explanation: All elements are 5; the first occurrence is at index 0.
```

---

## 💻 Starter Function

```python
from typing import List

def find_first_min_index(nums: List[int]) -> int:
    """
    Returns the index of the first occurrence of the minimum element in nums.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> This is the inaugural problem (Day 01, Level 01, Q01) for the Arrays & Hashing topic focusing on Linear Traversal & Search. Since no prior problems exist, we establish the absolute foundation: a single-pass linear scan that tracks both the running minimum value and its first index. This problem is canonical for teaching loop invariants, direct indexing, and comparison logic without any auxiliary data structures. It deliberately avoids the mechanics of the blocked list (e.g., duplicate detection, target search, two-pointer, sliding window, hashing) by focusing purely on the 'scan and track extremum' pattern. The next logical step (Q02) can introduce a complementary twist such as finding the last occurrence or counting frequency, but this first problem cements the core traversal mechanic.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
