# Partition Array Around Pivot

- **Day:** `Day 01`
- **Level:** `Level 06`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `pivot`, rearrange the array such that:

- All elements **less than** `pivot` appear before elements **equal to** `pivot`.
- All elements **equal to** `pivot` appear before elements **greater than** `pivot`.

Return the rearranged array. The relative order of elements in the less-than and greater-than groups does not matter, but all elements equal to `pivot` must be contiguous.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i], pivot <= 10^9`

**Example 1:**
```
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: Elements less than 10: [9,5,3]; equal to 10: [10,10]; greater than 10: [12,14]. Any permutation that keeps these three groups in order is accepted.
```

**Example 2:**
```
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: Less than 2: [-3]; equal to 2: [2]; greater than 2: [4,3] (order within group doesn't matter).
```

**Example 3:**
```
Input: nums = [5,5,5], pivot = 5
Output: [5,5,5]
```

---

## 💻 Starter Function

```python
def partition_array(nums: list[int], pivot: int) -> list[int]:
    """
    Rearranges nums so that all elements < pivot come first,
    then elements == pivot, then elements > pivot.
    Returns the rearranged list (can be done in-place).
    """
    # Your implementation here
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems explored two-way partitioning by parity (Level 03), sliding window bounds (Level 04), and prefix/suffix transforms (Level 05). This problem introduces the canonical three-way partitioning algorithm (Dutch National Flag) around an arbitrary pivot value. It is the fundamental partitioning step used in quicksort and quickselect, directly aligning with the 'Quickselect partitioning' core mechanic. The problem avoids duplication by generalizing beyond parity, not relying on sliding windows or prefix/suffix sums, and requires in-place index manipulation—reinforcing the day's theme of linear traversals and direct indexing.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
