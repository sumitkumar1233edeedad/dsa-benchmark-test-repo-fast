# Find First Occurrence of Target in Array

- **Day:** `Day 01`
- **Level:** `Level 01`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return the index of the first occurrence of `target` in `nums`. If `target` is not present in the array, return `-1`.

You must solve this problem using a linear scan (single pass) through the array.

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

**Example 1:**
```
Input: nums = [4, 2, 7, 2, 9], target = 2
Output: 1
Explanation: The first occurrence of 2 is at index 1.
```

**Example 2:**
```
Input: nums = [1, 3, 5, 7], target = 8
Output: -1
Explanation: 8 does not exist in the array.
```

**Example 3:**
```
Input: nums = [10], target = 10
Output: 0
Explanation: The only element is the target at index 0.
```

---

## 💻 Starter Function

```python
def find_first_occurrence(nums: list[int], target: int) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> As the very first question of the curriculum (Day 01, Level 01, Question 01), this problem establishes the fundamental skill of linear traversal and direct indexing. It requires a simple single-pass scan to locate a target value, reinforcing the concept of iterating through an array, comparing elements, and returning an index. This avoids duplication with the prohibited list (e.g., 'Contains Duplicate', 'First Unique Element', 'Move Zeroes') because it focuses purely on the canonical linear search pattern without additional constraints like uniqueness, sorting, or in-place modification. It serves as the essential building block for more complex search and traversal problems later in the week.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
