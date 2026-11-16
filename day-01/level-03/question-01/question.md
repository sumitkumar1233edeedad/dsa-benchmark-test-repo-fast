# Partition Array by Parity

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, rearrange the array **in-place** such that all even integers appear before all odd integers.

The relative order of the even integers and the relative order of the odd integers **does not** need to be preserved.

Return the modified array after partitioning.

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4

**Example 1:**
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The even numbers 2 and 4 are moved to the front. Any permutation with evens first then odds is accepted, e.g., [4,2,3,1] or [2,4,1,3].

**Example 2:**
Input: nums = [0,1,2,3,4]
Output: [0,2,4,1,3]
Explanation: Evens (0,2,4) precede odds (1,3).

**Example 3:**
Input: nums = [1,3,5]
Output: [1,3,5]
Explanation: No even numbers, array remains unchanged.

---

## 💻 Starter Function

```python
def partition_by_parity(nums: list[int]) -> list[int]:
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems (Levels 1-2) focused on linear traversal and hash-based lookups: finding min, local max, first duplicate, and longest unique prefix. This problem introduces in-place array modification using the two-pointers-from-ends technique, a core mechanic for partitioning. It avoids duplication by not being a duplicate removal or zero-moving problem (both explicitly avoided), while reinforcing the canonical two-pointer swap pattern. The parity partition is a fundamental algorithmic building block distinct from the avoided list and serves as the logical first step into two-pointer in-place manipulation.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
