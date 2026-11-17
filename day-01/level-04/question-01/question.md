# Longest Subarray with Sum at Most K

- **Day:** `Day 01`
- **Level:** `Level 04`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of positive integers `nums` and an integer `k`, find the length of the longest contiguous subarray such that the sum of its elements is less than or equal to `k`. If no such subarray exists, return 0.

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 10^9

**Example 1:**
Input: nums = [1, 2, 3, 4, 5], k = 10
Output: 4
Explanation: The subarray [1,2,3,4] has sum 10 which is <= 10, length 4.

**Example 2:**
Input: nums = [5, 1, 3, 2, 4], k = 7
Output: 3
Explanation: The subarray [1,3,2] has sum 6 <= 7, length 3.

**Example 3:**
Input: nums = [10, 20, 30], k = 5
Output: 0
Explanation: No subarray has sum <= 5.

---

## 💻 Starter Function

```python
def longest_subarray_sum_at_most_k(nums: list[int], k: int) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problems established linear traversal, hash-based duplicate detection, and two-pointer partitioning. This problem introduces the core sliding window mechanic for subarray sums with positive integers. It requires a dynamic window that expands right and contracts left when the sum exceeds k, teaching the fundamental 'expand-shrink' pattern. It avoids duplication because no prior problem handled constrained subarray sums, and the forbidden list excludes this exact premise (e.g., 'minimum-size-subarray-sum' targets minimum length with sum >= target, while this seeks maximum length with sum <= target).
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
